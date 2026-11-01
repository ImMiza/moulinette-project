# Notes — arc6 (`arcs/arc_6/arc_6_diplomes.rpy`)

Fichier lu en entier (2059 lignes). Titre affiché : `centered "ARC 6 : LE JOUR OÙ L'ÉCOLE S'ARRÊTE"` (l. 165). Le commentaire d'en-tête (l. 1) dit encore « ARC VI - REMISE DES DIPLÔMES : « APRÈS AUJOURD'HUI » ».

## Personnages

- **Jessy** : garde le stylo violet d'Ilona depuis le 12 janvier (l. 178-181) et arrive à 7 h 50 pour une cérémonie à 10 h (l. 192-193). Il a retiré sa veste d'uniforme, qu'Ilona lui a demandée (l. 684-685). Scène 4 : il se tient à l'écart pour laisser les cinq minutes (l. 1414-1415).
  - « Ceci est un objet de quête. Je le rends contre trois émeraudes. » (l. 322, option blague)
  - « Je crois que si je dis un truc, je vais essayer de le réparer. » (l. 1264, craquage d'Ilona)
- **Ilona** : mange un pain au lait, « elle mange toujours quand quelque chose va commencer » (l. 189). Elle raconte l'année (scène 3), dit qu'elle est fatiguée « depuis septembre » (l. 1246), écrit trois mots sous le col de la veste (l. 1330/1338/1346) et tranche elle-même (l. 1749-1750). Tenue `tokyo` à la gare (l. 2008).
  - « Je déteste le mot « souvenir », au fait. » (l. 741)
  - « Je te demande une seule chose. Et toi, qu'est-ce que tu veux ? » (l. 1578)
  - « T'as pas mal fait. T'as fait lentement. » (l. 1931, variante « elle part »)
- **Théo** : part à Tokyo le 6 avril, « dans onze jours » (l. 581-588, 1420-1421). Il propose un studio qui gère trois chaînes (l. 1434) et fixe une date limite au 3 avril (l. 1693-1694). Expressions : `defensive`, `annoyed`, `disappointed`, `jealousy`, `reassuring`, `tokyo reassuring`.
  - « J'appelle ça lui foutre la paix. » (l. 621)
  - « Je vais pas inventer. J'ai assez de vrai. » (l. 1518)
- **Allan** : connaît Théo depuis dix ans (l. 550) et a passé sa vie à le « traduire » (l. 554). Il reçoit l'enveloppe de décembre (l. 478-481) et part sans rien traduire (l. 651).
- **Sofiane** : « J'écoute toujours. Personne ne fait attention. » (l. 476). Il garde le secret de son travail (l. 500-519).
- **Alexandre** (`x`, sprite `alex`) et **Micka** (`mi`, trois enveloppes, une convocation, l. 382-388). Micka est un personnage tardif : ne pas le nommer hors spoiler.

## Lieux

- Salle de classe du matin : `images/scenes/backgrounds/school/bg_arc6_classroom_morning.jpg`.
- Gymnase de la cérémonie : `images/scenes/backgrounds/school/bg_arc6_gym_ceremony.jpg`.
- Salle 3-B décorée : `images/scenes/backgrounds/school/bg_arc6_classroom_festive.jpg`.
- Couloir vide du 2e étage : `bg_arc6_corridor_empty.jpg` est **absent**, le jeu affiche le secours `images/scenes/backgrounds/school/bg_shared_school_corridor.jpg`.
- Cour, 26 mars : `images/scenes/backgrounds/school/bg_arc6_courtyard_march.jpg`.
- Maison Minecraft, dernier soir : `bg_arc6_minecraft_last.jpg` est **absent**, le jeu affiche le secours `images/scenes/backgrounds/minecraft/bg_arc2_minecraft_house_summer_night.jpg`.
- Toit au crépuscule : `bg arc6 rooftop dusk` est défini (l. 140) mais jamais affiché. Le fichier est absent, le secours serait `bg_arc5_rooftop.jpg`.
- Flashbacks et gare : réutilisation des décors des arcs 2 à 5 (l. 144-150).

## Objets et concepts

- Stylo violet (`arc6_stylo`), veste d'uniforme avec trois mots sous le col (jamais révélés dans l'arc), carnet offert par Théo (rangé au fond du sac, l. 1774), écharpes, miniature de la maison, mot de passe du serveur.
- Gâteau « BONNE ROUTE » : planète ou ballon (l. 405-419).
- Enveloppe de Sofiane : « Les lumières ne disent pas où aller. Elles disent juste qu'il fait nuit. » (l. 481).
- Distributeur du 2e étage qui rend la monnaie en pièces de dix, bocal d'Ilona (l. 1180-1185).
- « Zéro yen » (l. 965).

## Mécaniques

- **Lues** : `etat_relation()` via `arc6_palier` (l. 159), puis toutes les variables du verdict (voir la page `mecaniques/verdict-arc-6.mdx`), `arc2_choix_activite_theo`, `arc3_reaction_rumeur`, `arc3_aide_stand`, `arc3_fin_minecraft`, `arc4_ilona_avec_theo`, `arc4_limite_ilona`, `arc4_cadeau_jessy`, `arc4_5_ilona_reaction`, `arc4_5_sofiane_maid`, `arc5_theo_proposition`, `arc5_fin_minecraft`, `arc5_cinema_ensemble`, `arc5_question_reponse`, `arc5_tension_accumulee`, `pression_stream`, `influence_theo` (≥ 8 → « Tu vas regretter », l. 1805), `souvenirs["jessy_repare"]`.
- **Écrites** : `arc6_penchant`/`arc6_penchant_debut`/`arc6_derive`, `arc6_score`, `arc6_route` (l. 160), `arc6_stylo` (l. 230-316), `arc6_gateau_planete` et `ilonanium_points += 1` (l. 434-435), `arc6_flashback`, `arc6_vignettes_count`, `arc6_vignettes_jouees`, `controle_repetitif` (store, l. 1201), `arc6_ilona_a_pleure` (l. 1270), `arc6_theo_attaques` et `arc6_attaque_1..3` (l. 1507-1510), `souvenir_flag_bonne`, `arc6_offre_theo`, `arc6_conversation` (l. 1600-1649), `arc6_derniere_construction` (l. 1858-1877).
- **Relues ensuite** : `arc6_score` et `controle_repetitif` (`arc_7_theo.rpy:81-86`), `arc6_offre_theo` (`arc_7_theo.rpy:88-95`, `:1059-1061` ; `arc_7_jessy.rpy:997-1014`), `arc6_conversation` (`arc_7_jessy.rpy:1008-1011`), `arc6_stylo` (`arc_7_theo.rpy:959-965`), `arc6_derniere_construction` (`arc_7_jessy.rpy:147-154`), `ilonanium_points` (`arc_7_jessy.rpy:1177`, `== 6`).
- **Jamais relues** : `arc6_gateau_planete`, `arc6_vignettes_jouees`, `arc6_ilona_a_pleure` (en dehors de la l. 1292), `arc6_penchant_debut`, `arc6_derive`.
- **Menus** : 5 au total. Stylo (4 options), gâteau (2), posture (4, sans effet), « Que répond Jessy ? » (5), dernière construction (4, variante « Ilona reste » seulement).
- **Vignettes** : plafond `< 8` jamais atteint en pratique (7 vignettes possibles avant `phrase_finie`).

## Chronologie

- Fin mars. Cérémonie le 26 mars à 10 h (l. 193, l. 1737). Théo part le 6 avril (onze jours), date limite le 3 avril.
- Variante « elle part » : le 28 mars, Ilona confirme et le studio réserve deux places. Le 31 mars, rangement. Le 3 avril passe. Le 6 avril, la gare (l. 1996-2005).
- Les cerisiers ne sont pas ouverts et doivent ouvrir « la semaine prochaine » (l. 736-739).

## Ressources

- Musiques : `audio/music/morning-piano.ogg` (s1), `audio/music/tense-piano.ogg` (s2, s4), `audio/music/melancolique-piano.ogg` (s3, s5), `audio/music/Subwoofer-Lullaby.ogg` (Minecraft, variante « elle reste »), `audio/music/spring-hope.ogg` (onze jours).
- Ambiance : `audio/ambience/crowd-noise.mp3` (gymnase).
- Sons : `audio/fx/bell.mp3`, `audio/fx/ApplauseClapping.mp3` (`audio.micka`), `audio/fx/aaughmp3.mp3` (`audio.eating`, gâteau), `audio/fx/piano-slam.mp3` (« Je vais partir avec Théo »), `audio/fx/train-stop.mp3`.
- Aucune CG affichée dans l'arc 6. `bg arc6 evil theo` (`images/scenes/cg/theo/bg_arc6_evil_theo.jpg`) et `audio.sirene` (`audio/fx/prowler_sound.mp3`) sont **définis** ici (l. 152-153) mais **utilisés** dans l'arc 5 (`arc_5_examens.rpy:1123-1124`, si `arc5_theo_proposition == "laisse"`).

## Incertitudes et contradictions

- `agents/systeme de points.md` §9 : la formule contient `+ arc6_mod`, **absent du code**. La documentation situe aussi le calcul dans le label `arc_6_calcul`, alors que le code calcule à la l. 160 et que `arc_6_calcul` ne fait qu'un `jump`.
- `script.rpy:292-293` et `:421` disent « label arc_6_calcul » et « calculée en fin d'arc 6 » : c'est inexact. `script.rpy:391` cite un label `arc_6_debug_score` qui n'existe pas.
- Maximum théorique : 572 (`script.rpy:397`) contre 568 (documentation).
- `remember("theo_utilise_une_verite")` est inconditionnel à `arc_3_rentree.rpy:619`. Le −6 de posture s'applique donc à toutes les parties (effet peut-être non voulu).
- `arc6_penchant == "theo"` dans `arc_6_decision_jessy` (l. 1805) semble mort (déduction : sur la Route A, l'indice est ≥ 144, donc le ton est au moins « indécis »).
- `cartographies/arc_6.md` place l'image « evil theo » et la sirène dans la bascule des onze jours. En réalité, elles sont jouées dans l'arc 5.
- `arc_7_theo.rpy:92-93` affirme que Théo a répondu « les deux » si `arc6_offre_theo == "question"`. Dans l'arc 6, il ne répond « Les deux » que si le ton est `"theo"` (l. 1465-1476). Avec un autre ton, il dit « Je veux que tu viennes ».
- Option « J'ai rien à mettre en face de Tokyo. » : la valeur `arc6_conversation = "continuer"` paraît incohérente (déjà relevé dans la cartographie).
- Les variantes « Ilona reste » et « Ilona part » de la scène 5 sont classées `arc6`, alors qu'un joueur n'en voit qu'une. Les passer en `routeA`/`routeB` est à décider.
