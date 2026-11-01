# Notes — Route A (`arcs/arc_7/arc_7_jessy.rpy`)

Clé : `routeA`. Titre en jeu : « ARC 7 : LA RANDONNÉE » (`arc_7_jessy.rpy:139`). Labels : `arc_7_jessy` (131), `_scene_2` (240), `_scene_3` (332), `_scene_4` (466), `_scene_5` (581), `_scene_6` (779), `_scene_7` (907), `_nuit_retour` (1075), `_scene_8` (1109), `_fin_relation` (1182).

## Personnages

- **Jessy** (`j`) : planificateur (feuille « pliée en huit » avec trois itinéraires et variantes, 312-316, abandonnée 325) ; pose des torches pour s'occuper les mains (160-165). Avoue préparer les réponses d'Ilona « et appeler ça faire attention » (643). Garde sa veste des diplômes non lavée « à cause du col » (652-656).
- **Ilona** (`i`) : mange pour gagner du temps (254, 674) ; choisit son sac seule (201) ; tourne la carte de Jessy (379). Prend l'initiative de l'aveu (682) : « Je suis amoureuse de toi. J'aimerais essayer. »
- **Sofiane** (`s`) : AE86 blanche et noire du cousin (« Ne la déçois pas. », 263) ; inscription de boutique de tofu sur la portière (797) ; gobelet d'eau comme test de conduite (792-796) ; travaille au maid café (786 : collègues « déjà en uniforme de maid café », affiché quel que soit `arc4_5_sofiane_maid`).
- **Alexandre** (`x`) : pêche au lac avec la canne de son grand-père ; grands-parents de l'autre côté du lac (523). Rappelle château de sable avec cuisine, porte inutile, miniature de Noël (549-551).
- **Allan** (`a`) : trois paquets de biscuits (207) ; à Tokyo depuis trois jours, repart jeudi (912, 1023) ; a « traduit » Théo dix ans (990-994).
- **Théo** (`t`) : appartement à deux chambres, deuxième clé dans un tiroir (958-959) ; propriétaire l'appelle « Tao » (943) ; 32 min de trajet (955) ; appelle Laplage « le Messi » (950).
- **Laplage** (`laplage`) : sur un ours, torse nu (481) ; derrière un pin, « réarmement démographique » (755-761, si tente) ; au volant d'une berline argentée, cheveux blancs, moustache (865) ; « appel codec » nocturne si amitié (1088-1095).
- Personnages anonymes : « Une collègue », « L'autre collègue » (collègues de Sofiane, scène 6) — pas d'identifiant ajouté.

Citations :
- Jessy, aux courses : « C'est tout. Je mets des torches pour m'occuper les mains. » (163)
- Ilona, avant l'aveu : « Et dis pas oui pour me faire plaisir. Si c'est non, je préfère un vrai non. » (683)
- Alexandre au lac : « N'est-ce pas magnifique ? » (540)
- Sofiane après le drift avec Laplage : « Ce soir, il est venu voir. La prochaine fois, ce sera une course. » (894)
- Théo : « Si un jour j'ai quelque chose à lui dire, je le dirai moi-même. Sans traducteur. » (1054)

Tenues (sprites définis 10-29, 44-45) :
- Jessy `Rando/` (neutral_attentiveness, shy_warm_smile, happy, nervous_embarrassment) et `Rando/With_bag/` ; `listening` réutilise neutral_attentiveness, `determined` réutilise happy (commentaire 12).
- Ilona `Rando/` (neutral, playful_warm_smile, awkward_embarrassment, sad) et `Rando/With_bag/` (neutral_rando, playful_warm_smile, awkward_embarrassment ; `With_bag/sad.png` existe mais n'est pas déclaré).
- Laplage `Bear/` (Laplage_neutral, Laplage_thumb_up).
- Courses (scène 1) : Allan `beach`, Alexandre `winter` (tenue d'hiver en été), Sofiane `beach`, Ilona `tokyo`, Jessy `beach`. Tokyo (scène 7) : Allan `beach` (« tenues estivales de ville », 9-11), Théo `tokyo`.

## Lieux

- Maison Minecraft : `bg arc7 jessy minecraft` → `bg_arc7_jessy_minecraft.jpg` absent, secours `images/scenes/backgrounds/minecraft/bg_arc2_minecraft_house_summer_night.jpg`.
- Magasin de sport : `images/scenes/backgrounds/hiking/bg_arc7_jessy_boutique.jpg` (jingle `Decathlons jingle.mp3`).
- Départ, route, sentier : `hiking/bg_arc7_jessy_depart.jpg`, `_route.jpg`, `_sentier.jpg`.
- Embranchement à l'ours : `hiking/bg_arc7_jessy_sentier_ours.png`.
- Lac : `hiking/alexandre_peche_lac_ponton_vide.jpg`.
- Bivouac : `hiking/bg_arc7_jessy_bivouac.jpg` ; nuit `bg_arc7_jessy_nuit_tente_ferme.jpg` ; aube `bg_arc7_jessy_aube.jpg`.
- Tokyo : `tokyo/bg_arc7_tokyo_restaurant_night.jpg`, `tokyo/bg_arc7_tokyo_park_night.jpg` (définis dans `arc_7_theo.rpy:37-38`).
- Route de montagne de nuit, parking du maid café : uniquement en CG (`sofiane_initial_d`).

## Objets et concepts

- **Fruit étoilé** : jaune pâle, presque lumineux (372) ; goûté → noyau en étoile gardé dans la poche du sac (414), ressorti à l'aube (1157). C'est le 6e objet cosmique (Ilonanium).
- **Les six objets cosmiques** (`ilonanium_points += 1`) : bonbon étoile `arc_1_printemps.rpy:352`, gelée lumineuse `arc_2_plage.rpy:1137`, étoile en sucre `arc_3_rentree.rpy:1150`, mochi pailleté `arc_4_noel.rpy:687`, gâteau-planète `arc_6_diplomes.rpy:435`, fruit étoilé `arc_7_jessy.rpy:406`. Arc V : aucun point, clin d'œil si `>= 3` (`arc_5_examens.rpy:2556`).
- Veste des diplômes, trois mots au feutre sous le col (contenu non dit, 656).
- Carte tenue à l'envers (379, 460-462, 1171) ; Allan aussi à Tokyo (1038-1040).
- Puff-Puff (731) + son `coins_fucking.mp3` (769).
- Photo floue Allan/Théo à Tokyo (1063) ; « Dîner raté. Comme promis. » (1068).

## Mécaniques

- Écrites : `derniere_route = "Route Jessy"` (132) ; reset puis `arc7_jessy_fruit` (405/416), `arc7_jessy_dejeuner` (437/445), `arc7_jessy_relation` (688/713), `arc7_jessy_tente` (741/749, reset 1189), `ilonanium_points += 1` (406).
- Lues : `arc6_derniere_construction` (147-154), `arc4_5_sofiane_maid` (297), `arc5_cinema_ensemble` (619), `arc4_cadeau_jessy == "miniature_aveu"` (621), `arc6_offre_theo` / `arc6_conversation` (997-1016), `ilonanium_points` (1177).
- Entrée : `arc6_route == "jessy"` (`arc_6_diplomes.rpy:1757`), calculé par `arc6_calcule_verdict()` (`:44-84`, appelé `:160`) avec `SEUIL_JESSY = 180` (`script.rpy:401`).
- Sortie : saut automatique vers `ending_ilonanium` (Fin A3, prioritaire, sans menu) si `ilonanium_points == 6 and arc7_jessy_fruit == "goute"` (1176-1178) ; sinon `arc_7_jessy_fin_relation` (1180, 1182) : amitié → `ending_friend`, amour → `ending_family`, vide → `arc7_jessy_tente = False` et retour scène 5 (1183-1190).

## Chronologie

- Arc VI : décision dans la cour le 26 mars ; Théo part « dans onze jours » (`arc_6_diplomes.rpy:1737, 1819`), soit le 6 avril (confirmé 976).
- Scène 1 : « Quatre jours après les diplômes » (146) ; courses « le samedi suivant » (191) ; « Juin passe » (236), départ fixé au premier week-end libre de l'été.
- Scènes 2-6 : un samedi d'été, de sept heures du matin (247) à la nuit. Scène 7 : « Le même soir, à Tokyo » (911), Allan et Théo ne se sont pas parlé depuis trois mois (922). Scène 8 : dimanche à l'aube (1118-1120).
- Ellipses : « Une heure de marche plus tard » (473), « Quarante-cinq minutes de marche plus tard » (511), « Une heure plus tard » (590).

## Ressources

- CG : `images/scenes/cg/jessy_epopee/` 01 à 11, 13, 14, 15 (pas de 12) ; `cg/alexandre_fishing/` (3) ; `cg/sofiane_initial_d/` (14 plans, affichés comme `bg arc7 sofiane …`).
- Musiques : `Subwoofer-Lullaby.ogg` (mcnight), `shopping.ogg`, `morning_romance.ogg`, `rando.ogg`, `alex_peace.ogg`, `the-sunset.ogg` (randoNight), `spirit_of_the_night.ogg`, `bar_jazzy.ogg`, `night-walk.ogg` (citynight).
- Ambiances : `breeze-birds.mp3`, `river.mp3`, `lake.mp3`, `forest_night.mp3`.
- Sons marquants : `re-zero-return.mp3` (audio.laplage), `Bear.mp3`, `drift.mp3`, `AE86_engine.mp3`, `yesss_1.mp3`, `coins_fucking.mp3`, `sploush.mp3`, `aaughmp3.mp3` (audio.eating, quand Ilona goûte).
- Décors définis mais jamais affichés : `bg arc7 jessy riviere`, `fleurs`, `promontoire`, `belvedere`, `cafe`, `nuit` (fichiers propres absents, secours seulement). Sprites définis non utilisés : `jessy rando bag determined`, `jessy rando bag listening`.

## Incertitudes et contradictions

- `audio.car_stop` joué en 782 n'est pas défini (seul `define audio.carStop`, 126). Risque d'erreur à l'entrée de la scène 6, sauf si le nommage automatique de Ren'Py couvre `audio/fx/car_stop.mp3` (non vérifié).
- `define audio.engineStart = "audio/fx/AE86_engine_start.mp3"` (124) alors que le fichier sur disque est `AE86_Engine_Start.mp3` : fonctionne sous Windows (insensible à la casse), risque sur build archivé ou système sensible à la casse.
- `sofiane_ae86_route_nuit_collegues_euphorie` : le code charge la version `.png` (79) alors qu'une `.jpg` existe aussi.
- Historique : une version antérieure proposait un menu final « Quel chemin suivent-ils après la montagne ? » (« Un dernier chapitre : Ilonanium. » / « Continuer la vie qu'ils ont choisie ensemble. ») quand la condition Ilonanium était remplie (remplacé par un déclenchement automatique, 1176-1180).
- Commentaire d'en-tête (2) : « le fruit ouvre Ilonanium » — en réalité il faut le fruit et 6 points.
- Cartographie `agents/cartographies/arc_7.md` : parle d'« aéroport » et de « kissaten » ; le script dit gare (158, 976-981) et « restaurant » (917).
- Scène 6 : les collègues sont en uniforme de maid café même si le joueur n'a pas découvert ce secret (`arc4_5_sofiane_maid` faux) ; information pour le joueur seulement (cf. `cartographies/ending_family.md`).
- Doc `systeme de points.md` nomme « gelée marine » et « mochi cosmique » ; script : « gelée lumineuse », « mochi pailleté » (variable `arc4_mochi_cosmique`).
