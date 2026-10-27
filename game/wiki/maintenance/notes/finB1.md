# Notes — Fin B1 (`finB1`)

Source : `arcs/endings/ending_neutre.rpy` (588 lignes, label `ending_neutre`, l.6). Aucun `centered` : pas de titre ni de catégorie affichés en jeu. Titre de travail en commentaire : « ENDING NEUTRE » (l.1).

## Personnages

**Ilona** : écrit et publie seule l'annonce de pause (l.38-59) ; refuse la campagne au téléphone et annonce la fin d'IlonaGaming (l.163-169) ; dernier direct de moins de trois minutes en veste bleue et perruque blanche (l.228-259) ; ne supprime pas la chaîne (l.271) ; décide de quitter Tokyo seule, destination non nommée, départ « vendredi matin » (l.292, 422-425). Emporte le carnet de croquis et le porte-clés bloc, laisse une veste trop chaude (l.440-447).
Sprites : `ilona short` (sad, sad_alt, neutral), `ilona streaming fatigue` pour le dernier direct.

**Théo** : éteint son téléphone, s'empêche de corriger (l.28, 49-56) ; tend le téléphone à Ilona au lieu de répondre (l.153-155) ; accepte un poste de coordination de production au studio, sans appartement (l.175-180) ; accompagne Ilona jusqu'au quai seulement (l.454-456, 524-567).
Sprites : `theo tokyo` (disappointed, hesitant, neutral).

Citations :
- « Reste là. Sans réparer. » — Ilona (l.35).
- « Ce sont tes mots. Ils n'ont pas besoin d'être les meilleurs. » — Théo (l.56).
- « Je ne veux plus être IlonaGaming. » — Ilona (l.206).
- « J'ai besoin de découvrir qui je suis quand tu n'es pas dans la pièce. » — Ilona (l.327).
- « Cette fois, personne ne remplit le blanc à sa place. » — narrateur, dernière ligne (l.586).

## Lieux

- Appartement de Tokyo : nuit `images/scenes/backgrounds/tokyo/bg_arc7_tokyo_house_night.png`, jour `images/scenes/backgrounds/tokyo/bg_arc7_tokyo_house_morning.jpg`.
- Gare : `images/scenes/backgrounds/tokyo/bg_arc7_tokyo_arrival_station.jpg` (même décor que l'arrivée, symétrie voulue l.476).

## Objets et concepts

- Carnet de planning fermé tout du long (l.80, 190). Porte-clés bloc et carnet de croquis emportés. Mug bleu. Badge du nouveau poste de Théo (l.495-508). Classement des onigiris (« Trahison confirmée », l.490-493).

## Mécaniques

- `record_ending("neutre")` (l.7) → `endings_seen`. Aucune lecture de `endings_seen` trouvée ailleurs.
- Aucun menu, aucune condition. Fin par `return` (l.588).

## Chronologie

- Nuit du 6 au 7 décembre : annonce de pause. Cinquième matin : courriers. Le lendemain de l'appel : dernier direct et annonce du départ. Deux jours de cartons. Départ un vendredi (« quelques jours plus tard », l.475).

## Ressources

- Musique : aucune commande au début ; `audio/music/sadness.ogg`, lancée dans la route (`arc_7_theo.rpy:1144`), continue jusqu'à `play music audio.apartsad` (l.291, `audio/music/apart_tokyo_sad.ogg`), arrêtée l.571.
- Ambiance `audio.foule` (gare, l.473) ; sons `audio.trainstop` (l.537), `audio.trainPassing` (l.566).
- Aucune CG.

## Incertitudes et contradictions

- Bail : « Ils vont au bout des huit mois prévus. On a jusqu'à la fin du mois. » (l.112) alors que huit mois depuis le 6 avril tombent le 6 décembre, déjà passé (voir aussi `arc_7_theo.rpy:162`).
- Destination d'Ilona jamais nommée (choix volontaire du texte, l.422, 475).
