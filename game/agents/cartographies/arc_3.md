# Arc 3 — Cartographie

Fichiers: `game/arcs/arc_3/arc_3_rentree.rpy` — label unique `arc_3_rentree` (titre « Arc III - Rentrée : les regards. »). Aucun call. Sortie: `jump arc_4_noel`. Lit des variables d'arc 2 (`arc2_reaction_coucher`, `arc2_choix_activite_theo`).

## 1. Résumé de l'intrigue
- **Train, septembre**: ouverture selon arc 2 (froid/`silence|interrogatoire|suivre|disparaitre`, complice/`confiance`, gêné/`dix_minutes`, défaut). Allan annonce le festival culturel: sa classe tient un café, classe de Jessy/Ilona fait la déco, Théo au comité de coordination. Ilona propose le thème **Blocky House Café** (= leur maison Minecraft).
- **Couloir 2e étage**: plan absurde d'Alexandre; Théo recadre utilement (« fausse porte importante ») → gêne de Jessy difficile à nommer.
- **Stand, J+3**: rumeur chuchotée (porte-clés rendu par Théo à la plage, « Jessy regardait ailleurs. Pathétique »). **Menu 1**. Théo: « on te met une pression »; Ilona le recadre.
- **Jour du festival**: Théo répond à la place d'Ilona → neutralité d'Allan se fissure. Ilona brille face au public, esquive la question d'Allan. **Menu 2**.
- **Couloir**: Allan/Alexandre enquêtent sur Laplage. Sofiane: « Faites attention à ceux qui creusent » (vise Théo).
- **Cour**: Ilona achète une étoile en sucre; confie à Laplage sa colère et que la gentillesse de Théo « me repose. Et après je m'en veux ».
- **Couloir, duel** Théo/Jessy. **Menu 3**. Sofiane console (thé vert). Ilona revient, avoue colère + attirance pour l'attention de Théo, craint que leur souvenir devienne spectacle. **Menu 4**.
- **Classe, soir**: bilan; Sofiane a fait tout le planning de rangement. Sort du panneau selon menu 4. Allan seul efface 3 brouillons.
- **Minecraft nuit**: fin selon menu 4 (panneau / rangement / porte fermée / destruction cuisine d'été). **Menu 5** (étoile) sauf si destruction. Narration finale: « La rentrée n'a rien tranché ».

## 2. Personnages
- **Jessy** (joueur, protagoniste): tutoie, humour sec d'autodérision, jalousie assumée ou refoulée selon choix, honte plus que colère. « On est condamnés. » / « Je suis jaloux. […] C'est dit, c'est moche » / « je t'aime assez pour ne pas transformer cette haine en laisse. »
- **Ilona**: absurde pince-sans-rire, phrases courtes, refuse d'être sauvée ou qu'on parle pour elle, lucide sur sa propre ambivalence envers Théo. Vulgarité rare (« ignorer les cons »). « C'est un sable engagé. » / « Je n'ai pas demandé ton avis. » / « Je te demande de ne pas me punir parce que tu as peur. »
- **Théo**: calme, compétent, « vérité utilisée comme une lame », exploite silence/honte; glisse vers manipulateur. « Tu vois ? Même là, tu préfères qu'elle devine. » / « Attention, Jessy. »
- **Allan**: médiateur, ironie administrative (« Reçu chef »); neutralité fissurée, ne sait pas ce qu'il pense.
- **Alexandre** (`x`): comique, portes inutiles. « Je déteste quand la géométrie gagne. »
- **Sofiane** (`s`): oracle laconique, métaphores de routes de montagne, organisateur discret. « ralentir n'est pas reculer. »
- **M. Laplage**: aphorismes absurdes, ubiquité, vouvoyé. « Un cœur vide prend de mauvaises décisions. »

## 3. Faits établis (continuité)
- Septembre, uniformes, train; lycée (couloir 2e étage, cour).
- Festival: Blocky House Café, « porte inutile », menu « salle moyennement importante » (référence intime). Tout le café vendu.
- Rumeur publique: porte-clés d'Ilona rendu par Théo à la plage; Jessy vu comme « pathétique ».
- Théo verbalise ouvertement sa stratégie; Jessy le déteste à la fin du duel.
- Sofiane: routes de montagne, thé vert, planning clés de la réserve.
- Laplage: confidences = « dette » (commentaire code → « porte de l'arc 6 »).
- Allan: 3 brouillons « En vrai, moi je pense que— » effacés.
- Talent d'Ilona pour captiver un public (non nommé) — lien probable `pression_stream`.
- Étoile en sucre: reste sur le bureau d'Ilona (ou mangée).
- Maison Minecraft: cuisine d'été (construite après la plage), salle secrète, porte inutile.

## 4. Variables / flags / points
- `default`: `arc3_reaction_rumeur`, `arc3_aide_stand`, `arc3_reaction_laplage`, `arc3_fin_minecraft` (= "").
- Tests: `arc2_reaction_coucher`, `arc2_choix_activite_theo`, `jalousie >= 6/9/3`, `souvenirs["jessy_nomme_sa_peur"]`, `ilona_peut_finir_ses_phrases < 2`, `interruptions_ilona > interruptions_reconnues`.
- Train: `lien_jessy_ilona += 1`.
- **Menu 1** `arc3_reaction_rumeur`: `demander_ilona` (autonomie_ilona+4, communication+2, confiance+2, ilona_peut_finir_ses_phrases+1, pression_stream-2) / `silence_paralysie` (communication-4, confiance-2, pression_stream+2, evitements+1) / `defendre_immediat` (autonomie_ilona-4, confiance-4, influence_theo+2, jalousie+6, lien_jessy_ilona-2, controles+1) / `blague_desarm` (lien_jessy_ilona+4). Si blague/silence: influence_theo+1, `remember("theo_utilise_une_verite")`.
- **Menu 2** `arc3_aide_stand`: `distance_honnete` (communication+4, confiance+2, jalousie-2, lien+2, `remember("jessy_nomme_sa_peur")`) / `aider_retrait` et `demande_directe` (autonomie+4, communication+2, confiance+2, pression_stream-2) / `blague_defense` (pack négatif comme `defendre_immediat`).
- Laplage: `confidences_laplage += 1` si `ilona_peut_finir_ses_phrases < 2`; `jugement_laplage += 1`.
- Duel: `remember("theo_utilise_une_verite")` inconditionnel. **Menu 3** (sans variable dédiée): silence (pack négatif évitement), admettre (communication+4, confiance+2, jalousie-2, lien+2), refuser duel (pack autonomie), rentrer dedans (pack contrôle).
- **Menu 4** `arc3_reaction_laplage`: `demander_besoin` (communication+4, confiance+2, ilona_peut_finir+1, jalousie-2, lien+2; puis lien+1) / `excuse_precise` (idem sans ilona_peut_finir; `remember("jessy_repare")` si blague; interruptions_reconnues/reparees+1; puis confiance+1) / `demande_reponse` (pack contrôle; puis pression_stream+1) / `promesse_theo` (pack évitement; puis influence_theo+1, pression_stream+1).
- Classe: besoin/excuse → lien+1, confiance+1; autres → pression_stream+1.
- `arc3_fin_minecraft`: `panneau_finir_phrase` (communication+1, autonomie+1, ajout `panneau_phrases_tremblent_arc3`) / `rangement_silencieux` (confiance+1, `cuisine_ete_rangee_arc3`) / `porte_fermee` (pression_stream+1, `porte_inutile_fermee_arc3`) / `destruction` (pression_stream+2, lien-1, `maison_minecraft_destructions` += `cuisine_ete_arc3`, `souvenirs["maison_respectee"] = False`) / `lanterne_cour` (inatteignable).
- **Menu 5** étoile: trace salle secrète (`remember("maison_respectee")`, lien+2) / manger (autonomie+2, communication+1, confiance+1, `ilonanium_points += 1`, pression_stream-1).

## 5. Conventions d'écriture
- Speakers: `j`, `i`, `t`, `a`, `x`, `s`, `laplage`, `systeme` (narrateur italique, sans nom).
- Narration 3e personne, présent, focalisation surtout Jessy (parfois Ilona, Allan). Aphoristique: « Pas X. Y. », triades anaphoriques.
- Sprites `<perso> festival <émotion>` + `at char_left/midleft/center/midright/right`; `scene … with fade`, `with dissolve`, `hpunch`; `renpy.pause(x, hard=True)` pour silences; musique/ambiance changeant par scène (`festi`, `festiMC`, `sadPiano`, `tensePiano`, `mcnight`).
- Menus: prompt narratif + 4 choix (schémas récurrents: autonomie / communication / évitement / contrôle).
- Répliques courtes (1–2 phrases). Guillemets « », ellipses « ... », tiret long « — » pour coupure, `{i}` pour emphase.

## 6. Faiblesses
- Narration surexplique l'émotion (« Jessy a défendu Ilona. Mais… » dupliqué l.271/274).
- Tics: « Pas X. Y. », « Mais il sait aussi… », « Ce n'est pas… C'est… ».
- Sofiane et Laplage interchangeables (oracles).
- Théo manipulateur trop appuyé, perd en ambiguïté.
- Branche `lanterne_cour` morte.
