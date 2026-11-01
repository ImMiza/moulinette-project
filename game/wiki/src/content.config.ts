import { defineCollection } from 'astro:content';
import { file, glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// Clés de progression valides (voir src/data/progression.json).
const key = z.enum(['public', 'prologue', 'arc1', 'arc2', 'arc3', 'arc4', 'arc5', 'arc6', 'routeA', 'routeB', 'finA1', 'finA2', 'finA3', 'finB1', 'finB2', 'extras']);
const src = z.object({ file: z.string(), line: z.number().int().optional(), label: z.string().optional() });

const characters = defineCollection({
  loader: file('src/data/characters.json'),
  schema: z.object({
    name: z.string(),
    color: z.string().optional(),
    // Clé à partir de laquelle le personnage peut être nommé sans spoiler.
    unlock: key,
    role: z.string(),
    firstAppearance: key,
    page: z.string().optional(),
    portrait: z.string().optional(),
    spriteDirs: z.array(z.string()).default([]),
    infobox: z.array(z.object({ label: z.string(), value: z.string(), requires: key.default('public') })).default([]),
    aliases: z.array(z.object({ name: z.string(), requires: key, note: z.string().optional() })).default([]),
    source: src.optional(),
  }),
});

const choice = z.object({
  line: z.number().int(),
  prompt: z.string().optional(),
  condition: z.string().optional(),
  options: z.array(z.object({ text: z.string(), effects: z.string().optional(), condition: z.string().optional() })),
});

const scenes = defineCollection({
  loader: glob({ pattern: '*.json', base: 'src/data/scenes', generateId: ({ entry }) => entry.replace(/\.json$/, '') }),
  schema: z.object({
    arc: key,
    title: z.string(),
    file: z.string(),
    scenes: z.array(z.object({
      id: z.string(),
      title: z.string(),
      label: z.string().optional(),
      lines: z.string(),
      requires: key.optional(),
      condition: z.string().optional(),
      location: z.string().optional(),
      characters: z.array(z.string()).default([]),
      summary: z.string(),
      choices: z.array(choice).default([]),
      consequences: z.array(z.string()).default([]),
      backgrounds: z.array(z.string()).default([]),
      cgs: z.array(z.string()).default([]),
      music: z.array(z.string()).default([]),
    })),
  }),
});

const endings = defineCollection({
  loader: file('src/data/endings.json'),
  schema: z.object({
    publicTitle: z.string(),
    title: z.string(),
    key,
    route: key,
    category: z.string().optional(),
    label: z.string(),
    record: z.string().optional(),
    conditionCode: z.string(),
    conditions: z.array(z.string()),
    summary: z.string(),
    cgs: z.array(z.string()).default([]),
    source: src,
  }),
});

const routes = defineCollection({
  loader: file('src/data/routes.json'),
  schema: z.object({
    publicTitle: z.string(),
    title: z.string(),
    key,
    label: z.string(),
    entryCode: z.string(),
    entry: z.array(z.string()),
    endings: z.array(z.string()),
    source: src,
  }),
});

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
  characters,
  scenes,
  endings,
  routes,
};
