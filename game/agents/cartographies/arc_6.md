# Arc 6 — Cartographie

Fichiers: `game/arcs/arc_6/arc_6_diplomes.rpy` (« Après aujourd'hui », remise des diplômes).
- Labels: `arc_6_diplomes` (entrée, scènes 1-4) → `arc_6_calcul` (passe-plat) → `arc_6_decision` → `arc_6_decision_jessy` → `jump arc_7_jessy` | `arc_6_decision_theo` → `arc_6_bascule_theo` → `jump arc_7_theo` (seul point d'entrée autorisé vers arc_7_theo).
- Fonctions init: `arc6_penche()`, `arc6_palier()`, `arc6_calcule_verdict()`, `arc6_construit_attaques_theo()`, `arc6_bg()`, `arc6_flashbg()`. Dépend de `etat_relation()` (script.rpy) et `SEUIL_JESSY` (180).

## 1. Résumé de l'intrigue
- **Entrée**: route calculée dès le début (`arc6_calcule_verdict`), ton fixé par `arc6_palier` (jessy/indecis/theo). Choix du jour = coloration seulement.
- **Sc.1 Stylo violet** (classe, 7h50): Jessy a gardé le stylo d'Ilona depuis le 12 janvier. Ilona (pain au lait) s'assoit plus ou moins loin selon penchant. Rappels conditionnels (écharpes, miniature, mot de passe serveur changé). Menu stylo.
- **Sc.2 Cérémonie** (gymnase, 340 noms): Micka, 3 enveloppes dont convocation. Gâteau « BONNE ROUTE »: « planète » vs « ballon ». Sofiane rend à Allan l'enveloppe de décembre (« Les lumières ne disent pas où aller… »). Allan confronte Théo; Théo annonce Tokyo (6 avril, 11 jours), offre sincère. SMS Ilona: « Salle 3-B. J'ai un feutre. »
- **Sc.3 Récapitulatif** (classe décorée): Ilona « raconte l'année », veste de Jessy sur les genoux. Vignettes flashback conditionnelles (max 8): plage, rumeur/porte-clés, maison Minecraft, Noël, nuit avec Théo, cinéma (main), gare. « Je saute un truc ». Menu posture. Vignette « phrase jamais finie », craquage/larmes si fatigue. « Tu as pas parlé de toi. » 3 mots au feutre sous le col de la veste (« Tu regarderas ce soir »).
- **Sc.4 Offre de Théo** (couloir vide): Jessy s'écarte. Studio Tokyo (équipe, modération, planning). « Opportunité ou venir avec toi ? » → « Les deux » / « Je veux que tu viennes ». Théo attaque Jessy avec faits réels des arcs 2-5. Ilona: « Et toi, qu'est-ce que tu veux ? » Menu clé. Ultimatum: 3 avril.
- **Sc.5 Décision** (cour, 26 mars): Ilona tranche, « vous allez me laisser finir ma phrase ».
  - Jessy: stylo rangé dans trousse (objet qui sert), carnet de Théo au fond du sac; reproches assumés à Jessy; stream « petit, amateur ». Théo part seul. Soir: dernier geste Minecraft (menu).
  - Théo: veste rendue pliée, stylo poche extérieure; « T'as pas mal fait. T'as fait lentement. » Jessy ne lit pas les 3 mots.
- **Bascule onze jours**: 28 mars confirmation, 31 mars rangement, 3 avril passe, 6 avril gare (tenues `tokyo`), Jessy absent. Image `bg arc6 evil theo` + sirène 5 s (présage sinistre).

## 2. Personnages
- **Jessy** (joueur, masculin « il »): tutoie, phrases courtes, humour gamer comme esquive, peur de perdre, tendance à réparer/couper. Évolue vers écoute silencieuse (« rester, c'est une action »).
  - « Ceci est un objet de quête. Je le rends contre trois émeraudes. »
  - « Je crois que si je dis un truc, je vais essayer de le réparer. »
- **Ilona**: centre émotionnel; lucide, aphorismes secs, familier (« j'ai pas », « je me fous »), mange quand quelque chose commence, fatiguée « depuis septembre », parle des autres jamais d'elle. Reprend la parole, exige de finir ses phrases, choisit elle-même.
  - « Je déteste le mot « souvenir ». »
  - « Je te demande une seule chose. Et toi, qu'est-ce que tu veux ? »
  - « Je me suis sentie comme un guichet. »
- **Théo**: calme, factuel, sûr de lui, dangereux parce que vrai; « Je sais compter. » Première hésitation de l'année face à Ilona; jalousie si Jessy répond juste.
  - « J'appelle ça lui foutre la paix. »
  - « Je vais pas inventer. J'ai assez de vrai. »
  - « Trois avril, Ilona. Après, je réserve pour une personne. »
- **Allan** (`a`): ami de Théo depuis 10 ans, « traducteur » de tous; arc perso: enveloppe de Sofiane, cesse de traduire. « Merde. »
- **Sofiane** (`s`): énigmatique, répliques-oracles, écoute tout. « J'écoute toujours. Personne ne fait attention. » « Je te dépose. » (sans voiture)
- **Alexandre** (`x`) taquin; **Micka** (`mi`, défini arc 5) comique (« optimisme administratif »).

## 3. Faits établis (continuité)
- Cérémonie: 26 mars (fin mars), 10h, gymnase; cerisiers pas encore ouverts (ouvrent semaine suivante).
- Théo part à Tokyo le **6 avril**, studio gérant 3 chaînes; deadline **3 avril**. Route Théo: Ilona part (2 places), stream à Tokyo.
- Stylo violet d'Ilona gardé depuis 12 janvier.
- Veste d'uniforme de Jessy: **3 mots au feutre sous le col**, contenu jamais révélé (à payer en arc 7).
- Carnet offert par Théo (Noël); écharpes (Théo / Jessy); miniature de la maison avec « couloir raté ».
- Panneau Minecraft « ICI, LES PHRASES ONT LE DROIT DE TREMBLER »; « porte inutile ».
- Micka: convocation chez le proviseur adjoint. Allan garde l'enveloppe de Sofiane. Photo maid de Sofiane chez Alexandre.
- Allan ↔ Théo: rupture tacite, Allan ne traduit plus.
- Distributeur 2e étage (pièces de 10), bâtiment en travaux l'été. Salle 3-B. « Zéro yen » → cadre Japon implicite.
- Running gags: « Personne ne fait ça », planète/ballon, Ilona mange.

## 4. Variables / flags / points
- Défauts: `arc6_stylo` (rendu/garde/rendu_explique/blague), `arc6_offre_theo` (laisse/question/accusation/aveu_vide), `arc6_ilona_a_pleure`, `arc6_gateau_planete` (jamais modifié), `arc6_conversation` (que_veux_tu/eviter/aveu_interruptions/partir/continuer), `arc6_derniere_construction` (porte_ouverte/panneau_partir/silence/cadenas, route Jessy seulement), `arc6_vignettes_jouees` (plage, rumeur, maison, noel, nuit_theo, cinema, gare, phrase_finie, craquage), `arc6_vignettes_count`, `arc6_flashback`, `arc6_theo_attaques`, `arc6_attaque_1..3`, `arc6_score`, `arc6_route`, `arc6_penchant_debut`, `arc6_penchant`, `arc6_derive` (compat, inutile), `souvenir_flag_bonne`, `controle_repetitif` (store).
- Verdict: `arc6_score = espace + posture + recidive - dette`; espace = `autonomie_ilona*4 + ilona_peut_finir_ses_phrases*6 + interruptions_reparees*6 + communication + confiance`; dette = `influence_theo*3 + max(0,controle_repetitif)*8 + pression_stream*2 + jalousie*2 + confidences_laplage*4`; posture via `souvenirs["jessy_nomme_sa_peur"|"jessy_repare"|"ilona_libre_sans_abandon"|"maison_respectee"|"theo_utilise_une_verite"]`; recidive via `controles`, `evitements`; +20 si `interruptions_reparees>=2` et `jessy_repare`. `controle_repetitif>=3` → theo forcé; sinon `>= SEUIL_JESSY` → jessy.
- Lus (arcs antérieurs): `arc2_choix_activite_theo`, `arc3_reaction_rumeur`, `arc3_aide_stand`, `arc3_fin_minecraft`, `arc4_ilona_avec_theo`, `arc4_limite_ilona`, `arc4_cadeau_jessy`, `arc4_5_ilona_reaction`, `arc4_5_sofiane_maid`, `arc5_theo_proposition`, `arc5_fin_minecraft`, `arc5_cinema_ensemble`, `arc5_question_reponse`, `arc5_tension_accumulee`, `pression_stream` (craquage si ≥12 ou tension ≥8), `influence_theo` (≥8 → « Tu vas regretter »).
- Menus: stylo (4), posture récap (4, aucun effet stocké), « Que répond Jessy ? » (5), dernière construction (4). Aucun ne modifie la route.

## 5. Conventions d'écriture
- Speakers: `j` Jessy, `i` Ilona, `t` Théo, `a` Allan, `x` Alexandre, `s` Sofiane, `mi` Micka, `systeme` narrateur (italique).
- Narration `systeme`: 3e personne, présent, focalisation interne légère, maximes finales (« C'est exactement le problème »).
- Dialogues très courts (1 phrase/ligne), rythmés par `$ renpy.pause(x, hard=True)`.
- `scene … with fade`, `show … at char_left/midleft/center/midright/right` + `with dissolve`, flashbacks `Dissolve(1.5)`; expressions neutral/smile/determined/fatigue/defensive/jealousy/listening/minecraft/tokyo.
- Triple branchement systématique `if arc6_penchant == "jessy"/"indecis"/else`.
- Typo: guillemets « », ellipses « ... », `{i}` pour citations écrites, pas de tirets cadratins.

## 6. Faiblesses
- Tics répétés: « Personne ne fait ça », « pour la première fois de l'année », « C'est exactement le problème », « C'est nouveau ».
- Choix sans poids (route fixée à l'entrée), menus posture sans flag.
- `arc_6_calcul` vide, `arc6_gateau_planete`/`arc6_derive` morts; `aveu_vide` → `conversation="continuer"` incohérent.
- Ilona surécrite en aphorismes, voix proche du narrateur.
- Image « evil theo » + sirène: rupture de ton abrupte.
