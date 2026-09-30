# Arc 4 (+ 4.5) — Cartographie

Fichiers:
- `game/arcs/arc_4/arc_4_noel.rpy` — label `arc_4_noel` (entrée). Fin: `call arc_4_5_maid_cafe` si `lien_jessy_ilona >= 10 and communication >= 25 and confiance >= 15` ; `call arc_4_5_theo` si `arc4_ilona_avec_theo` ; puis scène Minecraft → `jump arc_5_examens`.
- `game/arcs/arc_4/arc_4_5_maid_cafe.rpy` — label `arc_4_5_maid_cafe` (interlude 4.5 « bonne fin », `return`).
- `game/arcs/arc_4/arc_4_5_theo.rpy` — label `arc_4_5_theo` (interlude 4.5 « mauvaise fin », `return`, POV omniscient, Jessy absent).
- Les deux 4.5 sont mutuellement exclusifs en pratique (confiance >= 15 vs <= 8) ; possible qu'aucun ne se déclenche.

## 1. Résumé de l'intrigue

**arc_4_noel (décembre)**
1. Train (Jessy/Ilona): rappel fin Minecraft arc 3. Sortie prévue au marché de Noël. Jessy cache un paquet.
2. Galerie (Jessy/Alexandre): cadeau = miniature de la maison Minecraft avec ses erreurs. Menu 1 (aveu, souvenir, écharpe chère par panique, blague panneau, rien offrir).
3. Marché: Théo offre à Ilona un mini carnet de croquis (elle avait dit en juillet oublier ses idées dehors). Menu 2 (réaction Jessy). Si acide/crue: duel Jessy–Théo, Ilona: « Vous allez arrêter de transformer chaque putain de cadeau en duel. »
4. Laplage à Théo: un souvenir bien placé est une clé qui peut « verrouiller quelqu'un dedans » ; « tu gardes la clé ».
5. Allan/Alexandre: Théo « range ses souvenirs comme des arguments ». Enveloppe sans destinataire de Sofiane ; Allan ne la prend pas ; Sofiane la récupère.
6. Rivière: Ilona, carnet + mochi (menu). Laplage Père Noël: « Poser une limite n'est pas casser le cadeau ».
7. Jessy avoue la compétition. Menu 3 (limite). Ilona: « j'ai le droit de vous aimer tous les deux différemment sans que ce soit un classement ». Menu 4 (accueil). Issue: garde les cadeaux / rentre avec Allan / suspens.
8. Sortie: Théo propose de raccompagner. Si `influence_theo >= 10 and confiance <= 8 and demande_theo`: Ilona part avec lui (« quelqu'un qui ne me demande pas de le rassurer »).
9. Appels 4.5, puis Minecraft sous neige: 4 fins.

**arc_4_5_maid_cafe** (bonne synergie): Jessy et Ilona prolongent la soirée à deux sous la neige, entrent dans un maid café (menu). Sofiane y travaille en maid (« La route a faim »), exige le secret vis-à-vis d'Allan/Alexandre. Rire, rien résolu. « On reviendra. » « Promis. »

**arc_4_5_theo** (Ilona part avec Théo): parc, Théo lui donne son écharpe. Réaction d'Ilona calculée (pas de menu): `accepte` (rêve de streamer, Théo propose de gérer → « Bien sûr. » = dette), `directe` (« tu m'aides… ou tu veux être celui qui m'aide ? »), `prudente` (« du temps »). Même café: Laplage en maid, pouce horizontal. Fin: « remplacer une cage par une autre ».

## 2. Personnages

- **Jessy** (`j`, joué): tu, phrases courtes, « Ouais », « putain » rare, autodérision. Peur de perdre Ilona ; jalousie vs honnêteté selon choix. « Je veux gagner. Et je déteste tout ce que je viens de dire. » / « Émotionnellement, il va fuir. »
- **Ilona** (`i`): tu, pince-sans-rire, jurons rares et pesants, fatigue (stream), limites nettes, humour cosmique. « Je ne suis pas un trophée qu'on gagne avec des souvenirs bien placés. » / « Tu as l'air trop cosmique pour un dessert. »
- **Théo** (`t`): doux, attentif, minimaliste, stratège de la mémoire ; masque qui craque (« Moi ? »). « Un rien. » / « Je fais attention. » / « Je te propose juste… un espace. »
- **Alexandre** (`x`): vannes sèches, lexique architecture, lucide. « Si tu ne décides pas, ta peur le fera à ta place. » / « Respect du matériau source. »
- **Allan** (`a`): organisateur, humour logistique, médiateur neutre qui commence à s'en lasser, soutien physique (main sur épaule). « Je marche lentement, mais avec fiabilité émotionnelle. »
- **Sofiane** (`s`): aphorismes cryptiques, conducteur (« la route »), sérieux absolu en maid, vouvoie « Maîtres ». « Les lumières ne disent pas où aller. Elles disent juste qu'il fait nuit. »
- **Monsieur Laplage** (`laplage`): oracle absurde, tutoie les jeunes, Ilona le vouvoie ; langage de pouces (levé/horizontal). « Je vends surtout des pauses. »

## 3. Faits établis (continuité)

- Décembre ; festival = septembre (arc 3) ; plage = juillet (arc 2).
- Carnet de Théo: minuscule, couverture noire, coins renforcés, étiquette intérieure.
- Miniature de Jessy: maison Minecraft (couloir sans sortie, cuisine trop grande, pièce cachée/secrète), papier bleu sombre ; variante panneau « PIÈCE MOYENNEMENT IMPORTANTE, ÉDITION NEIGE ». Si non donnée: reste dans le sac « en attente ».
- Écharpe chère de Jessy (branche panique) → bloc de laine bleu dans un coffre Minecraft.
- 4.5 Théo: Ilona porte l'écharpe de Théo ; rêve « streamer pour de vrai » ; Théo propose de gérer son stream.
- Sofiane: job secret au maid café (3 mois, paie l'essence) ; Jessy/Ilona promettent de revenir et de ne rien dire. Allan/Alex savent seulement qu'il a « un service ». Enveloppe sans destinataire gardée par Sofiane (fil ouvert).
- Laplage: Père Noël intérimaire « Service des horizons froids » ; remplace en maid au même café (4.5 Théo).
- Running jokes: « le Messi » (Théo pour Laplage), mochi/astre, panneau, « JESSY A RUINÉ NOËL ».
- Commentaire code: confidence à Laplage = dette, « porte de l'arc 6 ».

## 4. Variables / flags / points

- Arc-locales: `arc4_cadeau_jessy` (miniature_aveu, miniature_souvenir, cadeau_couteux, blague_interne, discussion_honnete) ; `arc4_reaction_cadeau_theo` (reconnaitre, demander_ressenti, laisser_repondre, verite_crue, blague_acide) ; `arc4_limite_ilona` (demande_theo, cadeau_preuve [si couteux], cadeau_respirant [si miniature], parole_sans_verdict [si discussion], marche_silencieuse) ; `arc4_accueil_limite` (demander, silence, accueillir, accuser_theo, nommer_peur) ; `arc4_fin_minecraft` (miniature_trace, echarpe_coffre, carnet_hors_maison, neige_sur_toit) ; `arc4_carte_sofiane_lue` (toujours True) ; `arc4_mochi_cosmique` ; `arc4_ilona_avec_theo` ; `arc4_ilona_winter_sprite`, `arc4_theo_winter_sprite` (set, inutilisés) ; `arc4_5_sofiane_maid` ; `arc4_5_theo_proposition` (gestion_stream, question, temps) ; `arc4_5_ilona_reaction` (accepte, directe, prudente).
- Jauges modifiées: `communication`, `confiance`, `jalousie` (via `max(0, …)`), `lien_jessy_ilona`, `autonomie_ilona`, `pression_stream`, `evitements`, `controles`, `influence_theo`, `lien_ilona_theo`, `ilona_peut_finir_ses_phrases`, `interruptions_ilona` (+1 si blague_acide), `interruptions_reconnues`, `interruptions_reparees`, `confidences_laplage` (+1 si `ilona_peut_finir_ses_phrases < 4`), `jugement_laplage` (+1 rivière, +1 4.5 Théo), `ilonanium_points` (+1 mochi mangé).
- Barème: sain ≈ `communication` +4/`confiance` +2 ; évitement ≈ −4, `evitements` +1 ; contrôle ≈ `jalousie` +6/+9, `controles` +1.
- `remember(...)` (dict `souvenirs`): `maison_respectee`, `jessy_nomme_sa_peur`, `ilona_pose_une_limite` (si `ilona_peut_finir_ses_phrases >= 2 and interruptions_ilona <= interruptions_reparees`), `jessy_repare`, `theo_utilise_une_verite`, `ilona_veut_streamer_serieusement`.
- `maison_minecraft_ajouts.append`: `miniature_noel_arc4`, `espace_calme_arc4`, `echarpe_coffre_arc4`, `coin_dehors_carnet_arc4`, `neige_toit_arc4`.
- Testées (arcs antérieurs): `arc3_fin_minecraft` (destruction, porte_fermee, panneau_finir_phrase, rangement_silencieux), `arc2_choix_activite_theo` (suivre, dix_minutes), seuils `jalousie >= 9`, `pression_stream >= 6`, `influence_theo >= 6`, `lien_ilona_theo >= 2`, `confidences_laplage >= 1`, `communication >= 25` (garde-carnet).
- Réaction 4.5 Théo: `influence_theo >= 14 and autonomie_ilona <= 0` → accepte ; sinon `communication >= 15 or ilona_peut_finir_ses_phrases >= 3` → directe ; sinon `autonomie_ilona >= 15` → prudente ; sinon accepte.

## 5. Conventions d'écriture

- Speakers: `j`, `i`, `t`, `a`, `x`, `s`, `laplage`, narrateur `systeme` (italique, sans nom). Narration 3e personne, présent, focalisée Jessy (omnisciente en 4.5 Théo et scène Théo/Laplage).
- Sprites `perso winter <émotion>` (+ `scarf`), `laplage christmas/maid`, `sofiane maid` ; positions `char_left/midleft/center/midright/right`. `with fade`/`dissolve`, `renpy.pause(x, hard=True)`, `fade_channel`. Canaux `music`, `ambiant1`, `sound` (`audio.laplage`, `audio.wow`).
- Menus: prompt narratif, 2–5 options, options conditionnelles, effets `$` puis dialogue.
- Répliques courtes, ping-pong. Guillemets « », ellipses « ... ». Aphorismes fréquents.

## 6. Faiblesses

- Tics: « Pas X. Pas Y. Juste Z. », « La phrase claque », « Le rire aide. Un peu. ».
- `systeme` sur-explique le sous-texte ; tout le monde parle en aphorismes → voix qui se confondent.
- 4.5 Théo: réplique citée 3 fois et mal citée ; condition commentée (`>= 5`, `<= 2`) ≠ code (`>= 10`, `<= 8`) ; miniature « jamais regardée » alors que non offerte en `demande_theo` ; « Jessy rentré en métro » alors qu'il reste au marché.
- Code mort: `arc4_carte_sofiane_lue` toujours True ; variables sprite inutilisées ; fonds placeholder.
