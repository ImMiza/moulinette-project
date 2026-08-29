# Arc II - Vacances d'ete : la plage.
# Les variables importantes restent centralisees dans script.rpy.

image bg arc2 beach main = im.Scale("images/scenes/arc_2/bg_arc2_beach_main.jpg", 1920, 1080)
image bg arc2 beach sunset = im.Scale("images/scenes/arc_2/bg_arc2_beach_sunset.jpg", 1920, 1080)
image bg arc2 group parasol = im.Scale("images/scenes/arc_2/bg_arc2_group_parasol.jpg", 1920, 1080)
image bg arc2 jetty = im.Scale("images/scenes/arc_2/bg_arc2_jetty.jpg", 1920, 1080)
image bg arc2 kakigori counter = im.Scale("images/scenes/arc_2/bg_arc2_kakigori_counter.jpg", 1920, 1080)
image bg arc2 lost items table = im.Scale("images/scenes/arc_2/bg_arc2_lost_items_table.jpg", 1920, 1080)
image bg arc2 minecraft house summer night = im.Scale("images/scenes/arc_2/bg_arc2_minecraft_house_summer_night.jpg", 1920, 1080)
image bg arc2 tide pools = im.Scale("images/scenes/arc_2/bg_arc2_tide_pools.jpg", 1920, 1080)

define audio.footSand = "audio/fx/sand-walk.mp3"

default arc2_reaction_invitation = ""
default arc2_photo_reaction = ""
default arc2_choix_activite_theo = ""
default arc2_retour_minecraft = ""
default arc2_scene_laplage = False


label arc_2_plage:
    play music audio.ecole loop volume 0.8
    scene bg shared school corridor
    with fade

    systeme "Arc II - Vacances d'été : la plage."
    systeme "Juillet arrive avec une promesse simple : une journée sans cours, sans couloir, sans rumeur à moitié chuchotée."
    systeme "La théorie tient jusqu'au premier prénom qui reste un peu trop longtemps dans l'air."

    show allan excited at char_left
    show alex grin at char_midleft
    show jessy neutral at char_midright
    show ilona smile at char_right

    a "Plage samedi."
    x "C'est une annonce ou une menace ?"
    a "Une organisation."
    i "Donc une menace avec horaires."
    a "Exactement."
    a "Il y aura nous, vous deux, et Théo."

    show jessy embarrassed at char_midright
    systeme "Jessy connaît surtout Théo par les phrases d'Allan : toujours là au bon moment, toujours avec une réponse prête."

    menu:
        "Allan vient d'annoncer que Théo sera là."

        "Demander simplement qui vient.":
            $ arc2_reaction_invitation = "simple"
            $ communication += 1
            j "D'accord. On sera combien ?"
            a "Cinq. Six si Sofiane apparaît comme une énigme de fin de chapitre."
            i "Il fait ça souvent ?"
            x "Il respire en cliffhanger."

        "Faire une blague sur le château de sable impossible.":
            $ arc2_reaction_invitation = "blague"
            $ lien_jessy_ilona += 1
            j "Alexandre va construire un château techniquement inhabitable."
            x "Je vise l'illégalité architecturale."
            i "Notre maison Minecraft a formé toute une génération."

        "Répondre trop vite à propos de Théo.":
            $ arc2_reaction_invitation = "theo_trop_vite"
            $ jalousie += 1
            j "Ah. Théo aussi ?"
            i "Oui."
            $ renpy.pause(0.7)
            show ilona neutral at char_right
            systeme "Ilona ne se fâche pas. Elle garde simplement la fin de son sourire pour plus tard."
            $ renpy.pause(0.5)
            j "Pardon. Je demandais juste."
            i "D'accord."

        "Se taire.":
            $ arc2_reaction_invitation = "silence"
            $ communication -= 1
            systeme "Jessy hoche la tête."
            systeme "Ilona sourit encore. Son regard attend une phrase qui ne vient pas."

    hide allan
    hide alex
    hide jessy
    hide ilona
    with dissolve
    play music audio.mornPiano volume 0.9 fadeout 1.0 fadein 1.0 loop
    play ambiant1 audio.trainInside volume 0.8 fadein 1.5 loop
    scene bg shared train inside
    with fade
    show jessy neutral at char_left
    show ilona smile at char_right

    systeme "Samedi matin. Le train vers la mer est presque vide. Les sièges libres rendent les silences moins visibles."
    i "Tu crois qu'on devrait ajouter une pièce d'été à la maison ?"
    j "Une plage intérieure ?"
    i "Une cuisine de plage."
    j "Donc une quatrième cuisine."
    i "C'est important d'avoir des traditions."

    if ilona_peut_finir_ses_phrases >= 2:
        i "Au printemps, tu m'as laissée répondre à mon rythme."
        j "J'essaie."
        i "Ça se voit."
    elif communication < 1:
        i "C'est plus simple quand personne ne nous demande ce qu'on est."
        j "Oui."
        systeme "La réponse n'est pas fausse. Elle n'ouvre pas grand-chose non plus."

    show sofiane neutral at char_center
    with dissolve
    s "Les rails savent toujours où ils vont. C'est leur malédiction."
    i "Bonjour Sofiane."
    s "J'ai pris des chips."
    j "Tu viens avec nous ?"
    s "La mer a appelé. J'ai laissé sonner deux fois."
    hide sofiane
    with dissolve
    stop ambiant1 fadeout 1.0

    play music "music/plage-day.mp3" fadeout 1.0 fadein 2.0 loop volume 0.8
    play ambiant1 "ambience/ocean-waves.mp3" volume 0.3 loop fadein 2.0
    scene bg arc2 group parasol
    with fade
    show allan smirk at char_left
    show alex teasing at char_midleft
    show jessy neutral at char_midright
    show ilona smile at char_right

    systeme "Sur la plage, Alexandre mesure l'ombre du parasol comme si le sable avait besoin d'un permis de construire."
    x "Si on place les serviettes ici, le château aura une cuisine."
    a "Pourquoi un château de sable aurait une cuisine ?"
    i "Question dangereuse."
    j "Chez nous, c'est presque une obligation légale."

    show theo reassuring at char_center
    with dissolve
    t "Vous devriez vous mettre un peu plus loin des rochers. La marée monte vite ici."
    a "Vous voyez ? Théo sait même où l'eau va avant l'eau."
    t "Je lis les panneaux."
    x "Méthode honteusement fiable."

    play sound "fx/sand-noise.mp3"
    systeme "Théo ne demande pas. Il plante le parasol, ajuste l'angle, puis pose le sac d'Ilona dans l'ombre avant qu'elle ait le temps de répondre."
    t "Tu préfères l'ombre, non ?"
    systeme "Il le dit comme une question, mais le sac est déjà posé."
    i "... Oui. Merci."
    systeme "Elle sourit. Théo aussi. Jessy remarque que Théo a retenu ce détail sur Ilona sans avoir besoin de demander."

    menu:
        "Ilona cherche une place pour sa serviette."

        "L'aider sans commenter son désordre.":
            $ lien_jessy_ilona += 1
            $ autonomie_ilona += 1
            j "Je te garde ce coin ?"
            i "Oui. Merci."
            systeme "Jessy pose simplement le sac. Le geste ne cherche pas à devenir une preuve."

        "Faire une blague sur la zone Ilona.":
            $ lien_jessy_ilona += 1
            j "Attention, zone Ilona. Stock de snacks instable."
            if lien_jessy_ilona >= 5:
                i "Très instable. Ne pas approcher sans offrande."
            else:
                i "Je peux avoir une zone sans panneau ?"
                $ communication -= 1

        "Regarder surtout ce que fait Théo.":
            $ jalousie += 1
            systeme "Jessy regarde Théo organiser les sacs et les parasols."
            $ renpy.pause(0.8)
            show ilona neutral at char_right
            systeme "Ilona replie un coin de sa serviette. Elle a vu où regardait Jessy."
            i "Tu vérifies quelque chose ?"
            j "Non. Pardon."
            show ilona smile at char_right
            systeme "Ilona ne force pas la question, mais elle la laisse là, entre eux."

    systeme "La plage reprend ensuite ses droits : crème solaire mal étalée, serviettes déplacées trois fois, château de sable déclaré officiellement instable."
    x "Je refuse les normes de construction terrestres."
    a "Il vient de mettre une porte sur le toit."
    i "C'est une maison de vacances, alors."
    j "Notre influence devient préoccupante."
    systeme "Pendant quelques minutes, Théo n'est plus un sujet. Il est juste une personne de plus dans le groupe, ce qui rend la journée respirable."

    hide allan
    hide alex
    hide jessy
    hide ilona
    hide theo
    with dissolve

    #ambiance foule
    play sound audio.footSand 
    play ambiant1 "ambience/crowd-noise.mp3" volume 0.4
    scene bg arc2 kakigori counter
    with fade
    show ilona neutral at char_left
    show jessy neutral at char_midleft
    show theo neutral at char_midright

    systeme "Plus tard, Ilona revient du stand de kakigōri en fouillant son sac."
    i "Attendez."
    i "Mon porte-clés bloc."
    j "Celui de la maison ?"
    i "Oui."
    systeme "Jessy cherche tout de suite dans le sable, avec assez d'empressement pour déplacer plus de sable que d'air."
    show jessy embarrassed at char_midleft
    j "Il était accroché où exactement ?"
    i "À la fermeture du sac."
    j "D'accord. Donc—"
    t "Tu l'as sorti vers le stand, non ? Quand tu as parlé de la cuisine Minecraft."
    systeme "Théo se lève déjà. Pas pressé, juste... efficace."
    i "Je... oui, je crois."
    t "Tu portais ton sac à gauche. Je vais voir près du comptoir."

    hide theo
    with dissolve
    systeme "Théo retrouve le porte-clés près du comptoir, coincé contre une caisse de sirop bleu."
    systeme "Quand il revient, il le tend à Ilona. Ses doigts frôlent les siens une demi-seconde de trop."
    show theo reassuring at char_midright
    t "Il avait roulé sous la table. Tu l'avais regardé juste après avoir parlé de la cuisine."
    i "Tu as... tu te souviens de ça ?"
    t "Je fais attention."
    systeme "Ilona reprend le porte-clés. Elle rougit légèrement. Pas beaucoup. Juste assez."
    show ilona smile at char_left
    i "Merci. Vraiment. Je croyais l'avoir perdu."
    t "Je savais qu'il n'était pas loin."
    systeme "Jessy les regarde. Théo vient de faire en trente secondes ce que lui n'a pas su faire en deux minutes."
    systeme "Et Ilona sourit à Théo avec une reconnaissance que Jessy reconnaît : c'est celle qu'elle lui donnait avant, quand il réparait quelque chose pour elle."

    menu:
        "Théo vient de briller là où Jessy a échoué. Ilona le regarde encore."

        "Chercher aussi et trouver autre chose.":
            $ communication += 1
            $ jalousie += 1
            $ lien_jessy_ilona += 1
            systeme "Jessy se baisse. Il fouille le sable à son tour."
            systeme "Il ne trouve pas le porte-clés. Il trouve une petite coquille blanche."
            j "J'ai trouvé ça."
            i "C'est pas mon porte-clés."
            j "Je sais. Mais tu aimes bien les trucs inutiles."
            systeme "Ilona regarde la coquille. Puis elle sourit."
            i "C'est vrai."
            systeme "Elle prend la coquille. Garde le porte-clés que Théo a trouvé."
            systeme "Jessy n'a pas gagné. Mais il n'a pas disparu non plus."

        "Faire blague pour masquer blessure.":
            $ jalousie += 1
            $ communication -= 1
            j "Bon. Le sable est officiellement innocent."
            systeme "La blague tombe plate. Personne ne rit."
            i "Jessy..."
            systeme "Elle le regarde comme si elle venait de voir quelque chose se fissurer."
            systeme "La blague n'a pas caché la blessure. Elle l'a soulignée."

        "Le remercier sincèrement.":
            $ confiance += 1
            $ autonomie_ilona += 1
            $ lien_jessy_ilona += 1
            j "Merci. Vraiment."
            t "De rien."
            systeme "Théo sourit. Jessy aussi."
            systeme "Mais le sourire de Jessy travaille déjà. Il vient d'accepter de ne pas être celui qui répare."
            systeme "C'est mature. Mais ça lui coûte plus qu'il ne le montre."

        "Se taire et encaisser.":
            $ jalousie += 2
            $ communication -= 1
            $ influence_theo += 1
            systeme "Jessy ne dit rien. La phrase reste coincée dans sa gorge."
            systeme "Ilona attend une réponse qui ne vient pas. Puis elle range le porte-clés."
            systeme "Théo observe le silence. Il le note."

    systeme "Ils retournent vers les autres avec le porte-clés retrouvé."
    systeme "Allan parle d'une boisson renversée, Alexandre accuse le vent, mais Jessy voit bien qu'Ilona tient encore le porte-clés comme si c'était Théo qui le lui avait offert."
    if jalousie >= 2:
        systeme "Jessy sent quelque chose de sombre se tordre dans sa poitrine. Ce n'est pas de la colère. C'est pire : c'est de l'impuissance."
    stop ambiant1 fadeout 2.0
    hide jessy
    hide ilona
    hide theo
    with dissolve
    play sound audio.footSand 

    scene bg arc2 beach main
    with fade
    show allan neutral at char_left
    show alex grin at char_midleft
    show jessy neutral at char_center
    show ilona smile at char_midright
    show theo neutral at char_right

    play sound "fx/photo-taken.mp3" volume 1.0
    systeme "Quand le groupe prend une photo, Allan recule trop vite pour cadrer. Tout le monde se décale."
    systeme "Sur l'écran, Jessy est à une extrémité. Ilona sourit près de Théo."
    a "Désolé. J'ai bougé."
    x "Composition narrativement suspecte."
    a "Alexandre."
    x "Je retire le mot narrativement."

    menu:
        "La photo n'a rien décidé. Jessy la regarde pourtant comme si elle avait pris parti."

        "Dire que composition bizarre sans insister.":
            $ arc2_photo_reaction = "remarque_neutre"
            $ communication += 1
            j "Composition bizarre."
            a "Désolé. J'ai bougé trop vite."
            j "C'est pas grave."
            systeme "Jessy a reconnu le malaise sans le transformer en crise."
            systeme "Mais Allan voit bien que la phrase cachait quelque chose de plus lourd."

        "Proposer refaire photo, légèrement.":
            $ arc2_photo_reaction = "refaire_doux"
            $ communication += 1
            $ jalousie += 1
            j "On en refait une où je suis moins exilé ?"
            i "Oui."
            t "Bonne idée."
            play sound "fx/photo-taken.mp3"
            systeme "La première photo reste. La deuxième existe aussi."
            systeme "Jessy a exprimé son besoin. Mais il sait aussi qu'il vient de montrer son insécurité."

        "Se taire et garder pour soi.":
            $ arc2_photo_reaction = "silence_photo"
            $ jalousie += 1
            $ communication -= 1
            systeme "Jessy regarde la photo. Ne dit rien."
            systeme "La phrase reste dans sa gorge. Elle n'y gagne pas en légèreté."
            systeme "Ilona range le téléphone. Elle a senti le silence."

        "Accepter photo et complimenter Ilona.":
            $ arc2_photo_reaction = "accepter_compliment"
            $ confiance += 1
            $ lien_jessy_ilona += 1
            j "Elle est bien. Tu souris vraiment dessus."
            i "Oui."
            systeme "Ilona le regarde, surprise par la simplicité de la réponse."
            i "Merci."
            systeme "Jessy a choisi la confiance. Mais il voit bien qu'Ilona sourit près de Théo."
            systeme "Le compliment était sincère. La blessure aussi."

    systeme "Après la photo, le groupe se disperse sans vraiment se séparer."
    systeme "Allan part chercher les boissons. Alexandre tente de sauver son château de sable."
    i "Vous voulez quelque chose de spécial ?"
    j "Toi ?"
    i "Je vais prendre la gelée marine lumineuse."
    a "Le truc dont personne ne défend la composition ?"
    i "Il m'a regardée en premier."
    systeme "Le soleil descend un peu. Les ombres s'allongent. Les petites tensions aussi."

    hide allan
    hide alex
    hide jessy
    hide ilona
    hide theo
    with dissolve

    play sound audio.footSand 
    scene bg arc2 group parasol
    with fade
    show jessy embarrassed at char_left
    show allan neutral at char_midleft
    show ilona neutral at char_center
    show theo neutral at char_right

    systeme "Plus tard, Ilona revient du stand de kakigōri avec la gelée marine lumineuse qu'elle avait repérée."
    systeme "Allan distribue aussi les boissons avec l'air de quelqu'un qui a accepté une mission trop collante."
    a "Tu l'as vraiment prise, la gelée radioactive ?"
    i "Oui. Et je voulais aller voir les petites mares vers—"
    t "Les rochers, oui. C'est plus simple par la jetée."
    systeme "Théo coupe Ilona pour la deuxième fois aujourd'hui. Mais cette fois, Allan le voit."
    show allan doubt at char_midleft
    a "Attends. Elle parlait encore."
    t "Je sais. Désolé. Je voulais juste—"
    a "Oui. Je sais ce que tu voulais. Ralentis."
    systeme "Allan dit ça sans agressivité, mais le message est clair."
    systeme "Théo hoche la tête. Il sourit même. Mais son sourire ne monte pas jusqu'aux yeux."
    t "T'as raison. Pardon, Ilona."
    i "C'est bon."
    systeme "Elle dit ça vite. Trop vite. Comme si elle voulait que la tension disparaisse avant que ça devienne un problème."
    hide allan
    with dissolve

    play sound audio.footSand 
    # music plage soir
    play music "music/plage-sunset.mp3" fadeout 1.0 fadein 0.5 loop
    play ambiant1 "ambience/ocean-waves.mp3" volume 0.8 loop fadein 3.0
    scene bg arc2 tide pools
    with fade
    show jessy embarrassed at char_left
    show ilona neutral at char_center
    show theo neutral at char_right

    systeme "Le groupe s'est rapproché des rochers, mais personne n'a encore bougé plus loin."
    systeme "Ilona tient son gobelet lumineux d'une main et son porte-clés bloc de l'autre. Elle regarde les mares, puis Théo."
    i "Je veux vraiment aller voir."
    t "La jetée contourne les rochers glissants. Je peux te montrer."
    systeme "Il ne demande pas. Il propose comme si c'était déjà décidé."
    systeme "Jessy voit Ilona hésiter. Pas longtemps. Juste assez pour que ce soit visible."
    i "Jessy ?"
    systeme "Elle le regarde. Pas pour demander la permission. Pour vérifier s'il va exploser ou se taire."
    if jalousie >= 2:
        systeme "Depuis le porte-clés, la photo, les regards, Jessy sent que quelque chose est en train de lui échapper."
    elif jalousie == 1:
        systeme "Jessy a déjà ressenti cette pointe aujourd'hui. Elle revient, plus aiguë."
    else:
        systeme "Jessy ne pensait pas que ça ferait aussi mal."
    i "Je peux y aller ?"
    systeme "La question est simple. Trop simple. Comme si elle testait jusqu'où Jessy allait se laisser ronger."

    menu:
        "Ilona attend. Théo aussi. Comment Jessy gère-t-il ?"

        "Dire qu'il a besoin de dix minutes pour respirer.":
            play music audio.sadPiano fadeout 0.5 fadein 2.0 loop
            $ arc2_choix_activite_theo = "dix_minutes"
            $ lien_jessy_ilona += 1
            $ jalousie += 1
            $ communication += 2
            $ confiance += 1
            $ remember("jessy_nomme_sa_peur")
            j "Ça me met mal à l'aise."
            i "Pourquoi ?"
            j "Parce que j'ai peur."
            systeme "Ilona cligne des yeux. Elle ne s'attendait pas à ça."
            i "De quoi ?"
            j "Que tu reviennes différente. Ou que tu reviennes pas du tout."
            t "Je ramène pas les gens dans une autre dimension."
            j "Je sais. Mais j'ai quand même peur."
            systeme "Théo hausse un sourcil. Ilona soupire."
            i "D'accord. Je reviens dans dix minutes. Chronomètre-moi si tu veux."
            j "Non. Prends ton temps. J'avais juste besoin de le dire."

        "Partir sans répondre.":
            $ arc2_choix_activite_theo = "disparaitre"
            $ jalousie += 2
            $ communication -= 2
            $ influence_theo += 1
            j "Faites ce que vous voulez."
            play music audio.sadPiano fadeout 1.0 fadein 2.0 loop
            i "Jessy—"
            systeme "Il est déjà parti. Il entend son prénom, mais il continue de marcher."
            systeme "Derrière lui, il entend Théo murmurer quelque chose à Ilona. Puis leurs pas s'éloignent dans l'autre direction."

        "Lui faire confiance et proposer d'en parler au retour.":
            $ arc2_choix_activite_theo = "confiance"
            $ lien_jessy_ilona += 1
            $ confiance += 2
            $ autonomie_ilona += 2
            $ communication += 1
            $ remember("ilona_libre_sans_abandon")
            j "Vas-y."
            systeme "Ilona attend la suite. Il n'y en a pas."
            i "C'est tout ?"
            j "Oui. Amuse-toi bien."
            systeme "Elle le regarde comme si elle cherchait le piège. Il n'y en a pas."
            i "... Merci."
            j "Tu me raconteras au retour ?"
            i "Oui."
            systeme "Théo ne dit rien. Il se lève, attend Ilona, et ils partent."
            systeme "Jessy les regarde s'éloigner. Il serre les poings, mais il ne bouge pas."

        "Cacher sa jalousie derrière une blague.":
            $ arc2_choix_activite_theo = "blague_jalouse"
            $ jalousie += 2
            $ lien_jessy_ilona -= 1
            j "Ouais, vas-y. Je vais surveiller le sable."
            i "Jessy."
            j "Quoi ? C'était une blague."
            i "Non. C'était une pique."
            systeme "Théo se lève sans attendre."
            t "On y va ?"
            i "Oui."
            play music audio.sadPiano fadeout 1.0 fadein 2.0 loop
            systeme "Elle ne regarde même pas Jessy en partant."

        "Dire oui, puis les suivre discrètement.":
            $ arc2_choix_activite_theo = "suivre"
            $ jalousie += 3
            $ confiance -= 2
            $ autonomie_ilona -= 2
            $ influence_theo += 1
            $ interruptions_ilona += 1
            j "Oui. Vas-y."
            i "T'es sûr ?"
            j "Oui."
            systeme "Ilona s'éloigne avec Théo. Jessy reste près des serviettes."
            systeme "Puis il se lève. Il les suit à distance."
            systeme "Il se dit qu'il veut juste voir. Juste vérifier."
            systeme "Ilona tourne la tête. Elle le voit."
            show ilona frustrated at char_center
            stop music
            play sound "fx/piano-slam.mp3"
            i "Sérieusement ?"
            systeme "Théo s'arrête. Il regarde Jessy avec quelque chose entre la pitié et le mépris."
            t "Tu voulais venir ou tu voulais surveiller ?"
            systeme "Jessy ouvre la bouche. Rien ne sort."

    if arc2_choix_activite_theo == "confiance":
        hide ilona
        hide theo
        with dissolve
        play music audio.sadPiano fadeout 1.0 fadein 1.0 loop volume 1.0
        show alex concerned at char_midright
        x "Tu respires comme quelqu'un qui vient de poser un bloc au-dessus du vide."
        j "C'est à peu près ça."
        x "Alors ne saute pas dessus pour vérifier s'il tient."
        hide alex
        with dissolve
    elif arc2_choix_activite_theo == "dix_minutes":
        hide ilona
        hide theo
        with dissolve
        show alex concerned at char_midright
        x "Dix minutes, c'est vraiment dix minutes ?"
        j "Oui."
        x "Alors reviens avant que ton absence devienne une phrase."
        hide alex
        with dissolve
    elif arc2_choix_activite_theo == "blague_jalouse":
        hide ilona
        hide theo
        with dissolve
        show alex concerned at char_midright
        x "Elle a compris que c'était une blague."
        j "Alors ça va ?"
        x "Non. Comprendre une blague, ce n'est pas toujours la recevoir légèrement."
        hide alex
        with dissolve

    hide jessy
    hide ilona
    hide theo
    with dissolve

    if arc2_choix_activite_theo in ("confiance", "dix_minutes", "blague_jalouse"):
        #ambiance vague
        play sound audio.footSand 
        scene bg arc2 jetty
        with fade
        show ilona neutral at char_left
        show theo reassuring at char_right

        systeme "Près de la jetée, Ilona s'arrête devant les mares entre les rochers."
        systeme "L'eau brille. Le silence entre eux est confortable. Trop confortable."
        i "C'est beau."
        t "Oui."
        $ renpy.pause(1.5)
        systeme "Théo la regarde regarder l'eau. Pas les mares. Elle."
        t "Tu sais, je t'ai coupée tout à l'heure."
        i "Oui."
        t "Pardon."
        systeme "Il dit ça simplement. Comme s'il savait exactement quoi dire pour qu'elle se sente écoutée."
        i "C'est pas grave."
        t "Si. Je fais ça trop souvent. Je crois savoir ce que les gens veulent avant qu'ils finissent."
        systeme "Il marque une pause. Puis il sourit, comme s'il venait de se dévoiler."
        t "Avec toi, j'aimerais juste... écouter."
        systeme "Ilona rougit. Elle détourne les yeux vers l'eau."

        if arc2_choix_activite_theo == "blague_jalouse":
            systeme "Elle pense à Jessy. À sa blague qui sonnait faux. À la tension avant de partir."
            i "Jessy était bizarre."
            t "Il a peur."
            i "De quoi ?"
            t "De moi, probablement."
            systeme "Théo dit ça sans sourire. Juste comme un fait."
            i "Pourquoi il aurait peur de toi ?"
            t "Parce qu'il sait que je te comprends."
            systeme "Ilona ouvre la bouche. Puis la referme."
            systeme "Théo vient de dire tout haut ce qu'elle pensait tout bas."
        else:
            systeme "Théo se rapproche. Pas beaucoup. Juste assez."
            t "Je pense que Jessy a de la chance."
            i "Pourquoi tu dis ça ?"
            t "Parce que t'es le genre de personne qu'on remarque pas tout de suite. Mais une fois qu'on te voit vraiment..."
            systeme "Il laisse la phrase en suspens. Comme un cadeau à moitié déballé."
            i "..."
            systeme "Ilona ne sait pas quoi répondre. Alors elle ne répond pas."
            systeme "Le silence qui suit n'est pas vide. Il est lourd de possibilités."

        $ renpy.pause(2.0)
        $ lien_ilona_theo += 2

        if autonomie_ilona >= 3:
            $ renpy.pause(1.0)
            show ilona determined at char_left
            i "Je vais y retourner."
            t "Maintenant ?"
            i "Oui. Avant que ce moment devienne... autre chose."
            systeme "Théo hoche la tête. Il ne force rien. Il sait exactement ce qu'il vient de planter."
            t "D'accord."
        else:
            systeme "Ilona reste encore quelques secondes. Elle sait qu'elle devrait partir."
            systeme "Mais une partie d'elle ne veut pas."
            $ renpy.pause(1.5)
            i "On devrait y retourner."
            t "Oui."
            systeme "Ils y retournent. Mais quelque chose a changé."

        hide theo
        with dissolve

    elif arc2_choix_activite_theo == "suivre":
        scene bg arc2 tide pools
        with fade
        show ilona frustrated at char_left
        show jessy embarrassed at char_center
        show theo neutral at char_right

        stop ambiant1 fadeout 0.3
        play music audio.tensePiano loop fadeout 0.3 fadein 3.0 volume 0.6
        systeme "Après avoir remarqué Jessy derrière eux, plus personne ne parle."
        i "Pourquoi tu m'as suivie ?"
        j "Je... je voulais juste—"
        i "Me surveiller ?"
        j "Non ! Je—"
        t "Tu voulais vérifier qu'il se passait rien."
        systeme "Théo dit ça calmement. Trop calmement."
        j "Ferme-la."
        with hpunch
        t "Je dis juste ce que tu penses."
        j "T'en sais rien de ce que je pense."
        t "Alors pourquoi t'es là ?"
        systeme "Jessy ne répond pas. Parce qu'il n'a pas de bonne réponse."
        show ilona frustrated at char_left
        i "Je voulais marcher. Pas passer un test de fidélité."
        j "C'était pas ça—"
        i "Alors c'était quoi ?"
        systeme "Jessy ouvre la bouche. Rien ne sort."
        i "Je rentre."
        systeme "Elle part. Théo reste une seconde, regarde Jessy, puis secoue la tête."
        t "T'as tout gâché, mec."
        stop music fadeout 4.0
        systeme "Puis il part aussi."
        hide theo
        hide ilona
        with dissolve
        systeme "Jessy reste seul face aux rochers."

    else:
        scene bg arc2 beach sunset
        with fade
        show ilona fatigue at char_left
        show theo neutral at char_right

        systeme "Jessy est parti sans répondre. Ilona reste là, son gobelet à la main."
        t "Il a juste peur."
        i "De quoi ?"
        t "De te perdre."
        i "En me laissant voir des mares ?"
        t "Non. En te laissant exister sans lui."
        systeme "Ilona serre son gobelet. La gelée commence à fondre."
        i "C'est con."
        t "Oui."
        systeme "Théo s'assoit sur un rocher. Il regarde l'horizon comme s'il avait tout le temps du monde."
        t "Tu veux toujours aller voir les mares ?"
        systeme "Ilona hésite. Elle pense à Jessy. Puis elle pense à elle."
        i "Oui."
        t "Alors allons-y."
        hide ilona
        hide theo
        with dissolve
        systeme "Ils marchent vers les rochers. Derrière eux, le soleil descend sur une journée qui ne finira pas comme elle a commencé."

    play sound audio.footSand 
    play music "music/plage-sunset.mp3" fadeout 1.0 fadein 0.5 loop
    scene bg arc2 lost items table
    with fade
    show ilona neutral at char_left

    $ renpy.pause(0.5, hard=True)
    play sound "fx/re-zero-return.mp3" volume 0.6
    show laplage neutral at char_center
    with dissolve
    $ arc2_scene_laplage = True
    $ jugement_laplage += 1

    systeme "Sur le chemin du retour, une petite table est installée près de la jetée. Un panneau penché indique : OBJETS TROUVÉS."
    i "Vous travaillez ici ?"
    laplage "Je remplace quelqu'un qui n'était pas prévu."
    i "Donc non."
    laplage "Aujourd'hui, ça veut dire parasol."
    systeme "Ilona regarde la table. Deux sandales dépareillées, un chapeau, une serviette oubliée."
    i "Les gens oublient beaucoup de choses."
    laplage "Oui. Surtout ce qu'ils croyaient devoir garder."
    i "Vous rendez tout ce qu'on vous apporte ?"
    laplage "Seulement ce qu'on me demande."
    show laplage thumb_up at char_center
    laplage "Parfois, on rend un objet trop vite. Avant que la personne sache si elle en a encore besoin."
    i "Et si elle ne sait pas ?"
    laplage "Alors elle revient quand elle saura."
    systeme "Ilona hésite."
    i "Et si elle ne revient pas ?"
    laplage "Alors l'objet reste là. Personne ne le force."
    show laplage neutral at char_center
    systeme "Monsieur Laplage pose une main sur le parasol, comme s'il s'apprêtait à le ranger."
    i "La plage est calme, aujourd'hui."
    laplage "Oui, elle est sèche aussi."
    i "C'est une observation météo ou une phrase de Monsieur Laplage ?"
    laplage "Les deux, les bons jours."
    i "Une plage sèche, c'est pas juste... normal ?"
    laplage "Pas toujours."
    systeme "Ilona regarde le sable collé à ses sandales, puis souffle un rire discret."
    show ilona smile at char_left
    i "La plage est sèche."
    show laplage thumb_up at char_center
    laplage "Exactement."

    hide laplage
    with dissolve

    systeme "Ilona reste encore quelques secondes devant la table. Rien n'a été résolu, mais la question a cessé de courir."

    show allan neutral at char_midright
    with dissolve
    a "Je t'ai retrouvée."
    i "J'étais pas perdue."
    a "Je sais. Alexandre, par contre, a perdu une pelle en plastique."

    show alex grin at char_right
    with dissolve
    x "Faux. Elle menait une vie indépendante derrière les serviettes."
    i "C'est important de respecter les vocations."
    x "Merci. Enfin quelqu'un de raisonnable."

    show allan doubt at char_midright
    a "Ça va ?"
    a "Sur une échelle de \"tranquille\" à \"je jette la gelée à la mer\" ?"
    i "Je garde la gelée."
    i "Donc plutôt tranquille."
    i "Mais disons que je la tiens plus fermement qu'au début de la journée."
    a "Niveau intermédiaire sérieux."
    i "Voilà."
    i "Théo a répondu trop vite, tout à l'heure."
    a "Je sais. Je lui ai dit de ralentir."
    i "J'ai remarqué."
    a "Il veut aider. Mais des fois, il oublie que c'est pas une course."
    i "C'est pas dramatique."
    i "J'aimerais juste finir mes phrases avant qu'on trouve une solution pour moi."
    a "Je comprends."
    $ renpy.pause(0.5)
    a "Tu veux que j'en reparle avec lui ?"
    i "Non. Pas comme un reproche."
    i "S'il le remarque, ou si je le dis moi-même, ça suffit."
    show alex concerned at char_right
    x "Donc on ne monte pas un comité d'urgence autour d'une phrase coupée ?"
    i "S'il vous plaît, non."
    a "D'accord. Pas de comité."
    show alex grin at char_right
    x "Dommage. J'avais un titre : Commission temporaire des phrases inachevées."
    i "Refusé."
    x "Je respecte la décision administrative."
    show allan neutral at char_midright
    a "Tu reviens ?"
    i "Oui. Dans une minute."
    a "On garde une place sans panneau."
    i "Merci."
    hide allan
    hide alex
    with dissolve

    systeme "Quand elle revient vers les serviettes, le soleil est plus bas. Le groupe parle moins fort qu'au début de la journée."

    hide ilona
    with dissolve
    play sound audio.footSand 

    scene bg arc2 beach sunset
    with fade
    show jessy embarrassed at char_left
    show ilona neutral at char_center
    show alex concerned at char_midleft

    if arc2_choix_activite_theo == "disparaitre":
        play music audio.sadPiano loop fadeout 1.0 fadein 1.0
        x "Tu es parti sans rien dire."
        j "Je pouvais pas rester."
        x "Alors tu l'as laissée partir avec lui."
        j "Qu'est-ce que je devais faire ? Les suivre ? Lui interdire ?"
        x "Lui parler, peut-être ?"
        systeme "Jessy se tait. Alexandre a raison, et ça fait encore plus mal."
    elif arc2_choix_activite_theo == "suivre":
        play music audio.sadPiano loop fadeout 1.0 fadein 1.0
        x "T'as vérifié au lieu de faire confiance."
        j "Je sais."
        x "Elle va pas te pardonner ça facilement."
        j "Je sais."
        x "Alors pourquoi t'as fait ça ?"
        j "Parce que j'ai paniqué, bordel !"
        with hpunch
        systeme "Alexandre recule d'un pas. Jessy vient de crier."
    else:
        x "Allan est convaincu que Monsieur Laplage possède légalement le sable."
        j "Quoi ?"
        x "Il a dessiné un schéma avec une frite."
        systeme "La blague crée un peu d'air. Pas beaucoup."

    hide alex
    if arc2_choix_activite_theo == "confiance":
        show ilona smile at char_right
    elif arc2_choix_activite_theo == "dix_minutes":
        show ilona neutral at char_right
    else:
        show ilona frustrated at char_right
    with dissolve

    if arc2_choix_activite_theo == "confiance":
        i "J'ai vu un coquillage bizarre."
        j "C'était comment ?"
        i "Inutile. Comme nos portes."
        systeme "Elle sourit. Jessy aussi. Mais son sourire tremble un peu."
        systeme "Parce qu'il sait que quelque chose s'est passé là-bas. Il le voit dans ses yeux."
    elif arc2_choix_activite_theo == "dix_minutes":
        j "Je suis revenu."
        i "Oui."
        j "Ça va ?"
        i "Oui. Et toi ?"
        j "Non. Mais je voulais pas te laisser partir en colère."
        systeme "Ilona hoche la tête. Elle ne sourit pas. Elle ne se fâche pas non plus."
        i "Théo m'a dit que tu avais peur."
        j "Il a dit ça ?"
        i "Oui. Il avait raison ?"
        systeme "Jessy ne sait pas s'il doit remercier Théo ou le détester."
        j "Oui."
    elif arc2_choix_activite_theo in ("disparaitre", "suivre"):
        systeme "Ilona pose son sac. Elle ne le regarde pas."
        i "Tu pouvais juste me faire confiance."
        if arc2_choix_activite_theo == "suivre":
            i "Ou me dire que t'avais peur. Mais me suivre comme ça..."
        else:
            i "Ou me dire que t'avais peur. Mais partir comme ça..."
        systeme "Elle secoue la tête."
        i "T'as choisi la pire option."
        j "Je sais."
        i "Alors pourquoi ?"
        j "Parce que je suis con. Parce que j'avais peur. Parce que—"
        i "Stop."
        systeme "Elle lève la main."
        i "J'ai pas envie d'entendre des excuses maintenant."
        systeme "Jessy ferme la bouche. Le silence qui suit fait plus mal que n'importe quelle dispute."
    else:
        systeme "Ilona sourit, mais c'est un sourire fatigué."
        i "Les mares étaient belles."
        j "Tant mieux."
        i "Théo a été... gentil."
        systeme "Le mot reste suspendu entre eux comme une accusation."

    menu:
        "Le coucher de soleil commence. Que fait Jessy ?"

        "Se taire trop longtemps.":
            $ communication -= 2
            $ pression_stream += 1
            show ilona fatigue at char_right
            systeme "Jessy ouvre la bouche. Rien ne sort."
            systeme "Ilona attend. Cinq secondes. Dix. Vingt."
            i "T'as rien à dire ?"
            systeme "Jessy secoue la tête."
            i "Parfait."
            systeme "Elle se lève et part vers les serviettes."
            systeme "Le silence n'est pas violent. Mais il tue quand même quelque chose."

        "Demander ce qui s'est passé avec Théo.":
            $ jalousie += 2
            $ communication -= 1
            $ autonomie_ilona -= 1
            show jessy embarrassed at char_left
            j "Il s'est passé quelque chose ?"
            i "Quoi ?"
            j "Avec Théo. Il s'est passé quelque chose ?"
            show ilona frustrated at char_right
            i "Tu me demandes si j'ai trompé en allant voir des mares ?"
            j "Non ! Je—"
            i "Parce que ça ressemble beaucoup à ça."
            j "Je veux juste savoir—"
            i "Si je suis restée fidèle ? Si j'ai résisté à la tentation ?"
            systeme "Elle crache les mots comme du venin."
            i "Va te faire foutre, Jessy."
            with hpunch

        "Reconnaître précisément son erreur.":
            $ communication += 2
            $ autonomie_ilona += 1
            $ confiance += 1
            if arc2_choix_activite_theo in ("blague_jalouse", "suivre", "disparaitre"):
                $ remember("jessy_repare")
            if interruptions_ilona > interruptions_reconnues:
                $ interruptions_reconnues += 1
                $ interruptions_reparees += 1
            $ renpy.pause(1.2)
            show jessy listening at char_left
            if arc2_choix_activite_theo == "confiance":
                j "Merci d'être partie sans avoir à te justifier."
                $ renpy.pause(0.8)
                j "Je veux que ce soit normal. Que tu aies des moments à toi."
                systeme "Ilona le regarde. Quelque chose dans son regard change."
                i "Ça m'a fait du bien."
                systeme "Elle dit ça simplement. Mais Jessy entend ce qu'elle ne dit pas : Théo aussi lui a fait du bien."
            elif arc2_choix_activite_theo == "dix_minutes":
                j "Merci d'avoir attendu que je revienne."
                $ renpy.pause(0.8)
                j "Je suis parti pour pas te blesser. Mais je sais que revenir, c'était important."
                i "Oui. Ça l'était."
            elif arc2_choix_activite_theo == "blague_jalouse":
                j "Désolé pour ma blague de merde."
                $ renpy.pause(0.8)
                j "Je l'ai lancée pour cacher que j'avais peur. C'était lâche."
                i "Oui."
                systeme "Elle ne dit rien de plus. Mais elle ne part pas non plus."
            elif arc2_choix_activite_theo == "suivre":
                j "Désolé de t'avoir suivie."
                $ renpy.pause(0.8)
                j "J'ai vérifié au lieu de te faire confiance. C'était... pathétique."
                i "Oui. Ça l'était."
                systeme "Le mot fait mal. Mais Jessy l'a mérité."
            else:
                j "Désolé d'être parti sans rien dire."
                $ renpy.pause(0.8)
                j "Je t'ai laissée deviner ma peur alors que c'était à moi de la nommer."
                i "..."
                systeme "Elle ne répond pas tout de suite. Puis elle soupire."
                i "T'as de la chance que je sois fatiguée."

        "Nommer sa peur sans accuser.":
            $ communication += 2
            $ confiance += 1
            $ remember("jessy_nomme_sa_peur")
            $ renpy.pause(1.0)
            show jessy embarrassed at char_left
            j "J'ai eu peur."
            $ renpy.pause(0.6)
            j "Pas parce que t'as fait quelque chose de mal. Parce que je me suis senti remplaçable."
            systeme "Ilona cligne des yeux."
            i "Remplaçable ?"
            j "Théo a retrouvé ton porte-clés. Il savait où tu préfères t'asseoir. Il connaît le chemin vers les mares."
            j "Et moi je fouillais dans le sable au mauvais endroit."
            $ renpy.pause(0.8)
            show ilona neutral at char_right
            i "Tu penses que je vais te remplacer parce qu'il est plus attentif ?"
            j "Je... je sais pas. Peut-être."
            i "Jessy."
            systeme "Elle dit son nom comme une remise à l'ordre."
            i "Si je voulais être avec Théo, je serais avec Théo."
            systeme "Le silence qui suit est lourd. Parce qu'elle vient de dire qu'elle pourrait."

    if arc2_scene_laplage:
        systeme "Au loin, la table des objets trouvés ferme à la tombée du jour."
        systeme "Certaines choses se retrouvent. D'autres restent perdues un peu plus longtemps."

    hide jessy
    hide ilona
    with dissolve

    stop ambiant1 fadeout 1.0
    play music audio.mcnight volume 0.8 fadeout 1.0
    scene bg arc2 minecraft house summer night
    with Dissolve(2.0)
    show jessy minecraft at char_left
    show ilona minecraft at char_right

    systeme "Le soir, la maison Minecraft les attend."
    systeme "Ilona ouvre l'inventaire. Elle cherche des blocs qui brillent."
    systeme "Le gobelet de gelée marine est toujours là, sur le bureau d'Ilona, à moitié vide."
    $ renpy.pause(1.0)

    if arc2_choix_activite_theo in ("confiance", "dix_minutes"):
        if communication >= 4:
            $ arc2_retour_minecraft = "sortie_couloir"
            i "Je vais ajouter une sortie au couloir sans issue."
            j "Il sera plus sans issue, alors."
            i "C'est le but."
            $ renpy.pause(0.8)
            i "Comme ça, si quelqu'un a besoin de marcher, il peut revenir."
            systeme "Jessy hoche la tête. Il comprend le message."
            $ lien_jessy_ilona += 1
            $ confiance += 1
        else:
            $ arc2_retour_minecraft = "lanterne_bleue"
            i "Je pose une lanterne bleue dans la cuisine d'été."
            j "Pourquoi bleue ?"
            i "Parce que j'en ai envie."
            systeme "Le ton est sec. Jessy ne pose pas d'autre question."
    elif arc2_choix_activite_theo in ("suivre", "disparaitre"):
        $ arc2_retour_minecraft = "porte_fermee"
        systeme "Ilona se connecte. Elle regarde la maison."
        systeme "Puis elle construit un mur devant la porte d'entrée."
        j "Qu'est-ce que tu fais ?"
        i "Je ferme."
        j "Pourquoi ?"
        i "Parce que j'en ai besoin."
        systeme "Jessy essaie d'ouvrir. La porte est bloquée."
        systeme "Il reste dehors. Elle reste dedans."
        $ pression_stream += 2
        $ lien_jessy_ilona -= 1
    else:
        $ arc2_retour_minecraft = "silence"
        systeme "Ilona se connecte, mais elle ne construit rien."
        systeme "Elle marche juste dans les couloirs. Seule."
        $ renpy.pause(2.0)
        systeme "Jessy la suit à distance dans le jeu. Il n'ose pas s'approcher."
        $ pression_stream += 1

    menu:
        "Dans le jeu, Ilona place un bloc lumineux bleu dans l'inventaire."

        "Poser bloc lumineux dehors sans rien dire.":
            $ renpy.pause(1.0)
            systeme "Ilona place un seul bloc lumineux devant l'entrée."
            if arc2_choix_activite_theo in ("confiance", "dix_minutes"):
                j "C'est joli."
                i "Merci."
                systeme "Jessy ne demande pas pourquoi. Il comprend que ce n'est pas une décoration."
            else:
                systeme "Jessy regarde le bloc. Il ne dit rien."
                systeme "Ilona non plus."

        "Construire une version gelée lumineux dans salle secrète.":
            if arc2_choix_activite_theo not in ("suivre", "disparaitre"):
                $ remember("maison_respectee")
                $ lien_jessy_ilona += 1
                $ ilonanium_points += 1
                j "On en fait une version Minecraft dans la salle moyennement importante ?"
                i "Très bon niveau d'importance."
                systeme "Ils construisent ensemble. Pas parfaitement. Mais ensemble quand même."
            else:
                j "On pourrait—"
                i "Non."
                systeme "Jessy referme la bouche. Il a compris."

    if arc2_choix_activite_theo in ("suivre", "disparaitre"):
        systeme "L'été ne répare rien."
        systeme "Il laisse une photo, quelques mots de Théo qui résonnent encore, et une fissure dans la maison Minecraft."
        systeme "Le sable dans les chaussures ne partira pas facilement non plus."
    elif jalousie >= 3:
        systeme "L'été ne tranche rien."
        systeme "Il laisse une photo, un porte-clés retrouvé par quelqu'un d'autre, et une question qui n'a pas de réponse simple."
        systeme "Théo reste dans l'air comme du sel sur la peau."
    else:
        systeme "L'été laisse une photo, une promenade vers les mares, et la certitude que la confiance se construit pas à pas."
        systeme "Même quand ça fait peur."
    stop music fadeout 1.0
    stop ambiant1 fadeout 1.0
    jump arc_3_rentree
