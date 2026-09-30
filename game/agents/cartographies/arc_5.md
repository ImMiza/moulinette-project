# Arc 5 — Cartographie

Fichiers: `game/arcs/arc_5/arc_5_examens.rpy` (2611 l.). Labels: `arc_5_examens` (entrée) → `arc_5_scene_3` (via `jump` depuis branche cinéma, sinon enchaînement). Sortie: `jump arc_6_diplomes`. Définit `mi` (Micka) + sprites micka (happy/exhausted/gifts).
Thème (en-tête): « Connaître les goûts de quelqu'un ne veut pas dire savoir ce qu'il veut. » Peur vs confiance.

## 1. Résumé de l'intrigue
- **S1 Bibliothèque, 12 janvier**: Ilona épuisée/amaigrie. Théo apporte café + *le bon thé* d'Ilona → Jessy se sent inutile (menu). Laplage (badge « Consultant en Entropie Émotionnelle »). Ilona part. Allan: « Tu ne lui as pas demandé ? » (menu). Jessy ramasse le **stylo violet à étoiles** d'Ilona.
- **S2 Sortie ciné (1 semaine après, pluie)**: si stats hautes → Ilona vient: film « nul » devenu « chef-d'œuvre », mains frôlées, `jump arc_5_scene_3` (saute le café). Sinon SMS d'annulation (53 caractères) → menu. Café: Allan, puis Théo (« le Messi » = Laplage) qui va déposer ses notes à Ilona (absente 2 jours) → menu. Théo peut demander « Est-ce que tu lui fais confiance ? » ; Allan: Théo « ne perd jamais », trouve « un autre angle ».
- **S3 (`arc_5_scene_3`) février, résultats**: Théo propose à Jessy de « gérer » notes, club, festival de printemps et **stream** d'Ilona (qu'elle n'a jamais évoqué: pseudo « Gaming » depuis ses 12 ans, setups à 2h) — et veut que Jessy le propose à sa place. Menu.
- **S4 Saint-Valentin, 14 fév.**: gag Micka (15+ boîtes, profs Tanaka/anglais). Jessy a 3 chocolats d'Alexandre (« Ta fan mystérieuse, bisous, Alexandre, PS : c'est moi »). Toit: Ilona offre chocolats-blocs Minecraft (ambigu) / chocolats d'amitié / rien, selon stats → menu. Si `laisse`: SMS Théo « trié les messages du club ».
- **S5 Bibliothèque nuit**: Laplage (badge « Archiviste des Non-dits ») confident d'Ilona; contenu selon `arc5_etat_relation` (proche: peur que la confiance de Jessy ne dure que si ses choix lui conviennent / fragile: Jessy coupe par blagues / distant: « Qu'on me foute la paix »). Ilona texte: « On peut se voir ? J'ai quelque chose à te demander. »
- **S6 Gare**: rappel du train qui a coupé « Ilona, je voulais te dire que— ». LA question: « Est-ce que tu as peur de me perdre... ou est-ce que tu ne me fais pas confiance ? » (proche: « me feras-tu confiance même si je choisis ce que tu n'espérais pas ? »). Menu. Distant+temps: Ilona part en train.
- **S7 White Day, 14 mars**: Micka 37 gâteaux, prof d'anglais (numéro, opéra ganache), prof de sport. Parc cerisiers → menu réponse.
- **S8 Café Allan/Alex**: « Le problème avec Théo, c'est qu'il n'est jamais le problème » ; « non » = « pas encore ». Allan seul: il « traduit » Théo (4 fois ce mois), doute de ce rôle.
- **S9 Rue**: Sofiane: cousin part à l'armée, lui confie une **AE86** ; permis depuis 6 mois ; projet **montagnes cet été**.
- **S10 Minecraft**: état final de la maison (5 variantes), easter egg Ilonanium, épilogue → Arc VI.

## 2. Personnages
- **Jessy** (protagoniste, narré en 3e pers.): tu, familier (« ça me fait chier »). Anxieux, contrôlant par peur, compense/vérifie; arc = nommer sa peur, rendre l'espace. « Je peux essayer de le penser assez fort pour que ce soit vrai même quand j'ai peur. » / « En pratique, je ne sais pas faire la différence. »
- **Ilona**: épuisée, laconique (« Non. »), lucide, refuse d'être « réparée »/gérée; rêve de stream latent. Registre familier/cru. « Tu ne demandes pas. Tu vérifies. » / « Qu'on me foute la paix. » / « Essayer, c'est déjà beaucoup. »
- **Théo**: calme, attentif, « remarque tout », classe les infos « comme un dossier »; aide = influence; ne s'énerve jamais, « optimise ». Tu. « Ce n'est pas un secret, Jessy. C'est juste que personne ne regarde. » / « Calculer, c'est pour soi. Optimiser, c'est pour le résultat. » / « Je ne suis pas ton ennemi. »
- **Allan**: ironie sèche, analyste, « toujours là quand ça va mal »; ami de Théo (collège), commence à s'en méfier; fatigue d'« expliquer Théo ». « Progrès. » / « On devrait faire des t-shirts « Progrès émotionnel en cours ». »
- **Alexandre (x)**: humour absurde, exclamations en MAJ face à Micka; bienveillant. « C'était techniquement correct et émotionnellement insupportable. » / « Un crime organisé contre le beurre. »
- **Laplage**: apparitions/disparitions, badges absurdes, aphorismes stellaires, pouces (up/horizontal). « Les gens confondent souvent être proche et être propriétaire. »
- **Micka (mi)**: nouveau, garçon ultra-populaire, flegme naïf, courtisé par profs (gag). « L'ironie, c'est de l'affection mal exprimée. »
- **Sofiane (s)**: mystique, phrases oraculaires. « Les étoiles parlent à ceux qui savent se taire. »

## 3. Faits établis (continuité)
- Calendrier: 12 janv. → février (résultats) → 14 fév. → 14 mars → printemps; Arc VI = diplômes/orientation.
- Ilona: épuisée, annule souvent (« 3e fois ce mois »); rêve de **stream** (pseudo IlonaGaming) exposé par Théo; choix à venir: université/stream.
- Théo: notes les plus complètes; peut avoir le **mot de passe du serveur** Minecraft (`laisse`). Allan le connaît depuis le collège; Allan+Alex s'en méfient.
- Phrase coupée par le train (arc antérieur) rappelée à la gare. Deadline « White Day » (branche `temps`).
- Objets: stylo violet (jamais rendu), album photo, chocolats-blocs, panneau « BESOIN D'AIR », salle de repos « reliée mais séparée », coffre libre.
- Sofiane: AE86 du cousin, road-trip montagnes l'été. Micka: profs Tanaka (maths), Yamamoto, anglais, sport.

## 4. Variables / flags / points
- `default`: `arc5_sortie_annulee`, `arc5_theo_proposition`, `arc5_valentin_choix`, `arc5_valentin_offre`, `arc5_question_reponse`, `arc5_white_day_reponse`, `arc5_fin_minecraft`, `arc5_laplage_deuxieme_confidence`, `arc5_allan_voit_theo`, `arc5_allan_parti_cafe`, `arc5_tension_accumulee`, `arc5_theo_dans_maison`, `arc5_cinema_ensemble`, `arc5_etat_relation` (= `etat_relation()` figé en S5).
- Globales: `autonomie_ilona`, `confiance`, `communication`, `influence_theo`, `jalousie`, `lien_jessy_ilona`, `controles`, `evitements`, `pression_stream`, `interruptions_ilona`, `jugement_laplage` (+1 `refuse`/`demande`, +2 `honnete`), `confidences_laplage` (+1 si fragile/distant), `maison_minecraft_ajouts`, `souvenirs`, `ilonanium_points`.
- Barème par tiers: **S** (autonomie+4, comm+2, conf+2, pression−2); **A** (comm+4/+2, conf+2/+1, jalousie−2/−1, lien+2/+1); **C** (comm−4/−2, conf−2/−1, pression+2/+1, evitements+1); **D** (autonomie−4, conf−4, influence+2, jalousie+6, lien−2, controles+1). Souvent + `arc5_tension_accumulee`.
- Menus: S1 thé (D+`interruptions_ilona`, D, A, C); S1 Allan (C, C, A). S2: `silence` C (→ `honnetete` A ou reste), `inquiet` D, `confronte` D, `accepte` S. Café Théo: D, C, A, D (`arc5_allan_parti_cafe`). S3: `partiel` D, `laisse` D (influence+4, `arc5_theo_dans_maison`), `refuse` S, `questionne` S. S4: `rien_peur` C, `souvenir`/`simple` lien+4, `demande` S (+conf+2). S6: `responsable` (autonomie+6), `theo` (jalousie+9, conf−6), `temps` (comm−6), `honnete` (comm+6, lien+3). S7: `grand_geste` C, `espace` S, `retour` A (conf +2 ou −4), `mots` A; bonus si (espace|mots)&(honnete|responsable).
- Seuils: cinéma `(lien>=20 or autonomie>=30) and confiance>=15 and communication>=20`; offre ambigu `lien>=20&conf>=15`, amitié `lien>=10&conf>=8`; Théo interroge si `confronte` ou `jalousie>=12`; Allan avertit si `(arc5_allan_voit_theo or influence_theo>=10) and not arc5_allan_parti_cafe`.
- `remember(...)`: `ilona_libre_sans_abandon`, `jessy_nomme_sa_peur`, `theo_utilise_une_verite`, `maison_respectee`.
- Fin Minecraft: `salle_repos`, `distance`, `theo_presence`, `panneau`, `neutre` → ajouts `salle_repos_arc5`, `construction_loin_arc5`, `coffres_theo_arc5`, `panneau_air_arc5`, `coffre_libre_arc5`.
- Lues d'arcs précédents: `arc4_fin_minecraft`, `arc4_ilona_avec_theo`, `arc4_5_ilona_reaction`, `arc4_5_theo_proposition`, `arc2_photo_reaction`, `arc2_choix_activite_theo`, `arc4_cadeau_jessy`, `arc4_limite_ilona`, `arc3_fin_minecraft`, `arc4_ilona_winter_sprite`, `arc4_theo_winter_sprite`.

## 5. Conventions d'écriture
- Speakers: `j`, `i`, `t`, `a`, `x`, `s`, `laplage`, `mi`, `systeme` (narrateur italique).
- Narration `systeme`, 3e personne, présent, focalisée Jessy; phrases courtes, fragments (« Pas « ça va ». Juste « non ». »), aphorismes de fin de bloc.
- SMS: `systeme "{i}« ... »{/i}"`. Guillemets « » avec espaces; ellipses `...`; tiret cadratin rare (« que— »).
- Mise en scène: `scene bg arc5 ...` + `with fade`/`Dissolve(n)`, `show perso expr at char_left/midleft/center/midright/right`, sprites hiver via `show expression arc4_*_winter_sprite + " expr" as ...`; musique/ambiance systématiques (`play music ... fadein`, canal `ambiant1`), `renpy.pause(..., hard=True)`.
- Menus: prompt `systeme` en tête, 3–4 options, commentaire `# Tier X`.
- Répliques 1–2 phrases; Micka/Alex = interludes comiques.

## 6. Faiblesses
- Tics: « La question reste suspendue », « Le silence […] lourd », « c'est pour ça que ça fait mal », « Essayer, c'est déjà beaucoup » (×3).
- Morale explicitée par Allan/Laplage/Ilona: thérapie verbalisée.
- Gag Micka (profs séductrices) répété S4/S7, même chute.
- Incohérences: `inquiet` tombe dans le `else` « Rien de spécial » au café; branche cinéma saute le café (stylo jamais rendu); `responsable` exclu de `salle_repos` et de l'épilogue; « même café qu'au début du mois » (≠ janvier); `partiel` taggé D malgré dialogue assertif.
- Sofiane: scène isolée, pur setup.
