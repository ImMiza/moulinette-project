# Prologue — Cartographie

Fichiers:
- `game/arcs/prologue/prologue_minecraft.rpy` — label unique `prologue_minecraft` (appelé par `jump prologue_minecraft`, `script.rpy:382`). Sortie: `jump arc_1_printemps`. Aucun `call`.
- Défs locales: `pmj`/`pmi`/`pmx` (pseudos chat), audio `mc`, `mcdoor`, `build`, `mcwood`, `mcwalk`, `mcwater`, `mcChicken`, `discord`, `mcvilager`. Utilise aussi `audio.stonefall`, `audio.mcnight`, `audio.laplage` (définis dans `script.rpy`).

## 1. Résumé de l'intrigue
- Fin d'après-midi, serveur Minecraft public. Jessy finit une base devenue énorme (« développement »).
- Pancarte d'entrée. Ilona (IlonaGaming) arrive: « j'ai une idée : je vais entrer ».
- Visite: escalier « en cours de réflexion », porte qui « attend son étage ».
- Étage: Ilona retire un bloc → mur, plafond et une poule tombent.
- **Menu 1** réaction de Jessy (guerre de poulets / réagir trop vite / blague / réparer ensemble).
- Ilona veut transformer le trou plutôt que réparer (« Un mur, c'est triste »; « architecte de conséquences »).
- **Menu 2** transformation: serre aérienne / poulet géant gardien / toboggan vers coffre vide / piscine dans le couloir.
- Salle secrète derrière les escaliers: porte inutile, coffre vide, fleurs, pancarte « salle moyennement importante ».
- Chat trop lent (« pas CE mur ») → Ilona propose le vocal. **Menu 3**.
- Premier appel Discord (`pmj/pmi` → `j/i`): Ilona pointe l'esquive technique de Jessy.
- Alexandre (lorddarktime) commente la transformation, pose sa pancarte, se déconnecte.
- Nuit, toit: refus d'enlever des pièces.
- Rivière: silhouette sans pseudo (`m_inconnu`, sprite `laplage`) délivre sa phrase, disparaît.
- Fin: « On finira cette maison un jour. » → arc 1.

## 2. Personnages
**Jessy** (jessyCube, protagoniste joué, pronom « il »)
- Pince-sans-rire, esquive par technique/absurde administratif. Timide à l'oral. Tutoie, pas de vulgarité.
- Risque: réaction contrôlante (« ne touche plus à rien ») qu'il corrige aussitôt.
- « ça veut dire que les fondations sont légales »
- « c'est temporaire » (réplique répétée à Alexandre)
- « On finira cette maison un jour. »

**Ilona** (IlonaGaming)
- Directe, ludique, créative; transforme l'erreur en idée. Perspicace, ne force pas. Tutoie, pas de vulgarité, formules absurdes (« intimider les tomates »).
- « je vais entrer »
- « Un mur, c'est triste. »
- « Éviter les questions avec des détails techniques. »

**Relation Jessy–Ilona**: inconnus → complicité le même soir; accident = point de départ; « construite à deux ».

**Alexandre** (lorddarktime, `pmx`): ami de Jessy, bref, verdict sec. « Techniquement inhabitable. Donc parfaite. »

**Inconnu / Monsieur Laplage** (`m_inconnu`, callback `laplage`): apparition mystérieuse, ton sentencieux, thème réparation/destruction.

**Théo**: absent du prologue.

## 3. Faits établis (continuité)
- Rencontre Jessy/Ilona: serveur Minecraft public, fin d'après-midi → nuit, même soirée que le premier appel vocal (Discord).
- Ilona casse mur + plafond + fait tomber une poule. Transformation selon choix (serre / poulet géant / toboggan / piscine).
- Maison: trop grande, « trois cuisines », « couloir sans sortie » (Ilona veut le garder), tour inutile.
- Salle secrète: porte inutile, coffre vide, fleurs, pancarte « salle moyennement importante ».
- Pancartes: « NE PAS ENTRER. SAUF SI TU AS UNE BONNE IDÉE. » (Jessy), « NE SURTOUT PAS RENDRE ÇA NORMAL. » (Alexandre).
- Running gags: poules / guerre de poulets, « en cours de réflexion », « je ne promets rien » (Ilona), « c'est temporaire ».
- Promesse: finir la maison « un jour ».
- Mystère: personnage sans pseudo à la rivière (Jessy soupçonne mod/admin/Alexandre): « Construire ensemble, c'est facile. Le plus difficile, c'est de ne pas casser ce que l'autre construit. » = thème central.
- Trait de Jessy nommé: éviter les questions par détails techniques.

## 4. Variables / flags / points
Defaults dans `script.rpy`.
- **Menu 1** (effondrement):
  - Guerre de poulets: `lien_jessy_ilona += 2`
  - Réagir trop vite: `communication -= 2`, `confiance -= 1`, `pression_stream += 1`, `evitements += 1`
  - Blague: `lien_jessy_ilona += 2`
  - Réparer ensemble: `communication += 2`, `confiance += 1`, `jalousie = max(0, jalousie - 1)`, `lien_jessy_ilona += 1`, `remember("maison_respectee")` (→ `souvenirs["maison_respectee"] = True`)
- **Menu 2** — `maison_minecraft_transformation`:
  - `"serre"`: `autonomie_ilona += 2`, `communication += 1`, `confiance += 1`, `pression_stream = max(0, pression_stream - 1)`
  - `"poulet"` / `"toboggan"` / `"piscine"`: `lien_jessy_ilona += 2`
- Tests: `if maison_minecraft_transformation == "serre"/"piscine"/"toboggan"/else` (décor retour); `== "poulet"/"serre"/"piscine"/else` (dialogue Alexandre).
- **Menu 3** (vocal):
  - Accepter / Demander une minute: `communication += 2`, `confiance += 1`, `jalousie = max(0, jalousie - 1)`, `lien_jessy_ilona += 1`
  - Blague: `lien_jessy_ilona += 2`
- Inconditionnel: `jugement_laplage += 1`.
- Non utilisés ici: `maison_minecraft_destructions`, `maison_minecraft_ajouts`, `controles`.

## 5. Conventions d'écriture
- Speakers: `systeme` (narrateur, italique, 3e personne, présent), `pmj`/`pmi`/`pmx` (chat en jeu), `j`/`i` (vocal/voix réelle), `m_inconnu`. Alexandre = `x` ailleurs, `laplage` pour Monsieur Laplage.
- Chat: minuscules, sans point final, phrases très courtes, souvent échanges en rafale. Quelques capitales/points quand phrase longue (`pmx`, certains `pmi`).
- Vocal: ponctuation normale, majuscules.
- Narration: pince-sans-rire, personnification d'objets, 1–2 phrases par ligne; chute émotionnelle douce en fin de branche.
- Mise en scène: `scene bg prologue ...` + `with dissolve`/`fade`/`Dissolve(x)`; `jessy minecraft` `char_left`, `ilona` `char_right`, `alex`/`laplage` `char_center`; `play sound` avec volume; `$ renpy.pause(x, hard=True)` pour silences; `with hpunch`.
- Menus: légende-question narrative puis 3–4 choix à l'infinitif.
- Typo: guillemets « », ellipses « ... », pas de tirets cadratins, pancartes en MAJUSCULES.

## 6. Faiblesses
- Personnifications répétitives (tout « a une opinion »).
- Jessy et Ilona partagent le même humour absurde; voix peu différenciées.
- « couloir sans sortie » / « trois cuisines » introduits dans branches optionnelles, repris hors branche.
- 4 variantes Alexandre calquées (« c'est temporaire »).
- Menu 3: choix 1 et 3 identiques; tension faible.
- Laplage abrupt, morale explicite.
