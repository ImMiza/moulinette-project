# BAD ENDING - LA CAGE DORÉE
# Route Théo, fin catastrophe.
# Attendu : la chaîne « IlonaGaming » explose, Théo gère le succès, Ilona
# s'effondre en silence. Personne ne l'a vue parce que personne ne l'écoutait plus.
#
# Point d'entrée : arc_7_theo.rpy, menu final, option
# « Prioriser les sponsors, la chaîne avant tout. » -> jump bad_ending.
# Les scènes de contexte (stream, dialogue Ilona/Théo, choix) se trouvent dans
# arc_7_theo.rpy. Ce fichier reprend le 7 décembre, au lendemain du million.
#
# Les décors propres à cette fin sont dans images/scenes/ending. Le studio et le
# salon nocturne réutilisent ceux de l'arc 7. La découverte est montrée très
# brièvement à l'ouverture de la porte, puis traitée sur écran noir.

# --- Audio : pistes temporaires réutilisées depuis les assets existants ---
define audio.bakamitai = "audio/music/melancolique-piano.ogg"
define audio.hangShock = "audio/fx/piano-slam.mp3"
define audio.uneasy = "audio/music/tense-piano.ogg"
define audio.majulaLike = "audio/music/plage-sunset.ogg"

# --- Décors de la bad ending ---
image bg apartment night = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_night.png", 1920, 1080)
image bg apartment night nolight = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_night_nolight.jpg", 1920, 1080)
image bg apartment corridor = im.Scale("images/scenes/ending/bg_bad_ending_apartment_corridor_night.jpg", 1920, 1080)
image bg apartment ilona door = im.Scale("images/scenes/ending/bg_bad_ending_ilona_door_bedroom.jpg", 1920, 1080)
image bg apartment ilona bedroom = im.Scale("images/scenes/ending/bg_bad_ending_ilona_bedroom.png", 1920, 1080)
image bg tokyo bar = im.Scale("images/scenes/ending/bg_bad_ending_tokyo_bar_night.jpg", 1920, 1080)
image bg tokyo street night = im.Scale("images/scenes/ending/bg_bad_ending_tokyo_street_night.jpg", 1920, 1080)


label bad_ending:
    $ record_ending("bad_ending")

    # ------------------------------------------------------------------
    # 4. Le 7 décembre : Théo et Allan au bar
    # ------------------------------------------------------------------
    systeme "Le 7 décembre, au lendemain du million."
    systeme "La régie est partie avant l'aube pour le tournage extérieur préparé au studio. Elle ne sera presque pas joignable avant le jour suivant."
    systeme "Dans leur appartement, Ilona et Théo vivent seuls. Ce soir-là, Ilona est censée lancer sans la régie le live court que Théo a maintenu."

    scene bg tokyo bar
    with fade
    play music audio.citynight loop volume 0.5

    systeme "Théo vient de décrocher la campagne de six mois évoquée la veille, pour plusieurs millions de yens. En fin de journée, il retrouve Allan, son ami d'enfance, de passage à Tokyo, pour fêter ça autour d'un verre."

    show allan winter excited at char_left
    show theo tokyo smirk at char_right
    with dissolve

    a "Millionnaire, toi. Sérieux."
    t "Presque. Encore un peu de patience."
    a "Même pas neuf mois après la remise des diplômes. C'est complètement dingue."
    t "Huit mois à Tokyo. On a fait vite. Peut-être trop vite."

    show allan winter neutral at char_left
    show theo tokyo neutral at char_right
    with dissolve

    a "Et toi, sinon ?"
    t "Sinon quoi ?"
    a "Toi. Pas la chaîne, pas les contrats, pas le nombre d'abonnés. Comment tu vas ?"
    t "Je viens de te dire qu'on allait vite."
    a "Ça, c'est un rapport d'activité."
    t "J'habite dans un appartement correct. Le travail me plaît. Tokyo est plus simple que je le pensais."
    a "Immobilier, travail, urbanisme. Tu évites la question dans trois catégories différentes."
    t "Tu t'es entraîné pendant huit mois ?"
    a "J'avais du temps. Tes messages faisaient quatre lignes, captures d'écran comprises."
    t "C'étaient des informations utiles."
    a "C'étaient des courbes."

    show theo tokyo hesitant at char_right
    with dissolve

    t "Je vais bien."
    a "D'accord."
    t "Et tu m'as manqué."

    show allan winter support at char_left
    with dissolve

    a "Toi aussi."

    systeme "Leurs verres restent un instant posés entre eux. Leur dernière vraie conversation remontait au gymnase, le jour du diplôme."

    a "On s'était mal quittés."
    t "Tu m'as dit que j'étais assez malin pour éviter les questions qui me dérangeaient. Ensuite, je t'ai annoncé que je partais dans onze jours."
    a "Résumé fidèle."
    t "J'y ai repensé."
    a "Et ?"
    t "Je n'ai toujours pas toutes les réponses. Mais je ne t'en veux pas d'avoir posé les questions."
    a "Je vais prendre ça pour des excuses."
    t "Ce serait une mauvaise traduction."
    a "Alors ça aussi, ça m'avait manqué."

    show theo tokyo neutral at char_right
    with dissolve

    t "Et toi ? T'as fini par trouver où tu allais ?"
    a "Non. J'ai juste arrêté de traiter le fait de ne pas savoir comme une urgence."
    t "Et ça t'a mené jusqu'ici."
    a "Ça m'a mené à prendre un billet de train. Tokyo était écrit dessus."
    t "Tu es devenu insupportable."
    a "Dix ans à te fréquenter. Les séquelles finissent par se voir."
    t "Pourquoi Tokyo ?"
    a "Je voulais voir la ville. Et je voulais te voir, toi."
    t "Tu pouvais commencer par ça."
    a "Toi aussi."

    show allan winter excited at char_left
    show theo tokyo smirk at char_right
    with dissolve

    systeme "Allan lève son verre."
    a "À nous. Dix ans d'amitié, huit mois de messages nuls et notre premier verre à Tokyo."
    t "Tes messages étaient vagues."
    a "Tes réponses étaient des tableurs."
    t "Des captures de tableurs."
    a "Je sais ce que j'ai dit."

    systeme "Ils trinquent. Pendant quelques secondes, le silence entre eux n'a besoin d'être ni rempli ni traduit. Théo tient dix secondes."

    t "Ilona est en plein stream, là. Regarde, on va la mater deux minutes en buvant nos verres."

    show theo tokyo neutral at char_right
    with dissolve

    systeme "Peu après 20 h, Théo sort son téléphone. La chaîne « IlonaGaming » est hors ligne."

    show theo tokyo hesitant at char_right
    with dissolve

    t "Bizarre... Elle devrait streamer à cette heure-ci."

    systeme "Il l'appelle. Ça sonne dans le vide. Personne ne décroche."
    systeme "Il envoie un message : « Tout va bien ? Je ne te vois pas en stream et tu ne réponds pas. »"

    show theo tokyo disappointed at char_right
    with dissolve

    $ renpy.pause(1.0, hard=True)
    t "C'est la première fois que ça arrive."

    a "Elle va comment, Ilona, ces derniers temps ?"

    t "Elle est épuisée. Elle tire sur sa manche avant de demander quelque chose, elle laisse son verre intact, elle retourne le planning pour ne plus voir le lendemain."
    t "Hier, elle m'a dit qu'elle se sentait seule. Elle m'a demandé de passer l'après-midi avec elle, puis d'annuler le stream du soir."
    t "Alors j'ai réduit sa journée, gardé le rendez-vous sponsors et programmé une heure de live. Elle n'avait plus à choisir elle-même quoi enlever."

    show allan winter doubt at char_left
    with dissolve

    a "Encore un bilan. Je te demande comment elle va."
    t "Je viens de te répondre."
    a "Non. Tu m'as donné les signes, ce qu'elle a dit, puis la solution que t'as appliquée. T'entends pas le trou entre les deux ?"

    show theo tokyo defensive at char_right
    with dissolve

    t "J'ai enlevé le plus lourd. Quelqu'un devait protéger ce qu'elle a construit pendant qu'elle était trop fatiguée pour décider."
    a "Elle te demandait de la protéger de ce qu'elle avait construit."
    t "Elle m'a dit que c'était toujours après. Je l'ai entendue."
    a "Tu l'as entendue, puis t'as conclu à sa place."

    $ renpy.pause(1.0, hard=True)

    show theo tokyo hesitant at char_right
    with dissolve

    t "... Elle a dû s'endormir à l'appartement. Je lui avais libéré l'après-midi pour ça."

    show allan winter support at char_left
    with dissolve

    a "Théo. Faut que tu sois plus présent pour elle. Vraiment présent, pas juste un manager qui dit bravo."
    a "Elle t'a parlé. Toi, t'as transformé sa phrase en planning. C'est pas la même chose qu'écouter."
    a "Et rentre pas avec un restaurant déjà choisi, une heure de départ et trois raisons pour lesquelles ça va lui faire du bien."
    a "Demande-lui ce qu'elle veut. Puis accepte que la réponse puisse être non, rien, ou pas avec toi."

    show theo tokyo defensive at char_right
    with dissolve

    t "Pas avec moi, c'est pas ce qu'elle a demandé."
    a "T'en sais rien. Tu laisses jamais cette question exister assez longtemps."
    t "..."
    t "J'avais déjà choisi le restaurant pendant que tu parlais. Calme, pas loin de la maison, table au fond."
    a "Voilà."

    show theo tokyo disappointed at char_right
    with dissolve

    t "Je vais rentrer et lui demander ce qu'elle veut. Sans options déjà classées. Cette fois, je vais la laisser choisir."

    a "Passe-lui le bonsoir de ma part."

    show allan winter support at char_left
    show theo tokyo hesitant at char_right
    with dissolve

    systeme "Théo laisse son verre à moitié plein. Allan pose une main brève sur son épaule."
    a "Allez. Rentre."

    hide allan
    hide theo
    with dissolve
    stop music fadeout 1.5


    # ------------------------------------------------------------------
    # 5. Retour vers l'appartement
    # ------------------------------------------------------------------
    scene bg tokyo street night
    with fade
    play music audio.citynight loop volume 0.4

    systeme "Théo remonte la rue vers l'appartement. Par réflexe, il recommence à planifier : le restaurant calme, la table loin des enceintes, le trajet le plus court, l'heure à laquelle Ilona fatigue le moins."
    systeme "Au troisième carrefour, il s'arrête. Chaque détail est attentionné. Tout est déjà décidé."
    t "Non."
    systeme "Il efface la réservation qu'il avait ouverte sans même s'en rendre compte. Cette fois, il se le répète : il va la laisser choisir."

    scene bg arc7 intro stream
    with fade

    systeme "Il fait le détour par le studio, à deux rues de l'appartement. Les écrans sont noirs, les lumières éteintes. Ilona n'est jamais venue lancer le live. Elle doit déjà être rentrée, se dit-il. Elle doit se reposer."

    stop music fadeout 3.0

    scene bg apartment night nolight
    with fade

    systeme "Théo ouvre la porte de l'appartement avec ses clés. Dans l'entrée obscure, il reconnaît les chaussures d'Ilona."
    systeme "Aucune lumière n'est allumée."

    t "Je suis rentré !"

    systeme "Il actionne l'interrupteur près de la porte. Le salon s'éclaire. Pas un bruit."

    scene bg apartment night
    with dissolve

    t "Elle doit déjà dormir."

    scene bg apartment corridor
    with dissolve

    systeme "Avant de monter, Théo allume le couloir. Une lumière chaude s'étire jusqu'à la porte d'Ilona, mais aucune lueur ne passe dessous."
    systeme "Théo s'engage dans le couloir."

    scene bg apartment ilona door
    with dissolve

    systeme "Devant la porte de la chambre d'Ilona, Théo toque. Rien."

    t "Ilona ? T'es réveillée ?"
    t "Je suis désolé pour hier. Tu m'as parlé, et j'ai transformé ta réponse en planning."
    t "Je voulais te demander ce que tu veux et écouter la réponse, cette fois."

    systeme "Toujours rien."

    t "Si tu veux que je te laisse seule, je partirai. Si tu ne veux plus de moi, je l'entendrai."

    $ renpy.pause(0.8, hard=True)

    t "... J'entre."
    systeme "Il abaisse la poignée."

    scene black
    with Dissolve(0.3)

    $ renpy.pause(1.0, hard=True)

    systeme "Un déclic. Puis le frottement lent de la porte sur le sol."

    $ renpy.pause(1.5, hard=True)

    systeme "Théo retient son souffle."

    $ renpy.pause(1.0, hard=True)


    # ------------------------------------------------------------------
    # 6. Découverte
    # ------------------------------------------------------------------
    play sound audio.hangShock volume 0.8
    scene bg apartment ilona bedroom
    with vpunch
    stop music fadeout 0.2

    $ renpy.pause(0.35, hard=True)

    play music audio.uneasy loop volume 0.5

    systeme "La porte vient à peine de s'ouvrir. Théo ne voit ni l'ordinateur éteint ni le lit défait. Il ne voit qu'Ilona."

    $ renpy.pause(1.0, hard=True)

    t "Non."
    t "Non, non, non..."

    systeme "Le déni, d'abord. C'est inconcevable. Ilona ne ferait jamais ça."
    systeme "Puis la peur balaie tout le reste. Théo se précipite vers elle en appelant son nom."

    t "Ilona ! Ilona, réponds-moi, s'il te plaît..."
    t "Réveille-toi. Réveille-toi !"

    $ renpy.pause(1.5, hard=True)
    systeme "Il n'y a plus rien à répondre."

    t "Tu m'as dit que tu étais seule. J'ai répondu « après »."
    systeme "Le mot ne lui avait jamais semblé aussi court. Il contient désormais tout ce qu'il n'a pas fait."

    systeme "Il a perdu Ilona. La chaîne et les contrats lui reviennent ensuite, et avec eux l'horreur d'avoir fini par confondre ce qu'ils construisaient avec celle qui le portait."
    systeme "Tout ce qu'il croyait protéger s'effondre comme un château de cartes."

    scene black
    with Dissolve(0.15)

    stop music fadeout 4.0
    $ renpy.pause(2.0, hard=True)


    # ------------------------------------------------------------------
    # 7. Quarante ans plus tard - la plage
    # ------------------------------------------------------------------
    scene bg arc2 beach sunset
    with fade
    play music audio.majulaLike loop volume 0.5 fadein 3.0

    systeme "Quarante ans plus tard."
    systeme "Théo est assis au bord de la plage, dans un crépuscule qui ne change jamais vraiment. Ses cheveux ont grisonné ; la photo entre ses doigts a vieilli plus vite que son souvenir."
    systeme "Sur l'image froissée, Ilona et lui posent devant leur appartement, le jour de leur installation à Tokyo."
    t "..."
    systeme "Il se demande à quoi elle ressemblerait aujourd'hui, si elle était encore là. Pendant quarante ans, il a refait cette dernière journée en déplaçant chaque parole, chaque silence et chaque minute où il aurait pu rentrer plus tôt."

    play sound audio.laplage volume 0.6
    show laplage neutral at char_left
    with dissolve

    laplage "Je remplace quelqu'un qui n'était pas prévu."
    t "Vous dites toujours ça."
    laplage "C'est toujours vrai."

    t "Est-ce que j'aurais pu faire autrement ?"
    laplage "Tu pouvais ouvrir la porte plus tôt. Tu l'as ouverte quand même."
    t "Trop tard."
    laplage "Trop tard, c'est encore une heure. Jamais, ça n'en est pas une."

    t "Ça fait quarante ans que je reviens m'asseoir ici. Ça ne soulage rien."
    laplage "Ça n'a jamais été fait pour soulager. Juste pour que quelqu'un reste assis face à la mer, plutôt que de lui tourner le dos."

    show laplage thumb_up at char_left
    with dissolve

    laplage "Le prochain, c'est toi."

    systeme "Il tend un porte-clés en forme de bloc. Théo le prend. Il reconnaît l'objet qu'Ilona avait emporté à Tokyo et gardé jusqu'à sa dernière nuit."

    hide laplage
    with dissolve

    systeme "Monsieur Laplage s'en va comme d'habitude, sans se retourner. Théo reste face à la mer, le porte-clés au creux de la paume."
    systeme "Il avait appelé son épuisement un risque à gérer, pris son silence pour du repos et transformé sa demande d'aide en décision qu'il pouvait prendre à sa place. Ses regrets ne changent pas ce qu'il a fait. Ils ne se sont pourtant jamais tus."

    t "J'aurais dû t'écouter quand tu étais encore là."

    scene black
    with fade

    t "Je suis désolé, Ilona."

    stop music fadeout 4.0
    return
