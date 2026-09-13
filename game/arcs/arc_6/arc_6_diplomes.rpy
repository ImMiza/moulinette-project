# ARC VI - REMISE DES DIPLÔMES : « APRÈS AUJOURD'HUI »
default arc6_stylo = ""                   # rendu / garde / rendu_explique / blague
default arc6_offre_theo = ""              # laisse / question / accusation / aveu_vide
default arc6_ilona_a_pleure = False
default arc6_gateau_planete = False
default arc6_conversation = ""            # continuer / que_veux_tu / eviter / partir / aveu_interruptions
default arc6_derniere_construction = ""   # porte_ouverte / panneau_partir / silence / cadenas
default arc6_vignettes_jouees = []
default arc6_vignettes_count = 0
default arc6_flashback = False            # au moins une vignette à jouer en flashback
default arc6_theo_attaques = []
default arc6_attaque_1 = ""
default arc6_attaque_2 = ""
default arc6_attaque_3 = ""

default arc6_score = 0
default arc6_route = ""

default arc6_penchant_debut = ""
default arc6_penchant = ""            # ton initial herite des arcs I-V
default arc6_derive = 0               # conserve pour compatibilite avec les sauvegardes

init -5 python:
    ORDRE_PENCHANT = {"theo": 0, "indecis": 1, "jessy": 2}

    def arc6_penche():
        """Traduit etat_relation() en penchant narratif. Aucune metrique nouvelle."""
        etat = etat_relation()
        if etat == "proche":
            return "jessy"
        if etat == "fragile":
            return "indecis"
        return "theo"

    def arc6_palier():
        """Fixe le ton initial herite des arcs I-V."""
        p = arc6_penche()
        if not store.arc6_penchant_debut:
            store.arc6_penchant_debut = p
        store.arc6_penchant = p
        store.arc6_derive = 0
        return p

    def arc6_calcule_verdict():
        """Calcule une seule fois le verdict herite des arcs I-V."""
        s = store
        controle_repetitif = s.interruptions_ilona - s.interruptions_reparees

        espace = (
            s.autonomie_ilona * 4
            + s.ilona_peut_finir_ses_phrases * 6
            + s.interruptions_reparees * 6
            + s.communication
            + s.confiance
        )
        dette = (
            s.influence_theo * 3
            + max(0, controle_repetitif) * 8
            + s.pression_stream * 2
            + s.jalousie * 2
            + s.confidences_laplage * 4
        )
        posture = (
            6 * s.souvenirs["jessy_nomme_sa_peur"]
            + 8 * s.souvenirs["jessy_repare"]
            + 5 * s.souvenirs["ilona_libre_sans_abandon"]
            + 3 * s.souvenirs["maison_respectee"]
            - 6 * s.souvenirs["theo_utilise_une_verite"]
        )
        recidive = -6 * max(0, s.controles - 2) - 3 * max(0, s.evitements - 3)

        s.arc6_score = espace + posture + recidive - dette

        if s.interruptions_reparees >= 2 and s.souvenirs["jessy_repare"]:
            s.arc6_score += 20

        if controle_repetitif >= 3:
            s.arc6_route = "theo"
        elif s.arc6_score >= s.SEUIL_JESSY:
            s.arc6_route = "jessy"
        else:
            s.arc6_route = "theo"

        return s.arc6_route

    def arc6_construit_attaques_theo():
        """Liste ce que Théo peut reprocher sans devenir omniscient."""
        s = store
        attaques = []

        def add(phrase):
            if len(attaques) < 3:
                attaques.append(phrase)

        if s.arc2_choix_activite_theo == "suivre":
            add("À la plage, tu lui as dit oui, puis tu l'as suivie pour vérifier ce qui se passait avec moi.")
        elif s.arc2_choix_activite_theo == "disparaitre":
            add("À la plage, tu es parti sans répondre. Elle a dû finir ta phrase toute seule.")
        elif s.arc2_choix_activite_theo == "blague_jalouse":
            add("À la plage, tu as appelé ça une blague. Elle a entendu une pique.")

        if s.arc3_reaction_rumeur == "silence_paralysie":
            add("Au festival, elle a attendu que tu sois là. Tu as regardé les menus.")
        elif s.arc3_reaction_rumeur == "defendre_immediat":
            add("Au festival, tu l'as défendue avant de lui demander si elle voulait être défendue.")

        if s.arc3_aide_stand == "blague_defense":
            add("Au stand, tu as fait rire en prenant pour cible quelqu'un qui ne pouvait pas répondre.")
        elif s.arc3_aide_stand == "demande_directe":
            add("Au stand, tu lui as demandé de te rassurer au milieu de tout le monde.")

        if s.arc4_ilona_avec_theo and s.arc4_limite_ilona == "demande_theo":
            add("À Noël, elle est venue marcher avec moi parce qu'elle avait besoin de parler à quelqu'un qui ne lui demandait pas de le rassurer.")

        if s.arc5_theo_proposition == "laisse":
            add("Quand je t'ai dit que je pouvais gérer, tu as laissé son projet changer de mains sans qu'elle soit dans la pièce.")
        elif s.arc5_theo_proposition == "partiel":
            add("Quand je t'ai proposé d'organiser une partie de sa vie, tu as négocié avec moi avant de lui demander à elle.")

        return attaques

# Assets propres à l'arc 6 : gymnase de cérémonie, classe du matin,
# classe décorée de fin d'année.
# arc6_bg() prend l'asset arc_6 s'il existe, sinon le secours indique.
# fit="cover" recadre sans déformer, contrairement à im.Scale.
init -5 python:
    def arc6_bg(nom, secours):
        chemin = "images/scenes/arc_6/bg_arc6_{}.jpg".format(nom)
        if not renpy.loadable(chemin):
            chemin = secours
        return Transform(chemin, fit="cover", xysize=(1920, 1080), align=(0.5, 0.5))

    def arc6_flashbg(chemin):
        return Transform(chemin, fit="cover", xysize=(1920, 1080), align=(0.5, 0.5))

image bg arc6 classroom morning = arc6_bg("classroom_morning", "images/scenes/arc_5/bg_arc5_classroom.jpg")
image bg arc6 gym ceremony = arc6_bg("gym_ceremony", "images/scenes/arc_1/bg_arc1_school_cafeteria.jpg")
image bg arc6 corridor empty = arc6_bg("corridor_empty", "images/scenes/shared/bg_shared_school_corridor.jpg")
image bg arc6 classroom festive = arc6_bg("classroom_festive", "images/scenes/arc_3/bg_arc3_classroom_evening.jpg")
image bg arc6 courtyard march = arc6_bg("courtyard_march", "images/scenes/arc_5/bg_arc5_park_spring.jpg")
image bg arc6 rooftop dusk = arc6_bg("rooftop_dusk", "images/scenes/arc_5/bg_arc5_rooftop.jpg")
image bg arc6 minecraft last = arc6_bg("minecraft_last", "images/scenes/arc_2/bg_arc2_minecraft_house_summer_night.jpg")

# Backgrounds de flashback réutilisés tels quels par la scène 3.
image bg arc6 flash beach = arc6_flashbg("images/scenes/arc_2/bg_arc2_beach_sunset.jpg")
image bg arc6 flash festival = arc6_flashbg("images/scenes/arc_3/bg_arc3_festival_hallway.jpg")
image bg arc6 flash minecraft = arc6_flashbg("images/scenes/arc_2/bg_arc2_minecraft_house_summer_night.jpg")
image bg arc6 flash market = arc6_flashbg("images/scenes/arc_4/bg_arc4_christmas_market.jpg")
image bg arc6 flash bench = arc6_flashbg("images/scenes/arc_4/bg_arc4_park_bench.jpg")
image bg arc6 flash cinema = arc6_flashbg("images/scenes/arc_5/bg_arc5_cinema_seated.jpg")
image bg arc6 flash station = arc6_flashbg("images/scenes/arc_5/bg_arc5_train_station.jpg")

# SCÈNE 1 : LE STYLO VIOLET

label arc_6_diplomes:

    $ arc6_palier()
    $ arc6_calcule_verdict()

    play music audio.mornPiano fadein 2.0 loop volume 0.7
    scene bg arc6 classroom morning
    with fade

    

    systeme "Arc VI : le jour où l'école s'arrête."
    systeme "Fin mars. Les cerisiers de la cour ne sont pas encore ouverts. Ils ont l'air de retenir quelque chose."

    show jessy neutral at char_center
    with dissolve

    systeme "Jessy arrive une heure trop tôt. La salle est vide. Les tables sont alignées comme si personne n'avait jamais rien écrit dessus."

    j "J'ai un stylo violet dans la poche depuis le 12 janvier."
    j "Au début c'était : je lui rends demain."
    j "Après c'était : ça va faire bizarre de lui rendre maintenant."
    j "Depuis février c'est : je crois que je l'ai gardé exprès."

    $ renpy.pause(0.8, hard=True)

    show jessy neutral at char_left
    show ilona neutral at char_midright
    with dissolve

    systeme "Ilona entre. Elle mange un pain au lait. Elle mange toujours quand quelque chose va commencer."

    i "T'es là depuis quand ?"
    j "Sept heures cinquante."
    i "La cérémonie est à dix heures."
    j "Je sais."

    show ilona neutral at char_midright
    with dissolve

    if arc6_penchant == "jessy":
        i "D'accord."

        systeme "Elle pose son sac sur la table d'à côté et s'assoit dedans, dans la même rangée que lui."
        systeme "Elle ne demande pas pourquoi. C'est peut-être la chose la plus gentille qu'elle ait faite cette année."
    elif arc6_penchant == "indecis":
        i "D'accord."

        systeme "Elle regarde la rangée de Jessy, puis celle d'à côté. Elle prend celle d'à côté, sans que ça ait l'air d'une décision."
        systeme "Elle ne demande pas pourquoi. Ça pourrait être de la délicatesse. Ça pourrait être autre chose."
    else:
        i "Ok."

        systeme "Elle s'assoit deux rangées plus loin, face à la fenêtre, et finit son pain au lait en regardant la cour."
        systeme "Elle ne demande pas pourquoi. Elle a arrêté de demander à peu près en même temps qu'elle a arrêté d'être écoutée."

    # --- Rappels conditionnels : ce que chacun transporte ce matin ---
    if arc4_ilona_avec_theo:
        systeme "L'écharpe de Théo est autour de son cou. Elle ne l'a jamais rendue. Personne n'en a jamais reparlé."
    elif arc4_cadeau_jessy == "cadeau_couteux":
        systeme "L'écharpe que Jessy lui a offerte en décembre dépasse de son sac. Pliée. Jamais portée. Toujours pas expliquée."

    if arc4_cadeau_jessy in ("miniature_souvenir", "miniature_aveu"):
        systeme "Il y a une petite forme carrée dans son sac. La miniature de la maison. Elle l'emporte le jour du diplôme. Elle ne le dira pas."

    if arc5_fin_minecraft == "theo_presence":
        systeme "Elle a le nouveau mot de passe du serveur écrit au stylo sur le dos de la main. Ce n'est pas elle qui l'a changé."

    menu:

        "Le rendre, et dire pourquoi tu l'as gardé.":
            $ arc6_stylo = "rendu_explique"

            show jessy determined at char_left
            with dissolve

            j "Je l'ai depuis janvier."
            j "Je l'ai pas rendu parce que tant que je l'avais, il fallait bien que je te reparle un jour."
            j "C'est débile."

            show ilona neutral at char_midright
            with dissolve

            $ renpy.pause(0.8, hard=True)

            if arc6_penchant == "jessy":
                i "Tu aurais pu me le dire en janvier."
                j "Oui."

                show ilona smile at char_midright
                with dissolve

                i "Merci de le dire en mars."
            elif arc6_penchant == "indecis":
                i "Tu aurais pu me le dire en janvier."
                j "Oui."

                $ renpy.pause(1.0, hard=True)

                i "...Je sais pas quoi répondre à ça."

                show ilona embarrassed at char_midright
                with dissolve

                i "C'est pas un reproche. Je sais vraiment pas."
            else:
                i "Deux mois."

                $ renpy.pause(1.0, hard=True)

                i "T'as gardé un truc à moi deux mois pour être sûr d'avoir une raison de revenir."

                show ilona neutral at char_midright
                with dissolve

                j "...Ouais."
                i "Ok."

                systeme "Elle prend le stylo. Elle ne dit pas merci, et elle ne dit pas que c'est grave."
                systeme "Elle le fait tourner une fois entre ses doigts, comme si elle vérifiait que c'était bien le sien."

        "Le garder encore un peu.":
            $ arc6_stylo = "garde"

            systeme "Jessy referme la main dessus, au fond de la poche."

            show ilona neutral at char_midright
            with dissolve

            i "Tu voulais dire un truc ?"
            j "Non."
            i "D'accord."

            if arc6_penchant == "jessy":
                systeme "Elle n'insiste pas. Elle attend trois secondes de plus que d'habitude, au cas où."
                systeme "Puis elle laisse tomber. C'est exactement le problème."
            elif arc6_penchant == "indecis":
                systeme "Elle n'insiste pas. Elle n'insiste jamais. C'est exactement le problème."
            else:
                systeme "Elle n'insiste pas. Elle avait déjà tourné la tête avant la fin de la réponse."
                systeme "Elle a arrêté de poser des deuxièmes questions quelque part vers janvier. Personne n'a remarqué la date."

        "Le rendre, sans rien ajouter.":
            $ arc6_stylo = "rendu"

            j "Tiens."

            show ilona neutral at char_midright
            with dissolve

            i "...Mon stylo."
            i "Je le cherchais."
            j "Je sais."

            systeme "Elle le range dans sa trousse. La trousse était là depuis le début."

        "En faire une blague.":
            $ arc6_stylo = "blague"

            show jessy smile at char_left
            show ilona smile at char_midright
            with dissolve

            j "Ceci est un objet de quête. Je le rends contre trois émeraudes."
            i "J'ai un pain au lait."
            j "Vendu."

            if arc6_penchant == "jessy":
                systeme "Elle sourit pour de vrai. Puis elle attend une seconde de plus, au cas où il ajouterait une vraie phrase."
                systeme "Il n'ajoute rien. Le sourire tient quand même. Aujourd'hui, ça passe encore."
            elif arc6_penchant == "indecis":
                show ilona neutral at char_midright
                with dissolve

                systeme "Elle sourit par réflexe. C'était leur langue commune, avant. Puis quelque chose se referme, comme si la blague était arrivée à la place d'autre chose."
                systeme "Elle ne dit pas laquelle des deux elle aurait préféré."
            else:
                show ilona neutral at char_midright
                with dissolve

                systeme "Elle ne rentre plus dans le jeu. Elle prend le stylo, dit « merci », et le range."
                systeme "La blague reste en l'air, toute seule. C'est là qu'on voit qu'une porte s'est fermée : quand le jeu ne fait plus rire personne à deux."

    $ renpy.pause(1.0, hard=True)

    # --- Signe de bifurcation : ce qu'elle fait de ses affaires dit déjà la direction ---
    if arc6_penchant == "jessy":
        systeme "Elle se lève, glisse sa trousse dans son sac sans la fermer. Comme si quelque chose pouvait encore y revenir."
    elif arc6_penchant == "indecis":
        systeme "Elle ferme sa trousse, puis la rouvre une seconde pour vérifier quelque chose. Elle ne sort rien. Elle la referme."
    else:
        systeme "Elle range ses affaires vite, la trousse tout au fond du sac. Les choses qu'on met là sont celles qu'on ne veut plus rechercher."

    systeme "La salle se remplit. Un professeur passe dans les rangs pour vérifier les cols et les cravates."
    systeme "On leur demande de descendre au gymnase par ordre de classe, en silence, comme s'il restait quelque chose à apprendre."

    hide jessy
    hide ilona
    with dissolve

    


# SCÈNE 2 : LA CÉRÉMONIE
    stop music fadeout 1.0
    scene bg arc6 gym ceremony
    with fade

    play ambiant1 audio.foule fadein 2.0 loop volume 0.6

    systeme "Le gymnase ne ressemble plus au gymnase. Les lignes du terrain passent sous les rangées de chaises, l'estrade mord sur la raquette, et le micro siffle avant même que quelqu'un parle."
    systeme "Discours du proviseur. Personne n'écoute. Trois cent quarante noms."
    systeme "On appelle les noms par ordre alphabétique. Chacun monte, prend un papier, redescend. En quatre secondes, une année entière est classée."

    play sound audio.bell

    show alex neutral at char_left
    show allan neutral at char_midleft

    play sound audio.micka volume 0.8
    show micka happy at char_right
    with dissolve

    x "Micka a reçu son diplôme et trois enveloppes."
    a "Trois ?"
    mi "Deux lettres de profs. Et une convocation chez le proviseur adjoint."
    x "Le jour du diplôme."
    mi "Après le diplôme. Techniquement, c'est de l'optimisme administratif."
    a "Tu l'as lue ?"
    mi "Trois fois. Le mot « convocation » ne change pas."
    x "Je ne veux toujours pas savoir."

    hide micka
    hide alex
    hide allan
    with dissolve

    systeme "La cérémonie se termine sans qu'on sache exactement à quel moment. Les gens se lèvent par vagues, et d'un coup ce sont trois cents personnes debout qui ne savent plus quoi faire de leur journée."
    systeme "Au fond du gymnase, les profs de première année ont installé une table avec des jus, des chips, et un gâteau."

    $ renpy.pause(1.0, hard=True)

    show jessy neutral at char_left
    show ilona neutral at char_midright
    with dissolve

    systeme "Sur la table, un gâteau bleu nuit, couvert de sucre argenté. Quelqu'un a écrit « BONNE ROUTE » dessus, à côté d'une forme ronde qui devait être un ballon."

    i "C'est une planète."
    j "C'est un ballon."

    $ renpy.pause(1.0, hard=True)

    if arc6_penchant == "jessy":
        i "C'est une planète."

        systeme "Elle en met une part dans une serviette et la glisse dans son sac. Elle ne mange pas tout de suite."
        systeme "C'est nouveau."
    elif arc6_penchant == "indecis":
        i "...C'est une planète."

        systeme "Elle le dit une demi-seconde trop tard, comme si elle avait vérifié avant que ça vaille encore le coup."
        systeme "Elle en met une part dans une serviette et la glisse dans son sac. Elle ne mange pas tout de suite."
        systeme "C'est nouveau."
    else:
        systeme "Elle ne le redit pas."
        systeme "Elle prend une part, la plie dans une serviette, la met dans son sac, et regarde la banderole qu'on décroche au fond."

        i "Ouais. Bonne route."

        systeme "Elle ne mange pas tout de suite. C'est nouveau, et Jessy n'a aucune idée de ce que ça veut dire."

    hide jessy
    hide ilona
    with dissolve

    systeme "Elle part faire signer son livret par la prof d'anglais, qui pleure depuis le début de la matinée et n'a signé que quatre livrets."

    show allan neutral at char_midleft
    show sofiane observation at char_midright
    with dissolve

    systeme "À l'autre bout de la table, Allan pose son diplôme près des serviettes pendant qu'il cherche un mouchoir."
    systeme "Sofiane passe derrière lui avec deux verres de jus. Sa main frôle à peine la feuille."
    systeme "Quand Allan reprend son diplôme, une petite enveloppe sans nom reste sur la table."

    a "Micka en a oublié une."
    s "Non. Il en a trois."
    a "Alors celle-là est à qui ?"
    s "Pour celui qui la lit en pensant qu'elle n'était pas pour lui."

    show allan surprise at char_midleft
    with dissolve

    $ renpy.pause(0.8, hard=True)

    systeme "Allan ne bouge plus."
    systeme "Il a déjà entendu cette phrase. En décembre. Sur un banc."

    a "Le marché de Noël."
    s "Décembre."
    a "Tu l'avais reprise."
    s "Tu ne l'avais pas prise."
    a "Et tu viens de la glisser sous mon diplôme."
    s "Elle avait besoin d'une grande occasion."
    a "Tu as attendu quatre mois."
    s "J'ai attendu que ça te serve."
    a "Tu écoutais."
    s "J'écoute toujours. Personne ne fait attention."

    systeme "Allan ouvre l'enveloppe. Ses mains tremblent légèrement."
    systeme "Deux lignes manuscrites. Décembre. Marché de Noël."

    systeme "{i}« Les lumières ne disent pas où aller. Elles disent juste qu'il fait nuit. »{/i}"

    $ renpy.pause(2.0, hard=True)

    systeme "Allan la relit trois fois."
    systeme "Toute l'année, il a tenu la lumière pour les autres. Il a expliqué Théo. Rassuré Jessy. Traduit les silences."

    show allan doubt at char_midleft
    with dissolve

    systeme "Personne ne lui a jamais demandé s'il savait où il allait, lui."

    a "Merde."

    systeme "Il replie l'enveloppe et la met dans sa poche. Celle de décembre, il l'avait laissée sur le banc."

    show alex teasing at char_left
    with dissolve

    if arc4_5_sofiane_maid:
        x "J'ai une photo."

        show sofiane awkward at char_midright
        with dissolve

        s "Non."
        x "J'ai une photo depuis décembre."
        a "Montre."
        s "La route a faim."
        a "Ça ne répond pas à la question."
        s "Si."

        systeme "Alexandre montre l'écran. Allan met exactement trois secondes à comprendre ce qu'il regarde, et le reste de sa vie à l'oublier."
    else:
        x "Sofiane, t'as fait quoi cet hiver ?"
        s "J'ai financé de l'essence."
        x "C'est pas une réponse."
        s "C'est la seule qui reste vraie dans dix ans."

        systeme "Sofiane regarde ailleurs. Personne ne saura jamais."

    x "Bon."
    x "Moi je vais reprendre du gâteau avant que les premières années le finissent."
    s "Je te dépose."
    x "T'as pas de voiture."

    $ renpy.pause(1.0, hard=True)

    s "Je te dépose."

    hide alex
    hide sofiane
    with dissolve

    systeme "Ils s'en vont. Le gymnase se vide par petits paquets, comme une salle de cinéma après le générique."
    systeme "Deux premières années démontent déjà la table du buffet. Quelqu'un enroule la banderole. Le bruit ne disparaît pas : il maigrit."

    stop ambiant1 fadeout 4.0

    $ renpy.pause(1.2, hard=True)

    systeme "Allan reste au milieu, l'enveloppe pliée dans la poche, sans savoir où aller."
    systeme "Et c'est là qu'il le voit."
    systeme "Théo, près de la sortie, debout, à ne rien faire."
    systeme "Théo ne fait jamais rien. Théo attend quelqu'un, ou Théo va quelque part. Là, il regarde le gymnase se vider comme s'il essayait de le retenir."

    play music audio.tensePiano fadein 3.0 loop volume 0.7

    show allan neutral at char_midleft
    show theo neutral at char_midright
    with dissolve

    systeme "Allan connaît Théo depuis dix ans. C'est la première fois de l'année qu'il l'aborde sans avoir préparé une excuse pour lui."

    a "Théo."
    t "Allan."
    a "Dix ans que t'ouvres la bouche, que les gens le prennent mal, et que c'est moi qui traduis derrière."
    t "Je t'ai jamais demandé de le faire."
    a "Je sais."

    show allan doubt at char_midleft
    with dissolve

    a "C'est ça le problème."

    show theo defensive at char_midright
    with dissolve

    $ renpy.pause(1.2, hard=True)

    systeme "Théo ne répond pas tout de suite. C'est la première fois de l'année qu'il ne répond pas tout de suite."

    t "Tu penses que je lui fais du mal."
    a "Je pense que tu t'es jamais demandé si c'était bon pour elle, ou juste bon pour toi."
    a "Et que t'es assez malin pour avoir évité de te poser la question."

    $ renpy.pause(0.8, hard=True)

    show theo neutral at char_midright
    with dissolve

    t "Je pars."
    a "Tu pars où ?"
    t "Tokyo. Le 6."
    a "Le 6 avril."
    t "Oui."

    show allan surprise at char_midleft
    with dissolve

    a "C'est dans onze jours."
    t "Je sais compter."
    a "Elle le sait ?"
    t "Non."
    a "Tu comptes lui dire ?"
    t "Aujourd'hui."

    show allan doubt at char_midleft
    with dissolve

    a "Ne lui présente pas ça comme une offre, Théo."
    t "C'en est une."
    a "Justement."

    $ renpy.pause(1.0, hard=True)

    # Ce que Theo offre reellement, dit par lui, sans mauvaise foi. Le joueur
    # doit pouvoir comprendre pourquoi ca marche - c'est la condition pour que
    # la route Theo soit une tentation et pas un piege signale.
    t "Tu l'as regardée, cette année ?"
    a "Tous les jours."
    t "Alors t'as vu la même chose que moi."

    show theo neutral at char_midright
    with dissolve

    t "Elle passe ses journées à expliquer pourquoi elle a besoin de dix minutes. Aux profs. À vous. À moi."
    t "Là-bas, personne connaît son nom. Personne va lui demander de se justifier."

    show allan doubt at char_midleft
    with dissolve

    a "Tu appelles ça lui laisser de la place."
    t "J'appelle ça lui foutre la paix. C'est le seul truc qu'elle réclame depuis septembre."
    a "Elle le réclame quand elle est fatiguée."
    t "Elle est fatiguée depuis septembre."

    $ renpy.pause(1.2, hard=True)

    systeme "Allan n'a rien à répondre à ça. Pas parce qu'il est d'accord."
    systeme "Parce que Théo n'a pas tort, et que c'est exactement ce qui le rend dangereux."

    if arc6_penchant == "jessy":
        a "Elle viendra pas."

        $ renpy.pause(1.0, hard=True)

        t "Probablement pas."
        t "Mais je serai le seul à lui avoir proposé. Ça compte, à la fin d'une année comme ça."
    elif arc6_penchant == "indecis":
        a "Elle viendra pas."
        t "Tu es sûr de ça ?"
        a "...Non."
        t "Voilà."
    else:
        a "Elle viendra pas."

        systeme "Théo ne répond pas. Il regarde la porte du fond, celle par où elle est sortie tout à l'heure."

        t "Tu veux parier ?"
        a "Non."
        t "C'est bien ce que je dis."

    systeme "Il n'y a pas de réponse. Il n'y a pas de dispute non plus. Allan s'en va, et pour la première fois il ne traduit rien."

    hide allan
    hide theo
    with dissolve

    stop music fadeout 3.0

    systeme "Le gymnase finit de se vider. Les portes restent ouvertes, et l'air de mars entre par le fond."
    systeme "Quelque part dans le bâtiment, le téléphone de Jessy vibre. Un message d'Ilona : {i}« Salle 3-B. J'ai un feutre. »{/i}"

    $ renpy.pause(1.5, hard=True)


# SCÈNE 3 : LE RÉCAPITULATIF - ILONA RACONTE L'ANNÉE
# Cœur de l'arc. Ce n'est pas un flashback de Jessy : c'est Ilona qui relit
# l'année à voix haute. Le joueur voit sa partie racontée par la personne
# qui l'a subie. Aucune jauge affichée, et l'état est parfaitement lisible.


    play music audio.melanPiano volume 0.7 loop fadeout 1.0 fadein 2.0
    scene bg arc6 classroom festive
    with fade

    

    show jessy neutral at char_left
    show ilona neutral at char_midright
    with dissolve

    systeme "Après la cérémonie. La salle de classe sent le feutre, la poussière de craie et le papier crépon. Les premières années ont accroché des guirlandes trop courtes et une banderole qui se décolle déjà d'un côté."
    systeme "Personne n'est resté. Les chaises sont encore en rangées, comme si la fête avait été posée par-dessus un jour normal sans réussir à le déplacer."

    systeme "Jessy a retiré sa veste d'uniforme en entrant. Ilona la lui a demandée sans expliquer pourquoi."
    systeme "Elle a maintenant un feutre noir et la veste sur les genoux. Elle ne l'a pas encore ouverte."

    i "Je vais faire un truc bizarre."
    j "Tu as déjà mangé une étoile en sucre devant moi."
    i "Un truc plus bizarre."

    $ renpy.pause(0.8, hard=True)

    i "Je vais te raconter l'année."
    j "Tu étais là."
    i "Toi aussi."

    show ilona neutral at char_midright
    with dissolve

    i "Mais pas au même endroit que moi."

    j "Pourquoi maintenant ?"

    $ renpy.pause(0.8, hard=True)

    i "Parce que je ne l'ai jamais racontée à personne dans l'ordre."
    i "Je l'ai racontée en morceaux. À toi un bout, à Théo un bout, à un type déguisé en père Noël un bout."
    i "Et à chaque fois j'ai enlevé la partie qui allait faire réagir la personne en face."

    show ilona neutral at char_midright
    with dissolve

    if arc6_penchant == "jessy":
        i "Là, je vais tout dire dans l'ordre. Devant quelqu'un."
        i "C'est ça, la partie difficile. Le reste c'est juste des dates."
    elif arc6_penchant == "indecis":
        i "Là, je vais tout dire dans l'ordre. Pour voir à quoi ça ressemble."
        i "Peut-être que ça ne ressemble à rien."
    else:
        i "Là, je vais tout dire dans l'ordre. Une fois."

        $ renpy.pause(0.8, hard=True)

        i "Après je le range et j'y reviens plus."
        j "Pourquoi maintenant, alors ?"
        i "Parce qu'après aujourd'hui j'aurai plus de raison de le faire."

    systeme "Elle décapuchonne le feutre. Elle le recapuchonne. Elle le décapuchonne."

    i "Ça sent fort, ces trucs."
    j "C'est indélébile."
    i "Je sais. C'est pour ça que je le sens."

    $ renpy.pause(0.8, hard=True)

    i "Les cerisiers sont pas ouverts."
    j "Ils vont ouvrir la semaine prochaine."
    i "Ouais. Quand il n'y aura plus personne pour les regarder."
    i "Ils font toujours ça. Ils attendent que le bâtiment soit vide."

    i "Je déteste le mot « souvenir », au fait."
    j "Pourquoi ?"
    i "Parce qu'on l'utilise pour ranger. « C'est un souvenir », ça veut dire « c'est fini, tu peux le poser »."
    i "Moi j'ai pas fini. J'ai juste plus l'école."

    show ilona neutral at char_midright
    with dissolve

    $ renpy.pause(1.0, hard=True)

    i "Bon."

    $ arc6_vignettes_count = 0
    $ arc6_flashback = (arc2_choix_activite_theo != "") or (arc3_reaction_rumeur != "") or (arc3_fin_minecraft != "") or (arc4_limite_ilona != "") or arc4_ilona_avec_theo or arc5_cinema_ensemble or (arc5_question_reponse != "")

    if arc6_flashback:
        hide jessy
        hide ilona
        with Dissolve(1.5)
    else:
        i "Je croyais avoir préparé des morceaux. Là, il n'y en a aucun qui vient dans le bon ordre."
        i "Alors je vais garder les petites choses. C'est peut-être ça aussi, l'année."

    if arc6_vignettes_count < 8 and arc2_choix_activite_theo != "":
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("plage")

        scene bg arc6 flash beach
        with Dissolve(1.5)

        i "On commence par la plage. Juillet."
        i "Il faisait trop chaud, j'avais du sel partout, et j'avais envie d'aller voir les mares."

        if arc2_choix_activite_theo == "confiance":
            i "Tu m'as dit d'y aller. Sans rien ajouter."
            i "Théo m'a accompagnée, ce jour-là. Toi tu m'as laissée partir."
            i "J'ai mis longtemps à comprendre que c'étaient deux gestes différents."
            i "Tu ne sais pas ce que ça m'a fait, de ne pas avoir à me justifier."
            i "J'avais préparé trois arguments dans ma tête pendant qu'on marchait. Trois. Je les ai jamais utilisés."
            i "Et j'ai marché sur les rochers avec une phrase de rechange qui servait à rien, et c'était le meilleur moment de l'été."
        elif arc2_choix_activite_theo == "dix_minutes":
            i "Tu m'as dit que tu avais besoin de dix minutes."
            i "C'est la première fois que quelqu'un me disait où il en était, au lieu de me dire où j'en étais."
            i "J'ai compté. Tu en as pris douze."
            i "Ça m'a rassurée que tu mentes un peu. Ça voulait dire que c'était vrai."
        elif arc2_choix_activite_theo == "suivre":
            i "Tu nous as suivis."
            i "Je l'ai su tout de suite. Et j'ai passé le reste de l'été à faire semblant de ne pas le savoir."
            i "Tu sais ce qui est pire que d'être surveillée ? C'est de protéger la personne qui te surveille."
            i "J'ai menti pour toi. À moi-même. Tout l'été."
        elif arc2_choix_activite_theo == "disparaitre":
            i "Tu es parti."
            i "J'ai passé la journée à chercher ce que j'avais cassé."
            i "J'ai refait la conversation quinze fois dans ma tête pour trouver le mot qui t'avait fait partir."
            i "Je l'ai jamais trouvé. Alors j'ai décidé que le mot, c'était moi."
        else:
            i "Tu as fait une blague."
            i "Tu fais toujours une blague. Je ne sais jamais si c'est parce que ça va, ou parce que ça ne va pas du tout."
            i "J'ai ri. Je ris toujours. C'est plus simple que de demander laquelle des deux c'était."

    if arc6_vignettes_count < 8 and arc3_reaction_rumeur != "":
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("rumeur")

        scene bg arc6 flash festival
        with Dissolve(1.5)

        i "Après ça il y a eu septembre. Le festival."
        i "Et l'histoire du porte-clés dans le couloir."

        if arc3_reaction_rumeur == "demander_ilona":
            i "Tu m'as regardée avant de répondre."
            i "Personne ne fait ça. Tout le monde répond, et me regarde après."
            i "Une demi-seconde. C'est rien, une demi-seconde."
            i "J'y ai repensé en novembre, en décembre et en février. Donc apparemment non, c'est pas rien."
        elif arc3_reaction_rumeur == "silence_paralysie":
            i "Tu n'as rien dit."
            i "Et j'ai dû répondre toute seule à une question qui nous concernait tous les deux."
            i "Le pire c'est que j'ai bien répondu. Calme, drôle, propre."
            i "Et après je suis allée aux toilettes et j'ai eu les mains qui tremblaient pendant dix minutes."
        elif arc3_reaction_rumeur == "defendre_immediat":
            i "Tu m'as défendue tout de suite."
            i "C'était bien. Et je me suis quand même demandé contre quoi."
            i "Parce que si tu défends quelqu'un, c'est qu'il y a une accusation."
            i "Et j'ai passé la soirée à essayer de deviner de quoi on m'accusait."
        else:
            i "Tu les as fait rire."
            i "Ils ont arrêté d'en parler. Ils n'ont pas arrêté d'y penser."
            i "Et moi j'ai eu l'air de quelqu'un qui trouve ça drôle aussi."
            i "Je suis très bonne à ce jeu-là. C'est pas une qualité."

    if arc6_vignettes_count < 8 and arc3_fin_minecraft != "":
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("maison")

        scene bg arc6 flash minecraft
        with Dissolve(1.5)

        i "Et la maison, la même semaine."

        if arc3_fin_minecraft == "destruction":
            i "J'ai cassé la cuisine d'été."
            i "Toute seule. Devant toi."

            $ renpy.pause(1.0, hard=True)

            i "Tu as dit « Ilona... » et je t'ai dit de te taire."
            i "Tu t'es tu."
            i "J'ai passé la nuit à me demander si c'était bien ou si c'était grave."

            $ renpy.pause(1.0, hard=True)

            i "C'est des blocs. Je le sais que c'est des blocs."
            i "Mais c'était le seul endroit où j'avais construit un truc sans demander avant."
            i "Et je l'ai enlevé moi-même, parce que je supportais plus de le regarder."
            i "J'ai plus rien posé pendant trois mois. Personne l'a remarqué."
        elif arc3_fin_minecraft == "panneau_finir_phrase":
            i "Le panneau."
            i "« ICI, LES PHRASES ONT LE DROIT DE TREMBLER »."
            i "Je vais le garder. Même si le serveur ferme."

            $ renpy.pause(1.0, hard=True)

            i "Tu m'as demandé si c'était une règle. J'ai dit un avertissement."
            i "Et t'as répondu que t'allais essayer de pas faire semblant de savoir lire trop vite."

            $ renpy.pause(0.8, hard=True)

            i "Je me suis déconnectée après. Je suis restée assise. J'ai pleuré à peu près quatre minutes."
            i "Pas de tristesse. Juste parce que quelqu'un avait compris l'avertissement du premier coup."
        elif arc3_fin_minecraft == "porte_fermee":
            i "J'ai fermé la porte inutile. Un bouton, un bloc, et voilà."
            i "Tu as dit qu'elle menait nulle part. J'ai dit justement."

            $ renpy.pause(1.0, hard=True)

            i "Tu as compris que je parlais pas de la porte. Tu l'as pas dit, mais t'as compris."
            i "C'était la seule pièce qui servait à rien. C'est pour ça que je l'aimais."
            i "Les coffres rangent, les fours cuisent, les lits sauvegardent. Elle, elle existait."
            i "Et ce soir-là j'ai eu besoin de fermer même ça."
        elif arc3_fin_minecraft == "lanterne_cour":
            i "J'ai mis une lanterne devant la porte inutile."
            i "Tu m'as demandé si c'était pour qu'on la voie mieux."
            i "J'ai dit : pour qu'on arrête de faire semblant qu'elle existe pas."

            $ renpy.pause(1.0, hard=True)

            i "T'as juste dit « d'accord »."
            i "Deux syllabes. J'y ai repensé plus souvent que j'oserais l'avouer."
        else:
            i "J'ai rangé la cuisine d'été. Pas cassé, pas réparé. Rangé."
            i "Trois coffres, une table en trop, une lanterne remise droite."

            $ renpy.pause(1.0, hard=True)

            i "Et toi t'as demandé si tu pouvais aider."
            i "Personne demande. Les gens aident, ou ils regardent."
            i "J'ai dit oui. Mais doucement. Et t'as fait doucement."

    if arc6_vignettes_count > 0 and arc4_limite_ilona != "":
        $ renpy.pause(1.0, hard=True)

        i "Attends."
        i "Je saute un truc."
        j "C'est pas grave."

        $ renpy.pause(1.2, hard=True)

        i "Si."
        i "C'est exactement ça, le truc que je fais depuis un an."
        i "Je saute, et quelqu'un me dit que c'est pas grave, et on passe à la suite."

        i "Alors je le remets."

    if arc6_vignettes_count < 8 and arc4_limite_ilona != "":
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("noel")

        scene bg arc6 flash market
        with Dissolve(1.5)

        i "Décembre. Le marché. Les lumières et les gens qui achètent des trucs qu'ils vont perdre en janvier."

        if arc4_limite_ilona == "demande_theo":
            i "Tu m'as demandé ce que le cadeau de Théo voulait dire."
            i "À moi."
            i "Comme si mon travail c'était de te traduire quelqu'un d'autre."

            $ renpy.pause(1.0, hard=True)

            i "J'ai répondu, en plus. Poliment. J'ai expliqué son cadeau à sa place."
            i "J'étais dehors, il faisait moins deux, et j'ai fait le service après-vente d'un carnet que j'avais même pas demandé."
            i "Je me suis sentie comme un guichet."
        elif arc4_limite_ilona == "cadeau_respirant":
            i "Tu m'as donné la maison en petit. Avec le couloir raté."
            i "Tu n'as rien demandé en échange. Personne ne fait ça non plus."

            $ renpy.pause(1.0, hard=True)

            i "Tu avais gardé l'erreur. C'est ça qui m'a eue."
            i "N'importe qui d'autre aurait corrigé le couloir pour faire joli, et m'aurait offert une maison qui n'était pas la nôtre."
            i "Je l'ai posée sur mon bureau. Elle y est toujours. Elle prend une place débile."
        elif arc4_limite_ilona == "parole_sans_verdict":
            i "Tu es venu sans cadeau."
            i "C'était le seul cadeau que je pouvais refuser sans blesser personne."

            $ renpy.pause(1.0, hard=True)

            i "Tu sais combien de choses on m'a données cette année en me regardant les ouvrir ?"
            i "À chaque fois il faut faire le bon visage. Au bon moment. Assez fort."
            i "Toi t'es arrivé les mains vides et j'ai eu le droit d'avoir la tête que j'avais."
        elif arc4_limite_ilona == "cadeau_preuve":
            i "L'écharpe."
            i "Elle est très bien. Je ne l'ai jamais mise. Tu ne m'as jamais demandé pourquoi."

            $ renpy.pause(1.0, hard=True)

            i "Je vais te le dire, comme ça c'est fait."
            i "Parce qu'elle coûtait trop cher pour être un cadeau. Elle coûtait le prix d'une preuve."
            i "Et si je la mettais, j'avais l'impression de signer un truc."
        else:
            i "On a marché."
            i "C'est le seul soir de décembre où je n'ai rien eu à décider."
            i "On a fait deux kilomètres et j'ai pensé à rien. À rien du tout."
            i "C'est le plus beau cadeau qu'on m'ait fait et il coûtait zéro yen."

    if arc6_vignettes_count < 8 and arc4_ilona_avec_theo:
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("nuit_theo")

        scene bg arc6 flash bench
        with Dissolve(1.5)

        i "Après, il y a le soir où je suis partie avec Théo."
        i "Tu ne m'as jamais posé de question dessus. Pendant trois mois."
        i "Je sais pas si c'était de la délicatesse ou si t'avais trop peur de la réponse."

        $ renpy.pause(1.0, hard=True)

        i "Je vais te donner ce que je peux en donner."

        if arc4_5_ilona_reaction == "directe":
            i "Je lui ai demandé s'il voulait m'aider, ou être celui qui m'aide."
            i "Il n'a pas répondu."
            i "Ça fait trois mois qu'il n'a pas répondu."

            $ renpy.pause(1.0, hard=True)

            i "Et je crois que c'est la réponse."
            i "Il est très fort pour tout, sauf pour cette question-là."
        elif arc4_5_ilona_reaction == "prudente":
            i "Je lui ai demandé du temps."
            i "Il me l'a donné tout de suite. C'est ce qui m'a fait peur."

            $ renpy.pause(1.0, hard=True)

            i "Quelqu'un qui accepte tout de suite, c'est quelqu'un qui sait qu'il a le temps."
            i "Il a compté sur autre chose que sur moi. Il a compté sur la durée."
        else:
            i "J'ai dit oui."
            i "Deux mots. Je ne savais pas que ça comptait."
            i "Maintenant il y a un planning, et je ne sais plus lequel de nous deux l'a écrit."

            $ renpy.pause(1.0, hard=True)

            i "Le pire c'est que le planning est bon."
            i "Il est meilleur que tout ce que j'aurais fait toute seule."
            i "Et je me lève le matin en pensant à des horaires que j'ai pas choisis, et je trouve ça reposant."
            i "C'est ça qui me fait le plus peur. Que ce soit reposant."

        systeme "Il y a eu une nuit entière dont Jessy ne saura jamais rien. Il vient d'en recevoir quelques phrases. C'est tout ce qu'il aura."

    if arc6_vignettes_count < 8 and arc5_cinema_ensemble:
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("cinema")

        scene bg arc6 flash cinema
        with Dissolve(1.5)

        i "Et puis janvier. Le cinéma."
        i "J'ai failli annuler. J'avais des fiches jusque derrière les yeux et aucune place pour une phrase de plus."
        i "Je suis venue parce que j'avais besoin de deux heures où le reste n'existait pas."

        $ renpy.pause(1.0, hard=True)

        i "Avant d'entrer, tu m'as demandé si je voulais rentrer. Une fois."
        i "J'ai dit non, et tu ne l'as pas transformé en « t'es sûre ? ». Tu m'as crue."

        $ renpy.pause(1.0, hard=True)

        i "Et dans la salle, j'ai cherché l'accoudoir sans regarder. J'ai trouvé ta main."
        i "La première seconde, c'était un accident. Les vingt minutes suivantes, non."
        j "Je savais pas si je devais bouger."
        i "Moi non plus. C'est pour ça qu'on n'a pas bougé."

        $ renpy.pause(0.8, hard=True)

        j "Et le film était un chef-d'œuvre."
        i "Le film était un chef-d'œuvre. Ça aussi, c'était pas prévu."

    if arc6_vignettes_count < 8 and arc5_question_reponse != "":
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("gare")

        scene bg arc6 flash station
        with Dissolve(1.5)

        i "Et février. La gare."
        i "Là où je t'ai posé la seule vraie question que j'ai posée de toute l'année."

        if arc5_question_reponse == "honnete":
            i "Tu m'as dit que ta confiance tremblait encore."
            i "C'est la phrase la plus honnête que quelqu'un m'ait dite cette année."

            $ renpy.pause(1.0, hard=True)

            i "Elle m'a fait mal huit minutes, le temps du train."
            i "Et après j'ai eu quelque chose de vrai dans les mains, et j'ai pu commencer à travailler avec."
            i "On peut rien faire avec un mensonge gentil. C'est lisse. Ça glisse."
        elif arc5_question_reponse == "responsable":
            i "Tu m'as dit que ta peur t'appartenait."
            i "Elle débordait un peu quand même. Mais merci d'avoir essayé de ne pas me demander de la porter."

            $ renpy.pause(1.0, hard=True)

            i "Tu sais ce que ça change, de pas avoir à rassurer quelqu'un qui vient de te dire un truc grave ?"
            i "Ça change que j'ai pu réfléchir à ma réponse au lieu de réfléchir à la tienne."
        elif arc5_question_reponse == "theo":
            i "Tu m'as dit que le problème c'était Théo."
            i "Le problème n'a jamais été Théo."

            $ renpy.pause(1.0, hard=True)

            i "J'ai posé une question sur toi et moi, et tu as répondu sur quelqu'un d'autre."
            i "Et je suis montée dans le train en me disant que j'avais mal formulé."
            i "J'avais très bien formulé."
        else:
            i "Tu m'as demandé du temps."
            i "Je t'en ai donné. Je ne sais toujours pas ce que tu en as fait."

            $ renpy.pause(1.0, hard=True)

            i "C'est ça qui est bête. J'attendais pas une réponse rapide."
            i "J'attendais juste que tu reviennes me dire où tu en étais. N'importe quand."
            i "Il est fin mars."

    # SORTIE DE FLASHBACK : une seule fois.
    if arc6_flashback:
        scene bg arc6 classroom festive
        with Dissolve(1.5)

        show jessy listening at char_left
        show ilona neutral at char_midright
        with dissolve

    $ renpy.pause(1.0, hard=True)

    # Ce menu ne décide pas la route ; il colore seulement la posture de Jessy.
    show jessy listening at char_left
    show ilona neutral at char_midright
    with dissolve

    j "Tu racontes ça comme si tu cherchais une réponse."

    $ renpy.pause(1.0, hard=True)

    i "Oui."
    j "À quoi ?"

    $ renpy.pause(0.8, hard=True)

    i "À pourquoi je suis encore là."

    $ renpy.pause(1.2, hard=True)

    menu:

        "La laisser continuer.":
            j "Vas-y. Je bouge pas."

            $ renpy.pause(1.0, hard=True)

            i "..."
            i "Tu vois, ça. Me laisser aller au bout. Personne fait ça non plus."

        "Lui demander si elle parle de Théo.":
            show jessy neutral at char_left
            with dissolve

            j "Tu parles de Théo, là ?"

            show ilona frustrated at char_midright
            with dissolve

            i "Non. C'est exactement ça, le problème."
            i "Même maintenant, tu cherches le nom de quelqu'un d'autre dans une phrase sur moi."

        "S'excuser, précisément.":
            show jessy determined at char_left
            with dissolve

            j "Je m'excuse pour un truc précis."
            j "Pour toutes les fois où j'ai décidé de la fin de tes phrases à ta place."

            $ renpy.pause(1.0, hard=True)

            if souvenirs["jessy_repare"]:
                i "Je sais. Tu me l'as déjà dit une fois. C'est pour ça que je te le laisse redire sans lever les yeux au ciel."
            else:
                i "D'accord."
                i "C'est la première fois que tu nommes lequel."

        "Dire qu'il a peur de la perdre, sans le poser sur elle.":
            show jessy determined at char_left
            with dissolve

            j "J'ai peur de ce que tu es en train de comprendre."
            j "Mais je veux que tu ailles au bout. Même si le bout, c'est pas moi."

            $ renpy.pause(1.2, hard=True)

            i "..."
            i "Merci de pas me demander de te rassurer avant d'avoir fini."

    $ renpy.pause(1.0, hard=True)

    show ilona neutral at char_midright
    with dissolve

    # Là où le triangle cesse d'être abstrait : elle s'entend pencher.
    if arc6_penchant == "jessy":
        i "Et plus je parle, plus je me souviens des moments où j'ai respiré avec toi."
    elif arc6_penchant == "indecis":
        i "Et plus je parle, moins je sais si je suis restée par envie ou par habitude."
    else:
        i "Et plus je parle, plus je me rends compte que j'étais déjà en train de partir."

    $ renpy.pause(1.5, hard=True)

    i "Le distributeur du deuxième étage rendait la monnaie en pièces de dix."
    j "Il fait ça depuis trois ans."
    i "Je sais. J'ai un bocal."

    i "Ils vont le vider cet été. Le bâtiment est en travaux."
    i "Il y a un truc dans le monde qui va disparaître et je suis la seule personne au courant."

    $ renpy.pause(0.8, hard=True)

    j "Micka a eu trois enveloppes."
    i "J'ai vu."
    j "Il en a relu une trois fois."

    show ilona smile at char_midright
    with dissolve

    i "C'est le seul d'entre nous qui a compris comment vivre."

    show ilona neutral at char_midright
    with dissolve

    $ controle_repetitif = interruptions_ilona - interruptions_reparees
    if arc6_vignettes_count < 8 and controle_repetitif > 0:
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("phrase_finie")

        i "Il y a une phrase que je n'ai jamais finie."
        i "Tu l'as coupée. Pas méchamment. Tu avais déjà la solution."

        $ renpy.pause(1.0, hard=True)

        i "Je t'en veux pas pour la coupure. Je t'en veux pour l'habitude."
        i "Parce qu'au bout d'un moment j'ai commencé à préparer mes phrases plus courtes."
        i "Pour qu'elles rentrent avant."

        show ilona determined at char_midright
        with dissolve

        i "Je vais la finir maintenant. Tu n'as rien à faire. Juste attendre la fin."

        $ renpy.pause(2.5, hard=True)

        i "Voilà. C'était ça."
        i "C'est court, hein."

        $ renpy.pause(1.0, hard=True)

        i "Un an. Pour quatre secondes."

        if souvenirs["jessy_repare"]:
            i "Tu es revenu me le dire, une fois."
            i "Personne n'avait jamais fait ça."
            i "Les gens s'excusent sur le moment, parce que c'est gênant. Toi tu es revenu après, quand c'était plus gênant du tout."
            i "Ça, ça compte."

    # Rend visible la dette de fatigue sans modifier le verdict deja calcule.
    if pression_stream >= 12 or arc5_tension_accumulee >= 8:
        $ arc6_vignettes_jouees.append("craquage")

        stop music fadeout 3.0

        show ilona fatigue at char_midright
        with dissolve

        i "Je suis fatiguée."
        j "Depuis les examens ?"
        i "Depuis septembre."

        $ renpy.pause(1.5, hard=True)

        systeme "Elle ne pleure pas fort. Elle pleure comme quelqu'un qui a calculé combien de temps ça allait prendre et qui a décidé que c'était rentable."

        i "Je dors bien, en plus. C'est pas ça."
        i "C'est de faire attention. Tout le temps. À la tête que je fais, au moment où je réponds, à qui je réponds en premier."
        i "Je fais un travail que personne ne voit et il n'y a pas de vacances."

        $ renpy.pause(1.2, hard=True)

        show jessy listening at char_left
        with dissolve

        i "C'est bête. C'est le jour du diplôme."
        j "Ouais."
        i "Tu dis rien ?"
        j "Je crois que si je dis un truc, je vais essayer de le réparer."

        $ renpy.pause(1.2, hard=True)

        i "D'accord. Alors dis rien."

        $ arc6_ilona_a_pleure = True

        if souvenirs["jessy_repare"]:
            systeme "Il ne dit rien. Il reste. Il a mis un an à apprendre que c'était une action."
        else:
            systeme "Il ne dit rien. Il ne sait pas si c'est de la délicatesse ou de la lâcheté. Elle non plus."

        play music audio.melanPiano fadein 2.0

    $ renpy.pause(1.0, hard=True)

    i "Voilà."
    i "C'était l'année."

    $ renpy.pause(1.0, hard=True)

    j "Tu as pas parlé de toi."

    $ renpy.pause(1.2, hard=True)

    i "Ah."

    if arc6_ilona_a_pleure:
        show ilona fatigue at char_midright
    else:
        show ilona embarrassed at char_midright
    with dissolve

    i "Non."

    $ renpy.pause(1.0, hard=True)

    i "J'ai raconté une année entière et j'ai parlé que de ce que les autres ont fait."
    i "Y compris quand j'étais toute seule."

    j "Tu veux recommencer ?"
    i "Non."
    i "Je veux juste que tu saches que j'ai remarqué."

    $ renpy.pause(1.2, hard=True)

    if arc6_penchant == "jessy":
        show ilona embarrassed at char_midright
    elif arc6_penchant == "indecis":
        show ilona fatigue at char_midright
    else:
        show ilona neutral at char_midright
    with dissolve

    # Sortie de scène : elle ne peut plus prétendre que les deux futurs se valent.
    if arc6_penchant == "jessy":
        i "Je crois que j'avais besoin de vérifier que je pouvais tout te dire et rester là."
    elif arc6_penchant == "indecis":
        i "Je crois que je viens de comprendre que je peux plus continuer comme ça."
    else:
        i "Je crois que je t'ai raconté l'année parce que je voulais pas partir avec une version injuste de toi."

    $ renpy.pause(1.5, hard=True)

    if arc6_penchant == "jessy":
        systeme "Elle ouvre la veste sur ses genoux. Elle écrit trois mots au feutre, sous le col."
        systeme "Elle prend son temps. Elle raye un mot, le réécrit, souffle dessus pour que ça sèche."
        systeme "Elle rabat le tissu avant qu'il ait le temps de lire, et elle le lui rend plié."

        i "Tu regarderas ce soir."
        j "Pourquoi ce soir ?"
        i "Parce que ce soir je serai pas là quand tu feras ta tête."
    elif arc6_penchant == "indecis":
        systeme "Elle ouvre la veste sur ses genoux. Elle écrit trois mots au feutre, sous le col."
        systeme "Elle s'arrête au deuxième. Reste comme ça, le feutre en l'air, assez longtemps pour que ça devienne bizarre. Puis elle finit."
        systeme "Elle rabat le tissu avant qu'il ait le temps de lire, et elle le lui rend plié."

        i "Tu regarderas ce soir."
        j "Pourquoi ce soir ?"
        i "Parce que si tu regardes maintenant, je vais vouloir expliquer, et j'ai pas d'explication."
    else:
        systeme "Elle ouvre la veste sur ses genoux. Elle écrit trois mots au feutre, sous le col. Ça prend quatre secondes."
        systeme "Elle n'hésite sur aucun. C'est peut-être ça, le plus inquiétant."
        systeme "Elle rabat le tissu avant qu'il ait le temps de lire, et elle le lui rend plié."

        i "Tu regarderas ce soir."
        j "Pourquoi ce soir ?"

        $ renpy.pause(1.0, hard=True)

        i "Parce que ce soir, ce sera déjà plus la même journée."

    $ renpy.pause(1.5, hard=True)

    systeme "Elle se lève, remet sa chaise en rang avec les autres, par réflexe. Elle s'arrête une seconde en s'en rendant compte."

    i "Bon."
    i "On sort. Sinon on va rester là jusqu'à ce qu'un concierge nous trouve."

    hide jessy
    hide ilona
    with dissolve

    stop music fadeout 3.0

    systeme "Ils sortent dans le couloir du deuxième étage. À cette heure-ci, un jour de semaine, il y a huit cents personnes ici."
    systeme "Là, il y a des casiers ouverts, des photos scotchées sur les portes, et un seul type debout au milieu."

    $ renpy.pause(1.2, hard=True)

    # SCÈNE 4 : L'OFFRE DE THÉO
    # Climax. Théo attend seul dans le couloir vide. Il pose une offre concrète,
    # tangible, dangereuse parce que vraie. Jessy se tient à distance et la laisse
    # être formulée en entier avant d'intervenir.
    # Le ton est piloté par arc6_penchant ; la route réelle a déjà été tranchée
    # au début de l'arc. Ce que le joueur fait ici ne fait que colorer les arcs VII.

    scene bg arc6 corridor empty
    with fade

    play music audio.tensePiano fadein 2.0 loop volume 0.6

    show theo neutral at char_center
    with dissolve

    systeme "Le couloir du deuxième étage a perdu son bruit habituel. Les casiers ouverts font des rectangles sombres dans les murs, et les néons gardent la même lumière blanche que pendant les contrôles."
    systeme "Au bout, la fête continue encore un peu. Ici, il n'y a que Théo, les mains dans les poches, placé pile entre la salle et l'escalier."

    $ renpy.pause(1.0, hard=True)

    t "Je me doutais que vous passeriez par là."
    t "C'est le seul couloir qui évite le buffet."

    show theo neutral at char_midleft
    show ilona neutral at char_midright
    with dissolve

    i "Qu'est-ce que tu veux, Théo ?"

    t "Te parler. Cinq minutes."

    # Théo propose à Jessy de rester, mais Jessy choisit de leur laisser l'espace.
    show jessy neutral at char_left
    with dissolve

    t "Toi aussi tu peux rester. Ça t'évitera de te demander toute ta vie ce qui s'est dit."

    $ renpy.pause(1.0, hard=True)

    systeme "Jessy regarde Ilona. Elle ne lui demande ni de rester ni de partir. Alors il recule jusqu'aux fenêtres, à quelques mètres, et leur laisse les cinq minutes demandées."
    systeme "Il reste dans le couloir. Assez loin pour ne pas entrer dans leur face-à-face, assez près pour entendre sans les interrompre. C'est peut-être la première fois qu'il fait la différence."

    hide jessy
    with dissolve

    t "Je pars à Tokyo."
    t "Le six avril. Dans onze jours."

    show ilona neutral at char_midright
    with dissolve

    i "Onze jours."
    t "Onze jours."

    $ renpy.pause(1.2, hard=True)

    show theo reassuring at char_center
    with dissolve

    t "C'est pas une idée. C'est un studio. Une équipe qui gère déjà trois chaînes."
    t "Il y a une salle, du vrai matériel, quelqu'un dont le seul boulot c'est la modération du chat."
    t "Un planning. Des gens qui savent quoi faire quand ça monte trop vite."

    i "Et moi je fais quoi, là-dedans ?"

    t "Ce que tu fais déjà. En mieux entouré."
    t "Tu construis un nom. Pas une rumeur. Un nom que t'as choisi toi-même."

    $ renpy.pause(1.0, hard=True)

    t "Là-bas, personne connaît la plage. Personne connaît la rumeur, ni Noël, ni la gare."
    t "Personne te demandera pourquoi tu mets trois heures à répondre à un message."
    t "Tu recommences à zéro, avec des gens qui te jugent sur ce que tu fais, pas sur ce qu'on a dit de toi en octobre."

    show ilona fatigue at char_midright
    with dissolve

    systeme "Le pire, c'est qu'il ne ment pas. Il a regardé Ilona toute l'année. Il a vu la fatigue avant tout le monde, avant Jessy, avant elle."
    systeme "Il ne lui vend pas un rêve. Il lui décrit exactement l'endroit où elle arrêterait de faire attention. Et ça, elle en a envie. C'est ça qui fait mal."

    $ renpy.pause(1.5, hard=True)

    show ilona determined at char_midright
    with dissolve

    i "Théo. Question simple."
    i "Tu me proposes une opportunité, ou tu me demandes de venir avec toi ?"

    $ renpy.pause(1.5, hard=True)

    if arc6_penchant == "theo":
        show theo neutral at char_midleft
        with dissolve
        t "..."
        t "Les deux."
        t "Je vois pas pourquoi je choisirais, alors que jusqu'ici t'as jamais eu à choisir non plus."
    else:
        show theo defensive at char_midleft
        with dissolve
        systeme "Pour la première fois de l'année, il met une seconde de trop à répondre. Le sourire tient, mais quelque chose derrière a lâché."
        t "..."
        t "Je veux que tu viennes."

    $ renpy.pause(1.5, hard=True)

    i "Voilà. C'était aussi ça."

    play sound audio.bell

    j "J'ai tout entendu."

    if arc6_penchant == "jessy":
        show jessy neutral at char_midleft
        show ilona neutral at char_center
        show theo defensive at char_right
        with dissolve
        systeme "Il ne regarde pas Théo. Il se met à côté d'Ilona, à hauteur de son épaule, sans la toucher. Le corps sait déjà des choses que la bouche va mettre du temps à dire."
    elif arc6_penchant == "theo":
        show jessy neutral at char_left
        show theo neutral at char_center
        show ilona neutral at char_midright
        with dissolve
        systeme "Il reste dans l'encadrement. Entre Ilona et lui, il y a tout le couloir. Théo, lui, est à côté d'elle. La géométrie a déjà répondu à une question."
    else:
        show jessy neutral at char_midleft
        show theo neutral at char_center
        show ilona neutral at char_midright
        with dissolve
        systeme "Il s'avance, puis s'arrête à mi-chemin, comme s'il n'était sûr ni du droit d'être là, ni de celui de partir."

    $ renpy.pause(1.2, hard=True)

    $ arc6_theo_attaques = arc6_construit_attaques_theo()
    $ arc6_attaque_1 = arc6_theo_attaques[0] if len(arc6_theo_attaques) > 0 else ""
    $ arc6_attaque_2 = arc6_theo_attaques[1] if len(arc6_theo_attaques) > 1 else ""
    $ arc6_attaque_3 = arc6_theo_attaques[2] if len(arc6_theo_attaques) > 2 else ""

    if arc6_penchant == "jessy":
        show theo annoyed at char_right
        with dissolve
        t "Vas-y. Dis quelque chose."

        if len(arc6_theo_attaques) > 0:
            t "Je vais pas inventer. J'ai assez de vrai."
            t "[arc6_attaque_1]"
            if len(arc6_theo_attaques) > 1:
                t "[arc6_attaque_2]"
            t "Alors vas-y. Dis quelque chose de vrai maintenant."
        else:
            show theo defensive at char_right
            with dissolve
            t "Je vais pas mentir. T'as appris."
            t "C'est même ça, le problème."
            t "Elle a passé l'année à te dessiner les limites à ne pas franchir. Moi, je lui propose un endroit où elle n'aura pas à vérifier si tu les vois."

    elif arc6_penchant == "theo":
        show theo neutral at char_center
        with dissolve

        if len(arc6_theo_attaques) > 0:
            systeme "Théo n'attaque presque pas. Il n'en a pas besoin. Il choisit une seule vérité et la pose au milieu du couloir."
            t "[arc6_attaque_1]"
            t "Elle le sait. Toi aussi."
        else:
            systeme "Théo ne fabrique pas de procès. Il regarde Jessy comme on regarde un train déjà parti : sans colère, avec une vague pitié."
            t "Le problème, c'est pas une faute précise."
            t "C'est l'usure."
            t "T'arrives maintenant. C'est pas un reproche. C'est juste l'heure qu'il est."

    else:
        show theo neutral at char_center
        with dissolve

        if len(arc6_theo_attaques) > 0:
            t "Je vais dire les choses simplement."
            t "[arc6_attaque_1]"
            if len(arc6_theo_attaques) > 1:
                t "[arc6_attaque_2]"
            if len(arc6_theo_attaques) > 2:
                t "[arc6_attaque_3]"
            t "Je dis pas ça pour être cruel. Je dis ça parce que c'est vrai, et que tu le sais."
        else:
            show theo neutral at char_center
            with dissolve
            t "Je vais pas te fabriquer un dossier."
            t "T'as été meilleur que ça."
            t "Mais elle a dû t'apprendre comment ne pas l'étouffer. Et moi, je lui propose une vie où elle n'aura pas à l'enseigner tous les jours."

    $ renpy.pause(1.5, hard=True)

    if arc6_penchant == "jessy":
        show ilona determined at char_center
    else:
        show ilona determined at char_midright
    with dissolve

    i "Attends."
    i "Avant que tu dises quoi que ce soit, Jessy."
    i "Pas de procès. Pas de sauvetage. Pas de discours sur lui."
    i "Je me fous de ce que tu penses de Théo. Je te l'ai jamais demandé."

    $ renpy.pause(1.2, hard=True)

    i "Je te demande une seule chose. Et toi, qu'est-ce que tu veux ?"

    $ renpy.pause(1.5, hard=True)

    if arc6_penchant in ("jessy", "indecis"):
        show jessy determined at char_midleft
    else:
        show jessy determined at char_left
    with dissolve

    $ souvenir_flag_bonne = False
    menu:
        "Que répond Jessy ?"

        "« Je veux que tu restes. Mais pas pour me porter. »":
            j "Je veux être choisi. Ça, c'est vrai, autant le dire."
            j "Mais je veux pas que ma peur soit la chose la plus lourde dans ta décision."
            j "Si tu restes pour me rassurer, c'est encore moi que tu portes. Et t'as assez porté cette année."
            $ renpy.pause(1.0, hard=True)
            j "Et pour le stream."
            j "J'ai pas de studio. J'ai pas d'équipe. Je peux pas battre Tokyo avec un autre Tokyo."
            j "Mais si un jour t'as envie que ça reste petit, amateur, à toi, sans que ça devienne un métier, ça, je saurai pas te l'enlever."
            $ arc6_offre_theo = "question"
            $ arc6_conversation = "que_veux_tu"
            $ souvenir_flag_bonne = True

        "« Théo veut une place dans ton futur. »":
            j "Il te propose pas une opportunité. Il te demande de venir avec lui, il vient de le dire lui-même."
            j "C'est pas seulement pour toi qu'il fait ça. C'est aussi pour avoir une place dans ton futur."
            if arc6_penchant == "jessy":
                show theo disappointed at char_right
            else:
                show theo disappointed at char_center
            with dissolve
            i "Jessy."
            i "Je t'ai demandé ce que tu voulais, toi. Et même maintenant, tu me réponds avec lui."
            $ arc6_offre_theo = "accusation"
            $ arc6_conversation = "eviter"
            $ souvenir_flag_bonne = False

        "« Je t'ai coupée toute l'année. Je veux apprendre à te laisser finir. »":
            j "Je vais te dire un truc que j'aurais dû dire en octobre."
            j "Je t'ai coupé la parole. Souvent. Je décidais de la fin de tes phrases à ta place."
            j "Je veux pas te promettre que je vais tout réparer. J'ai déjà trop promis."
            j "Je veux juste que tu saches que je l'ai vu. Et que si tu restes, c'est un truc sur lequel tu peux me reprendre autant de fois qu'il faut."
            $ arc6_offre_theo = "question"
            $ arc6_conversation = "aveu_interruptions"
            $ souvenir_flag_bonne = True

        "Ne pas répondre.":
            systeme "Il ouvre la bouche. Il la referme. Il connaît le prix de chaque phrase et là, tout d'un coup, aucune ne lui paraît assez sûre."
            $ renpy.pause(1.5, hard=True)
            systeme "Le silence dure une seconde de trop. Puis deux. Théo, lui, n'a pas besoin de parler pour occuper l'espace : il est déjà là, entier, décidé."
            j "..."
            $ arc6_offre_theo = "laisse"
            $ arc6_conversation = "partir"
            $ souvenir_flag_bonne = False

        "« J'ai rien à mettre en face de Tokyo. »":
            j "Je vais pas faire semblant."
            if arc6_stylo == "garde":
                j "Il a un studio, une équipe, une ville. Moi j'ai un serveur Minecraft et un stylo que je t'ai jamais rendu."
            elif arc6_stylo == "rendu_explique":
                j "Il a un studio, une équipe, une ville. Moi j'ai un serveur Minecraft et un stylo que j'ai mis deux mois à rendre."
            elif arc6_stylo == "blague":
                j "Il a un studio, une équipe, une ville. Moi j'ai un serveur Minecraft et un stylo rendu avec une blague."
            else:
                j "Il a un studio, une équipe, une ville. Moi j'ai un serveur Minecraft et un stylo rendu trop tard pour être une preuve."
            j "J'ai rien à mettre en face."
            i "Je t'ai pas demandé de mettre quelque chose en face. Je t'ai demandé ce que tu voulais."
            $ arc6_offre_theo = "aveu_vide"
            $ arc6_conversation = "continuer"
            $ souvenir_flag_bonne = False

    $ renpy.pause(1.5, hard=True)

    if souvenir_flag_bonne:
        if arc6_penchant == "theo":
            show theo neutral at char_center
            with dissolve
            systeme "C'était juste. C'était même la seule chose juste qui ait été dite dans ce couloir. Mais c'est arrivé après onze mois. Et Théo, lui, arrive avec un train."
            t "C'est bien dit."
            t "Sincèrement. C'est bien dit."
            t "Mais moi, je te le demande pas dans un couloir le dernier jour. Je te le demandais toute l'année."
        else:
            if arc6_penchant == "jessy":
                show theo jealousy at char_right
            else:
                show theo jealousy at char_center
            with dissolve
            systeme "Le sourire ne revient pas. Pour la première fois, Théo a l'air de quelqu'un à qui on vient d'enlever le seul avantage qu'il croyait avoir : être le seul à l'avoir vraiment regardée."
            t "..."
            t "T'as mis un an à dire ça."
            j "Oui. J'ai mis un an."
            j "C'est pas une excuse. C'est juste pas zéro non plus."
    else:
        if arc6_penchant == "jessy":
            show theo reassuring at char_right
        else:
            show theo reassuring at char_center
        with dissolve
        t "Voilà."
        t "C'est exactement pour ça que je pars avec une place vide dans le train, au cas où."

    $ renpy.pause(1.5, hard=True)

    if arc6_penchant == "jessy":
        show ilona fatigue at char_center
        show theo neutral at char_right
    else:
        show ilona fatigue at char_midright
        show theo neutral at char_center
    with dissolve

    t "Je te force pas à répondre ce soir."
    t "Mais je dois savoir avant le trois avril. Le studio garde pas une place indéfiniment."
    t "Trois avril, Ilona. Après, je réserve pour une personne."

    $ renpy.pause(1.5, hard=True)

    systeme "Ilona ne répond pas à Théo. Elle tourne la tête vers Jessy, une seconde, juste pour voir s'il a compris ce qui vient de se jouer."
    systeme "Ce qu'elle cherche sur son visage, elle ne le dit pas. Mais elle le cherche."

    $ renpy.pause(1.5, hard=True)

    hide theo
    hide jessy
    hide ilona
    with dissolve

    stop music fadeout 3.0

    systeme "Elle passe devant eux deux et pousse la porte des escaliers. Elle ne dit à personne de la suivre. Ils suivent quand même."

    $ renpy.pause(1.2, hard=True)

    jump arc_6_calcul


# CALCUL DU VERDICT
# Le verdict est calcule a l'entree de l'arc VI, avant les choix du jour.
# Ce label ne recalcule rien : il envoie seulement vers la scene qui dit la route.

label arc_6_calcul:

    jump arc_6_decision


# SCÈNE 5 : LA DÉCISION
# Plus calme que la scène 4, plus lourde. La cour, en mars, avant la floraison.
# Pas de neutralité : Ilona tranche. Les objets parlent avant les phrases.

label arc_6_decision:

    scene bg arc6 courtyard march
    with fade

    play music audio.melanPiano fadein 3.0 loop volume 0.6

    systeme "La cour. Vingt-six mars. Les cerisiers sont alignés le long de la grille, encore fermés. Les branches font des traits noirs devant le ciel gris."
    systeme "Les bancs sont vides, les affiches de la cérémonie claquent doucement contre les vitres. La journée continue autour d'eux, mais plus personne ne parle assez fort pour la remplir."

    $ renpy.pause(1.5, hard=True)

    show ilona neutral at char_center
    with dissolve

    systeme "Ilona marche devant. Jessy et Théo la suivent à quelques pas, chacun d'un côté. Aucun des deux n'ose réduire la distance."

    $ renpy.pause(1.2, hard=True)

    i "Vous vous arrêtez tous les deux."
    i "Je vais le dire moi-même. Une fois. Et vous allez me laisser finir ma phrase."

    show ilona determined at char_center
    with dissolve

    $ renpy.pause(1.5, hard=True)

    if arc6_route == "jessy":
        jump arc_6_decision_jessy
    else:
        jump arc_6_decision_theo


label arc_6_decision_jessy:

    show theo neutral at char_right
    show jessy neutral at char_left
    with dissolve

    if arc6_stylo == "garde":
        systeme "Elle tend la main vers Jessy, sans un mot. Il comprend. Il sort enfin le stylo violet et le lui donne."
        systeme "Elle le range dans sa trousse, avec les autres, celui qui écrit tous les jours. Pas un objet gardé pour avoir une raison de revenir. Un objet qui sert."
    else:
        systeme "Elle sort le stylo violet de sa poche. Elle le range dans sa trousse, avec les autres, celui qui écrit tous les jours. Pas un objet de musée. Un objet qui sert."
    systeme "Le carnet que Théo lui avait offert, elle le referme et le glisse tout au fond de son sac. Elle ne le jette pas. Elle le range là où on range ce qui appartient à avant."

    $ renpy.pause(1.5, hard=True)

    show ilona fatigue at char_center
    i "Je vais rester avec Jessy."

    $ renpy.pause(1.2, hard=True)

    i "Pas parce qu'il sait mieux que toi où je vais, Théo. Il en a aucune idée, franchement."
    i "Parce qu'avec lui, aujourd'hui, je peux encore décider où je vais moi-même."
    i "Ton studio, il décide déjà. Ton planning décide. Ta ville décide. C'est reposant, et c'est exactement le problème."

    $ renpy.pause(1.2, hard=True)

    show jessy listening at char_left
    with dissolve

    i "Et toi, arrête de croire que tu m'as sauvée. T'as pas été à la hauteur toute l'année. T'as coupé, t'as repoussé, t'as eu peur."
    i "Je t'efface rien de tout ça. Si je reste, c'est avec ça aussi. Pas en faisant semblant que ça n'a pas existé."

    $ renpy.pause(1.2, hard=True)

    i "Le stream, il restera peut-être petit. Amateur. Regardé par trois cents personnes un bon soir."
    i "Il deviendra sérieux le jour où moi je déciderai qu'il l'est. Pas le jour où quelqu'un me construit un studio pour."

    $ renpy.pause(1.5, hard=True)

    show theo disappointed at char_right
    with dissolve

    if arc6_penchant == "theo" or influence_theo >= 8:
        t "Tu vas regretter."
        t "Pas tout de suite. Dans deux ans. Un soir où t'auras rien à dire et personne à qui le dire."
        i "Peut-être. Ce sera mon regret. Pas le tien."
    else:
        t "..."
        t "Je pensais vraiment que tu viendrais."
        i "Je sais. C'est pour ça que je te le dis en face et pas dans un message le trois avril."

    $ renpy.pause(1.5, hard=True)

    show theo neutral at char_right
    with dissolve

    systeme "Il recule d'un pas. Puis d'un autre. Il ne claque rien, ne jette rien. Il redevient juste quelqu'un qui prend un train dans onze jours, tout seul, avec une place vide qu'il ne comblera pas."

    hide theo
    with dissolve

    $ renpy.pause(1.5, hard=True)

    scene black
    with fade

    systeme "La fin de journée ne ressemble pas à une fin de film. Il faut encore rentrer, répondre à deux messages, enlever l'uniforme, faire semblant de dîner."
    systeme "Plus tard, quand la maison devient trop silencieuse, Jessy lance le serveur Minecraft."

    $ renpy.pause(1.2, hard=True)

    # --- Le dernier geste Minecraft : détermine arc6_derniere_construction ---
    scene bg arc6 minecraft last
    with dissolve

    show jessy minecraft at char_left
    show ilona minecraft at char_right
    with dissolve

    systeme "Le monde charge bloc par bloc. La maison est toujours là, avec ses murs de travers et ses fenêtres trop hautes."
    systeme "Ilona a une manière de dire les choses importantes en construisant autre chose à côté. Toujours."

    i "On laisse un truc. Un seul."
    i "Toi. Qu'est-ce qu'on laisse dans la maison ?"

    menu:
        "Que construit Jessy en dernier ?"

        "Une porte qui donne sur l'extérieur, sans mur autour.":
            systeme "Il pose une porte au milieu de rien. Une porte qui ne ferme aucune pièce, qui ne protège de rien. Une porte qu'on peut franchir dans les deux sens sans que ça compte."
            i "Elle sert à rien, cette porte."
            j "Ouais. C'est pour ça que je la mets."
            i "...Garde-la."
            $ arc6_derniere_construction = "porte_ouverte"

        "Deux panneaux : « finir ses phrases » et « droit de partir ».":
            systeme "Il plante deux panneaux devant la maison. Sur le premier : finir ses phrases. Sur le deuxième : avoir le droit de partir. Deux règles, écrites en blocs, qu'aucun des deux ne pourra faire semblant d'avoir oubliées."
            i "T'as mis « droit de partir » en premier ou en deuxième ?"
            j "En deuxième. Mais je l'ai mis quand même."
            $ arc6_derniere_construction = "panneau_partir"

        "Rien. Juste rester connectés en silence.":
            systeme "Il ne construit rien. Il reste là, à côté d'elle, dans la maison, sans remplir le silence avec un bloc de plus. Il a mis un an à comprendre que ne rien poser, parfois, c'était l'acte."
            i "Tu construis pas ?"
            j "Non. Je crois que là, c'est mieux si je pose rien."
            $ arc6_derniere_construction = "silence"

        "Un cadenas sur le coffre commun.":
            systeme "Il pose un cadenas sur le coffre où ils rangeaient tout à deux. Un réflexe de protection. Il le regarde une seconde de trop, comme s'il n'était pas sûr d'avoir fait la bonne chose."
            i "Un cadenas."
            j "Pour que personne d'autre touche à nos trucs."
            i "...D'accord. Mais laisse-moi la clé."
            $ arc6_derniere_construction = "cadenas"

    $ renpy.pause(1.5, hard=True)

    systeme "Les cerisiers, dehors, ne fleurissent toujours pas. Mais quelque chose, entre eux deux, cesse enfin d'attendre."
    systeme "Après tout ce qu'ils avaient fait cette année, elle ne pouvait presque pas décider autrement. Presque."

    hide jessy
    hide ilona
    with dissolve

    stop music fadeout 4.0

    $ renpy.pause(2.0, hard=True)

    jump arc_7_jessy


label arc_6_decision_theo:

    show jessy neutral at char_left
    show theo neutral at char_right
    with dissolve

    systeme "Elle prend la veste de Jessy, celle qu'elle portait depuis des semaines, et elle la lui rend. Pliée. Proprement. C'est presque pire qu'un geste brusque."
    if arc6_stylo == "garde":
        systeme "Le stylo violet est toujours dans la poche de Jessy. Elle ne le réclame pas. C'est pire qu'un oubli : c'est une raison de revenir qu'elle décide de ne plus prendre."
    else:
        systeme "Le stylo violet, elle le range dans la poche extérieure de son sac. Pas dans la trousse. Ailleurs. Là où on garde ce qu'on n'utilise plus mais qu'on ne jette pas encore."

    $ renpy.pause(1.5, hard=True)

    show ilona fatigue at char_center
    i "Je vais partir avec Théo."

    $ renpy.pause(1.5, hard=True)

    i "Pas parce qu'il a tout compris. Il a pas tout compris. Il a juste jamais eu peur de le dire, lui."
    if arc5_question_reponse == "temps":
        i "Parce qu'aujourd'hui, c'est lui qui marche vers demain. Toi, Jessy, tu marches vers « plus tard ». Et j'ai fait ça toute l'année. Je peux plus."
    else:
        i "Parce qu'aujourd'hui, c'est lui qui marche vers demain. Toi, Jessy, tu arrives avec tout ce qu'on a dû porter avant d'en arriver là. Et j'ai fait ça toute l'année. Je peux plus."

    $ renpy.pause(1.2, hard=True)

    show jessy listening at char_left
    with dissolve

    if arc5_question_reponse == "temps":
        systeme "Ce n'est pas une punition. Elle ne hausse pas la voix, elle ne fait pas la liste. Jessy ne perd pas contre Théo. Il perd contre le temps, contre la fatigue, contre toutes les phrases qu'il a remises à un jour qui n'est jamais arrivé."
    else:
        systeme "Ce n'est pas une punition. Elle ne hausse pas la voix, elle ne fait pas la liste. Jessy ne perd pas contre Théo. Il perd contre l'usure, contre la fatigue, contre tout ce qui est devenu trop lourd avant aujourd'hui."

    i "T'as pas mal fait. T'as fait lentement. Sur certaines choses, c'est la même conséquence."

    $ renpy.pause(1.5, hard=True)

    show jessy determined at char_left
    with dissolve

    j "..."
    j "Je vais pas te demander de rester pour que je respire."
    j "Ce serait encore te faire porter un truc. J'ai assez fait ça."

    $ renpy.pause(1.2, hard=True)

    i "..."
    i "Merci de pas me le demander."

    $ renpy.pause(1.5, hard=True)

    show ilona neutral at char_center
    show theo reassuring at char_right
    with dissolve

    systeme "Elle marche vers la grille. Théo est à côté d'elle, du bon côté du couloir, du bon côté de la cour, du bon côté de tout ce qui allait suivre."

    hide ilona
    hide theo
    with dissolve

    $ renpy.pause(1.5, hard=True)

    show jessy listening at char_left
    with dissolve

    systeme "Jessy reste sous les branches fermées. Il tient sa veste, celle qu'elle vient de lui rendre pliée."
    systeme "Sous le col, il y a trois mots, écrits au feutre un après-midi de cérémonie. Ils existent. Ils sont là, contre le tissu, à quelques centimètres de ses doigts."
    systeme "Il ne les lit pas. Pas encore. Il n'est pas sûr de vouloir savoir ce qu'on écrit à quelqu'un juste avant de choisir quelqu'un d'autre."

    $ renpy.pause(2.0, hard=True)

    hide jessy
    with dissolve

    stop music fadeout 4.0

    $ renpy.pause(2.0, hard=True)

    jump arc_6_bascule_theo


# BASCULE : LES ONZE JOURS
# Passage obligé vers arc_7_theo. On JOUE les onze jours (26 mars -> 6 avril)
# et le départ en gare, au lieu de les affirmer. Ne jamais jump arc_7_theo
# ailleurs qu'ici.

label arc_6_bascule_theo:

    scene black
    with fade

    play music audio.melanPiano fadein 3.0 loop volume 0.5

    systeme "Onze jours, ça passe vite quand on a arrêté d'attendre quelque chose."

    $ renpy.pause(1.5, hard=True)

    systeme "Vingt-huit mars. Ilona répond à Théo par un seul mot. Le studio réserve deux places au lieu d'une."
    systeme "Trente-et-un mars. Elle range sa chambre d'une manière qui ressemble à un départ avant même d'être un départ. Elle garde peu de choses. Le stylo violet n'en fait pas partie ; il n'en fait pas non plus vraiment le contraire."
    systeme "Trois avril. La date de Théo. Elle n'a pas eu besoin d'attendre jusque-là. Elle avait répondu depuis la cour."

    $ renpy.pause(1.5, hard=True)

    scene bg arc6 flash station
    with dissolve

    systeme "Six avril. La gare. Le vrai départ, celui avec des billets et des annonces au micro et un quai qui sent le café tiède."

    show theo reassuring at char_center
    show ilona neutral at char_left
    with dissolve

    t "T'as tout ?"
    i "J'ai ce que j'ai décidé de prendre. C'est pas pareil que tout."

    $ renpy.pause(1.2, hard=True)

    systeme "Jessy n'est pas venu. Personne ne le lui avait demandé, et il avait enfin appris à ne pas s'imposer là où on ne l'attendait pas. C'était peut-être sa seule vraie victoire de l'année, et elle arrivait le jour où il avait tout perdu."

    $ renpy.pause(1.5, hard=True)

    show ilona fatigue at char_left
    with dissolve

    systeme "Sur le quai, une seconde, Ilona regarde son téléphone. Un message pas écrit. Une veste pliée qui reste, quelque part, dans une autre ville, avec trois mots dessous qu'elle est la seule à connaître."
    systeme "Puis le train arrive. Et on ne fait pas attendre un train."

    $ renpy.pause(1.5, hard=True)

    hide ilona
    hide theo
    with dissolve

    stop music fadeout 4.0

    systeme "Elle monte. La porte se ferme. Ce n'est pas Théo qu'elle a choisi. C'est l'endroit où on lui épargnerait de parler. Ce n'est pas la même chose."
    systeme "Et c'est pire."

    $ renpy.pause(2.0, hard=True)

    jump arc_7_theo
