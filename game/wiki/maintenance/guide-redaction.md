# Guide de rédaction du wiki

Règles pour écrire ou mettre à jour le contenu éditorial (humains et agents).

## Sources

- **Vérité** : les scripts `game/**/*.rpy` (hors `game/wiki`, `game/tmp`, `*.bak`).
- **Contexte** : `game/agents/**` (docs de conception). Une info présente seulement en doc est marquée « prévu (doc) ». Toute contradiction doc/script est notée dans les notes, jamais tranchée en silence.
- Ne rien inventer. Une interprétation non confirmée est marquée « interprétation ».
- Chemins de ressources : relatifs à `game/` (ex. `images/backgrounds/beach/bg_beach_day.jpg`) et vérifiés sur disque.

## Clés de progression (spoilers)

`public`, tronc `prologue` → `arc1` → `arc2` → `arc3` → `arc4` (inclut scènes 4.5) → `arc5` → `arc6`, puis branches indépendantes `routeA` (fichier `arc_7_jessy.rpy`), `routeB` (`arc_7_theo.rpy`), fins `finA1` (ending_friend), `finA2` (ending_family), `finA3` (ending_ilonanium, secrète), `finB1` (ending_neutre), `finB2` (bad_ending), et `extras` (coulisses, contenus inutilisés).

Un contenu reçoit la clé du **dernier** moment de l'histoire qu'il révèle.

## Neutralité des éléments publics

Jamais de spoiler dans : titre de page, `description`, titres `##`, liens, alt d'images publiques, noms de scènes visibles hors spoiler.
- Routes : « Route A » / « Route B ». Fins : « Fin A1 », « Fin A2 », « Fin A3 », « Fin B1 », « Fin B2 ».
- Personnages tardifs (Micka, Lucy, Florentin, Tchat…) : jamais nommés hors spoiler.
- Titres d'arcs : les titres officiels affichés en jeu (`centered "ARC n : …"`) sont autorisés pour le prologue et les arcs 1 à 6.

## Composant Spoiler (MDX)

```mdx
import Spoiler from '../../../components/Spoiler.astro';

<Spoiler requires="arc3" note="détails de l'arc III">

Texte **Markdown** ici (lignes vides autour obligatoires).

</Spoiler>
```

- `requires` : une clé ou une liste (`requires={['finA1','finB1']}`), `mode="any"` pour « l'une des clés ».
- **Interdit dans un Spoiler** : titres Markdown (`##`, `###`) — ils fuiraient dans la table des matières. Utiliser `**Sous-titre**`.
- Pas d'images protégées hors Spoiler ; `<Media>` applique tout seul le prérequis de l'inventaire.

## Données de scènes : `src/data/scenes/<clé>.json`

```json
{
  "arc": "arc2",
  "title": "ARC 2 : VACANCES D'ÉTÉ — LA PLAGE",
  "file": "arcs/arc_2/arc_2_plage.rpy",
  "scenes": [
    {
      "id": "arc2-s1",
      "title": "Titre de scène (celui du commentaire # SCENE si présent)",
      "label": "arc_2_plage",
      "lines": "12-140",
      "requires": "arc2",
      "condition": "Seulement si … (code exact entre backticks absent : texte clair + variable)",
      "location": "Plage",
      "characters": ["jessy", "ilona"],
      "summary": "Paragraphe 1.\n\nParagraphe 2.",
      "choices": [
        { "line": 230, "prompt": "Question affichée (ou résumé si absente)", "condition": "si condition d'apparition",
          "options": [ { "text": "Texte exact de l'option", "effects": "communication +2, souvenir jessy_repare", "condition": "si condition sur l'option" } ] }
      ],
      "consequences": ["Effet narratif vérifié plus loin (avec fichier:ligne si utile)"],
      "backgrounds": ["images/..."],
      "cgs": ["images/scenes/cg/..."],
      "music": ["audio/music/....ogg"]
    }
  ]
}
```

Identifiants de personnages : `jessy`, `ilona`, `theo`, `allan`, `alexandre`, `sofiane`, `laplage`, `micka`, `tchat`, `lucy`, `florentin`, `narrateur`. Autre personnage nommé : identifiant minuscule sans accent, signalé dans les notes.

## Notes persistantes : `maintenance/notes/<clé>.md`

Sections : Personnages (faits confirmés avec `fichier:ligne`, apparence/tenues, relations, 2 à 5 citations courtes avec contexte), Lieux (+ décors associés), Objets et concepts, Mécaniques (variables écrites/lues), Chronologie (dates, saisons), Ressources (CG, musiques, sons marquants), Incertitudes et contradictions.
