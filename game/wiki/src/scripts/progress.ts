// Progression du lecteur, stockée localement (aucun envoi réseau).
import progression from '../data/progression.json';

export const STORAGE_KEY = 'moulinette-wiki:progress';
const trunk = progression.trunk.map((t) => t.key);
const parents: Record<string, string | null> = Object.fromEntries(progression.branches.map((b) => [b.key, b.parent]));

export type State = { keys: string[]; all: boolean };

export function load(): State {
  try {
    const s = JSON.parse(localStorage.getItem(STORAGE_KEY) || '');
    if (Array.isArray(s.keys)) return { keys: s.keys, all: !!s.all };
  } catch {}
  return { keys: [], all: false };
}

export function save(s: State) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(s));
  document.dispatchEvent(new CustomEvent('wiki:progress', { detail: s }));
}

// Une route implique tout le tronc ; une fin implique sa route ; un arc implique les arcs précédents.
export function expand(keys: string[]): Set<string> {
  const out = new Set<string>(['public']);
  for (let k of keys) {
    while (k) {
      out.add(k);
      const i = trunk.indexOf(k);
      if (i >= 0) { trunk.slice(0, i).forEach((t) => out.add(t)); break; }
      k = parents[k] as string;
    }
  }
  return out;
}

export function unlocked(requires: string[], mode: 'all' | 'any', s = load()): boolean {
  if (s.all) return true;
  if (!requires.length) return true;
  const have = expand(s.keys);
  return mode === 'any' ? requires.some((r) => have.has(r)) : requires.every((r) => have.has(r));
}
