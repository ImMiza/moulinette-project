#!/usr/bin/env node
// Contrôle de couverture et de fuites de spoilers. À lancer après `astro build`.
// Écrit maintenance/couverture.md et sort en erreur si un lien est cassé ou si un spoiler fuit.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { fileURLToPath } from 'node:url';

const WIKI = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const rd = (p) => fs.readFileSync(path.join(WIKI, p), 'utf8');
const json = (p) => JSON.parse(rd(p));
const walk = (d, ext) => fs.existsSync(d) ? fs.readdirSync(d, { withFileTypes: true }).flatMap((e) => e.isDirectory() ? walk(path.join(d, e.name), ext) : e.name.endsWith(ext) ? [path.join(d, e.name)] : []) : [];

const inv = json('src/data/generated/inventory.json');
const prog = json('src/data/progression.json');
const chars = json('src/data/characters.json');
const endings = json('src/data/endings.json');
const routes = json('src/data/routes.json');
const sceneFiles = fs.readdirSync(path.join(WIKI, 'src/data/scenes')).filter((f) => f.endsWith('.json'));
const scenes = Object.fromEntries(sceneFiles.map((f) => [f.replace(/\.json$/, ''), json('src/data/scenes/' + f)]));
const docs = walk(path.join(WIKI, 'src/content/docs'), '.mdx').concat(walk(path.join(WIKI, 'src/content/docs'), '.md'));
const docText = docs.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
const dataText = JSON.stringify({ scenes, endings, routes });

const errors = [], rows = [], todo = [];
const pct = (a, b) => `${a}/${b}${b ? ` (${Math.round((100 * a) / b)} %)` : ''}`;

// 1. Chapitres : chaque clé de progression a ses scènes et sa page.
const pageOf = { prologue: 'histoire/prologue', arc1: 'histoire/arc-1', arc2: 'histoire/arc-2', arc3: 'histoire/arc-3', arc4: 'histoire/arc-4', arc5: 'histoire/arc-5', arc6: 'histoire/arc-6', routeA: 'histoire/route-a', routeB: 'histoire/route-b', finA1: 'fins/a1', finA2: 'fins/a2', finA3: 'fins/a3', finB1: 'fins/b1', finB2: 'fins/b2' };
const keys = Object.keys(pageOf);
const keyOk = keys.filter((k) => scenes[k] && fs.existsSync(path.join(WIKI, 'src/content/docs', pageOf[k] + '.mdx')));
keys.filter((k) => !keyOk.includes(k)).forEach((k) => errors.push(`Chapitre sans page ou sans scènes : ${k}`));
rows.push(['Chapitres (prologue, arcs, routes, fins)', pct(keyOk.length, keys.length)]);
rows.push(['Scènes décrites', String(Object.values(scenes).reduce((n, s) => n + s.scenes.length, 0))]);

// 2. Labels atteignables couverts par une scène, une route ou une fin.
const labels = Object.values(inv.labels).filter((l) => l.reachable && l.key && l.key !== 'public');
const missLabels = labels.filter((l) => !dataText.includes(l.id));
rows.push(['Labels jouables rattachés à une scène', pct(labels.length - missLabels.length, labels.length)]);
missLabels.forEach((l) => todo.push(`Label non rattaché : \`${l.id}\` (${l.file}:${l.line})`));

// 3. Menus : chaque menu a son choix documenté (ligne ±3 dans un fichier du même dossier).
const choices = Object.values(scenes).flatMap((e) => e.scenes.flatMap((s) => (s.choices || []).map((c) => ({ dir: path.posix.dirname(e.file), line: c.line }))));
const menus = inv.menus.filter((m) => inv.labels[m.label]?.reachable !== false && !m.file.startsWith('tests/'));
const missMenus = menus.filter((m) => !choices.some((c) => m.file.startsWith(c.dir) && Math.abs(c.line - m.line) <= 3));
rows.push(['Menus de choix documentés', pct(menus.length - missMenus.length, menus.length)]);
missMenus.forEach((m) => todo.push(`Menu non documenté : ${m.file}:${m.line} « ${m.caption ?? ''} »`));

// 4. Fins et routes.
const recorded = [...new Set((inv.endings || []).map((e) => e.key ?? e.id ?? e))];
rows.push(['Fins documentées', `${endings.length} (record_ending dans le jeu : ${recorded.length})`]);
rows.push(['Routes documentées', String(routes.length)]);

// 5. Personnages parlants.
const speaking = Object.values(inv.characters).filter((c) => c.lines > 0);
const known = new Set(chars.map((c) => c.name));
const missChars = speaking.filter((c) => !known.has(c.name) && !docText.includes(c.name));
rows.push(['Personnages parlants présents dans le wiki', pct(speaking.length - missChars.length, speaking.length)]);
missChars.forEach((c) => errors.push(`Personnage absent : ${c.name} (${c.file}:${c.line})`));
for (const c of chars.filter((c) => c.page)) if (!fs.existsSync(path.join(WIKI, 'src/content/docs', c.page.replace(/\/$/, '') + '.mdx'))) errors.push(`Fiche manquante : ${c.page}`);

// 6. Ressources : chaque fichier est montré dans une galerie ou classé.
const shown = { images: ['images/scenes/backgrounds/', 'images/scenes/cg/', 'images/scenes/illonanium/', 'images/promo/', 'images/personnages/'], audio: ['audio/music/', 'audio/ambience/', 'audio/fx/'] };
const assets = Object.values(inv.assets);
const media = json('src/data/generated/media.json');
const inGallery = (a) => (shown[a.kind] || []).some((p) => a.path.startsWith(p)) && media[a.path];
const byStatus = {};
for (const a of assets) byStatus[a.status] = (byStatus[a.status] || 0) + 1;
const gal = assets.filter(inGallery);
const other = assets.filter((a) => !inGallery(a) && a.kind !== 'gui');
rows.push(['Images et sons visibles dans les galeries', pct(gal.length, assets.filter((a) => a.kind !== 'gui').length)]);
rows.push(['Ressources du jeu par statut', Object.entries(byStatus).map(([k, v]) => `${k} : ${v}`).join(' ; ')]);
other.forEach((a) => todo.push(`Ressource hors galerie : \`${a.path}\` (${a.status})`));

// 7. Site construit : liens internes, images, fuites de spoilers.
const DIST = path.join(WIKI, 'dist');
const pages = walk(DIST, '.html');
const strip = (h) => { let p; do { p = h; h = h.replace(/<template>(?:(?!<template>)[\s\S])*?<\/template>/g, ''); } while (h !== p); return h; };
const visible = (html) => strip(html).replace(/<script[\s\S]*?<\/script>/g, '').replace(/<style[\s\S]*?<\/style>/g, '');
// Termes qui ne doivent jamais apparaître hors d'un bloc protégé (noms tardifs, titres de fins, fichiers révélateurs).
const LEAKS = ['Micka', 'Lucy', 'Florentin', 'Oliver', 'Ilonanium', 'Illonanium', 'Tokyo', 'Le dernier été', 'Petits Sommets', 'berceau de l', 'cage dorée', 'bad_ending', 'ending_', 'arc_7_', 'venu du futur'];
const leaks = [];
let links = 0;
for (const f of pages) {
  const rel = path.relative(DIST, f).replaceAll('\\', '/');
  const raw = fs.readFileSync(f, 'utf8').replace(/<script[\s\S]*?<\/script>/g, '');
  const html = visible(raw);
  for (const t of LEAKS) {
    const i = html.toLowerCase().indexOf(t.toLowerCase());
    if (i >= 0) leaks.push(`${rel} : « ${t} » … ${html.slice(Math.max(0, i - 60), i + 40).replace(/\s+/g, ' ')}`);
  }
  for (const [, u] of raw.matchAll(/(?:href|src)="([^"#?]+)[^"]*"/g)) {
    if (/^(https?:|mailto:|data:|\/\/)/.test(u)) continue;
    links++;
    const target = decodeURI(u.startsWith('/') ? path.join(DIST, u) : path.join(path.dirname(f), u));
    if (!fs.existsSync(target) && !fs.existsSync(path.join(target, 'index.html'))) errors.push(`Lien cassé dans ${rel} : ${u}`);
  }
}
// Index de recherche : les fragments Pagefind ne doivent rien contenir de protégé.
for (const f of walk(path.join(DIST, 'pagefind/fragment'), '.pf_fragment')) {
  const txt = zlib.gunzipSync(fs.readFileSync(f)).toString('utf8');
  for (const t of LEAKS) if (txt.toLowerCase().includes(t.toLowerCase())) leaks.push(`index de recherche (${JSON.parse(txt.replace(/^pagefind_dcd/, '')).url}) : « ${t} »`);
}
rows.push(['Pages générées', String(pages.length)]);
rows.push(['Liens et images internes vérifiés', `${links} (${errors.filter((e) => e.startsWith('Lien')).length} cassé(s))`]);
rows.push(['Fuites de spoilers détectées', String(leaks.length)]);
errors.push(...leaks.map((l) => `Fuite : ${l}`));

const out = [
  '# Rapport de couverture',
  '',
  `Généré par \`npm run coverage\` le ${new Date().toISOString().slice(0, 16).replace('T', ' ')} à partir de l'inventaire du ${inv.generatedAt?.slice(0, 10) ?? '?'} et du site construit.`,
  '',
  '| Contrôle | Résultat |', '| --- | --- |', ...rows.map(([a, b]) => `| ${a} | ${b} |`),
  '', `## Erreurs (${errors.length})`, '', ...(errors.length ? errors.map((e) => `- ${e}`) : ['Aucune.']),
  '', `## À vérifier (${todo.length})`, '', ...(todo.length ? todo.map((e) => `- ${e}`) : ['Rien.']),
  '', `## Avertissements de l'inventaire (${inv.warnings.length})`, '', ...inv.warnings.map((w) => `- ${w.type} : \`${w.path ?? w.name ?? ''}\`${w.actual ? ` (réel : \`${w.actual}\`)` : ''} — ${w.file ?? ''}${w.line ? ':' + w.line : ''}`),
  '',
].join('\n');
fs.writeFileSync(path.join(WIKI, 'maintenance/couverture.md'), out);
console.log(rows.map(([a, b]) => `${a} : ${b}`).join('\n'));
console.log(`${errors.length} erreur(s), ${todo.length} point(s) à vérifier → maintenance/couverture.md`);
if (errors.length) { console.log(errors.slice(0, 30).join('\n')); process.exit(1); }
