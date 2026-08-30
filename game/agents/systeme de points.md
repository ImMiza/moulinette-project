# Moulinette — Système de points

Guide d'équipe. À lire avant d'écrire ou de modifier un menu.

Document technique complet et table des 38 menus : `game/agents/recalibrage.md`.
Scénario de l'arc 6 : `game/agents/arc_6 scenario.md`.

---

## 1. La règle de base

> **On ne gagne pas Ilona. On apprend — ou non — à construire avec elle un endroit où elle veut rester.**

Le système de points existe pour rendre cette phrase mécaniquement vraie. Concrètement :

- Un joueur qui accumule de la **complicité** (blagues, cadeaux, tendresse) sans jamais laisser Ilona finir ses phrases **n'atteint pas** la bonne fin.
- Un joueur qui lui laisse de l'**espace** sans jamais rien risquer atteint l'*ending ami*, pas la romance.
- La romance demande les deux, dosés. C'est une fenêtre étroite, pas un maximum.

Chaque choix ne se demande pas « est-ce gentil ? » mais **« quelle posture ça révèle ? »**.

---

## 2. Les compteurs

### Les 5 compteurs qui décident de la route

| Compteur | Sens | Ordre de grandeur en fin de jeu |
|---|---|---|
| `autonomie_ilona` | On lui laisse décider et exister seule | 0 à 100 |
| `communication` | Jessy dit les choses avant qu'elles explosent | −34 à 79 |
| `confiance` | Jessy croit sa parole sans vérifier | −99 à 63 |
| `ilona_peut_finir_ses_phrases` | Compteur d'écoute réelle | 0 à ~8 |
| `interruptions_reparees` | Erreurs reconnues **et** réparées | 0 à ~4 |

### Les 5 compteurs de dette

| Compteur | Sens |
|---|---|
| `influence_theo` | Emprise de Théo sur la dynamique |
| `pression_stream` | Charge accumulée sur Ilona |
| `jalousie` | Peur transformée en surveillance |
| `interruptions_ilona` | Nombre de fois où on lui a coupé la parole |
| `confidences_laplage` | **Nombre de fois où elle a dû parler à quelqu'un d'autre** |

⚠️ `confidences_laplage` est une **dette**, pas un crédit. Si Ilona se confie à Laplage, c'est que personne autour d'elle ne l'écoutait. Les trois occurrences du jeu sont conditionnées par `ilona_peut_finir_ses_phrases < 2 / < 4 / < 6`.

### Le compteur à part

`lien_jessy_ilona` — la complicité. **Il n'entre pas dans la porte de l'arc 6.** Il ne sert qu'à départager *ami* et *romance* dans l'arc 7. Un choix qui ne donne que du `lien`, c'est du plaisir sans progrès. C'est légitime, mais ça ne fait pas avancer la relation.

### Les compteurs de récidive

`evitements` et `controles`. Incrémentés automatiquement par les tiers C et D. Ils punissent la **répétition**, pas l'erreur isolée : le malus ne commence qu'à partir de 3 évitements ou 3 contrôles.

### Les clamps

Ces compteurs ne descendent jamais sous zéro :

```
jalousie, pression_stream, influence_theo,
interruptions_ilona, ilona_peut_finir_ses_phrases
```

Toujours écrire `$ jalousie = max(0, jalousie - 2)` et jamais `$ jalousie -= 2`.

---

## 3. Les 5 tiers

Chaque option de menu appartient à **un seul** tier. C'est la seule décision d'auteur à prendre ; les points en découlent mécaniquement.

| Tier | Posture | Exemple type |
|---|---|---|
| **S** | Rendre l'espace | Demander au lieu de supposer, laisser Ilona répondre, accepter un non |
| **A** | Se nommer | Dire sa peur, reconnaître une erreur, réparer |
| **B** | Complicité | Blague, cadeau, geste tendre, souvenir partagé |
| **C** | Évitement | Silence, esquive, mensonge, changement de sujet |
| **D** | Contrôle | Surveiller, exiger, accuser, décider à sa place |
| **N** | Neutre | Easter egg, choix purement esthétique |

### Grille de base (poids ×1)

```renpy
# S
$ autonomie_ilona += 2
$ communication += 1
$ confiance += 1
$ pression_stream = max(0, pression_stream - 1)

# A
$ communication += 2
$ confiance += 1
$ lien_jessy_ilona += 1
$ jalousie = max(0, jalousie - 1)

# B
$ lien_jessy_ilona += 2

# C
$ communication -= 2
$ confiance -= 1
$ pression_stream += 1
$ evitements += 1

# D
$ autonomie_ilona -= 2
$ confiance -= 2
$ jalousie += 3
$ influence_theo += 1
$ lien_jessy_ilona -= 1
$ controles += 1
```

---

## 4. Les 3 poids

On multiplie toute la grille par le poids du menu.

| Poids | Quand | Nombre de menus |
|---|---|---|
| **×1** routine | Le choix ne laisse aucune trace | 12 |
| **×2** structurant | Le choix pose un flag relu dans un arc ultérieur | 23 |
| **×3** pivot | Le choix redéfinit la relation | 3 |

Les 3 pivots du jeu :

- `arc_2_plage.rpy` — Ilona part aux mares avec Théo (`arc2_choix_activite_theo`)
- `arc_4_noel.rpy` — la limite posée par Ilona (`arc4_limite_ilona`)
- `arc_5_examens.rpy` — LA question à la gare (`arc5_question_reponse`)

Un pivot ×3 en tier D coûte : `autonomie −6, confiance −6, jalousie +9, influence_theo +3, lien −3`. C'est volontairement brutal.

---

## 5. Les 5 règles dures

**1. Un tier B ne donne jamais de `communication`.**
Jessy blague *pour ne pas parler*. C'est son gag structurant. Créditer la blague en communication récompensait l'inverse de la thèse du jeu — c'était le bug principal de l'ancien système.

**2. Un tier C ne donne jamais de bonus.**
Aucun. Le silence, l'esquive et le mensonge ne rapportent rien, jamais, même partiellement.

**3. Un tier D coûte sur au moins 3 axes**, et incrémente `interruptions_ilona` s'il coupe littéralement la parole.

**4. `lien_jessy_ilona` reste hors de la porte.** Ne jamais le glisser dans une condition de route.

**5. La récidive est punie par `evitements` / `controles`**, pas par une aggravation des deltas.

---

## 6. Recette : écrire un nouveau choix

1. **Nommer la posture.** Pas « est-ce sympa », mais : est-ce que Jessy rend de l'espace (S), se nomme (A), fait plaisir (B), évite (C), ou contrôle (D) ?
2. **Trouver le poids du menu.** Le choix pose-t-il un flag relu plus tard ? Redéfinit-il la relation ?
3. **Copier la grille × le poids.** Ne rien inventer.
4. **Ajouter les extras autorisés** (section 7).
5. **Conserver** les assignations de flag, les `remember(...)` et les blocs conditionnels existants.

### Exemple réel — `arc_3_rentree.rpy`, menu de la rumeur (×2)

```renpy
    "Regarder Ilona d'abord et lui laisser la main.":
        $ arc3_reaction_rumeur = "demander_ilona"
        # tier S x2
        $ autonomie_ilona += 4
        $ communication += 2
        $ confiance += 2
        $ pression_stream = max(0, pression_stream - 2)
        $ ilona_peut_finir_ses_phrases += 1
        j "..."

    "Défendre Ilona immédiatement, sans lui demander.":
        $ arc3_reaction_rumeur = "defendre_immediat"
        # tier D x2 : defendre sans demander, c'est decider a sa place
        $ autonomie_ilona -= 4
        $ confiance -= 4
        $ jalousie += 6
        $ influence_theo += 2
        $ lien_jessy_ilona -= 2
        $ controles += 1
        j "..."
```

Le deuxième choix se *présente* comme protecteur. C'est exactement pour ça qu'il est en D.

---

## 7. Ce qu'on a le droit d'ajouter hors grille

| Extra | Qui peut le porter |
|---|---|
| `ilona_peut_finir_ses_phrases += 1` | **tier S uniquement** |
| `interruptions_ilona += 1` | **tier D uniquement**, et seulement s'il coupe la parole |
| `influence_theo = max(0, influence_theo - N)` | tier S qui tient tête à Théo |
| `jugement_laplage += 1` | scènes avec Laplage |
| `ilonanium_points += 1` | les 6 objets cosmiques, rien d'autre |
| `remember("...")` | quand la scène l'appelle |

**Les 6 objets cosmiques** (Ilonanium) : bonbon-météorite (arc 1), gelée marine (arc 2), étoile en sucre (arc 3), mochi cosmique (arc 4), gâteau-planète (arc 6), bloc-lune (arc 7 Jessy). Ne pas en ajouter d'autres : le seuil de la fin cachée est calé sur exactement 6.

**Les clés de `souvenirs`** — à ne poser que quand c'est mérité, jamais inconditionnellement :

```
jessy_nomme_sa_peur          +6   dans le score
jessy_repare                 +8
ilona_libre_sans_abandon     +5
maison_respectee             +3
theo_utilise_une_verite      −6
ilona_pose_une_limite        conditionnel, ne compte que si on l'a écoutée
```

---

## 8. Les seuils de gating

Quand on écrit un `if` qui compare un compteur à une constante, il faut le caler sur les **magnitudes réelles**, pas au jugé.

Référence, à la fin de l'arc 3 :

| Parcours | comm | conf | auto | lien | jal |
|---|---|---|---|---|---|
| Idéal (que du S) | 38 | 28 | 36 | 12 | 0 |
| Naïf (1ʳᵉ option) | 29 | 18 | 14 | 25 | 0 |
| Romantique | 26 | 13 | 0 | 45 | 0 |
| Hostile | −16 | −42 | −34 | −11 | 51 |

Ordres de grandeur utiles : un seuil « élevé » sur `communication` en fin d'arc 4, c'est **25**, pas 5. Sur `jalousie`, un seuil « visible », c'est **9**.

`ilona_peut_finir_ses_phrases`, `interruptions_*`, `lien_ilona_theo` et `arc5_tension_accumulee` sont restés en pas de +1 : leurs seuils n'ont pas été rescalés.

---

## 9. La porte de l'arc 6

`arc_6_diplomes.rpy`, label `arc_6_calcul`.

```renpy
$ controle_repetitif = interruptions_ilona - interruptions_reparees

$ espace = (autonomie_ilona * 4 + ilona_peut_finir_ses_phrases * 6
            + interruptions_reparees * 6 + communication + confiance)

$ dette = (influence_theo * 3 + max(0, controle_repetitif) * 8
           + pression_stream * 2 + jalousie * 2 + confidences_laplage * 4)

$ posture = (6 * souvenirs["jessy_nomme_sa_peur"] + 8 * souvenirs["jessy_repare"]
             + 5 * souvenirs["ilona_libre_sans_abandon"] + 3 * souvenirs["maison_respectee"]
             - 6 * souvenirs["theo_utilise_une_verite"])

$ recidive = -6 * max(0, controles - 2) - 3 * max(0, evitements - 3)

$ arc6_score = espace + posture + recidive + arc6_mod - dette
```

Plus deux mécanismes narratifs :

- **Plancher de rachat** : `+20` si `interruptions_reparees >= 2 and souvenirs["jessy_repare"]`. Réparer vraiment rattrape.
- **Verrou dur** : `controle_repetitif >= 3` force la route Théo, quel que soit le score. Couper Ilona trois fois sans jamais réparer est le seul comportement absolument disqualifiant.

### Seuils (`script.rpy`)

```renpy
define SEUIL_JESSY = 180     # sous ce score -> arc_7_theo
define SEUIL_ROMANCE = 320   # au-dessus -> option romance debloquee en arc 7
define SEUIL_LIEN = 35       # complicite minimale requise pour la romance
```

### Ce que ça donne

| Parcours | Score | Lien | Route |
|---|---|---|---|
| Que du tier S | 568 | 19 | Jessy → **ami** |
| 1ʳᵉ option partout | 246 | 46 | Jessy → **ami** de justesse |
| Dernière option partout | −395 | 18 | **Théo** |
| Pire choix partout | −1042 | −31 | **Théo** |

Score maximum théorique : **572**. Parties aléatoires : médiane −104, seuil 180 franchi par ~0,3 %.

### La fenêtre romance

Le tier B ne donne que du `lien`. Chaque point de `lien` gagné coûte donc environ **7 points de score**.

```
lien 18 -> score 569     lien 55 -> score 380
lien 35 -> score 491     lien 64 -> score 325
lien 45 -> score 438     lien 65 -> score 316   <- sous le seuil
```

Avec `SEUIL_ROMANCE = 320` et `SEUIL_LIEN = 35`, la romance est atteignable pour `lien ∈ [35, 64]`. Ni triviale, ni impossible : il faut doser.

C'est la traduction mécanique de la thèse. Espace sans complicité → *ami*. Complicité sans espace → *Théo*. Les deux → *romance*.

---

## 10. Erreurs classiques (déjà commises, ne pas refaire)

| Erreur | Pourquoi c'est grave |
|---|---|
| Une blague qui donne `communication` | Récompense l'esquive, contredit le personnage |
| Le silence classé comme de l'écoute | Confond « ne pas gêner » et « laisser de la place » |
| Un mensonge qui donne `confiance` | Le joueur est payé pour tromper son ami |
| Un menu pivot pesant comme un menu de routine | Le score devient une somme de volume, pas de qualité |
| Un `remember(...)` inconditionnel | Rend le souvenir inutilisable comme condition |
| `$ jalousie -= 3` sans `max(0, ...)` | La jalousie devient un bonus caché |
| Un seuil laissé à l'ancienne échelle | Se déclenche pour tout le monde ou pour personne |

---

## 11. Tester une modification

Les scripts d'analyse vivent dans `%TEMP%\opencode\` (à recréer si besoin, ils ne sont pas versionnés).

| Script | Rôle |
|---|---|
| `calibrage.py` | Parse les `.rpy` et extrait tous les deltas par choix de menu |
| `recal.py` | Modèle de référence : grille, table des menus, politiques de jeu |
| `final.py` | Rejoue le code réel et applique la porte de l'arc 6 |
| `pareto.py` | Trace la frontière score / lien |

Après toute modification d'un menu :

```powershell
python "$env:TEMP\opencode\calibrage.py" "C:\projects\allan\renpy\moulinette"
```

Vérifier que les quatre parcours de référence gardent leur route :
idéal → *ami*, naïf → *ami de justesse*, hostile → *Théo*, pire → *Théo*.

Label de debug disponible en jeu : `arc_6_debug_score` (`arc_6_diplomes.rpy`).

---

## 12. Ordre des choix dans un menu

**Les options d'un menu ne sont plus triees du meilleur au pire.**

Avant, les menus etaient rediges dans l'ordre naturel de l'auteur : la bonne
reponse d'abord, la pire en dernier. Mesure faite sur le code : 67 % des options
en position 1 etaient de tier S ou A. Consequence, une strategie « toujours la
premiere reponse » suffisait a terminer le jeu du bon cote de la porte
(score +276, route Jessy). Ce n'est plus le cas.

Les 39 menus ont ete permutes de facon a ce que chaque position affiche a peu
pres la distribution globale des tiers :

| position | S | A | B | C | D | N |
|---|---|---|---|---|---|---|
| 1 | 8 | 8 | 7 | 8 | 6 | 2 |
| 2 | 8 | 8 | 8 | 7 | 6 | 2 |
| 3 | 7 | 8 | 7 | 7 | 6 | 0 |
| 4 | 6 | 6 | 6 | 6 | 5 | 0 |
| 5 | 2 | 1 | 1 | 1 | 1 | 0 |

Resultat : aucune position ne gagne. Les scores des cinq strategies
positionnelles sont desormais -131, -140, -85, -78 et -61, tous du cote Theo.

### Ce que ca implique quand vous ecrivez

1. **Ne remettez pas la bonne reponse en premier.** C'est le reflexe naturel, et
   c'est exactement ce qui recree l'exploit.
2. **Ne rangez pas non plus systematiquement le pire en dernier.** Meme probleme,
   symetrique.
3. En ajoutant un menu, placez les tiers au hasard, ou regardez la table
   ci-dessus et comblez la colonne la moins fournie.
4. Si vous reordonnez un menu existant pour des raisons de lecture, verifiez
   ensuite la distribution avec `pos.py`.
5. Un choix conditionnel (`"..." if cond:`) peut changer de place, mais gardez a
   l'esprit qu'il disparait parfois : ne comptez pas sur lui pour equilibrer une
   colonne.

### Ce que le shuffle ne change pas

L'ordre d'ecriture n'a **aucun** effet sur les points. Un choix garde ses deltas,
son tier et son poids ou qu'il soit dans la liste. Le shuffle ne corrige donc pas
un desequilibre de barème, il supprime seulement un exploit d'interface.

---

## 13. Encodage

Tous les fichiers sont en **UTF-8**. Les commentaires sont écrits **sans accents** (convention historique du projet), les dialogues **avec**.

Ne jamais éditer un `.rpy` avec un outil qui réécrit en CP1252 : ça produit du mojibake (`très` → `trÃ¨s`) invisible dans certains éditeurs. En cas de doute, vérifier en Python par code points, pas à l'œil dans une console Windows — la console remplace par `?` des caractères parfaitement valides.
