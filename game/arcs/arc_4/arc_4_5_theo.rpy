# Arc 4.5 - La marche avec Théo
# Déclenché si arc4_ilona_avec_theo = True (influence_theo >= 5, confiance <= 2, arc4_limite_ilona == "demande_theo")
# Ce fichier montre la scène du point de vue omniscient, pas celui de Jessy
# CONTEXTE : Ilona vient de vivre la scène du marché de Noël. Jessy a posé une question jalouse sur le carnet de Théo.
# Elle a d'abord refusé de marcher avec Théo ("J'ai dit avec Allan"), puis l'a rappelé.
# Elle a dit à Jessy : "J'ai besoin de parler à quelqu'un qui ne me demande pas de le rassurer."

# Images
# Le parc résidentiel sert aux plans de marche et de banc tant que la rue dédiée n'existe pas.
image bg arc4_5 street winter night = im.Scale("images/scenes/arc_4/bg_arc4_park_bench.jpg", 1920, 1080)
image bg arc4_5 park bench = im.Scale("images/scenes/arc_4/bg_arc4_park_bench.jpg", 1920, 1080)

# Sprites Laplage maid
image laplage maid neutral = speaker_sprite("laplage", "images/personnages/laplage/maid/neutral.png", 843, 1264)
image laplage maid thumb_horizontal = speaker_sprite("laplage", "images/personnages/laplage/maid/thumb_horizontal.png", 843, 1264)

transform laplage_maid_counter:
    xalign 0.50
    yalign 1.0
    zoom 0.50

# Variables locales
default arc4_5_theo_proposition = ""
default arc4_5_ilona_reaction = ""

label arc_4_5_theo:
    stop music fadeout 1.0
    stop ambiant1 fadeout 1.0
    scene black
    with Dissolve(1.0)
    
    systeme "Quelque part dans la ville, la neige commence à tomber."
    systeme "Après la scène au marché de Noël, Ilona avait dit qu'elle rentrait avec Allan."
    systeme "Théo avait proposé de l'accompagner aussi. Elle avait refusé : « J'ai dit avec Allan. »"
    systeme "Théo était parti."
    systeme "Mais quelque chose avait changé."
    systeme "Elle l'avait rappelé : « Finalement... je veux bien marcher un peu. Avant de rentrer. »"
    systeme "Jessy est rentré chez lui en métro. Il ne voit pas ce qui suit."
    
    $ renpy.pause(1.5, hard=True)
    play music audio.citynight volume 0.8 loop fadein 1.0
    scene bg arc4_5 street winter night
    with Dissolve(2.0)
    
    show theo neutral at char_left
    show ilona fatigue at char_right
    with dissolve
    
    systeme "Théo et Ilona suivent l'allée d'un petit parc résidentiel. Le froid mord, mais aucun des deux ne propose de rentrer."
    systeme "Dans son sac, Ilona sent le poids du carnet que Théo lui a offert. Et la question de Jessy, encore chaude."
    systeme "« Son cadeau... ça veut dire quelque chose pour toi ? »"
    systeme "Elle avait répondu : « Tu me demandes de te rassurer avant même que j'aie le temps de comprendre ce que moi je ressens. »"
    systeme "Puis elle avait dit à Jessy : « J'ai besoin de parler à quelqu'un qui ne me demande pas de le rassurer. »"
    systeme "Et c'est pour ça qu'elle marche avec Théo maintenant."
    systeme "Mais elle ne sait pas encore si c'est une respiration ou une fuite."
    
    t "Tu trembles."
    i "C'est rien."
    t "Je sais que c'est rien. Mais tu trembles quand même."
    
    systeme "Il enlève son écharpe. Pas théâtralement. Juste le geste de quelqu'un qui a remarqué."
    
    show theo reassuring
    
    t "Tiens."
    i "Et toi ?"
    t "J'ai l'habitude. Le froid, ça se gère."
    
    systeme "Elle hésite. Puis elle prend l'écharpe."
    systeme "C'est un geste simple. Trop simple pour être analysé. Mais Théo analyse quand même."
    
    $ lien_ilona_theo += 1
    
    # Pause au banc, dans le même parc résidentiel.
    systeme "Ils ralentissent près du banc sous le lampadaire. Les illuminations de Noël clignotent au loin."

    show theo neutral at char_left
    show ilona fatigue at char_right
    with dissolve
    
    t "Tu peux parler, tu sais. Ou pas. Je ne vais pas te demander de choisir quoi que ce soit."
    
    systeme "C'est exactement ce qu'il fallait dire. C'est pour ça que c'est dangereux."
    
    show ilona neutral
    
    i "Jessy a essayé. Vraiment. Je le vois."
    t "Je sais."
    i "Alors pourquoi j'ai l'impression que ça ne suffit pas ?"
    systeme "Elle pense à ce qu'elle a dit au marché : « Tu me demandes de te rassurer avant même que j'aie le temps de comprendre ce que moi je ressens. »"
    systeme "Elle avait posé une limite. Jessy avait transformé le carnet de Théo en verdict."
    systeme "Et maintenant, elle marche avec Théo parce qu'elle a dit qu'elle avait besoin de ne pas rassurer quelqu'un."
    systeme "Mais elle se demande si c'est un besoin légitime ou une fuite."
    
    show theo reassuring
    
    t "Parce qu'essayer et réussir, c'est pas la même chose. Et tu as le droit d'attendre plus qu'un effort."
    
    systeme "Ce n'est pas faux. C'est même vrai. C'est exactement ce qu'Ilona a ressenti au marché."
    systeme "Mais Théo sait que les vérités bien placées ouvrent des portes."
    systeme "Et qu'elles créent aussi des dettes."
    
    $ influence_theo += 2
    
    i "Il a peur de me perdre."
    t "Oui."
    i "Mais sa peur, c'est... c'est lourd à porter."
    
    show theo neutral
    
    t "C'est lourd parce qu'il te demande de le rassurer alors que toi, tu as juste besoin de respirer."
    
    systeme "Ilona ne répond pas. Elle regarde les lumières."
    if arc3_fin_minecraft == "destruction":
        systeme "Elle pense à la maison Minecraft. Au trou dans la cuisine d'été. Aux phrases qu'elle n'a jamais pu finir."
    elif arc3_fin_minecraft == "porte_fermee":
        systeme "Elle pense à la maison Minecraft. À la porte fermée qu'elle n'a pas encore rouverte. Aux phrases qu'elle n'a jamais pu finir."
    else:
        systeme "Elle pense à la maison Minecraft. Aux détails qu'ils ont construits ensemble. Aux phrases qu'elle n'a jamais pu finir."
    
    show ilona fatigue
    
    i "Parfois je me demande si je suis obligée de choisir."
    t "Obligée par qui ?"
    i "Par... tout le monde. Les rumeurs. Jessy. Toi."
    systeme "Elle pense au carnet dans son sac. À la question de Jessy : « Son cadeau... ça veut dire quelque chose pour toi ? »"
    if arc4_cadeau_jessy in ("miniature_souvenir", "blague_interne", "miniature_aveu"):
        systeme "Elle pense à la miniature qu'elle n'a jamais regardée vraiment, parce que Jessy a transformé ça en épreuve de loyauté."
    elif arc4_cadeau_jessy == "cadeau_couteux":
        systeme "Elle pense à l'écharpe qu'elle a reçue sans vraiment la vouloir. Un cadeau né de la panique de Jessy."
    else:
        systeme "Elle pense à l'absence de cadeau. Jessy avait quelque chose, mais n'a pas osé le donner. Ou a choisi de parler à la place."
    
    show theo defensive at char_left
    
    t "Moi ?"
    
    systeme "Premier craquement dans le masque. Juste une seconde."
    
    show theo reassuring
    
    t "Je ne te demande rien, Ilona. Je te propose juste... un espace."
    
    # Choix invisible - ce qu'Ilona ressent
    # Ces choix sont basés sur les variables accumulées, pas sur le joueur
    # Le joueur ne contrôle pas Ilona dans cette scène
    
    systeme "La neige tombe plus fort. Ilona doit décider ce qu'elle fait de cette conversation."
    
    # Détermination de la réaction d'Ilona.
    # L'ordre compte : une emprise déjà forte de Théo court-circuite tout le reste,
    # même si Jessy a bien communiqué. Sinon, ce que Jessy a construit décide.
    # Seuils calés sur le barème de game/agents/recalibrage.md.
    if influence_theo >= 14 and autonomie_ilona <= 0:
        $ arc4_5_ilona_reaction = "accepte"
    elif communication >= 15 or ilona_peut_finir_ses_phrases >= 3:
        $ arc4_5_ilona_reaction = "directe"
    elif autonomie_ilona >= 15:
        $ arc4_5_ilona_reaction = "prudente"
    else:
        $ arc4_5_ilona_reaction = "accepte"

    if arc4_5_ilona_reaction == "accepte":
        # Ilona est épuisée et vulnérable, elle accepte l'aide de Théo
        $ influence_theo += 3
        $ autonomie_ilona -= 3
        
        show ilona neutral
        
        i "Un espace... c'est peut-être ce dont j'ai besoin."
        
        systeme "Elle soupire. La fatigue transparaît."
        
        show ilona fatigue
        
        i "J'ai l'impression que tout le monde... attend quelque chose de moi."
        
        show theo neutral at char_left
        
        t "Qu'est-ce que toi, tu veux ?"
        
        systeme "La question est simple. Directe. Ilona ne s'y attendait pas."
        
        show ilona embarrassed
        
        i "Je... je sais pas."
        t "Pas maintenant. Plus tard. Dans six mois. Dans un an."
        t "Qu'est-ce que tu veux faire ?"
        
        systeme "Ilona réfléchit. Personne ne lui demande ça. On lui demande ce qu'elle ressent. Ce qu'elle veut dire. Mais jamais ce qu'elle veut faire."
        
        show ilona neutral
        
        i "J'aimerais... avoir un truc à moi. Un espace où je décide."
        t "Comme quoi ?"
        i "Je sais pas. Peut-être... streamer. Pour de vrai."
        
        systeme "Elle dit ça presque timidement. Comme si ce n'était pas sérieux. Comme si c'était juste un rêve."
        
        i "Pas juste essayer de temps en temps. Mais vraiment. Avec un planning. Une communauté. Quelque chose que je construis."
        
        show theo reassuring at char_left
        
        t "Tu sais, je pourrais t'aider avec ça."
        
        systeme "Ilona lève les yeux. Théo sourit. Pas le sourire moqueur. Le sourire rassurant."
        
        t "Modérer le chat. Gérer les horaires. Filtrer les commentaires qui te fatiguent."
        t "Pas en prenant ta place. Juste en protégeant l'espace que tu veux construire."
        
        systeme "Il dit ça avec une douceur naturelle. Comme si c'était évident."
        systeme "Comme si aider, c'était juste ça. Simple. Généreux. Sans contrepartie."
        
        show ilona neutral
        
        i "Tu ferais ça ?"
        t "Bien sûr."
        
        systeme "« Bien sûr. » Deux mots. Une dette qui commence."
        systeme "Ilona ne voit pas encore la cage. Elle voit juste quelqu'un qui écoute ses rêves et propose de les rendre possibles."
        
        $ arc4_5_theo_proposition = "gestion_stream"
        $ pression_stream += 4
        $ remember("theo_utilise_une_verite")
        $ remember("ilona_veut_streamer_serieusement")
    
    elif arc4_5_ilona_reaction == "directe":
        # Ilona a appris à poser des questions directes
        $ communication += 3
        
        show ilona determined
        
        i "Théo, est-ce que tu m'aides parce que tu veux m'aider... ou parce que tu veux être celui qui m'aide ?"
        
        systeme "Silence."
        systeme "La neige tombe. Théo ne s'attendait pas à ça."
        
        show theo defensive
        
        t "C'est quoi la différence ?"
        i "La différence, c'est que dans un cas, tu t'en vas quand je vais mieux. Dans l'autre, tu restes pour que j'aie besoin de toi."
        
        systeme "Théo ouvre la bouche. Rien ne sort."
        systeme "Ilona vient de mettre des mots sur quelque chose qu'il n'avait jamais regardé en face."
        
        show theo neutral
        
        t "Je... je veux t'aider. Vraiment."
        i "Je sais. Mais « vraiment », ça veut dire quoi, pour toi ?"
        
        systeme "Il n'a pas de réponse. Pas ce soir."
        
        $ arc4_5_theo_proposition = "question"
        $ influence_theo = max(0, influence_theo - 3)
    
    else:
        # Ilona garde une distance prudente
        $ autonomie_ilona += 3
        
        show ilona determined
        
        i "Théo... je ne sais pas ce que je veux. Et je n'ai pas envie qu'on me dise ce que je devrais vouloir."
        
        show theo neutral
        
        t "Je comprends."
        
        systeme "Il comprend. C'est vrai. Mais comprendre et accepter, ce n'est pas la même chose."
        
        i "Jessy fait des erreurs. Toi aussi, parfois."
        t "Moi ?"
        i "Tu parles comme si tu avais toutes les réponses. Et moi je ne veux pas de réponses. Je veux juste... du temps."
        
        systeme "Le sourire de Théo reste, mais quelque chose se fige derrière ses yeux."
        
        show theo neutral at char_left
        
        t "D'accord. Prends le temps que tu veux."
        
        systeme "Il ne supporte pas bien qu'on refuse son aide. Mais il est patient."
        
        $ arc4_5_theo_proposition = "temps"
    
    
    # Transition maid café
    scene black
    with Dissolve(0.5)
    
    systeme "Ils quittent les allées résidentielles et marchent encore un moment. Le froid devient sérieux."
    
    $ renpy.pause(1.0, hard=True)
    scene bg arc4_maid_cafe_exterior
    with Dissolve(1.5)
    
    show theo neutral at char_left
    show ilona fatigue at char_right
    with dissolve
    
    systeme "Ils arrivent dans une petite rue commerçante presque vide, encore mouillée par la neige."
    systeme "La plupart des boutiques ont déjà baissé leur rideau."
    systeme "Mais une vitrine reste allumée, chaude au milieu du bleu de la nuit, avec une pancarte : « MAID CAFÉ — OUVERT JUSQU'À MINUIT »."
    
    t "On devrait se réchauffer."
    
    show ilona embarrassed
    
    i "Un maid café ?"
    
    show theo smirk at char_left
    
    t "Pourquoi pas. T'as peur ?"
    i "Non. C'est juste... inattendu."
    t "C'est ouvert. C'est chaud. C'est suffisant."
    
    systeme "Ils entrent."
    play music audio.maidcafe volume 0.6 loop fadeout 1.0 fadein 1.0
    scene bg arc4_maid_cafe_interior
    with fade
    
    systeme "L'intérieur est plus calme que prévu. Quelques tables occupées. Une décoration soignée sans être kitsch."
    systeme "Et derrière le comptoir, presque invisible dans la pénombre..."
    
    # Apparition Laplage en maid
    $ renpy.pause(0.5, hard=True)
    play sound audio.wow volume 1.0
    show laplage maid neutral at laplage_maid_counter
    with dissolve
    
    systeme "Monsieur Laplage."
    systeme "En tenue de maid."
    systeme "Il essuie un verre. Expression parfaitement neutre."
    
    laplage "Bonsoir."
    
    show theo annoyed at char_left
    show ilona embarrassed at char_right
    with dissolve
    
    systeme "Silence absolu."
    
    t "...Le Messi ?"
    
    laplage "Théo. Ilona."
    
    systeme "Il pose le verre. En prend un autre. Aucune surprise dans son ton."
    
    show ilona neutral
    
    i "Vous... vous travaillez ici ?"
    laplage "Temporairement."
    laplage "Quelqu'un devait remplacer quelqu'un qui devait remplacer quelqu'un."
    laplage "La chaîne s'arrête à moi pour ce soir."
    
    systeme "Théo ne sait pas quoi faire de cette phrase. Ilona non plus."
    
    show theo neutral
    
    t "On va prendre deux boissons."
    
    laplage "Café ou thé ?"
    i "Thé."
    t "Café."
    
    systeme "Laplage les sert avec une précision étrange. Ni trop rapide, ni trop lent."
    systeme "Il pose les tasses devant eux sans un mot. Puis il les regarde."
    
    laplage "Vous rentrez ensemble ?"
    i "Non. On se sépare après."
    
    show laplage maid thumb_horizontal at laplage_maid_counter
    
    laplage "Les chemins qui divergent font moins de bruit."
    laplage "Mais le silence n'est pas toujours une paix."
    
    systeme "Il tend son pouce. Ni levé. Ni baissé. Juste horizontal."
    systeme "Puis il retourne au comptoir et disparaît dans l'ombre."
    
    $ jugement_laplage += 1
    
    hide laplage
    with dissolve
    
    # Séparation
    scene black
    with Dissolve(0.5)
    
    systeme "Dehors, la neige s'est calmée."
    
    $ renpy.pause(1.0, hard=True)
    play music audio.citynight volume 0.6 loop fadeout 1.0 fadein 1.0
    scene bg arc4_maid_cafe_exterior
    with Dissolve(1.5)
    
    show theo neutral at char_left
    show ilona neutral at char_right
    with dissolve
    
    t "Je te raccompagne ?"
    i "Non. Je connais le chemin."
    
    show theo reassuring
    
    t "D'accord. Message-moi quand t'es arrivée."
    i "Théo..."
    t "Oui ?"
    
    show ilona fatigue
    
    if arc4_5_ilona_reaction == "accepte":
        i "Merci. Pour l'écharpe. Et pour... tout ça."
        t "C'est normal."
        systeme "Normal. Comme si c'était une évidence. Comme si refuser n'avait jamais été une option."
        $ lien_ilona_theo += 1
        
    elif arc4_5_ilona_reaction == "prudente":
        i "On verra. Pour tout ça. Je te dis demain."
        t "Pas de pression."
        systeme "Pas de pression. Mais la proposition reste en suspens. Les propositions de Théo restent toujours en suspens."
        
    else:  # directe
        i "Réponds à ma question. Un jour."
        show theo defensive
        t "...Je vais y réfléchir."
        systeme "C'est peut-être la première fois que quelqu'un lui demande de réfléchir à ce qu'il veut vraiment."
    
    # Fin de la scène
    hide theo
    hide ilona
    with dissolve
    stop music fadeout 2.0
    scene black
    with Dissolve(1.5)
    
    systeme "Ilona rentre seule. L'écharpe de Théo est toujours autour de son cou."
    
    if arc4_cadeau_jessy in ("miniature_souvenir", "blague_interne", "miniature_aveu"):
        systeme "Elle pense à Jessy. À la miniature qu'elle n'a pas vraiment regardée."
    elif arc4_cadeau_jessy == "cadeau_couteux":
        systeme "Elle pense à Jessy. À l'écharpe qu'elle a reçue sans vraiment la vouloir."
    else:
        systeme "Elle pense à Jessy. Au cadeau qu'il n'a pas osé lui donner."
    
    systeme "Elle pense au carnet de Théo. À cette façon qu'il a de toujours avoir une réponse."
    
    if arc4_5_ilona_reaction == "directe":
        systeme "Elle pense à la question qu'elle a posée : « Est-ce que tu m'aides parce que tu veux m'aider... ou parce que tu veux être celui qui m'aide ? »"
        systeme "Et elle se demande si avoir une réponse, c'est la même chose que poser la bonne question."
    elif arc4_5_ilona_reaction == "accepte":
        systeme "Elle pense à ce qu'elle a dit. À son rêve de stream. À la proposition de Théo."
        systeme "« Je pourrais t'aider. Modérer. Gérer. Protéger l'espace que tu veux construire. »"
        systeme "Ça semblait si simple. Si naturel. Comme si partager un rêve suffisait pour que quelqu'un veuille le protéger."
        systeme "Mais quelque chose la dérange. Pas assez pour refuser. Juste assez pour se demander."
    else:  # prudente
        systeme "Elle pense à ce qu'elle a dit : « Je ne sais pas ce que je veux. »"
        systeme "C'est vrai. Mais au moins, elle le sait. Et elle a dit non à quelqu'un qui avait déjà une réponse toute faite."
    
    systeme "Mais surtout, elle se demande si elle n'est pas en train de remplacer une cage par une autre."
    systeme "Plus confortable. Mieux éclairée. Avec quelqu'un qui se souvient de tout ce qu'elle dit."
    
    if arc4_5_ilona_reaction == "accepte":
        systeme "Avec quelqu'un qui a écouté son rêve. Qui veut l'aider à le construire. Qui veut protéger son espace."
        systeme "Mais protéger... ça veut dire contrôler quoi, exactement ?"
    
    systeme "Mais une cage quand même."
    
    $ renpy.pause(2.0, hard=True)
    stop music fadeout 1.0 
    stop ambiant1 fadeout 1.0
    
    # Retour vers la suite (le jeu continue normalement, mais avec arc4_ilona_avec_theo = True)
    return
