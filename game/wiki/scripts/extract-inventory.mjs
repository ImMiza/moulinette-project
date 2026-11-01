#!/usr/bin/env node
// Extrait un inventaire technique traçable depuis les scripts Ren'Py et les ressources du jeu.
// Ne lit que game/ (hors game/wiki) et n'écrit que src/data/generated/inventory.json.
// Les textes éditoriaux (src/content, src/data/*.json hors generated) ne sont jamais touchés.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const WIKI = path.resolve(here, '..');
const GAME = path.resolve(process.env.GAME_DIR ?? path.join(WIKI, '..'));
const OUT = path.join(WIKI, 'src/data/generated/inventory.json');
const progression = JSON.parse(fs.readFileSync(path.join(WIKI, 'src/data/progression.json'), 'utf8'));

const rel = (p) => path.relative(GAME, p).split(path.sep).join('/');
const SKIP_DIRS = new Set(['wiki', 'cache', 'saves', 'tmp', 'tl', '.agents', 'node_modules']);

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory()) {
      if (dir === GAME && SKIP_DIRS.has(e.name)) continue;
      walk(path.join(dir, e.name), out);
    } else out.push(path.join(dir, e.name));
  }
  return out;
}

const allFiles = walk(GAME);
const scripts = allFiles.filter((f) => f.endsWith('.rpy'));

// ---------- lexing helpers ----------
function stripComment(line) {
  let q = null;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (q) {
      if (c === '\\') i++;
      else if (c === q) q = null;
    } else if (c === '"' || c === "'") q = c;
    else if (c === '#') return line.slice(0, i);
  }
  return line;
}
const parenDepth = (s) => {
  let d = 0, q = null;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (q) { if (c === '\\') i++; else if (c === q) q = null; continue; }
    if (c === '"' || c === "'") q = c;
    else if ('([{'.includes(c)) d++;
    else if (')]}'.includes(c)) d--;
  }
  return d;
};
const firstString = (s) => {
  const m = s.match(/^\s*(?:_\()?\s*"((?:[^"\\]|\\.)*)"/) || s.match(/^\s*'((?:[^'\\]|\\.)*)'/);
  return m ? m[1] : null;
};
const ASSET_RE = /["']((?:images|audio|videos|gui)\/[^"']+\.(?:png|jpe?g|webp|svg|ogg|mp3|wav|opus|webm|mp4|json))["']/gi;

function fileKey(file) {
  for (const [prefix, key] of Object.entries(progression.fileKeys)) if (file.startsWith(prefix)) return key;
  return null;
}

// ---------- parse ----------
const inv = {
  generatedAt: new Date().toISOString(),
  files: [], labels: {}, edges: [], menus: [], characters: {}, variables: {},
  images: {}, imageUses: [], audio: {}, audioUses: [], assetRefs: [], assets: {},
  remembers: [], endings: [], centered: [], sceneMarkers: [], dynamicShows: [], warnings: [],
};

// pre-pass: characters may be used in a file loaded before the one defining them
for (const abs of scripts) {
  const src = fs.readFileSync(abs, 'utf8');
  for (const m of src.matchAll(/^define\s+([\w.]+)\s*=\s*Character\(([^\n]*(?:\n\s+[^\n]*){0,6})/gm)) {
    const expr = m[2];
    const nm = expr.match(/^\s*(?:_\()?\s*(None|"([^"]*)")/);
    const color = expr.match(/color\s*=\s*"(#[0-9a-fA-F]{3,8})"/);
    const tag = expr.match(/speaker_callback\(\s*"([^"]*)"/);
    const line = src.slice(0, m.index).split('\n').length;
    inv.characters[m[1]] ||= { var: m[1], name: nm?.[2] ?? null, color: color?.[1] ?? null, tag: tag?.[1] ?? null, file: rel(abs), line, lines: 0, firstLine: null, byLabel: {} };
  }
}

const pathHelpers = {}; // fonction python -> modèle de chemin "..._{}.jpg"
for (const abs of scripts) {
  const file = rel(abs);
  let m0, curDef = null;
  const raw = fs.readFileSync(abs, 'utf8').replace(/^\uFEFF/, '').split(/\r?\n/);
  inv.files.push({ file, lines: raw.length, key: fileKey(file), test: file.startsWith('tests/') });

  // raw comment pass: scene markers and commented asset refs
  raw.forEach((l, i) => {
    const t = l.trim();
    const sm = t.match(/^#\s*(SC[EÈ]NE|SCENE|Scène|Scene)\s*([0-9]+[a-z]?)?\s*[:\-–]?\s*(.*)$/i);
    if (sm) inv.sceneMarkers.push({ file, line: i + 1, num: sm[2] || null, title: sm[3].trim() });
    if (t.startsWith('#')) for (const m of t.matchAll(ASSET_RE)) inv.assetRefs.push({ path: m[1], file, line: i + 1, commented: true });
  });

  // logical lines (join unbalanced parens)
  const lines = [];
  for (let i = 0; i < raw.length; i++) {
    let text = stripComment(raw[i]);
    const start = i;
    while (parenDepth(text) > 0 && i + 1 < raw.length) text += ' ' + stripComment(raw[++i]).trim();
    if (!text.trim()) continue;
    lines.push({ n: start + 1, indent: text.match(/^\s*/)[0].replace(/\t/g, '    ').length, t: text.trim() });
  }

  let label = null;
  const stack = []; // {indent, kind, cond, menu}
  let python = null; // indent of python block
  let lastTopStmt = null;
  const labelOrder = [];

  const conds = () => stack.filter((s) => s.cond).map((s) => s.cond);
  const ctx = (n) => ({ file, line: n, label, conds: conds() });

  for (const L of lines) {
    while (stack.length && L.indent <= stack.at(-1).indent) stack.pop();
    if (python !== null && L.indent <= python) python = null;
    const t = L.t;

    // Helpers python qui construisent un chemin : def f(nom, ...): "..._{}.jpg".format(nom)
    if ((m0 = t.match(/^def\s+(\w+)\s*\(/))) curDef = m0[1];
    if (python !== null && curDef && (m0 = t.match(/"([^"]*\{\}[^"]*)"\.format\(/))) pathHelpers[curDef] ||= m0[1];

    for (const m of t.matchAll(ASSET_RE)) inv.assetRefs.push({ path: m[1], file, line: L.n, label, commented: false, text: t.slice(0, 300) });

    if (python !== null || t.startsWith('$')) {
      const body = t.startsWith('$') ? t.slice(1).trim() : t;
      const am = body.match(/^(?:store\.|s\.)?([A-Za-z_]\w*)\s*(\+=|-=|\*=|=)(?!=)\s*(.+)$/);
      if (am && label) {
        const v = (inv.variables[am[1]] ||= { name: am[1], writes: [], reads: [] });
        v.writes.push({ ...ctx(L.n), op: am[2], expr: am[3].slice(0, 160), menuOption: stack.findLast((s) => s.kind === 'option')?.cond ?? null });
      }
      const rm = body.match(/remember\(\s*["'](\w+)["']\s*\)/);
      if (rm) inv.remembers.push({ key: rm[1], ...ctx(L.n) });
      const em = body.match(/record_ending\(\s*["'](\w+)["']\s*\)/);
      if (em) inv.endings.push({ key: em[1], ...ctx(L.n) });
      if (t.startsWith('$')) { lastTopStmt = t; continue; }
      if (python !== null) continue;
    }

    let m;
    if ((m = t.match(/^(init(?:\s+-?\d+)?\s+)?python\b.*:$/))) { python = L.indent; continue; }
    if ((m = t.match(/^label\s+([\w.]+)\s*(\(.*\))?\s*:/)) && !t.includes('"') && file !== 'screens.rpy') {
      label = m[1];
      labelOrder.push(label);
      inv.labels[label] = { id: label, file, line: L.n, key: fileKey(file), says: {}, shows: [], music: [], menus: [], jumps: [], centered: [] };
      lastTopStmt = null;
      continue;
    }
    if ((m = t.match(/^default\s+([\w.]+)\s*=\s*(.+)$/))) {
      const v = (inv.variables[m[1]] ||= { name: m[1], writes: [], reads: [] });
      v.default = { file, line: L.n, value: m[2].slice(0, 200) };
      continue;
    }
    if ((m = t.match(/^define\s+([\w.]+)\s*=\s*(.+)$/))) {
      const [, name, expr] = m;
      if (name.startsWith('audio.') || name.startsWith('auddio.')) {
        const p = firstString(expr);
        inv.audio[name.replace(/^audd?io\./, '')] = { name, path: p, file, line: L.n, typo: name.startsWith('auddio.') };
      } else if (/Character\(/.test(expr)) {
        // déjà enregistré par la pré-passe
      } else {
        const v = (inv.variables[name] ||= { name, writes: [], reads: [] });
        v.define = { file, line: L.n, value: expr.slice(0, 200) };
      }
      continue;
    }
    if ((m = t.match(/^image\s+([^=:]+?)\s*(=\s*(.+)|:)$/))) {
      const name = m[1].trim().replace(/\s+/g, ' ');
      let paths = m[3] ? [...m[3].matchAll(ASSET_RE)].map((x) => x[1]) : [];
      const hm = m[3]?.match(/^(\w+)\(\s*["']([^"']+)["']/);
      if (hm && pathHelpers[hm[1]]) {
        // Le helper essaie d'abord le chemin construit ; le chemin littéral n'est qu'un secours.
        const built = pathHelpers[hm[1]].replace('{}', hm[2]);
        if (fs.existsSync(path.join(GAME, built))) paths = [built];
      }
      inv.images[name] = { name, paths, expr: (m[3] || 'ATL').slice(0, 220), file, line: L.n, uses: 0 };
      if (m[2] === ':') stack.push({ indent: L.indent, kind: 'image', imageName: name });
      continue;
    }
    // ATL image block content
    const imgBlock = stack.findLast((s) => s.kind === 'image');
    if (imgBlock) {
      for (const x of t.matchAll(ASSET_RE)) inv.images[imgBlock.imageName].paths.push(x[1]);
      continue;
    }
    if (!label) continue;
    const lab = inv.labels[label];

    if ((m = t.match(/^menu(\s+\w+)?\s*:$/))) {
      const menu = { id: `${file}:${L.n}`, file, line: L.n, label, conds: conds(), caption: null, options: [] };
      inv.menus.push(menu);
      lab.menus.push(menu.id);
      stack.push({ indent: L.indent, kind: 'menu', menu });
      lastTopStmt = t;
      continue;
    }
    const parentMenu = stack.at(-1)?.kind === 'menu' ? stack.at(-1).menu : null;
    if (parentMenu && t.startsWith('"')) {
      const text = firstString(t);
      if (t.endsWith(':')) {
        const cm = t.match(/"\s+if\s+(.+):$/);
        const opt = { text, cond: cm ? cm[1].trim() : null, line: L.n, sets: [], jumps: [], remembers: [] };
        parentMenu.options.push(opt);
        stack.push({ indent: L.indent, kind: 'option', cond: `choix « ${text} »`, opt });
      } else parentMenu.caption = text;
      continue;
    }
    if ((m = t.match(/^(if|elif|while)\s+(.+):$/))) {
      // pour un elif, on garde la trace des branches sœurs précédentes
      stack.push({ indent: L.indent, kind: m[1], cond: `${m[1] === 'elif' ? 'elif' : m[1]} ${m[2]}` });
      for (const v of m[2].matchAll(/\b([a-z_][a-z0-9_]*)\b/g)) inv.variables[v[1]]?.reads.push({ file, line: L.n, label, expr: m[2].slice(0, 200) });
      continue;
    }
    if (t === 'else:') { stack.push({ indent: L.indent, kind: 'else', cond: 'else' }); continue; }

    const opt = stack.findLast((s) => s.kind === 'option')?.opt;
    if ((m = t.match(/^(jump|call)\s+(expression\s+)?([\w.]+)/))) {
      const e = { from: label, to: m[2] ? null : m[3], expr: m[2] ? t : null, type: m[1], ...ctx(L.n) };
      inv.edges.push(e);
      lab.jumps.push({ to: e.to, type: e.type, line: L.n, conds: e.conds });
      if (opt) opt.jumps.push(e.to);
      if (L.indent <= (inv.labels[label] ? 4 : 0)) lastTopStmt = t;
      continue;
    }
    if (t === 'return') { lastTopStmt = t; continue; }
    if ((m = t.match(/^(scene|show)\s+(.+)$/))) {
      const rest = m[2];
      if (/^(screen|text)\b/.test(rest)) continue;
      if (/^expression\b/.test(rest)) { inv.dynamicShows.push({ expr: rest.slice(0, 160), ...ctx(L.n) }); continue; }
      const toks = [];
      for (const tok of rest.split(/\s+/)) {
        if (['at', 'with', 'as', 'behind', 'onlayer', 'zorder', ':'].includes(tok)) break;
        toks.push(tok.replace(/:$/, ''));
      }
      if (!toks.length) continue;
      const name = toks.join(' ');
      inv.imageUses.push({ name, kind: m[1], ...ctx(L.n) });
      lab.shows.push(name);
      continue;
    }
    if ((m = t.match(/^(play|queue)\s+(\w+)\s+(.+)$/))) {
      const expr = m[3];
      const refs = [];
      const s = firstString(expr);
      const call = expr.match(/^(\w+)\((.*)\)/);
      if (s) refs.push({ path: s });
      else if (call) {
        // helper(chemin, secours) : toutes les chaînes sont des candidats
        for (const q of call[2].matchAll(/["']([^"']+)["']/g)) refs.push({ path: q[1], via: call[1] });
        for (const n of call[2].matchAll(/audio\.(\w+)/g)) refs.push({ name: n[1], via: call[1] });
      } else {
        const list = expr.match(/^\[(.*?)\]/);
        const body = list ? list[1] : expr.split(/\s+/)[0];
        for (const tok of body.split(',')) {
          const tt = tok.trim();
          const q = firstString(tt);
          if (q) refs.push({ path: q });
          else if (tt) refs.push({ name: tt.replace(/^audio\./, '') });
        }
      }
      for (const r of refs) inv.audioUses.push({ ...r, channel: m[2], ...ctx(L.n) });
      if (m[2] === 'music') lab.music.push(refs.map((r) => r.name || r.path).join('+'));
      continue;
    }
    if ((m = t.match(/^centered\s+"(.*)"/))) { inv.centered.push({ text: m[1], ...ctx(L.n) }); lab.centered.push(m[1]); continue; }
    // say statements
    if ((m = t.match(/^([A-Za-z_]\w*)\s+(?:[\w\s]*?\s)?"((?:[^"\\]|\\.)*)"/)) && inv.characters[m[1]] !== undefined) {
      const c = inv.characters[m[1]];
      c.lines++;
      c.byLabel[label] = (c.byLabel[label] || 0) + 1;
      c.firstLine ||= { ...ctx(L.n), text: m[2].slice(0, 200) };
      lab.says[m[1]] = (lab.says[m[1]] || 0) + 1;
      continue;
    }
    if (t.startsWith('"')) { lab.says._narration = (lab.says._narration || 0) + 1; continue; }
  }

  // fallthrough between consecutive labels of the same file (Ren'Py continues into the next label)
  for (let k = 0; k < labelOrder.length - 1; k++) {
    const a = inv.labels[labelOrder[k]];
    const last = a.jumps.at(-1);
    const unconditional = a.jumps.some((j) => j.type === 'jump' && j.conds.length === 0);
    if (!unconditional && !(last && last.conds.length === 0)) {
      inv.edges.push({ from: a.id, to: labelOrder[k + 1], type: 'fallthrough', file, line: inv.labels[labelOrder[k + 1]].line, label: a.id, conds: [], uncertain: true });
    }
  }
}

// ---------- assets ----------
const assetFiles = allFiles.filter((f) => /^(images|audio|videos|gui)\//.test(rel(f)) && !/\.(rpyc?|md|txt|json)$/i.test(f));
for (const f of assetFiles) {
  const p = rel(f);
  inv.assets[p] = { path: p, bytes: fs.statSync(f).size, kind: p.split('/')[0], declaredBy: [], refs: [], usedIn: [] };
}
const norm = (p) => p.replace(/\\/g, '/');
const lowerMap = Object.fromEntries(Object.keys(inv.assets).map((p) => [p.toLowerCase(), p]));
// Résout un chemin comme Ren'Py : exact, puis préfixe audio/, puis casse différente (signalée).
function findAsset(p, ctx) {
  p = norm(p);
  for (const c of [p, `audio/${p}`]) {
    if (inv.assets[c]) return inv.assets[c];
    const lc = lowerMap[c.toLowerCase()];
    if (lc) { ctx && inv.warnings.push({ type: 'case-mismatch', path: p, actual: lc, file: ctx.file, line: ctx.line }); return inv.assets[lc]; }
  }
  return null;
}
// Chemins construits à l'exécution ("..._{}.jpg".format(x), "[prefix_]") : correspondance par motif.
const patternOf = (p) => /\{\}|\[\w+\]|%s/.test(p) ? new RegExp('^' + norm(p).replace(/[.+^$()|\\]/g, '\\$&').replace(/\{\}|\[\w+\]|%s/g, '[^/]*') + '$', 'i') : null;
for (const r of inv.assetRefs) {
  const re = patternOf(r.path);
  if (re) {
    const hits = Object.values(inv.assets).filter((a) => re.test(a.path));
    for (const a of hits) { a.refs.push({ file: r.file, line: r.line, commented: r.commented, pattern: r.path }); if (r.label && !r.commented) a.usedIn.includes(r.label) || a.usedIn.push(r.label); }
    if (!hits.length && !r.commented) inv.warnings.push({ type: 'missing-asset', path: r.path, file: r.file, line: r.line, pattern: true });
    r.pattern = true;
    continue;
  }
  const a = findAsset(r.path, r.commented ? null : r);
  if (a) a.refs.push({ file: r.file, line: r.line, commented: r.commented });
  else if (!r.commented) {
    const fb = r.text && new RegExp(`\\w+\\(\\s*["']${r.path.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']\\s*,`).test(r.text);
    inv.warnings.push({ type: fb ? 'missing-asset-fallback' : 'missing-asset', path: r.path, file: r.file, line: r.line });
  }
}
for (const img of Object.values(inv.images)) for (const p of img.paths) inv.assets[p]?.declaredBy.push(img.name);

// image uses -> resolve to declarations (exact, else longest declared prefix)
const imgNames = Object.keys(inv.images);
for (const u of inv.imageUses) {
  let decl = inv.images[u.name] ? u.name : null;
  if (!decl) {
    const cand = imgNames.filter((n) => u.name.startsWith(n + ' ') || n.startsWith(u.name + ' ')).sort((a, b) => b.length - a.length);
    if (cand.length === 1) decl = cand[0];
  }
  u.resolved = decl;
  if (!decl) {
    if (!['black', 'white'].includes(u.name) && !u.name.startsWith('expression')) inv.warnings.push({ type: 'unresolved-image', name: u.name, file: u.file, line: u.line });
    continue;
  }
  const img = inv.images[decl];
  img.uses++;
  for (const p of img.paths) {
    const a = inv.assets[p];
    if (a && !a.usedIn.includes(u.label)) a.usedIn.push(u.label);
  }
}
// dynamic shows: `show expression VAR + " suffixe"` -> candidats depuis les valeurs connues de VAR
for (const d of inv.dynamicShows) {
  d.note = 'Image calculée à l’exécution : résolution statique partielle.';
  const m = d.expr.match(/^expression\s+(\w+)\s*\+\s*"([^"]*)"/);
  if (!m) continue;
  const v = inv.variables[m[1]];
  const vals = new Set([v?.default?.value, v?.define?.value, ...(v?.writes || []).map((w) => w.expr)].filter(Boolean).flatMap((e) => [...e.matchAll(/"([^"]+)"/g)].map((x) => x[1])));
  d.candidates = [...vals].map((x) => x + m[2]).filter((n) => inv.images[n]);
  for (const n of d.candidates) {
    inv.images[n].uses++;
    for (const p of inv.images[n].paths) { const a = inv.assets[p]; if (a && !a.usedIn.includes(d.label)) a.usedIn.push(d.label); }
  }
}

// Noms audio non définis : Ren'Py peut les déduire des fichiers de game/audio (résolution signalée comme probable).
const autoAudio = {};
for (const p of Object.keys(inv.assets)) if (p.startsWith('audio/')) autoAudio[path.basename(p, path.extname(p)).toLowerCase()] ||= p;
for (const u of inv.audioUses) {
  let p = u.path ? norm(u.path).replace(/^<[^>]*>/, '') : inv.audio[u.name]?.path;
  if (!p && u.name && autoAudio[u.name.toLowerCase()]) { p = autoAudio[u.name.toLowerCase()]; u.auto = true; inv.warnings.push({ type: 'audio-auto-name', name: u.name, path: p, file: u.file, line: u.line }); }
  u.resolved = p || null;
  if (!p) { inv.warnings.push({ type: 'unresolved-audio', name: u.name, file: u.file, line: u.line }); continue; }
  const a = findAsset(p, u);
  if (!a) { if (!u.via) inv.warnings.push({ type: 'missing-audio-file', path: p, file: u.file, line: u.line }); continue; }
  if (!a.usedIn.includes(u.label)) a.usedIn.push(u.label);
}
// direct string refs inside a label (Movie(), add "...", etc.)
for (const r of inv.assetRefs) if (!r.commented && r.label && !r.pattern) { const a = findAsset(r.path); if (a && !a.usedIn.includes(r.label)) a.usedIn.push(r.label); }
// main menu / gui config
for (const r of inv.assetRefs) if (!r.commented && !r.pattern && /^(options|gui|screens|script)\.rpy$/.test(r.file) && !r.label) { const a = findAsset(r.path); if (a && /^(gui|videos|audio)\//.test(a.path) && !a.usedIn.includes('@interface')) a.usedIn.push('@interface'); }
for (const p of ['gui/main_menu.png', 'gui/game_menu.png', 'audio/music/main_music.ogg']) inv.assets[p] && !inv.assets[p].usedIn.includes('@interface') && inv.assets[p].usedIn.push('@interface');

// status + spoiler requirement
const trunk = progression.trunk.map((t) => t.key);
for (const a of Object.values(inv.assets)) {
  const keys = [...new Set(a.usedIn.map((l) => (l === '@interface' ? 'public' : inv.labels[l]?.key)).filter(Boolean))];
  a.keys = keys;
  if (a.usedIn.length) a.status = 'utilisé';
  else if (a.kind === 'gui') a.status = 'interface (implicite)';
  else if (a.declaredBy.length || a.refs.some((r) => !r.commented)) a.status = 'déclaré, non affiché';
  else if (a.refs.length) a.status = 'référencé en commentaire';
  else a.status = 'non référencé';
  if (keys.includes('public') || a.kind === 'gui') a.requires = [];
  else {
    const t = keys.filter((k) => trunk.includes(k)).sort((x, y) => trunk.indexOf(x) - trunk.indexOf(y));
    a.requires = t.length ? [t[0]] : keys.length ? keys : ['extras'];
    a.requiresMode = t.length ? 'all' : 'any';
  }
}

// characters: count first-line per key order
for (const c of Object.values(inv.characters)) c.keys = [...new Set(Object.keys(c.byLabel).map((l) => inv.labels[l]?.key).filter(Boolean))];

// reachability from start
const adj = {};
for (const e of inv.edges) if (e.to) (adj[e.from] ||= []).push(e.to);
const seen = new Set(['start', 'splashscreen', 'after_load']);
const q = ['start'];
while (q.length) for (const n of adj[q.shift()] || []) if (!seen.has(n)) { seen.add(n); q.push(n); }
for (const l of Object.values(inv.labels)) l.reachable = seen.has(l.id);
for (const l of Object.values(inv.labels)) if (!l.reachable && !l.file.startsWith('tests/')) inv.warnings.push({ type: 'unreachable-label', label: l.id, file: l.file, line: l.line });

// summary
const st = {};
for (const a of Object.values(inv.assets)) st[`${a.kind}:${a.status}`] = (st[`${a.kind}:${a.status}`] || 0) + 1;
inv.summary = {
  scripts: inv.files.length, labels: Object.keys(inv.labels).length, menus: inv.menus.length,
  options: inv.menus.reduce((n, m) => n + m.options.length, 0), characters: Object.keys(inv.characters).length,
  imagesDeclared: Object.keys(inv.images).length, audioDeclared: Object.keys(inv.audio).length,
  assets: Object.keys(inv.assets).length, assetStatus: st, warnings: inv.warnings.length,
};
delete inv.assetRefs;
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(inv, null, 1));
console.log(JSON.stringify(inv.summary, null, 2));
