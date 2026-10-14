# Good ending Family — Jessy et Ilona

Fichier : `game/arcs/endings/ending_family.rpy`.
Source narrative : `game/agents/Good ending.md`.

## Entrée et déroulement

Entrée : `arc_7_jessy_fin_relation` → `ending_family` uniquement si `arc7_jessy_relation == "amour"` **et** `arc7_jessy_tente == True`. Il faut donc choisir l'amour puis rejoindre Ilona dans sa tente. Le choix du hamac mène à `ending_friend`, comme l'amitié ou une ancienne sauvegarde sans choix complet. La fin secrète Ilonanium garde son aiguillage prioritaire. `record_ending("family")` est conservé à l'entrée.

1. **Restaurant en ville, quelques jours après la randonnée.** Ils souhaitent habiter ensemble dans les montagnes et découvrent qu'ils ont sélectionné la même annonce. Appel au propriétaire ; Sofiane accepte de les conduire.
2. **Visite le lendemain.** Monsieur Laplage possède le restaurant et la maison. Il entretenait les lieux après le départ à la retraite d'amis restaurateurs. Visite de la salle et de la maison, puis retour dans la salle pour les questions, le don et les signatures. Sortie dans la cour pour les adieux définitifs de Laplage, dont le mystère reste ouvert.
3. **Installation.** Ilona nomme le restaurant **Les Petits Sommets**. Vraie scène du premier matin dans la maison (`ending_family_premier_matin`) : Jessy rate la forme de ses pancakes, Ilona le rejoint, ils préparent le petit déjeuner ensemble et prennent le temps de le manger sur le canapé. Les deux tasses et les clés concrétisent leur premier foyer commun. Puis reprise du montage (`ending_family_preparatifs`) : démarches, apprentissage, ouverture modeste, premiers services. Le lundi reste leur jour de repos. Ilona garde son bureau, ses jeux et ses streams.
4. **Retrouvailles, un mois plus tard.** Soirée privée. Sofiane transporte le groupe en deux voyages. Théo, venu de Tokyo, a repris contact et présenté ses excuses ; Ilona l'a invité après en avoir parlé avec Jessy.
5. **Repas.** Le groupe entre dans la salle décorée avant le retour de Sofiane avec Micka. Micka entre avec le nouveau sprite `party flowers`, puis passe à `party neutral` quand il donne le bouquet à Ilona. Son ancien sprite `gifts` représente des chocolats et reste réservé aux autres arcs. Les cadeaux sont déballés près du comptoir. Alexandre offre un dessin encadré inspiré de la première maison Minecraft ; il est accroché avant le repas. Chacun raconte sa vie. Micka annonce qu'il s'est marié avec **Claire Martin**, leur ancienne prof d'anglais (nom conservé à la demande de l’auteur ; la réplique précise « notre ancienne prof d’anglais », sans « Madame Martin »). Toast d'Allan.
6. **Fête.** Ilona boit du thé ; Sofiane reste au coca. Karaoké avec fond jazz pour le montage, Baka Mitai uniquement au tour de Théo (sans boucle), puis battle Jessy/Kiryu et Théo/Majima sur le fond de soirée. Aucune piste eurobeat dans cette fin.
7. **Départ.** Au revoir, menace humoristique de Sofiane à propos de sa voiture, Alexandre inquiet. Deux trajets de retour. Jessy et Ilona ferment et rentrent ensemble.
8. **Annonce, quelques jours plus tard.** Jardin, désir d'enfant déjà évoqué au repas, annonce de la grossesse. Jessy se fige, un nouveau sprite étonné accompagne son incrédulité, puis il sourit. Ilona disparaît progressivement de l'image ; Jessy glisse au centre et dit « Je vais être papa ? ». Le jardin du soir et le sprite `Jessy/papa/neutral.png` apparaissent alors ensemble, en coupe franche, pour révéler d'un coup l'ellipse de plusieurs années.
9. **Coupe franche, plusieurs années plus tard.** Même jardin au crépuscule. Lucy offre des fleurs à son père. Ilona arrive, enceinte d'Oliver. Gag du bébé qui fait sa randonnée ; Lucy veut lui construire une maison. Retour à trois, main dans la main. Noir et silence, phrase finale du conte, générique.

## Continuité et partis pris

- L'histoire se déroule au Japon depuis le début. Le restaurant et la maison sont dans les montagnes japonaises ; le départ de Théo à Tokyo est un déplacement à l'intérieur du pays.
- La décision de vivre ensemble précède l'aide de Laplage. Son don reprend le brainstorming ; il n'explique pas la réussite amoureuse.
- La réconciliation avec Théo prolonge sa conversation avec Allan à Tokyo. Son invitation ne tombe pas sans préparation.
- Le café du festival prépare le projet, mais le couple doit encore apprendre à tenir un restaurant.
- L'accès à cette fin, et donc à l'annonce de grossesse, exige l'amour et le choix de partager la tente à la randonnée.
- Les références optionnelles des anciennes branches ne sont pas imposées : pas de miniature de Noël supposée offerte. Le café de Sofiane est évoqué en aparté par Jessy et Ilona seulement si `arc4_5_sofiane_maid` vaut `True`. Sinon son lieu de travail reste inconnu de la tablée. Les révélations contradictoires de l’arc 6 (photo d’Alexandre) et de l’arc 7 S2 (aveu sans l’arc IV.5) ont été corrigées. La scène du trajet de Sofiane seul avec ses collègues reste une information du joueur, pas des protagonistes.
- La Trueno effectue deux rotations pour transporter tous les invités.
- Le contenu des trois mots sur la veste reste celui du récit précédent, non explicité dans cette fin.

## Décors intégrés

Les huit décors initiaux et le nouveau plan du câlin sont intégrés depuis `images/scenes/ending/family/`, sans fond de secours. Les décors initiaux font 2752 × 1536 ; le plan du câlin fait 1672 × 941. Tous sont affichés en 1920 × 1080 avec `Transform(..., fit="cover")` pour conserver leurs proportions.

| Fichier intégré | Contenu visible |
| --- | --- |
| `bg_family_rendezvous.jpg` | Café lumineux, plantes, table pour deux, vélos dans la rue |
| `bg_family_restaurant_jour.jpg` | Façade crème et bois, tuiles grises, noren vert, cour avec tables, maison à droite |
| `cg_family_laplage_adieux.png` | Nouveau point de vue depuis la cour : Ilona et Laplage enlacés près du portillon, Jessy témoin en retrait |
| `bg_family_salle.jpg` | Fenêtres à gauche, long comptoir et tabourets à droite, cuisine ouverte, cahier et linge plié |
| `bg_family_maison.jpg` | Canapé, table basse, pièce en tatamis, escalier, cuisine et galerie sur le jardin |
| `cg_family_pancakes_01.png` | Même maison, Jessy à la poêle et Ilona qui l'enlace devant le premier pancake raté |
| `cg_family_pancakes_02.png` | Même angle de caméra, Ilona au fourneau et Jessy à ses côtés devant le pancake réussi |
| `bg_family_restaurant_soir.jpg` | Même façade, enseigne Les Petits Sommets, guirlandes et fenêtres éclairées |
| `bg_family_fete.jpg` | Tablée près des fenêtres, guirlandes, poste de musique au fond, maisons en blocs encadrées |
| `bg_family_jardin_jour.jpg` | Arbre et banc à gauche, cabanon au fond, maison à droite, parcelle de terre nue |
| `bg_family_jardin_soir.jpg` | Même cadrage, légumes et fraisiers, bottes roses, porte dessinée sur celle du cabanon, maison éclairée |

Les textes suivent ces décors : plus de volets verts ni de linge étendu ; visite de la maison racontée depuis le séjour ; pause sur le canapé après le service du midi ; danse dans le passage entre table et comptoir ; lumières maintenues pour les départs. Le changement jardin jour/soir conserve la coupe franche.

## Ressources encore provisoires

Les nouvelles tenues sont intégrées et ont été inspectées visuellement :

| Personnage / tenue | Usage et expressions |
| --- | --- |
| Ilona `summer` | Rendez-vous et visite : neutre pour les questions et les adieux, sourire pour la complicité, gêne lors de la cession. Sans chapeau. |
| Ilona `house` | Premier matin, préparatifs et annonce : neutre pour le réveil/l’écoute, sourire pour les échanges tendres, gêne pour les confidences. Aucun sprite de fatigue disponible dans cette tenue : ne pas revenir à la tenue de plage pour une émotion. |
| Ilona `party` | Accueil des invités, repas, karaoké et départ : sourire, écoute neutre et gêne pour le projet d’enfant. |
| Ilona `house pregnant` | Seulement dans l’épilogue, à sa sortie de la maison, enceinte d’Oliver. |
| Jessy `beach` | Tenue décontractée conservée au quotidien : neutre, gêne, sourire doux, joie et détermination. Aucun dossier `summer` ou `house` n’est présent pour lui. |
| Jessy `party` | Soirée : neutre pour l’écoute et le départ de Laplage raconté à table, sourire doux pour la tendresse, joie pour les plaisanteries et la danse. |
| Jessy `papa neutral` | Apparaît avec le nouveau décor en coupe franche juste après « Je vais être papa ? », puis reste pendant tout l’épilogue. Un seul sprite adulte est disponible. |
| Allan `party` | Costume blanc et chemise bordeaux pendant toute la fête : sourire malicieux pour l'accueil et les plaisanteries, neutre quand il raconte son travail. |
| Alexandre `party` | Costume noir et chemise violette : sourire pour les plaisanteries, gêne devant l'annonce du mariage et le réfrigérateur, inquiétude avant le départ en voiture. |
| Sofiane `party` | Costume blanc, chemise noire et cravate ; neutre discret depuis son arrivée jusqu'au dernier trajet en voiture. |
| Micka `party` | Costume noir du dossier `micka/party`. Variante `flowers` à son entrée, puis `neutral` pendant le repas, le karaoké et le départ. |
| Théo `party` | Chemise bordeaux, cravate et bretelles : neutre à son arrivée et avant le karaoké, rassurant dans les échanges, sourire complice pour la danse. |

Les sprites utilisent `speaker_sprite` et les tailles existantes ; celui de Jessy `party smile` (843 × 1264) est normalisé à 842 × 1264. Les sept participants utilisent désormais leur tenue `party` pendant toute la fête, y compris l'accueil et les départs. Les personnages au premier plan changent selon la conversation, avec trois positions au maximum ; un personnage hors cadre reste présent dans la pièce. Les chanteurs se succèdent réellement à l’image. Les départs vers la gare/la voiture retirent les personnages du cadre.

Lucy utilise `images/personnages/lucy/neutral.png` et `happy.png`, avec un canvas de 576 × 864 avant le zoom 0,50, pour conserver une taille d’enfant. Elle entre après son premier « Papa ! », reste au centre entre ses parents et disparaît avec eux à la fin. Sa pose joyeuse aux bras levés est réservée aux élans de joie ; le neutre revient pour les échanges calmes. Son callback utilise le tag `lucy`. La narration ne lui prête plus un gilet absent du sprite. Les mains, embrassades et déplacements fins sont racontés : les fichiers disponibles sont des poses fixes, pas des animations.

Deux pistes prévues, chargées seulement si le fichier existe :

- `audio/music/family_save_the_world.ogg` : **SAVE the World**, après la coupe vers les années suivantes. Secours : `audio.springHope`.
- `audio/music/family_hopes_dreams_save_last_goodbye.ogg` : **Hopes and Dreams + SAVE the World + Last Goodbye**, au générique. Secours : `audio.realLove`.

Le karaoké utilise le fichier existant `Baka_Mitai.ogg` seulement au tour de Théo, sans boucle ; le fond jazz reprend quand Allan relance la musique pour la danse. `audio.spirit_of_the_night` est retiré de cette fin. Les autres chansons sont évoquées sans paroles reproduites. Le générique comporte des cartons cliquables et se termine par `return`.

Le fond `bg_family_karaoke.png` montre Jessy à gauche, Allan au centre et Théo au micro à droite. Il a été corrigé avec imagegen le 14 octobre 2026 : Allan porte son costume blanc et sa chemise bordeaux `party`, Théo sa chemise bordeaux, sa cravate et ses bretelles `party`. Les poses, Jessy, la table et la salle restent identiques dans le plan. L'ancienne image est conservée hors du jeu dans `family_review/bg_family_karaoke_before_party.png`.

Consigne de retouche utilisée :

> Use case: precise-object-edit. Asset type: existing Ren'Py visual-novel karaoke CG. Image 1 is the EDIT TARGET and authoritative composition. Image 2 is Allan's exact PARTY outfit and identity reference. Image 3 is Théo's exact PARTY outfit and identity reference. Make a precise continuity correction to Image 1 ONLY: the man in the BACK CENTER with dark sunglasses (Allan) must wear Image 2's white suit jacket over a burgundy open-collar shirt, NO tie and NO patterned vest. Keep his sunglasses, face, hair, lean-on-chair pose, visible arms and smile. The man at RIGHT holding the microphone (Théo) must wear Image 3's burgundy/plum button-down shirt with black tie and black suspenders, sleeves rolled up, instead of the dark turtleneck. Keep his face, glasses, hair, seated posture, hand gripping microphone, and gaze exactly as in Image 1. The laughing bearded man at LEFT (Jessy) is ALREADY CORRECT; do not change any part of him, his white shirt or navy bow tie, or his hands. Preserve every other pixel of the restaurant interior as closely as possible: same wood beams and table, dinner dishes, glasses, warm string lights, moonlit window, exact camera angle and character positions. Keep lighting, palette, anatomy, expressions, depth of field, 16:9 wide 1672x941 framing and opaque background. Only these two wardrobe corrections; no extra characters, no text, no UI, no redesigned scenery, no altered tableware.

## Vérification

Relecture des décors, inspection des nouvelles tenues et des sprites invités, contrôle des noms d’images et de leurs fichiers, contrôle des positions affichées. Compilation/lint Ren’Py 8.5.3 sur une copie temporaire : aucun diagnostic dans `ending_family.rpy`. Les avertissements globaux concernent les manipulateurs `im.Scale` existants et les noms de fichiers accentués de Théo. Les deux valeurs de `arc4_5_sofiane_maid` sont vérifiées dans les passages modifiés. Une lecture visuelle complète en jeu reste à faire pour juger les fondus et le rythme de lecture.

## Variante de surprise de Jessy — 14 octobre 2026

Fichier ajouté : `images/personnages/Jessy/beach/surprised.png`. Génération avec l’outil imagegen intégré, à partir du sprite neutre de la tenue de plage et d’une première variante. Expression : yeux écarquillés, sourcils relevés et bouche entrouverte, avant la joie. Le PNG de 1024 × 1536 possède une transparence vérifiée sur fond uni et est affiché en 842 × 1264 via `speaker_sprite`. L’image originale est conservée. Une variante générée n’est pas une retouche pixel à pixel : le motif de la chemise varie légèrement.

Consigne finale utilisée :

> Precise sprite edit: use FIRST image as exact base. Change ONLY the eyes, eyebrows and mouth to surprised happy disbelief as in second image. Keep FIRST image's exact silhouette, head size, all pixels outside the face, body pose, framing, palm tree shirt pattern and original transparent canvas. IMPORTANT remove all backdrop completely: outside character must be fully transparent alpha 0, no brown halo, no gradient, no glow, no shadow, no background of any kind. Character interior opaque. Output single clean cutout visual novel character sprite. Original dimensions 842x1264 preferred, preserve original aspect ratio. Surprise expression: wide eyes, eyebrows raised, mouth slightly open, overwhelmed by unexpectedly wonderful news. Everything else in first reference remains unchanged.

## Bouquet de Micka — 14 octobre 2026

Fichier ajouté : `images/personnages/micka/party/flowers.png`. Créé avec imagegen intégré à partir de `micka/party/neutral.png`, sans modifier l’original. Le PNG de 1024 × 1536 a une transparence contrôlée sur fond uni ; Ren’Py l’affiche en 842 × 1264. Le bouquet est volumineux, mais laisse le visage visible, ce que précise désormais la narration. Les détails du costume peuvent varier légèrement entre les deux poses générées.

Consigne finale utilisée :

> Use case: precise-object-edit. Create a matching visual-novel sprite variant of the supplied Micka character. Keep exactly the same young man's face, dark hair, smile, sunglasses resting on top of his head, black formal suit, white shirt, dark bow tie, anatomy, line work, palette, camera angle and character scale. The only change is that he is holding a very large lush bouquet of fresh flowers in both hands in front of his torso, an amusingly oversized florist bouquet which partially hides his jacket and reaches up toward the lower half of his face without covering the face or eyes. Mixed pink, white and warm yellow flowers, modest green foliage, plain paper wrap; clearly flowers, not boxed gifts or chocolate. Transparent background with true alpha 0 outside the character and bouquet, clean cutout without halo, no scenery, no text. Single full-body portrait sprite, same framing and 842:1264 aspect ratio as the reference so it can swap seamlessly to the neutral costume sprite.

## Diaporama des pancakes — refait le 14 octobre 2026

Les deux anciens visuels ont été supprimés. Les nouveaux plans opaques de 1672 × 941 ont été créés avec imagegen intégré, sans prendre les anciens pancakes comme référence. Les seules références du premier plan sont le décor de la maison et les sprites de Jessy et d'Ilona. Le second plan part du premier pour conserver exactement l'angle de caméra, la cuisine, la lumière du matin, les tenues et le pancake raté sur l'assiette.

`cg_family_pancakes_01.png` accompagne le câlin d'Ilona derrière Jessy : il maintient la poêle à plat, avec le premier pancake plié sur l'assiette. Le décor ordinaire et les sprites reviennent pendant leurs gestes et leur conversation. `cg_family_pancakes_02.png` montre Ilona au même fourneau avec un nouveau pancake rond dans la poêle, Jessy penché à côté d'elle. Les personnages sont peints dans les deux images ; aucun sprite ne se superpose aux plans.

Consignes de génération : premier plan intime dans la cuisine de leur maison, matin ensoleillé, Jessy en chemise hawaïenne et Ilona en chemise à carreaux rouges ; second plan comme continuation du premier avec la même caméra et les mêmes accessoires, en changeant seulement leurs positions et le pancake dans la poêle. Aucun halo ni personnage supplémentaire.

## Câlin d’adieu Ilona / Laplage — refait le 14 octobre 2026

Le plan intégré est désormais `images/scenes/ending/family/cg_family_laplage_adieux.png` (1672 × 941). Il a été recréé avec imagegen à partir du décor de la cour et des sprites d'Ilona, de Monsieur Laplage et de Jessy, sans reprendre la composition de l'ancien câlin. La caméra est placée dans la cour, en direction du portillon ouvert et du chemin de départ. Ilona et Laplage occupent le premier plan ; Jessy reste en retrait près du restaurant. Le geste décrit par la narration — un bras autour d'Ilona et une main sur sa tête — est visible.

Le plan apparaît après « Me reposer » et reste pendant l'étreinte et les deux répliques. Un fondu de 1,2 seconde le relie au plan large de la cour, qui revient pour la poignée de main de Jessy. L'ancien `bg_family_calin.jpg` a été supprimé du projet.

Consigne de génération : nouvelle prise de vue depuis la cour, accolade paternelle et émouvante près du portillon, fatigue de Laplage, gratitude d'Ilona, Jessy témoin discret, silhouettes intégrées au décor et lumière naturelle sans halo.

## Continuité visuelle et rythme — 14 octobre 2026

Trois variantes opaques ont été produites avec l'outil imagegen intégré, à partir des décors existants, puis ajoutées sans remplacer les originaux :

| Nouveau fichier | Moment d'utilisation |
| --- | --- |
| `bg_family_fete_fin.png` | Après le toast, desserts terminés : assiettes presque vides, quelques verres et tasses. Reste en place pendant le karaoké et la danse. |
| `bg_family_fete_rangement.png` | Après le premier trajet de Sofiane : table presque débarrassée, derniers verres et part de gâteau à emballer près du comptoir. |
| `bg_family_restaurant_nuit.png` | Départs tardifs et baiser : même façade et cadrage que le crépuscule, ciel nocturne et fenêtres éclairées. |

Les originaux `bg_family_fete.jpg` et `bg_family_restaurant_soir.jpg` restent utilisés pour l'arrivée et le repas. Les retouches d'image ont demandé de préserver le cadrage, l'architecture, le mobilier, les guirlandes et l'enseigne « Les Petits Sommets » ; seules la table après repas et la lumière extérieure changent.

Au karaoké, `Baka_Mitai.ogg` joue maintenant un extrait de 22 à 58 secondes, sans boucle, avec une pause de 8 secondes sur le plan de Théo. Le jazz revient au début de la battle. La coupe vers Jessy adulte reste franche, avec 1,5 seconde pour lire le nouveau décor avant la narration. La réplique de Laplage est corrigée en « Je peux me reposer en paix, désormais. » Les deux pistes Undertale prévues restent absentes du projet ; leurs musiques de secours continuent à être utilisées.
