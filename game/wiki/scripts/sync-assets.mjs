#!/usr/bin/env node
// Copie optimisée des ressources du jeu vers public/media (originaux jamais modifiés).
// Images -> WebP redimensionnées (transparence conservée). Audio -> copie telle quelle.
// Incrémental : un fichier n'est régénéré que si l'original est plus récent.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const here = path.dirname(fileURLToPath(import.meta.url));
const WIKI = path.resolve(here, '..');
const GAME = path.resolve(process.env.GAME_DIR ?? path.join(WIKI, '..'));
const OUT = path.join(WIKI, 'public/media');
const inv = JSON.parse(fs.readFileSync(path.join(WIKI, 'src/data/generated/inventory.json'), 'utf8'));

const manifest = {};
const stale = (src, dst) => !fs.existsSync(dst) || fs.statSync(dst).mtimeMs < fs.statSync(src).mtimeMs;
let done = 0, skipped = 0, failed = [];

// ponytail: dossiers de travail (pistes non intégrées, droits non vérifiés) jamais publiés.
const jobs = Object.values(inv.assets).filter((a) => !a.path.includes('/to_work/') && (a.kind === 'images' || a.kind === 'audio' || ['gui/main_menu.png', 'gui/window_icon.png'].includes(a.path)));
for (const a of jobs) {
  const src = path.join(GAME, a.path);
  if (/\.(png|jpe?g|webp)$/i.test(a.path)) {
    const rel = a.path.replace(/\.[^.]+$/, '.webp');
    const dst = path.join(OUT, rel);
    const sprite = a.path.startsWith('images/personnages/');
    try {
      if (stale(src, dst)) {
        fs.mkdirSync(path.dirname(dst), { recursive: true });
        await sharp(src).resize(sprite ? { height: 900, withoutEnlargement: true } : { width: 1280, withoutEnlargement: true }).webp({ quality: 80, alphaQuality: 90 }).toFile(dst);
        done++;
      } else skipped++;
      const m = await sharp(dst).metadata();
      manifest[a.path] = { src: `media/${rel}`, w: m.width, h: m.height };
    } catch (e) { failed.push(`${a.path}: ${e.message}`); }
  } else if (/\.(ogg|mp3|wav|opus)$/i.test(a.path)) {
    const dst = path.join(OUT, a.path);
    if (stale(src, dst)) { fs.mkdirSync(path.dirname(dst), { recursive: true }); fs.copyFileSync(src, dst); done++; } else skipped++;
    manifest[a.path] = { src: `media/${a.path}` };
  }
}
fs.writeFileSync(path.join(WIKI, 'src/data/generated/media.json'), JSON.stringify(manifest, null, 1));
fs.copyFileSync(path.join(GAME, 'gui/window_icon.png'), path.join(WIKI, 'public/favicon.png'));
console.log(`media: ${done} générés, ${skipped} à jour, ${failed.length} échecs`);
if (failed.length) console.log(failed.join('\n'));
