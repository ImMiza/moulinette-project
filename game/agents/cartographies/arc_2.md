# Arc 2 — Cartographie

Fichiers: `game/arcs/arc_2/arc_2_plage.rpy` — label unique `arc_2_plage` (appelé par `jump arc_2_plage` depuis arc_1_printemps) → fin `jump arc_3_rentree`. Aucun call.

## 1. Résumé de l'intrigue
Juillet, samedi, sortie plage. Linéaire, 7 menus, branches internes via `arc2_choix_activite_theo`.
1. **Couloir école** : Allan annonce la plage, Théo invité (Jessy le connaît via Allan). Menu 1.
2. **Train** : Ilona veut une « cuisine de plage » (4e cuisine). Sofiane apparaît.
3. **Parasol** : château d'Alexandre. Théo pose le sac d'Ilona à l'ombre sans demander. Menu 2.
4. **Stand kakigōri** : Ilona parle seule pour choisir. Perd son porte-clés bloc ; Jessy fouille en vain, Théo le retrouve, doigts frôlés, Ilona rougit. Menu 3.
5. **Photo** : Jessy au bord, Ilona près de Théo. Menu 4. Ilona prend la « gelée marine lumineuse ».
6. **Parasol** : Théo coupe Ilona ; Allan : « Ralentis. »
7. **Mares** : « Je peux y aller ? ». Menu 5 (pivot), puis commentaire d'Alexandre.
8. **Jetée** (confiance/dix_minutes/blague) : Théo s'excuse, « Avec toi, j'aimerais juste... écouter ». `suivre` : confrontation, « T'as tout gâché, mec ». `disparaitre` : Théo « En te laissant exister sans lui ».
9. **Objets trouvés** : Laplage + Ilona (objets rendus trop vite, « La plage est sèche »). Allan/Alexandre ; Ilona veut « finir mes phrases avant qu'on trouve une solution pour moi ».
10. **Coucher de soleil** : Jessy + Alexandre puis Ilona, dialogue selon branche. Menu 6.
11. **Maison Minecraft, nuit** : issue selon `arc2_retour_minecraft`. Menu 7. Narration de clôture (3 variantes).

## 2. Personnages
- **Jessy** (joueur, masculin) : phrases courtes, tutoie, humour pour masquer, vulgaire sous stress. Jalousie envers Théo, se sent « remplaçable ». « Parce que j'ai peur. » / « Parce que j'ai paniqué, bordel ! » / « Je sais. Mais tu aimes bien les trucs inutiles. »
- **Ilona** : humour absurde (cuisines, portes inutiles), phrases coupées par autrui, répond « trop vite » pour désamorcer, besoin d'autonomie. Tranchante si surveillée. « Je voulais marcher. Pas passer un test de fidélité. » / « Il m'a regardée en premier. » / « Va te faire foutre, Jessy. »
- **Théo** : attentif, efficace, anticipe, décide à la place (« Il propose comme si c'était déjà décidé »). Codé manipulateur doux : sourire qui « ne monte pas jusqu'aux yeux », note les silences. « Je fais attention. » / « Parce qu'il sait que je te comprends. »
- **Allan** : organisateur, ami de Théo mais le recadre, protège Ilona. « On garde une place sans panneau. »
- **Alexandre** (`x`) : humour méta/administratif, voix de la raison. « Alors reviens avant que ton absence devienne une phrase. »
- **Sofiane** : cryptique. « La mer a appelé. J'ai laissé sonner deux fois. »
- **Monsieur Laplage** : oracle à paraboles, gag « plage sèche ».

## 3. Faits établis (continuité)
- Jessy et Ilona en couple implicite (fidélité évoquée) ; maison Minecraft commune : plusieurs cuisines, « cuisine d'été », portes inutiles, « salle moyennement importante », « couloir sans issue ».
- Porte-clés bloc d'Ilona retrouvé par Théo ; coquille blanche offerte par Jessy (branche) ; photo où Jessy est « exilé » (2e photo si `refaire_doux`).
- Ilona : préfère l'ombre, parle seule pour choisir, veut finir ses phrases ; refuse un « comité » contre Théo.
- Théo coupe les gens (« Je fais ça trop souvent »), Allan l'a recadré.
- Gags : château inhabitable, pelle « vie indépendante », « Commission temporaire des phrases inachevées », Laplage « possède légalement le sable », gelée lumineuse.
- Référence printemps : Jessy a laissé Ilona finir ses phrases.

## 4. Variables / flags / points
Locales : `arc2_photo_reaction`, `arc2_choix_activite_theo`, `arc2_reaction_coucher`, `arc2_retour_minecraft`.
Globales : `lien_jessy_ilona`, `communication`, `confiance`, `jalousie`, `autonomie_ilona`, `influence_theo`, `controles`, `pression_stream`, `evitements`, `interruptions_ilona`, `interruptions_reconnues`, `interruptions_reparees`, `lien_ilona_theo`, `jugement_laplage` (+1), `ilonanium_points`.
Tests : `ilona_peut_finir_ses_phrases >= 2`, `communication < 0`, `lien_jessy_ilona >= 10`, `jalousie >= 6 / > 0 / >= 9`, `autonomie_ilona >= 12`, `communication >= 12`.
`remember()` : `ilona_libre_sans_abandon`, `jessy_nomme_sa_peur` (x2 possibles), `jessy_repare`, `maison_respectee`.
- M1 : blague château (lien+2) ; demander (comm+2, conf+1, jal-1, lien+1) ; trop vite (auto-2, conf-2, infl+1, jal+3, lien-1, ctrl+1) ; se taire (comm-2, conf-1, stream+1, evit+1).
- M2 : aider (auto+2, comm+1, conf+1, stream-1) ; « zone Ilona » (lien+2) ; regarder Théo (= « trop vite »).
- M3 : remercier (comm+4, conf+2, jal-2, lien+2) ; coquille (lien+4) ; blague / se taire (comm-4, conf-2, stream+2, evit+1).
- M4 `arc2_photo_reaction` : `silence_photo`, `refaire_doux` (comm+1, jal+1), `remarque_neutre`, `accepter_compliment` (lien+2).
- M5 `arc2_choix_activite_theo` : `confiance` (auto+6, comm+3, conf+3, stream-3), `suivre` (auto-6, conf-6, infl+3, interruptions_ilona+1, jal+9, lien-3, ctrl+1), `blague_jalouse`, `dix_minutes` (comm+6, conf+3, jal-3, lien+3), `disparaitre`. `lien_ilona_theo += 2` sauf `suivre`.
- M6 `arc2_reaction_coucher` : `silence`, `reparation` (+répare interruptions si `interruptions_ilona > interruptions_reconnues`), `interrogatoire` (jal+6, conf-4…), `peur_nommee`.
- `arc2_retour_minecraft` : `porte_fermee` (silence/interrogatoire ou suivre/disparaitre), `sortie_couloir` (comm≥12), `lanterne_bleue`, `silence`.
- M7 : gelée (cachée si `porte_fermee` ; `maison_respectee`, ilonanium+1, lien+2) ; bloc lumineux (rien).

## 5. Conventions d'écriture
- Speakers : `j`, `i`, `t`, `a` (Allan), `x` (Alexandre), `s` (Sofiane), `laplage`, `systeme` (narrateur italique).
- Narration `systeme` 3e personne, présent, focalisée Jessy.
- `scene bg arc2 ...` + `with fade`, `show <perso> beach <émotion> at char_*`, `hide ... with dissolve`, `hpunch`, `renpy.pause` pour silences, musique + `ambiant1` par scène.
- Menus à légende ; choix typés (sain / blague / contrôle / évitement).
- Répliques très courtes (2-10 mots). Guillemets « », tiret cadratin « — » pour coupures, « ... » points séparés.

## 6. Faiblesses
- Tics : « Trop vite. / Trop calmement. », « Pas beaucoup. Juste assez. » (x3), « Je sais. » répété.
- Narrateur surexplique l'émotion.
- Théo trop ouvertement manipulateur ; presque toutes les branches le rapprochent d'Ilona.
- Ouverture en couloir d'école en juillet ; sprites non-plage au début.
- Bascule brutale d'Ilona (« Va te faire foutre ») ; scène Laplage détachée.
