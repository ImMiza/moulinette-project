// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  // Chemins relatifs à la racine du domaine ; définir `site`/`base` pour publier dans un sous-dossier.
  site: process.env.WIKI_SITE,
  base: process.env.WIKI_BASE,
  integrations: [
    starlight({
      title: 'Wiki Moulinette',
      description: 'Wiki non officiel du visual novel Moulinette : personnages, arcs, routes, fins et ressources, avec protection des spoilers.',
      favicon: '/favicon.png',
      defaultLocale: 'root',
      locales: { root: { label: 'Français', lang: 'fr' } },
      customCss: ['./src/styles/custom.css'],
      // Empêche Pagefind de prendre la première image d'une page (souvent un décor protégé) comme aperçu.
      head: [{ tag: 'meta', attrs: { 'data-pagefind-meta': 'image:/favicon.png' } }],
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      sidebar: [
        { label: 'Guide', items: [{ autogenerate: { directory: 'guide' } }] },
        { label: 'Histoire', items: [{ autogenerate: { directory: 'histoire' } }] },
        { label: 'Fins', items: [{ autogenerate: { directory: 'fins' } }] },
        { label: 'Personnages', items: [{ autogenerate: { directory: 'personnages' } }] },
        { label: 'Monde', items: [{ autogenerate: { directory: 'monde' } }] },
        { label: 'Mécaniques', items: [{ autogenerate: { directory: 'mecaniques' } }] },
        { label: 'Médias', items: [{ autogenerate: { directory: 'medias' } }] },
        { label: 'Glossaire', link: '/glossaire/' },
      ],
    }),
  ],
});
