# Arc 7 — Cartographie

Fichiers:
- `game/arcs/arc_7/arc_7_jessy.rpy` — entrée `arc_7_jessy` (jump depuis `arc_6_diplomes.rpy`). Chaîne : `arc_7_jessy` → `arc_7_jessy_scene_2`…`_scene_7` → `arc_7_jessy_nuit_retour` → `_scene_8` → `ending_ilonanium` ou `arc_7_jessy_fin_relation` → `ending_no_contact` (amitié) / `ending_jessy_ilona` (amour).
- `game/arcs/arc_7/arc_7_theo.rpy` — entrée `arc_7_theo`, toujours via `arc_6_bascule_theo`. Label unique (sections 1–1N, 2, 3). Sorties : `ending_neutre` / `bad_ending`. `ending_monsieur_laplage`, `ending_theo_vtuber` = code mort.
- Aiguillage (`arc6_calcule_verdict`, arc 6) : `controle_repetitif = interruptions_ilona - interruptions_reparees` ; `>= 3` → Théo forcé ; sinon `arc6_score >= SEUIL_JESSY` (180) → Jessy, sinon Théo. Score = espace (autonomie, phrases finies, réparations, communication, confiance) + souvenirs − dette (`influence_theo`, contrôle, `pression_stream`, `jalousie`, `confidences_laplage`).

## 1. Résumé de l'intrigue

**Route Jessy — « La randonnée »** (début été ; Ilona reste en France)
- S1 : Minecraft, 4 jours après diplômes. Ilona : « Théo part le 6 », indécise sur l'aéroport. Jessy propose une rando ; oui. Courses à cinq (Alex inspecte coutures, Allan biscuits). Allan ira voir Théo à Tokyo ; Sofiane promet la route.
- S2 : Sofiane en AE86 du cousin, dépose au sentier. Feuille « pliée en huit » de Jessy abandonnée.
- S3 : intro épique parodique (« l'épapopé de la jaj »). Oiseau, renard, rivière, fruit étoilé, carte à l'envers. Promontoire : menus fruit + déjeuner.
- S4 : Laplage sur un ours. Lac : Alexandre pêche une feuille, discours sur les choses absurdes qui comptent.
- S5 : bivouac. Veste des diplômes (3 mots au feutre sous le col). Ilona déclare son amour → menu ; sous-menu tente.
- S6 : Sofiane drifte avec deux collègues du maid café ; Laplage le double.
- S7 : Tokyo, kissaten. Allan/Théo réconciliation partielle ; Théo seul, triste ; apprend la rando, refuse de passer un message par Allan. Photo floue ; SMS « Dîner raté. Comme promis. » / « J'appelle demain. »
- Nuit : si amitié, Laplage en « appel codec » (porte ouverte).
- S8 : aube, rangement, descente. Menu secret Ilonanium possible.

**Route Théo — « Le monde après le départ »** (6 avril → ~novembre ; Ilona à Tokyo)
- Arrivée gare, appart fourni par le studio, règles de coloc. Studio violet « IlonaGaming », 1er stream (pic 2417, gag manette).
- J+10 : restaurant, Théo demande à sortir « pour de vrai » → oui, 1er baiser. Kung Pow.
- 10k abonnés ; parc : Laplage (« laisser une place au rien »).
- Dérive : 100k (juin), cadeau = opération sponsor, dîner seule, Shaolin Soccer refusé, carnet de planning retourné/remis face visible. 250k, 600k. Rappels conditionnels arcs 2-6.
- Le million (8 mois, 46k viewers). « Quand tu dis "on", tu parles de qui ? » Konbini, demande d'un après-midi à deux vs sponsors 15h.
- Menu final : écouter (Ilona veut une vraie pause, écrit elle-même le message → `ending_neutre`) / sponsors (« C'est toujours après », cage dorée, pleurs → `bad_ending`).

## 2. Personnages

- **Jessy** (`j`) : planificateur anxieux, autodérision, références Minecraft/jeu (« loot rare », Puff-Puff, MGS). Tu, oral sans « ne », zéro vulgarité. Évolue : arrête de remplir les silences, nomme ses sentiments. Absent de la route Théo.
  - « Je mets des torches pour m'occuper les mains. »
  - « Je savais pas quoi construire avec. »
- **Ilona** (`i`) : directe, pince-sans-rire, pratique ; mange pour gagner du temps. Tu, oral (« grave kiffé » en stream). Route Jessy : prend l'initiative de l'aveu. Route Théo : émerveillement → épuisement, « Ah. », tire sur sa manche.
  - « Si c'est non, je préfère un vrai non. »
  - « C'est toujours après. »
- **Théo** (`t`) : précis, chiffré (832, 2417, 32 min), phrases courtes, « ne » souvent conservé. Attention = contrôle ; anticipe et décide seul. Appelle Laplage « le Messi ». Route Jessy : isolé, lucide, s'ouvre à Allan.
  - « Je réponds avec une information utile. »
  - « J'ai peur que si on ralentit, tout disparaisse. Mais c'est ma peur. Pas ta consigne. »
- **Allan** (`a`) : clown, obsédé goûter/sandwichs ; a « traduit » Théo 10 ans. « Le nord est une convention sociale. »
- **Alexandre** (`x`) : rigueur d'ingénieur devenue contemplation. « N'est-ce pas magnifique ? »
- **Sofiane** (`s`) : laconique, solennel, culte de la route. « C'est une direction. Un programme, ça a des horaires. »
- **Laplage** (`laplage`) : prof absurde ubiquitaire, vouvoie, aphorismes, pouce levé. « Du réarmement démographique. »
- **Tchat** (`tchat`) : pseudos récurrents sakura_mod, pixel_ramen, misterclip, kiwi_no_kimi, darkflame92.

## 3. Faits établis (continuité)

- Théo part pour Tokyo le 6 avril (studio, « trois chaînes »).
- Route Jessy : Théo parti seul, personne à l'aéroport ; Allan avait l'heure (via la mère de Théo). Appart de Théo : 2 chambres, 2e clé dans un tiroir, 32 min de trajet, proprio l'appelle « Tao ». Dispute du gymnase Allan/Théo ; Allan repart jeudi ; Théo promet d'appeler.
- Laplage à Théo à Noël : « Non. Mais tu gardes la clé. »
- 3 mots d'Ilona au feutre sous le col de la veste de Jessy.
- Gags : carte à l'envers (Jessy, Allan), porte inutile, sandwichs « Assez », feuille pliée en huit/quatre, pêche d'une feuille, Laplage sur un ours, « sourit depuis le troisième virage ».
- Grands-parents d'Alexandre près du lac ; AE86 du cousin (« Ne la déçois pas ») ; Sofiane et le maid café.
- Fruit/noyau étoilé = piste Ilonanium.
- Route Théo : couple dès J+10 ; appart à 2 rues du studio ; paliers 10k, 100k, 250k (fin août), 600k (fin oct.), 1M ; cheveux courts dès 6 déc. ; persona stream veste bleue + perruque blanche ; écharpe de Théo près de la porte ; porte-clés bloc de la plage ; carnet de croquis de Noël ; quai : « J'ai ce que j'ai décidé de prendre. » Ilona n'aime pas le melon.

## 4. Variables / flags / points

- Route Jessy (reset en entrée) : `arc7_jessy_fruit` ("goute"/"jette"), `arc7_jessy_dejeuner` ("amitie"/"crush"), `arc7_jessy_relation` ("amitie"/"amour"), `arc7_jessy_tente`, `arc7_jessy_family_epilogue`. `derniere_route = "Route Jessy"`.
- Menus : fruit (goûter → `ilonanium_points += 1`) ; déjeuner (texte bivouac adapté) ; réponse à l'aveu ; si amour, tente (`arc7_jessy_tente = True`) ou hamac ; final si `ilonanium_points >= 6 and arc7_jessy_fruit == "goute"`.
- `arc7_jessy_family_epilogue = arc6_score >= SEUIL_ROMANCE and lien_jessy_ilona >= SEUIL_LIEN and souvenirs["jessy_repare"] and souvenirs["maison_respectee"] and interruptions_reparees >= 1` (320 / 35).
- Testés (Jessy) : `arc6_derniere_construction` (porte_ouverte, panneau_partir, cadenas), `arc6_offre_theo` (laisse, accusation, aveu_vide, question), `arc6_conversation` (que_veux_tu, aveu_interruptions).
- Route Théo : `derniere_route = "Route Théo"`, `controle_repetitif` recalculé. Testés : `arc6_score`, `arc6_offre_theo`, `arc6_stylo` (garde, rendu_explique, rendu, blague), `souvenirs["ilona_veut_streamer_serieusement"]`, `arc4_ilona_avec_theo`, `arc4_5_theo_proposition` (gestion_stream, question, temps), `arc2_choix_activite_theo` (suivre, disparaitre), `arc5_fin_minecraft == "theo_presence"`, `arc5_theo_proposition` (partiel, laisse, refuse, questionne), `arc3_reaction_rumeur` (blague_desarm, silence_paralysie), `arc4_reaction_cadeau_theo` (blague_acide, verite_crue). Menu final : aucun flag, jump direct.

## 5. Conventions d'écriture

- Speakers : `j`, `i`, `t`, `a` (Allan), `x` (Alexandre), `s` (Sofiane), `laplage`, `systeme` (narrateur italique), `tchat` (défini localement), anonymes `"Une collègue"`.
- `systeme` : 3e personne, présent ; passé simple pour l'intro épique, plus-que-parfait pour rappels. SMS en `{i}« ... »{/i}`.
- Répliques de 1-2 phrases, ping-pong comique puis chute émotionnelle ; aphorisme de clôture en `systeme`.
- `scene bg ... with fade`, `show perso expr at char_left/right/center with dissolve`, `play music audio.X loop fadein`, canal `ambiant1`, `$fade_channel`, `$ renpy.pause(x, hard=True)`, titre `centered`. Fonds de secours via `arc7_jessy_bg()` ; sprites `ilona tokyo/short/streaming`, `theo tokyo`.
- Menus : question-titre, options en phrases complètes.
- Typo : guillemets « », « ... » pour hésitation, apostrophes droites, tirets rares.

## 6. Faiblesses

- `systeme` surexplique (« C'est ça, le piège ») ; tournures répétées (« Tout serait vrai », « Bien sûr que tu as vérifié/testé »).
- Route Théo : blocs de rappels conditionnels plaqués, exposition peu dramatisée.
- Laplage deus ex récurrent ; gags absurdes empilés diluent la tension.
- Route Jessy : peu de conflit, rythme uniforme.
- Incohérences possibles : `define auddio.depressed` (typo) alors que `audio.depressed` est joué ; « chacun sa chambre » vs « je te rejoins au lit » ; « vtubeuse » alors qu'elle est filmée en perruque.
