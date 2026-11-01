# Consigne fiches personnages

Lis : `maintenance/guide-redaction.md`, `maintenance/modele-page-personnage.mdx`, `src/data/characters.json`, puis TOUTES les notes `maintenance/notes/*.md` (prologue, arc1..arc6, routeA, routeB, finA1..A3, finB1, finB2) et les `src/data/scenes/*.json`. Vérifie et complète dans les scripts `game/**/*.rpy` (grep du tag du personnage : `j`, `i`, `t`, `a`, `x`, `s`, `laplage`, `mi`, `tchat`, `family_lucy`, `ilonanium_florentin`, `m_inconnu`, `pmj`/`pmi`/`pmx`…) pour les citations exactes et faits. Docs `game/agents/cartographies/fiches_personnages.md` = contexte seulement (contradictions → notes).

Pour chaque personnage, écrire :

1. `src/content/docs/personnages/<id>.mdx` selon le modèle (onglets **Présentation / Relations / Histoire / Galerie**). Contenu riche et fidèle :
   - **Présentation** : description, caractéristiques (âge/classe/études/métier/loisirs/pseudo… seulement si confirmés), apparence et tenues (avec l'arc d'apparition), personnalité, citations (3 à 8, exactes, avec contexte arc/scène), chacune protégée par la clé de l'arc où elle est dite.
   - **Relations** : une section `##` par personnage lié (titre = nom public du personnage ; pour Micka/Lucy/Florentin/Tchat titre neutre « Autres liens » et noms dans Spoiler), évolution découpée en Spoilers par arc/route/fin.
   - **Histoire** : `## Prologue`, `## Arc I` … `## Arc VI`, `## Route A`, `## Route B`, `## Fins` — seulement les sections où le personnage agit ; contenu dans un Spoiler de la clé correspondante ; actions, choix qui le concernent (option exacte → effet), variables liées (`influence_theo`…), variantes selon l'état de la relation.
   - **Galerie** : `<Gallery prefix="images/personnages/<Dossier>/" sprite />` (+ CG pertinentes : `<Gallery prefix={["images/scenes/cg/..."]} />` si le personnage y figure).
   - Tout ce qui dépasse la première apparition est dans un Spoiler précis. Aucun `##`/`###` dans un Spoiler (utiliser **gras**). Titres `##` toujours neutres. Liens : `../<id>/` entre fiches, `../../histoire/arc-3/#arc3-s4` vers scènes, `../../fins/a1/`.
   - Les routes A/B et fins ne sont jamais décrites hors Spoiler.
2. `maintenance/characters/<id>.json` : `{ "id": "...", "firstAppearance": "<clé vérifiée>", "role": "<rôle public neutre court>", "infobox": [{"label":"…","value":"…","requires":"<clé>"}], "aliases": [{"name":"…","requires":"<clé>","note":"…"}], "sources": ["fichier:ligne", …] }` — infobox = caractéristiques confirmées (ex. Pseudo, Classe, Âge, Passion, Couleur de dialogue) ; alias = surnoms, pseudos, identités cachées.

Valide JSON avec node. Ne modifie rien d'autre (pas `characters.json`, pas les scripts du jeu). Réponse finale ≤10 lignes.
