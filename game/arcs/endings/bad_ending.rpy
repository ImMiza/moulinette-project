# BAD ENDING - LA CAGE DOREE
# Route Theo, fin catastrophe.
# Attendu : la chaine "IlonaGaming" explose, Theo gere le succes, Ilona s'effondre
# en silence. Personne ne l'a vue parce que personne ne l'ecoutait plus.
#
# STATUT : brouillon complet. Point d'entree : arc_7_theo.rpy, menu final,
# option "Prioriser les sponsors, la chaine avant tout." -> jump bad_ending.
# Les scenes de contexte (stream, dialogue Ilona/Theo, choix) ont ete deplacees
# dans arc_7_theo.rpy. Ce fichier reprend le lendemain, en fin de journee.
#
# ASSETS : les decors propres a cette fin sont dans images/scenes/ending ; le
# salon nocturne reutilise celui de l'arc 7. Les sprites perso
# (ilona/theo/allan/laplage) reutilisent les poses deja existantes du jeu.
# Aucune image explicite de la scene de pendaison n'est utilisee : le moment est
# traite en ecran noir + son + texte, jamais montre a l'image (choix deliberer,
# coherent avec le ton du jeu et plus sobre qu'un rendu graphique).

# --- Audio : pistes temporaires reutilisees depuis les assets existants ---
define audio.bakamitai = "audio/music/melancolique-piano.ogg"
define audio.hangShock = "audio/fx/piano-slam.mp3"
define audio.uneasy = "audio/music/tense-piano.ogg"
define audio.majulaLike = "audio/music/plage-sunset.ogg"

# --- Decors de la bad ending ---
image bg apartment night = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_night.png", 1920, 1080)
image bg apartment corridor = im.Scale("images/scenes/ending/bg_bad_ending_apartment_corridor_night.jpg", 1920, 1080)
image bg apartment ilona door = im.Scale("images/scenes/ending/bg_bad_ending_ilona_door_bedroom.jpg", 1920, 1080)
image bg apartment ilona bedroom = im.Scale("images/scenes/ending/bg_bad_ending_ilona_bedroom.jpg", 1920, 1080)
image bg tokyo bar = im.Scale("images/scenes/ending/bg_bad_ending_tokyo_bar_night.jpg", 1920, 1080)
image bg tokyo street night = im.Scale("images/scenes/ending/bg_bad_ending_tokyo_street_night.jpg", 1920, 1080)


label bad_ending:
    $ record_ending("bad_ending")

    # ------------------------------------------------------------------
    # 4. Le lendemain : Theo et Allan au bar
    # ------------------------------------------------------------------
    systeme "Le lendemain."
    systeme "La regie est partie avant l'aube pour le tournage exterieur prepare au studio. Elle ne sera presque pas joignable avant le jour suivant."
    systeme "A l'appartement, Ilona et Theo vivent seuls. Ce soir-la, Ilona est censee lancer sans la regie le live court que Theo a maintenu."

    scene bg tokyo bar
    with fade
    play music audio.citynight loop volume 0.5

    systeme "Theo vient de decrocher la campagne de six mois evoquee la veille, pour plusieurs millions de yens. En fin de journee, il retrouve Allan, son ami d'enfance, de passage a Tokyo, pour feter ca autour d'un verre."

    show allan winter excited at char_left
    show theo tokyo smirk at char_right
    with dissolve

    a "Millionnaire, toi. Sérieux."
    t "Presque. Encore un peu de patience."
    a "Meme pas neuf mois apres la remise des diplomes. C'est completement dingue."
    t "Huit mois a Tokyo. On a fait vite. Peut-etre trop vite."

    show allan winter neutral at char_left
    show theo tokyo neutral at char_right
    with dissolve

    a "Et toi, sinon ?"
    t "Sinon quoi ?"
    a "Toi. Pas la chaine, pas les contrats, pas le nombre d'abonnes. Comment tu vas ?"
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
    t "Et tu m'as manque."

    show allan winter support at char_left
    with dissolve

    a "Toi aussi."

    systeme "Leurs verres restent un instant poses entre eux. Leur derniere vraie conversation remontait au gymnase, le jour du diplome."

    a "On s'etait mal quittes."
    t "Tu m'as dit que j'etais assez malin pour eviter les questions qui me derangeaient. Ensuite, je t'ai annonce que je partais dans onze jours."
    a "Resume fidele."
    t "J'y ai repense."
    a "Et ?"
    t "Je n'ai toujours pas toutes les reponses. Mais je ne t'en veux pas d'avoir pose les questions."
    a "Je vais prendre ca pour des excuses."
    t "Ce serait une mauvaise traduction."
    a "Alors ca aussi, ca m'avait manque."

    show theo tokyo neutral at char_right
    with dissolve

    t "Et toi ? T'as fini par trouver ou tu allais ?"
    a "Non. J'ai juste arrete de prendre le fait de pas savoir pour une urgence."
    t "Et ca t'a mene au Japon."
    a "Ca m'a mene a prendre un billet. Le Japon etait ecrit dessus."
    t "Tu es devenu insupportable."
    a "Dix ans a te frequenter. Les sequelles finissent par se voir."
    t "Pourquoi Tokyo ?"
    a "Je voulais voir la ville. Et je voulais te voir, toi."
    t "Tu pouvais commencer par ca."
    a "Toi aussi."

    show allan winter excited at char_left
    show theo tokyo smirk at char_right
    with dissolve

    systeme "Allan leve son verre."
    a "A nous. Dix ans d'amitie, huit mois de messages nuls, et notre premier verre a Tokyo."
    t "Tes messages etaient vagues."
    a "Tes reponses etaient des tableurs."
    t "Des captures de tableurs."
    a "Je sais ce que j'ai dit."

    systeme "Ils trinquent. Pendant quelques secondes, le silence entre eux n'a besoin d'etre ni rempli ni traduit. Theo tient dix secondes."

    t "Ilona est en plein stream la, tiens, regarde, on va la mater deux minutes en buvant nos verres."

    show theo tokyo neutral at char_right
    $ renpy.pause(0.5, hard=True)
    systeme "Theo sort son telephone. La chaine « IlonaGaming » est hors ligne."

    t "Bizarre... elle stream, normalement, a cette heure-ci."

    show theo tokyo defensive at char_right
    systeme "Il l'appelle. Ca sonne dans le vide. Personne ne decroche."
    systeme "Il envoie un message : « tout va bien ? je te vois pas en stream et tu reponds pas. »"

    $ renpy.pause(1.0, hard=True)
    t "C'est la premiere fois que ca arrive, ca."

    a "Elle va comment, Ilona, ces derniers temps ?"

    show theo tokyo disappointed at char_right
    t "Elle est epuisee. Elle tire sur sa manche avant de demander quelque chose, elle laisse son verre intact, elle retourne le planning pour ne plus voir le lendemain."
    t "Hier, elle m'a dit qu'elle se sentait seule. Elle m'a demande de passer l'apres-midi avec elle, puis d'annuler le stream du soir."
    t "Alors j'ai reduit sa journee, garde le rendez-vous sponsors et programme une heure de live. Elle n'avait plus a choisir elle-meme quoi enlever."

    show allan winter doubt at char_left
    a "Encore un bilan. Je te demande comment elle va."
    t "Je viens de te repondre."
    a "Non. Tu m'as donne les signes, ce qu'elle a dit, puis la solution que t'as appliquee. T'entends pas le trou entre les deux ?"

    show theo tokyo defensive at char_right
    t "J'ai enleve le plus lourd. Quelqu'un devait proteger ce qu'elle a construit pendant qu'elle etait trop fatiguee pour decider."
    a "Elle te demandait de la proteger de ce qu'elle avait construit."
    t "Elle m'a dit que c'etait toujours apres. Je l'ai entendue."
    a "Tu l'as entendue, puis t'as conclu a sa place."

    $ renpy.pause(1.0, hard=True)

    show theo tokyo disappointed at char_right
    t "... Elle a du s'endormir a l'appartement. Je lui avais libere l'apres-midi pour ca."

    show allan winter support at char_left
    a "Theo. Faut que tu sois plus present pour elle. Vraiment present, pas juste un manager qui dit bravo."
    a "Elle t'a parle. Toi, t'as transforme sa phrase en planning. C'est pas la meme chose qu'ecouter."
    a "Et rentre pas avec un restaurant deja choisi, une heure de depart et trois raisons pour lesquelles ca va lui faire du bien."
    a "Demande-lui ce qu'elle veut. Puis accepte que la reponse puisse etre non, rien, ou pas avec toi."

    show theo tokyo defensive at char_right
    t "Pas avec moi, c'est pas ce qu'elle a demande."
    a "T'en sais rien. Tu laisses jamais cette question exister assez longtemps."
    t "..."
    t "J'avais deja choisi le restaurant pendant que tu parlais. Calme, pas loin de la maison, table au fond."
    a "Voila."

    show theo tokyo disappointed at char_right
    t "Je vais rentrer et lui demander ce qu'elle veut. Sans options deja classees. Cette fois, je vais la laisser choisir."

    a "Passe-lui le bonsoir de ma part."

    show allan winter support at char_left
    show theo tokyo neutral at char_right
    systeme "Theo laisse son verre a moitie plein. Allan pose une main breve sur son epaule."
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

    systeme "Theo remonte la rue vers l'appartement. Par reflexe, il recommence a planifier : le restaurant calme, la table loin des enceintes, le trajet le plus court, l'heure a laquelle Ilona fatigue moins."
    systeme "Au troisieme carrefour, il s'arrete. Tout est attentionne. Tout est deja decide."
    t "Non."
    systeme "Il efface la reservation qu'il avait ouverte sans meme s'en rendre compte. Cette fois, il se le repete, il va la laisser choisir."
    systeme "Il fait le detour par le studio, a deux rues de l'appartement. Les locaux sont noirs. Ilona n'est jamais venue lancer le live. Elle doit deja etre rentree, se dit-il. Elle doit se reposer."

    stop music fadeout 3.0

    scene bg apartment night
    with fade

    systeme "Theo ouvre la porte de l'appartement avec ses cles. Dans l'entree, il reconnait les chaussures d'Ilona."
    systeme "Aucune lumiere n'est allumee."

    t "Je suis rentre !"

    systeme "Il allume la lumiere du salon. Pas un bruit."

    t "Elle doit deja dormir."

    scene bg apartment corridor
    with dissolve

    systeme "Theo s'engage dans le couloir. La lumiere du salon s'etire jusqu'a la porte d'Ilona, mais aucune lumiere ne passe dessous."

    scene bg apartment ilona door
    with dissolve

    systeme "Devant la porte de la chambre d'Ilona, Theo toque. Rien."

    t "Ilona ? T'es reveillee ?"
    t "Tu m'as parle hier. C'est moi qui ai transforme ta reponse en planning."
    t "Je vais pas te dire ce qui te ferait du bien. On peut sortir, rester ici, parler, ne rien faire... ou tu peux vouloir que je te laisse seule."
    t "C'est toi qui choisis. Et si la reponse, c'est pas avec moi, je l'entendrai."

    systeme "Toujours rien."

    t "... J'entre."


    # ------------------------------------------------------------------
    # 6. Decouverte - traitee hors-champ, jamais montree a l'image
    # ------------------------------------------------------------------
    scene bg apartment ilona bedroom
    with dissolve

    systeme "La porte s'ouvre sur la chambre silencieuse. L'ordinateur est eteint. Le lit est defait."

    $ renpy.pause(1.0, hard=True)

    scene black
    with fade

    play sound audio.hangShock volume 0.8
    with vpunch
    stop music fadeout 0.2
    play music audio.uneasy loop volume 0.5

    $ renpy.pause(1.5, hard=True)

    systeme "..."
    systeme "Theo reste immobile dans l'encadrement de la porte."

    t "Non."
    t "Non, non, non..."

    systeme "Le deni, d'abord. C'est inconcevable. Ilona ne ferait jamais ca."
    systeme "Puis la tristesse arrive, et elle ne laisse plus de place pour le deni."

    t "Ilona ! Ilona, reponds-moi, s'il te plait..."
    t "Reveille-toi. Reveille-toi !"

    $ renpy.pause(1.5, hard=True)
    systeme "Il n'y a plus rien a repondre."

    scene black
    with fade

    systeme "Il a perdu Ilona. La chaine et les contrats lui reviennent ensuite, et avec eux l'horreur d'avoir fini par confondre ce qu'ils construisaient avec celle qui le portait."
    systeme "Tout ce qu'il croyait proteger s'effondre comme un chateau de cartes."

    stop music fadeout 4.0
    $ renpy.pause(2.0, hard=True)


    # ------------------------------------------------------------------
    # 7. Quarante ans plus tard - la plage
    # ------------------------------------------------------------------
    scene bg arc2 beach sunset
    with fade
    play music audio.majulaLike loop volume 0.5 fadein 3.0

    systeme "Quarante ans plus tard."

    show theo tokyo disappointed at char_center  # Remplace provisoirement le sprite dedie "Theo age".
    systeme "Un vieil homme est assis au bord de la plage, dans un crepuscule qui ne change jamais vraiment. Meme tenue que Monsieur Laplage, sans le porte-cles creeper."

    systeme "Il sort une vieille photo froissee de sa poche : lui et Ilona devant leur appartement, le jour de leur installation a Tokyo."
    t "..."
    systeme "Il se demande a quoi elle ressemblerait aujourd'hui, si elle etait encore la. Il regrette les mauvais choix. Surtout celui d'avoir ignore ses appels a l'aide, tant qu'il etait encore temps de les entendre."

    play sound audio.laplage volume 0.6
    show laplage neutral at char_left
    with dissolve

    laplage "Je remplace quelqu'un qui n'etait pas prevu."
    t "Vous dites toujours ca."
    laplage "C'est toujours vrai."

    t "Est-ce que j'aurais pu faire autrement ?"
    laplage "Tu pouvais ouvrir la porte plus tot. Tu l'as ouverte quand meme."
    t "Trop tard."
    laplage "Trop tard, c'est encore une heure. Jamais, ca n'en est pas une."

    t "Ca fait quarante ans que je m'assois ici. Ca soulage rien."
    laplage "Ca n'a jamais ete fait pour soulager. Juste pour que quelqu'un reste assis face a la mer, au lieu de dos a elle."

    show laplage thumb_up at char_left
    laplage "Le prochain, c'est toi."

    systeme "Il tend un porte-cles en forme de bloc. Theo le prend, sans trop savoir pourquoi ca lui semble juste."

    hide laplage
    with dissolve

    systeme "Monsieur Laplage s'en va comme d'habitude, sans se retourner."

    show theo tokyo reassuring at char_center  # Equivalent disponible de la pose "pouce leve".
    systeme "Theo leve le pouce vers l'horizon, exactement comme lui."

    scene black
    with fade

    systeme "Générique."
    # TODO: play music audio.bakamitai loop volume 0.6 - asset a fournir.

    return
