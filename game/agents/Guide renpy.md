# Guide de référence Ren’Py pour la création de jeu 

Ce document sert de cahier des techniques et de cahier des scénarios pour permettre à une IA de créer correctement un jeu Ren’Py. 

--- 

# Document 1 – Cahier technique Ren’Py (pour l’IA) 

- ## 1.1. Structure d’un projet Ren’Py 

# Un projet Ren’Py contient typiquement : 

- `game/` 

- `script.rpy` : scénario principal (défaut). 

- `gui.rpy` : paramètres du GUI (couleurs, tailles, images). 

- `options.rpy` : options globales (titre, version, langues, etc.). 

- `screens.rpy` : écrans (menu principal, menu de sauvegarde, etc.). 

- `audio/` : musiques et sons. 

- `images/` : backgrounds et personnages. 

- `tl/` : traductions. 

L’IA doit : 

- Garder le script principal dans `script.rpy`. 

- Mettre les assets dans `images/` et `audio/`. 

- Ne pas modifier `*.rpyc` (fichiers compilés). 

--- 

- ## 1.2. Syntaxe de base du script 

### 1.2.1. Labels et jumps 

- `label nom:` : définit un point d’entrée. 

- `label start:` est spécial : c’est le point d’entrée du jeu. 

- `jump nom:` : saute vers un label. 

- `return` : termine la scène / le jeu. 

Exemple : 

```renpy 

label start: 

# scénario 

return 

label chapter1: # scène jump chapter2 

label chapter2: # scène return ``` 

--- 

### 1.2.2. Personnages (Character) 

On définit les personnages avec `define` : 

```renpy define s = Character("Sylvie", color="#c8ffc8") define m = Character("Me", color="#c8c8ff") ``` 

Usage dans le script : 

```renpy s "Hi there! How was class?" m "Good..." ``` 

--- 

### 1.2.3. Dialogues et narration 

- Narration : 

```renpy "Ceci est une narration." ``` 

- Dialogue avec nom explicite (sans Character) : 

```renpy 

"Sylvie" "Ceci est un dialogue." 

``` 

- Dialogue avec Character : 

```renpy 

s "Ceci est un dialogue de Sylvie." ``` 

--- 

### 1.2.4. Images (backgrounds et sprites) 

- Définition implicite via fichiers dans `images/` : 

- `bg meadow.jpg` →image `bg meadow` 

- `sylvie green smile.png` →image `sylvie green smile` 

- Afficher une background : 

```renpy 

scene bg meadow with fade ``` 

- Afficher un sprite : 

```renpy 

show sylvie green smile with dissolve ``` 

- Cacher une image : 

```renpy hide sylvie ``` 

# - Positionnement : 

```renpy 

show sylvie green smile at right ``` 

# Positions prédéfinies : `left`, `right`, `center`, `truecenter`. 

--- 

# ### 1.2.5. Transitions 

- `with dissolve` : transition de dissolution. 

- `with fade` : fondu au noir puis fondu. 

- `with None` : transition “vide” (pas d’effet visuel). 

Exemple : 

```renpy scene bg meadow with fade 

show sylvie green smile with dissolve ``` 

--- 

### 1.2.6. Sons et musique 

- Musique : 

```renpy play music "audio/illurock.ogg" fadeout 1.0 fadein 1.0 ``` 

- Son : 

```renpy play sound "audio/effect.ogg" ``` 

- Stop musique : 

```renpy stop music fadeout 1.0 ``` 

--- 

### 1.2.7. Variables et conditions (Python intégré) 

Initialisation : 

```renpy default book = False ``` 

Modification : 

```renpy label book: $ book = True jump marry ``` 

Condition : 

```renpy if book: "On suit le chemin du livre." else: "On suit le chemin du jeu." ``` 

Les lignes avec `$` sont des instructions Python. 

--- 

### 1.2.8. Menus interactifs 

Exemple simple : 

```renpy menu: "Tu veux aller au parc ?" 

"Oui": jump park 

"Non": 

jump home 

``` 

--- 

### 1.2.9. Pauses 

```renpy pause pause 3.0 ``` 

--- 

# ## 1.3. Règles de nommage et conventions 

- Fichiers images : lowercase, sans espaces, extensions `.png`, `.jpg`, `.webp`, `.avif`. 

- Noms d’images : tag + attributs séparés par espaces (ex. `sylvie green smile`). 

- Noms de variables : lettres, chiffres, `_`, début par lettre. 

- Labels : mêmes règles, sans espaces. 

--- 

# Document 2 – Architecture du jeu (pour l’IA) 

# ## 2.1. Type de jeu attendu 

Type : visual novel interactif (avec choix, variables, plusieurs scènes). Support : PC, mobile, web (HTML5 via Ren’Py Web). 

--- 

# ## 2.2. Architecture scénaristique 

# L’IA doit structurer le jeu en : 

1. **Écran titre →menu principal** (géré par Ren’Py, via `screens.rpy`). 

2. **Scènes narratives** : 

- Chaque grande portion du récit = `label` (ex. `chapter1`, `chapter2`, …). 

- Chaque scène contient : 

- définitions (backgrounds, sprites, sons). 

- dialogues et narration. 

- menus interactifs si nécessaire. 

3. **Fin(s)** : 

- Chaque fin = `label` (ex. `ending_good`, `ending_bad`). 

- Chaque fin doit : 

- Afficher un texte d’ending. 

- Terminer avec `return`. 

Exemple : 

```renpy label start: 

"Bienvenue dans le jeu." jump chapter1 

label chapter1: scene bg city with fade 

s "Salut, tu es prêt ?" m "Oui, je suis prêt." 

menu: 

"On va au parc ?" 

"Oui": 

jump park_scene 

"Non": 

jump home_scene 

label park_scene: 

# ... jump chapter2 

label home_scene: # ... jump chapter2 

label chapter2: # ... jump ending_good 

label ending_good: "Fin heureuse." return 

``` 

--- 

# ## 2.3. Variables de jeu (design) 

# L’IA doit définir explicitement : 

- **Variables de scénario** : 

- `book` (bool) : choix de type “interactive book vs jeu”. 

- `score` (int) : score/réputation. 

- `relationship_x` (int) : niveau de relation avec un personnage. 

- **Variables d’état** : 

- `has_picked_item` (bool) : a‑ t‑ il pris un objet ? 

- `visited_place` (dict ou bools) : lieux visités. 

Initialisation (dans `script.rpy` avant `label start`) : 

```renpy 

default book = False default score = 0 default relationship_s = 0 default has_picked_item = False ``` 

--- 

## 2.4. Gestion des choix et debranchements 

Pour chaque choix important : 

1. Définir un `menu:`. 

2. Pour chaque option : 

- Modifier des variables. 

- `jump` vers un label différent. 

3. Éviter les boucles infinies : 

- Utiliser des `if` basés sur les variables pour orienter vers les bons labels. 

Exemple simplifié : 

```renpy label meet_sylvie: 

s "Tu viens avec moi ?" 

# menu: 

"Oui, je te suit." 

"Oui": 

$ relationship_s += 1 $ score += 5 jump follow_sylvie 

"Non, je reste ici." 

"Non": 

$ relationship_s -= 1 jump stay_here 

``` 

--- 

## 2.5. Scènes et transitions visuelles 

L’IA doit : 

- Définir pour chaque scène : 

- Background : `scene bg <nom>` 

- Personnages présents : `show <tag> <attributs> at <position>` 

- Transitions : `with dissolve` / `with fade`. 

- Éviter de surcharger la scène : 

- 1 à 3 personnages maximum par scène. 

- Pas plus de 2 backgrounds différents par chapitre. 

--- 

## 2.6. Musicaux et ambiances 

Pour chaque scène : 

- Choisir un fichier musique : `audio/xxx.ogg`. 

- Policy : 

- Musique principale : `play music "audio/main.ogg"`. 

- -changements de contexte : `play music "audio/tension.ogg" fadeout 1.0 fadein 1.0`. 

- Sons d’ambiance : 

- `play sound "audio/door_opens.ogg"`. 

--- 

# Document 3 – Modèle de script type (pour l’IA) 

Ci‑ dessous un modèle minimal complet que l’IA pourra adapter. 

```renpy 

# ========== DEFINITIONS ========== 

default book = False 

default score = 0 default relationship_s = 0 

define s = Character("Sylvie", color="#c8ffc8") define m = Character("Me", color="#c8c8ff") 

# ========== SCENARIO ========== 

label start: 

scene bg city with fade 

"Le soleil brille dans la ville. C’est une journée ordinaire." 

s "Salut, tu es prêt ?" 

m "Oui, je suis prêt." 

menu: 

"On va au parc ?" 

"Oui": 

$ relationship_s += 1 

$ score += 5 jump park_scene 

"Non": 

$ relationship_s -= 1 jump home_scene 

label park_scene: 

scene bg park with dissolve 

s "Le parc est magnifique aujourd’hui." 

m "Je suis content de l’avoir choisi." 

if relationship_s >= 2: "La relation avec Sylvie est bonne." else: 

"La relation avec Sylvie est faible." 

jump chapter2 

label home_scene: scene bg home with fade 

s "Tu préfères rester ici ?" m "Oui, je veux rester tranquille." 

$ score += 2 jump chapter2 

label chapter2: "Fin du premier chapitre." jump ending_good 

label ending_good: "Fin heureuse." if book: "Ton histoire ressemble à un livre interactif." else: "Tu as vécu une aventure vidéo." 

return ``` 

--- 

# Document 4 – Checklist pour l’IA avant génération finale 

L’IA doit, avant de générer le jeu : 

1. **Valider la structure** : 

- Labels cohérents (`start`, `chapter1`, `chapter2`, fins). 

- Aucun `jump` vers un label inexistant. 

2. **Valider les assets** : 

- backgrounds : `bg_<nom>.jpg/png` dans `images/`. 

- sprites : `<tag>_<attributs>.png` dans `images/`. 

- musiques : `<nom>.ogg` dans `audio/`. 

3. **Valider les variables** : 

- Toutes les variables utilisées sont initialisées avec `default`. 

- Les conditions `if` utilisent bien ces variables. 

4. **Valider les transitions** : 

- Chaque `scene` + `show` important est suivi d’un `with` (si effet visuel souhaité). 

5. **Valider la compatibilité web** : 

- Fichiers audio en `.ogg` / `.opus`. 

- Images en `.png` / `.jpg` / `.webp`. 

- Pas de dépendances externes non permises sur le web. 

