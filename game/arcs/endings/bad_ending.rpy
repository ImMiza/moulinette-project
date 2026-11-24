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
# Les décors propres à cette fin sont dans images/scenes/backgrounds/tokyo/. Le studio et le
# salon nocturne réutilisent ceux de l'arc 7. La découverte est montrée très
# brièvement à l'ouverture de la porte, puis traitée sur écran noir.

# --- Audio : pistes temporaires reutilisees depuis les assets existants ---
define audio.sayonara = "audio/music/ddlc-sayori-death-music-rz-3-gu-5.ogg"
define audio.majulaLike = "audio/music/Majula.ogg"
define audio.bar = "audio/music/bar_jazz.ogg"

# --- Décors de la bad ending ---
image bg apartment night = im.Scale("images/scenes/backgrounds/tokyo/bg_arc7_tokyo_house_night.png", 1920, 1080)
image bg apartment night nolight = im.Scale("images/scenes/backgrounds/tokyo/bg_arc7_tokyo_house_night_nolight.jpg", 1920, 1080)
image bg apartment corridor = im.Scale("images/scenes/backgrounds/tokyo/bg_bad_ending_apartment_corridor_night.jpg", 1920, 1080)
image bg apartment ilona door = im.Scale("images/scenes/backgrounds/tokyo/bg_bad_ending_ilona_door_bedroom.jpg", 1920, 1080)
image bg apartment ilona bedroom = im.Scale("images/scenes/backgrounds/tokyo/bg_bad_ending_ilona_bedroom.png", 1920, 1080)
image bg tokyo bar = im.Scale("images/scenes/backgrounds/tokyo/bg_bad_ending_tokyo_bar_night.jpg", 1920, 1080)
image bg tokyo street night = im.Scale("images/scenes/backgrounds/tokyo/bg_bad_ending_tokyo_street_night.jpg", 1920, 1080)
image cg bad allez rentre = "images/scenes/cg/bad_ending/allez_rentre.png"
image cg bad coin plie = "images/scenes/cg/bad_ending/coin_plie.png"
image cg bad le prochain = "images/scenes/cg/bad_ending/le_prochain.png"
image cg bad cabine = "images/scenes/cg/bad_ending/cabine_sur_le_sable.png"


init python:
    renpy.register_shader("moulinette.discovery_vignette", variables="""
        varying vec2 v_tex_coord;
        uniform float u_discovery_vignette;
    """, fragment_450="""
        vec2 centered = (v_tex_coord - vec2(0.5)) * 2.0;
        float radius = length(centered);
        float inner_edge = mix(0.65, 0.30, u_discovery_vignette);
        float outer_edge = mix(1.25, 1.15, u_discovery_vignette);
        float darkness = mix(0.20, 0.65, u_discovery_vignette);
        float vignette = smoothstep(inner_edge, outer_edge, radius);
        gl_FragColor.rgb *= 1.0 - darkness * vignette;
    """)


transform bad_ending_discovery_shock:
    subpixel True
    xalign 0.5
    yalign 0.5
    mesh True
    shader "moulinette.discovery_vignette"
    u_discovery_vignette 0.0
    matrixcolor TintMatrix("#ffd0cb") * SaturationMatrix(0.80) * ContrastMatrix(1.20)
    # Le cadrage serre garde les bords couverts pendant la secousse.
    zoom 1.08
    xoffset -24
    yoffset 14
    linear 0.04 xoffset 24 yoffset -14
    linear 0.04 xoffset -20 yoffset 12
    linear 0.04 xoffset 18 yoffset -10
    linear 0.05 xoffset -14 yoffset 8
    linear 0.05 xoffset 10 yoffset -6
    linear 0.05 xoffset -6 yoffset 3
    linear 0.05 xoffset 0 yoffset 0
    # Le regard se fixe, puis le cadrage recule lentement.
    ease 0.40 zoom 1.22
    pause 0.60
    # Le rouge se vide en gris bleute pendant que les bords s'assombrissent.
    ease 5.0 zoom 1.0 matrixcolor TintMatrix("#becddd") * SaturationMatrix(0.18) * ContrastMatrix(1.12) u_discovery_vignette 1.0


label bad_ending:
    $ record_ending("bad_ending")

    # ------------------------------------------------------------------
    # 4. Le 7 décembre : Théo et Allan au bar
    # ------------------------------------------------------------------
    systeme "Le 7 décembre, au lendemain du million."
    systeme "La régie est partie avant l'aube pour le tournage extérieur préparé au studio. Elle ne sera presque pas joignable avant le jour suivant."
    systeme "Dans leur appartement, Ilona et Théo vivent seuls. Ce soir-là, Ilona est censée lancer sans la régie le live court que Théo a maintenu."
    play music audio.bar loop volume 0.7 fadein 2.0
    scene bg tokyo bar
    with fade

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
    a "Ca, c'est un rapport d'activite."
    t "J'habite dans un appartement correct. Le travail me plait. Tokyo est plus simple que je pensais."
    a "Immobilier, travail, urbanisme. Tu evites la question dans trois categories differentes."
    t "Tu t'es entraine pendant huit mois ?"
    a "J'avais du temps. Tes messages faisaient quatre lignes, captures d'ecran comprises."
    t "C'etaient des informations utiles."
    a "C'etaient des courbes."

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
    show cg bad allez rentre zorder 10
    with dissolve

    systeme "Théo laisse son verre à moitié plein. Allan pose une main brève sur son épaule."
    a "Allez. Rentre."

    hide cg
    hide allan
    hide theo
    with dissolve
    stop music fadeout 1.5


    # ------------------------------------------------------------------
    # 5. Retour vers l'appartement
    # ------------------------------------------------------------------
    scene bg tokyo street night
    with fade

    systeme "Théo remonte la rue vers l'appartement. Par réflexe, il recommence à planifier : le restaurant calme, la table loin des enceintes, le trajet le plus court, l'heure à laquelle Ilona fatigue le moins."
    systeme "Au troisième carrefour, il s'arrête. Chaque détail est attentionné. Tout est déjà décidé."
    t "Non."
    systeme "Il efface la réservation qu'il avait ouverte sans même s'en rendre compte. Cette fois, il se le répète : il va la laisser choisir."

    scene bg arc7 intro stream
    with fade

    systeme "Il fait le détour par le studio, à deux rues de l'appartement. Les écrans sont noirs, les lumières éteintes. Ilona n'est jamais venue lancer le live. Elle doit déjà être rentrée, se dit-il. Elle doit se reposer."

    stop music fadeout 0.0
    stop sound fadeout 0.0
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
    systeme "Il a encore ses clés à la main. Il referme les doigts dessus et glisse le trousseau dans sa poche."

    scene bg apartment ilona door
    with dissolve

    systeme "Devant la chambre, il frappe deux petits coups et recule d'un pas pour lui laisser la place d'ouvrir."

    t "Ilona ? T'es réveillée ?"

    t "Pour hier… J'aurais dû rester avec toi."
    systeme "D'habitude, il aurait déjà posé une deuxième question. Cette fois, il lui laisse le temps."

    t "Ilona ?"

    $ renpy.pause(0.8, hard=True)

    systeme "Il pose la main sur la poignée. Même à travers le bois, il devrait l'entendre si elle se levait."
    t "C'est moi. J'ouvre, d'accord ?"
    systeme "Il pousse la porte du bout des doigts."
    t "{cps=40}Au fait, Allan te passe le bonso-{/cps}{nw}"

    # ------------------------------------------------------------------
    # 6. Découverte
    # ------------------------------------------------------------------

    window hide None
    play music audio.sayonara loop volume 1
    $ renpy.pause(0.20, hard=True)
    scene bg apartment ilona bedroom at bad_ending_discovery_shock
    # Laisser la decouverte et le recul se jouer avant la premiere reaction.
    $ renpy.pause(7.0, hard=True)

    t "Non."
    t "Non, non, non... Ilona, non..."

    systeme "Le déni, d'abord. C'est inconcevable. Ilona ne ferait jamais ça."
    systeme "Puis la peur balaie tout le reste. Théo se précipite vers elle en appelant son nom."

    t "Ilona ! Ilona, réponds-moi, s'il te plaît..."
    t "Réveille-toi. Réveille-toi ! Tu peux pas me laisser sans un mot. Pas comme ça..."

    $ renpy.pause(1.5, hard=True)
    systeme "Il n'y a plus rien à répondre."

    t "Tu m'as dit que tu étais seule. J'ai répondu « après »."
    t "Après le stream. Après les sponsors. Après tout ce que je devais encore régler pour nous."
    t "Je me suis épuisé à tout tenir debout. J'ai tout prévu, tout porté, tout repoussé..."
    t "Je me répétais que c'était pour toi. Pour nous. Que si je prenais les décisions à ta place, tu pourrais enfin souffler."
    t "J'ai fait tellement de choses par amour que j'ai fini par ne plus te demander ce dont tu avais besoin."

    $ renpy.pause(0.8, hard=True)

    t "Alors pourquoi tu ne m'as pas dit que c'était si grave ?"
    t "Pourquoi tu m'as laissé croire qu'il restait du temps ?"
    t "Dis-moi ce que j'aurais dû comprendre. Dis-moi ce que j'aurais dû faire !"
    t "Je t'en prie... donne-moi une explication. Même si elle me détruit."

    systeme "Sa voix se brise. La colère n'arrive pas à tenir debout sans la peur, ni les reproches sans l'amour qui les a nourris."

    t "Tu m'avais demandé de rester avec toi. Pas de réparer ta vie. Juste de rester..."
    t "Et moi, j'ai encore trouvé quelque chose à faire avant."
    t "Je voulais te protéger de tout. Mais je ne t'ai même pas protégée de ma façon de t'aimer."
    t "Pardon. Pardon, Ilona... s'il te plaît, réponds-moi."

    systeme "Le mot ne lui avait jamais semblé aussi court. Il contient désormais tout ce qu'il n'a pas fait, et tout ce qu'il ne pourra plus lui demander de pardonner."

    systeme "Il a perdu Ilona. La chaîne et les contrats lui reviennent ensuite, et avec eux l'horreur d'avoir fini par confondre ce qu'ils construisaient avec celle qui le portait."
    systeme "Tout ce qu'il croyait protéger s'effondre comme un château de cartes."

    window auto hide
    stop music fadeout 1.5
    $ renpy.pause(2.0, hard=True)

    scene black with fade
    pause 2.0

    if boucle_passe():
        jump bad_ending_boucle_rejouee


    # ------------------------------------------------------------------
    # 7. Quarante ans plus tard - la plage
    # ------------------------------------------------------------------
    play ambiant1 audio.wave loop volume 0.40 fadein 2.0
    scene bg arc2 beach sunset
    show theo ilonanium older_regretful at char_right
    with fade

    systeme "Quarante ans plus tard."
    show ilonanium_photo at Transform(pos=(0.5, 0.40), anchor=(0.5, 0.5), rotate=-3) zorder 20 with dissolve
    systeme "Théo tient une photo entre ses doigts. Ilona et lui, serrés dans le cadre, le sourire un peu trop grand. Il se rappelle l'heure de la photo. Il a oublié qui les a fait rire."
    systeme "Certains soirs, dans sa tête, il rentre directement. D'autres, il s'arrête au studio et l'appelle depuis la rue. Il arrive toujours devant la même porte."
    hide ilonanium_photo with dissolve

    play sound audio.laplage volume 0.6
    show laplage neutral at char_left
    with dissolve

    laplage "Je peux m'asseoir ?"
    systeme "Théo pose la photo sur le sable et se décale."
    t "Si j'étais rentré une heure plus tôt..."
    laplage "Elle t'avait demandé quoi, la veille ?"
    t "Comment vous savez ça ?"
    laplage "Je me suis posé la question assez souvent. Réponds."
    t "De rester avec elle l'après-midi. D'annuler le live."
    systeme "Il lisse du pouce un coin de la photo."
    t "J'ai gardé une heure de live. Je lui ai dit qu'après, on aurait toute la soirée."

    pause 1.5
    systeme "Laplage décroche de son manteau le petit creeper vert. Il le pose sur le sable, à côté de la photo."
    laplage "Il reste des passages vers le passé. Seulement là où les lignes temporelles se croisent."
    show theo ilonanium older_surprised at char_right with dissolve
    t "...Vous vous foutez de moi ?"
    laplage "Non."
    t "Le passé. Comme ça. Assis sur une plage, avec un porte-clés."
    laplage "Poche gauche. Un bloc de Minecraft. Elle l'avait perdu ici. C'est toi qui l'as retrouvé."
    systeme "Théo plonge la main dans sa poche. Le bloc est là. Il ne l'a montré à personne."
    t "...Admettons. Alors je peux revenir ce soir-là."
    laplage "Le premier passage d'ici s'ouvrira dans dix ans."
    t "Et il mène à quelle date ?"
    laplage "Avant la rentrée d'avril. Ilona ne connaîtra Jessy que depuis une soirée de Minecraft."
    show theo ilonanium older_regretful at char_right with dissolve
    t "Pas ce soir-là."
    laplage "Non. Pas ce soir-là."
    systeme "Théo baisse les yeux vers la photo. Cette soirée n'existe plus nulle part où il pourrait entrer."
    t "Et je pourrai revenir à aujourd'hui ?"
    laplage "Un aller simple. Le passage se refermera derrière toi."

    t "Elle va me prendre pour un fou. Je pourrais lui montrer la photo. Lui expliquer ce qui va se passer."
    laplage "Et si elle te demande de la laisser tranquille ?"

    show theo ilonanium older_regretful at char_right with dissolve
    systeme "Théo ouvre la bouche. Il avait déjà trouvé par quoi commencer pour la convaincre."
    pause 2.0
    t "Alors il faudra que je la laisse tranquille."

    show cg bad coin plie zorder 10 with dissolve
    systeme "Laplage sort une photo de son manteau et la pose à côté de celle de Théo. Même photo. Même coin plié, usé au même endroit par le même pouce."
    pause 1.5
    hide cg with dissolve
    systeme "Théo relève les yeux. Sous la moustache de Laplage, il reconnaît son propre visage."
    t "Vous êtes… moi."
    systeme "Laplage ne dément pas."
    t "Vous aussi, on vous l'a donné ici ?"
    laplage "À peu près à la même place."
    show cg bad le prochain zorder 10 with dissolve
    systeme "Laplage ramasse le creeper et le dépose dans la main de Théo. Une chaleur lui remonte dans le poignet."
    laplage "Tu sentiras le passage s'ouvrir. Serre le creeper dans ta main et le TARDIS viendra."

    laplage "Le prochain, c'est toi."

    hide cg
    hide laplage
    with dissolve
    systeme "Théo sort de sa poche le porte-clés en forme de bloc qu'Ilona avait gardé à Tokyo. Il range les deux porte-clés dans la même poche, puis replie la photo."

    # 8. Le passage et la première apparition de Laplage
    scene black with fade
    centered "DIX ANS PLUS TARD"
    scene bg arc2 beach sunset
    with fade
    systeme "Dix ans à ne parler à personne. Les deux porte-clés n'ont pas quitté la même poche."
    systeme "Au bord de l'eau, le creeper se réchauffe dans la main de Théo."
    play sound audio.ilonanium_arrival volume 0.55
    scene cg bad cabine with dissolve
    systeme "Un grondement monte derrière lui. Il se retourne. Une cabine bleue s'est posée sur le sable."
    systeme "Théo glisse la photo dans son manteau, pousse la porte et monte à l'intérieur."
    stop ambiant1 fadeout 1.0
    play sound audio.ilonanium_departure volume 0.65
    scene black
    with fade

    play music audio.mcnight volume 0.65 fadein 2.0
    scene bg prologue roof night
    show jessy minecraft at char_left
    show ilona minecraft at char_right
    with dissolve
    i "Elle est vraiment trop grande."
    j "On peut enlever des pièces."
    i "Non. Ce serait triste."

    play sound audio.laplage volume 0.6
    scene bg prologue river laplage
    show laplage minecraft at char_center
    with dissolve
    systeme "Au bord de la rivière, un personnage apparaît. Aucun pseudo ne flotte au-dessus de sa tête. Il lève les yeux vers la maison."
    systeme "Dans sa poche, il referme la main sur le porte-clés en forme de bloc."
    pause 1.0
    m_inconnu "Construire ensemble, c'est facile."
    pause 0.8
    m_inconnu "Le plus difficile, c'est de ne pas casser ce que l'autre construit."
    pause 1.5

    stop sound fadeout 0.5
    stop music fadeout 2.0
    scene black with fade
    $ enregistrer_boucle()
    return


# ----------------------------------------------------------------------
# 7-8 bis. Bad ending rejouée alors que la boucle a déjà eu lieu
# (persistent.retour_dans_le_passe) : Laplage est le Théo de la boucle précédente.
# ----------------------------------------------------------------------
label bad_ending_boucle_rejouee:
    play ambiant1 audio.wave loop volume 0.40 fadein 2.0
    scene bg arc2 beach sunset
    show theo ilonanium older_regretful at char_right
    with fade

    systeme "Quarante ans plus tard."
    show ilonanium_photo at Transform(pos=(0.5, 0.40), anchor=(0.5, 0.5), rotate=-3) zorder 20 with dissolve
    systeme "Théo tient une photo entre ses doigts. Ilona et lui, serrés dans le cadre. Le coin est plié. Il ne se souvient pas de l'avoir plié."
    systeme "Depuis quarante ans, une phrase lui revient plus souvent que les autres. Un serveur en tenue de maid, un soir d'hiver : « La chaîne s'arrête à moi. J'espère. »"
    hide ilonanium_photo with dissolve

    play sound audio.laplage volume 0.6
    show laplage neutral at char_left
    with dissolve

    t "Le Messi."
    laplage "Ça faisait longtemps que personne ne m'avait appelé comme ça."
    systeme "Laplage s'assoit sans demander. Il a l'air plus vieux que dans les souvenirs de Théo. Plus vieux que Théo aussi, ce qui ne devrait pas être possible."
    t "Vous étiez partout. Le festival, Noël, Tokyo. Vous disiez des phrases que je ne comprenais pas."
    laplage "Tu les comprenais. Tu ne voulais pas qu'elles parlent de toi."
    t "Au marché de Noël, je vous ai dit que je me souvenais de tout. Vous avez répondu « moi aussi »."
    laplage "Je me souvenais de ce soir-là. Du bar. De l'heure de live. De la porte."

    pause 1.5
    show theo ilonanium older_surprised at char_right with dissolve
    t "...Vous saviez."
    laplage "Oui."
    t "Et vous m'avez laissé faire."
    laplage "Je suis revenu pour qu'elle puisse choisir. Pas pour choisir à ta place."
    laplage "Je t'ai dit ce que j'aurais voulu entendre. Tu as fait ce que j'avais fait."
    show theo ilonanium older_regretful at char_right with dissolve
    t "Alors ça ne sert à rien."
    laplage "Ça sert à une chose. Maintenant, tu sais que ce n'était pas une question de souvenirs."

    show cg bad coin plie zorder 10 with dissolve
    systeme "Laplage pose sa photo à côté de celle de Théo. Même photo. Même coin plié. Mais le sien est usé jusqu'à la trame, comme si deux pouces l'avaient frotté l'un après l'autre."
    pause 1.5
    hide cg with dissolve
    t "Combien de fois ?"
    laplage "Assez pour reconnaître la plage."
    t "Et si je refuse ? Si je reste ici ?"
    laplage "Alors quelqu'un d'autre viendra peut-être s'asseoir. Ou personne."

    pause 1.0
    systeme "Laplage décroche le creeper de son manteau et le pose sur le sable, entre les deux photos."
    laplage "Le passage s'ouvrira dans dix ans. Avant la rentrée d'avril. Aller simple, comme la dernière fois."
    t "La dernière fois, c'était vous."
    laplage "La dernière fois, c'était nous."
    t "Qu'est-ce que je fais de différent ?"
    laplage "Ne prépare rien. Pas de discours, pas de plan, pas de photo à lui montrer."
    laplage "Et quand elle te demandera de rester, ne garde pas une heure pour toi."

    show cg bad le prochain zorder 10 with dissolve
    systeme "Théo ramasse le creeper lui-même. Cette fois, personne ne le lui tend."
    laplage "Le prochain, c'est encore toi."

    hide cg
    hide laplage
    with dissolve
    systeme "Quand Théo relève la tête, la place à côté de lui est vide. Dans le sable, une seule série de traces de pas. Les siennes."
    systeme "Il range le creeper avec le porte-clés en forme de bloc. Il passe le pouce sur le coin plié de la photo. Cette fois, il sait pourquoi il est usé."

    scene black with fade
    centered "DIX ANS PLUS TARD"
    scene bg arc2 beach sunset
    with fade
    systeme "Dix ans. Cette fois, Théo ne les a pas passés à répéter ce qu'il dirait. Il a appris à se taire."
    systeme "Au bord de l'eau, le creeper se réchauffe dans sa main."
    play sound audio.ilonanium_arrival volume 0.55
    scene cg bad cabine with dissolve
    systeme "La cabine bleue se pose sur le sable. Théo reconnaît le grincement de la porte avant de l'entendre."
    stop ambiant1 fadeout 1.0
    play sound audio.ilonanium_departure volume 0.65
    scene black
    with fade

    play music audio.mcnight volume 0.65 fadein 2.0
    scene bg prologue roof night
    show jessy minecraft at char_left
    show ilona minecraft at char_right
    with dissolve
    i "Elle est vraiment trop grande."
    j "On peut enlever des pièces."
    i "Non. Ce serait triste."
    j "Même le couloir sans sortie ?"
    i "Surtout lui."

    play sound audio.laplage volume 0.6
    scene bg prologue river laplage
    show laplage minecraft at char_center
    with dissolve
    systeme "Au bord de la rivière, un personnage apparaît. Cette fois, il ne lève pas les yeux vers la maison. Il regarde Ilona."
    pause 1.0
    m_inconnu "Construire ensemble, c'est facile."
    pause 0.8
    m_inconnu "Le plus difficile, c'est de ne pas casser ce que l'autre construit."
    pause 1.5
    systeme "Il reste au bord de l'eau. Il ne s'approche pas."

    stop sound fadeout 0.5
    stop music fadeout 2.0
    scene black with fade
    return
