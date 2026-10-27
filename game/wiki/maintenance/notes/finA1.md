# Notes — Fin A1 (`arcs/endings/ending_friend.rpy`)

Clé : `finA1`. GOOD ENDING FRIEND, titre « Le dernier été » (`ending_friend.rpy:68, 1180-1181`). Labels : `ending_friend` (60), `_distance` (73), `_invitation` (171), `_trajet` (215), `_chateau` (345), `_promenade` (505), `_promesse` (623), `_photo` (737), `_annees` (838), `_retrouvailles` (1009), `_generique` (1179). Aucun menu ; `record_ending("friend")` (61).

## Personnages

- **Jessy** : tient sa promesse du bivouac, ne construit pas de surprise (81-82), accepte « Je préfère rester seule ce soir » (89-90). Commence une formation (178, 301) ; deux ans plus tard, dit oui pour un appartement (939) ; porte du placard réparée (1018-1023).
- **Ilona** : lance un petit stream de dessin (139-151) ; idée de lives de « bâtiments impossibles » (583) ; cherche un petit boulot (659) ; affiche d'atelier (934-936). Aveu : « J'avais peur de rentrer en ayant encore mal. » (546)
- **Alexandre** : trou Minecraft (100-133), pelle avec housse (187-189), château, déménagement avec balcon (650-654). Anniversaire en appel vidéo, feutres gris (876-903).
- **Allan** : buffet démesuré, serviettes oubliées (355-365) ; veut un rendez-vous annuel ; son frère a perdu son groupe d'amis (688-689) ; déménage « de l'autre côté du palier » (982-983).
- **Théo** : vit à Tokyo, rejoint à la correspondance (192) ; dîner raté (277-289) ; batterie externe oubliée chez Allan, rendue presque deux ans après (895, 970-980).
- **Sofiane** : transporte le matériel en Trueno (188, 327) ; service du soir (177).
- **Tchat** : pseudos `pixel_ramen`, `kiwi_no_kimi` (144, 148).
- Anonyme : « La vendeuse » (567-570).

Citations :
- Jessy à la brindille : « Elle a moins de responsabilités. » (479)
- Ilona : « Dire des bêtises avec toi. Sans préparer le début. » (539)
- Allan : « J'ai pas envie qu'on passe notre temps à s'expliquer pourquoi on peut pas venir. » (691)
- Narration finale : « Trois étés plus tard, ils ont encore trouvé une place pour chacun. » (1157)

Tenues : Jessy `Home/neutral_attentiveness` (20), Alexandre `Home/playful_grin` (21), Ilona `House` (stream, 137-153), tenues `beach` pour tous à la plage (22-27), Théo `tokyo` chez Allan (966), Jessy, Ilona et Alexandre en `minecraft`.

## Lieux

- Chambres : `images/scenes/backgrounds/friend/bg_friend_chambre_jessy.png`, `bg_friend_chambre_ilona.png`.
- Minecraft : `minecraft/bg_arc2_minecraft_house_summer_night.jpg`, `minecraft/bg_friend_minecraft_trou_ouvert.png`, `_trou_ferme.png`.
- Gare et train : `friend/bg_friend_gare_matin.png`, `transport/bg_shared_train_inside.jpg`, `transport/bg_arc5_train_station.jpg`, `friend/bg_friend_train_nuit.png`.
- Plage : `beach/bg_arc2_beach_main.jpg`, `bg_arc2_group_parasol.jpg`, `bg_arc2_kakigori_counter.jpg`, `bg_arc2_beach_sunset.jpg` ; promenade `friend/bg_friend_promenade_depart.png`, `bg_friend_promenade_arrivee.png`.
- Café de la gare : `city/bg_arc5_cafe.jpg`. Appel : `friend/bg_friend_appel_alexandre.png`, `bg_friend_discord_cinq.png`, `bg_friend_discord_six.png`. Appartement d'Allan : `friend/bg_friend_appartement_allan.png`, `_repas.png`.

## Objets et concepts

- Porte-brindille de Jessy (400-405, 477-483), restaurant pour crabes (432-451), réserve à biscuits (385-392).
- Citron « assez » d'Allan (515, 571, 598-617).
- Deux photos de groupe au retardateur comparées à la fin (763, 1139-1157).
- Batterie externe de Théo (895, 970-989).

## Mécaniques

Aucune variable écrite hors `endings_seen` via `record_ending("friend")`. Aucune variable lue. Entrée : `arc7_jessy_relation == "amitie"` dans `arc_7_jessy_fin_relation` (`arc_7_jessy.rpy:1183-1184`), seulement si la Fin A3 automatique (6 points + fruit goûté, 1177-1178) ne s'est pas déclenchée.

## Chronologie

- Soir du retour (78) ; « Quelques jours plus tard » (86) ; « Le vendredi » (100) ; « Les semaines passent » (160).
- « Vers la fin de l'été » (174) ; « DIMANCHE » (218), rendez-vous 9 h 10 (205).
- « L'ANNÉE SUIVANTE » (839) ; « PLUS TARD, CETTE MÊME ANNÉE » (872), anniversaire d'Alexandre fêté trois jours après (876) ; « LE DIMANCHE SUIVANT » (909).
- « L'ANNÉE D'APRÈS » (920) ; « AU PRINTEMPS SUIVANT » (962), « Près de deux ans » pour la batterie (979) ; « CET ÉTÉ-LÀ » (1010) = « Trois étés plus tard » (1157).

## Ressources

- CG : `images/scenes/cg/friend/cg_friend_chateau_sable.png`, `cg_friend_salut_brindille.png`, `cg_friend_raquettes.png`, `cg_friend_photo_premier_ete.png`, `cg_friend_photo_retrouvailles.png`.
- Musiques : `Subwoofer-Lullaby.ogg` (mcnight), `Haggstrom.ogg` (mc), `ilona_stream.ogg` (stream, défini dans `arc_7_theo.rpy:21`), `morning-piano.ogg`, `plage-day.ogg`, `plage-sunset.ogg`, `cafe.ogg`, `spring-hope.ogg`.
- Ambiances : `crowd-noise.mp3`, `tram-inside.mp3`, `ocean-waves.mp3`, `rain-inside.mp3`. Sons : `discord-call-sound.mp3`, `train-stop.mp3`, `sand-noise.mp3`, `photo-taken.mp3`, `minecraft-door.mp3`.

## Incertitudes et contradictions

- Les photos de groupe sont, selon `agents/cartographies/ending_friend.md`, des compositions fixes de sprites ; illustrations dédiées « à prévoir » (doc).
- `ending_friend.md` situe les adieux « au coucher du soleil » sur la promenade ; le script affiche `bg_friend_promenade_depart.png` après le sunset (790), cohérent.
- Sofiane apparaît encore avec la Trueno à la plage de fin d'été (327) ; la doc précise que sa possession n'est pas supposée trois ans plus tard : au dernier été, il arrive « avec les derniers sacs » sans mention de voiture (1043), cohérent.
- Le script ne nomme aucun lieu ni métier précis (choix revendiqué par la doc).
