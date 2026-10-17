# Décors et illustrations

Les images sont classées par lieu ou par séquence, indépendamment de l'arc qui
les utilise. Un décor partagé reste à un seul emplacement et peut être référencé
par plusieurs arcs.

## Arborescence

```text
scenes/
├── backgrounds/
│   ├── beach/           # Plage, jetée, parasol, stands et marée basse
│   ├── city/            # Commerces, café, cinéma, parc et rues
│   ├── family/          # Maison, restaurant, jardin et fête de la fin Family
│   ├── friend/          # Chambres, appels et appartement de la fin Friend
│   ├── hiking/          # Randonnée, lac, bivouac et tente
│   ├── minecraft/       # Maison Minecraft, prologue et variantes nocturnes
│   ├── school/          # Lycée, bibliothèque, festival et remise des diplômes
│   ├── streaming/       # Décor du stream d'introduction
│   ├── tokyo/           # Appartement, studio et ville, y compris la bad ending
│   ├── transport/       # Trains, quais et gares
│   └── winter/          # Illuminations, marché de Noël, banc et rivière en hiver
└── cg/
    ├── alexandre_fishing/ # Plans d'Alexandre pendant la pêche
    ├── family/           # Illustrations de la fin Family
    ├── jessy_epopee/     # Diaporama de randonnée et sa documentation
    ├── sofiane_initial_d/ # Séquence de conduite nocturne
    └── theo/             # Plan de Théo dans l'arc 6
```

## Conventions

- `backgrounds/` contient les décors ; `cg/` contient les plans illustrés avec
  personnages ou actions intégrés à l'image.
- Les noms de fichiers existants sont conservés, y compris leurs préfixes d'arc,
  pour garder leur provenance et les noms d'images automatiques de Ren'Py.
- Les noms déclarés avec `image bg ...` ou `image cg ...` restent identiques :
  les instructions `scene` et `show` du scénario ne changent pas.
- Les déclarations restent dans les fichiers `.rpy` des arcs et dans `script.rpy`.
  Utiliser les chemins à partir de `images/scenes/`, avec des `/`.
- Pour réutiliser une image, référencer son emplacement existant plutôt que la
  copier dans un dossier d'arc. Les variantes visuelles existantes sont conservées.
- `arc6_bg()` reçoit le chemin complet d'un décor optionnel et celui de son
  secours. `arc7_jessy_bg()` cherche dans `backgrounds/hiking/` ;
  `arc7_sofiane_cg()` cherche dans `cg/sofiane_initial_d/`.
  Les fichiers optionnels absents continuent d'utiliser leur image de secours.

## Décors de la fin Friend

Les sept nouveaux décors remplacent les fonds unis de `ending_friend.rpy` :
chambres distinctes de Jessy et d'Ilona, bureau d'Alexandre pour les appels,
appartement d'Allan avant et après l'arrivée du repas, trou Minecraft ouvert
puis refermé. Les deux derniers sont rangés dans `backgrounds/minecraft/`.
Les originaux PNG sont opaques, proches du 16:9, et affichés avec
`Transform(..., xysize=(1920, 1080), fit="cover")`.

Les références, les consignes de génération et les fichiers livrés sont recensés
dans `backgrounds/friend/README.md`. Les deux photos de groupe restent des CG
provisoires distinctes de ces décors.
