# Notes — Fin B2 (`finB2`)

Source : `arcs/endings/bad_ending.rpy` (368 lignes, label `bad_ending`, l.31). Aucun `centered` : pas de titre ni de catégorie affichés en jeu. Titre de travail en commentaire : « BAD ENDING - LA CAGE DORÉE » (l.1). L'expression « cage dorée » apparaît en jeu dans la route (`arc_7_theo.rpy:1473`).

## Personnages

**Théo** : a décroché la campagne de six mois « pour plusieurs millions de yens » (l.44) ; fête ça avec Allan ; rentre, découvre Ilona (l.267-305) ; quarante ans plus tard, cheveux grisonnants, sur la plage (l.325-365).
Sprites : `theo tokyo` (smirk, neutral, hesitant, disappointed, defensive).

**Allan** (`a`) : « de passage à Tokyo », ami d'enfance (« Dix ans d'amitié », l.114) ; dernière vraie conversation au gymnase le jour du diplôme (l.83-86) ; pousse Théo à demander à Ilona ce qu'elle veut (l.174-177). Sprites `allan winter` (excited, neutral, support, doubt) définis dans `arcs/arc_4/arc_4_noel.rpy:52-59`.

**Monsieur Laplage** : sur la plage (l.331-357), sprites `neutral`, `thumb_up` ; remet le porte-clés bloc.

**Ilona** : n'apparaît pas en sprite. Morte dans sa chambre ; cause non nommée, geste volontaire suggéré par « Ilona ne ferait jamais ça » (l.278) — interprétation.

Citations :
- « T'entends pas le trou entre les deux ? » — Allan (l.154).
- « Demande-lui ce qu'elle veut. Puis accepte que la réponse puisse être non, rien, ou pas avec toi. » — Allan (l.177).
- « Je voulais te protéger de tout. Mais je ne t'ai même pas protégée de ma façon de t'aimer. » — Théo (l.304).
- « Trop tard, c'est encore une heure. Jamais, ça n'en est pas une. » — Laplage (l.342).
- « J'aurais dû t'écouter quand tu étais encore là. » — Théo (l.360).

## Lieux

- Bar : `images/scenes/backgrounds/tokyo/bg_bad_ending_tokyo_bar_night.jpg`.
- Rue : `images/scenes/backgrounds/tokyo/bg_bad_ending_tokyo_street_night.jpg`.
- Studio (détour) : `images/scenes/backgrounds/streaming/bg_arc7_intro_stream.jpg` (≠ décor du studio dans la route).
- Appartement : `bg_arc7_tokyo_house_night_nolight.jpg`, `bg_arc7_tokyo_house_night.png` (redéclarés sous les noms `bg apartment night[ nolight]`, l.22-23), couloir `bg_bad_ending_apartment_corridor_night.jpg`, porte `bg_bad_ending_ilona_door_bedroom.jpg`, chambre `bg_bad_ending_ilona_bedroom.png`.
- Plage : `images/scenes/backgrounds/beach/bg_arc2_beach_sunset.jpg` (`bg arc2 beach sunset`, défini `arcs/arc_2/arc_2_plage.rpy:4`).

## Objets et concepts

- Porte-clés bloc (plage de l'arc 2 → Tokyo → remis par Laplage, l.352). Photo de l'installation à Tokyo (l.327).
- « Je remplace quelqu'un qui n'était pas prévu » / « Le prochain, c'est toi. » (l.335, 350) : sens non expliqué (interprétation : Théo prendrait la place de Laplage).

## Mécaniques

- `record_ending("bad_ending")` (l.32) → `endings_seen`. Aucun menu, aucune condition. Fin par `return` (l.368).

## Chronologie

- 7 décembre, lendemain du million (l.37) ; peu après 20 h, chaîne hors ligne (l.127). Puis « Quarante ans plus tard » (l.325).

## Ressources

- Musique jouée : `audio.bar` → `audio/music/bar_jazz.ogg` (l.40, arrêtée l.205). Ensuite aucune musique.
- Déclarées non jouées : `audio.bakamitai` (`Baka_Mitai.ogg`), `audio.sayonara` (`Sayo-nara.ogg`), `audio.majulaLike` (`Majula.ogg`, `play` commenté l.323). Commentaire l.15 : « pistes temporaires ».
- Son `audio.laplage` (l.331). Effet `vpunch` à la découverte (l.269).
- Aucune CG ; la découverte est un décor (`bg_bad_ending_ilona_bedroom.png`).

## Incertitudes et contradictions

- Le commentaire l.11-12 dit que « le studio et le salon nocturne réutilisent ceux de l'arc 7 », mais le studio utilise `bg arc7 intro stream`, décor jamais montré dans la route (qui utilise `bg_arc7_tokyo_streaming_studio_night.jpg`).
- Accents manquants dans plusieurs répliques d'Allan/Théo (l.63-69 : « Ca », « activite », « evites », « entraine »…), contrairement au reste du fichier.
- `stop music fadeout 4.0` final (l.367) alors qu'aucune musique ne joue.
- Musique de l'option sponsors (`audio.depressed`, typo `auddio` dans `arc_7_theo.rpy:27`) arrêtée avant le saut (`arc_7_theo.rpy:1499`).
