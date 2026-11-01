# Wiki Moulinette

Wiki statique du visual novel Ren'Py *moulinette*, construit avec [Astro](https://astro.build) 6 et [Starlight](https://starlight.astro.build) 0.40.
Il protège les spoilers selon la progression du lecteur (enregistrée dans le navigateur, sans compte).

## Prérequis

- Node.js 22 (testé avec 22.20) et npm.
- Le dossier du jeu (`game/`) est par défaut le parent de ce dossier ; sinon définir `GAME_DIR` (chemin de `game/`) avant `npm run refresh`.

## Commandes

À lancer depuis `game/wiki/` :

| Commande | Rôle |
| --- | --- |
| `npm install` | Installe les dépendances. |
| `npm run refresh` | Relit les scripts du jeu (`inventory`) puis regénère les médias optimisés (`assets`). |
| `npm run dev` | Serveur de développement : http://localhost:4321 |
| `npm run check` | Vérification TypeScript / Astro. |
| `npm run build` | Construit le site dans `dist/` (+ index de recherche Pagefind), puis lance le contrôle de couverture. |
| `npm run coverage` | Relance seul le contrôle de couverture sur `dist/` et réécrit `maintenance/couverture.md`. |
| `npm run preview` | Sert `dist/` en local pour vérifier le build. |

Premier lancement : `npm install`, `npm run refresh`, `npm run dev`.

## Publier

`dist/` est un site statique : n'importe quel hébergeur de fichiers convient (GitHub Pages, Netlify, serveur web).
Pour publier dans un sous-dossier, définir les variables avant le build :

```powershell
$env:WIKI_SITE = "https://exemple.org"; $env:WIKI_BASE = "/wiki"; npm run build
```

Le build échoue (code 1) si le contrôle de couverture trouve un lien cassé, une fuite de spoiler ou un élément du jeu non documenté. Lire alors `maintenance/couverture.md`.

## Actualiser après une modification du jeu

1. `npm run refresh` : met à jour `src/data/generated/inventory.json` (labels, menus, choix, variables, persos, ressources, avertissements) et `public/media/` (WebP et audio copiés ; seuls les fichiers modifiés sont retraités).
2. `npm run build` : la couverture signale ce qui manque (nouveau label, menu non documenté, nouvelle ressource, personnage parlant sans fiche…).
3. Compléter à la main les fichiers éditoriaux indiqués ci-dessous.

Les scripts n'écrivent que dans `src/data/generated/`, `public/media/`, `public/favicon.png` et `maintenance/couverture.md` : le contenu rédigé n'est jamais écrasé.

## Organisation

```
scripts/
  extract-inventory.mjs   analyse des .rpy et des ressources → src/data/generated/inventory.json
  sync-assets.mjs         images → WebP optimisés, audio copié → public/media/ (originaux intacts)
  coverage.mjs            contrôle inventaire ↔ wiki ↔ site construit
src/
  content/docs/           pages (Markdown / MDX)
  data/
    progression.json      clés de spoiler (tronc, routes, fins) et correspondance fichier .rpy → clé
    characters.json       personnages (infobox, alias protégés)
    routes.json           routes (conditions d'entrée)
    endings.json          fins (conditions exactes, sources)
    scenes/<clé>.json     scènes de chaque chapitre (lieu, persos, choix, conséquences)
    generated/            produit par les scripts, ne pas éditer
  components/             Spoiler, Media, Gallery, AudioList, SceneList, CharacterInfobox, ProgressPanel…
  scripts/progress.ts     progression du lecteur (localStorage)
  styles/custom.css
maintenance/
  guide-redaction.md      règles d'écriture et de protection des spoilers
  modele-page-*.mdx       modèles de pages
  notes/                  notes d'analyse par chapitre (avec fichier:ligne)
  characters/             notes sources des fiches personnages
  rapport.md              incertitudes, contradictions, bugs probables, ressources inutilisées
  couverture.md           généré par le build
```

## Spoilers

- Progression : un tronc (prologue → arc VI) puis deux routes et cinq fins débloquables indépendamment (page *Guide › Ma progression*, bouton « Tout autoriser »).
- `<Spoiler requires="arc3">…</Spoiler>` (ou `requires={["finA1","finA2"]} mode="any"`) : le contenu est placé dans un `<template>` (ni affiché, ni lu par les lecteurs d'écran, ni chargé), exclu de la recherche (`data-pagefind-ignore`), et révélé au clic ou automatiquement si la progression le permet.
- Ne jamais mettre de titre `##` dans un Spoiler (il apparaîtrait dans la table des matières). Titres, descriptions, légendes et alt publics restent neutres (« Route A », « Fin B2 »…).
- Les médias reçoivent automatiquement le prérequis du premier chapitre où ils apparaissent (inventaire).
- `coverage.mjs` recherche des mots révélateurs dans le HTML visible et dans l'index Pagefind ; compléter sa liste `LEAKS` si de nouveaux noms sensibles apparaissent.

## Intégration au jeu

Seule modification du jeu : `game/options.rpy` exclut `game/wiki/**` des builds Ren'Py (`build.classify('game/wiki/**', None)`), pour ne pas distribuer le wiki ni `node_modules`.
Ren'Py scanne quand même `game/` au lancement en développement : si cela ralentit le démarrage, déplacer le dossier hors de `game/` et définir `GAME_DIR`.
