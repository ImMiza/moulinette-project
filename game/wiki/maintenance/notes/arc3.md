# Notes — Arc 3 (`arcs/arc_3/arc_3_rentree.rpy`)

Clé : `arc3`. Label unique `arc_3_rentree` (l. 55), sortie `jump arc_4_noel` (l. 1162). Aucun marqueur `# SCENE` : les 11 scènes du JSON suivent les changements de décor, et le long passage du couloir est coupé au retour d'Ilona (l. 741). 5 menus.

## Personnages

**Jessy** (`j`)
- Honte plus que colère face à la rumeur (l. 209).
- Peut dire « Je suis jaloux. […] C'est dit, c'est moche » (l. 390-392).
- Peut dire « je t'aime assez pour ne pas transformer cette haine en laisse » (l. 807).
- Déteste Théo à la fin du duel (l. 698).
- Tenue : `Jessy/Festival/*`, dont `angry` (l. 10-15).

**Ilona** (`i`)
- Propose le thème Blocky House Café (l. 127-129) ; capte le public au stand pendant des heures (l. 351-352).
- Élude la question d'Allan : « C'est un stand de café, Allan. » (l. 364).
- Confidences :
  - à Laplage : « Ça me repose. Et après je m'en veux. » (l. 554) ;
  - à Jessy : « une partie de moi trouve ça agréable » (l. 789) ;
  - « Je te demande de ne pas me punir parce que tu as peur. » (l. 812).
- Tenue : `Ilona/Festival/*` (l. 17-22).

**Théo** (`t`)
- Au comité de coordination du festival (l. 110). Ajuste le plan au lieu de le prendre (l. 166-175).
- Répond à la place d'Ilona au stand (l. 334-336).
- Phrase clé : « certaines personnes écoutent Ilona seulement quand elles ont peur de la perdre » (l. 617).
- Si Jessy se tait : « Tu vois ? Même là, tu préfères qu'elle devine. » (l. 637).
- Tenue : `Theo/Festival/*` (l. 24-29).

**Allan** (`a`)
- Sa classe tient le café ; celle de Jessy et Ilona fait la déco (l. 110).
- Sa neutralité se fissure (l. 339).
- Garde trois brouillons « En vrai, moi je pense que— » puis les efface (l. 1028-1035).
- Tenue : `Allan/Festival/*`.

**Alexandre** (`x`)
- Plan avec cuisine dans l'entrée (l. 156-158) ; « Je déteste quand la géométrie gagne. » (l. 168).
- Remarque sur Ilona : « Elle est bonne » (l. 354-356).

**Sofiane** (`s`)
- « Faites attention à ceux qui creusent. » (l. 492).
- Offre du thé vert à Jessy : « La vérité peut être une main tendue. Ou un poing fermé. » (l. 729).
- Organise en secret tout le planning de rangement (l. 952-957). Métaphores de routes de montagne et de virages en épingle (l. 732, 959).
- Sprites par défaut (`observation`, `smirk`), sans tenue de festival.

**Monsieur Laplage**
- Tient le stand de takoyaki : « Aujourd'hui, je tourne les sphères. » (l. 536).
- Ubiquité : vu au stand de tir trente secondes plus tôt (l. 580) et dans un couloir fermé (l. 467).
- Aphorismes : « Un cœur vide prend de mauvaises décisions. » (l. 571).
- Sprites `Laplage/Festival/*` (l. 42-43).

**Figurants** : deux élèves anonymes qui lancent la rumeur (l. 197-202), sans speaker défini.

## Lieux et décors (images résolues)

- Train : `images/scenes/backgrounds/transport/bg_shared_train_inside.jpg`.
- Couloir du 2e étage : `images/scenes/backgrounds/school/bg_arc3_festival_hallway.jpg`. Utilisé aussi pour l'enquête, le duel et la confession.
- Stand avant le festival : `images/scenes/backgrounds/school/bg_arc3_festival_stand.jpg`.
- Stand le jour J : `images/scenes/backgrounds/school/bg_arc3_festival_stand_with_students.jpg`.
- Cour du lycée : `images/scenes/backgrounds/school/bg_arc3_festival_courtyard.jpg`.
- Salle de classe le soir : `images/scenes/backgrounds/school/bg_arc3_classroom_evening.jpg`.
- Maison Minecraft : `image bg arc3 minecraft night` réutilise `images/scenes/backgrounds/minecraft/bg_arc2_minecraft_house_summer_night.jpg` (l. 8).
- Cadre : un lycée (« lycéens » l. 330, « cour du lycée » l. 514).

## Objets et concepts

- **Blocky House Café** : café cubique avec monstres en papier, portes qui ne mènent nulle part et menu « salle moyennement importante » (l. 129, 190). Tout le café est vendu (l. 938).
- **Porte inutile** : « fausse porte importante » (l. 170). Alexandre écrit « porte en réflexion » sur une vraie porte de secours (l. 915).
- **Étoile en sucre** : objet cosmique Ilonanium de l'arc 3 (systeme de points.md:201), achetée l. 518. Mangée (+1) ou gardée sur le bureau (l. 1143).
- **Panneau principal** du café : gardé, confié à Allan ou retourné face au mur (l. 977-1013).
- **Maison Minecraft** : ajouts `panneau_phrases_tremblent_arc3`, `cuisine_ete_rangee_arc3`, `porte_inutile_fermee_arc3`, `lanterne_porte_inutile_arc3` (inatteignable). Destruction possible : `cuisine_ete_arc3`.
- **Salle secrète** de la maison (l. 1140).

## Mécaniques

Variables propres (défauts l. 45-48) :
- `arc3_reaction_rumeur` (menu l. 216).
- `arc3_aide_stand` (menu l. 379).
- `arc3_reaction_laplage` (menu l. 793). Nom trompeur : c'est la réponse à la confession d'Ilona.
- `arc3_fin_minecraft` (dérivée l. 1051-1125).

Lit l'arc 2 :
- `arc2_reaction_coucher` et `arc2_choix_activite_theo` (l. 70-101).
- `arc2_choix_activite_theo` (l. 211-214, 645).
- `souvenirs["jessy_nomme_sa_peur"]` (l. 118).

Écrites hors menus :
- `lien_jessy_ilona +1` (l. 134).
- `influence_theo +1` et souvenir `theo_utilise_une_verite` si rumeur `blague_desarm` ou `silence_paralysie` (l. 309-311).
- `confidences_laplage +1` si `ilona_peut_finir_ses_phrases < 2` (l. 530) ; `jugement_laplage +1` (l. 532).
- Souvenir `theo_utilise_une_verite` sans condition (l. 619).
- Ajustements après la confession (l. 882, 894, 902-903, 913), en classe (l. 984-1013) et sur Minecraft (l. 1053-1116).
- `souvenirs["maison_respectee"] = False` en cas de destruction (l. 1116).

Seuils lus dans l'arc :
- `jalousie >= 6` (l. 116).
- `jalousie >= 9` ou `silence_paralysie` ou `blague_defense` → Ilona « en colère » (l. 774).
- `jalousie >= 3` ou `defendre_immediat` → « frustrée » (l. 778) ; sinon « perdue ».

Relues ailleurs :
- `arc3_reaction_rumeur` : arc_6_diplomes.rpy:102-105, 754, 801-821 ; arc_7_theo.rpy:1153.
- `arc3_aide_stand` : arc_6_diplomes.rpy:107-110.
- `arc3_fin_minecraft` : arc_4_noel.rpy:112-140, 211-220, 1288 ; arc_4_5_theo.rpy:116-121 ; arc_5_examens.rpy:2454-2461 ; arc_6_diplomes.rpy:754, 832-890.
- `confidences_laplage` : arc_4_noel.rpy:720 ; script.rpy:312 (`etat_relation`) ; arc_6_diplomes.rpy:61.
- Souvenirs : arc_4_noel.rpy:231 (`jessy_nomme_sa_peur`), 589 (`theo_utilise_une_verite`) ; arc_6_diplomes.rpy:64-68.
- `maison_minecraft_ajouts` et `maison_minecraft_destructions` : jamais relues.

Menu conditionnel : le menu de l'étoile (l. 1132) n'apparaît pas si `arc3_fin_minecraft == "destruction"`. Le point Ilonanium de l'arc est alors perdu.

## Chronologie

- Septembre (l. 64), en train avec les uniformes revenus.
- « Le lendemain » : chantier du couloir (l. 155).
- « Trois jours plus tard » : collage des menus et rumeur (l. 188).
- Jour du festival (l. 330), avec l'enquête « en milieu d'après-midi » (l. 464).
- Le soir : bilan en classe (l. 935), puis Minecraft « le soir même » (l. 1048).

## Ressources

- Musiques :
  - `audio/music/morning-piano.ogg` (train) ;
  - `audio/music/festival.ogg` (couloir) ;
  - `audio/music/cafeMC.ogg` (stand) ;
  - `audio/music/sad-piano.ogg` (rumeur, Laplage, après le duel) ;
  - `audio/music/tense-piano.ogg` (duel, destruction) ;
  - `audio/music/ecole-nuit.ogg` (classe le soir) ;
  - `audio/music/Subwoofer-Lullaby.ogg` (Minecraft).
- Ambiances : `audio/ambience/tram-inside.mp3`, `audio/ambience/crowd-noise.mp3` (alias `foule`).
- Sons :
  - `audio/fx/whispers.mp3` (rumeur, l. 196) ;
  - `audio/fx/re-zero-return.mp3` (Laplage, l. 524) ;
  - `audio/fx/stones-falling.mp3` (destruction, l. 1095 et 1101) ;
  - `audio/fx/aaughmp3.mp3` (étoile mangée, l. 1155).
- Aucune CG.

## Incertitudes et contradictions

- **Branche morte** `lanterne_cour` (l. 1117-1125) : `arc3_reaction_laplage` reçoit toujours l'une des quatre valeurs testées avant. La cartographie arc_3.md le signale aussi. Elle est pourtant relue à arc_5_examens.rpy:2460 et arc_6_diplomes.rpy:881.
- **Panneau** : l'arc 3 écrit « ICI, LES PHRASES ONT LE DROIT DE TREMBLER » (l. 1059), comme l'arc 6 (l. 859). L'arc 5 cite « Laisse-la finir ses phrases » (arc_5_examens.rpy:2458). Contradiction.
- **Destruction** : l'arc 3 détruit la « cuisine d'été » (l. 1091-1115), comme le confirment l'arc 4 (l. 113, 1289) et l'arc 6 (l. 842). L'arc 5 parle de la « salle moyennement importante » jamais reconstruite (arc_5_examens.rpy:2455). Contradiction.
- **Lanterne** : l'arc 5 évoque « la lanterne bleue de la cour » pour `lanterne_cour` (l. 2461), alors que la lanterne bleue appartient à la cuisine d'été de l'arc 2 (`lanterne_bleue`, arc_2_plage.rpy:1120). Confusion probable.
- **Serviette** : « Tu as fini par retrouver ta serviette ? » (l. 75) renvoie à une perte de serviette absente de l'arc 2.
- **Cuisine d'été** : elle serait « construite après la plage » (l. 1091), mais aucune scène de construction n'existe à l'arc 2.
- **Doc vs script** : `agents/systeme de points.md:164-174` cite « Regarder Ilona d'abord et lui laisser la main. » et « Défendre Ilona immédiatement, sans lui demander. ». Le script affiche « Regarder Ilona d'abord. » et « Défendre Ilona immédiatement. » (l. 219, 256). Les effets sont identiques.
- **Ambiguïté de Sofiane** : la cible de « ceux qui creusent » n'est pas tranchée (Laplage ou Théo, l. 498-499). La cartographie dit « vise Théo » ; c'est une interprétation appuyée par l. 491.
- **Sprites** : Sofiane garde ses sprites par défaut au festival, sans tenue dédiée.
