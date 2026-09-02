# =============================================================================
# ARC VI - REMISE DES DIPLÔMES : « APRÈS AUJOURD'HUI »
# =============================================================================
# Fin mars. Les cerisiers ne sont pas encore ouverts.
#
# Triple fonction de l'arc :
#   1. Payer les fils ouverts des arcs I à V.
#   2. Rendre l'année lisible sans afficher une seule jauge
#      (c'est Ilona qui raconte, c'est le pouce de Laplage qui note).
#   3. Basculer vers arc_7_jessy ou arc_7_theo.
#
# RÈGLE ABSOLUE : cet arc ne doit jamais se lire comme « Ilona choisit un garçon ».
#   arc_7_jessy = Ilona reste dans un endroit où elle peut parler.
#   arc_7_theo  = Ilona part vers un endroit où on lui épargne de parler.
#
# Les compteurs globaux restent centralisés dans script.rpy.
# Le barème des choix est documenté dans game/agents/recalibrage.md.
# =============================================================================

# --- Variables locales Arc VI ---
default arc6_stylo = ""                   # rendu / garde / rendu_explique / blague
default arc6_enveloppe_lue = False
default arc6_secret_sofiane = ""          # révélé / tenu
default arc6_allan_confronte_theo = False
default arc6_offre_theo = ""              # laisse / question / accusation / aveu_vide
default arc6_ilona_a_pleure = False
default arc6_ilona_dit_la_paix = False
default arc6_gateau_planete = False
default arc6_conversation = ""            # continuer / que_veux_tu / eviter / partir / aveu_interruptions
default arc6_derniere_construction = ""   # porte_ouverte / panneau_partir / silence / cadenas
default arc6_vignettes_jouees = []
default arc6_vignettes_count = 0
default arc6_flashback = False            # au moins une vignette à jouer en flashback

default arc6_mod = 0
default arc6_score = 0
default arc6_route = ""

# Etat de la relation lu une seule fois par scene, via etat_relation()
# (script.rpy). Evite qu'une scene bascule de ton entre deux repliques.
default arc6_etat_relation = ""

# --- Images Arc VI ---
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

# =============================================================================
# SCÈNE 1 : LE STYLO VIOLET
# =============================================================================

label arc_6_diplomes:

    scene bg arc6 classroom morning
    with fade

    play music audio.mornPiano fadein 2.0

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

    i "D'accord."

    systeme "Elle ne demande pas pourquoi. C'est peut-être la chose la plus gentille qu'elle ait faite cette année."

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

        "Le rendre en disant pourquoi il ne l'a pas rendu.":
            $ arc6_stylo = "rendu_explique"
            $ communication += 4
            $ confiance += 2
            $ jalousie = max(0, jalousie - 2)
            $ lien_jessy_ilona += 2
            $ arc6_mod += 5
            $ remember("jessy_nomme_sa_peur")

            show jessy determined at char_left
            with dissolve

            j "Je l'ai depuis janvier."
            j "Je l'ai pas rendu parce que tant que je l'avais, il fallait bien que je te reparle un jour."
            j "C'est débile."

            show ilona neutral at char_midright
            with dissolve

            $ renpy.pause(0.8, hard=True)

            i "Tu aurais pu me le dire en janvier."
            j "Oui."

            show ilona smile at char_midright
            with dissolve

            i "Merci de le dire en mars."

        "Le garder encore un peu.":
            $ arc6_stylo = "garde"
            $ communication -= 2
            $ confiance -= 1
            $ pression_stream += 1
            $ evitements += 1

            systeme "Jessy referme la main dessus, au fond de la poche."

            j "Rien."
            i "D'accord."

            systeme "Elle n'insiste pas. Elle n'insiste jamais. C'est exactement le problème."
        "Le lui rendre.":
            $ arc6_stylo = "rendu"
            $ autonomie_ilona += 2
            $ communication += 1
            $ confiance += 1
            $ pression_stream = max(0, pression_stream - 1)

            j "Tiens."

            show ilona embarrassed at char_midright
            with dissolve

            i "...Mon stylo."
            i "Je le cherchais."
            j "Je sais."

            systeme "Elle le range dans sa trousse. La trousse était là depuis le début."

        "En faire une blague.":
            $ arc6_stylo = "blague"
            $ lien_jessy_ilona += 2

            show jessy smile at char_left
            show ilona smile at char_midright
            with dissolve

            j "Ceci est un objet de quête. Je le rends contre trois émeraudes."
            i "J'ai un pain au lait."
            j "Vendu."

            systeme "C'est drôle. Ça ne coûte rien. Ça ne rapporte rien non plus."

    $ renpy.pause(1.0, hard=True)

    systeme "La salle se remplit. Un professeur passe dans les rangs pour vérifier les cols et les cravates."
    systeme "On leur demande de descendre au gymnase par ordre de classe, en silence, comme s'il restait quelque chose à apprendre."

    hide jessy
    hide ilona
    with dissolve

    stop music fadeout 3.0


# =============================================================================
# SCÈNE 2 : LA CÉRÉMONIE
# =============================================================================

    scene bg arc6 gym ceremony
    with fade

    play ambiant1 audio.foule fadein 2.0

    systeme "Le gymnase a été vidé de tout ce qui sert à faire du sport. Il reste des chaises, une estrade, et un micro qui siffle."
    systeme "Discours du proviseur. Personne n'écoute. Trois cent quarante noms."
    systeme "On appelle les noms par ordre alphabétique. Chacun monte, prend un papier, redescend. En quatre secondes, une année entière est classée."

    # --- 2.1 Micka : contrepoint obligatoire ---
    play sound "fx/japanese-school-bell-sound-488954.mp3"

    show alex neutral at char_left
    show allan neutral at char_midleft
    show micka happy at char_right
    with dissolve

    x "Micka a reçu son diplôme et trois enveloppes."
    a "Trois ?"
    mi "Une de la prof d'anglais. Une de la prof de bio."
    x "Et la troisième ?"
    mi "Du proviseur adjoint. Mais c'est un malentendu."
    x "Je ne veux pas savoir."
    mi "C'est écrit « convocation »."
    x "Je ne veux VRAIMENT pas savoir."
    a "Il l'a ouverte ?"
    mi "Trois fois."

    hide micka
    hide alex
    hide allan
    with dissolve

    systeme "La cérémonie se termine sans qu'on sache exactement à quel moment. Les gens se lèvent par vagues, et d'un coup ce sont trois cents personnes debout qui ne savent plus quoi faire de leur journée."
    systeme "Au fond du gymnase, les profs de première année ont installé une table avec des jus, des chips, et un gâteau."

    $ renpy.pause(1.0, hard=True)

    # --- 2.2 Le buffet et le gâteau-planète ---
    show jessy neutral at char_left
    show ilona neutral at char_midright
    with dissolve

    systeme "Sur la table, un gâteau bleu nuit, couvert de sucre argenté. Quelqu'un a écrit « BONNE ROUTE » dessus, à côté d'une forme ronde qui devait être un ballon."

    i "C'est une planète."
    j "C'est un ballon."

    $ renpy.pause(1.0, hard=True)

    i "C'est une planète."

    systeme "Elle en met une part dans une serviette et la glisse dans son sac. Elle ne mange pas tout de suite."
    systeme "C'est nouveau."

    # --- 2.3 L'enveloppe de Sofiane ---
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

    systeme "Allan reste immobile."
    systeme "Depuis décembre, cette phrase le suit."
    systeme "Celui qui ne sait jamais si les choses sont pour lui."

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

    systeme "Allan relit la phrase trois fois."
    systeme "Toute l'année, il a éclairé les autres."
    systeme "Il a expliqué Théo. Rassuré Jessy. Traduit les silences."
    systeme "Il a tenu les lumières pour que les autres voient leur chemin."

    show allan doubt at char_midleft
    with dissolve

    systeme "Mais lui, il n'a jamais su où aller."
    systeme "Les lumières ne montrent pas la direction."
    systeme "Elles révèlent juste qu'on est dans le noir."

    a "Merde."

    $ arc6_enveloppe_lue = True

    systeme "Il plie l'enveloppe et la garde dans sa poche."
    systeme "Cette fois, il sait qu'elle était pour lui."

    # --- 2.4 Le secret du maid café ---
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

        $ arc6_secret_sofiane = "revele"

        systeme "Alexandre montre l'écran. Allan met exactement trois secondes à comprendre ce qu'il regarde, et le reste de sa vie à l'oublier."
    else:
        x "Sofiane, t'as fait quoi cet hiver ?"
        s "J'ai financé de l'essence."
        x "C'est pas une réponse."
        s "C'est la seule qui reste vraie dans dix ans."

        $ arc6_secret_sofiane = "tenu"

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

    # --- 2.5 Allan confronte Théo ---
    systeme "Ils s'en vont. Le gymnase se vide par petits paquets, comme une salle de cinéma après le générique."
    systeme "Deux premières années démontent déjà la table du buffet. Quelqu'un enroule la banderole. Le bruit ne disparaît pas : il maigrit."

    stop ambiant1 fadeout 4.0

    $ renpy.pause(1.2, hard=True)

    systeme "Allan reste au milieu, l'enveloppe pliée dans la poche, sans savoir où aller."
    systeme "Et c'est là qu'il le voit."
    systeme "Théo, près de la sortie, debout, à ne rien faire."
    systeme "Théo ne fait jamais rien. Théo attend quelqu'un, ou Théo va quelque part. Là, il regarde le gymnase se vider comme s'il essayait de le retenir."

    play music audio.tensePiano fadein 3.0

    show allan neutral at char_midleft
    show theo neutral at char_midright
    with dissolve

    systeme "Allan connaît Théo depuis dix ans. C'est la première fois de l'année qu'il l'aborde sans avoir préparé une excuse pour lui."

    a "Théo."
    t "Allan."
    a "Depuis dix ans, quand tu dis un truc et que les gens le prennent mal, c'est moi qui explique ce que tu voulais dire."
    t "Je ne t'ai jamais demandé de faire ça."
    a "Je sais."

    show allan doubt at char_midleft
    with dissolve

    a "C'est ça le problème."

    show theo defensive at char_midright
    with dissolve

    $ renpy.pause(1.2, hard=True)

    systeme "Théo ne répond pas tout de suite. C'est la première fois de l'année qu'il ne répond pas tout de suite."

    t "Tu penses que je lui fais du mal."
    a "Je pense que tu ne t'es jamais demandé si tu lui faisais du bien, ou si tu faisais du bien à toi."
    a "Et je pense que tu es assez intelligent pour avoir évité de te poser la question."

    $ arc6_allan_confronte_theo = True
    $ influence_theo = max(0, influence_theo - 2)

    # --- 2.6 Amorce du départ de Théo (prépare la scène 4) ---
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

    systeme "Il n'y a pas de réponse. Il n'y a pas de dispute non plus. Allan s'en va, et pour la première fois il ne traduit rien."

    hide allan
    hide theo
    with dissolve

    stop music fadeout 3.0

    systeme "Le gymnase finit de se vider. Les portes restent ouvertes, et l'air de mars entre par le fond."
    systeme "Quelque part dans le bâtiment, le téléphone de Jessy vibre. Un message d'Ilona : {i}« Salle 3-B. J'ai un feutre. »{/i}"

    $ renpy.pause(1.5, hard=True)


# =============================================================================
# SCÈNE 3 : LE RÉCAPITULATIF - ILONA RACONTE L'ANNÉE
# =============================================================================
# Cœur de l'arc. Ce n'est pas un flashback de Jessy : c'est Ilona qui relit
# l'année à voix haute. Le joueur voit sa partie racontée par la personne
# qui l'a subie. Aucune jauge affichée, et l'état est parfaitement lisible.
#
# Sélection par variables, PAS par chronologie. Maximum 8 vignettes
# conditionnelles ; le craquage de clôture reste hors décompte.
# =============================================================================

    stop music fadeout 2.0

    scene bg arc6 classroom festive
    with fade

    play music audio.melanPiano fadein 2.0

    show jessy neutral at char_left
    show ilona neutral at char_midright
    with dissolve

    systeme "Après la cérémonie. La salle de classe a été décorée par les premières années : des guirlandes en papier, un tableau où quarante mains différentes ont écrit « FÉLICITATIONS », une banderole qui se décolle d'un côté."
    systeme "Personne n'est resté. Les chaises sont encore en rangées. C'est ça qui est bizarre : tout est décoré, et tout est rangé comme un jour normal."

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

    i "Là, je vais tout dire dans l'ordre. Pour voir à quoi ça ressemble."
    i "Peut-être que ça ne ressemble à rien."

    # --- Digression 1 : de tout et de rien ---
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

    # -------------------------------------------------------------------------
    # ENTRÉE EN FLASHBACK : une seule fois. Les vignettes s'enchaînent ensuite
    # sans jamais revenir à la salle de classe. La musique ne s'arrête pas.
    # -------------------------------------------------------------------------
    if arc6_flashback:
        hide jessy
        hide ilona
        with Dissolve(1.5)

    # --- V1 : LA PLAGE ---
    if arc6_vignettes_count < 8 and arc2_choix_activite_theo != "":
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("plage")

        scene bg arc6 flash beach
        with Dissolve(1.5)

        i "On commence par la plage. Juillet."
        i "Il faisait trop chaud, j'avais du sel partout, et j'avais envie d'aller voir les mares."

        if arc2_choix_activite_theo == "confiance":
            i "Tu m'as dit d'y aller. Sans rien ajouter."
            i "Tu ne sais pas ce que ça m'a fait, de ne pas avoir à me justifier."
            i "J'avais préparé trois arguments dans ma tête pendant qu'on marchait. Trois. Je les ai jamais utilisés."
            i "Et j'ai marché sur les rochers avec une phrase de rechange qui servait à rien, et c'était le meilleur moment de l'été."
            $ confiance += 2
            $ autonomie_ilona += 2
        elif arc2_choix_activite_theo == "dix_minutes":
            i "Tu m'as dit que tu avais besoin de dix minutes."
            i "C'est la première fois que quelqu'un me disait où il en était, au lieu de me dire où j'en étais."
            i "J'ai compté. Tu en as pris douze."
            i "Ça m'a rassurée que tu mentes un peu. Ça voulait dire que c'était vrai."
            $ communication += 2
        elif arc2_choix_activite_theo == "suivre":
            i "Tu nous as suivis."
            i "Je l'ai su tout de suite. Et j'ai passé le reste de l'été à faire semblant de ne pas le savoir."
            i "Tu sais ce qui est pire que d'être surveillée ? C'est de protéger la personne qui te surveille."
            i "J'ai menti pour toi. À moi-même. Tout l'été."
            $ pression_stream += 2
        elif arc2_choix_activite_theo == "disparaitre":
            i "Tu es parti."
            i "J'ai passé la journée à chercher ce que j'avais cassé."
            i "J'ai refait la conversation quinze fois dans ma tête pour trouver le mot qui t'avait fait partir."
            i "Je l'ai jamais trouvé. Alors j'ai décidé que le mot, c'était moi."
            $ pression_stream += 2
        else:
            i "Tu as fait une blague."
            i "Tu fais toujours une blague. Je ne sais jamais si c'est parce que ça va, ou parce que ça ne va pas du tout."
            i "J'ai ri. Je ris toujours. C'est plus simple que de demander laquelle des deux c'était."

    # --- V2 : LA RUMEUR ---
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
            $ ilona_peut_finir_ses_phrases += 1
        elif arc3_reaction_rumeur == "silence_paralysie":
            i "Tu n'as rien dit."
            i "Et j'ai dû répondre toute seule à une question qui nous concernait tous les deux."
            i "Le pire c'est que j'ai bien répondu. Calme, drôle, propre."
            i "Et après je suis allée aux toilettes et j'ai eu les mains qui tremblaient pendant dix minutes."
            $ pression_stream += 2
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

    # --- V3 : LA MAISON ---
    if arc6_vignettes_count < 8 and arc3_fin_minecraft != "":
        $ arc6_vignettes_count += 1
        $ arc6_vignettes_jouees.append("maison")

        scene bg arc6 flash minecraft
        with Dissolve(1.5)

        i "Et la maison, la même semaine."

        if arc3_fin_minecraft == "destruction":
            i "Tu as cassé la cuisine d'été."
            i "Je ne l'ai pas reconstruite. Pas par colère."
            i "Parce que je ne savais plus si j'avais le droit."

            $ renpy.pause(1.0, hard=True)

            i "C'est des blocs, Jessy. Je le sais que c'est des blocs."
            i "Mais c'était le seul endroit où j'avais construit un truc sans demander avant."
            i "Et un soir il était plus là. Sans que personne me prévienne."
            i "Alors j'ai arrêté de construire. Pendant trois mois. Personne ne l'a remarqué."
            $ pression_stream += 2
        elif arc3_fin_minecraft == "panneau_finir_phrase":
            i "Le panneau."
            i "« ICI, LES PHRASES ONT LE DROIT DE TREMBLER »."
            i "Je vais le garder. Même si le serveur ferme."

            $ renpy.pause(1.0, hard=True)

            i "Tu sais ce que j'ai fait le soir où tu l'as posé ?"
            i "Je me suis déconnectée, je suis restée assise, et j'ai pleuré à peu près quatre minutes."
            i "Pas de tristesse. Juste parce que quelqu'un avait écrit la chose exacte, sans que j'aie eu à la demander."
            $ communication += 2
            $ remember("maison_respectee")
        elif arc3_fin_minecraft == "porte_fermee":
            i "Tu as condamné la porte inutile."
            i "C'était la seule pièce de la maison qui ne servait à rien. C'est pour ça que je l'aimais."
            i "Tout le reste a une fonction. Les coffres rangent, les fours cuisent, les lits sauvegardent."
            i "Elle, elle existait. C'est tout. Comme moi le dimanche."
        else:
            i "Tu as rangé sans rien dire."
            i "J'ai compris. C'est déjà beaucoup."
            i "Enfin, j'ai compris un truc. J'ai jamais vérifié si c'était le bon."

    # --- Digression 2 : elle saute, puis se reprend ---
    $ renpy.pause(1.0, hard=True)

    i "Attends."
    i "Je saute un truc."
    j "C'est pas grave."

    $ renpy.pause(1.2, hard=True)

    i "Si."
    i "C'est exactement ça, le truc que je fais depuis un an."
    i "Je saute, et quelqu'un me dit que c'est pas grave, et on passe à la suite."

    i "Alors je le remets."

    # --- V4 : NOËL ---
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
            $ pression_stream += 2
        elif arc4_limite_ilona == "cadeau_respirant":
            i "Tu m'as donné la maison en petit. Avec le couloir raté."
            i "Tu n'as rien demandé en échange. Personne ne fait ça non plus."

            $ renpy.pause(1.0, hard=True)

            i "Tu avais gardé l'erreur. C'est ça qui m'a eue."
            i "N'importe qui d'autre aurait corrigé le couloir pour faire joli, et m'aurait offert une maison qui n'était pas la nôtre."
            i "Je l'ai posée sur mon bureau. Elle y est toujours. Elle prend une place débile."
            $ confiance += 2
        elif arc4_limite_ilona == "parole_sans_verdict":
            i "Tu es venu sans cadeau."
            i "C'était le seul cadeau que je pouvais refuser sans blesser personne."

            $ renpy.pause(1.0, hard=True)

            i "Tu sais combien de choses on m'a données cette année en me regardant les ouvrir ?"
            i "À chaque fois il faut faire le bon visage. Au bon moment. Assez fort."
            i "Toi t'es arrivé les mains vides et j'ai eu le droit d'avoir la tête que j'avais."
            $ autonomie_ilona += 2
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

    # --- V5 : LA NUIT AVEC THÉO ---
    # La plus importante : le joueur a vu cette nuit, Jessy non. Ilona la lui donne.
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
            $ influence_theo = max(0, influence_theo - 2)
            $ communication += 2
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
            $ pression_stream += 2
            $ influence_theo += 2

        systeme "Il y a eu une nuit entière dont Jessy ne saura jamais rien. Il vient d'en recevoir quelques phrases. C'est tout ce qu'il aura."

    # --- V6 : LE CINÉMA ---
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

    # --- V7 : LA GARE ---
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
            $ confiance += 2
            $ communication += 2
        elif arc5_question_reponse == "responsable":
            i "Tu m'as dit que ta peur t'appartenait."
            i "Elle débordait un peu quand même. Mais merci d'avoir essayé de ne pas me demander de la porter."

            $ renpy.pause(1.0, hard=True)

            i "Tu sais ce que ça change, de pas avoir à rassurer quelqu'un qui vient de te dire un truc grave ?"
            i "Ça change que j'ai pu réfléchir à ma réponse au lieu de réfléchir à la tienne."
            $ confiance += 2
        elif arc5_question_reponse == "theo":
            i "Tu m'as dit que le problème c'était Théo."
            i "Le problème n'a jamais été Théo."

            $ renpy.pause(1.0, hard=True)

            i "J'ai posé une question sur toi et moi, et tu as répondu sur quelqu'un d'autre."
            i "Et je suis montée dans le train en me disant que j'avais mal formulé."
            i "J'avais très bien formulé."
            $ pression_stream += 2
        else:
            i "Tu m'as demandé du temps."
            i "Je t'en ai donné. Je ne sais toujours pas ce que tu en as fait."

            $ renpy.pause(1.0, hard=True)

            i "C'est ça qui est bête. J'attendais pas une réponse rapide."
            i "J'attendais juste que tu reviennes me dire où tu en étais. N'importe quand."
            i "Il est fin mars."

    # -------------------------------------------------------------------------
    # SORTIE DE FLASHBACK : une seule fois.
    # -------------------------------------------------------------------------
    if arc6_flashback:
        scene bg arc6 classroom festive
        with Dissolve(1.5)

        show jessy listening at char_left
        show ilona neutral at char_midright
        with dissolve

    $ renpy.pause(1.0, hard=True)

    # --- Digression 3 : respiration, petits riens ---
    i "Le distributeur du deuxième étage rendait la monnaie en pièces de dix."
    j "Il fait ça depuis trois ans."
    i "Je sais. J'ai un bocal."

    show ilona smile at char_midright
    with dissolve

    i "Ils vont le vider cet été. Le bâtiment est en travaux."
    i "Il y a un truc dans le monde qui va disparaître et je suis la seule personne au courant."

    $ renpy.pause(0.8, hard=True)

    j "Micka a eu trois enveloppes."
    i "J'ai vu."
    j "Il en a ouvert une trois fois."
    i "C'est le seul d'entre nous qui a compris comment vivre."

    show ilona neutral at char_midright
    with dissolve

    # --- V8 : LA PHRASE JAMAIS FINIE ---
    # Pas de flashback. Salle de classe, plein jour.
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

        $ ilona_peut_finir_ses_phrases += 1

        if souvenirs["jessy_repare"]:
            i "Tu es revenu me le dire, une fois."
            i "Personne n'avait jamais fait ça."
            i "Les gens s'excusent sur le moment, parce que c'est gênant. Toi tu es revenu après, quand c'était plus gênant du tout."
            i "Ça, ça compte."
            $ confiance += 2

    # --- CLÔTURE : LE CRAQUAGE ---
    # Paie la dette technique de arc5_ilona_a_pleure.
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
        $ arc5_ilona_a_pleure = True

        if souvenirs["jessy_repare"]:
            systeme "Il ne dit rien. Il reste. Il a mis un an à apprendre que c'était une action."
            $ confiance += 4
        else:
            systeme "Il ne dit rien. Il ne sait pas si c'est de la délicatesse ou de la lâcheté. Elle non plus."

        play music audio.melanPiano fadein 2.0

    # --- Clôture de la scène 3 ---
    $ renpy.pause(1.0, hard=True)

    i "Voilà."
    i "C'était l'année."

    $ renpy.pause(1.0, hard=True)

    j "Tu as pas parlé de toi."

    $ renpy.pause(1.2, hard=True)

    i "Ah."

    show ilona embarrassed at char_midright
    with dissolve

    i "Non."

    $ renpy.pause(1.0, hard=True)

    i "J'ai raconté une année entière et j'ai parlé que de ce que les autres ont fait."
    i "Y compris quand j'étais toute seule."

    j "Tu veux recommencer ?"
    i "Non."
    i "Je veux juste que tu saches que j'ai remarqué."

    systeme "Elle ouvre la veste sur ses genoux. Elle écrit trois mots au feutre, sous le col."
    systeme "Elle rabat le tissu avant qu'il ait le temps de lire, et elle le lui rend plié."

    i "Tu regarderas ce soir."
    j "Pourquoi ce soir ?"
    i "Parce que ce soir je serai pas là quand tu feras ta tête."

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


# =============================================================================
# SCÈNE 4 : THÉO A DÉCOUVERT
# =============================================================================

    scene bg arc6 corridor empty
    with fade

    play music audio.tensePiano fadein 2.0

    show jessy neutral at char_left
    show ilona neutral at char_center
    show theo neutral at char_right
    with dissolve

    systeme "Théo attend. Il n'a jamais attendu personne de toute l'année. Il arrivait toujours avant."

    systeme "Il a une phrase prête. Ça se voit à la façon dont il inspire avant de la dire."

    t "Je pars le 6."
    i "Le 6 ?"
    t "Avril. Le 6 avril. À Tokyo."

    show ilona neutral at char_center
    with dissolve

    $ renpy.pause(1.2, hard=True)

    i "D'accord."
    i "Onze jours."
    t "Oui."

    i "Tu me dis ça pourquoi ?"

    show theo neutral at char_right
    with dissolve

    $ renpy.pause(1.0, hard=True)

    t "Parce que si je te le disais pas, je serais parti en me sachant lâche."

    i "C'est pas une réponse, ça."

    $ renpy.pause(0.8, hard=True)

    t "Non."

    systeme "Il regarde le couloir. Il n'a pas l'air d'un type qui déroule un plan. Il a l'air d'un type qui a répété seul dans sa chambre."

    t "C'est un studio. Trois personnes, une régie, des locaux pourris à Nakano."
    t "Ils cherchent quelqu'un pour la partie live. Le planning, le chat, les collabs."
    t "Il y a une place à pourvoir."

    $ renpy.pause(1.0, hard=True)

    t "Je ne dis pas qu'elle est pour toi. Je ne sais pas si tu es faite pour ça."
    t "Je dis qu'elle existe, et qu'elle sera prise en mai."

    if souvenirs["ilona_veut_streamer_serieusement"]:
        t "Et tu m'as dit en décembre que tu voulais le faire pour de vrai."
        t "Pas essayer. Le faire."

        show ilona neutral at char_center
        with dissolve

        i "Je t'ai dit ça sur un banc, à minuit, en ayant froid."
        t "Tu me l'as dit quand même."
    else:
        t "Et je ne sais même pas si c'est ce que tu veux."

        show theo defensive at char_right
        with dissolve

        t "C'est ça le problème. Je devine."
        t "Je devine depuis juillet et je ne t'ai jamais posé la question une seule fois."

        systeme "C'est peut-être la phrase la plus honnête qu'il ait dite de l'année. Elle lui coûte visiblement."

        $ renpy.pause(1.0, hard=True)

        systeme "Jessy ne dit rien. En février, près des casiers, Théo lui avait déjà déroulé la liste : les commentaires à voix haute, la file d'attente de septembre, les setups à deux heures du matin."
        systeme "Il a eu deux mois pour poser la question. Il ne l'a pas posée non plus."

    $ renpy.pause(1.2, hard=True)

    t "Voilà. C'est dit. Tu fais ce que tu veux avec."

    # --- 6.1 Ilona reprend son rêve ---
    show ilona determined at char_center
    with dissolve

    $ renpy.pause(1.0, hard=True)

    i "Je veux streamer."
    i "Pas « peut-être ». Pas « un jour »."
    i "Je veux le faire."

    $ renpy.pause(1.0, hard=True)

    if souvenirs["ilona_veut_streamer_serieusement"]:
        i "Et je viens de réaliser que je ne l'ai dit qu'à une personne cette année."

        show ilona determined at char_center
        with dissolve

        i "Et que c'était pas toi."

        systeme "Ce n'est pas une accusation. C'est un constat. C'est pire."
    else:
        i "C'est la première fois que je le dis à voix haute."

        $ renpy.pause(1.0, hard=True)

        i "Un an. Je l'ai jamais dit à personne."
        i "Et la première fois que ça sort, c'est dans un couloir, coincée entre vous deux, parce qu'il y a un train pour Tokyo dans onze jours."

        show ilona frustrated at char_center
        with dissolve

        i "C'est n'importe quoi comme moment."

        systeme "Ce n'est pas un aveu. C'est une chose qui tombe. Elle a l'air aussi surprise que les deux autres."

    $ remember("ilona_veut_streamer_serieusement")

    # --- 6.2 MENU 2 : la réponse de Jessy à l'offre ---
    menu:
        "Se taire. C'est sa décision.":
            $ arc6_offre_theo = "laisse"
            $ autonomie_ilona += 4
            $ communication += 2
            $ confiance += 2
            $ pression_stream = max(0, pression_stream - 2)
            $ ilona_peut_finir_ses_phrases += 1

            systeme "Jessy ne dit rien. C'est le truc le plus dur qu'il ait fait de l'année."

            i "Tu dis rien ?"
            j "C'est pas à moi de répondre."

            $ renpy.pause(1.0, hard=True)

            i "Ok."

            systeme "Elle a l'air d'avoir de la place, tout d'un coup. Beaucoup de place. Ça a l'air de faire un peu peur."

        "« Moi, je n'ai rien à te proposer. »":
            $ arc6_offre_theo = "aveu_vide"
            $ communication += 4
            $ confiance += 2
            $ jalousie = max(0, jalousie - 2)
            $ lien_jessy_ilona += 2
            $ arc6_mod += 5
            $ remember("jessy_nomme_sa_peur")

            show jessy determined at char_left
            with dissolve

            j "J'ai pas de studio."
            j "J'ai pas de planning, pas de régie, pas de date."
            j "J'ai un serveur Minecraft avec une maison mal foutue dessus."
            j "C'est tout ce que j'ai."

            $ renpy.pause(1.2, hard=True)

            show ilona neutral at char_center
            with dissolve

            i "Je sais."

            systeme "Elle l'a dit très bas. Ce n'était pas une consolation."

        "« Pourquoi tu as attendu aujourd'hui pour le dire ? »":
            $ arc6_offre_theo = "question"
            $ communication += 4
            $ confiance += 2
            $ jalousie = max(0, jalousie - 2)
            $ lien_jessy_ilona += 2
            $ influence_theo = max(0, influence_theo - 2)

            j "Pourquoi aujourd'hui ?"
            t "Parce que c'est aujourd'hui que le lycée s'arrête."
            j "Non. Pourquoi aujourd'hui et pas en décembre, ou en janvier, quand elle dormait plus."

            show theo defensive at char_right
            with dissolve

            t "..."
            j "T'avais déjà le studio en janvier."
            t "Oui."

            systeme "Un mot. C'est la première fois qu'il en dit un seul."

        "« Tu l'as toujours voulue pour toi. »":
            $ arc6_offre_theo = "accusation"
            $ autonomie_ilona -= 4
            $ confiance -= 4
            $ influence_theo += 2
            $ jalousie += 6
            $ lien_jessy_ilona -= 2
            $ interruptions_ilona += 1
            $ controles += 1
            $ remember("theo_utilise_une_verite")

            j "T'as toujours voulu qu'elle soit à toi."

            show theo defensive at char_right
            with dissolve

            t "Non."
            t "J'ai voulu être celui qui savait quoi faire pour elle."
            t "Toi aussi. La différence, c'est que moi j'ai fait quelque chose."

            systeme "Et Jessy n'a rien à répondre à ça, parce que c'est en partie vrai, et parce que les vérités partielles sont exactement l'arme de Théo."

            show ilona frustrated at char_center
            with dissolve

            i "Vous avez fini de parler de moi à la troisième personne ?"

    # --- 6.3 « Qu'on me foute la paix » ---
    # Fil ouvert d'arc V : Ilona ne l'avait dit qu'à Laplage, qui lui avait
    # répondu de le dire « pas à moi, à eux ». Elle le fait ici, devant les deux.
    $ renpy.pause(0.8, hard=True)

    show ilona determined at char_center
    with dissolve

    i "Je peux dire un truc ?"
    i "Vous êtes deux à vouloir m'aider."
    i "Et depuis six mois, aucun des deux ne m'a demandé si je voulais qu'on m'aide."

    $ renpy.pause(1.2, hard=True)

    i "Alors je vais le dire une fois, et après on n'en parle plus."

    stop music fadeout 1.0

    i "Qu'on me foute la paix."

    $ renpy.pause(2.0, hard=True)

    systeme "Personne ne bouge. Le couloir est très long et très vide."

    i "...Pas pour toujours."
    i "Juste assez pour que j'arrive à entendre ce que je veux, moi."

    # --- Réaction calibrée : ce moment ne peut plus rester neutre.
    # On penche déjà vers la route Jessy ou la route Théo, avant même
    # le calcul final. Aperçu grossier, sans jauge affichée.
    $ controle_repetitif = interruptions_ilona - interruptions_reparees
    $ espace_p4 = (autonomie_ilona * 4) + (ilona_peut_finir_ses_phrases * 6) + (interruptions_reparees * 6) + communication + confiance
    $ dette_p4 = (influence_theo * 3) + (max(0, controle_repetitif) * 8) + (pression_stream * 2) + (jalousie * 2) + (confidences_laplage * 4)
    $ score_p4 = espace_p4 + arc6_mod - dette_p4

    if controle_repetitif >= 3:
        show theo neutral at char_right
        with dissolve

        systeme "Théo ne dit rien. Il n'a pas besoin de dire quoi que ce soit : il sait déjà qu'elle reviendra vers ce qui décide à sa place."

        show jessy listening at char_left
        with dissolve

        systeme "Jessy ne bouge pas. Il a coupé trop de ses phrases pour avoir le droit de retenir celle-ci."
    elif score_p4 >= SEUIL_JESSY:
        show theo defensive at char_right
        with dissolve

        systeme "Théo baisse les yeux le premier. Ça ne lui arrive jamais."

        show jessy listening at char_left
        with dissolve

        systeme "Jessy ne bouge pas non plus. Mais cette fois, c'est parce qu'il a compris qu'il ne fallait pas, pas parce qu'il ne sait pas quoi faire."
    else:
        show theo smirk at char_right
        with dissolve

        systeme "Théo hoche la tête, presque satisfait. Comme si la scène confirmait quelque chose qu'il pensait déjà."

        show jessy listening at char_left
        with dissolve

        systeme "Jessy voudrait la retenir. Il ne sait plus si c'est pour elle, ou pour ne pas rester seul avec Théo dans ce couloir."

    $ arc6_ilona_dit_la_paix = True
    $ autonomie_ilona += 6
    $ ilona_peut_finir_ses_phrases += 1

    hide ilona
    with dissolve

    systeme "Elle part. Personne ne la suit."
    systeme "C'est le premier moment de toute l'année où personne ne la suit."

    hide theo
    hide jessy
    with dissolve


# =============================================================================
# SCÈNE 5 : MONSIEUR LAPLAGE, DERNIÈRE FOIS
# =============================================================================
# Troisième et dernière scène symbolique. Après ça, il ne réapparaît
# qu'au post-générique.
# =============================================================================

    scene bg arc6 courtyard march
    with fade

    systeme "Elle traverse la cour. Elle ne va nulle part : elle s'éloigne. Ce n'est pas la même chose."
    systeme "Les cerisiers ne sont pas encore ouverts. Sous le plus grand, il y a une table pliante qui n'était pas là ce matin."
    systeme "Une table, une chaise, un tampon, et une pile de formulaires parfaitement vierges."

    $ renpy.pause(1.5, hard=True)

    play sound "fx/re-zero-return.mp3"

    show laplage neutral at char_midright
    with Dissolve(1.5)

    systeme "L'homme derrière la table prend une feuille blanche, la tamponne, la range. Il en prend une autre."
    systeme "Il porte un badge : {i}« Régisseur de Fins d'Année - Service des Départs »{/i}."

    show ilona neutral at char_midleft
    with dissolve

    $ renpy.pause(1.0, hard=True)

    i "Vous tamponnez quoi ?"
    laplage "Des départs."
    i "Elles sont vides."
    laplage "Elles se remplissent après. Parfois des années après."
    laplage "Mon service ne s'occupe pas du contenu. Seulement de la date."

    systeme "Jessy s'est arrêté à dix mètres, sous le préau. Il entend tout."
    systeme "Ce n'est probablement pas un hasard, et probablement pas de son fait à lui."

    $ renpy.pause(1.0, hard=True)

    laplage "Vous avez fini l'école."
    i "Oui."
    laplage "Ce n'est pas la même chose que finir quelque chose."
    i "Non."

    systeme "Il regarde les branches."

    laplage "Ils ne sont pas ouverts."
    i "Ils vont s'ouvrir la semaine prochaine."
    laplage "Oui. Et personne ne leur a demandé s'ils étaient prêts."

    $ renpy.pause(1.2, hard=True)

    laplage "Je vous ai posé une question, en février."
    i "Je m'en souviens."
    laplage "Vous n'avez pas répondu."
    i "Non."
    laplage "Ce n'était pas une question qui attendait une réponse."
    laplage "C'était une question qui attendait que vous ayez le droit de ne pas répondre."

    # Meme regle que les deux confidences precedentes : Ilona ne se confie
    # a Laplage que si personne d'autre ne la laisse finir. C'est une dette.
    # L'etat est fige ici pour que le ton de la scene reste coherent.
    $ arc6_etat_relation = etat_relation()

    if arc6_etat_relation == "proche":
        i "Aujourd'hui, j'ai le droit."
        laplage "Je sais. C'est pour ça que je ne repose pas la question."
        systeme "Il tamponne une feuille vierge et la lui tend."
    elif arc6_etat_relation == "fragile":
        i "J'apprends. Doucement."
        laplage "Doucement, c'est encore une vitesse."
        systeme "Il tamponne une feuille vierge et la pose sur le bord de la table."
    else:
        i "Je ne sais pas si je l'aurai un jour, ce droit."
        laplage "Alors gardez la question. Elle tient dans une poche."
        systeme "Il tamponne une feuille vierge et la range avec les autres."

    if arc6_etat_relation != "proche":
        $ confidences_laplage += 1
    $ jugement_laplage += 1

    hide ilona
    with dissolve

    # --- 7.1 Le pouce = la jauge ---
    # Seul retour chiffré que le joueur reçoit de tout le jeu.
    # Remplace un écran de stats, et reste diégétique.
    show jessy neutral at char_left
    with dissolve

    $ controle_repetitif = interruptions_ilona - interruptions_reparees
    $ espace = (autonomie_ilona * 4) + (ilona_peut_finir_ses_phrases * 6) + (interruptions_reparees * 6) + communication + confiance
    $ dette = (influence_theo * 3) + (max(0, controle_repetitif) * 8) + (pression_stream * 2) + (jalousie * 2) + (confidences_laplage * 4)
    $ posture = 0
    if souvenirs["jessy_nomme_sa_peur"]:
        $ posture += 6
    if souvenirs["jessy_repare"]:
        $ posture += 8
    if souvenirs["ilona_libre_sans_abandon"]:
        $ posture += 5
    if souvenirs["maison_respectee"]:
        $ posture += 3
    if souvenirs["theo_utilise_une_verite"]:
        $ posture -= 6
    $ recidive = (-6 * max(0, controles - 2)) + (-3 * max(0, evitements - 3))
    $ arc6_score_partiel = espace + posture + recidive - dette

    systeme "Laplage se tourne vers Jessy. C'est la dernière fois qu'il donne un avis sur cette année. Après ça, il ne reste que le résultat."

    if controle_repetitif >= 3:
        show laplage thumb_down at char_midright
        with dissolve
        laplage "Ça, ce n'est pas une question de score."
        systeme "Il ne regarde même pas la feuille avant de tamponner. Couper quelqu'un trois fois sans jamais réparer, ça ne se moyenne pas avec le reste. Ça s'additionne tout seul."
        laplage "Tu as appris à construire des maisons qui tiennent debout. Ça ne sert à rien si tu n'apprends jamais à laisser quelqu'un ouvrir la porte lui-même."
    elif arc6_score_partiel >= SEUIL_ROMANCE:
        show laplage thumb_up at char_midright
        with dissolve
        laplage "Continuez."
        laplage "Tu as mis longtemps à comprendre qu'écouter, ça ne se prouve pas. Ça se pratique, en silence, jusqu'à ce que ça devienne un réflexe."
    elif arc6_score_partiel >= SEUIL_JESSY:
        show laplage thumb_horizontal at char_midright
        with dissolve
        laplage "Ce n'est pas fini."
        laplage "Toi non plus, tu n'es pas fini. C'est un compliment, venant de quelqu'un qui a fini d'apprendre depuis longtemps."
    else:
        show laplage thumb_down at char_midright
        with dissolve
        laplage "Faites attention à ce que vous appelez aimer."
        laplage "On confond souvent protéger et retenir. Les deux se ressemblent, vus de dedans."

    $ renpy.pause(1.5, hard=True)

    hide laplage
    with dissolve

    systeme "Il s'en va par la grille. Personne ne le reverra avant très longtemps."

    hide jessy
    with dissolve

    systeme "Quand Jessy se retourne vers la table pliante, il n'y a plus de table pliante."
    systeme "Il y a un cerisier fermé, une cour vide, et une après-midi entière devant lui."

    stop music fadeout 3.0

    scene black
    with Dissolve(1.5)

    $ renpy.pause(2.0, hard=True)


# =============================================================================
# SCÈNE 6 : LE TOIT, LE SOIR - LE MENU PIVOT
# =============================================================================

    scene bg arc6 rooftop dusk
    with fade

    play music audio.sadPiano fadein 2.0

    systeme "Ilona a demandé de l'air à quatorze heures. Il est dix-neuf heures."
    systeme "Jessy a attendu cinq heures avant de monter."
    systeme "Cinq heures. Ce n'est pas un exploit. C'est juste la première fois."

    show jessy neutral at char_left
    show ilona neutral at char_midright
    with dissolve

    systeme "Elle est là. La part de gâteau bleu est sur ses genoux, dans sa serviette en papier. Elle l'a ouverte il y a une heure. Elle n'y a pas touché."

    j "En avril, dans le train, j'ai commencé une phrase."
    i "« Ilona, je voulais te dire que— »."
    j "Tu t'en souviens ?"
    i "Je m'en souviens de toutes celles que tu finis pas."

    $ renpy.pause(1.0, hard=True)

    menu:

        "Partir avant sa réponse.":
            $ arc6_conversation = "partir"
            $ arc6_mod -= 20
            $ autonomie_ilona -= 6
            $ confiance -= 6
            $ influence_theo += 3
            $ jalousie += 9
            $ lien_jessy_ilona -= 3
            $ interruptions_ilona += 1
            $ controles += 1

            i "Attends, je—"

            hide jessy
            with dissolve

            systeme "Jessy est déjà dans l'escalier."
            systeme "Elle avait commencé une phrase."

        "« Je t'ai coupée. Plusieurs fois. Je le sais maintenant. »" if souvenirs["jessy_repare"] and interruptions_reparees >= 1:
            $ arc6_conversation = "aveu_interruptions"
            $ arc6_mod += 25
            $ communication += 6
            $ confiance += 3
            $ jalousie = max(0, jalousie - 3)
            $ lien_jessy_ilona += 3
            $ interruptions_reparees += 1

            show jessy determined at char_left
            with dissolve

            j "Je t'ai coupée."
            j "Plusieurs fois. Je croyais que j'aidais."
            j "J'ai mis un an à comprendre que finir la phrase de quelqu'un, c'est lui prendre la fin."

            $ renpy.pause(1.5, hard=True)

            show ilona neutral at char_midright
            with dissolve

            i "..."
            i "Redis-le."
            j "J'ai mis un an."
            i "Non. L'autre partie."
            j "Je t'ai coupée."
            i "Voilà."

            show ilona smile at char_midright
            with dissolve

            systeme "Elle a l'air de respirer."

            i "Voilà."

        "« Tu veux continuer avec moi, après l'école ? »":
            $ arc6_conversation = "continuer"
            $ arc6_mod -= 5
            $ lien_jessy_ilona += 6
            $ pression_stream += 1

            j "Tu veux continuer avec moi, après l'école ?"

            systeme "C'est une belle phrase. Elle sonne bien. Elle est entièrement construite autour de ce que Jessy a peur de perdre."

            show ilona neutral at char_midright
            with dissolve

            i "Tu me demandes si je reste."
            j "Oui."
            i "Tu me demandes pas ce que je veux."
            j "..."
            i "C'est pas grave. C'est juste pas pareil."

        "Éviter la conversation.":
            $ arc6_conversation = "eviter"
            $ arc6_mod -= 10
            $ communication -= 6
            $ confiance -= 3
            $ pression_stream += 3
            $ evitements += 1

            show jessy embarrassed at char_left
            with dissolve

            j "Il fait froid, non ?"
            i "Ouais."

            systeme "Ils parlent de la météo."
            $ renpy.pause(2.0, hard=True)
            systeme "Onze minutes."
            $ renpy.pause(2.0, hard=True)
            systeme "Quatorze."
            $ renpy.pause(2.0, hard=True)
            systeme "Ils parlent encore du froid. Le soleil est descendu derrière le gymnase et personne n'a rien dit d'autre."

        "« Qu'est-ce que tu veux vraiment, pour la suite ? »":
            $ arc6_conversation = "que_veux_tu"
            $ arc6_mod += 15
            $ autonomie_ilona += 6
            $ communication += 3
            $ confiance += 3
            $ pression_stream = max(0, pression_stream - 3)
            $ ilona_peut_finir_ses_phrases += 1

            j "Qu'est-ce que tu veux, toi ? Vraiment. Pour la suite."

            show jessy listening at char_left
            with dissolve

            systeme "Elle ne répond pas tout de suite. Elle repose la serviette à côté d'elle. Elle prend le temps que personne ne lui a jamais donné."

    # --- 8.2 La réponse d'Ilona : modulée par l'état réel de la relation ---
    # C'est ici que l'accumulation de tout le jeu devient audible.
    $ controle_repetitif = interruptions_ilona - interruptions_reparees
    $ espace = (autonomie_ilona * 4) + (ilona_peut_finir_ses_phrases * 6) + (interruptions_reparees * 6) + communication + confiance
    $ dette = (influence_theo * 3) + (max(0, controle_repetitif) * 8) + (pression_stream * 2) + (jalousie * 2) + (confidences_laplage * 4)
    $ posture = 0
    if souvenirs["jessy_nomme_sa_peur"]:
        $ posture += 6
    if souvenirs["jessy_repare"]:
        $ posture += 8
    if souvenirs["ilona_libre_sans_abandon"]:
        $ posture += 5
    if souvenirs["maison_respectee"]:
        $ posture += 3
    if souvenirs["theo_utilise_une_verite"]:
        $ posture -= 6
    $ recidive = (-6 * max(0, controles - 2)) + (-3 * max(0, evitements - 3))
    $ arc6_score_preview = espace + posture + recidive + arc6_mod - dette

    if controle_repetitif >= 3:
        show ilona neutral at char_midright
        with dissolve
        i "Je crois que c'est là que je devrais dire un truc important."
        i "Mais je sais déjà comment ça se passe si je le dis lentement."
        systeme "Elle ne finit pas la phrase. Elle a arrêté d'essayer de savoir si, cette fois, tu la laisserais aller jusqu'au bout."
    elif arc6_score_preview >= SEUIL_ROMANCE:
        show ilona determined at char_midright
        with dissolve
        i "Je veux streamer. Je vais peut être le faire mal au début. Mais je veux que ce soit à moi."
        i "Et je veux quelqu'un qui me regarde le faire sans essayer de le faire à ma place."
        systeme "Elle ne le regarde pas."
        i "C'est pas une question."
    elif arc6_score_preview >= SEUIL_JESSY:
        show ilona neutral at char_midright
        with dissolve
        i "Je sais pas encore."
        i "Mais c'est la première fois que quelqu'un me demande sans avoir déjà la réponse dans la poche."
        i "Laisse-moi juste... ne pas savoir, quelques semaines."
    else:
        show ilona fatigue at char_midright
        with dissolve
        i "Je sais pas."
        i "Et j'ai plus la force de chercher devant quelqu'un."
        systeme "Elle referme la serviette sur le gâteau et la remet dans son sac. Elle ne l'a pas entamé. Elle finit toujours ce qu'elle mange."

    $ renpy.pause(1.5, hard=True)

    hide jessy
    hide ilona
    with dissolve

    stop music fadeout 4.0

    systeme "Ils descendent du toit sans se dire au revoir, parce que dire au revoir un jour comme celui-là, ça voudrait dire quelque chose."
    systeme "Ils prennent le même train, descendent à deux arrêts différents, et s'écrivent « bien rentré ? » comme tous les soirs depuis un an."

    scene black
    with Dissolve(1.5)

    $ renpy.pause(1.5, hard=True)

    systeme "Vingt-deux heures. Jessy pose sa veste d'uniforme pliée sur son lit, sans l'ouvrir."
    systeme "Il regarde le col pendant un moment. Puis il allume son PC à la place. C'est plus facile."

    $ renpy.pause(1.5, hard=True)


# =============================================================================
# SCÈNE 7 : LA DERNIÈRE CONNEXION
# =============================================================================

    scene bg arc6 minecraft last
    with fade

    play music audio.mcnight fadein 2.0

    show jessy minecraft at char_left
    show ilona minecraft at char_midright
    with dissolve

    systeme "Le soir. Le serveur tourne encore. Il tournera encore longtemps : personne ne coupe jamais ces serveurs-là, ils s'éteignent tout seuls quand plus personne ne se connecte."

    # --- 9.1 État des lieux : la maison comme journal de l'année ---
    systeme "Deux joueurs connectés. La maison n'a pas bougé. Elle a juste enregistré."

    if "panneau_phrases_tremblent_arc3" in maison_minecraft_ajouts:
        systeme "Le panneau est encore là. Le texte a un peu bavé."
    if "cuisine_ete_rangee_arc3" in maison_minecraft_ajouts:
        systeme "La cuisine d'été est rangée. Trop rangée."
    if "porte_inutile_fermee_arc3" in maison_minecraft_ajouts:
        systeme "La porte inutile est condamnée depuis septembre."
    if "lanterne_porte_inutile_arc3" in maison_minecraft_ajouts:
        systeme "Il y a une lanterne devant une porte qui ne s'ouvre pas."
    if "miniature_noel_arc4" in maison_minecraft_ajouts:
        systeme "Il y a une maison dans la maison."
    if "espace_calme_arc4" in maison_minecraft_ajouts:
        systeme "Il y a une pièce où personne ne construit."
    if "echarpe_coffre_arc4" in maison_minecraft_ajouts:
        systeme "Dans un coffre, un bloc de laine. Jessy sait lequel."
    if "coin_dehors_carnet_arc4" in maison_minecraft_ajouts:
        systeme "Il y a un coin dehors, en bordure, qui n'appartient à personne."
    if "neige_toit_arc4" in maison_minecraft_ajouts:
        systeme "La neige de décembre n'a jamais fondu. C'est Minecraft."
    if "salle_repos_arc5" in maison_minecraft_ajouts:
        systeme "La salle de repos est reliée à la maison. Elle a sa propre porte."
    if "construction_loin_arc5" in maison_minecraft_ajouts:
        systeme "Il y a une construction, loin, au bord du render distance."
    if "coffres_theo_arc5" in maison_minecraft_ajouts:
        systeme "Les coffres sont triés par ordre alphabétique. Ce n'est pas Ilona qui a fait ça."
    if "panneau_air_arc5" in maison_minecraft_ajouts:
        systeme "Un panneau : « JE REVIENS ». Pas de date."
    if "coffre_libre_arc5" in maison_minecraft_ajouts:
        systeme "Un coffre vide, avec son nom dessus."

    if "cuisine_ete_arc3" in maison_minecraft_destructions:
        systeme "Là où était la cuisine d'été, il y a un trou carré. Personne ne l'a rebouché. Ça fait sept mois."

    # --- 9.2 Le gâteau-planète (Ilonanium) ---
    # Choix binaire assumé : soit elle la mange (point cosmique), soit non.
    systeme "Elle sort la serviette de son sac et la pose devant elle. La part de gâteau bleu nuit est intacte. Le sucre argenté a un peu fondu."

    i "Je l'ai gardée toute la journée."
    j "C'est un ballon."
    i "C'est une planète, Jessy."

    $ renpy.pause(0.8, hard=True)

    i "Je la mange, ou je la garde ?"

    menu:
        "Lui dire de la garder pour l'été.":
            $ lien_jessy_ilona += 2
            $ confiance += 1

            j "Garde-la pour cet été."
            i "L'été c'est dans quatre mois."
            j "Ouais."

            $ renpy.pause(1.0, hard=True)

            i "...D'accord."

            systeme "Elle replie la serviette sans y toucher et la range. C'est la première fois qu'elle met quelque chose de comestible de côté pour plus tard."
            systeme "La planète reste entière. Quelque part, un univers respire un peu mieux, et n'en saura rien."

        "Lui dire de la manger maintenant.":
            $ ilonanium_points += 1
            $ arc6_gateau_planete = True
            $ lien_jessy_ilona += 2

            j "Mange-la."
            i "Maintenant ?"
            j "Maintenant."

            play sound audio.eating

            systeme "Elle mange la part de gâteau bleu nuit sur le toit de la maison, assise dans le noir, à onze heures du soir. Elle ne laisse pas une miette."

            i "Voilà."
            i "Une de moins."

    if ilonanium_points >= 6:
        systeme "L'écran vacille très légèrement. Pas un glitch. Une respiration."
        i "..."
        j "Quoi ?"
        i "Rien."
        i "J'ai juste plus faim. Pour la première fois depuis longtemps."
        systeme "Quelque part, très loin, une constellation compte ses membres et en trouve un de moins."

    # --- 9.3 MENU 5 : la dernière construction ---
    systeme "Il reste un peu de temps avant que quelqu'un se déconnecte le premier."

    menu:

        "Mettre un cadenas sur la salle secrète.":
            $ arc6_derniere_construction = "cadenas"
            $ autonomie_ilona -= 4
            $ confiance -= 4
            $ influence_theo += 2
            $ jalousie += 6
            $ lien_jessy_ilona -= 2
            $ pression_stream += 2
            $ controles += 1
            $ maison_minecraft_ajouts.append("cadenas_salle_secrete_arc6")

            i "Tu fais quoi ?"
            j "Comme ça personne d'autre peut entrer."

            i "...Moi non plus, alors."
            j "Toi si, t'as la clé."
            i "C'est pas pareil, Jessy."
            i "Avant j'avais pas besoin de clé."

        "Poser un panneau : « ICI, ON A LE DROIT DE PARTIR ».":
            $ arc6_derniere_construction = "panneau_partir"
            $ autonomie_ilona += 4
            $ communication += 4
            $ confiance += 2
            $ pression_stream = max(0, pression_stream - 2)
            $ maison_minecraft_ajouts.append("panneau_droit_de_partir_arc6")

            systeme "Le panneau se pose à côté de celui de septembre. Deux lignes maintenant."
            systeme "« ICI, LES PHRASES ONT LE DROIT DE TREMBLER. »"
            systeme "« ICI, ON A LE DROIT DE PARTIR. »"

            i "Le deuxième est plus dur que le premier."
            j "Je sais."

        "Ne rien construire. Rester connectés en silence.":
            $ arc6_derniere_construction = "silence"
            $ lien_jessy_ilona += 4
            $ confiance += 1
            $ pression_stream = max(0, pression_stream - 2)

            systeme "Personne ne pose de bloc. Ils restent assis sur le toit. Le compteur de temps de jeu monte tout seul."

        "Ouvrir la porte inutile. Lui faire une sortie.":
            $ arc6_derniere_construction = "porte_ouverte"
            $ autonomie_ilona += 4
            $ communication += 2
            $ confiance += 2
            $ pression_stream = max(0, pression_stream - 2)
            $ remember("maison_respectee")
            $ maison_minecraft_ajouts.append("sortie_porte_inutile_arc6")

            play sound "fx/minecraft-wood-break-place.mp3"

            systeme "Jessy casse deux blocs. Il y a maintenant une sortie au bout du couloir qui ne menait nulle part."

            i "Tu l'as ouverte."
            j "Ouais."
            i "Pourquoi ?"
            j "Pour que ce soit toi qui décides si tu la prends."

            $ renpy.pause(2.5, hard=True)

            systeme "Son personnage ne bouge pas du tout pendant très longtemps."

            i "Ok."

    # --- 9.4 Fin d'arc ---
    $ renpy.pause(1.0, hard=True)

    systeme "23h41. Deux joueurs connectés."
    systeme "Demain, il n'y a pas de cours."
    systeme "Demain, il n'y a plus jamais de cours."

    hide ilona
    with dissolve

    systeme "{i}IlonaGaming a quitté la partie.{/i}"

    $ renpy.pause(2.0, hard=True)

    stop music fadeout 3.0
    scene black
    with Dissolve(2.0)

    $ renpy.pause(1.5, hard=True)

    jump arc_6_calcul


# =============================================================================
# ARC 6 - CALCUL DU POINT DE BASCULE
# =============================================================================
# Trois strates chiffrées, aucun verrou binaire pur (sauf le contrôle répété).
#
#   ESPACE   : ce que Jessy a construit autour d'Ilona.
#   DETTE    : ce qui s'est refermé autour d'elle.
#   POSTURE  : les souvenirs, pondérés fortement.
#   RÉCIDIVE : pénalité d'accumulation d'évitements et de contrôles.
#   ARC6_MOD : le menu pivot du toit, de -20 à +25.
#
# Sorties :
#   arc_7_jessy -> game/arcs/arc_7/arc_7_jessy.rpy
#   arc_7_theo  -> game/arcs/arc_7/arc_7_theo.rpy
#
# lien_jessy_ilona est VOLONTAIREMENT absent de la porte : on ne gagne pas
# Ilona avec des points d'affection. Il ne sert qu'à l'intérieur d'arc_7_jessy
# pour départager « ami » et « romance ».
#
# Seuils calibrés empiriquement, voir game/agents/recalibrage.md.
# =============================================================================

label arc_6_calcul:

    # --- Dérivées ---
    $ ecoute_reelle = ilona_peut_finir_ses_phrases + interruptions_reparees
    $ controle_repetitif = interruptions_ilona - interruptions_reparees

    # --- Axe A : espace de parole construit ---
    $ espace = (autonomie_ilona * 4) \
             + (ilona_peut_finir_ses_phrases * 6) \
             + (interruptions_reparees * 6) \
             + communication \
             + confiance

    # --- Axe B : dette accumulée autour d'Ilona ---
    $ dette = (influence_theo * 3) \
            + (max(0, controle_repetitif) * 8) \
            + (pression_stream * 2) \
            + (jalousie * 2) \
            + (confidences_laplage * 4)

    # --- Posture : les souvenirs, pondérés ---
    $ posture = 0
    if souvenirs["jessy_nomme_sa_peur"]:
        $ posture += 6
    if souvenirs["jessy_repare"]:
        $ posture += 8
    if souvenirs["ilona_libre_sans_abandon"]:
        $ posture += 5
    if souvenirs["maison_respectee"]:
        $ posture += 3
    if souvenirs["theo_utilise_une_verite"]:
        $ posture -= 6

    # --- Récidive : la répétition coûte plus cher que l'erreur ---
    $ recidive = (-6 * max(0, controles - 2)) + (-3 * max(0, evitements - 3))

    # --- Score final ---
    $ arc6_score = espace + posture + recidive + arc6_mod - dette

    # --- Plancher de rachat : la réparation répétée remonte le sol ---
    if interruptions_reparees >= 2 and souvenirs["jessy_repare"]:
        $ arc6_score += 20

    # --- Verrou dur : le contrôle répété non réparé ---
    # Couper Ilona trois fois sans jamais réparer ferme la route Jessy,
    # quel que soit le score. C'est le seul comportement non rachetable.
    if controle_repetitif >= 3:
        $ arc6_route = "theo"
        # Route Theo : Ilona part vers un endroit ou on lui epargne de parler.
        jump arc_7_theo

    if arc6_score >= SEUIL_JESSY:
        $ arc6_route = "jessy"
        # Route Jessy : Ilona reste dans un endroit ou elle peut parler.
        jump arc_7_jessy
    else:
        $ arc6_route = "theo"
        # Route Theo : dette trop lourde autour d'Ilona.
        jump arc_7_theo


# =============================================================================
# LABEL DE DEBUG - à appeler manuellement pendant le réglage
# =============================================================================

label arc_6_debug_score:

    $ ecoute_reelle = ilona_peut_finir_ses_phrases + interruptions_reparees
    $ controle_repetitif = interruptions_ilona - interruptions_reparees

    systeme "ESPACE [espace] | DETTE [dette] | POSTURE [posture] | RÉCIDIVE [recidive] | MOD [arc6_mod]"
    systeme "SCORE [arc6_score] (seuil jessy [SEUIL_JESSY] / romance [SEUIL_ROMANCE])"
    systeme "autonomie [autonomie_ilona] comm [communication] confiance [confiance] lien [lien_jessy_ilona]"
    systeme "theo [influence_theo] pression [pression_stream] jalousie [jalousie] contrôle [controle_repetitif]"
    systeme "évitements [evitements] contrôles [controles] laplage [confidences_laplage] ilonanium [ilonanium_points]"
    return


# =============================================================================
# ARC 6 - RÉCAPITULATIF
#
# VARIABLES MODIFIÉES
#   globales : lien_jessy_ilona, confiance, communication, jalousie,
#              autonomie_ilona, influence_theo, pression_stream,
#              ilona_peut_finir_ses_phrases, interruptions_ilona,
#              interruptions_reparees, confidences_laplage, jugement_laplage,
#              ilonanium_points, evitements, controles
#   souvenirs : jessy_nomme_sa_peur, maison_respectee,
#               theo_utilise_une_verite, ilona_veut_streamer_serieusement
#   locales : arc6_stylo, arc6_offre_theo, arc6_conversation,
#             arc6_derniere_construction, arc6_flashback,
#             arc6_mod, arc6_score, arc6_route
#
# CHOIX À CONSÉQUENCE
#   MENU 3 (toit) -> arc6_mod, seul modificateur direct du point de bascule
#                    (-20 à +25 ; la 5e option n'existe que si le joueur
#                     a déjà réparé une interruption)
#   MENU 2 (offre Théo) -> autonomie_ilona / influence_theo
#   MENU 4 (gâteau-planète) -> binaire : elle le mange (5e objet cosmique,
#                    +1 ilonanium) ou elle le garde entier (aucun point).
#                    Sans ce point, ending_ilonanium devient inatteignable.
#   MENU 5 (dernière construction) -> dernier ajustement de l'espace
#
# ASSETS
#   arc6_bg(nom, secours) teste images/scenes/arc_6/bg_arc6_<nom>.jpg et
#   retombe sur un décor d'un arc précédent s'il n'existe pas encore.
#   Les backgrounds principaux de l'arc 6 sont fournis : gym_ceremony,
#   classroom_morning, classroom_festive. Ancien nom "bg arc6 classroom empty"
#   -> "classroom festive".
#
# FILS FERMES
#   stylo violet rendu (ou non)
#   enveloppe de Sofiane lue par Allan
#   secret du maid café
#   Allan confronte Théo, puis apprend son départ (scène 2.6)
#   Ilona dit « qu'on me foute la paix » à Jessy ET Théo
#   Ilona reprend son projet de stream à son compte
#   (conditionné : si elle ne l'avait jamais dit, l'arc 6 est la première fois)
#   Ilona craque (arc5_ilona_a_pleure enfin payé)
#   question de Laplage de février
#   phrase jamais finie du train d'avril (arc 1)
#   5e objet cosmique : le gâteau-planète
#
# FILS LAISSÉS OUVERTS POUR L'ARC 7
#   l'AE86 de Sofiane / l'été en montagne
#   Micka et les enveloppes
#   la nature de Laplage
#   ce qu'Ilona a écrit sur la veste d'uniforme de Jessy
#   le départ de Théo le 6 avril
#   le 6e objet cosmique (bloc-lune) : à collecter dans arc_7_jessy
# =============================================================================
