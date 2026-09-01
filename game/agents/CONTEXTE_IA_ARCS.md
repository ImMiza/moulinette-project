# Moulinette - Contexte IA des arcs

Dernière vérification statique : 2026-09-01.

Ce document sert de point d'entrée avant toute correction narrative, Ren'Py ou mécanique. Il décrit le code actif, ses dépendances et ses écarts connus. Lire ensuite uniquement le fichier d'arc concerné et les producteurs/consommateurs des variables modifiées.

## 1. Ordre de vérité

En cas de contradiction, utiliser cet ordre :

1. Code `.rpy` actif pour comportement actuel.
2. `game/agents/systeme de points.md` pour intention mécanique.
3. `game/agents/projet moulinette scenario.md` pour intention narrative et ton.
4. Flowcharts pour vue générale seulement.

Points importants :

- Ne jamais modifier les `.rpyc` : fichiers compilés.
- Ignorer `game/arcs/arc_4/arc_4_noel.rpy.bak` : ancienne sauvegarde, non chargée.
- Les fichiers `game/arcs/endings/*.rpy` sont seulement des fiches d'intention commentées. Les six labels exécutables sont dans `game/script.rpy`.
- `game/agents/flow scenario.md` décrit une ancienne randonnée en Arc VII. Code actuel : deux routes courtes, festival Jessy ou stream Théo.
- `game/agents/flowchart.md` oublie séparation Family/Jessy-Ilona : route Jessy possède quatre fins, pas trois.
- `game/agents/arcs_1-5_flowchart.md` simplifie ou inverse certains effets. Vérifier les deltas dans code.
- `systeme de points.md` reste référence de design, mais ses liens `recalibrage.md` et `arc_6 scenario.md` sont absents. Il annonce aussi trois confidences Laplage alors que code peut en compter quatre.
- Préserver changements utilisateur déjà présents. Faire petite correction ciblée, sans réordonner ou reformater tout menu.

## 2. Carte rapide du projet

| Rôle | Source active |
|---|---|
| Personnages, sprites communs, audio commun, état global, seuils, fins | `game/script.rpy` |
| Prologue | `game/arcs/prologue/prologue_minecraft.rpy` |
| Arc I | `game/arcs/arc_1/arc_1_printemps.rpy` |
| Arc II | `game/arcs/arc_2/arc_2_plage.rpy` |
| Arc III | `game/arcs/arc_3/arc_3_rentree.rpy` |
| Arc IV | `game/arcs/arc_4/arc_4_noel.rpy` |
| Interlude sain/comique | `game/arcs/arc_4/arc_4_5_maid_cafe.rpy` |
| Interlude Ilona/Théo | `game/arcs/arc_4/arc_4_5_theo.rpy` |
| Arc V | `game/arcs/arc_5/arc_5_examens.rpy` |
| Arc VI et calcul de route | `game/arcs/arc_6/arc_6_diplomes.rpy` |
| Route VII Jessy | `game/arcs/arc_7/arc_7_jessy.rpy` |
| Route VII Théo | `game/arcs/arc_7/arc_7_theo.rpy` |

Graphe actif :

```text
start
  -> prologue_minecraft
  -> arc_1_printemps
  -> arc_2_plage
  -> arc_3_rentree
  -> arc_4_noel
       -> call arc_4_5_maid_cafe -> return  [stats saines]
       -> call arc_4_5_theo      -> return  [route Théo amorcée]
  -> arc_5_examens
       -> arc_5_scene_3
  -> arc_6_diplomes
  -> arc_6_calcul
       -> arc_7_jessy -> 4 fins possibles
       -> arc_7_theo  -> 2 fins possibles
  -> ending_* -> post_generique -> return
```

Les arcs sont surtout linéaires. Menus modifient état puis reconvergent. Les branches différées et calcul Arc VI portent conséquences réelles.

## 3. Thèse, ton et motifs

Thèse : on ne « gagne » pas Ilona. On construit, ou non, un espace où elle peut parler, décider et rester librement.

Règles narratives :

- Jalousie = peur possible, jamais preuve automatique d'amour.
- Distance peut être saine seulement si la personne revient et explique.
- Théo voit vrais problèmes mais transforme parfois attention en contrôle. Il n'est ni omniscient ni simple rival romantique.
- Monsieur Laplage pose image ou question ; il ne résout pas conflit.
- Ilona existe hors triangle : fatigue, stream, limites, projets et décisions doivent rester visibles.
- Humour offre respiration ou complicité, mais ne remplace pas communication.
- Réparation compte plus que perfection. Excuse ne garantit pas pardon immédiat.
- Maison Minecraft = mémoire relationnelle, jamais trophée. Portes, couloirs, pièces, ajouts et destructions reflètent état du lien.
- Objets/cadeaux peuvent être attention, preuve imposée ou dette selon présentation.

Tonalités : romance lente, comédie absurde, mélancolie cumulative, étrangeté sérieuse autour de Laplage.

## 4. Personnages

### Jessy (`j`)

Créatif, loyal, attentif aux détails. Transforme émotion en blague, cadeau ou construction pour éviter parole risquée. Arc : nommer peur, demander plutôt que supposer, écouter jusqu'au bout, réparer sans exiger réponse.

### Ilona (`i`)

Co-autrice du lien, pas récompense. Besoin de choisir rythme, projet et limites. Plus fatigue/pression monte, plus aide qui décide à sa place devient dangereuse. Son projet de stream devient explicite en arcs IV.5-Théo et VI.

### Théo (`t`)

Observateur, compétent, rassurant, souvent anticipateur. Comprend détails réels puis peut utiliser vérités comme levier. Danger : rendre son aide indispensable, filtrer options, confondre efficacité et consentement.

### Allan (`a`)

Organisateur et médiateur. Traduit longtemps Théo, puis comprend que neutralité protège dynamique. Commence à prendre position en arcs III-IV, confronte Théo en VI.

### Alexandre (`x`)

Humour frontal et soutien pragmatique. Désamorce sans prétendre résoudre. Reste près de Jessy dans fin No Contact.

### Sofiane (`s`)

Observateur cryptique, parfois protecteur. Gags maid café et AE86. Ses phrases orientent surtout Allan. Arc VII randonnée annoncé par anciennes docs n'est pas implémenté.

### Monsieur Laplage (`laplage`, d'abord `m_inconnu`)

Figure symbolique impossible, grave jusque dans absurdité. Confidences sont dette mécanique : signe qu'Ilona a dû parler ailleurs. `jugement_laplage` augmente mais n'influence actuellement aucune route.

## 5. État global et système de choix

État central dans `game/script.rpy` :

- Espace : `autonomie_ilona`, `communication`, `confiance`, `ilona_peut_finir_ses_phrases`, `interruptions_reparees`.
- Dette : `influence_theo`, `pression_stream`, `jalousie`, `interruptions_ilona`, `confidences_laplage`.
- Complicité : `lien_jessy_ilona`, hors calcul de route, utilisé pour romance.
- Récidive : `evitements`, `controles`.
- Secondaires : `lien_ilona_theo`, `jugement_laplage`, `ilonanium_points`.
- Mémoire Minecraft : `maison_minecraft_ajouts`, `maison_minecraft_destructions`.
- Souvenirs : `souvenirs` et helper `remember(key)`.

Souvenirs actifs :

| Clé | Sens / score Arc VI |
|---|---|
| `jessy_nomme_sa_peur` | +6 |
| `jessy_repare` | +8 |
| `ilona_libre_sans_abandon` | +5 |
| `maison_respectee` | +3 |
| `theo_utilise_une_verite` | -6 |
| `ilona_pose_une_limite` | condition narrative, pas score direct |
| `ilona_veut_streamer_serieusement` | projet d'Ilona, pas score direct |

### Tiers et grille de base

| Tier | Posture | Effet ×1 |
|---|---|---|
| S | Rendre espace | autonomie +2, communication +1, confiance +1, pression -1 |
| A | Se nommer/réparer | communication +2, confiance +1, lien +1, jalousie -1 |
| B | Complicité | lien +2 seulement |
| C | Évitement | communication -2, confiance -1, pression +1, `evitements +1` |
| D | Contrôle | autonomie -2, confiance -2, jalousie +3, influence +1, lien -1, `controles +1` |
| N | Neutre | cosmique/esthétique, pas score relationnel |

Poids : ×1 routine, ×2 structurant, ×3 pivot. Pivots actifs : activité plage Arc II, limite Noël Arc IV, question gare Arc V.

Règles dures :

- Tier B ne donne pas `communication`.
- Tier C ne donne aucun bonus.
- `interruptions_ilona` seulement si parole réellement coupée.
- Réduire `jalousie`, `pression_stream` et `influence_theo` avec `max(0, ...)`.
- Conserver flags, `remember(...)` et branches différées quand correction touche deltas.
- Ne pas trier options du meilleur au pire : ordre a été mélangé pour éviter stratégie positionnelle.
- Commentaires de code historiquement sans accents ; dialogues en UTF-8 avec accents.

### Calcul Arc VI

Source unique : label `arc_6_calcul`.

```python
controle_repetitif = interruptions_ilona - interruptions_reparees

espace = (autonomie_ilona * 4
          + ilona_peut_finir_ses_phrases * 6
          + interruptions_reparees * 6
          + communication + confiance)

dette = (influence_theo * 3
         + max(0, controle_repetitif) * 8
         + pression_stream * 2
         + jalousie * 2
         + confidences_laplage * 4)

posture = (+6 * souvenirs["jessy_nomme_sa_peur"]
           +8 * souvenirs["jessy_repare"]
           +5 * souvenirs["ilona_libre_sans_abandon"]
           +3 * souvenirs["maison_respectee"]
           -6 * souvenirs["theo_utilise_une_verite"])

recidive = -6 * max(0, controles - 2) -3 * max(0, evitements - 3)
arc6_score = espace + posture + recidive + arc6_mod - dette
```

Bonus rachat : +20 si au moins deux interruptions réparées et souvenir `jessy_repare`.

Porte finale :

- `controle_repetitif >= 3` force route Théo.
- Sinon `arc6_score >= 180` donne route Jessy.
- Sinon route Théo.
- Romance disponible en route Jessy si `arc6_score >= 320` et `lien_jessy_ilona >= 35`.

`lien_jessy_ilona` ne doit pas entrer dans calcul de route. Il distingue espace sans romance et espace avec complicité.

## 6. Chronologie et contrats par arc

### Prologue - Maison Minecraft

Rôle : rencontre Jessy/Ilona, accident, réparation/transformation, première voix Discord, Alexandre, première apparition Laplage.

Flux : maison extérieure -> effondrement -> réaction -> transformation (`serre`, `poulet`, `toboggan`, `piscine`) -> salle secrète -> vocal -> toit nocturne -> Arc I.

Sorties importantes :

- `maison_minecraft_transformation`, relu Arc I.
- `prologue_reaction`, `prologue_appel_discord`, `maison_minecraft_detail`, actuellement non relus.
- Peut poser `maison_respectee`.
- `jugement_laplage += 1`.

Continuité : passage alias chat `pmj/pmi/pmx` vers personnages réels `j/i/x` marque appel vocal.

### Arc I - Printemps

Rôle : découverte même école, passage relation écran/réel, toit/train/konbini, photo, question publique sur couple, entrée Allan/Alexandre/Sofiane.

Scènes : couloir -> toit -> train/photo -> konbini/Laplage -> rencontre groupe -> conversation silences -> cantine.

Lectures : transformation Minecraft ; `lien_jessy_ilona >= 6` pour variante.

Sorties : surtout scores globaux et `ilona_peut_finir_ses_phrases`. Aucun tracker local d'arc.

Continuité : Théo est annoncé mais absent. Laplage rencontré dans réel après apparition Minecraft.

### Arc II - Plage

Rôle : entrée physique Théo, porte-clés perdu, photo de groupe, jalousie Jessy, activité aux mares, confrontation et retour Minecraft.

Pivot : `arc2_choix_activite_theo` = `confiance`, `dix_minutes`, `blague_jalouse`, `suivre` ou `disparaitre`.

Consommateurs : arcs III, IV, V et VI. Ne jamais renommer valeurs sans modifier tous lecteurs.

Autres sorties :

- `arc2_photo_reaction`, relu Arc V.
- `arc2_reaction_invitation` et `arc2_retour_minecraft`, actuellement non relus.
- `lien_ilona_theo += 2` sauf branche `suivre`.
- Souvenirs `ilona_libre_sans_abandon`, `jessy_nomme_sa_peur`, `jessy_repare`, `maison_respectee` selon branches.
- `arc2_scene_laplage` devient toujours vrai sur chemin normal.

Contrat de continuité : branche `dix_minutes` signifie, selon arcs III/IV/VI, que Jessy part respirer puis revient. Scène Arc II affiche actuellement Ilona/Théo partant et produit contradiction.

### Arc III - Rentrée et festival culturel

Rôle : conséquences plage, Blocky House Café, rumeur triangle, festival Ilona/Théo, duel Jessy/Théo, vérité d'Ilona, première fissure d'Allan, coda Minecraft.

Scènes : train -> préparation/rumeur -> festival -> enquête comique -> confidence Laplage -> confrontation -> rangement -> Minecraft.

Sorties importantes :

- `arc3_reaction_rumeur`, relu Arc VI.
- `arc3_fin_minecraft` = `panneau_finir_phrase`, `rangement_silencieux`, `porte_fermee`, `destruction` ou fallback `lanterne_cour`; relu arcs IV, IV.5-Théo, V et VI.
- `arc3_aide_stand`, `arc3_reaction_laplage` seulement locaux.
- `arc3_ilona_a_choisi_theme`, `arc3_rumeur_aggravee`, `arc3_theo_message_festival`, actuellement sans lecteur aval.
- Peut ajouter/détruire éléments maison. Destruction remet `souvenirs["maison_respectee"] = False`.

Laplage : scène de confidence est toujours jouée ; seul incrément `confidences_laplage` est conditionnel. Ne pas croire commentaire affirmant scène conditionnelle.

### Arc IV - Noël

Rôle : cadeau Jessy, carnet précis de Théo, mémoire comme attention/dette, limite d'Ilona, évolution Allan, possible route Théo, coda Minecraft.

Scènes : train -> galerie/cadeau -> marché/carnet -> Théo/Laplage -> groupe -> rivière/mochi -> limite -> interlude optionnel -> Minecraft.

Sorties importantes :

- `arc4_cadeau_jessy` : sens du cadeau ; relu arcs IV.5-Théo, V et VI.
- `arc4_limite_ilona` : réponse pivot ; relu arcs V et VI.
- `arc4_fin_minecraft`, relu arcs V et VI.
- `arc4_ilona_avec_theo`, déclenche interlude Théo et est relu ensuite.
- `arc4_reaction_cadeau_theo` sans lecteur après Arc IV.

Appels conditionnels :

- Maid café si `lien >= 10`, `communication >= 25`, `confiance >= 15`.
- Théo si `arc4_ilona_avec_theo`; activation vient de forte influence, faible confiance et limite `demande_theo`.
- Routes presque exclusives car route Théo exige confiance basse.

Laplage : comme Arc III, confidence jouée même quand compteur n'augmente pas.

### Arc IV.5 - Maid café

Rôle : récompense de complicité et respiration. Jessy/Ilona découvrent Sofiane maid. Ne résout pas triangle.

Sorties : `arc4_5_sofiane_maid = True`, relu Arc VI ; `arc4_5_maid_cafe_visite`, sans lecteur aval. Donne lien et baisse pression.

### Arc IV.5 - Ilona/Théo

Rôle : montrer aide devenant potentiellement dépendance. Aucun menu joueur ; réaction d'Ilona calculée par stats.

Branches `arc4_5_ilona_reaction` :

- `accepte` si influence très haute/autonomie basse, ou fallback moyen.
- `directe` si communication/écoute suffisante.
- `prudente` si autonomie élevée.

`arc4_5_theo_proposition` devient `gestion`, `question` ou `temps`. Les deux trackers sont relus arcs V/VI. Branche `accepte` peut poser `ilona_veut_streamer_serieusement` et `theo_utilise_une_verite`.

Dépendance technique : fonds maid café et `audio.wow` sont définis dans fichier Maid café, mais utilisés ici. Ren'Py charge définitions globalement, donc ordre d'exécution n'est pas problème.

### Arc V - Examens, Saint-Valentin et White Day

Rôle : fatigue d'Ilona, examens, cinéma conditionnel, offre de gestion Théo, cadeaux, question centrale confiance/peur, White Day, bilan Allan, annonce AE86, coda Minecraft.

Scènes : bibliothèque -> cinéma ou annulation/café -> proposition Théo -> Saint-Valentin -> confidence Laplage -> gare -> White Day -> café Allan/Alexandre -> Sofiane -> Minecraft.

Porte cinéma : `(lien >= 20 or autonomie >= 30) and confiance >= 15 and communication >= 20`. Succès saute branche annulation vers `arc_5_scene_3`.

Sorties majeures :

- `arc5_theo_proposition`, relu plus tard dans Arc V et sa coda, mais pas par Arc VI.
- `arc5_question_reponse` = `responsable`, `theo`, `temps`, `honnete`; relu Arc VI.
- `arc5_white_day_reponse` structure coda locale ; `arc5_fin_minecraft` est relu Arc VI.
- `arc5_tension_accumulee`, relu Arc VI.
- `arc5_allan_voit_theo`, `arc5_allan_parti_cafe`, `arc5_theo_dans_maison` pilotent scènes/coda locales.
- `arc5_jessy_a_menti`, `arc5_cinema_ensemble`, `arc5_ilona_a_pleure`, actuellement peu ou pas exploités aval.

Question gare est pivot ×3 : peur responsable, accusation Théo, demande de temps ou honnêteté totale.

### Arc VI - Diplômes

Rôle : payer fils I-V, rendre année lisible sans jauge, donner projet stream à Ilona, faire prendre position à Allan, puis calculer route.

Chronologie : stylo violet -> cérémonie -> jusqu'à huit vignettes -> offre Tokyo de Théo -> Laplage -> toit -> Minecraft -> calcul.

Entrées : nombreux trackers arcs II-V, compteurs globaux, souvenirs et état maison.

Menus : stylo, offre Théo, conversation toit, gâteau-planète, dernière construction.

Sorties :

- `arc6_conversation` et `arc6_derniere_construction`, relus Arc VII Jessy.
- `arc6_offre_theo`, relu Arc VII Théo.
- `arc6_score`, décision route et romance.
- `arc6_mod`, modifié par stylo, offre et surtout toit.
- `arc6_gateau_planete` documente objet cosmique mais Arc VII regarde directement `ilonanium_points`.

Vignettes ajoutent encore des deltas : toute correction d'un vieux choix doit vérifier rappel Arc VI pour éviter double récompense ou contradiction.

### Arc VII - Route Jessy

Rôle actuel : bref résumé au festival d'été, collecte bloc-lune, menu de fin. Ancienne randonnée non implémentée.

Options :

- No Contact, toujours visible.
- Ilonanium si points après bloc-lune >= 6.
- Romance si score >= 320 et lien >= 35 ; Family si `jessy_repare`, `maison_respectee` et au moins une interruption réparée, sinon Jessy/Ilona.

Attention : entrée avec `ilonanium_points >= 5` ajoute un point chaque fois. Pas de flag d'idempotence.

### Arc VII - Route Théo

Rôle actuel : bref résumé stream centré sur absence d'espace, puis choix de fin.

Options :

- Laplage/neutre si `confidences_laplage >= 3` et `influence_theo <= 6`.
- Théo/Vtuber toujours visible.

Texte établit explicitement qu'Ilona n'a pas « choisi Théo » : elle va vers lieu où parler semble moins nécessaire.

## 7. Fins actives

Labels dans `game/script.rpy`, pas dans stubs `game/arcs/endings/`.

| Label | Clé `endings_seen` | Accès | Intention |
|---|---|---|---|
| `ending_family` | `family` | romance + réparations | couple futur/famille, actuellement très résumé |
| `ending_jessy_ilona` | `jessy_ilona` | romance sans toutes conditions Family | couple présent, maison imparfaite conservée |
| `ending_no_contact` | `no_contact` | toujours route Jessy | séparation/distance, mais libellé Arc VII reste contradictoire |
| `ending_monsieur_laplage` | `laplage` | route Théo, confidences hautes/influence basse | sortie autonome d'Ilona, non romantique |
| `ending_theo_vtuber` | `theo_vtuber` | toujours route Théo | aide de Théo devenue emprise |
| `ending_ilonanium` | `ilonanium` | six objets, route Jessy | gag cosmique caché |

Toutes sautent vers `post_generique`, actuellement toujours joué. `endings_seen` est enregistré mais jamais lu ; intention narrative disait post-générique débloqué après plusieurs fins.

Objets Ilonanium attendus : bonbon-météorite Arc I, gelée marine Arc II, étoile sucre Arc III, mochi Arc IV, gâteau-planète Arc VI, bloc-lune Arc VII. Arc I accorde actuellement aussi point quand bonbon est conservé en mentionnant Laplage, ce qui contredit « six objets mangés ».

## 8. Dépendances critiques à rechercher avant renommage

Valeurs les plus couplées :

- `arc2_choix_activite_theo` -> arcs III, IV, V, VI.
- `arc3_fin_minecraft` -> arcs IV, IV.5-Théo, V, VI.
- `arc4_cadeau_jessy`, `arc4_limite_ilona`, `arc4_ilona_avec_theo` -> arcs IV.5, V, VI.
- `arc4_5_ilona_reaction`, `arc4_5_theo_proposition` -> arcs V, VI.
- `arc5_question_reponse`, `arc5_fin_minecraft`, `arc5_tension_accumulee` -> Arc VI.
- `arc6_conversation`, `arc6_derniere_construction`, `arc6_offre_theo`, `arc6_score` -> Arc VII.
- Clés `souvenirs` -> Arc VI, route Jessy et Family.

Commande de recherche recommandée avant changement de chaîne/flag :

```powershell
rg -n "nom_variable|valeur_de_branche" game -g "*.rpy"
```

## 9. Écarts connus à ne pas propager

### Runtime/assets probables

- Chemins directs `"fx/..."` invalides dans prologue, Arc II et Arc VI. Assets sont normalement sous `audio/fx/...`; préférer alias `audio.*` existant.
- Arc V déclare `images/scenes/arc_5/bg_arc5_cinema.jpg`, fichier absent.
- Arc VI sonnerie japonaise `fx/japanese-school-bell-sound-488954.mp3` absente.
- Arc I utilise trois fois `volume 1 loop volume 0.4` dans même instruction.
- Arc IV répète `loop` dans instruction musique marché.
- Casse `kombini_open.mp3` diffère du fichier `Kombini_open.mp3`, risque hors Windows.

### Continuité/logique fortes

- Arc II `dix_minutes` montre mauvaise personne partir par rapport aux rappels futurs.
- Arc II annonce « deuxième » interruption de Théo sans première interruption claire.
- Arc II incrémente `interruptions_ilona` pour surveillance, pas parole coupée.
- Arc I demande suppression photo de façon claire, Ilona respecte limite, mais choix reçoit pénalités évitement.
- Arc II demande nouvelle photo raisonnablement, mais reçoit pénalités contrôle.
- Arc I omet rappel `toboggan` à cantine.
- Arc IV contient deux options visuellement identiques `miniature_aveu` avec deltas différents.
- Arc IV réponse « Il a dit le service » joue même si Sofiane n'a pas prononcé phrase conditionnelle.
- Arc IV `arc4_carte_sofiane_lue` devient vrai avant lecture réelle, rendant branche alternative inaccessible.
- Arcs III-IV jouent confidences Laplage même si commentaires disent scènes conditionnelles.
- Arc V meilleure coda `salle_repos` accepte `honnete`, pas réponse `responsable` pourtant valorisée ailleurs.
- Arc VII option « Rester ensemble, sans se mettre ensemble » saute vers fin de rupture `ending_no_contact`.
- Routes VII et fins sont résumés très courts par rapport à bible narrative ; traiter comme état actuel, pas inventer développement sans demande.

### État mort ou documentation dérivée

- Plusieurs trackers écrits sans lecteur. Ne pas les supprimer automatiquement : ils peuvent préparer contenu futur ou sauvegardes.
- `jugement_laplage`, `arc6_route`, `derniere_route` et `endings_seen` n'ont pas d'effet aval actuel.
- `ecoute_reelle` est calculée dans debug/calcul mais sans rôle direct final.
- Récapitulatifs chiffrés en fin d'arcs et flowcharts peuvent être obsolètes après recalibrage.

## 10. Méthode de correction

1. Identifier label, scène, intention et tier du choix.
2. Lire scène avant/après, pas seulement ligne fautive.
3. Rechercher toutes lectures du tracker, de sa valeur chaîne et souvenirs touchés.
4. Vérifier rappels différés dans Arc VI et route/fins Arc VII.
5. Préserver grille tier/poids sauf correction explicitement mécanique.
6. Vérifier assets avec casse exacte et chemins relatifs depuis `game/`.
7. Ne pas ajouter label d'ending dans stub sans déplacer label existant de `script.rpy`.
8. Après modification narrative, vérifier pronoms, personne qui part/revient, objet possédé/mangé, date et lieu.
9. Après modification de menu, vérifier clamps, `evitements`, `controles`, interruptions et ordre non prédictible des options.
10. Lancer validation la plus ciblée : recherche statique, lint Ren'Py, puis parcours branche concernée si possible.

Checklist de sortie :

- Aucun jump/call vers label absent.
- Aucun label dupliqué.
- Aucun asset référencé absent ou mauvaise casse.
- Toute variable initialisée par `default`.
- Valeurs de branche cohérentes chez tous consommateurs.
- Dialogue et deltas racontent même posture.
- Choix cosmique ne modifie pas relation sauf intention explicite.
- Modification ne rend pas route impossible ou triviale.
- Aucun `.rpyc`, `.bak` ou changement utilisateur annexe touché.

## 11. Validation disponible

- Label debug : `arc_6_debug_score` dans `arc_6_diplomes.rpy`. Il dépend toutefois de variables calculées précédemment et n'est pas totalement autonome.
- Scripts de calibrage mentionnés dans `systeme de points.md` vivaient dans `%TEMP%\opencode\` et ne sont pas versionnés.
- Pour correction simple : lancer lint Ren'Py du projet puis tester label/branche visée.
- Pour changement de deltas ou seuils : recalculer parcours de référence et distribution des routes, pas seulement vérifier syntaxe.

Ce fichier décrit état actuel, pas cible idéale. Si correction vise écart entre code et bible, demander quelle source doit gagner avant de modifier logique ou narration.
