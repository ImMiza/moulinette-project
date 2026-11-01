# Notes — Arc 2 (`arcs/arc_2/arc_2_plage.rpy`)

Clé : `arc2`. Label unique `arc_2_plage` (l. 52), sortie `jump arc_3_rentree` (l. 1171). Aucun marqueur `# SCENE` : les 11 scènes du JSON suivent les changements de décor (`scene bg …`). 7 menus.

## Personnages

**Jessy** (`j`, joueur, masculin)
- Ne connaît Théo « surtout par les phrases d'Allan » (l. 76).
- Fouille le sable sans trouver le porte-clés (l. 265-269) ; branche coquille blanche (l. 305-315).
- Peut nommer sa peur : « Parce que j'ai peur. » (l. 564) ; « je me suis senti remplaçable » (l. 1062).
- Crie sur Alexandre dans la branche `suivre` : « Parce que j'ai paniqué, bordel ! » (l. 902).
- Tenue : sprites `Jessy/Beach/*` (l. 12-16), sprites par défaut dans le couloir d'ouverture (l. 65), `minecraft` le soir (l. 1087).

**Ilona** (`i`)
- Couple implicite avec Jessy : « test de fidélité » (l. 717), « Tu me demandes si j'ai trompé […] ? » (l. 1042).
- Parle seule pour choisir (l. 248-254) ; préfère l'ombre (l. 184-186).
- Possède un porte-clés bloc « de la maison » (l. 262-264).
- Choisit la gelée marine lumineuse : « Il m'a regardée en premier. » (l. 427).
- Veut « finir mes phrases avant qu'on trouve une solution pour moi » (l. 852) ; refuse un « comité » (l. 856-860).
- Tenue : sprites `Ilona/Beach/*`, dont `sad` (l. 18-24).

**Théo** (`t`) — première apparition à l'écran (l. 175)
- Seulement mentionné jusque-là (arc_1_printemps.rpy:607). Ami d'Allan (l. 76, 178).
- Attentions sans demander : parasol, sac à l'ombre (l. 183-185), porte-clés retrouvé (l. 270-286).
- Coupe Ilona (l. 449-450) ; s'en excuse aux mares : « Je fais ça trop souvent. » (l. 643).
- Phrases clés : « Je fais attention. » (l. 282) ; « Avec toi, j'aimerais juste... écouter. » (l. 645) ; « T'as tout gâché, mec. » (l. 723, branche `suivre`).
- Tenue : `Theo/Beach/neutral` et `reassuring_smile` uniquement (l. 26-27).

**Allan** (`a`)
- Organise la sortie (l. 68-73).
- Recadre Théo : « Attends. Elle parlait encore. […] Ralentis. » (l. 452-454).
- Rejoint Ilona aux objets trouvés : « On garde une place sans panneau. » (l. 869).

**Alexandre** (`x`)
- Château de sable « techniquement inhabitable », avec une porte sur le toit (l. 83, 227).
- Pelle à « vie indépendante » (l. 835) ; « Commission temporaire des phrases inachevées » (l. 863).
- Conseille Jessy après le pivot (l. 594-616).

**Sofiane** (`s`)
- Seulement dans le train : « La mer a appelé. J'ai laissé sonner deux fois. » (l. 155).
- Sprite `Sofiane/Beach/reserved_neutral` (l. 38).

**Monsieur Laplage** (`laplage`)
- Tient une table d'objets trouvés : « Je remplace quelqu'un qui n'était pas prévu. » (l. 790).
- Gag récurrent : « la plage est sèche » (l. 808-817).
- Sprites par défaut `neutral` / `thumb_up`.

## Lieux et décors (images résolues)

- Couloir de l'école : `images/scenes/backgrounds/school/bg_shared_school_corridor.jpg` (déclaré dans `script.rpy:91`).
- Train : `images/scenes/backgrounds/transport/bg_shared_train_inside.jpg` (`script.rpy:92`).
- Coin du parasol : `images/scenes/backgrounds/beach/bg_arc2_group_parasol.jpg`.
- Stand de kakigōri : `images/scenes/backgrounds/beach/bg_arc2_kakigori_counter.jpg`.
- Plage (photo) : `images/scenes/backgrounds/beach/bg_arc2_beach_main.jpg`.
- Mares entre les rochers : `images/scenes/backgrounds/beach/bg_arc2_tide_pools.jpg`.
- Jetée : `images/scenes/backgrounds/beach/bg_arc2_jetty.jpg`.
- Objets trouvés : `images/scenes/backgrounds/beach/bg_arc2_lost_items_table.jpg`.
- Coucher de soleil : `images/scenes/backgrounds/beach/bg_arc2_beach_sunset.jpg`.
- Maison Minecraft de nuit : `images/scenes/backgrounds/minecraft/bg_arc2_minecraft_house_summer_night.jpg`. Réutilisé aux arcs 3, 4, 5, 6 et en Route A.

## Objets et concepts

- **Porte-clés bloc** d'Ilona, retrouvé par Théo (l. 262-286). Objet récurrent : rumeur de l'arc 3, arc 5:650, arc 6:809, Route B (arc_7_theo.rpy:1020, 1494), fins B1 et B2 (ending_neutre.rpy:440, bad_ending.rpy:352).
- **Coquille blanche** offerte par Jessy, branche « Chercher aussi » (l. 308-314). Jamais relue.
- **Photo de groupe** : Jessy au bord, Ilona près de Théo (l. 363-364). Une deuxième photo existe si `refaire_doux` (l. 393-394).
- **Gelée marine lumineuse** : objet cosmique Ilonanium de l'arc 2 (systeme de points.md:201). Seulement si Ilona la mange (l. 1135-1142).
- **Maison Minecraft** : plusieurs cuisines, « cuisine de plage » proposée (l. 136), « cuisine d'été » (l. 1120), « couloir sans issue » (l. 1110), « salle moyennement importante » (l. 1143).

## Mécaniques

Variables propres (défauts l. 46-49) :
- `arc2_photo_reaction` (menu l. 370).
- `arc2_choix_activite_theo` (menu pivot l. 490).
- `arc2_reaction_coucher` (menu l. 964).
- `arc2_retour_minecraft` (calculé l. 1095-1130).

Écrites :
- Compteurs : `lien_jessy_ilona`, `communication`, `confiance`, `jalousie` (avec plancher `max(0, …)` sur les baisses), `autonomie_ilona`, `influence_theo`, `controles`, `evitements`, `pression_stream`.
- `interruptions_ilona` (+1 seulement si `suivre`), `interruptions_reconnues` / `interruptions_reparees` (menu du coucher).
- `lien_ilona_theo` (+2 l. 672 ou l. 763), `jugement_laplage` (+1 l. 786), `ilonanium_points` (+1 l. 1137).
- Souvenirs : `ilona_libre_sans_abandon` (l. 499), `jessy_nomme_sa_peur` (l. 561, 1057), `jessy_repare` (l. 991, conditionnel), `maison_respectee` (l. 1136).

Lues dans l'arc :
- `ilona_peut_finir_ses_phrases >= 2`, `communication < 0` (l. 140-147).
- `lien_jessy_ilona >= 10` (l. 204).
- `jalousie >= 6` (l. 344, 481), `> 0` (l. 483), `>= 9` (l. 1162).
- `autonomie_ilona >= 12` (l. 674), `communication >= 12` (l. 1108).

Relues ailleurs :
- `arc2_choix_activite_theo` : arc_3_rentree.rpy:70-101, 211-214, 645 ; arc_4_noel.rpy:173, 783-795 ; arc_5_examens.rpy:862 ; arc_6_diplomes.rpy:95-100 (reproches de Théo), 754, 764-791 (vignettes) ; arc_7_theo.rpy:1019-1026.
- `arc2_reaction_coucher` : arc_3_rentree.rpy:70.
- `arc2_photo_reaction` : arc_5_examens.rpy:649 (`silence_photo` uniquement).
- `arc2_retour_minecraft` : jamais relue hors arc 2.
- `lien_ilona_theo` : arc_4_noel.rpy:356.
- `jugement_laplage` : jamais relue dans le jeu.
- `ilonanium_points` : arc_5_examens.rpy:2556 (`>= 3`) ; arc_7_jessy.rpy:1177 (`== 6`, fin secrète).
- Souvenirs : arc_6_diplomes.rpy:64-68 (score).

Menus conditionnels : au menu de la l. 1132, l'option gelée est masquée si `arc2_retour_minecraft == "porte_fermee"` ; le point Ilonanium de l'arc est alors perdu.

## Chronologie

- Juillet (l. 60), annonce de la sortie « samedi » (l. 68).
- Samedi matin dans le train (l. 133), puis journée à la plage jusqu'au coucher du soleil (l. 964).
- Le soir même sur Minecraft (l. 1090).
- Référence au printemps (arc 1) : « Au printemps, tu m'as laissée répondre à mon rythme » (l. 141).

## Ressources

- Musiques :
  - `audio/music/ecole-music.ogg` (couloir) ;
  - `audio/music/morning-piano.ogg` (train) ;
  - `audio/music/plage-day.ogg` (plage) ;
  - `audio/music/plage-sunset.ogg` (mares, objets trouvés, coucher) ;
  - `audio/music/sad-piano.ogg` (branches du pivot, coucher) ;
  - `audio/music/tense-piano.ogg` (`suivre`) ;
  - `audio/music/Subwoofer-Lullaby.ogg` (Minecraft).
- Ambiances : `audio/ambience/tram-inside.mp3`, `audio/ambience/ocean-waves.mp3`, `audio/ambience/crowd-noise.mp3` (alias `audio.foule`, `script.rpy:188`).
- Sons :
  - `audio/fx/sand-walk.mp3`, `audio/fx/sand-noise.mp3`, `audio/fx/photo-taken.mp3` ;
  - `audio/fx/piano-slam.mp3` (Ilona découvre qu'on la suit, l. 529) ;
  - `audio/fx/re-zero-return.mp3` (arrivée de Laplage, l. 783) ;
  - `audio/fx/aaughmp3.mp3` (gelée mangée, l. 1139).
- Aucune CG.

## Incertitudes et contradictions

- Ouverture : le couloir d'école en juillet est déjà signalé comme faiblesse dans `agents/cartographies/arc_2.md`. Les sprites y restent par défaut, pas en tenue de plage.
- Gelée marine : elle « commence à fondre » ou « fond lentement » dans la branche `disparaitre` (l. 742, 751), mais le gobelet est intact le soir (« Elle n'y a pas touché », l. 1092) et peut être mangé.
- « Cuisine d'été » : citée comme existante (l. 1120), alors que le train ne parle que d'un projet de « cuisine de plage » (l. 136). L'arc 3 la dit « construite après la plage » (arc_3_rentree.rpy:1091), sans scène de construction.
- Sofiane : Allan ne l'évoque que dans l'option « Demander simplement qui vient » (l. 93), mais il apparaît dans le train dans tous les cas. Il ne réapparaît plus à la plage.
- `arc2_retour_minecraft = "silence"` : ne survient qu'avec `blague_jalouse` suivi de `reparation` ou `peur_nommee` (logique l. 1095-1125).
- Doc vs script : la cartographie annonce `lien_ilona_theo += 2` sauf `suivre`, ce qui est confirmé. Le pivot est bien `arc2_choix_activite_theo` (systeme de points.md:129). Aucune divergence d'effets relevée sur les 7 menus.
- `jugement_laplage` : incrémenté ici et ailleurs, mais aucune lecture trouvée (`grep` sur `game/**/*.rpy`). Interprétation : variable vestigiale ou prévue.
