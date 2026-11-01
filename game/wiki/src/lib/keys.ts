import progression from '../data/progression.json';

const labels: Record<string, string> = Object.fromEntries(
  [...progression.trunk, ...progression.branches].map((k) => [k.key, k.label]),
);
labels.public = 'aucun prérequis';

export const keyLabel = (k: string) => labels[k] ?? k;
export const trunkKeys = progression.trunk.map((t) => t.key);

export function requirementText(requires: string[], mode: 'all' | 'any' = 'all') {
  const names = requires.map(keyLabel);
  if (names.length <= 1) return names[0] ?? '';
  return names.slice(0, -1).join(', ') + (mode === 'any' ? ' ou ' : ' et ') + names.at(-1);
}

export const toArray = (v?: string | string[]) => (v ? (Array.isArray(v) ? v : v.split(/[ ,]+/).filter(Boolean)) : []);
