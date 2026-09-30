# Arc 1 — Cartographie

Fichiers: `game/arcs/arc_1/arc_1_printemps.rpy`. Label unique `arc_1_printemps`, qui finit par `jump arc_2_plage`. Pas de `call`. Dépend du prologue via `maison_minecraft_transformation`.

## 1. Résumé de l'intrigue
« Arc I - Printemps : la vie hors écran. » Avril, rentrée.
1. **Couloir**: Jessy et Ilona se parlaient chaque soir sur Discord (vocal seulement, pas de photo). Ils se croisent devant le panneau des classes, elle reconnaît sa voix : même école. Rappel de la maison, sonnerie, rendez-vous à midi.
2. **Toit, midi**: boissons au melon, gêne du face-à-face. Ilona offre un bout d'omelette (menu 1).
3. Ellipse : une habitude « par petits morceaux ».
4. **Quai et train**: même train. Ilona prend Jessy en photo par surprise (menu 2). Jessy tente une déclaration (« je voulais te dire que— »), coupée par le train, puis renonce.
5. **Konbini, vendredi**: bonbon étoile (« sucre ou destin »). **Monsieur Laplage**, déjà vu à la rivière Minecraft, apparaît au rayon boissons puis disparaît côté lessives, sans sortie (menu 3).
6. **Couloir, lundi**: Allan et Alexandre abordent « la maison Minecraft bizarre ». Allan demande : « Donc... vous sortez ensemble ? » (gag Metal Gear, menu 4).
7. **Toit, soir**: SMS « toit ? ». En ligne, les blancs se cachent ; ici, « on les entend » (menu 5).
8. **Cantine**: Allan propose trois hypothèses sur Laplage (prof, employé, apparition). Alex a une capture de la maison. Théo est mentionné. Sofiane glisse une sentence. Fin : « plus seulement dans Minecraft ».

## 2. Personnages
**Jessy (`j`, joueur)**: maladroit, autodérision, pince-sans-rire, réfléchit trop, fuit les tensions. Tutoie, vouvoie Laplage. Familier sans vulgarité (« je sais pas »). Évolue de la gêne à un aveu tenté.
- « Super première impression. »
- « Utile émotionnellement. »
- « Je crois en moi. »

**Ilona (`i`)**: taquine, directe, goût de l'absurde, mais timide en vrai. Pose des limites avec douceur (« Tu peux juste dire non »). C'est elle qui initie.
- « Si tu n'aimes pas, tu peux souffrir en silence. »
- « C'est une omelette, Jessy. Pas mon héritage familial. »

**Allan (`a`)**: curieux, sans filtre, raisonne à voix haute, connaît Théo. « Vous réparez rien, en fait. »

**Alexandre (`x`)**: blagueur, fan de la maison. « Si. Chez moi, si. »

**Monsieur Laplage (`laplage`)**: calme impossible, sage absurde, pouce levé. « Aujourd'hui, oui. » / « Choisir un bonbon, c'est déjà choisir une petite catastrophe. »

**Sofiane (`s`)**: observateur, une seule réplique, « toujours là depuis le début ».

**Théo (`t`)**: seulement mentionné. « Il a toujours une réponse », « parle comme s'il avait déjà lu la fin ».

## 3. Faits établis (continuité)
- Avant l'arc : relation vocale seulement, née de la maison Minecraft.
- Jessy : première B, 2e étage. Même école et même train qu'Ilona.
- Lieux : couloir, toit (lieu intime du duo), train, konbini, cantine.
- Première photo de Jessy : gardée, supprimée ou doublée selon le choix.
- Déclaration interrompue, en suspens.
- Bonbon étoile : pour la « salle secrète », mangé, ou gardé « pour plus tard ».
- La maison est « pas finie », avec pièces inutiles et salle secrète. Gag : on ne répare rien.
- Laplage existe hors du jeu. Son nom vaut « aujourd'hui ». Mystère ouvert.
- « Vous sortez ensemble ? » reste ouvert. Ilona : « Je sais pas encore ».
- Le poulet géant s'appelle « Monsieur Plume » (branche `poulet`).

## 4. Variables / flags / points
Defaults dans `script.rpy` : 0 partout, `maison_minecraft_transformation = ""`. Aucun `persistent`.

**Tests**
- `maison_minecraft_transformation` : couloir → `"serre"`, `"piscine"`, `"toboggan"`, else ; cantine → `"poulet"`, `"serre"`, `"piscine"`.
- `lien_jessy_ilona >= 6` : ligne bonus (menu 4, « J'aimerais bien »).

**Profils d'effets**
- **L2** : `lien_jessy_ilona += 2`
- **A2** : `autonomie_ilona += 2`, `communication += 1`, `confiance += 1`, `pression_stream = max(0, pression_stream - 1)`
- **E2** : `communication -= 2`, `confiance -= 1`, `pression_stream += 1`, `evitements += 1`
- **A4** : `autonomie_ilona += 4`, `communication += 2`, `confiance += 2`, `ilona_peut_finir_ses_phrases += 1`, `pression_stream` -2 (min 0)
- **S4** : `communication += 4`, `confiance += 2`, `jalousie = max(0, jalousie - 2)`, `lien_jessy_ilona += 2`
- **E4** : `communication -= 4`, `confiance -= 2`, `pression_stream += 2`, `evitements += 1`

**Menus**
- **M1 (omelette)** : accepter L2 ; demander A2 ; refuser E2 ; blague Minecraft L2.
- **M2 (photo)** : supprimer E2 ; garder A2 ; 2e photo L2.
- **M3 (étoile)** : salle secrète L2 ; manger A2 + `ilonanium_points += 1` ; Laplage L2 + `ilonanium_points += 1`.
- **M4 (sortez ensemble)** : « J'aimerais bien » S4 ; blague `lien_jessy_ilona += 4` ; laisser Ilona A4 ; nier E4.
- **M5 (toit)** : demander ce qui aide A4 ; blague puis sincérité S4 ; se défendre E4 ; « prends ton temps » A4.

## 5. Conventions d'écriture
- Locuteurs : `j`, `i`, `a`, `x`, `s`, `laplage`, et `systeme` (narrateur italique, 3e personne, présent, phrases courtes).
- Dialogues en ping-pong de 1 à 8 mots, avec chute comique.
- Mise en scène : `scene bg arc1 …` + `fade` ; `show perso expr at char_left/right/midleft/midright/center` + `dissolve`. Jessy à gauche, Ilona à droite.
- Audio dense ; `renpy.pause(x, hard=True)` pour les silences.
- Menus : une légende, puis 3 ou 4 options à l'infinitif.
- Typographie : « », « ... », « — » pour une phrase coupée.

## 6. Faiblesses
- Effets figés en 6 profils : peu de nuance.
- Ping-pong monosyllabique (« Oui. » / « Un peu. ») : les voix de Jessy et d'Ilona se confondent.
- Beaucoup d'ellipses racontées par `systeme`.
- Les deux scènes du toit sont redondantes.
- Branches maison incohérentes : rien pour `toboggan` à la cantine, rien pour `poulet` au couloir.
- Allan et Alex peu différenciés. Sofiane et Théo plaqués.
