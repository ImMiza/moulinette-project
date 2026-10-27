# Notes — Route B (`routeB`)

Source : `arcs/arc_7/arc_7_theo.rpy` (1501 lignes, label unique `arc_7_theo`). Titre affiché : `centered "ARC 7 : LE MONDE APRÈS LE DÉPART"` (l.78).

## Personnages

**Ilona** (`i`)
- Arrive à Tokyo le 6 avril (l.105). Lance la chaîne IlonaGaming au studio, à deux rues de l'appartement (l.135, 312).
- Accepte de sortir avec Théo dix jours après l'arrivée (l.519-537) ; premier baiser au restaurant (l.565-571).
- Persona de stream : veste bleue et longue perruque blanche (l.1120, 1252) ; hors stream, pull / col roulé gris (l.1120, 1252).
- Cheveux courts hors stream « à partir du 6 décembre » (commentaire l.47 ; sprites `ilona short` utilisés dès l.986).
- Tics : « Ah. » quand elle n'a plus l'énergie de dire que c'est trop (l.815, 1010-1011) ; tire sur sa manche avant de demander (l.1302, 1320). N'aime pas le melon (l.990-993). Tousse si elle boit trop froid après un stream (l.1168).
- Tenues/sprites :
  - `ilona tokyo` (embarrassed, neutral, smile, fatigue, sad) → `images/personnages/Ilona/Tokyo/*.png` (l.41-45). `sad` déclaré mais non utilisé dans le fichier.
  - `ilona short` (neutral, sad, sad_alt, crying) → `images/personnages/Ilona/Short_hair/*.png` (l.48-51 ; fichier `Crying.png` avec majuscule).
  - `ilona streaming` (victory, celebration, joy, smile, fatigue) → `images/personnages/Ilona/Streaming/*.png` (l.54-58).

**Théo** (`t`)
- Gère studio, régie, sponsors, planning ; précis et chiffré (832, 2 417, « vingt-deux virgule huit », « vingt-sept minutes », « deux minutes trente ») (l.126, 297, 351, 654, 830).
- Promesse au restaurant : « Je dois entendre ton non. Même si on sort ensemble. » (l.560), rappelée au choix final (l.1419, 1466).
- Sprites `theo tokyo` (disappointed, annoyed, defensive, innocent, hesitant, smirk, neutral, jealousy, reassuring) → `images/personnages/Theo/Tokyo/*.png` (l.60-69). `hesitant` réutilise `feigned_innocence.png` (commentaire l.64). `annoyed`, `innocent`, `jealousy` déclarés mais non utilisés.

**Monsieur Laplage** (`laplage`) : apparaît au parc de nuit (l.700-736), sprites `laplage neutral` / `thumb_up`, son `audio.laplage` (`audio/fx/re-zero-return.mp3`).

**Tchat** (`tchat`, défini l.18 : `Character("Tchat", color="#7fd6ff")`) : personnage local, pseudos sakura_mod, pixel_ramen, misterclip, kiwi_no_kimi, darkflame92, xXShadow_JPxX, moon_walker21.

Citations :
- « L'équipe les a fait venir. Toi, tu les as fait rester. » — Théo après le premier stream (l.363).
- « Le bonheur peut parler très fort. Vérifiez seulement qu'il ne répond pas à votre place. » — Laplage au parc (l.728).
- « Avec Théo, être comprise et être conduite prennent souvent la même voix. » — narrateur, 6 décembre (l.1040).
- « Quand tu dis « on », tu parles de qui ? » — Ilona après le million (l.1215).
- « C'est toujours après. » — Ilona, option sponsors (l.1458).

## Lieux

- Gare de Tokyo — `bg arc7 tokyo arrival` → `images/scenes/backgrounds/tokyo/bg_arc7_tokyo_arrival_station.jpg`.
- Appartement (2 chambres, cuisine ouverte, salon ; loué par le studio « pour huit mois au moins », l.155-162) — matin `bg_arc7_tokyo_house_morning.jpg`, nuit `bg_arc7_tokyo_house_night.png`, nuit éteinte `bg_arc7_tokyo_house_night_nolight.jpg`.
- Studio (deux rues de l'appartement, lumière violette) — `bg_arc7_tokyo_streaming_studio_night.jpg`.
- Konbini — `bg_arc7_tokyo_konbini_night.png`. Restaurant — `bg_arc7_tokyo_restaurant_night.jpg`. Parc — `bg_arc7_tokyo_park_night.jpg`.
- `bg arc7 intro stream` (`images/scenes/backgrounds/streaming/bg_arc7_intro_stream.jpg`) : déclaré l.30, **jamais utilisé dans ce fichier** ; utilisé seulement dans `bad_ending.rpy:219`.

## Objets et concepts

- Carnet de planning (retourné face contre table par Ilona, remis face visible par Théo, l.945-946, 996).
- Carnet de croquis offert à Noël (l.975), second carnet de planning (l.976-983).
- Stylo violet (variantes `arc6_stylo`, l.959-966). Écharpe de Théo près de la porte (si `arc4_ilona_avec_theo`, l.973).
- Porte-clés bloc retrouvé par Théo à la plage (l.1020-1026, 1494).
- « Une place au rien » (Laplage, l.722-724, rappel l.1029).
- Films : Kung Pow (l.592-606), Shaolin Soccer (l.913-919).

## Mécaniques

- Écrites : `derniere_route = "Route Théo"` (l.72, pas de `default` trouvé dans les scripts) ; `controle_repetitif` recalculé (l.73).
- Lues : `controle_repetitif`, `arc6_score`, `SEUIL_JESSY` (l.81-86) ; `arc6_offre_theo` (l.88-95, 1059-1062) ; `arc6_stylo` (l.959-966) ; `souvenirs["ilona_veut_streamer_serieusement"]` (l.968) ; `arc4_ilona_avec_theo` (l.971, 1478) ; `arc4_5_theo_proposition` (l.976-983, 1476) ; `arc2_choix_activite_theo` (l.1019-1027) ; `arc5_fin_minecraft` (l.1057) ; `arc5_theo_proposition` (l.1098-1105) ; `arc3_reaction_rumeur` (l.1153) ; `arc4_reaction_cadeau_theo` (l.1231).
- Menu unique l.1365 « La réponse de Théo. » : aucune variable écrite ; option 1 → `jump ending_neutre` (l.1436), option 2 → `jump bad_ending` (l.1501).
- Entrée : uniquement via `arc_6_bascule_theo` (`arc_6_diplomes.rpy:2059`), après `arc_6_decision_theo` ; verdict `arc6_calcule_verdict` (`arc_6_diplomes.rpy:77-82`) : `controle_repetitif >= 3` ou `arc6_score < SEUIL_JESSY` (180, `script.rpy:401`).

## Chronologie

- 26 mars : décision dans la cour (arc 6). 28 mars, 31 mars, 3 avril : onze jours (`arc_6_bascule_theo`). 6 avril : départ / arrivée à Tokyo.
- 7 avril (lendemain) : premier stream. J+10 : restaurant, couple. Lendemain : 10 000 abonnés.
- Juin (« deux mois après le lancement ») : 100 000. Semaine suivante : opération spéciale.
- Fin août : 250 000 (l.1068). Fin octobre : 600 000 (l.1079).
- 6 décembre : matin (cheveux courts), puis million « après huit mois », 23 h passées (l.1112-1125). Le choix final a lieu peu après minuit.
- Le récit place le 6 décembre (l.951) **avant** de revenir sur fin août et fin octobre (l.1068-1080) : retour en arrière non signalé explicitement.

## Ressources

Musiques (toutes vérifiées sur disque) :
- `audio.tokyo` → `audio/music/tokyo.ogg` ; `audio.stream` → `audio/music/ilona_stream.ogg` ; `audio.restojazz` → `audio/music/resto_jazz.ogg` ; `audio.sadness` → `audio/music/sadness.ogg` ; `audio.apart` → `audio/music/apart_tokyo.ogg` ; `audio.apartsad` → `audio/music/apart_tokyo_sad.ogg` (définis l.21-26).
- Globales : `audio.citynight` → `audio/music/night-walk.ogg`, `audio.sadPiano` → `audio/music/sad-piano.ogg` (`script.rpy:164,169`).
- **Typo** : `define auddio.depressed = "audio/music/depressed.ogg"` (l.27) au lieu de `audio.depressed`. La l.1439 joue `audio.depressed`. Le fichier `audio/music/depressed.ogg` existe ; la lecture ne fonctionnerait que si Ren'Py définit automatiquement ce nom à partir du dossier `audio/` (non vérifié en jeu). À corriger dans le script.
- Ambiance : `audio.foule` (`audio/ambience/crowd-noise.mp3`) à la gare. Son : `audio.laplage` au parc.
- Aucune CG dans la route.

## Incertitudes et contradictions

- Typo `auddio.depressed` (ci-dessus).
- Le 3e rappel d'ouverture (« La route a gardé une trace fausse », l.85-86) ne s'affiche que si `controle_repetitif < 3` et `arc6_score >= SEUIL_JESSY` sur la Route B : cas normalement impossible, sauf si `controle_repetitif` recalculé l.73 diffère de celui du verdict (calculé une seule fois au début de l'arc 6, `arc_6_diplomes.rpy:160`).
- 6 décembre : Théo annonce pour « demain » un tournage sponsor à 14 h (l.1007) ; le soir, il parle des « sponsors à quinze heures » (l.1337). Peut-être deux rendez-vous distincts (non tranché).
- Cartographie `agents/cartographies/arc_7.md` : « 6 avril → ~novembre » ; le script place le million au 6 décembre (l.951, confirmé par `bad_ending.rpy:37`).
- Bail : « huit mois au moins » (l.162) ; dans la Fin B1, le bail va encore « jusqu'à la fin du mois » mi-décembre (`ending_neutre.rpy:112`), soit plus de huit mois.
- Le tchat l'appelle « best vtubeuse » (l.1131) alors qu'elle stream en caméra avec perruque (l.1120) : simple vocabulaire du tchat ou incohérence (non tranché).
- Personnages ids : `tchat` (local). Pas d'autre personnage nommé.
- Commentaire d'en-tête `arc_7_theo.rpy:5` : « confidences_laplage >= 3 -> sortie Laplage possible si influence basse ». Aucun code de la route ne lit `confidences_laplage` : prévu (commentaire), non implémenté.
