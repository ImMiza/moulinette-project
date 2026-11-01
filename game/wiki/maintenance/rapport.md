# Rapport de maintenance — scripts, doc de conception et ressources

- **But** : lister les bugs probables, les contradictions, le code mort et les ressources inutilisées relevés pendant la rédaction du wiki, pour corriger le jeu ou la doc plus tard.
- **Date** : 27/10/2026.
- **Sources** : notes `maintenance/notes/` (`prologue.md`, `arc1.md` à `arc6.md`, `routeA.md`, `routeB.md`, `finA1.md`, `finA2.md`, `finA3.md`, `finB1.md`, `finB2.md`), fragments `maintenance/characters/*.json`, inventaire `src/data/generated/inventory.json` (`npm run inventory`), scripts `game/**/*.rpy` (ils font foi) et docs de conception `game/agents/`.
- **Nature** : ce rapport est **éditorial**. Il faut le mettre à jour à la main. Le fichier `maintenance/couverture.md` est différent : il est **régénéré** par `npm run build` ou `npm run coverage`.
- **Convention** : `fichier:ligne` est relatif à `game/`. Tous les points ont été revérifiés dans le code le 27/10/2026, sauf ceux marqués « non revérifié ».

---

## 1. Bugs probables dans les scripts

La doc Ren'Py 8.5 (« Audio Directory and Namespace ») indique que chaque fichier de `game/audio/` **et de ses sous-dossiers** reçoit automatiquement un nom dans l'espace `audio` : nom du fichier sans extension, en minuscules. Le jeu est compilé avec Ren'Py 8.5.3 (`agents/cartographies/ending_family.md:89`, version non vérifiée sur l'installation). Les points B1 à B3 ne devraient donc pas faire planter le jeu. Ils dépendent toutefois de ce mécanisme implicite.

| # | Emplacement | Constat | Impact |
|---|---|---|---|
| B1 | `arcs/arc_7/arc_7_jessy.rpy:782`, `:874` | `play sound audio.car_stop` / `audio.car_go`, alors que les `define` s'appellent `audio.carStop` (`:126`) et `audio.carGo` (`:128`). Les fichiers `audio/fx/car_stop.mp3` et `car_go.mp3` existent. | Le son est trouvé grâce au nommage automatique. Si ce mécanisme ne s'applique pas, erreur à l'entrée de la scène 6 de la Route A. Correction : utiliser `carStop` / `carGo`. |
| B2 | `arcs/arc_7/arc_7_theo.rpy:27` | `define auddio.depressed = …` (faute de frappe). La ligne `:1439` joue `audio.depressed`. `audio/music/depressed.ogg` existe. | Le `define` est inutile (il crée un espace `auddio`). La musique de l'option « sponsors » ne fonctionne que grâce au nommage automatique. Correction : `audio.depressed`. |
| B3 | `arcs/arc_5/arc_5_examens.rpy:914`, `:1475` | `audio.library` n'est défini nulle part. Seul `audio.lib` l'est (`script.rpy:170`, utilisé `:50`). `audio/music/library.ogg` existe. | Même dépendance au nommage automatique. Correction : `audio.lib`. |
| B4 | `arcs/arc_1/arc_1_printemps.rpy:10` (joué `:274`) | Le chemin `audio/fx/kombini_open.mp3` ne correspond pas à la casse du fichier réel, `Kombini_open.mp3`. | Fonctionne sous Windows. Risque sur un système sensible à la casse (Linux, Android, web) ou dans une archive. Non testé. |
| B5 | `arcs/arc_7/arc_7_jessy.rpy:124` (joué `:308`, `:801` ; `arcs/endings/ending_family.rpy:940`) | Le chemin `audio/fx/AE86_engine_start.mp3` ne correspond pas à la casse du fichier réel, `AE86_Engine_Start.mp3`. | Même risque que B4. |
| B6 | `arcs/arc_6/arc_6_diplomes.rpy:137`, `:141` (affichés `:1382`, `:1837`) | `bg_arc6_corridor_empty.jpg` et `bg_arc6_minecraft_last.jpg` sont absents. `arc6_bg()` (`:127-130`) affiche un décor de secours : `bg_shared_school_corridor.jpg` et `bg_arc2_minecraft_house_summer_night.jpg`. | Aucun plantage. Les décors de secours restent provisoires. |
| B7 | `arcs/arc_6/arc_6_diplomes.rpy:140` | `bg_arc6_rooftop_dusk.jpg` est absent, avec `bg_arc5_rooftop.jpg` en secours. Le décor n'est jamais affiché. | Aucun. Voir aussi §4. |
| B8 | `arcs/arc_7/arc_7_jessy.rpy:74` (affiché `:141`) | `hiking/bg_arc7_jessy_minecraft.jpg` est absent ; le secours est le décor Minecraft d'été de l'arc 2. | Décor provisoire. |
| B9 | `arcs/endings/ending_family.rpy:1032`, `:1133`, `:1138` | `family_save_the_world.ogg` et `family_hopes_dreams_save_last_goodbye.ogg` sont absents. Les secours sont `spring-hope.ogg` et `real-love.ogg`. | Le carton de crédits Undertale (`:1138-1139`) n'est jamais affiché. |
| B10 | `arcs/endings/ending_ilonanium.rpy:318-319`, `:831`, `:872`, `:890-895` | `ilonanium_across_the_void.ogg`, `ilonanium_vanirs_legacy.ogg` et `ilonanium_roundabout.ogg` sont absents. Pour le premier, la musique précédente (`tense-piano`) continue. Les secours des deux autres sont `spring-hope.ogg` et `alex_peace.ogg`. | Les crédits IXION et Yes ne sont pas affichés. |
| B11 | `screens.rpy:1204` | `gui/confirm_frame.png` est absent. Le `Frame` reçoit la liste `["gui/confirm_frame.png", "gui/frame.png"]` et `gui/frame.png` existe. | Probablement aucun (modèle Ren'Py standard). Non vérifié en jeu. |
| B12 | `arcs/prologue/prologue_minecraft.rpy:38`, `:42`, `:46` | `play sound "fx/…"` sans préfixe `audio/`, alors que `game/fx/` n'existe pas. | Ren'Py cherche ensuite dans `game/audio/fx/` (doc 8.5), donc probablement aucun impact. Non testé en jeu. |
| B13 | `script.rpy:380` | Une ligne `systeme` de développement est affichée au joueur : « La base actuelle pose les arcs, les variables… ». | Texte de travail visible au début de la partie. |
| B14 | `arcs/endings/bad_ending.rpy:63`, `:65`, `:66` | Accents manquants (« Ca », « activite », « evites », « categories differentes », « entraine »). | Coquilles visibles. |
| B15 | `arcs/endings/bad_ending.rpy:367` | `stop music fadeout 4.0`, alors qu'aucune musique ne joue depuis `:205`. | Aucun. Instruction inutile. |

---

## 2. Contradictions entre la doc de conception et les scripts

| Sujet | La doc dit | Le script fait | Source |
|---|---|---|---|
| Formule du score de l'arc 6 | `arc6_score = espace + posture + recidive + arc6_mod - dette` | Pas de `arc6_mod` : `espace + posture + recidive - dette`, +20 de rachat | `agents/systeme de points.md:254` ↔ `arcs/arc_6/arc_6_diplomes.rpy:72-75` |
| Moment du calcul de l'arc 6 | Dans le label `arc_6_calcul`, « en fin d'arc 6 » | Calcul au **début** de l'arc (`$ arc6_calcule_verdict()`, `:160`). `arc_6_calcul` (`:1721-1723`) se contente d'un `jump`, ce que confirme le commentaire `:1717-1719`. | `systeme de points.md:237` ; `script.rpy:292-293`, `:421` |
| Label `arc_6_debug_score` | Cité | N'existe pas | `script.rpy:391` |
| Score max théorique | « Que du tier S : 568, lien 19 » (et « max 572 » deux lignes plus bas) | Commentaire : « 572 (que du tier S, lien 18) » | `systeme de points.md:272`, `:277` ↔ `script.rpy:397` |
| `theo_utilise_une_verite` | Souvenirs « à ne poser que quand c'est mérité, jamais inconditionnellement » (−6) | `remember(...)` **inconditionnel** au duel : le −6 de posture s'applique à toutes les parties. Seule la pose de `:311` est conditionnelle. | `systeme de points.md:203-210` ↔ `arcs/arc_3/arc_3_rentree.rpy:619` (`:309-311`) |
| `confidences_laplage` | « Les trois occurrences » sont conditionnées par `ilona_peut_finir_ses_phrases < 2 / < 4 / < 6` | Quatre incréments. Arcs 3 et 4 : `< 2` et `< 4`. Arc 5 : deux incréments exclusifs selon `arc5_etat_relation` (`fragile` / `distant`), sans test `< 6`. | `systeme de points.md:46` ↔ `arc_3_rentree.rpy:530-531`, `arc_4_noel.rpy:749-750`, `arc_5_examens.rpy:1554`, `:1585` |
| Conditions de la scène 4.5 Théo | `influence_theo >= 5, confiance <= 2` (commentaire) | `influence_theo >= 10 and confiance <= 8 and arc4_limite_ilona == "demande_theo"` | `arcs/arc_4/arc_4_5_theo.rpy:2` ↔ `arcs/arc_4/arc_4_noel.rpy:1203` |
| Variables de sprite d'hiver | « set, inutilisés » | Relues par `show expression` dans l'arc 5 (`arc_5_examens.rpy:375-1935`, d'après les notes ; plage non revérifiée) | `agents/cartographies/arc_4.md:50`, `:70` |
| Fruit étoilé (Fin A3) | Ilona « sort une baie » et la mange au début de la fin | Le fruit est goûté pendant la randonnée (`arc_7_jessy.rpy:404-406`). Commentaire : « Le fruit est déjà mangé à l'arc 7 ». | `agents/illonanium/Fin ilonanium.md:5` ↔ `arcs/endings/ending_ilonanium.rpy:3` |
| Réplique de Laplage (A3) | « Laisser digérer. » Pouce levé. | « Laissez digérer. », sans pouce | `Fin ilonanium.md:19` ↔ `ending_ilonanium.rpy:369` |
| Lieux de la Route A | « aéroport » (S1), « kissaten » (S7) | « à la gare » (`arc_7_jessy.rpy:158`), « Le restaurant » (`:917`) | `agents/cartographies/arc_7.md:11`, `:17`, `:49` |
| Durée de la Route B | « 6 avril → ~novembre » | Million le 6 décembre (`arc_7_theo.rpy:951`), après « huit mois » (`:1125`) | `cartographies/arc_7.md:21` |
| Image « evil theo » et sirène | Jouées lors de la bascule des onze jours (arc 6) | Définies dans l'arc 6 (`arc_6_diplomes.rpy:152-153`), mais jouées dans l'arc 5 si `arc5_theo_proposition == "laisse"` (`arc_5_examens.rpy:1121-1126`, d'après les notes) | `cartographies/arc_6.md:16`, `:65` |
| Libellés du menu de la rumeur | « Regarder Ilona d'abord et lui laisser la main. » / « Défendre Ilona immédiatement, sans lui demander. » | « Regarder Ilona d'abord. » / « Défendre Ilona immédiatement. » (effets identiques) | `systeme de points.md:164`, `:174` ↔ `arc_3_rentree.rpy:219`, `:256` |
| Noms des objets cosmiques | « gelée marine », « mochi cosmique » | « gelée lumineuse », « mochi pailleté » (la variable reste `arc4_mochi_cosmique`) | `systeme de points.md:201` ↔ notes `routeA.md` (non revérifié ligne à ligne) |
| Pouces de Laplage | « pouces levés ou baissés » | `laplage thumb_down` est déclaré (`script.rpy:150`) mais jamais affiché. Le pouce est levé, horizontal (`arc_4_5_theo.rpy:13`) ou explicitement non levé. | `cartographies/fiches_personnages.md:147` |
| Alexandre au prologue | « ami de Jessy » | Il connaît Jessy et l'appelle par son prénom, sans que le mot « ami » soit dit (notes, non revérifié) | `cartographies/prologue.md:39` |
| Taille de l'arc 5 | 2611 lignes | 2620 lignes | `cartographies/arc_5.md:3` |
| Sortie Laplage sur la Route B | `confidences_laplage >= 3 -> sortie Laplage possible` (commentaire) | Aucun code de la route ne lit `confidences_laplage` | `arcs/arc_7/arc_7_theo.rpy:5` |
| Déclenchement de la Fin A3 | « le fruit ouvre Ilonanium » (commentaire) | Il faut `ilonanium_points == 6` **et** `arc7_jessy_fruit == "goute"` | `arc_7_jessy.rpy:2` ↔ `:1177-1178` |
| Commentaire du maid café | « Seule soupape de pression du jeu » | D'autres choix baissent aussi `pression_stream` (ex. prologue, arc 1) | `arcs/arc_4/arc_4_5_maid_cafe.rpy:210` |

---

## 3. Incohérences internes au récit

| # | Constat | Source |
|---|---|---|
| R1 | « Jessy est rentré chez lui en métro », alors qu'il reste « immobile » au marché, la main d'Allan sur l'épaule. | `arc_4_5_theo.rpy:35` ↔ `arc_4_noel.rpy:1237-1238` |
| R2 | Citation déformée : « Tu me demandes de te rassurer… », alors que la réplique d'origine est « Tu demandes si je dois te rassurer… ». | `arc_4_5_theo.rpy:49`, `:92` ↔ `arc_4_noel.rpy:813` |
| R3 | En 4.5 Théo (chemin `demande_theo`), Ilona repense à la miniature ou à l'écharpe, alors que ce chemin ne les fait pas offrir. | `arc_4_5_theo.rpy:130-132` (et `:430-432`, non revérifié) |
| R4 | Avec `marche_silencieuse` et la miniature choisie, Ilona construit « une version de ton cadeau » sans l'avoir reçue (réception non revérifiée, `:942` selon les notes). | `arc_4_noel.rpy:1281-1297` |
| R5 | Ilona a la miniature dans son sac dès que le cadeau choisi est `miniature_*`, même si elle ne l'a pas reçue. | `arc_6_diplomes.rpy:221` |
| R6 | « Tu as fini par retrouver ta serviette ? » : aucune serviette perdue à l'arc 2. | `arc_3_rentree.rpy:75` |
| R7 | La gelée « commence à fondre » ou « fond lentement », mais le gobelet est intact le soir et peut encore être mangé. | `arc_2_plage.rpy:742`, `:751` ↔ `:1092` |
| R8 | La cuisine d'été est d'abord un projet de « cuisine de plage » (train), puis une construction existante le soir même. L'arc 3 la dit « construite après la plage » sans qu'on voie la construction. | `arc_2_plage.rpy:136`, `:1120` ; `arc_3_rentree.rpy:1091` |
| R9 | Texte du panneau : « ICI, LES PHRASES ONT LE DROIT DE TREMBLER » (arc 3) devient « Laisse-la finir ses phrases » (arc 5). | `arc_3_rentree.rpy:1059` ↔ `arc_5_examens.rpy:2458` |
| R10 | L'arc 3 détruit la cuisine d'été, mais l'arc 5 parle de la « salle moyennement importante » jamais reconstruite. | `arc_3_rentree.rpy:1087-1116` ↔ `arc_5_examens.rpy:2455` |
| R11 | « La lanterne bleue de la cour » (branche morte, voir §4) : la lanterne bleue est dans la cuisine d'été de l'arc 2. | `arc_5_examens.rpy:2461` ↔ `arc_2_plage.rpy:1120` |
| R12 | « la troisième annulation » est citée dès que `arc5_tension_accumulee >= 4`, même si Jessy n'a jamais choisi `confronte`. | `arc_5_examens.rpy:1155-1158` |
| R13 | Branche `inquiet` (« Tu es sûre que ça va ? », `:547`) : elle n'est pas traitée et tombe dans le `else` (« Rien de spécial » / « Tu mens »). | `arc_5_examens.rpy:672-717` |
| R14 | « Le même café qu'au début du mois » : la scène se passe en mars, le café date de janvier. | `arc_5_examens.rpy:2297` |
| R15 | Tournage sponsor « à quatorze » le lendemain, puis « les sponsors à quinze heures » le soir même. Il peut s'agir de deux rendez-vous (non tranché). | `arc_7_theo.rpy:1007` ↔ `:1337` |
| R16 | Le bail court « pour huit mois au moins » à partir du 6 avril, mais la Fin B1 dit « On a jusqu'à la fin du mois » après le 6 décembre. | `arc_7_theo.rpy:162` ↔ `endings/ending_neutre.rpy:112` |
| R17 | La Route B rappelle que Théo a répondu « les deux », alors qu'il ne le dit que si `arc6_penchant == "theo"`. Sinon, il répond « Je veux que tu viennes ». | `arc_7_theo.rpy:92-93` ↔ `arc_6_diplomes.rpy:1465-1476` |
| R18 | Route B : le récit place le 6 décembre avant de revenir à fin août et fin octobre, sans signaler le retour en arrière. | `arc_7_theo.rpy:951` ↔ `:1068-1080` (notes) |
| R19 | Le tchat dit « best vtubeuse » alors qu'Ilona streame en caméra, avec une perruque. | `arc_7_theo.rpy:1131` ↔ `:1120` |
| R20 | Les collègues de Sofiane sont « déjà en uniforme de maid café » même si le joueur ne connaît pas ce secret. C'est voulu d'après la doc (information destinée au joueur). | `arc_7_jessy.rpy:786` ; `cartographies/ending_family.md:27` |
| R21 | Bonbon étoile : Ilona « ouvre déjà » le bonbon, mais deux options le conservent (non revérifié). | `arc_1_printemps.rpy:295` |
| R22 | Ouverture de l'arc 2 : couloir d'école en juillet, avec les sprites par défaut. Faiblesse déjà signalée dans la doc (non revérifié). | `cartographies/arc_2.md` |

---

## 4. Code mort, branches inatteignables, variables jamais relues

| # | Élément | Détail | Source |
|---|---|---|---|
| M1 | Branche `lanterne_cour` | Le `else` est inatteignable : le menu de `:793` donne toujours l'une des quatre valeurs testées avant (`:797`, `:815`, `:838`, `:859`). Les lectures en aval sont donc mortes aussi. | `arc_3_rentree.rpy:1117-1125` ; lu `arc_5_examens.rpy:2460`, `arc_6_diplomes.rpy:881` |
| M2 | Branche `neige_sur_toit` | Le `else` est inatteignable, car `arc4_limite_ilona` est toujours fixé par le menu de `:797`. Le `else` de `arc_5_examens.rpy:96-97`, qui en dépend, l'est aussi (non revérifié). | `arc_4_noel.rpy:1343-1352` |
| M3 | Variante du maid café « sans carte » | `arc4_carte_sofiane_lue = True` est inconditionnel sur le chemin unique de l'arc. La variante `else` est inatteignable. | `arc_4_noel.rpy:624` ; `arc_4_5_maid_cafe.rpy:195-204` |
| M4 | « Et ton cadeau, je le veux » sous `cadeau_respirant` sans miniature | Inatteignable selon les notes (non revérifié). | `arc_4_noel.rpy:1103-1106` |
| M5 | `jugement_laplage` | Neuf incréments, aucune lecture. | `script.rpy:228` ; `prologue_minecraft.rpy:373`, `arc_2_plage.rpy:786`, `arc_3_rentree.rpy:532`, `arc_4_noel.rpy:751`, `arc_4_5_theo.rpy:372`, `arc_5_examens.rpy:1064`, `:1414`, `:1889`, `:1913` |
| M6 | `maison_minecraft_ajouts` / `maison_minecraft_destructions` | Alimentés par des `.append` dans les arcs 3, 4 et 5, jamais relus. Commentaire : « pour cohérence arcs futurs ». Le prologue (effondrement) et l'arc 1 (bonbon dans la salle secrète) n'y écrivent rien. | `script.rpy:242-244` ; `arc_3_rentree.rpy:1063-1125`, `arc_4_noel.rpy:1286-1352`, `arc_5_examens.rpy:2489-2552` |
| M7 | `endings_seen` | Écrit par `record_ending()` dans les cinq fins, jamais lu ni affiché. C'est un `default` (une liste par sauvegarde), pas une donnée `persistent`. | `script.rpy:256`, `:279-281` |
| M8 | `arc_6_debug_score` | Label cité, inexistant. `arc_6_calcul` n'est qu'un passe-plat. | `script.rpy:391` ; `arc_6_diplomes.rpy:1721-1723` |
| M9 | `arc6_penchant == "theo"` dans `arc_6_decision_jessy` | Clause morte par déduction : la route Jessy exige un score ≥ 180, donc un indice espace − dette ≥ 138 (180 − 22 de posture max − 20 de rachat), donc un état au moins « fragile ». Le `or influence_theo >= 8` reste actif. | `arc_6_diplomes.rpy:1805` |
| M10 | Rappel « La route a gardé une trace fausse » | Inatteignable en pratique : la Route B n'est atteinte que si `controle_repetitif >= 3` ou si le score est inférieur au seuil. | `arc_7_theo.rpy:85-86` |
| M11 | Branche « ancienne sauvegarde » | Compatibilité ; normalement inatteignable (relation toujours fixée). | `arc_7_jessy.rpy:1187-1190` |
| M12 | Variables écrites jamais relues | `arc6_gateau_planete`, `arc6_vignettes_jouees` (9 `append`), `arc6_penchant_debut` (seulement relue par sa propre initialisation, `:38`), `arc6_derive` (« conservé pour compatibilité », `:21`), `derniere_route` (`arc_7_theo.rpy:72`, `arc_7_jessy.rpy:132`, sans `default`). | `arc_6_diplomes.rpy:5-21` |
| M13 | Variables relues seulement dans leur arc | `arc2_retour_minecraft` (arc 2), `arc4_mochi_cosmique`, `arc4_accueil_limite` (arc 4), `arc5_sortie_annulee`, `arc5_valentin_*`, `arc5_white_day_reponse`, `arc5_etat_relation`, `arc5_allan_*`, `arc5_laplage_deuxieme_confidence`, `arc5_theo_dans_maison` (arc 5), `interruptions_reconnues` (seulement comparée à elle-même). Ce n'est pas du code mort, mais aucun effet à long terme. | grep `game/**/*.rpy` |
| M14 | Condition redondante | `arc5_theo_dans_maison` n'est vrai que dans `laisse` : le double test est redondant (non revérifié). | `arc_5_examens.rpy:2507` |
| M15 | Plafond de vignettes `< 8` | Jamais atteint : 7 vignettes possibles au maximum (non revérifié). | `arc_6_diplomes.rpy` (notes `arc6.md`) |
| M16 | Vidéo d'intro commentée | L'écran `studio_intro` et son appel sont commentés. | `script.rpy:325-350` |
| M17 | Pistes déclarées non jouées (Fin B2) | `audio.bakamitai`, `audio.sayonara`, `audio.majulaLike` (`play` commenté `:323`). Commentaire `:15` : « pistes temporaires ». | `bad_ending.rpy:16-18` |
| M18 | Fichier de sauvegarde de script | `arc_4_noel.rpy.bak` (ancienne version, ignorée). | `arcs/arc_4/` |

---

## 5. Ressources présentes mais inutilisées (`inventory.json`)

### 5.1 Comptage par statut (inventaire du 26/10/2026)

| Statut | Nombre | Détail par type |
|---|---|---|
| utilisé | 540 | audio 97, gui 27, images 416 |
| déclaré, non affiché | 51 | audio 3, images 48 |
| non référencé | 48 | audio 5, images 42, vidéos 1 |
| interface (implicite) | 71 | gui 71 |
| référencé en commentaire | 1 | vidéos 1 |
| **Total** | **711** | audio 105, gui 98, images 506, vidéos 2 |

Tous les assets « non utilisé » hors interface portent `requires: ["extras"]` dans le wiki.

### 5.2 Faux positifs de l'inventaire

Corrigés dans `scripts/extract-inventory.mjs` (27/10/2026) : chemins construits par un helper `"…_{}.jpg".format(nom)` (`arc7_jessy_bg()`, `arc7_sofiane_cg()`, `arc_7_jessy.rpy:33-37`, `:87-99`) et sons d'interface de `screens.rpy` (`jessy_laugh.ogg` l.311, `bubble.ogg` l.1650) sont désormais « utilisé ».

Reste un faux positif connu :
- `images/ui/ilonanium_to_be_continued.svg` : écran affiché par `ending_ilonanium.rpy:882` (référence hors label, non suivie). La prise en charge du SVG par le moteur n'est pas vérifiée.

Correction de la note `notes/routeA.md` : `bg arc7 jessy nuit` (`arc_7_jessy.rpy:69`) est déclaré mais jamais affiché (seul `bg arc7 jessy nuit tente ferme` l'est, l.1077/1081) ; il est bien « déclaré, non affiché ».

Il reste donc **37** assets réellement « déclarés, non affichés » (38 dans l'inventaire, moins le SVG).

### 5.3 Déclarés mais jamais affichés ou joués (36)

- `audio/music/` : `Sayo-nara.ogg` (`bad_ending.rpy:17`).
- `images/personnages/Alexandre/` : `genuine_laughter.png`, `supportive_encouragement.png` (`script.rpy:131`, `:135`).
- `images/personnages/Alexandre/Winter/` : `akward_realization.png`, `genuine_laughter.png`, `peace.png` (`arc_4_noel.rpy:61-66`).
- `images/personnages/Allan/` : `awkward_embarrassment.png` (`script.rpy:119`) ; `Allan/Winter/awkward_embarrassment.png` (`arc_4_noel.rpy:52`).
- `images/personnages/Florentin/illonanium/` : `futuristic_armor.png` (`ending_ilonanium.rpy:162`).
- `images/personnages/Ilona/` : `Tokyo/sad.png` (`arc_7_theo.rpy:45`), `Winter/sad.png` (`arc_4_noel.rpy:22`), `Winter/Winter_with_scarf/sad.png` (`:30`).
- `images/personnages/Jessy/` : `Rando/With_bag/happy.png` (`arc_7_jessy.rpy:21`, sprite `jessy rando bag determined` ; `bag listening`, `:20`, n'est pas affiché non plus), `Winter/angry.png`, `Winter/happy.png` (`arc_4_noel.rpy:10`, `:12`), `illonanium/prophet_with_gem.png` (`ending_ilonanium.rpy:150`).
- `images/personnages/Laplage/` : `thumb_down.png` (`script.rpy:150`) ; `illonanium/thumb_up.png` (`ending_ilonanium.rpy:132`).
- `images/personnages/Micka/illonanium/` : `sci_fi_armor.png` (`:142`).
- `images/personnages/Sofiane/` : `dramatic_intensity.png`, `relieved_smile.png`, `reserved_neutral.png`, `shy_embarrassment.png` (`script.rpy:140-145`) ; `Winter/cryptic_smirk.png`, `Winter/reserved_neutral.png` (`arc_4_noel.rpy:71-73`) ; `illonanium/tactical_sci_fi_armor.png` (`ending_ilonanium.rpy:159`).
- `images/personnages/Theo/` : `knowing_smirk.png` (`script.rpy:114`) ; `Tokyo/controlled_annoyance.png`, `Tokyo/quiet_jalousy.png` (`arc_7_theo.rpy:61`, `:68`) ; `Winter/controlled_annoyance.png`, `feigned_innocence.png`, `quiet_jalousy.png` (`arc_4_noel.rpy:35-40`) ; `Winter/Winter_with_scarf/controlled_annoyance.png`, `quiet_jalousy.png` (`:44`, `:49`) ; `illonanium/older_neutral.png` (`ending_ilonanium.rpy:166`).
- `images/scenes/cg/sofiane_initial_d/` : `sofiane_ae86_route_nuit_collegues_euphorie.jpg`. Le code charge la version `.png` (`arc_7_jessy.rpy:79`) ; le `.jpg` n'est cité que par le motif générique `:88`.

Décors déclarés sans fichier propre et jamais affichés (hors inventaire des fichiers) : `bg arc6 rooftop dusk` (`arc_6_diplomes.rpy:140`) ; `bg arc7 jessy riviere`, `fleurs`, `promontoire`, `belvedere`, `cafe` (`arc_7_jessy.rpy:46-48`, `:71-72`). `bg arc7 intro stream` est déclaré dans la Route B (`arc_7_theo.rpy:30`) mais affiché seulement en Fin B2.

### 5.4 Non référencés (48)

- `audio/ambience/` : `foule.mp3` (l'alias `audio.foule` pointe vers `crowd-noise.mp3`), `high_school_indoor_ambience_corridor.mp3`.
- `audio/fx/` : `Chicken_hurt1.ogg`, `female-sigh.mp3`, `footsteps-snow.mp3`.
- `images/personnages/Alexandre/Beach/` : `blunt_seriousness.png`, `genuine_laughter.png`.
- `images/personnages/Alexandre/Festival/` : `blunt_seriousness.png`, `genuine_laughter.png`, `neutral.png`, `peace.png`, `supportive_encouragement.png`.
- `images/personnages/Alexandre/Party/` : `blunt_seriousness_party.png`, `genuine_laughter_party.png`, `neutral_party.png`, `peace_party.png`, `supportive_encouragement_party.png`, `teasing_skepticism_party.png`.
- `images/personnages/Allan/Beach/` : `cheerful_excitement.png`, `wide_eye_surprise.png`.
- `images/personnages/Allan/Festival/` : `awkward_embarrassment.png`, `cheerful_excitement.png`, `wide_eye_surprise.png`.
- `images/personnages/Allan/Party/` : `cheerful_excitement.png`, `quiet_support.png`, `uncomfortable_silence.png`.
- `images/personnages/Ilona/Festival/awkward_embarrassment.png` ; `Ilona/Rando/With_bag/sad.png` (fichier présent, sprite non déclaré).
- `images/personnages/Jessy/Festival/happy.png` ; `Jessy/illonanium/beach_surprised.png`.
- `images/personnages/Sofiane/Beach/quiet_observation.png` ; `Sofiane/Party/quiet_observation.png`.
- `images/personnages/Theo/Beach/` : `cold_disappointment.png`, `controlled_annoyance.png`, `defense_frustration.png`, `feigned_innocence.png`, `quiet_jalousy.png`.
- `images/personnages/Theo/Festival/` : `feigned_innocence.png`, `quiet_jalousy.png` ; `Theo/Party/feigned_innocence.png`.
- `images/personnages/Theo/Theo_laplage/` : `neutral.png`, `neutral_laplage.png`, `picture.png`, `thumb_up_laplage.png` (dossier entier inutilisé).
- `images/promo/ilonanium/annonce_ending_ilonanium_discord.png` (visuel promotionnel).
- `images/scenes/backgrounds/school/bg_arc1_school_corridor.jpg` et `transport/bg_arc1_train_inside.jpg`. L'arc 1 utilise les versions `bg_shared_*`.
- `videos/muchacho_studio_internation_studio.webm`.

### 5.5 Référencé en commentaire (1)

- `videos/intro.webm` (`script.rpy:330`, écran `studio_intro` commenté).

### 5.6 Interface implicite (71)

La plupart sont des fichiers GUI du modèle Ren'Py. Quatorze sont des restes de travail visibles à leur nom : `gui/game_menu.old.png`, `main_menu_old.png`, `namebox1.png`, `namebox_old.png`, `namebox_old2.png`, `namebox_test.png`, `namebox_test2.png`, `namebox_test3.png`, `textbox1.png`, `textbox_old.png`, `textbox_old2.png`, `gui/overlay/main_menu_old.png`, `gui/button/choice_hover_background_old.png`, `choice_idle_background_old.png`.

### 5.7 Fichiers manquants (avertissements de l'inventaire : 24)

Six écarts de casse (B4, B5), huit secours, six fichiers manquants (B6 à B11) et quatre noms audio automatiques (B1, B3).

---

## 6. Interprétations non confirmées retenues dans le wiki

| # | Interprétation | Appui dans le texte | Où dans le wiki |
|---|---|---|---|
| I1 | Fin B2 : la mort d'Ilona est un geste volontaire. | Cause jamais nommée ; « Ilona ne ferait jamais ça » (`bad_ending.rpy:278`) | `fins/b2.mdx:33`, `personnages/ilona.mdx:825`, `data/scenes/finB2.json:45` |
| I2 | Alias « l'Ilonanium » pour Ilona. | Le texte nomme ainsi « ce monde de cauchemar », l'astre formé autour d'elle (`ending_ilonanium.rpy:361-364`), pas Ilona elle-même. | `maintenance/characters/ilona.json:15` |
| I3 | La « voix au téléphone » de la Fin A2 est Monsieur Laplage. | « Je connais cette voix » (`ending_family.rpy:150-159`), puis Laplage ouvre comme propriétaire | `personnages/autres.mdx:441`, `personnages/laplage.mdx:468` |
| I4 | L'inconnu « ??? » du prologue est Monsieur Laplage. | Affirmé par les personnages : « Le type de la rivière » (`arc_1_printemps.rpy:316-317`) | `characters/inconnu.json`, `characters/laplage.json` |
| I5 | Fin B2 : « Le prochain, c'est toi » signifie que Théo prendra la place de Laplage. | Non expliqué en B2 (`bad_ending.rpy:350`) ; explicite seulement en Fin A3 | `personnages/laplage.mdx:480` |
| I6 | « première B, deuxième étage » est la classe de Jessy. | `arc_1_printemps.rpy:28` | `monde/factions.mdx:25` |
| I7 | Sofiane travaille au maid café depuis septembre environ. | « Depuis trois mois » en décembre (`arc_4_5_maid_cafe.rpy:156`) | `histoire/chronologie.mdx:53` |
| I8 | La scène de la cantine (arc 1) a lieu un jour suivant. | `arc_1_printemps.rpy:589` | `histoire/chronologie.mdx:35` |
| I9 | `jugement_laplage` est une variable vestigiale ou prévue. | Jamais lue (M5) | `personnages/laplage.mdx:428` |
| I10 | « Ceux qui creusent » vise Théo. | `arc_3_rentree.rpy:491-499` ; la cible n'est pas tranchée | notes `arc3.md` |
| I11 | Origine du surnom « le Messi » | Donnée par Allan avec « Probablement » (`arc_4_noel.rpy:573-577`) | notes `arc4.md` |
| I12 | « depuis le festival » renvoie au festival de l'arc 3. | `arc_5_examens.rpy:2360` (non revérifié) | notes `arc5.md` |

---

## 7. Limites de l'analyse

- **Rien n'a été testé en jeu.** Ni rendu Ren'Py, ni lint, ni test automatisé (`game/tests/ilonanium.rpy` existe mais n'a pas été lancé). Les plantages possibles (B1 à B5, B11, B12) sont déduits de la doc Ren'Py 8.5 et de la présence des fichiers sur disque.
- **Version du moteur** : 8.5.3 selon `cartographies/ending_family.md:89`, non confirmée sur l'installation. Le nommage audio automatique dans les sous-dossiers et la prise en charge du SVG en dépendent.
- **Système de fichiers** : les écarts de casse n'ont été vérifiés que sous Windows. Aucun build archivé (`.rpa`), Android ou web n'a été testé.
- **Traduction** : `game/tl/` ne contient que `None/common.rpym` (et son `.rpymc`), sans traduction du jeu. Le wiki ne couvre que le français.
- **Pas de galerie ni de succès** : aucun `Gallery`, `achievement` ni écran des fins vues dans les scripts. `endings_seen` n'est jamais affiché (M7).
- **Inventaire** : il est statique. Les helpers `"…{}".format(nom)` et les sons d'interface de `screens.rpy` sont suivis ; les autres chemins dynamiques (`renpy.loadable`, écrans hors labels, actions `Play`) ne le sont pas (voir §5.2). Les comptes par statut du §5 datent de la rédaction ; les chiffres à jour sont dans `couverture.md`.
- **Déductions** : M9 et M10 reposent sur un raisonnement sur les formules (`arc_6_diplomes.rpy:44-84`, `script.rpy:283-323`), sans exploration exhaustive des parcours.
- **Notes d'arc** : les points marqués « non revérifié » viennent des notes sans nouvelle lecture du code. Correction à reporter dans `notes/routeA.md` : `bg arc7 jessy nuit` **est** affiché, et `hiking/bg_arc7_jessy_nuit.jpg` existe. Il ne fait pas partie des décors « jamais affichés ».
- **Fichier `.bak`** (`arc_4_noel.rpy.bak`) : non relu.
