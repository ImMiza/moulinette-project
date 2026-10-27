# Notes — Arc V (`arc5`)

Source : `game/arcs/arc_5/arc_5_examens.rpy` (2620 lignes). Labels `arc_5_examens` (l.48) et `arc_5_scene_3` (l.908). Entrée : `arc_4_noel.rpy:1373` (`jump arc_5_examens`). Sortie : `jump arc_6_diplomes` (l.2620). Titre affiché : « ARC 5 : JANVIER MANGE LES GENS DE L'INTÉRIEUR » (l.53). Thème d'en-tête : « Connaître les goûts de quelqu'un ne veut pas dire savoir ce qu'il veut. » (l.2).

## Personnages

**Jessy** — protagoniste, narration en focalisation interne. Il se sent inutile face à Théo (l.152). Il avoue ne pas savoir distinguer « demander comment ça va » et « réparer » (l.336-343). En hiver, il porte le sprite `jessy winter` (scènes 2 et 6) ; dans Minecraft, `jessy minecraft`.
- « En pratique, je ne sais pas faire la différence. » (l.343, à Allan)
- « Je peux essayer de le penser assez fort pour que ce soit vrai même quand j'ai peur. » (l.1425, Saint-Valentin, amitié + demande)

**Ilona** — épuisée et amaigrie (« ses pulls flottent », l.87), elle a manqué deux jours de cours (l.748). Elle refuse d'être « réparée », ce qui rappelle Noël (l.337). La narration la montre avec un projet de stream encore latent (pseudo finissant par « Gaming » depuis ses 12 ans, l.970 ; à confirmer avec les autres arcs). Elle porte en hiver un sprite variable (`arc4_ilona_winter_sprite`, l.375, 1648).
- « Tu ne demandes pas. Tu vérifies. » (l.175, scène 1)
- « Qu'on me foute la paix. » (l.1596, confidence distante)
- « Je veux juste pouvoir finir une phrase de temps en temps. » (l.1566, confidence fragile)
- « Essayer, c'est déjà beaucoup. » (l.1946/1960/1973)

**Théo** — il apporte le bon thé (l.133-136), a « les notes les plus complètes du groupe » (l.780) et propose de « gérer » (l.944-950). Il connaît des détails intimes sur Ilona, qu'il classe « comme les pièces d'un dossier » (l.977). Il surnomme Laplage « le Messi » et « le GOAT des conseils cryptiques » (l.735-737). Sprite hiver variable (`arc4_theo_winter_sprite`, l.726).
- « Ce n'est pas un secret, Jessy. C'est juste que personne ne regarde. » (l.974)
- « Calculer, c'est pour soi. Optimiser, c'est pour le résultat. » (l.1110)
- « Jessy. Je ne suis pas ton ennemi. » (l.846)

**Allan** — il connaît Théo « depuis le collège » (l.885) et commence à s'en méfier (l.890-898, 2321-2332). Il « traduit » Théo : quatre fois ce mois-ci (l.2354-2355). Il reçoit un message d'Ilona : « T'es pas obligé de toujours tout expliquer. » (l.2353). Réplique : « On devrait faire des t-shirts « Progrès émotionnel en cours ». » (l.820).

**Alexandre (`x`, sprite `alex`)** — il fait un planning de révisions « organisé comme un bâtiment » (l.79). Il envoie trois chocolats à Jessy sous pseudonymes, le troisième signé « Ta fan mystérieuse, bisous, Alexandre, PS : c'est moi » (l.1251). Il réagit en majuscules aux histoires de Micka. « C'était techniquement correct et émotionnellement insupportable. » (l.71) ; « un crime organisé contre le beurre » (l.2017).

**Monsieur Laplage** — badges « Consultant en Entropie Émotionnelle » (l.247) et « Archiviste des Non-dits » (l.1491) ; pouce levé (l.262), pouce horizontal (l.1618) ; son FX = `audio/fx/re-zero-return.mp3`.
- « Les étoiles qui ne se reposent jamais finissent par s'effondrer sur elles-mêmes. » (l.255)
- « Les gens confondent souvent être proche et être propriétaire. » (l.1587)
- « Les étoiles qui demandent la permission avant de briller... ne brillent jamais. » (l.1616)

**Sofiane (`s`)** — son cousin part à l'armée et lui confie une AE86 « comme dans Initial D » (l.2405-2407). Il a le permis depuis six mois sans l'avoir dit (l.2409) et projette un été dans les montagnes (l.2415). « Les étoiles parlent à ceux qui savent se taire. » (l.2428).

**Micka (`mi`)** — **première apparition dans le jeu** : `define mi = Character("Micka", color="#e91e63", …)` (l.35). Garçon (« Il ne les ramasse pas », l.1200). Il reçoit énormément de chocolats, y compris de trois professeures (l.1188), et a cessé de compter à 42 (l.2020). Il fait 37 gâteaux pour le White Day (l.2015). La prof d'anglais lui a donné son prénom et son numéro (l.2038). Ton flegmatique, inconscient du sous-entendu. « L'ironie, c'est de l'affection mal exprimée. » (l.1209). Sprites : `micka gifts` (S4), `micka exhausted` (S7) ; `micka happy` est déclaré l.37 mais utilisé seulement dans l'Arc VI (`arc_6_diplomes.rpy:379`). Son entrée s'accompagne d'applaudissements (`audio.micka` = `audio/fx/ApplauseClapping.mp3`). Pas de page dédiée : rattacher à `personnages/autres/`.

**Personnages seulement cités (sans sprite ni réplique)** : Madame Tanaka, prof de maths (l.1186) ; Madame Yamamoto (l.2026) ; la prof d'anglais (l.1211, 2027) ; la prof de sport (l.2051) ; la caissière du cinéma (l.408) ; le cousin de Sofiane (l.2405). Aucun identifiant de personnage n'est nécessaire.

## Lieux

| Lieu | Scènes | Décor (`image` résolue) |
|---|---|---|
| Bibliothèque (jour) | 1 | `images/scenes/backgrounds/school/bg_arc5_library.jpg` (`bg arc5 library`, l.20) |
| Bibliothèque (soir) | 3, 5 | `images/scenes/backgrounds/school/bg_arc5_library_night.jpg` (l.21) |
| Rue sous la pluie / devant le cinéma | 2, 9 | `images/scenes/backgrounds/city/bg_arc5_rain_street.jpg` (l.23) |
| Cinéma : hall, salle, sièges | 2 (version cinéma) | `bg_arc5_cinema_box_office.jpg`, `bg_arc5_cinema_auditorium.jpg`, `bg_arc5_cinema_seated.jpg` (l.26-28, `images/scenes/backgrounds/city/`) ; le dernier montre déjà Jessy et Ilona assis (commentaire l.430) |
| Café | 2, 8 | `images/scenes/backgrounds/city/bg_arc5_cafe.jpg` (l.22) |
| Salle de classe | 4, 7 | `images/scenes/backgrounds/school/bg_arc5_classroom.jpg` (l.24) |
| Toit du lycée | 4 | `images/scenes/backgrounds/school/bg_arc5_rooftop.jpg` (l.25) |
| Gare (quai) | 6 | `images/scenes/backgrounds/transport/bg_arc5_train_station.jpg` (l.31) |
| Parc près de la gare (cerisiers) | 7 | `images/scenes/backgrounds/city/bg_arc5_park_spring.jpg` (l.29) |
| Maison Minecraft (nuit) | 10 | `images/scenes/backgrounds/minecraft/bg_arc2_minecraft_house_summer_night.jpg` (réutilisé, `bg arc5 minecraft night`, l.30) |

## Objets et concepts

- **Stylo violet à étoiles** : trouvé sous la chaise d'Ilona (l.350), « Il le lui rendra demain » (l.351) ; toujours dans la poche au café (l.646). Jamais rendu dans l'arc ; repris dans l'Arc VI (`arc_6_diplomes.rpy:178` « depuis le 12 janvier ») et sur la Route B (`arc_7_theo.rpy:960-966`).
- **Le thé d'Ilona** : celui qu'elle prend « quand elle est à bout » (l.135) ; renvoie au thé choisi au maid café (l.140, variante `accepte`).
- **Stream d'Ilona** : projet que Théo révèle ou rappelle (l.946-977). Il est évoqué dans la confidence à Laplage (l.1517).
- **Chocolats-blocs Minecraft** (l.1274), **chocolats d'amitié** (l.1303).
- **Album photo** « qui pèse trois kilos » (l.2149-2159).
- **Phrase coupée par le train** : « Ilona, je voulais te dire que— » (l.1696, 1732). L'origine est `arc_1_printemps.rpy:260`.
- **Maison Minecraft** : salle de repos « reliée, mais séparée » (l.2473) ; panneau « BESOIN D'AIR » devant la salle secrète (l.2527-2528) ; mot de passe du serveur donné à Théo (l.2516).
- **Événement caché « traînée cosmique »** (l.2554-2564) : condition `ilonanium_points >= 3 and arc5_valentin_choix == "demande"`. Le commentaire précise qu'il ne donne aucun point. Lien avec la Fin A3 : ne le mentionner que sous Spoiler `finA3`.
- **AE86** du cousin de Sofiane (l.2407). Elle annonce la Route A (`arc_7_jessy.rpy:77-96`) et la Fin A3 (`ending_ilonanium.rpy:499`).
- **Festival de printemps** cité par Théo (l.945).

## Mécaniques

**Variables propres (default l.5-18)** : `arc5_sortie_annulee` (silence/honnetete/inquiet/confronte/accepte), `arc5_theo_proposition` (partiel/laisse/refuse/questionne), `arc5_valentin_offre` (ambigu/amitie/rien), `arc5_valentin_choix` (rien_peur/souvenir/simple/demande), `arc5_question_reponse` (responsable/theo/temps/honnete), `arc5_white_day_reponse` (grand_geste/espace/retour/mots), `arc5_fin_minecraft` (salle_repos/distance/theo_presence/panneau/neutre), `arc5_laplage_deuxieme_confidence`, `arc5_allan_voit_theo`, `arc5_allan_parti_cafe`, `arc5_tension_accumulee`, `arc5_theo_dans_maison`, `arc5_cinema_ensemble`, `arc5_etat_relation`.

**Globales écrites** : `autonomie_ilona`, `confiance`, `communication`, `influence_theo`, `jalousie`, `lien_jessy_ilona`, `controles`, `evitements`, `pression_stream`, `interruptions_ilona` (+1 seulement l.180), `jugement_laplage` (l.1064, 1414, 1889, 1913), `confidences_laplage` (l.1554, 1585), `maison_minecraft_ajouts`, souvenirs via `remember()` (`ilona_libre_sans_abandon` l.595/1435/2171, `jessy_nomme_sa_peur` l.1751/1884/1908, `theo_utilise_une_verite` l.1822, `maison_respectee` l.2467).

**Lues depuis les arcs précédents** : `arc4_fin_minecraft` (l.89), `arc4_ilona_avec_theo` + `arc4_5_ilona_reaction` (l.100, 138, 752, 988, 2106), `arc4_5_theo_proposition` (l.103, 946, 996, 1021, 1048, 2156), `arc2_photo_reaction == "silence_photo"` (l.649), `arc2_choix_activite_theo == "suivre"` (l.862), `arc4_cadeau_jessy` / `arc4_limite_ilona` (l.2092-2104), `arc3_fin_minecraft` (l.2454-2461), `ilonanium_points` (l.2556).

**Seuils internes** :
- Cinéma : `(lien_jessy_ilona >= 20 or autonomie_ilona >= 30) and confiance >= 15 and communication >= 20` (l.374). Effets : lien +1, confiance +1, `arc5_cinema_ensemble = True`, puis `jump arc_5_scene_3` (l.501-506).
- Question de Théo : `arc5_sortie_annulee == "confronte" or jalousie >= 12` (l.851) → `arc5_allan_voit_theo = True`.
- Avertissement d'Allan : `(arc5_allan_voit_theo or influence_theo >= 10) and not arc5_allan_parti_cafe` (l.879).
- Remarque d'Alexandre : `arc5_sortie_annulee == "confronte" or arc5_tension_accumulee >= 4` (l.1155) ; « On devrait peut-être parler » : `arc5_tension_accumulee >= 3` (l.1259).
- Offre de la Saint-Valentin : ambigu si lien ≥ 20 et confiance ≥ 15 (l.1272) ; amitié si lien ≥ 10 et confiance ≥ 8 (l.1297) ; sinon rien.
- `arc5_etat_relation = etat_relation()` est figé à la ligne 1510 (`script.rpy:283-323`). Calcul : indice = espace − dette. Le résultat est `distant` si contrôle non réparé ≥ 3. Il est `proche` si indice ≥ 200 et écoute (`ilona_peut_finir_ses_phrases + interruptions_reparees`) ≥ 4. Il est `fragile` si indice ≥ 40, sinon `distant` (`script.rpy:414-416`).
- `confidences_laplage += 1` si fragile (l.1554) ou distant (l.1585).
- Option « honnete » : texte différent selon `arc5_etat_relation == "proche"` ou non (conditions d'option l.1882, 1906).
- Bonus du White Day : `(espace|mots) and (honnete|responsable)` → confiance +1, lien +1 (l.2268).
- Fin Minecraft (if/elif l.2463-2552) : `honnete` + (espace|mots) → salle_repos ; `theo` → distance ; `laisse` + `arc5_theo_dans_maison` → theo_presence ; `grand_geste` → panneau ; sinon neutre.

**Relu plus loin (vérifié)** :
- `arc5_cinema_ensemble` : `arc_6_diplomes.rpy:754, 1013` ; `arc_7_jessy.rpy:619`.
- `arc5_question_reponse` : `arc_6_diplomes.rpy:754, 1041-1085, 1916, 1926`.
- `arc5_theo_proposition` : `arc_6_diplomes.rpy:115-118` ; `arc_7_theo.rpy:1098-1105`.
- `arc5_fin_minecraft == "theo_presence"` : `arc_6_diplomes.rpy:224` ; `arc_7_theo.rpy:1057`.
- `arc5_tension_accumulee >= 8` (ou `pression_stream >= 12`) : vignette « craquage », `arc_6_diplomes.rpy:1236`.
- Souvenirs : score de posture, `arc_6_diplomes.rpy:63-69`.
- Non relues hors de l'arc : `arc5_sortie_annulee`, `arc5_valentin_offre`, `arc5_valentin_choix`, `arc5_white_day_reponse`, `arc5_etat_relation`, `arc5_allan_*`, `arc5_laplage_deuxieme_confidence`, `arc5_theo_dans_maison`. `jugement_laplage` n'est relu par aucune condition dans les scripts. Les ajouts `*_arc5` de `maison_minecraft_ajouts` ne sont jamais relus.

## Chronologie

- 12 janvier : révisions (l.57), neige dehors.
- Une semaine plus tard : sortie au cinéma ou annulation, sous la pluie (l.359).
- Février : fin des examens et résultats (l.913-918).
- 14 février : Saint-Valentin (l.1133).
- « Quelques jours plus tard » : confidence à Laplage (l.1479). Le lendemain : la gare (l.1640), en février d'après l'Arc VI (`arc_6_diplomes.rpy:1048`).
- 14 mars : White Day (l.1990) ; premiers cerisiers (l.2073).
- Le même jour ou peu après : café Allan/Alexandre, Sofiane, Minecraft ; « Le printemps s'installe » (l.2593). L'Arc VI commence fin mars (`arc_6_diplomes.rpy:171`).

## Ressources

- **CG** : `images/scenes/cg/theo/bg_arc6_evil_theo.jpg` (`bg arc6 evil theo`, déclaré `arc_6_diplomes.rpy:152`), affiché 5 s avec `audio.sirene` = `audio/fx/prowler_sound.mp3` si `laisse` (l.1121-1126).
- **Musiques** : `audio/music/library.ogg` (`audio.lib` l.50 ; `audio.library` l.914, 1475 — voir incertitudes), `city-rain.ogg`, `cafe.ogg`, `sad-piano.ogg`, `saintv.ogg` (`audio.saintV`, l.41), `ecole-roof.ogg`, `ecole-nuit.ogg`, `truth-piano.ogg`, `tense-piano.ogg`, `spring-hope.ogg`, `melancolique-piano.ogg`, `love-piano.ogg`, `Subwoofer-Lullaby.ogg` (`audio.mcnight`). Musique du cinéma : `audio/ambience/the_city_mouse_and_the_country_mouse.mp3` (`audio.arc5Cinema`, l.33), jouée sur le canal musique.
- **Ambiances** : `audio/ambience/rain.mp3`, `rain-inside.mp3` (l.42), `winter-wind.mp3` (l.43), `breeze-birds.mp3`.
- **Sons** : `audio/fx/MGS-Ringtone.mp3` (SMS d'annulation, l.508), `train-passing.mp3`, `train-stop.mp3` (Ilona part, l.1877), `ApplauseClapping.mp3` (Micka), `re-zero-return.mp3` (Laplage).
- **Sprites de Micka** : `images/personnages/Micka/happy.png`, `exhausted.png`, `happy_with_gifts.png` (l.37-39).

## Incertitudes et contradictions

1. **Doc ≠ script (nombre de lignes)** : la cartographie (`agents/cartographies/arc_5.md`) annonce 2611 lignes ; le fichier en compte 2620.
2. **Doc ≠ script (`confidences_laplage`)** : `agents/systeme de points.md` (l.46) affirme que les trois occurrences sont conditionnées par `ilona_peut_finir_ses_phrases < 2 / < 4 / < 6`. Dans l'arc 5, l'incrément dépend de `arc5_etat_relation` (fragile/distant, l.1554 et 1585), et il y a deux incréments exclusifs l'un de l'autre.
3. **Café, branche `inquiet`** : la chaîne if/elif (l.672-724) ne traite pas `inquiet`. Allan répond alors « Tu mens » à « Rien de spécial », alors que Jessy a en réalité demandé « Tu es sûre que ça va ? ».
4. **Remarque d'Alexandre (l.1155-1158)** : elle se déclenche aussi quand `arc5_tension_accumulee >= 4` sans `confronte`, mais cite toujours « la troisième annulation », que Jessy n'a peut-être jamais évoquée.
5. **« Le même café qu'au début du mois » (l.2297)** : la scène se passe en mars ; le café de la scène 2 date de janvier.
6. **Fin Minecraft `salle_repos`** : elle exige `honnete` et exclut `responsable` (l.2463), alors que le bonus du White Day et le récit d'Allan acceptent les deux. L'épilogue (l.2596-2601) n'a pas non plus de ligne pour `responsable`.
7. **`arc5_theo_dans_maison`** n'est mis à True que dans la branche `laisse` : la double condition de la ligne 2507 est redondante.
8. **`audio.library`** (l.914, 1475) n'est défini par aucun `define` ; seul `audio.lib` l'est (`script.rpy:170`). Le fichier `audio/music/library.ogg` existe ; la piste fonctionne probablement grâce au nommage automatique des fichiers audio par Ren'Py (non vérifié en jeu).
9. **Version cinéma** : elle saute le café, donc le rappel du stylo et la scène avec Théo et Allan. `arc5_sortie_annulee` reste vide ; les variantes qui en dépendent sont ignorées.
10. **Cartographie** : elle décrit `souvenir`/`simple` comme « lien+4 » sans tier, ce qui correspond au script. Elle classe `partiel` en tier D « malgré dialogue assertif », ce qui correspond aussi au commentaire du script (l.1006).
11. **Interprétation** : « depuis le festival » (l.2360) renvoie probablement au festival de l'Arc III.
