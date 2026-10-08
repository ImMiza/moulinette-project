# ARC VII - ROUTE JESSY : LA RANDONNEE
# La reponse au bivouac fixe la relation ; le fruit ouvre la piste Ilonanium.

default arc7_jessy_fruit = ""       # goute / jette
default arc7_jessy_dejeuner = ""    # amitie / crush
default arc7_jessy_relation = ""    # amitie / amour
default arc7_jessy_tente = False
default arc7_jessy_family_epilogue = False

# Tenues estivales de ville pour les scènes hors montagne.
image allan beach silence = speaker_sprite("allan", "images/personnages/Allan/beach/uncomfortable_silence.png")
image allan beach support = speaker_sprite("allan", "images/personnages/Allan/beach/quiet_support.png")
# Tenues de randonnée. Les expressions indisponibles sans sac reprennent le sprite le plus proche.
image jessy rando neutral = speaker_sprite("jessy", "images/personnages/Jessy/rando/neutral_attentiveness.png")
image jessy rando smile = speaker_sprite("jessy", "images/personnages/Jessy/rando/shy_warm_smile.png")
image jessy rando listening = speaker_sprite("jessy", "images/personnages/Jessy/rando/neutral_attentiveness.png")
image jessy rando determined = speaker_sprite("jessy", "images/personnages/Jessy/rando/happy.png")
image jessy rando embarrassed = speaker_sprite("jessy", "images/personnages/Jessy/rando/nervous_embarrassment.png")
image jessy rando bag neutral = speaker_sprite("jessy", "images/personnages/Jessy/rando/with_bag/neutral_attentiveness.png")
image jessy rando bag smile = speaker_sprite("jessy", "images/personnages/Jessy/rando/with_bag/shy_warm_smile.png")
image jessy rando bag listening = speaker_sprite("jessy", "images/personnages/Jessy/rando/with_bag/neutral_attentiveness.png")
image jessy rando bag determined = speaker_sprite("jessy", "images/personnages/Jessy/rando/with_bag/happy.png")
image jessy rando bag embarrassed = speaker_sprite("jessy", "images/personnages/Jessy/rando/with_bag/nervous_embarrassment.png")
image ilona rando neutral = speaker_sprite("ilona", "images/personnages/Ilona/rando/neutral.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona rando smile = speaker_sprite("ilona", "images/personnages/Ilona/rando/playful_warm_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona rando embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/rando/awkward_embarrassment.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona rando sad = speaker_sprite("ilona", "images/personnages/Ilona/rando/sad.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona rando bag neutral = speaker_sprite("ilona", "images/personnages/Ilona/rando/with_bag/neutral_rando.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona rando bag smile = speaker_sprite("ilona", "images/personnages/Ilona/rando/with_bag/playful_warm_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona rando bag embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/rando/with_bag/awkward_embarrassment.png", ILONA_SIZE[0], ILONA_SIZE[1])

# Les futurs decors propres a l'arc remplaceront automatiquement ces secours.
init -5 python:
    def arc7_jessy_bg(nom, secours):
        chemin = "images/scenes/arc_7/bg_arc7_jessy_{}.jpg".format(nom)
        if not renpy.loadable(chemin):
            chemin = secours
        return im.Scale(chemin, 1920, 1080)

image bg arc7 jessy boutique = arc7_jessy_bg("boutique", "images/scenes/arc_4/bg_arc4_shopping_gallery.jpg")
image bg arc7 jessy depart = arc7_jessy_bg("depart", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
image bg arc7 jessy route = arc7_jessy_bg("route", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
image bg arc7 jessy sentier = arc7_jessy_bg("sentier", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
image bg arc7 jessy sentier ours = im.Scale("images/scenes/arc_7/bg_arc7_jessy_sentier_ours.png", 1920, 1080)
image laplage bear neutral = speaker_sprite("laplage", "images/personnages/laplage/bear/Laplage_neutral.png")
image laplage bear thumb_up = speaker_sprite("laplage", "images/personnages/laplage/bear/Laplage_thumb_up.png")
image bg arc7 jessy riviere = arc7_jessy_bg("riviere", "images/scenes/prologue/bg_prologue_river_laplage.png")
image bg arc7 jessy fleurs = arc7_jessy_bg("fleurs", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
image bg arc7 jessy promontoire = arc7_jessy_bg("promontoire", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
# Diaporama de la scene 3 : personnages peints directement dans chaque CG.
image cg arc7 jessy marche = "images/scenes/arc_7/jessy_epopee/01_marche.jpg"
image cg arc7 jessy oiseau = "images/scenes/arc_7/jessy_epopee/02_oiseau.jpg"
image cg arc7 jessy renard = "images/scenes/arc_7/jessy_epopee/03_renard.jpg"
image cg arc7 jessy riviere main = "images/scenes/arc_7/jessy_epopee/04_riviere_main.jpg"
image cg arc7 jessy riviere chaussure = "images/scenes/arc_7/jessy_epopee/05_riviere_chaussure.jpg"
image cg arc7 jessy fleurs fruit = "images/scenes/arc_7/jessy_epopee/06_fleurs_fruit.jpg"
image cg arc7 jessy carte = "images/scenes/arc_7/jessy_epopee/07_carte.jpg"
image cg arc7 jessy gourde = "images/scenes/arc_7/jessy_epopee/08_gourde.jpg"
image cg arc7 jessy promontoire = "images/scenes/arc_7/jessy_epopee/09_promontoire.jpg"
image cg arc7 jessy fruit question = "images/scenes/arc_7/jessy_epopee/10_fruit_question.jpg"
image cg arc7 jessy fruit goute = "images/scenes/arc_7/jessy_epopee/11_fruit_goute.jpg"
image cg arc7 jessy dejeuner = "images/scenes/arc_7/jessy_epopee/13_dejeuner.jpg"
image cg arc7 jessy amitie = "images/scenes/arc_7/jessy_epopee/14_amitie.jpg"
image cg arc7 jessy aveu = "images/scenes/arc_7/jessy_epopee/15_aveu.jpg"
image bg arc7 jessy lac = im.Scale("images/scenes/arc_7/alexandre_fishing/alexandre_peche_lac_ponton_vide.jpg", 1920, 1080)
image cg arc7 alexandre peche dos = im.Scale("images/scenes/arc_7/alexandre_fishing/alexandre_peche_de_dos_au_lac.jpg", 1920, 1080)
image cg arc7 alexandre portrait yeux ouverts = im.Scale("images/scenes/arc_7/alexandre_fishing/alexandre_peche_portrait_yeux_ouverts.jpg", 1920, 1080)
image cg arc7 alexandre portrait yeux fermes = im.Scale("images/scenes/arc_7/alexandre_fishing/alexandre_peche_portrait_yeux_fermes.jpg", 1920, 1080)
image bg arc7 jessy bivouac = arc7_jessy_bg("bivouac", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
image bg arc7 jessy nuit = arc7_jessy_bg("nuit", "images/scenes/arc_7/bg_arc7_tokyo_park_night.jpg")
image bg arc7 jessy nuit tente ferme = im.Scale("images/scenes/arc_7/bg_arc7_jessy_nuit_tente_ferme.jpg", 1920, 1080)
image bg arc7 jessy belvedere = arc7_jessy_bg("belvedere", "images/scenes/arc_7/bg_arc7_tokyo_park_night.jpg")
image bg arc7 jessy cafe = arc7_jessy_bg("cafe", "images/scenes/arc_5/bg_arc5_cafe.jpg")
image bg arc7 jessy aube = arc7_jessy_bg("aube", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
image bg arc7 jessy minecraft = arc7_jessy_bg("minecraft", "images/scenes/arc_2/bg_arc2_minecraft_house_summer_night.jpg")

# CG de la contre-soiree de Sofiane : la descente de nuit et la rencontre avec Laplage.
image bg arc7 sofiane belvedere = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_belvedere_collegues.jpg", 1920, 1080)
image bg arc7 sofiane conduite collegues = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_conduite_collegues.jpg", 1920, 1080)
image bg arc7 sofiane route euphorie = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_route_nuit_collegues_euphorie.png", 1920, 1080)
image bg arc7 sofiane route sourire = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_route_nuit_collegues_sourire.jpg", 1920, 1080)
image bg arc7 sofiane conduite profil = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_conduite_profil.jpg", 1920, 1080)
image bg arc7 sofiane croisement laplage = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_croisement_laplage.jpg", 1920, 1080)
image bg arc7 sofiane croisement laplage pouce = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_croisement_laplage_pouce.jpg", 1920, 1080)

# CG epiques a generer : tant que le fichier manque, une image existante prend le relais.
init -5 python:
    def arc7_sofiane_cg(nom, secours):
        chemin = "images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_{}.jpg".format(nom)
        if not renpy.loadable(chemin):
            chemin = "images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_{}".format(secours)
        return im.Scale(chemin, 1920, 1080)

image bg arc7 sofiane phares = arc7_sofiane_cg("phares_depart", "belvedere_collegues.jpg")
image bg arc7 sofiane pedalier = arc7_sofiane_cg("pedalier_talon_pointe", "conduite_profil.jpg")
image bg arc7 sofiane epingles = arc7_sofiane_cg("epingles_vue_aerienne", "route_nuit_collegues_euphorie.png")
image bg arc7 sofiane epingles laplage = im.Scale("images/scenes/arc_7/sofiane_inital_d/sofiane_ae86_epingles_vue_aerienne_with_laplage.jpg", 1920, 1080)
image bg arc7 sofiane gobelet = arc7_sofiane_cg("gobelet_eau", "conduite_profil.jpg")
image bg arc7 sofiane retroviseur = arc7_sofiane_cg("retroviseur_phares", "conduite_profil.jpg")
image bg arc7 sofiane route vide = arc7_sofiane_cg("route_vide_fumee", "conduite_profil.jpg")

define audio.alex_peace = "audio/music/alex_peace.ogg"
define audio.spirit_of_the_night = "audio/music/spirit_of_the_night.ogg"
define audio.rando = "audio/music/rando.ogg" #peut etre changer
define audio.shopping = "audio/music/shopping.ogg"
define audio.randoNight = "audio/music/the-sunset.ogg"
define audio.barjazz = "audio/music/bar_jazzy.ogg"
define audio.morningLove = "audio/music/morning_romance.ogg" #changer

define audio.river = "audio/ambience/river.mp3"
define audio.lake = "audio/ambience/lake.mp3"
define audio.forestNight = "audio/ambience/forest_night.mp3"

define audio.deca = "audio/fx/Decathlons jingle.mp3"
define audio.bush = "audio/fx/bush.mp3"
define audio.bushbird = "audio/fx/bushbird.mp3"
define audio.map = "audio/fx/map.mp3"
define audio.shiny = "audio/fx/shiny.ogg"
define audio.plouf = "audio/fx/plouf.mp3"
define audio.softWind = "audio/fx/soft-wind.mp3"
define audio.yess = "audio/fx/yesss_1.mp3"
define audio.bear = "audio/fx/Bear.mp3"
define audio.engine = "audio/fx/AE86_engine.mp3"
define audio.drift = "audio/fx/drift.mp3"
define audio.engineStart = "audio/fx/AE86_engine_start.mp3"
define audio.puffpuff = "audio/fx/coins_fucking.mp3"
define audio.carStop = "audio/fx/car_stop.mp3"
define audio.sploush = "audio/fx/sploush.mp3"
define audio.carGo = "audio/fx/car_go.mp3"

# SCENE 1 - LE DEPART SE PREPARE
label arc_7_jessy:
    $ derniere_route = "Route Jessy"
    $ arc7_jessy_fruit = ""
    $ arc7_jessy_dejeuner = ""
    $ arc7_jessy_relation = ""
    $ arc7_jessy_tente = False
    $ arc7_jessy_family_epilogue = False
    scene black
    with fade
    centered "ARC 7 : LA RANDONNÉE"
    play music audio.mcnight loop volume 0.7 fadein 1.5
    scene bg arc7 jessy minecraft
    with fade
    show jessy minecraft at char_left
    show ilona minecraft at char_right
    with dissolve
    systeme "Quatre jours après les diplômes, Jessy et Ilona se connectent à leur maison Minecraft."
    if arc6_derniere_construction == "porte_ouverte":
        systeme "La porte inutile est restée ouverte. Aucun des deux ne l'a refermée."
    elif arc6_derniere_construction == "panneau_partir":
        systeme "Le panneau posé le soir des diplômes n'a pas bougé. Personne n'a eu besoin de le relire."
    elif arc6_derniere_construction == "cadenas":
        systeme "Le cadenas est toujours sur le coffre commun. La clé est dans l'inventaire d'Ilona."
    else:
        systeme "Rien n'a été posé depuis la dernière fois. Ils font le tour du jardin sans remplir le silence."
    i "Théo part le 6."
    j "Je sais."
    i "Il m'a envoyé l'heure de son train. Juste l'heure. Pas de message."
    j "Tu vas aller le voir à la gare avant qu'il parte ?"
    i "J'ai pas décidé."
    systeme "Jessy ouvre la bouche, puis la referme. Il pose une torche sur un mur qui n'en avait pas besoin."
    j "D'accord."
    i "C'est tout ?"
    j "C'est tout. Je mets des torches pour m'occuper les mains."
    i "Il y en a déjà quatre sur ce mur."
    j "C'est un mur très sombre."
    systeme "Elle rit. Il attend que le rire retombe pour parler, comme on attend qu'un creeper s'éloigne."
    j "Je pensais aller marcher en montagne cet été. Un vrai sentier. Pas un sommet héroïque. Juste de l'air et un endroit où dormir."
    j "Tu voudrais venir ? Tu peux répondre plus tard."
    i "C'est pas une contre-offre, hein ?"
    j "Non. Tokyo, c'est un studio, trois chaînes et un planning. Moi, j'ai un sentier et des sandwichs."
    i "Tant mieux. Je signerai rien."
    i "Oui. J'ai envie de venir."
    j "Ah. D'accord. Cool."
    j "Très cool. Je vais arrêter de dire cool."
    i "Il faudra des chaussures. De l'eau. Un truc pour dormir. Je sais pas ce qu'on met dans un sac de randonnée, en vrai."
    i "On pourrait aller acheter tout ça avec Allan, Alexandre et Sofiane ? Juste pour les courses. La marche, c'est nous deux."
    systeme "Jessy avait imaginé les préparatifs à deux, penchés sur une carte. L'image se replie. Il reste la plus importante : elle a dit oui à la marche."
    j "Bonne idée. Tu leur écris ?"
    i "C'est déjà fait."
    systeme "Sur l'écran du téléphone d'Ilona, le message est parti avant la fin de la phrase : {i}« Courses rando samedi. 14h. Venez. »{/i}"

    scene bg arc7 jessy boutique
    with fade
    play music audio.shopping loop volume 0.7 fadeout 1.0 fadein 2.0
    show allan beach smirk at char_left
    show alex winter neutral at char_midleft
    show sofiane beach neutral at char_center
    show ilona tokyo smile at char_midright
    show jessy beach neutral at char_right
    with dissolve
    systeme "Le samedi suivant, les cinq amis envahissent le rayon randonnée d'un magasin de sport."
    play sound audio.deca volume 0.6
    a "Vingt-deux mille yens. Pour un sac. Il y a un deuxième sac dedans ?"
    x "Il y a un dos ventilé et une répartition de charge sur les hanches."
    a "Mon sac de cours aussi avait une répartition de charge. Tout finissait au fond, sous les miettes."
    systeme "Alexandre soupèse chaque sac, tire sur les coutures, inspecte les boucles comme un ingénieur qui vérifie un pont."
    x "Celui-là a une couture qui lâchera au premier orage. Je ne dis pas ça pour te faire peur. Je le dis parce que c'est vrai."
    i "Donc pas celui-là."
    j "Essaie-le chargé. Ils mettent des sacs de sable au fond du rayon."
    i "Je sais. J'ai lu la pancarte."
    systeme "Ilona remplit le sac, ajuste les bretelles seule, fait trois allers-retours entre les chaussures et les tentes."
    i "Il tire pas sur les épaules. Je le prends."
    x "Validé. Il tiendra toute la randonnée. Même si Allan le remplit de biscuits."
    a "La couleur, par contre. Vous allez regarder ce vert kaki pendant deux jours."
    i "Je regarderai le chemin."
    a "Techniquement, le chemin sera aussi vert kaki."
    systeme "Allan glisse trois paquets de biscuits dans le panier. Ilona en repose deux. Il en remet un."
    i "Allan."
    a "Les provisions sont un équipement de sécurité. C'est écrit nulle part, mais c'est vrai."
    x "Vous avez vu la température la nuit, là-haut ? Ça descend vite après le coucher du soleil."
    i "Tente légère pour moi. Hamac pour Jessy. On a regardé la météo quatre fois."
    j "Cinq. J'ai regardé une fois de plus en cachette."
    a "Vous avez préparé une randonnée sans me consulter sur les sandwichs. Je suis blessé."
    i "On a prévu des sandwichs."
    a "Combien ?"
    i "Assez."
    a "Ce n'est pas un nombre."
    i "Au fait. Vous faites quoi, vous, cet été ?"
    j "Moi, ce week-end. Après, je verrai. C'est déjà beaucoup de projet pour moi."
    x "Rien de prévu. Je veux voir ce que ça fait, un été qui n'a pas de programme."
    a "Me promener. Et peut-être aller voir Théo à Tokyo, si on trouve une date qui nous va à tous les deux."
    systeme "Le nom passe dans le rayon sans que personne ne s'arrête dessus. Ilona hoche la tête."
    i "Ça te ferait du bien de le voir."
    a "Oui. On s'est quittés sur un accrochage au gymnase. J'aimerais que ce soit pas la version définitive."
    s "Moi, je n'ai pas de programme non plus."
    s "Je prendrai la voiture de mon cousin. Je trouverai une route de montagne que je ne connais pas. Je m'arrêterai dans un café au bord de cette route."
    j "Sofiane. C'est littéralement un programme."
    s "C'est une direction. Un programme, ça a des horaires."
    i "Pour être claire : la randonnée, c'est Jessy et moi. Je suis contente que vous soyez là aujourd'hui."
    i "Sofiane, tu pourrais nous déposer au départ du sentier ?"
    s "Oui. Je vous dépose. Ensuite, la montagne est à vous."
    a "Attends. C'est la virée en montagne que tu nous promets depuis l'hiver ?"
    s "La route, je l'ai promise en hiver. La marche, c'est la leur. Ce ne sont pas les mêmes promesses."
    a "Tu te rends compte que tu parles comme une bande-annonce ?"
    s "... Je confirme la date avec mon cousin ce soir."
    systeme "Ils fixent le premier week-end libre de l'été. Juin passe en révisions de permis, en petits boulots, en soirées Minecraft. Le départ approche."
    jump arc_7_jessy_scene_2

# SCENE 2 - L'AUBE DU VOYAGE
label arc_7_jessy_scene_2:
    play music audio.morningLove loop volume 0.7 fadein 2.0 fadeout 1.0
    scene bg arc7 jessy depart
    with fade
    show jessy rando bag neutral at char_left
    show ilona rando bag smile at char_right
    with dissolve
    systeme "Samedi, sept heures. L'été est bien là : il fait déjà chaud, et les cigales ont commencé avant tout le monde."
    systeme "Jessy et Ilona attendent au point de rendez-vous, sacs sur le dos. La rosée assombrit encore le bord du trottoir."
    i "T'as dormi ?"
    j "Assez pour ne pas confondre la carte avec mon oreiller. Et toi ?"
    i "J'ai vérifié trois fois que j'avais la gourde. Puis je l'ai posée à côté du sac pour être sûre de la voir."
    j "Elle est où, là ?"
    i "Dans le sac. J'ai vérifié une quatrième fois."
    systeme "Elle sort un pain au lait de sa poche et mord dedans. Quelque chose commence : Ilona mange."
    play sound audio.carStop volume 0.6
    systeme "Au bout de la rue, un moteur monte dans les tours. Grave, régulier, bien trop fort pour sept heures du matin."
    show sofiane beach neutral at char_center
    with dissolve
    systeme "Une AE86 blanche et noire s'arrête devant eux. Elle brille comme si elle sortait d'un catalogue. Sofiane descend avec la gravité d'un pilote sur la grille de départ."
    j "Tu l'as vraiment eue."
    s "Mon cousin me l'a laissée. Il m'a dit une seule chose en partant."
    i "Quoi ?"
    s "« Ne la déçois pas. »"
    j "Il parlait de la voiture ?"
    s "Je n'ai pas osé demander."
    i "Tu l'as lavée jusqu'aux rétroviseurs ?"
    s "Jusqu'aux rétroviseurs. Et les rétroviseurs aussi."
    j "On monte, ou on doit d'abord passer un examen de conduite ?"
    s "Montez. Ne touchez à aucun réglage."
    i "Elle est plus propre que nos chaussures."
    s "Je vous fais confiance pour ne pas inverser les priorités."
    systeme "Ilona glisse son sac dans le coffre. Jessy cale le sien à côté, la carte coincée dans la poche du haut."
    scene bg arc7 jessy route
    with fade
    systeme "La ville recule dans le rétroviseur. Puis les zones commerciales. Puis les derniers ronds-points."
    systeme "Sofiane conduit à deux mains, le dos droit. Il ne parle presque pas. À chaque virage, un coin de sa bouche bouge."
    i "Tu souris."
    s "Non."
    i "Tu souris depuis le troisième virage."
    s "... J'attends cette route depuis l'hiver. Depuis avant, peut-être."
    j "Et tu comptes respecter les virages ?"
    s "Je les respecte. C'est pour ça que je les regarde autant."
    systeme "La route monte. Les arbres se resserrent, puis s'ouvrent sur une vallée qu'aucun d'eux n'avait jamais vue."
    i "La ville a l'air loin, déjà."
    j "C'est un peu pour ça que j'ai proposé. Pour que ce soit assez loin pour entendre ce qu'on pense."
    i "Et si on pense rien ?"
    j "Alors on marchera. C'est bien aussi."
    scene bg arc7 jessy sentier
    with fade
    show sofiane beach neutral at char_left
    show ilona rando neutral at char_midright
    show jessy rando neutral at char_right
    with dissolve
    systeme "Au départ des sentiers, Sofiane sort les sacs du coffre et les pose sur l'herbe comme on remet une épée."
    i "Et toi, tu fais quoi pendant qu'on marche ?"
    s "Je marche un peu. Je redescends. Ce soir, je ramène deux collègues du maid café avant leur service."
    if arc4_5_sofiane_maid:
        j "Toujours le maid café."
        s "Ne le dis pas trop fort. Les arbres ont des oreilles."
    else:
        i "Attends. Tes collègues du quoi ?"
        s "Du maid café."
        j "Depuis quand tu travailles dans un maid café ?"
        s "Depuis assez longtemps pour dessiner un cœur au ketchup sans trembler."
        i "... On a énormément de questions."
        s "Gardez-les pour la descente. Ça fait passer les lacets."
    i "Merci d'avoir fait toute cette route pour nous."
    s "Ce n'est pas pour vous. Enfin. Pas seulement."
    s "Marchez à votre rythme. La montagne n'a pas de chronomètre."
    play sound audio.engineStart volume 0.6
    systeme "Il remonte dans la voiture. Le moteur répond au premier tour de clé. Le bruit s'éloigne dans les lacets, puis il n'y a plus que le vent."
    hide sofiane
    with dissolve
    systeme "Devant eux, deux sentiers partent entre les arbres. Jessy sort de sa poche une feuille pliée en huit."
    i "C'est quoi ?"
    j "Trois itinéraires. Une variante en cas de pluie. Et une variante de la variante."
    i "Jessy."
    j "Je sais. Je suis pas très bon sans plan."
    i "On choisit au fur et à mesure. Si je veux faire demi-tour, je le dis. Si toi tu veux faire demi-tour, tu le dis aussi."
    j "Je le dirai pas."
    i "Je sais. Je surveillerai tes mollets."
    j "... Lequel te tente ?"
    i "Celui-là. Il monte doucement, sous les arbres."
    j "J'y pensais depuis des jours, tu sais. À ce week-end. J'ai mis longtemps avant d'oser t'en parler."
    i "T'as fini par le faire. Et je suis là."
    i "Et je suis contente d'être là."
    systeme "Elle part la première. Il range la feuille pliée en huit. Il ne la ressortira pas."
    show ilona rando bag neutral at char_midright
    show jessy rando bag neutral at char_right
    with dissolve
    jump arc_7_jessy_scene_3

# SCENE 3 - L'EPAPOPE DE LA JAJ
label arc_7_jessy_scene_3:
    stop music fadeout 1.0
    scene black
    with fade
    play ambiant1 audio.windBirds loop volume 0.4
    systeme "Il est des légendes que les montagnes se racontent entre elles, quand le vent tombe."
    systeme "Celle de deux voyageurs partis sans carrosse ni armée, avec un sac vert kaki, un hamac et trop de biscuits."
    systeme "Devant eux : des rivières sans pont, des bêtes sans nom, des fruits que nul n'a goûtés, et une carte que l'un d'eux tenait à l'envers."
    systeme "On sait seulement comment leur marche commença."
    play music audio.rando loop volume 0.7 fadein 1.5
    scene cg arc7 jessy marche
    with fade
    systeme "Et l'épapopé de la jaj commença."
    play sound audio.bushbird volume 0.5
    scene cg arc7 jessy oiseau
    with dissolve
    systeme "Un oiseau jaillit du fossé. Jessy recule d'un pas. Ilona ne bouge pas."
    i "C'était un oiseau."
    j "Je sais. Je lui ai laissé la priorité."
    scene cg arc7 jessy renard
    play sound audio.bush volume 0.5
    with dissolve
    systeme "Plus loin, quelque chose de roux traverse le sentier et s'arrête pour les regarder. Ils s'arrêtent aussi. Personne ne bouge. L'animal décide que ce n'est pas son problème et disparaît dans les fougères."
    i "Il nous a jugés."
    j "Il nous a trouvés inoffensifs. C'est vexant."
    scene cg arc7 jessy riviere main
    play ambiant1 audio.river loop volume 0.4
    with dissolve
    systeme "Une rivière coupe le chemin. Ilona observe les pierres, en choisit trois, traverse sans se mouiller. Sur l'autre rive, elle tend la main."
    i "Tu veux la main ?"
    j "J'avais prévu de prétendre que j'avais pas besoin d'aide."
    j "... Mais oui."
    scene cg arc7 jessy riviere chaussure
    with dissolve
    play sound audio.sploush volume 0.6
    systeme "Il prend sa main. La troisième pierre bouge quand même. Sa chaussure plonge dans l'eau ; il rejoint la berge avec toute sa dignité, ou presque."
    scene cg arc7 jessy fleurs fruit
    with dissolve
    play sound audio.shiny volume 0.4
    play ambiant1 audio.windBirds loop volume 0.4
    systeme "Un champ de fleurs ondule jusqu'à la crête. Au bord du sentier, Ilona s'accroupit et ramasse un petit fruit en forme d'étoile, jaune pâle, presque lumineux."
    i "Regarde."
    j "Ça, c'est un loot rare. Ravitaillement légendaire. Aucune chance de drop."
    i "Je déciderai au prochain arrêt si ça se mange."
    play sound audio.map volume 0.5
    scene cg arc7 jessy carte
    with dissolve
    systeme "Dans la montée, Jessy déplie la carte. Il la contemple longtemps. Ilona se penche, la tourne d'un demi-tour sans rien dire, et pose le doigt sur le nord."
    j "... Elle était déjà comme ça quand je l'ai achetée."
    i "Je sais."
    scene cg arc7 jessy gourde
    with dissolve
    systeme "Ilona boit à la gourde, puis la tend à Jessy sans essuyer le goulot. Il le remarque. Il ne dit rien. Il la prend quand même."
    systeme "Quand la pente s'adoucit, Ilona s'arrête."
    i "À toi. Le prochain arrêt."
    j "Là-haut. Le rocher plat."
    i "Parfait. Et on mange avant de repartir. C'est pas négociable."
    scene cg arc7 jessy promontoire
    with fade
    systeme "Début d'après-midi. Ils posent les sacs sur un promontoire. En dessous, la vallée entière, les routes en fil, un village grand comme une maison Minecraft vue de haut."
    j "On a fait tout ça avec la carte à l'envers ?"
    i "La moitié. L'autre moitié, c'est mes chaussures."
    j "Et la rivière où tu m'as sauvé la vie."
    i "Elle faisait trois pas de large."
    j "Trois pas très hostiles."
    scene cg arc7 jessy fruit question
    with dissolve
    play sound audio.shiny volume 0.4
    systeme "Ilona sort le fruit étoilé et le fait tourner au soleil. Sa peau luit doucement. Aucun d'eux ne sait ce que c'est."
    i "Il est beau. Je sais pas s'il est comestible."
    menu:
        "Que fait Ilona de sa trouvaille ?"
        "La laisser goûter.":
            $ arc7_jessy_fruit = "goute"
            $ ilonanium_points += 1
            i "Tant pis. Je tente."
            scene cg arc7 jessy fruit goute
            with dissolve
            play sound audio.eating volume 0.6
            systeme "Elle croque. Sucré d'abord, puis acide, puis quelque chose qui n'a pas de nom. Elle ferme les yeux."
            i "J'ai peut-être mangé un astre."
            j "Encore ?"
            systeme "Elle garde le noyau, en forme d'étoile lui aussi, et le glisse dans la poche de son sac."
        "Le laisser à la montagne.":
            $ arc7_jessy_fruit = "jette"
            i "Non. Je joue pas aux devinettes avec un fruit sauvage."
            scene cg arc7 jessy promontoire
            with dissolve
            systeme "Elle le pose sur le rocher, face à la vallée, comme une offrande à quelqu'un qui passerait après eux."
            j "Quelqu'un va le trouver et vivre une aventure incroyable."
            i "Ou un écureuil va mourir."
    scene cg arc7 jessy dejeuner
    with dissolve
    systeme "Ils mangent les sandwichs. Assez de sandwichs. Allan aurait dit que ce n'est pas un nombre."
    i "Après le lycée, j'ai envie d'essayer des trucs. Plein. Sans savoir où ils mènent."
    i "Le stream. Un job nul. Un voyage. Me tromper un peu. C'est bizarre de pas avoir de plan ?"
    j "Moi j'ai que des plans. Tu as vu ma feuille pliée en huit."
    j "Je crois que je veux continuer à construire des trucs. Avec les gens qui comptent. Même quand je sais pas encore à quoi ils servent."
    i "Comme la porte inutile."
    j "Comme la porte inutile."
    systeme "Ilona regarde la vallée. Puis elle le regarde, lui."
    i "Et nous ? Tu espères quoi, pour nous, après l'été ?"
    menu:
        "Que dit Jessy de leur lien ?"
        "Dire qu'il tient à leur amitié.":
            $ arc7_jessy_dejeuner = "amitie"
            j "Que ça continue. Les soirées Minecraft, les trucs débiles, toi qui me tournes la carte dans le bon sens."
            j "Je tiens à ce qu'on a. Même si ça reste exactement ça."
            i "Moi aussi, je veux garder ça."
            scene cg arc7 jessy amitie
            with dissolve
            systeme "Elle le dit simplement. Puis elle mord dans un biscuit d'Allan et regarde longtemps la vallée."
        "Lui avouer ce qu'il ressent.":
            $ arc7_jessy_dejeuner = "crush"
            j "J'avais préparé une phrase. Avec une métaphore de construction. Elle était très bien."
            j "Je l'ai oubliée. Alors, sans métaphore : tu me plais. Pas depuis hier."
            scene cg arc7 jessy aveu
            with dissolve
            j "T'as pas à répondre maintenant. Je voulais juste arrêter de le cacher derrière des torches."
            systeme "Ilona ne répond pas tout de suite. Elle repose son biscuit. Ses joues ont pris une couleur qui n'a rien à voir avec le soleil."
            i "Merci de me le dire. Vraiment."
            i "Je veux te répondre bien, pas vite. Tu me laisses la journée ?"
            j "Prends la journée. Prends la montagne entière s'il faut."
            i "La journée, ça suffira."
    scene cg arc7 jessy promontoire
    with dissolve
    systeme "Rien n'est promis sur ce rocher. Rien n'est fermé non plus."
    i "On descend vers le lac ?"
    j "Après toi. Cette fois, je tiens la carte dans le bon sens."
    i "Tu la tiens à l'envers."
    j "... Après toi."
    jump arc_7_jessy_scene_4

# SCENE 4 - A LA CROISEE DES CHEMINS
label arc_7_jessy_scene_4:
    scene bg arc7 jessy sentier ours
    with fade
    play ambiant1 audio.windBirds loop volume 0.45
    show jessy rando bag neutral at char_left
    show ilona rando bag neutral at char_right
    with dissolve
    systeme "Une heure de marche plus tard, à un embranchement, des pas lourds font trembler les feuilles. Jessy tire Ilona derrière un rocher. Elle se dégage, puis se cache quand même."
    show jessy rando bag embarrassed at char_left
    show ilona rando bag embarrassed at char_right
    $ renpy.pause(0.5, hard=True)
    play sound audio.laplage volume 0.6
    show laplage bear neutral at char_center
    with dissolve
    play sound audio.bear volume 0.6
    systeme "Un ours sort des arbres, paisible, énorme. Sur son dos, jambes croisées, torse nu, Monsieur Laplage."
    systeme "L'ours s'arrête pour renifler un buisson."
    i "Monsieur Laplage ?"
    j "Vous êtes... sur un ours."
    laplage "J'avais besoin d'un raccourci. Il connaît la région."
    i "Et il a accepté ?"
    laplage "Certaines rencontres n'ont pas besoin d'être expliquées."
    j "Vous saviez qu'on serait là ?"
    play sound audio.bear volume 0.6
    laplage "Moi, non. C'est l'ours qui a choisi le chemin."
    systeme "L'ours relève la tête et les regarde. Jessy décide de ne plus faire aucun mouvement de sa vie."
    i "Vous avez l'air content."
    laplage "Je suis sur un ours. Je suis content en général."
    laplage "Et vous deux. Vous avez hésité. Vous vous êtes trompés. Vous avez appris à vous écouter. C'est long, chez les humains."
    j "Donc on est sur le bon chemin ?"
    laplage "Cette partie-là vous appartient encore."
    systeme "L'ours éternue dans le buisson. Une pluie de pétales retombe sur Laplage, qui ne cille pas."
    show laplage bear thumb_up at char_center
    play sound audio.bear volume 0.6
    systeme "Il lève le pouce. L'ours repart. Ils disparaissent entre les arbres sans se retourner."
    hide laplage
    with dissolve
    j "On en parle ?"
    i "Non."
    j "D'accord. On en parle jamais."

    stop ambiant1 fadeout 1.0
    stop music fadeout 2.0
    scene black
    with fade
    systeme "Quarante-cinq minutes de marche plus tard..."
    scene bg arc7 jessy lac
    with fade
    play ambiant1 audio.lake volume 0.4 loop fadein 2.0
    systeme "Jessy et Ilona découvrent un lac immense, lové entre les montagnes. L'eau claire reflète les sommets ; un ponton de bois s'avance dans ce calme presque irréel. Une canne à pêche et un panier attendent au bord de l'eau."
    show cg arc7 alexandre peche dos
    with dissolve
    play music audio.alex_peace volume 0.7 loop fadein 2.0
    play sound audio.plouf volume 0.6
    i "... Alexandre ?"
    j "Qu'est-ce que tu fais là ? Depuis quand tu pêches ?"
    x "Depuis ce matin. Je sais pas encore si j'aime ça."
    x "Mes grands-parents habitent de l'autre côté du lac. J'ai emprunté la canne de mon grand-père. Il m'a dit que j'avais la patience d'un moustique."
    i "T'as jamais parlé de tes grands-parents."
    x "Vous avez jamais demandé. Moi non plus, remarque. Asseyez-vous."
    systeme "Ils posent leurs sacs près du ponton et s'installent. Le flotteur reste immobile. Les montagnes se reflètent à l'envers dans l'eau, comme sur la carte de Jessy."
    show jessy rando neutral at char_left
    show ilona rando neutral at char_right
    with dissolve
    j "T'as attrapé quelque chose ?"
    x "Rien. Pas une touche."
    play sound audio.softWind volume 1.0
    systeme "Alexandre laisse son regard suivre les crêtes. Il ferme les yeux un instant. Le vent passe sur le lac."
    scene cg arc7 alexandre portrait yeux fermes
    with Dissolve(1.0)
    $ renpy.pause(0.8, hard=True)
    scene cg arc7 alexandre portrait yeux ouverts
    with Dissolve(1.0)
    systeme "Quand il les rouvre, son sourire est paisible."
    x "N'est-ce pas magnifique ?"
    j "Tu as rien attrapé de la journée."
    x "J'ai appris que la patience garantit rien. Le paysage, lui, a tenu sa promesse dès la première minute."
    scene cg arc7 alexandre peche dos
    with Dissolve(1.0)
    show jessy rando neutral at char_left
    show ilona rando neutral at char_right
    with dissolve
    x "Je pensais à des trucs, avant de vous voir arriver au bord de l'eau."
    x "Le château de sable, cet été. Tu voulais une cuisine dedans. Un château de sable avec une cuisine."
    x "La porte inutile, au festival. {i}« Porte en réflexion. »{/i} Tu l'as défendue vingt minutes."
    x "Et ta miniature, à Noël. Je t'ai demandé si c'était un souvenir ou une réponse."
    j "Je m'en souviens."
    x "Moi, j'ai passé l'année à chercher à quoi servaient les choses. La cuisine, la porte, la miniature. Il fallait que tout ait une fonction."
    x "Et au final, ce que je garde, c'est les trucs absurdes. Et les fois où on s'est parlé pour de vrai."
    x "On peut laisser un moment compter avant de savoir comment l'appeler. Je crois. Je suis pas sûr. Une journée entière à pêcher, ça fait réfléchir."
    play sound audio.plouf volume 0.6
    systeme "Le flotteur s'enfonce. Alexandre se redresse et mouline, sérieux comme un chirurgien."
    systeme "Au bout de la ligne : une feuille."
    scene cg arc7 alexandre portrait yeux ouverts
    with Dissolve(0.8)
    x "Une nouvelle espèce de poisson. Très plate."
    i "Tu vas la relâcher ?"
    x "Quand j'aurai fini de l'étudier. C'est une découverte scientifique majeure."
    j "Tu vas lui donner un nom ?"
    x "Pas encore. Je la laisse compter d'abord."
    scene cg arc7 alexandre peche dos
    with Dissolve(0.8)
    show jessy rando neutral at char_left
    show ilona rando smile at char_right
    with dissolve
    systeme "Ilona rit si fort que l'écho revient du lac. Ils restent encore un moment, pour rien. C'est le but."
    i "Merci, Alexandre. On avait besoin de s'arrêter, je crois."
    j "Content de t'avoir croisé. Même au milieu de nulle part."
    x "Surtout au milieu de nulle part. Vous me raconterez la suite. Pas tout. Juste la suite."
    i "Promis."
    x "Bonne route."
    systeme "Ils récupèrent leurs sacs et quittent la rive. Derrière eux, Alexandre est de nouveau tourné vers le lac, la feuille posée à côté de lui comme un trophée."
    jump arc_7_jessy_scene_5

# SCENE 5 - AU CREPUSCULE DE L'AVENTURE
label arc_7_jessy_scene_5:
    play music audio.randoNight loop volume 0.7 fadeout 1.0 fadein 2.0
    play ambiant1 audio.forestNight loop volume 0.4 fadein 2.0
    scene bg arc7 jessy bivouac
    with fade
    
    show jessy rando smile at char_left
    show ilona rando smile at char_right
    with dissolve
    systeme "Une heure plus tard, le soleil passe derrière les crêtes. Dans une clairière à l'abri du vent, la tente et le hamac sont prêts pour la nuit."
    j "Bilan de la journée : un ours avec Monsieur Laplage dessus, un pêcheur de feuilles."
    i "Tu oublies la carte à l'envers."
    j "J'ai dit bilan, pas procès."
    j "Et le meilleur moment, c'était quoi ?"
    i "Quand t'as accepté ma main, à la rivière."
    j "J'ai surtout demandé à ma chaussure de rester sèche. Elle m'a pas écouté."
    i "Ta chaussure, je m'en fiche. Tu m'as demandé de l'aide."
    systeme "Jessy ouvre la bouche pour plaisanter, puis la referme. La lampe balance doucement entre les pins."
    j "J'ai cru que tu allais me laisser traverser tout seul."
    i "Je t'ai tendu la main. J'attendais que tu décides de la prendre."
    systeme "Ilona s'assoit sur son sac. Elle regarde le ciel virer au violet."
    i "J'aimerais que l'été dure. Pas pour toujours. Juste un peu plus que prévu."
    j "J'ai eu le même réflexe à la fin du lycée. Si on restait assez longtemps dans la salle, personne serait obligé de sortir."
    i "Moi, je voulais sortir. J'avais juste peur de laisser les bonnes choses à l'intérieur."
    i "Tu imagines quoi, quand on rentrera ?"
    if arc7_jessy_dejeuner == "crush":
        j "Je repense à ce que je t'ai dit à midi. J'avais peur de l'avoir lâché là-haut et de te forcer à le porter tout l'après-midi."
        i "Je l'ai porté. Mais tu m'as pas demandé de le porter pour toi. C'est différent."
        j "Tu me plais toujours. Et je veux entendre ce que toi tu veux, même si c'est pas ce que j'espère."
        i "Ta phrase de midi, elle a marché avec moi tout l'après-midi. Elle a pris toute la place dans le sac."
        i "Par moments je voulais te répondre tout de suite. Et puis je me rappelais que j'avais demandé jusqu'à ce soir."
        j "Pour une fois, j'ai réussi à pas te demander toutes les dix minutes."
        i "J'ai remarqué."
    else:
        j "Qu'on se voie encore. Que ça devienne pas un truc qu'on raconte plus tard en disant : on était proches, à l'époque."
        j "À midi, j'ai parlé d'amitié parce que je sais ce que je veux garder. Je veux pas que ça ressemble à une limite que je t'impose."
        i "Moi aussi, j'y tiens. C'est pour ça que j'ai pas voulu répondre à midi avec le premier mot qui me venait."
        i "Depuis ce matin, je me pose une question. Et plus je marche, moins elle part."
        if arc5_cinema_ensemble:
            i "En vrai, elle date pas de ce matin. Elle date du cinéma. De ta main, que t'as pas retirée."
        elif arc4_cadeau_jessy == "miniature_aveu":
            i "En vrai, elle date pas de ce matin. Elle date de ta miniature, à Noël. Elle ressemblait pas à un souvenir."
        else:
            i "En vrai, elle date pas de ce matin. Elle date de cette année. De toutes les fois où tu m'as écoutée jusqu'au bout."
        j "Tu peux me la poser. Même si j'ai pas de réponse toute faite."
        i "C'est justement pour ça que j'attends encore un peu."
    systeme "Jessy vérifie les sangles du hamac. Ilona retend un coin de la tente ; ils ajustent ensemble la corde de la lampe."
    j "Toi, t'as une petite maison portative. Moi, deux sangles et beaucoup d'optimisme."
    i "Si ton optimisme lâche, la maison a une deuxième place."
    j "Je vais éviter de tester avant la nuit."
    i "J'ai pas dit que je voulais te voir tomber."
    systeme "La phrase reste entre eux. Ilona tire encore sur un piquet déjà bien planté."
    i "Quand tu m'as proposé cette marche, j'ai cru que tu avais choisi une façon plus jolie de me demander de rester."
    j "Je sais. J'ai failli te dire que c'était pas ça. Mais j'aurais menti un peu. J'avais envie de te voir, aussi."
    i "J'avais peur qu'en disant oui au sentier, je dise oui à tout le reste sans le savoir."
    j "Et aujourd'hui ?"
    i "Aujourd'hui, je sais que j'ai choisi le sentier. Je sais aussi que j'ai cherché ta main sur les pierres. Les deux sont vrais."
    j "À la rivière, je pensais que si je prenais ta main, tu allais croire que j'avais déjà décidé ce qu'on était."
    i "Moi, j'ai pensé que tu allais tomber à l'eau."
    j "C'est arrivé aussi."
    systeme "Ils rient, mais Ilona ne lâche pas le piquet. Jessy s'accroupit près d'elle sans y toucher."
    i "Tu sais ce qui m'a fait peur cette année ? Pas que tu tiennes à moi. Que parfois tu savais déjà ce que j'allais dire avant que j'ouvre la bouche."
    j "Je croyais t'aider. Je préparais des réponses pour nous deux et j'appelais ça faire attention."
    i "Et moi, je raccourcissais mes phrases pour pas te décevoir."
    j "Je suis désolé. Pas pour que tu me dises que c'est réglé. Je sais que ça se règle pas avec une randonnée."
    i "Non. Mais aujourd'hui, quand j'ai mis du temps à trouver mes mots, tu m'as laissée respirer. Même si ça te faisait peur."
    j "Terriblement. J'ai fait semblant de m'intéresser à la pêche pour pas te regarder toutes les secondes."
    i "Alexandre s'intéressait davantage à sa feuille que toi à la pêche."
    systeme "Le froid descend d'un coup. Jessy cherche un pull dans son sac. Ilona regarde le col de sa chemise de randonnée. Rien d'écrit dessous."
    show jessy rando neutral at char_left
    show ilona rando neutral at char_right
    i "Ta veste des diplômes. Tu l'as gardée ?"
    j "Dans mon placard. Sur un cintre. Je l'ai pas lavée."
    i "Pourquoi ?"
    j "À cause du col."
    systeme "Les trois mots au feutre sont là-bas, dans le placard, loin de la montagne. Ils sont quand même un peu là ce soir."
    i "Tu les as lus. Le soir même ?"
    j "Le soir même. Plusieurs fois."
    i "Tu m'as jamais rien dit."
    j "Je savais pas quoi construire avec."
    i "C'était pas un plan de construction, Jessy. C'était des mots."
    j "Je sais. Je cherchais ce que j'avais le droit d'en faire sans te demander."
    i "Tu pouvais me demander. J'aurais peut-être dit que je savais pas encore."
    j "J'avais peur de ce 'pas encore'. Je le transformais en promesse dès que j'y pensais."
    i "Et moi, je croyais t'avoir écrit quelque chose de clair. C'était pas une promesse. C'était une manière de pas partir sans rien dire."
    systeme "Jessy cesse de fouiller dans son sac. Ilona relâche enfin le piquet."
    j "Tu sais, j'ai gardé aussi la veste parce que c'est toi qui as écrit dessus. Même si j'avais jamais compris ces mots, ça aurait compté."
    i "Ça, j'aurais aimé l'entendre plus tôt."
    j "Je te le dis maintenant. Et j'aimerais qu'on continue à se dire les choses même quand c'est maladroit."
    i "Moi aussi. Mais là, si on reste devant la tente, je vais finir par dire un truc juste pour remplir le silence."
    systeme "La nuit tombe tout à fait. Ils se souhaitent bonne nuit. Ilona va jusqu'à sa tente, pose la main sur la fermeture éclair, et s'arrête."
    show ilona rando embarrassed at char_right
    with dissolve
    systeme "Elle ouvre le paquet de biscuits d'Allan. En mange un. Pour gagner quelques secondes."
    i "Jessy. Je veux pas redescendre demain en faisant comme si rien avait changé."
    if arc7_jessy_dejeuner == "crush":
        i "À midi, je t'ai demandé la journée. Je l'ai eue. J'ai eu le temps de sentir ce que ça me faisait, ta phrase."
    else:
        i "Ma question. J'ai eu onze kilomètres pour y répondre. Et une soirée à t'écouter sans qu'on fasse semblant."
    i "J'avais peur de te le dire parce que je voulais pas que notre maison, nos soirées, même cette marche deviennent les preuves d'un truc que je te devais."
    i "Mais quand tu m'as pris la main à la rivière, j'ai pas pensé au passé. J'ai eu envie qu'on trouve un autre chemin ensemble."
    i "Je suis amoureuse de toi. J'aimerais essayer. Nous deux. Pour de vrai."
    i "Et dis pas oui pour me faire plaisir. Si c'est non, je préfère un vrai non."
    systeme "Jessy la regarde. Elle attend, sans toucher à la fermeture éclair. Pour une fois, aucune carte ne peut lui souffler la réponse."
    menu:
        "Que répond Jessy ?"
        "Il tient à elle, mais veut rester son ami.":
            $ arc7_jessy_relation = "amitie"
            show jessy rando listening at char_left
            with dissolve
            systeme "Jessy cherche une blague. Il en trouve trois. Il les laisse toutes dans sa poche."
            j "Tu comptes énormément. Et je sais que ça ne rendra pas ma réponse moins douloureuse."
            if arc7_jessy_dejeuner == "crush":
                j "À midi, je t'ai dit que tu me plaisais. C'était vrai. Mais je me rends compte que j'ai parlé avant de savoir ce que je pouvais t'offrir."
                j "Je t'ai laissé croire que j'attendais la même chose que toi. Je suis désolé."
            else:
                j "Quand j'ai parlé d'amitié à midi, c'était pas une façon de me protéger en attendant que tu fasses le premier pas. Je le pensais."
            j "Je suis pas amoureux de toi comme tu l'es de moi. Si je disais oui ce soir, tu le sentirais demain matin."
            show ilona rando sad at char_right
            with dissolve
            systeme "Ilona hoche la tête trop vite. Elle émiette le biscuit entre ses doigts avant de s'en rendre compte."
            i "J'avais demandé un vrai non. Je pensais pas que ça ferait aussi mal d'en avoir un."
            j "Je sais pas quoi te dire pour que ça fasse moins mal."
            i "Rien. Surtout pas que ça va redevenir comme avant. Je pourrai pas faire ça demain."
            j "Je te le demanderai pas. Et j'essaierai pas de réparer ça en étant partout autour de toi."
            i "Merci. J'ai besoin de savoir que tu vas pas transformer ma peine en problème à résoudre."
            j "Tu me dois rien. Même pas de me dire que ça va."
            i "Ça va pas, là. Mais ça ira. J'aurai besoin de temps. Je sais pas combien."
            systeme "Ils restent côte à côte une seconde encore, sans trouver de geste qui ne promette pas autre chose."
            systeme "Elle entre dans la tente. La fermeture éclair descend lentement."
            systeme "Jessy s'allonge dans son hamac. Il reste éveillé longtemps, les yeux dans les branches. Il ne reprend pas sa réponse. Ça fait mal quand même."
        "Il l'aime aussi et veut essayer.":
            $ arc7_jessy_relation = "amour"
            show jessy rando determined at char_left
            with dissolve
            systeme "Jessy cherche une métaphore Minecraft. Il n'en trouve aucune d'assez bien. Tant mieux."
            j "Moi aussi. Je suis amoureux de toi. Depuis assez longtemps pour avoir oublié ce que je faisais avant de regarder si tu étais connectée."
            j "Quand tu m'as dit oui pour la randonnée, j'ai passé une heure à sourire devant mon écran. Et ensuite j'ai eu peur d'avoir encore décidé à ta place ce que ce oui voulait dire."
            i "J'ai choisi la randonnée. Je suis aussi en train de te choisir, là. C'est pas le même oui."
            j "Je sais. C'est pour ça que je veux pas répondre avec un plan pour nous deux. J'ai envie d'essayer avec toi, même si on sait pas encore à quoi ça ressemblera."
            i "Tu sais que je vais te reprendre quand tu finiras mes phrases ?"
            j "J'espère. Et je vais probablement me tromper encore. Mais je veux apprendre à t'écouter quand tu me le dis, pas attendre que tu te taises."
            systeme "Ilona lâche la fermeture éclair. Jessy n'avance pas ; il attend qu'elle l'invite à s'approcher."
            i "Alors approche. Mais une étape à la fois."
            j "Ça, je peux essayer."
            systeme "Ils s'embrassent. D'abord maladroitement, le nez au mauvais endroit. Puis avec le soulagement de ne plus avoir à deviner."
            systeme "Ils se séparent. Se regardent. Rient, parce qu'il n'y a rien d'autre à faire."
            show jessy rando smile at char_left
            show ilona rando smile at char_right
            i "Tu... voudrais dormir dans ma tente ?"
            j "Attends. Tu parles d'un Puff-Puff ?"
            systeme "Quelque part dans la tête de Jessy démarre la musique des soirées Minecraft du confinement. Celle qu'il n'a jamais su éteindre."
            show ilona rando embarrassed at char_right
            i "Je parlais de dormir. D'abord."
            i "Pour le reste... on peut en parler. Si tu veux."
            $fade_channel("music",0.4,1.0)
            play sound audio.yess volume 0.6
            menu:
                "Que préfère Jessy pour cette nuit ?"
                "Garder son hamac et prendre leur temps.":
                    $fade_channel("music",0.7,1.0)
                    j "J'ai envie d'être avec toi. Et ce soir, je crois que j'ai surtout envie de pas aller trop vite."
                    j "Le hamac et moi, on a des choses à régler."
                    i "Ça me va. On a tout l'été."
                    systeme "Elle l'embrasse encore, plus doucement. Puis chacun rejoint son couchage, sans se lâcher des yeux jusqu'à la dernière seconde."
                "Rejoindre Ilona dans la tente après en avoir parlé.":
                    $fade_channel("music",0.7,1.0)
                    $ arc7_jessy_tente = True
                    j "J'aimerais te rejoindre. On se dit ce qu'on veut, ce qu'on veut pas. Et on change d'avis si on veut."
                    i "D'accord. On commence par être ensemble. Le reste, on verra."
                    hide ilona
                    with dissolve
                    systeme "Ilona se glisse dans la tente et laisse la toile entrouverte derrière elle."
                    show laplage thumb_up at char_center
                    with dissolve
                    systeme "Derrière un pin, à la lueur de la lampe, Monsieur Laplage lève le pouce vers Jessy."
                    j "... Monsieur Laplage ?"
                    laplage "C'est l'heure."
                    j "L'heure de quoi ?"
                    laplage "Du réarmement démographique."
                    hide laplage
                    with dissolve
                    systeme "Il n'y a plus personne derrière le pin. Il n'y a peut-être jamais eu personne."
                    stop music fadeout 1.5
                    systeme "Jessy décide de ne jamais en parler, et rejoint Ilona. La nuit garde la suite pour elle."
                    scene black
                    with fade
                    play sound audio.puffpuff volume 0.6
                    $ renpy.pause(8.0, hard=True)
    stop ambiant1 fadeout 1.5
    stop music fadeout 1.5
    stop sound fadeout 1.5
    scene black
    with fade
    jump arc_7_jessy_scene_6

# SCENE 6 - LES CONTRE-SOIREES : SOFIANE
label arc_7_jessy_scene_6:
    systeme "Pendant ce temps, la nuit tombe sur les routes de montagne."
    play music audio.spirit_of_the_night volume 0.7 loop fadein 2.0
    play sound audio.car_stop volume 0.6
    scene bg arc7 sofiane belvedere
    with fade
    systeme "L'AE86 s'immobilise au belvédère. Le moteur cliquette en refroidissant. En contrebas, la vallée s'allume point par point, comme une piste qu'on balise."
    systeme "Les deux collègues de Sofiane descendent, déjà en uniforme de maid café. Sofiane s'adosse au capot, les mains dans les poches. Il ne regarde pas la vue. Il regarde la route qui descend."
    "Une collègue" "Tu nous as fait faire vingt minutes de détour juste pour cette vue ?"
    s "La vue, c'est pour vous. Le détour, c'est pour la descente."
    "L'autre collègue" "Et les drifts ? Tu nous les promets depuis le printemps."
    s "Je ne promets rien. Je montre."
    #bruit de portiere
    systeme "Il ouvre la portière, sort un gobelet en carton de la boîte à gants et le remplit d'eau à ras bord. Il le cale dans le porte-gobelet, entre les deux sièges."
    "Une collègue" "C'est pour quoi, ça ?"
    s "Mon cousin m'a appris à conduire avec. Si une goutte tombe, j'ai mal conduit."
    "L'autre collègue" "Et s'il se renverse entièrement ?"
    s "Alors je rends la voiture et je livre du tofu à vélo pour le reste de ma vie."
    systeme "Sur la portière, des caractères noirs annoncent une boutique de tofu. Le cousin n'a jamais voulu expliquer pourquoi."
    s "Montez. Ceintures. Et accrochez-vous à quelque chose que vous aimez."
    scene bg arc7 sofiane phares
    with dissolve
    play sound audio.engineStart volume 0.6
    systeme "Les phares escamotables se lèvent dans un claquement sec. Deux yeux ronds s'ouvrent sur la nuit."
    play sound audio.engine volume 0.6 fadeout 1.0 fadein 0.5
    systeme "Le moteur tousse, puis rugit. Le bruit rebondit sur la paroi et redescend dans la vallée avant eux."
    scene bg arc7 sofiane conduite collegues
    with dissolve
    systeme "Les portières claquent. Sofiane pose une main en haut du volant. Une seule."
    systeme "Au premier virage, le moteur monte jusqu'au rupteur. Au deuxième, les collègues arrêtent de parler. Au troisième, une goutte de sueur descend le long de sa tempe."
    "Une collègue" "Sofiane... on va un peu vite, non ?"
    s "On n'a pas encore commencé."
    "L'autre collègue" "Comment ça, pas encore ?!"
    systeme "Devant, la route plonge. Un panneau jaune annonce une épingle à gauche."
    play sound audio.engine volume 0.6
    scene bg arc7 sofiane pedalier
    with Dissolve(0.2)
    systeme "Sofiane freine tard. Très tard. Puis tout va très vite : le pied droit lâche le frein, le pied gauche enfonce l'embrayage jusqu'au plancher."
    systeme "Un coup de gaz sec. Rapport inférieur. La pédale de frein remonte, encore brillante dans la pénombre, et le moteur hurle dans la nuit."
    play sound audio.drift volume 0.6
    scene bg arc7 sofiane route euphorie
    with hpunch
    systeme "L'AE86 se met en travers. Les pneus crient. Les phares balaient la glissière, puis le vide, puis la lune, puis la route à nouveau. La voiture glisse tout entière à trente centimètres du rail, et Sofiane la tient du bout des doigts."
    "Une collègue" "AAAAH ! ON EST DE TRAVERS ! ON EST COMPLÈTEMENT DE TRAVERS !"
    "L'autre collègue" "ENCORE ! FAIS-LE ENCORE !"
    s "Il y en a cinq autres avant le pont."
    play sound audio.drift volume 0.6
    scene bg arc7 sofiane epingles
    with hpunch 
    systeme "Vue d'en haut, la montagne ressemble à un ruban jeté dans le noir. Et sur ce ruban, deux phares qui dessinent des virgules de lumière."
    systeme "Deuxième épingle. Troisième. La Trueno enchaîne les virages comme on tourne des pages : gauche, droite, gauche, sans jamais lâcher la trajectoire."
    systeme "Dans la quatrième, il pose la roue intérieure dans le caniveau. La voiture tourne comme si elle était accrochée à un rail. Le moteur ne redescend plus."
    play sound audio.drift volume 0.6
    scene bg arc7 sofiane route sourire
    with vpunch
    systeme "À l'arrière, les deux collègues ne crient plus. Elles rient. Du fond du ventre, les yeux fermés, comme au sommet d'un grand huit."
    "L'autre collègue" "Tu nous avais promis une balade !"
    s "Je ne vous ai rien promis. Je vous avais prévenues."
    "Une collègue" "Regarde mes bras ! J'ai la chair de poule jusqu'aux épaules !"
    s "Moi aussi."
    scene bg arc7 sofiane conduite profil
    with dissolve
    systeme "Sofiane ne dit plus rien. Les virages arrivent, il les prend. Il ne pense plus au cousin, ni à la voiture, ni au service de ce soir."
    systeme "Il y a la route, le volant, et le moteur qui chante à la bonne note. Il attendait cette descente depuis l'hiver. Elle est encore mieux que dans sa tête."
    scene bg arc7 sofiane gobelet
    with dissolve
    systeme "Dans le porte-gobelet, l'eau tremble à peine."
    scene bg arc7 sofiane retroviseur
    with Dissolve(0.3)
    systeme "Puis, dans le rétroviseur, deux phares ronds s'allument au sommet de la descente. Loin. Trop loin pour compter."
    systeme "Virage suivant, ils sont plus près. Celui d'après, encore plus. Personne ne remonte Sofiane dans cette descente. Personne."
    "Une collègue" "Sofiane... il y a quelqu'un derrière."
    s "Je sais. Depuis trois virages."
    "L'autre collègue" "Il nous rattrape ?!"
    s "Non. Il nous a déjà rattrapés. Il attend que je lui fasse de la place."
    systeme "Sofiane ne lève pas le pied. Il retarde son freinage d'un mètre. Puis d'un autre. Dans le rétroviseur, les phares ne décrochent pas."
    play sound audio.drift volume 0.6
    scene bg arc7 sofiane epingles laplage
    with hpunch
    systeme "Dans la grande courbe avant le pont, l'AE86 et la berline argentée entrent en glisse côte à côte."
    scene bg arc7 sofiane conduite profil
    with dissolve
    play sound audio.laplage volume 0.6
    scene bg arc7 sofiane croisement laplage
    with hpunch
    systeme "La berline argentée reste à hauteur de l'AE86, en travers à ses côtés. Portière contre portière. Cinquante centimètres entre les deux carrosseries."
    systeme "Au volant, cheveux blancs, moustache impeccable : Monsieur Laplage. Une main sur le volant, le coude à la fenêtre, comme au feu rouge un dimanche matin."
    "L'autre collègue" "C'est... c'est un papy ?"
    "Une collègue" "IL Y A UN PAPY QUI DRIFTE À CÔTÉ DE NOUS !"
    s "Ne criez pas. Regardez. Ça n'arrivera pas deux fois."
    systeme "Deux voitures de travers dans la même courbe. Même angle, même vitesse, même fumée blanche sous les roues. Aucun des deux ne lâche un centimètre. À l'arrière, plus personne ne respire."
    scene bg arc7 sofiane croisement laplage pouce
    with dissolve
    systeme "À la corde, Laplage tourne la tête. Il regarde Sofiane. Il regarde le gobelet. Puis il lève le pouce."
    systeme "Sofiane incline la tête d'un centimètre. Pas plus. C'est tout ce qu'un pilote dit à un autre pilote, et c'est déjà beaucoup."
    play sound audio.car_go volume 0.6
    scene bg arc7 sofiane conduite profil
    with dissolve
    systeme "À la sortie du virage, la berline argentée accélère et passe devant. Elle double l'AE86 par l'extérieur, là où il n'y a pas la place."
    play sound audio.drift volume 0.6 
    scene bg arc7 sofiane epingles
    with dissolve
    systeme "La berline file hors du cadre. L'AE86 reste seule dans la courbe, avalée un instant par la fumée."
    scene bg arc7 sofiane route vide
    with Dissolve(0.3)
    systeme "Au moment où elle se rabat devant eux, il n'y a plus rien. Pas de feux arrière. Pas de bruit de moteur. La route est vide jusqu'au pont."
    systeme "Il ne reste qu'un voile de fumée blanche qui flotte dans les phares, et qui retombe doucement."
    "L'autre collègue" "Il est passé où ?"
    "Une collègue" "Il y a pas de sortie. Il y a pas de sortie, Sofiane !"
    s "Je sais."
    "L'autre collègue" "Et ça te fait rien ?!"
    s "Si. Ça me donne envie de revenir."
    scene bg arc7 sofiane conduite profil
    with dissolve
    systeme "Sofiane regarde la route vide un long moment. Ses mains sont moites sur le volant. Il sourit."
    s "Ce soir, il est venu voir. La prochaine fois, ce sera une course."
    "Une collègue" "Tu te rends compte que c'est la phrase la plus classe que tu aies jamais dite ?"
    s "Je sais. Je ne la répéterai pas."
    systeme "L'AE86 finit la descente. Les lumières de la ville approchent. Les deux collègues arriveront à l'heure. En avance, même."
    play sound audio.carStop volume 0.6 
    stop music fadeout 2.0
    systeme "Sur le parking du maid café, Sofiane coupe le moteur et baisse les yeux vers le porte-gobelet."
    systeme "Pas une goutte."
    systeme "Quelque part, un cousin n'est pas déçu."
    stop music fadeout 1.0
    jump arc_7_jessy_scene_7

# SCENE 7 - LES CONTRE-SOIREES : ALLAN ET THEO
label arc_7_jessy_scene_7:
    play music audio.barjazz loop volume 0.7 fadein 1.0
    scene bg arc7 tokyo restaurant
    with fade
    systeme "Le même soir, à Tokyo. La pluie vient de s'arrêter."
    systeme "Allan est arrivé il y a trois jours. Trois jours à écrire des messages à Théo et à les effacer avant la fin de la première phrase."
    systeme "Ce matin, il a fini par envoyer la photo d'une vieille enseigne, avec une seule question : {i}« Tu connais cet endroit ? »{/i}"
    systeme "La réponse est arrivée quarante minutes plus tard : {i}« Oui. 19h. »{/i} Allan l'a relue plus de fois qu'il ne l'avouera."
    show allan beach neutral at char_midleft
    with dissolve
    systeme "Le restaurant est calme. Des tables de bois occupent la salle, éclairées par une lanterne au-dessus de la table près de la fenêtre. Les lumières de la ville se brouillent dans la vitre."
    systeme "Allan est arrivé avec vingt minutes d'avance. Il fixe le menu comme un manuscrit à déchiffrer."
    systeme "La porte s'ouvre. Théo secoue son parapluie sur le seuil."
    show theo tokyo neutral at char_midright
    with dissolve
    systeme "Allan se lève. Se rassoit. Se relève à moitié, parce qu'il ne sait plus ce qu'on fait avec quelqu'un qu'on connaît depuis dix ans et à qui on n'a pas parlé depuis trois mois."
    t "Assieds-toi. Tu fais peur au patron."
    a "Je me lève par politesse. On m'a bien élevé."
    t "On se lève pas pour un pote. On dirait un entretien d'embauche."
    show allan beach smirk
    a "Parfait. Je voulais pas me fondre dans la masse."
    systeme "Théo s'assoit en face. Il pose son pull humide sur le dossier, bien plié, comme toujours. Il a maigri. Ou alors c'est la lumière."
    t "Tu as commandé quoi ?"
    a "Aucune idée. J'ai pointé du doigt. Deux fois la même pâtisserie."
    t "Pourquoi deux fois la même ?"
    a "Pour t'en laisser une."
    t "Tu aurais pu en choisir une que j'aime."
    a "Le menu est écrit à la main par le patron. J'ai reconnu trois caractères sur dix-huit. J'ai fait confiance au destin."
    t "C'est de la patate douce."
    a "Tu lis son écriture, maintenant ?"
    t "Le menu, oui. Le reste, pas encore."
    systeme "Il mange quand même. Allan fait semblant de ne pas remarquer que ça le fait sourire."
    a "Bon. Rapport de mission. Je me suis perdu quatre fois en trois jours."
    a "Un distributeur m'a vendu un café tellement chaud que j'ai encore la marque dans la paume. Et j'ai trouvé un sanctuaire en cherchant une station de métro."
    t "C'est la seule bonne façon de trouver les sanctuaires."
    a "Et toi ?"
    t "Mon propriétaire m'appelle par un nom différent chaque semaine. Cette semaine, c'est Tao."
    a "C'est presque ça."
    t "Je prends le train sans vérifier le plan trois fois. Deux fois, maintenant. Et je mange la même chose tous les soirs, parce que je fais jamais les courses."
    a "Toi. Le mec qui faisait des tableaux de révision pour ses amis."
    t "Les tableaux, c'est plus facile quand c'est pour les autres."
    a "Laplage m'a souhaité bon voyage, la veille de mon départ. Je l'avais dit à personne."
    show theo tokyo smirk
    t "Le Messi sait toujours."
    a "Tu l'appelles encore comme ça."
    t "Il y a des titres qu'on retire pas."
    a "Et vivre seul, ici ? Ça donne quoi ?"
    show theo tokyo neutral
    t "Le loyer est correct. Le trajet jusqu'au studio, trente-deux minutes. Les horaires sont stables, les trois chaînes tournent bien, le..."
    systeme "Il s'arrête au milieu du mot. Il tourne sa tasse d'un quart de tour. Puis d'un autre."
    t "C'est plus silencieux que prévu."
    t "J'ai pris un appartement avec deux chambres. Je me suis dit : au cas où."
    t "La deuxième clé est dans un tiroir de la cuisine. Je la vois chaque fois que je cherche une fourchette."
    show allan beach silence
    systeme "Allan avait une blague prête. Il la garde pour lui."
    t "Je regrette pas d'être venu. Le travail, je le voulais vraiment."
    t "Mais des fois, il se passe un truc. Un chat sur un vélo. Un vieux qui chante dans le métro. Et j'ai envie de l'envoyer à quelqu'un, et je sais pas par où commencer."
    a "Tu m'as envoyé des photos, pourtant."
    t "Oui."
    a "Ton plan de travail. Un tableau d'horaires. Un plan de métro avec ta ligne surlignée en jaune."
    a "J'ai regardé ton plan de métro pendant dix minutes, Théo. Pour voir si t'avais écrit quelque chose dans la marge."
    show theo tokyo hesitant
    t "J'envoyais ce que je savais expliquer."
    a "Une photo floue d'un dîner raté m'aurait suffi. Et les téléphones peuvent encore appeler. C'est même leur fonction d'origine, techniquement."
    t "... La prochaine fois, je t'envoie le dîner raté."
    a "Et tu appelles."
    t "Et j'appelle."
    systeme "La pluie tambourine sur la vitre. Allan repose sa tasse sans avoir bu."
    show allan beach doubt
    a "Le 6 avril, j'avais l'heure de ton train. Ta mère me l'avait donnée."
    t "Je savais pas."
    a "Je l'ai regardée passer sur mon téléphone. J'étais dans ma cuisine. J'avais même mis mes chaussures."
    show theo tokyo disappointed
    t "Je suis parti seul. Je m'étais dit que c'était plus simple pour tout le monde."
    t "À la gare, j'ai regardé l'escalier du quai jusqu'au départ. Comme un idiot. Au cas où quelqu'un..."
    systeme "Il ne finit pas la phrase. Allan ne sait pas quel prénom devait venir après. Peut-être que Théo ne le sait pas non plus."
    a "J'aurais dû venir."
    t "Je t'avais pas demandé de venir."
    a "Tu demandes jamais. C'est pour ça que j'aurais dû venir quand même."
    a "Au gymnase. Notre prise de bec. Je veux pas que ce soit la dernière vraie chose qu'on se soit dite."
    t "Moi non plus."
    t "J'y repense souvent. Dans le train, surtout. Trente-deux minutes, c'est long, quand t'as une phrase coincée."
    t "T'avais raison. Pas sur tout. Mais sur assez de choses pour que ça m'empêche de dormir."
    t "Tu m'as traduit pendant dix ans. Aux profs, aux autres, à Ilona. Je t'ai jamais demandé si ça te fatiguait."
    a "Ça me fatiguait."
    t "Je sais. Maintenant, je sais."
    show allan beach support
    a "J'ai pas arrêté de te traduire pour te punir, Théo. J'ai arrêté parce que je voulais que tu me parles à moi. Pas à travers moi."
    systeme "Théo baisse les yeux sur sa pâtisserie à moitié mangée. Sa mâchoire se serre, comme au collège, quand il refusait de pleurer devant un prof."
    t "T'as bien fait de pas laisser ça pourrir dans le silence. Moi, je l'aurais laissé. Pendant des années, sûrement."
    if arc6_offre_theo == "laisse":
        t "Dans le couloir, Jessy a rien dit. J'ai pris son silence pour une réponse. Ça m'arrangeait."
        t "J'ai fait pareil avec toi. Je me taisais, et je te laissais deviner ce que je pensais. Tu devinais toujours juste, alors je me suis jamais forcé."
        t "Je veux plus te faire deviner."
    elif arc6_offre_theo == "accusation":
        t "Jessy m'a dit que Tokyo, c'était surtout un moyen d'avoir une place dans l'avenir d'Ilona."
        t "Et au passage, il a répondu à sa place à elle. Les deux étaient vrais."
        t "J'ai passé tout le trajet à lui en vouloir pour la deuxième partie. Comme ça, j'avais pas à penser à la première."
    elif arc6_offre_theo == "aveu_vide":
        t "Jessy a dit qu'il avait rien à mettre en face de Tokyo. Sur le moment, j'ai trouvé ça pathétique."
        t "Mais elle comparait pas deux offres. C'est moi qui comparais. Elle, elle regardait deux personnes."
    elif arc6_conversation == "que_veux_tu":
        t "Jessy a dit qu'il voulait qu'elle reste. Sans lui demander de porter ça pour lui."
        t "Moi, j'avais un studio, une équipe, un planning. Et j'ai jamais dit ce que je voulais, moi. J'ai laissé le planning parler à ma place."
    elif arc6_conversation == "aveu_interruptions":
        t "Jessy a reconnu devant moi qu'il la coupait tout le temps. J'avais préparé trois arguments. Il venait de les dire lui-même."
        t "Moi, je la coupais pas. Je finissais ses projets à sa place. Je sais pas si c'est mieux."
    elif arc6_offre_theo == "question":
        t "Jessy a posé une question au lieu de répondre. Sur le moment, j'ai trouvé ça faible."
        t "C'était sûrement la chose la plus honnête dite dans ce couloir. Et c'était pas moi qui l'avais dite."
    t "À Noël, j'ai demandé au Messi si je forçais quelqu'un à rester. Il m'a répondu : « Non. Mais tu gardes la clé. »"
    t "J'ai mis quatre mois à comprendre que c'était pas un compliment."
    a "Et la clé dans ton tiroir ?"
    t "Je sais pas quoi faire d'une clé que personne m'a demandée."
    a "Et maintenant ?"
    t "Maintenant, quoi ?"
    a "Qu'est-ce que tu veux faire ? Pas cette année. Ce soir. On a une soirée entière, et je repars jeudi."
    systeme "Théo réfléchit longtemps. Allan le connaît assez pour savoir qu'il cherche la réponse la plus efficace, et qu'il n'en trouve pas."
    show theo tokyo neutral
    t "Marcher. Avec quelqu'un qui se perd."
    show allan beach smirk
    a "Tu tombes bien. C'est ma spécialité."
    stop ambiant1 fadeout 1.5
    stop music fadeout 1.5
    $ renpy.pause(1.0, hard=True)
    play music audio.citynight loop volume 0.7 fadein 1.0 fadeout 1.0
    scene bg arc7 tokyo park
    show allan beach smirk at char_midleft
    show theo tokyo neutral at char_midright
    with fade
    systeme "Ils ressortent et rejoignent un parc voisin. Les allées sont encore humides ; les lampadaires éclairent les cerisiers et, au-delà des arbres, les immeubles de Tokyo."
    systeme "Allan déplie une carte papier. Théo la retourne. Allan la retourne à nouveau. Ils se disputent deux minutes sur la position du nord, avec l'énergie de deux gamins de douze ans."
    t "Tu tiens les cartes à l'envers depuis le collège."
    a "Le nord est une convention sociale."
    a "Tu as des nouvelles d'Ilona ?"
    t "Pas vraiment. Pourquoi ?"
    a "Elle est en randonnée. Avec Jessy. Ce week-end."
    systeme "Théo marche encore trois pas avant de répondre. Allan les compte."
    t "Bien."
    show theo tokyo disappointed
    t "Ça pique un peu. Je vais pas te mentir, t'as fait une centaine de kilomètres pour venir."
    t "Mais elle est restée. Elle avance dans la vie qu'elle a choisie. Je vais pas parler à sa place. J'ai assez fait ça."
    t "Et mon départ, c'est ma décision. Je veux pas qu'elle le porte comme un truc qu'elle m'aurait fait."
    show allan beach neutral
    a "Tu veux que je lui dise quelque chose, en rentrant ?"
    systeme "Théo y pense vraiment. Allan le voit trier des phrases, en jeter la plupart."
    t "Non."
    t "Si un jour j'ai quelque chose à lui dire, je le dirai moi-même. Sans traducteur."
    show allan beach support
    a "Bonne réponse."
    systeme "Près d'un banc, Allan s'arrête devant les lumières de la ville. Il lève son téléphone par réflexe, puis le baisse. Théo est à côté de lui. Il n'a plus besoin de lui envoyer."
    show theo tokyo reassuring
    t "Prends-la quand même. Ça fera une preuve."
    a "Une preuve de quoi ?"
    t "Qu'on y était. Tous les deux."
    a "Alors pas la ville. Nous."
    systeme "Allan tend le bras pour les prendre en photo avec la ville en arrière-plan. Théo se penche au dernier moment, trop tard. La photo est floue. Ils la gardent."
    systeme "Dix ans d'amitié ne se cassent pas en trois mois de silence. Ça a vacillé, c'est tout. Ils rentrent par le même chemin, et se trompent deux fois de rue, ensemble."
    scene black
    with fade
    systeme "À une heure du matin, dans sa chambre d'hôtel, le téléphone d'Allan vibre."
    systeme "Une photo floue. Un bol de nouilles renversé sur un plan de travail. {i}« Dîner raté. Comme promis. »{/i}"
    systeme "Une deuxième vibration. {i}« J'appelle demain. »{/i}"
    a "... Il a mis un point. Même à ça."
    stop music fadeout 1.0
    jump arc_7_jessy_nuit_retour

# RETOUR AU BIVOUAC APRES LES CONTRE-SOIREES
label arc_7_jessy_nuit_retour:
    play ambiant1 audio.forestNight volume 0.4 loop fadein 1.5
    scene bg arc7 jessy nuit tente ferme
    with fade
    systeme "Au même moment, loin de Tokyo, la nuit avance sur la montagne."
    if arc7_jessy_relation == "amitie":
        scene bg arc7 jessy nuit tente ferme
        with dissolve
        show jessy rando embarrassed at char_left
        show laplage neutral at char_right
        with dissolve
        systeme "Près du hamac, une silhouette immobile regarde Jessy dormir. Jessy ouvre les yeux. Se fige."
        j "Un clochard !"
        systeme "Laplage a l'air sincèrement choqué. Puis, comme dans un appel codec au milieu d'une infiltration, il porte deux doigts à son oreille."
        laplage "Jessy. Il faut parfois savoir laisser la porte ouverte."
        j "La porte ouverte ?"
        laplage "Et ne pas confondre attendre avec renoncer."
        j "Attendre, ce n'est pas renoncer ?"
        laplage "Ce que choisira Ilona lui appartient. Ce que tu ressens aussi."
        j "Ce que je ressens... ?"
        laplage "Termine l'appel, Jessy."
        hide laplage
        with dissolve
        systeme "Laplage n'est plus là. Il n'y a que les branches et le bruit de la toile qui bouge un peu, à quelques mètres."
        systeme "Jessy fixe le ciel. Il pense à Metal Gear Solid, à la Citadelle, aux portes qu'on laisse ouvertes. Puis il se rendort."
    else:
        if arc7_jessy_tente:
            systeme "La lampe est éteinte. Derrière la toile de la tente, leurs voix se sont tues. La montagne garde le silence jusqu'à l'aube."
        else:
            systeme "La lampe est éteinte. La montagne garde un silence paisible autour de la tente et du hamac."
    stop ambiant1 fadeout 1.0
    jump arc_7_jessy_scene_8

# SCENE 8 - LA FIN ET LE COMMENCEMENT
label arc_7_jessy_scene_8:
    scene bg arc7 jessy aube
    with fade
    play music audio.morningLove loop volume 0.7 fadein 1.0
    play ambiant1 audio.windBirds loop volume 0.4
    show jessy rando neutral at char_left
    show ilona rando neutral at char_right
    with dissolve
    if arc7_jessy_tente:
        systeme "Dimanche, à l'aube. La rosée couvre la toile. Jessy se réveille le dos raide contre le sol. Ilona a déjà la tête dehors, les cheveux en bataille."
    else:
        systeme "Dimanche, à l'aube. La rosée couvre la tente. Jessy se réveille dans son hamac, le dos raide. La fermeture éclair s'ouvre ; Ilona passe la tête, les cheveux en bataille."
    i "Bonjour."
    j "C'est déjà le matin ?"
    i "Les oiseaux ont l'air d'en être convaincus."
    if arc7_jessy_relation == "amour":
        if arc7_jessy_tente:
            i "T'as bien dormi ?"
            systeme "Elle sourit. Un sourire timide qu'il ne lui connaissait pas."
            show ilona rando smile at char_right
            i "Tu prends beaucoup de place, en vrai. Pour quelqu'un qui dort en boule."
            j "Je peux plaider la tente trop petite ?"
            i "Non."
        else:
            i "Ton hamac a tenu ?"
            j "Par morceaux. J'ai dormi en quatre épisodes. Le troisième était bien."
            show jessy rando smile at char_left
        i "Je suis contente qu'on se soit parlé. Pour de vrai."
        j "Moi aussi. Et on est pas obligés de tout dessiner avant d'être en bas."
        i "Tu vas quand même faire un plan."
        j "Un petit. Plié en quatre. Pas en huit."
    else:
        systeme "Il y a un flottement. Un petit. Elle le laisse passer avant de parler."
        show ilona rando sad at char_right
        i "Merci pour hier. D'avoir été honnête."
        i "Ce que je ressens a pas disparu cette nuit. Ça va prendre un peu de temps."
        j "Je sais. Prends-le."
        systeme "Il n'ajoute rien. Il ne demande pas si ça va. Pour une fois, il laisse la phrase finir toute seule."
    i "En tout cas, Alexandre a vraiment pêché une feuille."
    j "Et Monsieur Laplage est vraiment passé sur un ours."
    i "Personne va nous croire."
    j "Tant mieux. C'est à nous."
    systeme "Ils rient. Le matin n'efface pas la veille. Il lui donne juste assez d'air pour continuer."
    systeme "Jessy décroche le hamac. Ilona replie la tente, en huit minutes cette fois. Ils ramassent chaque papier, chaque miette. Le bivouac redevient une clairière."
    if arc7_jessy_fruit == "goute":
        systeme "Ilona sort le noyau étoilé de sa poche et le regarde dans la lumière."
        i "Tu crois qu'on en retrouvera un, un jour ?"
        j "Je crois surtout qu'Alexandre lui aurait cherché une fonction."
        i "Il en a pas besoin."
    j "Pour redescendre, tu préfères quel chemin ?"
    i "Celui qui longe les arbres. Il a l'air de prendre son temps."
    j "Alors on prend celui-là."
    show jessy rando bag smile at char_left
    show ilona rando bag smile at char_right
    with dissolve
    systeme "Ils descendent côte à côte dans la lumière neuve. Jessy tient la carte. À l'envers. Ilona ne dit rien."
    stop ambiant1 fadeout 1.0
    stop music fadeout 2.0
    scene black
    with fade
    # La collection complete offre une fin secrete sans effacer leur choix.
    if ilonanium_points >= 6 and arc7_jessy_fruit == "goute":
        menu:
            "Quel chemin suivent-ils après la montagne ?"
            "Suivre la piste du fruit étoilé et finir la planète.":
                jump ending_ilonanium
            "Continuer la vie qu'ils ont choisie ensemble.":
                jump arc_7_jessy_fin_relation
    else:
        jump arc_7_jessy_fin_relation

label arc_7_jessy_fin_relation:
    if arc7_jessy_relation == "amitie":
        jump ending_no_contact
    else:
        $ arc7_jessy_family_epilogue = arc6_score >= SEUIL_ROMANCE and lien_jessy_ilona >= SEUIL_LIEN and souvenirs["jessy_repare"] and souvenirs["maison_respectee"] and interruptions_reparees >= 1
        jump ending_jessy_ilona
