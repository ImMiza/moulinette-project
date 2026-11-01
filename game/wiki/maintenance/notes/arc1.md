# Notes — Arc I (`arc1`)

Source : `game/arcs/arc_1/arc_1_printemps.rpy` (646 lignes, label unique `arc_1_printemps`, entrée depuis `prologue_minecraft.rpy:395`, sortie `jump arc_2_plage` l. 646).
Titre affiché : `centered "ARC 1 : PRINTEMPS — LA VIE HORS ÉCRAN"` (l. 19). En-tête de fichier : « Arc I - Printemps : la vie hors écran. »

## Personnages

**Jessy** (`j`)
- Cherche son nom sur le panneau : « Alors... première B, deuxième étage... » (l. 28) — sa classe, interprétation.
- Déclaration interrompue par le train : « Ilona, je voulais te dire que— » (l. 260) ; « Peut-être. Si je retrouve le courage. » (l. 268).
- Vouvoie Monsieur Laplage (« C'est votre nom ? », l. 319).
- Citations : « Super première impression. » (l. 43) ; « Je crois en moi. » (l. 249) ; « Utile émotionnellement. » (l. 64, branche piscine).
- Sprites : `jessy embarrassed/neutral/smile/listening/determined` (`script.rpy:96-100`, tenue de base).

**Ilona** (`i`)
- Reconnaît Jessy « à [sa] voix » (l. 40) ; ils ne s'étaient jamais vus (« Pas de caméra. Pas de photo. », l. 24).
- Initie : boissons melon (l. 102), photo (l. 204-207), konbini (l. 281), SMS « toit ? » (l. 494).
- Pose une limite douce : « Tu peux juste dire non. C'est pas grave. » (l. 156).
- « En ligne, c'est plus facile. » / « Là, on les entend. » (l. 509-516).
- Citations : « C'est une omelette, Jessy. Pas mon héritage familial. » (l. 118) ; « Ou destin. » (l. 291).
- Sprites : `ilona neutral/smile/embarrassed/frustrated/determined/fatigue` (`script.rpy:103-108`).

**Allan** (`a`) — première apparition (l. 392). Pose la question « Donc... vous sortez ensemble ? » (l. 418). À la cantine, trois hypothèses sur Laplage (l. 599). Connaît Théo : « Je demanderai à Théo. Il a toujours une réponse. » (l. 607). Sprites `allan neutral/surprise/smirk/excited/doubt`.

**Alexandre** (`x`) — a vu la maison : « Elle est incroyable. » / « Si. Chez moi, si. » (l. 401-405). A « une capture de la maison », « Pour la science. » (l. 602-604). Sprites `alex grin/teasing/awkward`.

**Monsieur Laplage** (`laplage`) — apparaît au konbini, rayon boissons (l. 304-325). Reconnu comme « Le type de la rivière » (l. 317). Se nomme : « Monsieur Laplage. » / « Aujourd'hui, oui. » (l. 318-320). « Je surveille les horizons. Et parfois les offres deux pour un. » (l. 322). « Choisir un bonbon, c'est déjà choisir une petite catastrophe. » (l. 324). Part vers les lessives, sans sortie (l. 330-331). Pouce levé (sprite `laplage thumb_up`, l. 323 ; repris « Le monsieur au pouce levé », l. 410). Allan l'a vu à son tour « devant les distributeurs » (l. 592).

**Sofiane** (`s`) — première apparition, une réplique depuis la table voisine : « Les premiers liens font beaucoup de bruit quand personne ne sait encore quoi dire. » (l. 631). « Je crois qu'il est toujours là depuis le début. » (Alexandre, l. 636). Sprite `sofiane observation`.

**Théo** — seulement mentionné : « Un ami. Il parle comme s'il avait déjà lu la fin. » (Allan, l. 609).

## Lieux

- École, couloir : `bg arc1 school corridor` → `images/scenes/backgrounds/school/bg_shared_school_corridor.jpg` (l. 3 ; scènes l. 20 et 383).
- Toit (lieu intime du duo) : `images/scenes/backgrounds/school/bg_arc1_rooftop_lunch.jpg` (l. 4 ; l. 96 et 498).
- Quai : `images/scenes/backgrounds/transport/bg_arc1_train_platform.jpg` (l. 5).
- Intérieur du train : `images/scenes/backgrounds/transport/bg_shared_train_inside.jpg` (l. 6).
- Konbini : `images/scenes/backgrounds/city/bg_arc1_konbini_snacks.jpg` (l. 7).
- Cantine : `images/scenes/backgrounds/school/bg_arc1_school_cafeteria.jpg` (l. 8).
Tous vérifiés sur disque.

## Objets et concepts

- **Bonbon étoile** (l. 289-375) : paquet avec une étoile ; « sucre » ou « destin ». Premier des six objets cosmiques (`agents/systeme de points.md:201`). Point `ilonanium_points +1` seulement si Ilona le mange (l. 352). Sinon : proposé pour la salle secrète (l. 344) ou gardé dans la poche d'Ilona (l. 375). Plus jamais mentionné ensuite (grep « bonbon » dans `game/arcs`).
- **Photo du train** (l. 203-251) : première photo de Jessy ; supprimée, gardée ou doublée.
- **Maison Minecraft** : « Elle est pas finie. » (l. 402). Poulet géant nommé **Monsieur Plume** (l. 618, branche `poulet`). Piscine : le couloir « a des vagues maintenant » + « toboggan aquatique » (l. 625-626). Serre : « intimide toujours les tomates » (l. 621).
- **Gag Metal Gear** : son `snake-alert.mp3` + musique `Metal-gear.ogg` au moment de la question d'Allan (l. 414-420).

## Mécaniques

Menus (5) :
- l. 120 omelette : biscuits `lien +2` ; demander `autonomie_ilona +2, communication +1, confiance +1, pression_stream -1 (min 0)` ; refuser `communication -2, confiance -1, pression_stream +1, evitements +1` ; blague `lien +2`.
- l. 216 photo : supprimer (profil négatif -2/-1/+1/+1) ; garder (profil autonomie +2) ; deuxième photo `lien +2`.
- l. 337 bonbon : salle secrète `lien +2` ; manger `ilonanium_points +1` + profil autonomie +2 ; mentionner Laplage `lien +2`.
- l. 422 « sortez ensemble » : « J'aimerais bien » `communication +4, confiance +2, jalousie -2 (min 0), lien +2` puis `if lien_jessy_ilona >= 6` (l. 442) ligne bonus ; blague `lien +4` ; laisser Ilona `autonomie_ilona +4, communication +2, confiance +2, ilona_peut_finir_ses_phrases +1, pression_stream -2 (min 0)` ; nier `communication -4, confiance -2, pression_stream +2, evitements +1`.
- l. 518 toit : demander / prendre son temps (profil autonomie +4 avec `ilona_peut_finir_ses_phrases +1`) ; blague puis sincérité (profil communication +4) ; se défendre (profil négatif -4).

Lectures :
- `maison_minecraft_transformation` : l. 56-76 (couloir : serre / piscine / toboggan / else) et l. 612-628 (cantine : poulet / serre / piscine, rien pour toboggan).
- `lien_jessy_ilona >= 6` : l. 442.
- `ilonanium_points` (écrit l. 352) : relu `arc_5_examens.rpy:2556` (`>= 3` et `arc5_valentin_choix == "demande"`, easter egg sans point) et `arc_7_jessy.rpy:1177` (`== 6` et `arc7_jessy_fruit == "goute"` → déclenchement automatique de la fin Ilonanium, clé `finA3`).
- `ilona_peut_finir_ses_phrases` : `etat_relation` (`script.rpy:301,304`) et `arc_6_diplomes.rpy:51` (x6).
- `evitements` : `arc_6_diplomes.rpy:70` uniquement.

## Chronologie

- Avril (l. 23), jour de la rentrée (l. 25) : couloir le matin, toit à midi.
- « Au bout de quelques jours » (l. 175) : habitude.
- « Un après-midi » : quai/train (l. 184) ; la photo reste un sujet « pendant deux jours » (l. 254) ; « Un soir » : déclaration interrompue (l. 256).
- « Le vendredi » : konbini (l. 281). Week-end (l. 380).
- « Le lundi », premier intercours : Allan et Alexandre (l. 387-418) ; « Quand les cours se terminent » : toit (l. 494-503).
- « À midi » : cantine (l. 589) — vraisemblablement un jour suivant (interprétation : le toit est après les cours du lundi).

## Ressources

- Musiques : `audio/music/ecole-music.ogg` (`audio.ecole`), `ecole-roof.ogg`, `ecole-nuit.ogg`, `kombini.ogg` (`audio.kombini`, l. 11), `Metal-gear.ogg` (`audio.metalgear`, l. 13).
- Ambiances : `audio/ambience/breeze-birds.mp3` (toit, quai), `tram-inside.mp3` (train), `crowd-noise.mp3` (cantine), canal `ambiant1`.
- Sons : `bell.mp3`, `train-stop.mp3`, `photo-taken.mp3`, `kombini_open.mp3`, `re-zero-return.mp3` (apparition de Laplage), `snake-alert.mp3`, `aaughmp3.mp3` (Ilona mange l'étoile).
- Aucune CG. Fichiers présents mais non utilisés par l'arc : `images/scenes/backgrounds/transport/bg_arc1_train_inside.jpg`, `images/scenes/backgrounds/school/bg_arc1_school_corridor.jpg` (les `image` de l'arc pointent vers les versions `shared`).

## Incertitudes et contradictions

- Doc `cartographies/arc_1.md` : conforme au script sur menus et effets.
- Branches maison incohérentes (aussi notées en doc) : pas de réplique `poulet` dédiée au couloir (branche générale), aucune réplique `toboggan` à la cantine.
- Bonbon : Ilona « ouvre déjà » le bonbon (l. 295) mais deux options le conservent (salle secrète, poche).
- Option « salle secrète » : objet réel proposé pour une salle Minecraft ; non enregistré dans `maison_minecraft_ajouts`.
- Alexandre est présenté avec Allan comme s'il découvrait le duo (« C'est vous… ? » est dit par Allan seulement) alors qu'il a vu la maison et Jessy au prologue : pas de contradiction stricte.
- Le lien « Laplage = personnage de la rivière » est affirmé par les personnages (l. 316-317), sans autre preuve.
- Doc `cartographies/fiches_personnages.md:147` : Laplage signalerait par des « pouces levés ou baissés ». Script : `laplage thumb_down` est déclaré (`script.rpy:150`) mais jamais affiché ; le pouce est seulement levé, horizontal (arc 4.5 Théo, arc 5) ou explicitement non levé (`arc_4_noel.rpy:557`).
- Sofiane : sprites de base `shy`, `intense`, `smile`, `neutral` déclarés (`script.rpy:138-145`) mais jamais affichés ; la doc le dit « surtout timide », trait non montré à l'écran.
