# Notes — Fin A3 (`arcs/endings/ending_ilonanium.rpy`)

Clé : `finA3` (fin secrète). SPECIAL ENDING ILONANIUM ; générique « Le berceau de l'humanité » (`ending_ilonanium.rpy:886-887`). Quatorze scènes (en-tête 2) : `ending_ilonanium` (175), `_silence` (212), `_chez_elle` (235), `_bascule` (269), `_catastrophe` (314), `_deux_soleils` (377), `_survivants` (470), `_bar` (515), `_conseil` (560), `_celui_qui_reste` (639), `_adieux` (711), `_promesse` (771), `_reconquete` (827), `_alexandre` (870). Aucun menu ; `record_ending("ilonanium")` (176).

## Personnages

- **Ilona** : malade le lendemain (188-200), attire les objets (257-261) ; le fruit étoilé était « le dernier qu'il manquait » (285-290) ; devient l'astre Ilonanium (361-364). Voix intérieure qui guide Jessy : « Jessy… Retrouve-moi. » (489). Sprite `Ilona/illonanium/sick.png`.
- **Jessy** : fonde le culte de Laplage, prophète (487) ; ne vieillit pas, croit que c'est Ilona qui l'en empêche (592) ; reste 999 ans pour faire construire le TAIKUN (657-674) ; revient en robe blanche et longue barbe (783). Tenues `illonanium/beach_*`, `priest_*`, `prophet_*`.
- **Monsieur Laplage** : sauve un dixième de l'humanité avec le TARDIS (339-365) ; révèle être Théo venu du futur (398) ; dans sa vie, Ilona s'est donné la mort à cause de lui (402-403) ; pouvoirs reçus d'un vieil homme à son visage sur une plage terrestre (409) ; transmet le porte-clés creeper (413-419) ; part « marcher un peu » (454). Tenues `illonanium/exhausted`, `farewell`, `farewell_no_creeper`, `neutral`.
- **Théo** : vieilli (`older_*`), puis en tenue « Laplage » après la transmission (`laplage_*`) ; décide de sauter 999 ans dans le futur (443-448) ; appelle le TARDIS (751-754).
- **Allan** : PDG de Muchacho Corporation et Gringos Industry (506) ; tenues `ceo*`, `military_commander`.
- **Micka** (`mi`) : gouverneur de l'humanité, « gigachad de la Légion d'honneur » (479-481) ; recherches sur l'infertilité ; « mes femmes » (691). Tenues `governor_*`, `armor_commanding`.
- **Sofiane** : « l'ange de la route » ; a battu Laplage à la course ; sa Trueno a reçu un fragment du pouvoir de Laplage et sert de base au moteur du TAIKUN (497-499, 608-614). Tenues `older_civilian_*`, `armor_focused`.
- **Florentin** (`ilonanium_florentin`, couleur `#cf8671`, 121) : commandant de la milice, plus grande armée de l'humanité ; sa femme est restée sur Terre (544-547, 624). Sprites `Florentin/illonanium/armor_angry`, `armor_resolved` (`futuristic_armor` déclaré, non affiché).
- **Alexandre** : resté sur Terre (356) ; vivant sur l'Ilonanium, dans une maison au toit de chaume (874-877).
- Anonymes : « Messagerie » (219), « La foule », « Une voix » (780-781).

Citations :
- Laplage : « Laissez digérer. » (369)
- Laplage à Théo : « Vous. Avec beaucoup de retard. » (398)
- Laplage : « Réussis là où j'ai échoué. Le prochain, c'est toi. » (418)
- Théo à Jessy : « Pour toi, mille ans. Pour nous, quelques secondes. » (743)
- Alexandre : « N'est-ce pas magnifique ? » (877)

## Lieux

- Chambre de Jessy : `images/scenes/backgrounds/friend/bg_friend_chambre_jessy.png` (réutilisée).
- Rue d'Ilona : `hiking/bg_arc7_jessy_depart.jpg` (`bg ilonanium rue`) ; chambre : `friend/bg_friend_chambre_ilona.png`.
- Plage à deux soleils : `backgrounds/ilonanium/plage_deux_soleils.png` ; plage reconstruite / exoplanète : `images/scenes/illonanium/plage_exoplanete.png`.
- Bar d'Allan : `illonanium/bar.png` ; bureau du gouverneur : `illonanium/governor_office.png` ; Capitole : `illonanium/capitole_depart.png`, `capitole_retour.png`.
- Espace : `illonanium/taikun_orbite.png`, `fin_ilonanium0.png` (TAIKUN devant l'Ilonanium), `passerelle_taikun.png`, astre `cg/ilonanium/12_ilonanium.png`.
- Maison d'Alexandre : `illonanium/fin_ilonanium1.jpg`, `fin_ilonanium2.jpg`.

## Objets et concepts

- Six objets cosmiques (voir notes Route A) ; le noyau étoilé traverse le sac (285).
- TARDIS (cabine bleue), porte-clés creeper (commande le TARDIS), nœuds de convergence : voyages en aller simple, dates ressenties ; dernier il y a plus de 41 ans, prochains dans un mois, dix ans, puis 999 ans et un mois (427-440).
- TAIKUN : station annulaire autonome (604) ; moteur tiré de la Trueno, « en V8000 » (613-614).
- Culte de Laplage, prophétie du retour du Messi et de ses apôtres (680) ; symbole du pouce levé (779).
- Photo Théo/Ilona d'une autre vie (`theo_ilona_picture.png`, animation `ilonanium_photo_lancer`, 54-68, 392).

## Mécaniques

- Lues : `arc7_jessy_relation` (193-199, 301-306, 593-596).
- Écrite : `endings_seen` via `record_ending("ilonanium")`.
- Condition d'accès : `ilonanium_points == 6 and arc7_jessy_fruit == "goute"` → `jump ending_ilonanium` automatique, sans menu, prioritaire sur A1/A2 (`arc_7_jessy.rpy:1176-1178`). Points : `arc_1_printemps.rpy:352`, `arc_2_plage.rpy:1137` (option si `arc2_retour_minecraft != "porte_fermee"`), `arc_3_rentree.rpy:1150` (menu si `arc3_fin_minecraft != "destruction"`), `arc_4_noel.rpy:687`, `arc_6_diplomes.rpy:435`, `arc_7_jessy.rpy:406`.
- Helper `ilonanium_asset(chemin, secours)` (6-8) : fichier s'il existe, sinon secours.
- Test : `game/tests/ilonanium.rpy` (relations amour et amitié, CG sans sprites superposés).

## Chronologie

- Samedi : fruit mangé (287). « LE LENDEMAIN DU RETOUR » (181) ; « MARDI » (215).
- « QUARANTE ANS PLUS TARD » (378) ; « TROIS JOURS PLUS TARD » (555) ; « VINGT-SEPT JOURS PLUS TARD » (714).
- « NEUF CENT QUATRE-VINGT-DIX-NEUF ANS PLUS TARD » (772) ; traversée de cinq ans (822).
- « MILLE QUARANTE-QUATRE ANS APRÈS LA CATASTROPHE » (828) = 40 + 999 + 5 (plus environ un mois).

## Ressources

- CG `images/scenes/cg/ilonanium/` : 01 à 11, 12_ilonanium, 13_adieux_laplage, 13_reconquete_espoir, 14_calin_jessy_theo, 14_transmission_adieux, 15_depart_tardis, 15_preparatifs_taikun, 16_jessy_survivants, theo_ilona_picture (tous `.png`).
- Musiques : `Subwoofer-Lullaby.ogg`, `tense-piano.ogg`, `Majula.ogg`, `spring-hope.ogg`, `bar_jazzy.ogg`, `truth-piano.ogg`, `melancolique-piano.ogg`, `alex_peace.ogg`.
- Secours effectifs : `audio/music/ilonanium_across_the_void.ogg` absent → aucune nouvelle piste, `tense-piano.ogg` continue (318-319) ; `ilonanium_vanirs_legacy.ogg` absent → `audio/music/spring-hope.ogg` (831) ; `ilonanium_roundabout.ogg` absent → `audio/music/alex_peace.ogg` (872). Les crédits IXION et Yes ne s'affichent pas (890-895).
- Ambiances/sons : `breeze-birds.mp3`, `crowd-noise.mp3`, `re-zero-return.mp3`.
- UI : `images/ui/ilonanium_to_be_continued.svg` (écran `ilonanium_to_be_continued`, 106-119) ; transformation sépia `ilonanium_jojo_sepia` (93-95).

## Incertitudes et contradictions

- `images/ui/ilonanium_to_be_continued.svg` n'est pas vide : 244 octets, un seul `<path>` (bandeau flèche) ; le texte « TO BE CONTINUED » est dessiné par l'écran Ren'Py. Prise en charge du SVG par la version de Ren'Py utilisée non vérifiée.
- Doc `agents/illonanium/Fin ilonanium.md` : Ilona sort et mange la baie au début de la fin ; le script la fait manger pendant la randonnée (`arc_7_jessy.rpy:404-414`, commentaire `ending_ilonanium.rpy:3`). Doc : « Laisser digérer » + pouce levé ; script : « Laissez digérer. » sans pouce (369).
- Sprites déclarés non affichés : `laplage ilonanium thumb_up`, `micka ilonanium armor` (sci_fi_armor), `jessy ilonanium prophet` (with_gem), `sofiane ilonanium armor` (tactical), `florentin ilonanium armor` (futuristic), `theo ilonanium older` (older_neutral).
- Dossiers de décors à l'orthographe double : `scenes/illonanium/` et `backgrounds/ilonanium/`, `personnages/*/illonanium/` vs `cg/ilonanium/`.
- Micka parle de « mes femmes » (691), alors que la Fin A2 le marie à Claire Martin : fins indépendantes, pas une contradiction de continuité.
- Une version antérieure de la Route A proposait un menu « Continuer la vie qu'ils ont choisie ensemble. » ; supprimé, la Fin A3 est désormais automatique (`arc_7_jessy.rpy:1176-1180`).
