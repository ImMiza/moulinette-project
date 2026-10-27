import media from '../data/generated/media.json';
import inventory from '../data/generated/inventory.json';

type M = { src: string; w?: number; h?: number };
const base = import.meta.env.BASE_URL.replace(/\/?$/, '/');

export const mediaUrl = (path: string) => {
  const m = (media as Record<string, M>)[path];
  return m ? base + m.src : null;
};
export const mediaInfo = (path: string) => (media as Record<string, M>)[path] ?? null;

export type Asset = {
  path: string; bytes: number; kind: string; status: string; usedIn: string[]; keys: string[];
  requires: string[]; requiresMode?: 'all' | 'any'; declaredBy: string[];
};
export const assets = inventory.assets as unknown as Record<string, Asset>;
export const assetList = Object.values(assets);
export const labels = inventory.labels as unknown as Record<string, { id: string; file: string; line: number; key: string | null; reachable: boolean }>;

export const fileName = (p: string) => p.split('/').pop()!.replace(/\.[^.]+$/, '');
