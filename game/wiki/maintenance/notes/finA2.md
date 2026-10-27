# Notes — Fin A2 (`arcs/endings/ending_family.rpy`)

Clé : `finA2`. GOOD ENDING FAMILY ; générique « Jessy et Ilona / Les Petits Sommets » (`ending_family.rpy:1134-1135`). En-tête : « GOOD ENDING (FAMILY) - JESSY ET ILONA » (1). Labels : `ending_family` (74), `_restaurant` (84), `_visite` (178), `_chez_nous` (353), `_premier_matin` (380), `_preparatifs` (494), `_retrouvailles` (534), `_repas` (612), `_fete` (779), `_depart` (893), `_annonce` (983), `_lucy` (1037), `_generique` (1132). Aucun menu ; `record_ending("family")` (75).

## Personnages

- **Jessy** : en couple avec Ilona ; signe la cession (299) ; « Je l'aime. Je vais faire de mon mieux. » (310) ; tenue `papa` dans l'épilogue (55, 1029).
- **Ilona** : veut vivre « là-haut, dans les montagnes » (112) ; la randonnée est « le plus beau moment de ma vie » (115) ; garde son bureau, ses jeux, ses streams (259, 758) ; nomme le restaurant (370) ; annonce la grossesse (1007) ; enceinte d'Oliver dans l'épilogue (1076-1078).
- **Monsieur Laplage** : propriétaire, donne restaurant et maison (279-282) ; adieux définitifs : « Je peux me reposer en paix, désormais. » (343), « Ils ne reverront jamais Monsieur Laplage. » (347). Probable « voix au téléphone » (150-159, interprétation : Jessy reconnaît la voix, puis Laplage ouvre).
- **Sofiane** : chauffeur (Trueno, deux rotations) ; cousin lui laisse la Trueno un an de plus (657) ; coca, conduit (792-798).
- **Théo** : a repris contact et s'est excusé auprès d'Ilona (582-583) ; Baka Mitai (854-862) ; battle Yakuza 0, Majima (869).
- **Micka** (`mi`) : bouquet énorme (614-623) ; marié à **Claire Martin**, ancienne prof d'anglais (706-723 ; personnage mentionné, absent).
- **Allan** : boutique d'informatique (645). **Alexandre** : prépare sa rentrée, deuxième feuille pêchée (650-654), dessin encadré de la première maison Minecraft (632).
- **Lucy** (`family_lucy`, couleur `#f4d183`, 65) : fille de Jessy et Ilona, sprites `Lucy/neutral.png`, `happy.png` (canvas 576×864, 63-64).
- **Oliver** : enfant à naître, nommé seulement (1086-1091, générique 1136). Pas de sprite.
- Anonyme : « La voix au téléphone » (150-154).

Citations :
- Laplage : « Je vous ai entendus dans la cuisine. Vous aviez déjà faim de demain. » (286)
- Ilona : « Les Petits Sommets. […] Et on peut y arriver même quand on est nuls avec une carte. » (370-372)
- Lucy : « Oliver ! La sortie, c'est pas par là ! » (1091)
- Narration finale : « Ils vécurent heureux et eurent beaucoup d'enfants. » (1128)

Tenues (31-64) : Ilona `Summer` (rendez-vous, visite), `House` (maison, annonce), `House/pregnant` (épilogue), `Party` (soirée) ; Jessy `Beach` au quotidien (pas de tenue summer/house ; `Beach/surprised.png` ajouté pour l'annonce), `Party`, `Papa` ; Allan, Alexandre, Sofiane, Théo, Micka en `Party` (Micka `flowers` puis `neutral`).

## Lieux

- Restaurant en ville : `images/scenes/backgrounds/family/bg_family_rendezvous.jpg`.
- Route : `hiking/bg_arc7_jessy_route.jpg` (réutilisé).
- Les Petits Sommets : cour `family/bg_family_restaurant_jour.jpg`, `_soir.jpg`, `_nuit.png` ; salle `bg_family_salle.jpg`, `bg_family_fete.jpg`, `bg_family_fete_fin.png`, `bg_family_fete_rangement.png`, `bg_family_karaoke.png` ; maison `bg_family_maison.jpg` ; jardin `bg_family_jardin_jour.jpg`, `bg_family_jardin_soir.jpg`.
- Restaurant décrit : toit de tuiles grises, rideau vert, grand arbre, maison attenante avec pièce en tatamis, sentier vers la forêt et le lac (201-202, 255, 369).

## Objets et concepts

- Annonce identique trouvée par les deux, pouce flou sur la photo (126-132).
- Clés : Jessy en détache une pour Ilona (314) ; restées près du pot de confiture (489).
- Nom du restaurant : Les Petits Sommets (370) ; lundi fermé (295-297, 529).
- Dessin encadré d'Alexandre au-dessus du comptoir (632-637).
- Petit verre au canard (1065, 1118).

## Mécaniques

- Écrite : `endings_seen` via `record_ending("family")`.
- Lue : `arc4_5_sofiane_maid` (661-682).
- Helper `family_music(chemin, secours)` (6-8) : renvoie le fichier s'il est chargeable, sinon le secours.
- Entrée : `arc7_jessy_relation == "amour"` (`arc_7_jessy.rpy:1185-1186`), tente ou hamac indifférent, si la Fin A3 automatique (1177-1178) ne s'est pas déclenchée.

## Chronologie

- « QUELQUES JOURS APRÈS LA RANDONNÉE » (79) ; « LE LENDEMAIN » (181), visite à 14 h ; emménagement « quelques jours plus tard » (384), premier matin le lendemain (389) ; « Les jours suivants » (499).
- « UN MOIS PLUS TARD » (538) : soirée de retrouvailles.
- « QUELQUES JOURS PLUS TARD » (984), un lundi (991) : annonce.
- « Plusieurs années plus tard » (1038) : Lucy, Ilona enceinte d'Oliver.

## Ressources

- CG : `images/scenes/cg/family/cg_family_laplage_adieux.png`, `cg_family_pancakes_01.png`, `cg_family_pancakes_02.png` (déclarés comme `bg family pancakes rate/reussi`), `cg_family_toast.png`, `cg_family_entrance_kiss.png`, `cg_family_lucy_hug.png`, `cg_family_homecoming.png`.
- Musiques : `resto_jazz.ogg` (restojazz, défini dans `arc_7_theo.rpy:23`), `rando.ogg`, `morning-piano.ogg`, `love-piano.ogg`, `bar_jazzy.ogg`, extrait 22-58 s de `Baka_Mitai.ogg` (854), `real-love.ogg`, `spring-hope.ogg`.
- Secours effectifs : `audio/music/family_save_the_world.ogg` absent → `audio/music/spring-hope.ogg` (1032) ; `audio/music/family_hopes_dreams_save_last_goodbye.ogg` absent → `audio/music/real-love.ogg` (1133), et le carton de crédits Undertale (1138-1139) ne s'affiche pas.
- Sons : `car_go.mp3`, `bell.mp3`, `AE86_engine.mp3`, `AE86_Engine_Start.mp3` (via `audio.engineStart`, casse différente).

## Incertitudes et contradictions

- `audio.engineStart` pointe vers `AE86_engine_start.mp3`, fichier réel `AE86_Engine_Start.mp3` (940) : voir notes Route A.
- Titre « officiel » : le jeu n'affiche pas de titre de fin distinct ; « Les Petits Sommets » vient du générique (1135). Choix éditorial.
- Commentaires du fichier numérotés 1 à 9 alors qu'il y a 11 labels de scène (premier matin et préparatifs non numérotés).
- Micka dit « On a tous fini le lycée en même temps » (714) à propos de sa femme, ancienne prof : formulation humoristique, non clarifiée.
