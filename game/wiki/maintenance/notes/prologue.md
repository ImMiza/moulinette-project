# Notes — Prologue (`prologue`)

Source : `game/arcs/prologue/prologue_minecraft.rpy` (395 lignes, label unique `prologue_minecraft`, sortie `jump arc_1_printemps` l. 395). Entrée : `script.rpy:374-382` (label `start`, fond `bg minecraft` = `Solid("#18241d")`, deux lignes `systeme` d'introduction, `jump prologue_minecraft`).
Titre affiché : pas de `centered`. Ligne `systeme` l. 29 : « Prologue - Minecraft : une maison beaucoup trop grande. » → titre wiki « Prologue — Minecraft ».

## Personnages

**Jessy** — pseudo chat `jessyCube` (`pmj`, l. 8), voix `j` lors de l'appel (l. 302+).
- Bâtisseur de la maison ; refuse le mot « erreur », préfère « développement » (l. 35).
- Ilona lui reproche d'« éviter les questions avec des détails techniques » ; il concède « Peut-être. » (l. 309-311).
- Promesse finale : « On finira cette maison un jour. » (l. 390).
- Apparence : sprite `jessy minecraft` (`images/personnages/Jessy/minecraft.png`, `script.rpy:95`).
- Citations : « ça veut dire que les fondations sont légales » (l. 54, au chat) ; « c'est temporaire » (répété à Alexandre, l. 320/326/332/337) ; « il y a trois murs derrière le mur » (l. 268).

**Ilona** — pseudo `IlonaGaming` (`pmi`, l. 9), voix `i` lors de l'appel.
- Entre malgré la pancarte : « j'ai une idée » / « je vais entrer » (l. 56-58).
- Casse mur + plafond + fait tomber une poule (l. 88-99).
- « Un mur, c'est triste. » (l. 151) ; « je préfère architecte de conséquences » (l. 153).
- Propose le passage en vocal (l. 270).
- Sprite `ilona minecraft` (`images/personnages/Ilona/minecraft.png`, taille fixe `ILONA_SIZE`, `script.rpy:102`).

**Alexandre** — pseudo `lorddarktime` (`pmx`, l. 10, callback `alex`). Nommé par la narration (l. 343, 348). Connaît Jessy (l'appelle par son prénom, l. 319). Verdict : « Techniquement inhabitable. » « Donc parfaite. » (l. 340-341). Pose la pancarte « NE SURTOUT PAS RENDRE ÇA NORMAL. » (l. 344). Sprite `alex minecraft` (`images/personnages/Alexandre/minecraft.png`). Le script ne dit pas explicitement qu'il est « ami » de Jessy (doc oui).

**Inconnu « ??? »** — `m_inconnu` (`script.rpy:67`, nom « ??? », callback `laplage`), sprite `laplage minecraft` (`images/personnages/Laplage/minecraft.png`). Sans pseudo, aucun message serveur (l. 374). Répliques l. 377 et 379. Identité (Monsieur Laplage) révélée en arc I → clé `arc1`. Identifiant JSON utilisé dans `prologue.json` : `inconnu` (pour ne pas afficher « Monsieur Laplage » dans une carte de scène de clé `prologue`).

**Théo** : absent.

## Lieux

- Serveur Minecraft public, maison de Jessy sur une colline : `bg prologue house afternoon` → `images/scenes/backgrounds/minecraft/bg_prologue_house_afternoon.png`.
- Entrée (pancarte) : `bg_prologue_house_entrance.png`.
- Intérieur « bizarre » : `bg_prologue_weird_interior.png`.
- Étage inachevé, accident : `bg_prologue_accident_floor.png`.
- Branches de transformation : `bg_prologue_greenhouse_branch.jpg` (serre), `bg_prologue_chicken_roof_branch.png` (poulet), `bg_prologue_slide_branch.png` (toboggan), `bg_prologue_pool_branch.png` (piscine).
- Salle secrète : `bg_prologue_secret_room.png`.
- Toit de nuit : `bg_prologue_roof_night.png`.
- Rivière : `bg_prologue_river_laplage.png` (nom de fichier = spoiler arc1, ne pas l'afficher en légende).
Tous déclarés `script.rpy:71-81`, vérifiés sur disque.

## Objets et concepts

- **Maison Minecraft** : trop de fenêtres, trop de toits, une passerelle, une tour « pour justifier l'existence d'une autre tour » (l. 34). « trois cuisines » (l. 135, branche blague seulement). « couloir sans sortie » (l. 109, branche guerre de poulets ; repris sans condition l. 361).
- **Pancartes** : « NE PAS ENTRER. SAUF SI TU AS UNE BONNE IDÉE. » (Jessy, l. 44) ; « NE SURTOUT PAS RENDRE ÇA NORMAL. » (Alexandre, l. 344) ; « salle moyennement importante » (salle secrète, l. 247-248).
- **Transformations** (`maison_minecraft_transformation`) : `serre` (serre aérienne : terre, fleurs, lanterne suspendues, l. 173) ; `poulet` (poulet géant gardien de la cuisine, sur le toit, l. 183-193 ; nommé « Monsieur Plume » en arc I) ; `toboggan` (d'une chambre inachevée à un coffre vide, « le mystère contient trois graines », l. 208-210) ; `piscine` (traverse deux pièces, condamne un escalier, eau dans le couloir, l. 224-227).
- **Poule / guerre de poulets** : une poule tombe avec le plafond (l. 89) ; option « guerre de poulets » (l. 104-111).
- **Salle secrète** : renfoncement derrière les escaliers ; porte inutile « à garder le mystère », coffre vide, fleurs, pancarte (l. 228-249).
- **Escalier « en cours de réflexion »**, porte qui « attend son étage » (l. 73-79).
- **Premier appel Discord** (son `discord-call-sound.mp3`, l. 299) : bascule des pseudos (`pmj/pmi`) vers `j/i`.

## Mécaniques

Variables écrites :
- Menu l. 101 : guerre de poulets `lien_jessy_ilona +2` ; réagir trop vite `communication -2, confiance -1, pression_stream +1, evitements +1` ; blague `lien_jessy_ilona +2` ; réparer ensemble `communication +2, confiance +1, jalousie = max(0, jalousie-1), lien_jessy_ilona +1, remember("maison_respectee")`.
- Menu l. 155 : `maison_minecraft_transformation` = `serre` (+ `autonomie_ilona +2, communication +1, confiance +1, pression_stream -1 plancher 0`) / `poulet` / `toboggan` / `piscine` (+ `lien_jessy_ilona +2` chacun).
- Menu l. 273 : accepter / demander une minute `communication +2, confiance +1, jalousie -1 (plancher 0), lien_jessy_ilona +1` ; blague `lien_jessy_ilona +2`.
- Inconditionnel : `jugement_laplage += 1` (l. 373).

Variables lues :
- `maison_minecraft_transformation` : l. 252-259 (décor de retour), l. 318-339 (Alexandre) ; `arc_1_printemps.rpy:56-76, 612-628`. Aucune autre lecture dans `game/arcs`.
- `souvenirs["maison_respectee"]` : `arc_6_diplomes.rpy:67` (+3 dans `posture`). Réécrit ailleurs : remis à `False` en `arc_3_rentree.rpy:1116` (branche destruction), réactivé `arc_2_plage.rpy:1136`, `arc_3_rentree.rpy:1136`, `arc_4_noel.rpy:246/263/853`, `arc_5_examens.rpy:2467`.
- `evitements` : seulement `arc_6_diplomes.rpy:70` (`-3 * max(0, evitements - 3)`).
- `jugement_laplage` : **jamais lu** (seulement incrémenté : prologue l. 373, arc 2, 3, 4, 4.5, 5).
- `lien_jessy_ilona` : seuils `arc_1:442`, `arc_2:204`, `arc_4:615/626/1255…`, `arc_5:374/1272/1297` ; absent du score de l'arc VI (`arc6_calcule_verdict`, `arc_6_diplomes.rpy:44-84`) et de `etat_relation` (`script.rpy:283-323`).
- `maison_minecraft_destructions` / `maison_minecraft_ajouts` (`script.rpy:243-244`) : non utilisés dans le prologue (l'effondrement n'y est pas enregistré).

Menus : 3. Aucun menu conditionnel.

## Chronologie

- Fin d'après-midi → nuit, même soirée (l. 30, 264, 355). Saison/date non précisées ; antérieur à avril (arc I : « Depuis la maison Minecraft… presque tous les soirs », `arc_1_printemps.rpy:23`).
- Ordre : construction → pancarte → arrivée d'Ilona → visite → effondrement → transformation → salle secrète → vocal → Alexandre → toit de nuit → rivière.

## Ressources

- Musique : `audio/music/Haggstrom.ogg` (`audio.mc`, l. 12, joué l. 24) ; `audio/music/Subwoofer-Lullaby.ogg` (`audio.mcnight`, `script.rpy:161`, l. 349).
- Sons : `audio/fx/minecraft-walking-on-grass.mp3`, `minecraft-wood-break-place.mp3`, `minecraft-door.mp3`, `stones-falling.mp3` (effondrement + `hpunch`), `construction.mp3`, `big-Chicken.mp3`, `water-minecraft.mp3`, `discord-call-sound.mp3`, `villager.mp3` (arrivée d'Alexandre), `re-zero-return.mp3` (`audio.laplage`, apparition de l'inconnu).
- Aucune CG.

## Incertitudes et contradictions

- Lignes 38, 42, 46 : `play sound "fx/…"` sans préfixe `audio/`. Le dossier `game/fx` n'existe pas ; les fichiers sont dans `game/audio/fx/`. Résolution probable via le répertoire audio de Ren'Py (interprétation, non testé en jeu).
- `audio.mcvilager` (orthographe « vilager ») pointe bien vers `audio/fx/villager.mp3`.
- `script.rpy:380` affiche au joueur une ligne de développement (« La base actuelle pose les arcs, les variables… »).
- Doc `cartographies/prologue.md` : conforme au script sur les menus et effets. Elle dit Alexandre « ami de Jessy » : non explicite dans le script.
- « couloir sans sortie » et « trois cuisines » n'apparaissent que dans des branches optionnelles mais sont repris ou supposés ailleurs (signalé aussi dans la doc).
- Menu l. 273 : options 1 et 3 ont des effets identiques.
- La branche `else` des tests (l. 258, 335) couvre `poulet` (décor) et `toboggan` (Alexandre) ; la valeur vide `""` est impossible après le menu l. 155.
