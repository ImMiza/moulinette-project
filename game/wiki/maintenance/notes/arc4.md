# Notes — Arc IV (clé `arc4`, scènes 4.5 incluses)

Sources : `game/arcs/arc_4/arc_4_noel.rpy` (1373 l.), `game/arcs/arc_4/arc_4_5_maid_cafe.rpy` (255 l.), `game/arcs/arc_4/arc_4_5_theo.rpy` (463 l.). Chemins ci-dessous relatifs à `game/arcs/arc_4/` sauf mention contraire. Ignoré : `arc_4_noel.rpy.bak` (60 Ko, ancienne version, non relue).
Contexte : `game/agents/cartographies/arc_4.md`, `game/agents/systeme de points.md` (l.130, 133, 201, 229).
Entrée : `arcs/arc_3/arc_3_rentree.rpy:1162` (`jump arc_4_noel`). Sortie : `arc_4_noel.rpy:1373` (`jump arc_5_examens`).
Titre officiel : `arc_4_noel.rpy:102` « ARC 4 : NOËL — LE CADEAU QUI DIT TROP DE CHOSES ».

## Personnages

**Jessy** (`j`)
- Transporte un paquet depuis le matin (`arc_4_noel.rpy:177-179`). C'est une miniature de la maison Minecraft dans un papier bleu sombre (l.200-209), avec ses erreurs : couloir sans sortie, cuisine trop grande, « pièce que personne ne comprend ».
- Branche panique : achète une écharpe « Belle. Chère. Vide. » (l.288).
- Avoue la compétition : « Si. Ça l'est devenu. » / « j'ai l'impression de perdre sans même savoir qu'on jouait » (l.779-781).
- Citation : « Je veux gagner. » … « Et je déteste tout ce que je viens de dire. » (l.917-919, branche parole_sans_verdict).
- Citation : « Émotionnellement, il va fuir. » (l.1349, branche neige_sur_toit, en pratique inaccessible).
- Absent de la scène 4.5 Théo.

**Ilona** (`i`)
- Avait dit une seule fois en juillet, à la plage, qu'elle oubliait ses idées dehors (l.373-376).
- Parle au mochi : « Tu as l'air trop cosmique pour un dessert. » (l.679).
- Juron rare : « Vous allez arrêter de transformer chaque putain de cadeau en duel. » / « Je ne suis pas un trophée qu'on gagne avec des souvenirs bien placés. » (l.491-493).
- Limite : « Ce n'est pas parce que quelqu'un connaît mes goûts qu'il sait ce que je veux. » (l.972) ; « j'ai le droit de vous aimer tous les deux différemment sans que ce soit un classement » (l.982).
- Branche parole_sans_verdict : « Moi aussi, des fois, je veux que tu m'aimes plus que ton jeu. Plus qu'Alexandre. » (l.921).
- 4.5 Théo, réaction accepte : veut « streamer. Pour de vrai », avec planning et communauté (`arc_4_5_theo.rpy:196-200`). Fin de scène : peur de « remplacer une cage par une autre » (l.450).
- Fatigue liée au stream évoquée si pression_stream ≥ 6 (`arc_4_noel.rpy:166-168`).

**Théo** (`t`)
- Offre un carnet de croquis minuscule : couverture noire, coins renforcés, étiquette intérieure (l.372). « Un rien. » (l.369) / « Je fais attention. » (l.380).
- Appelle Laplage « le Messi » (l.544). Origine selon Allan : Théo l'avait d'abord appelé « le GOAT des conseils cryptiques » (l.576-577).
- 4.5 : donne son écharpe à Ilona (`arc_4_5_theo.rpy:58-71`) ; « Je te propose juste... un espace. » (l.144) ; masque qui craque : « Moi ? » (l.138-140) ; réponse « Bien sûr. » = « Une dette qui commence. » (l.217-219).

**Allan** (`a`)
- Organise la sortie (l.158-159). Commence à trouver « sa neutralité fatigante » (l.569).
- « Je passe mon temps à éclairer les chemins des autres. Mais je ne sais pas où va le sien. » (l.644-645). Refuse l'enveloppe : « Si elle est vraiment pour moi, elle attendra. » (l.657).
- Soutient Ilona face à Théo : « Elle a répondu, Théo. » (l.1187). « Je marche lentement, mais avec fiabilité émotionnelle. » (l.1176).

**Alexandre** (`x`)
- Aide Jessy à choisir le papier (l.197). « Si tu ne décides pas, ta peur le fera à ta place. » (l.229). « Respect du matériau source. » (l.209).
- « comprendre quelqu'un, c'est pas forcément avoir raison sur lui » (l.598).
- 4.5 maid : « Bonne nuit, les pas-amoureux. » (`arc_4_5_maid_cafe.rpy:28`).

**Sofiane** (`s`)
- « Les lumières ne disent pas où aller. Elles disent juste qu'il fait nuit. » (l.604). Pose une enveloppe sans nom sur le banc puis la récupère fermée (l.607-613, 661-663).
- Si synergie forte : « Le service m'appelle. » / « Celui qui nourrit la route. » (l.615-619).
- 4.5 maid : travaille dans un maid café « Depuis trois mois. Le salaire finance l'essence. La route a faim. » (`arc_4_5_maid_cafe.rpy:156`). Vouvoie « Maîtres ». Demande le secret vis-à-vis d'Allan et Alexandre (l.193).

**Monsieur Laplage** (`laplage`)
- En Père Noël : « Père Noël intérimaire. Service des horizons froids. » (l.704) ; « Je travaille surtout entre les endroits. » (l.706).
- À Théo : « un souvenir bien placé, c'est comme une clé » … « Ou verrouiller quelqu'un dedans. » / « Mais tu gardes la clé. » (l.550-555).
- À Ilona : « Poser une limite n'est pas casser le cadeau. » (l.728) ; « Les décisions froides méritent une main chaude. » (l.734) ; « Je vends surtout des pauses. » (l.737). Pouce levé (l.738).
- 4.5 Théo : remplaçant en tenue de maid au même café : « Quelqu'un devait remplacer quelqu'un qui devait remplacer quelqu'un. » (`arc_4_5_theo.rpy:345`). Pouce « Ni levé. Ni baissé. Juste horizontal. » (l.369).
- Effet sonore d'apparition : `audio.laplage` = `audio/fx/re-zero-return.mp3`.

### Tenues / sprites
- **Winter** : Jessy, Ilona, Théo, Allan, Alexandre, Sofiane (`arc_4_noel.rpy:10-73`, dossiers `images/personnages/<Perso>/Winter/`).
- **Winter_with_scarf** : Ilona et Théo (l.26-32, 43-50). Théo porte l'écharpe par défaut au marché (`theo winter scarf`). En 4.5 Théo, Ilona prend l'écharpe et Théo passe en `theo winter` (`arc_4_5_theo.rpy:69-71`).
- **Christmas** : Laplage `neutral`, `thumb_up` (l.75-76).
- **Maid** : Sofiane `images/personnages/Sofiane/maid.png` (déclaré dans `game/script.rpy:141`) ; Laplage `images/personnages/Laplage/Maid/neutral.png`, `thumb_horizontal.png` (`arc_4_5_theo.rpy:12-13`, transform `laplage_maid_counter` zoom 0.5).
- **Minecraft** : `jessy minecraft`, `ilona minecraft` (`script.rpy:95, 102`).
- Aucun personnage nouveau. Identifiants utilisés : jessy, ilona, theo, allan, alexandre, sofiane, laplage.

## Lieux

- Train du matin → `images/scenes/backgrounds/transport/bg_arc4_train_inside.jpg` (`bg arc4 train inside`).
- Galerie commerciale (papeterie) → `images/scenes/backgrounds/city/bg_arc4_shopping_gallery.jpg`.
- Rue illuminée → `images/scenes/backgrounds/winter/bg_arc4_illuminations.jpg` (réutilisé comme `bg arc4_city_night` dans la scène du maid café).
- Marché de Noël du quartier (stand de mochi, stand de cartes postales, banc près du brasero) → `images/scenes/backgrounds/winter/bg_arc4_christmas_market.jpg`.
- Rambarde le long de la rivière → `images/scenes/backgrounds/winter/bg_arc4_riverside_winter.jpg`.
- Maison Minecraft sous la neige → déclarée `bg arc4 minecraft winter night`, mais l'image est `images/scenes/backgrounds/minecraft/bg_arc2_minecraft_house_summer_night.jpg` (décor d'été réutilisé).
- Maid café « OUVERT JUSQU'À MINUIT » → `images/scenes/backgrounds/city/bg_arc4_5_maid_cafe_exterior.jpg`, `.../bg_arc4_5_maid_cafe_interior.jpg`.
- Parc résidentiel (allée, banc sous lampadaire) → `images/scenes/backgrounds/winter/bg_arc4_park_bench.jpg`, sous deux alias (`bg arc4_5 street winter night`, `bg arc4_5 park bench`). Commentaire `arc_4_5_theo.rpy:8` : le parc sert de remplaçant « tant que la rue dédiée n'existe pas ».

## Objets et concepts

- **Miniature de la maison Minecraft** (cadeau de Jessy). Variante blague avec le panneau « PIÈCE MOYENNEMENT IMPORTANTE, ÉDITION NEIGE » (l.869). Si elle n'est pas offerte, elle reste dans le sac, « en attente » (l.320).
- **Carnet de croquis de Théo** (l.372).
- **Écharpe chère** de Jessy (branche cadeau_couteux) ; dans Minecraft, elle devient un bloc de laine bleu rangé dans un coffre (l.1320).
- **Écharpe de Théo**, donnée à Ilona en 4.5 Théo.
- **Mochi cosmique** pailleté : l'un des 6 objets cosmiques (doc `systeme de points.md:201`). Manger = `ilonanium_points +1` ; garder = rien.
- **Enveloppe sans destinataire** de Sofiane : fil ouvert, jamais lue dans l'arc.
- **« Le service »** de Sofiane = job au maid café (révélé en 4.5).
- **Café chaud** de Laplage (« Je vends surtout des pauses »).
- Rappels de la maison Minecraft de l'arc III : trou, porte inutile fermée, panneau, cuisine d'été rangée, lanterne (l.112-146).
- « Mise en abyme émotionnelle » (l.1307) : la miniature reconstruite dans la salle secrète.

## Mécaniques

**Variables posées (defaults l.82-91, maid l.10, Théo l.20-21)** : `arc4_cadeau_jessy`, `arc4_reaction_cadeau_theo`, `arc4_limite_ilona` (pivot ×3, doc `systeme de points.md:130`), `arc4_accueil_limite`, `arc4_fin_minecraft`, `arc4_carte_sofiane_lue`, `arc4_mochi_cosmique`, `arc4_ilona_avec_theo`, `arc4_ilona_winter_sprite`, `arc4_theo_winter_sprite`, `arc4_5_sofiane_maid`, `arc4_5_theo_proposition`, `arc4_5_ilona_reaction`.

**Menus** (6 au total) :
1. `arc_4_noel.rpy:237` : cadeau (5 options).
2. `:385` : réaction au carnet (5 options).
3. `:682` : mochi (2 options).
4. `:797` : limite, pivot (5 options, dont 3 conditionnées par `arc4_cadeau_jessy`).
5. `:987` : accueil de la limite (5 options).
6. `arc_4_5_maid_cafe.rpy:86` : entrée au maid café (3 options).

Effets exacts : voir `src/data/scenes/arc4.json`. La scène 4.5 Théo n'a pas de menu : réaction calculée (`arc_4_5_theo.rpy:156-163`).

**Lectures de jauges et variables antérieures dans l'arc** : `arc3_fin_minecraft` (l.112, 211, 1288 ; `arc_4_5_theo.rpy:116`), `arc2_choix_activite_theo` (l.173, 783, 790), `jalousie >= 9` (l.151), `confiance >= 15 and communication >= 15` (l.155), `pression_stream >= 6` (l.166), `influence_theo >= 6` / `lien_ilona_theo >= 2` (l.353-356), souvenirs `jessy_nomme_sa_peur` (l.231) et `theo_utilise_une_verite` (l.589), `confidences_laplage >= 1` (l.720).

**Seuils clés** :
- Synergie : `lien_jessy_ilona >= 10 and communication >= 25 and confiance >= 15`. Testée l.615, 626 (répliques de Sofiane), l.1255 (phrase de fin) et l.1258 (appel du maid café).
- Garder les cadeaux : limite ∈ {cadeau_respirant, parole_sans_verdict, marche_silencieuse}, accueil ≠ accuser_theo, `communication >= 25` (l.1089).
- Départ avec Théo : `influence_theo >= 10 and confiance <= 8 and arc4_limite_ilona == "demande_theo"` (l.1203).
- Souvenir `ilona_pose_une_limite` : `ilona_peut_finir_ses_phrases >= 2 and interruptions_ilona <= interruptions_reparees` (l.977), testé avant le menu d'accueil.
- `confidences_laplage += 1` si `ilona_peut_finir_ses_phrases < 4` (l.749-750). Commentaire l.748 : « Une confidence à Laplage est une dette, pas un crédit (porte de l'arc 6) » ; relu dans `arc_6_diplomes.rpy:61` et `script.rpy:312`.

**Souvenirs (`remember`)** : `maison_respectee`, `jessy_nomme_sa_peur`, `ilona_pose_une_limite`, `jessy_repare`, `theo_utilise_une_verite`, `ilona_veut_streamer_serieusement` (ces deux derniers seulement en 4.5 Théo, réaction accepte).

**Ajouts à la maison (`maison_minecraft_ajouts`)** : `miniature_noel_arc4`, `espace_calme_arc4`, `echarpe_coffre_arc4`, `coin_dehors_carnet_arc4`, `neige_toit_arc4` (inaccessible).

**Relectures ultérieures (vérifiées par grep)** :
- `arc4_fin_minecraft` : `arc_5/arc_5_examens.rpy:89-97`.
- `arc4_cadeau_jessy` : `arc_5_examens.rpy:2092-2098`, `arc_6/arc_6_diplomes.rpy:218-221`, `arc_7/arc_7_jessy.rpy:621`.
- `arc4_limite_ilona` : `arc_5_examens.rpy:2092, 2102` ; `arc_6_diplomes.rpy:112, 754, 900-952` (vignettes).
- `arc4_reaction_cadeau_theo` : `arc_7/arc_7_theo.rpy:1231`.
- `arc4_ilona_avec_theo` : `arc_5_examens.rpy:100, 138, 752, 988, 2106` ; `arc_6_diplomes.rpy:112, 216, 754, 967` ; `arc_7_theo.rpy:971, 1478`.
- `arc4_5_ilona_reaction` / `arc4_5_theo_proposition` : `arc_5_examens.rpy` (nombreuses lignes, 101-1100, 2107-2257) ; `arc_6_diplomes.rpy:982-991` ; `arc_7_theo.rpy:976-980, 1476`.
- `arc4_5_sofiane_maid` : `arc_6_diplomes.rpy:500`, `arc_7_jessy.rpy:297`, `endings/ending_family.rpy:661`.
- `arc4_ilona_winter_sprite` / `arc4_theo_winter_sprite` : `arc_5_examens.rpy:375-1935` (`show expression`).
- `arc4_mochi_cosmique`, `arc4_accueil_limite` : lus uniquement dans l'arc 4.
- `ilonanium_points` : `arc_5_examens.rpy:2556` (≥ 3), `arc_7_jessy.rpy:1177` (== 6).
- `jugement_laplage` (+1 l.751, +1 `arc_4_5_theo.rpy:372`) : écrit partout, jamais relu (grep).

## Chronologie

- Décembre (l.106). Festival = septembre (l.106), plage = juillet (l.376).
- Une seule journée : train du matin → galerie après les cours → marché « une heure plus tard » (l.343) → rivière → sortie → (4.5 dans la nuit, neige) → maison Minecraft « plus tard » dans la nuit.
- Sofiane travaille au maid café depuis trois mois, donc depuis environ septembre (interprétation).

## Ressources

- Musiques : `audio/music/morning-piano.ogg` (train), `xmas-mall.ogg` (galerie, défini l.78), `xmas-market.ogg` (marché, l.79), `melancolique-piano.ogg` (rivière), `Subwoofer-Lullaby.ogg` (Minecraft), `night-walk.ogg` et `maidCafe.ogg` (4.5).
- Ambiances : `audio/ambience/tram-inside.mp3`, `audio/ambience/crowd-noise.mp3`.
- Sons : `audio/fx/train-stop.mp3`, `audio/fx/re-zero-return.mp3` (Laplage), `audio/fx/aaughmp3.mp3` (mochi mangé), `audio/fx/WOW.mp3` (apparition de Sofiane et de Laplage en maid, défini `arc_4_5_maid_cafe.rpy:8`).
- Aucun CG dans l'arc ni dans les scènes 4.5.
- Tous les chemins ont été vérifiés sur disque.

## Incertitudes et contradictions

1. **Conditions de la scène 4.5 Théo** : le commentaire `arc_4_5_theo.rpy:2` indique `influence_theo >= 5, confiance <= 2`, alors que le code (`arc_4_noel.rpy:1203`) teste `>= 10` et `<= 8`. Le code fait foi.
2. **Jessy « rentré en métro »** (`arc_4_5_theo.rpy:35`), alors qu'il reste « immobile » au marché, la main d'Allan sur l'épaule (`arc_4_noel.rpy:1237-1238`).
3. **Citation déformée** : `arc_4_5_theo.rpy:49, 92` cite « Tu me demandes de te rassurer… », alors que la réplique réelle est « Tu demandes si je dois te rassurer avant même… » (`arc_4_noel.rpy:813`).
4. **Cadeaux jamais offerts** : en 4.5 Théo (chemin `demande_theo`), Ilona pense à « la miniature qu'elle n'a jamais regardée vraiment » ou à « l'écharpe qu'elle a reçue » (`arc_4_5_theo.rpy:130-132, 430-432`). Or l'option `demande_theo` ne fait offrir ni la miniature ni l'écharpe.
5. **Doc ≠ script** : `cartographies/arc_4.md:50` dit les variables de sprite « inutilisées », alors qu'elles sont relues dans `arc_5_examens.rpy` (`show expression`).
6. **`arc4_carte_sofiane_lue`** est toujours vrai (l.624), alors que personne ne lit la carte. La variante `arc_4_5_maid_cafe.rpy:200-204` est donc inaccessible.
7. **Code mort** : la branche `neige_sur_toit` (l.1343-1352) est inaccessible, car le menu l.797 fixe toujours `arc4_limite_ilona`. Idem pour le `else` de `arc_5_examens.rpy:96`. Les lignes l.1103-1106 (« Et ton cadeau, je le veux » sous `cadeau_respirant` sans miniature) sont aussi inaccessibles.
8. **Miniature reconstruite** : avec `marche_silencieuse` + miniature, Ilona construit « une version de ton cadeau » (l.1297) sans l'avoir reçue ni vue dans cette branche (l.942). Incohérence mineure.
9. **Miniature dans le sac d'Ilona** : `arc_6_diplomes.rpy:221` montre la miniature dans son sac pour `miniature_souvenir` / `miniature_aveu`, même quand elle n'a pas été offerte (`demande_theo`, `marche_silencieuse`). À surveiller (hors périmètre arc 4).
10. **Commentaire du maid café** : « Seule soupape de pression du jeu » (`arc_4_5_maid_cafe.rpy:210`), alors que d'autres choix baissent aussi `pression_stream` (ex. l.310, 412). Il s'agit probablement de la seule soupape « hors choix » (interprétation).
11. **Exclusivité des 4.5** : elle découle des seuils de confiance (≥ 15 contre ≤ 8 puis −1), pas d'un test explicite. Aucune des deux ne se joue si aucune condition n'est remplie (cohérent avec la cartographie l.7).
12. **Décor Minecraft d'hiver** : il réutilise l'image d'été de l'arc 2 (placeholder probable).
13. **Le Messi** : l'origine du surnom est donnée par Allan avec « Probablement » (l.573-577). C'est une explication interne au jeu, pas une certitude du narrateur.
