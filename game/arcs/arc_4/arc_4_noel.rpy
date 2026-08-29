# Arc IV - Noel : le cadeau qui dit trop de choses.
# Les variables importantes restent centralisees dans script.rpy.

image bg arc4 train inside = im.Scale("images/scenes/arc_4/bg_arc4_train_inside.jpg", 1920, 1080)
image bg arc4 illuminations = im.Scale("images/scenes/arc_4/bg_arc4_illuminations.jpg", 1920, 1080)
image bg arc4 shopping gallery = im.Scale("images/scenes/arc_4/bg_arc4_shopping_gallery.jpg", 1920, 1080)
image bg arc4 christmas market = im.Scale("images/scenes/arc_4/bg_arc4_christmas_market.jpg", 1920, 1080)
image bg arc4 riverside winter = im.Scale("images/scenes/arc_4/bg_arc4_riverside_winter.jpg", 1920, 1080)
image bg arc4 minecraft winter night = im.Scale("images/scenes/arc_2/bg_arc2_minecraft_house_summer_night.jpg", 1920, 1080)

image laplage christmas neutral = speaker_sprite("laplage", "images/personnages/laplage/christmas/neutral.png", 843, 1264)
image laplage christmas thumb_up = speaker_sprite("laplage", "images/personnages/laplage/christmas/thumb_up.png", 843, 1264)
image laplage christmas thumb_horizontal = speaker_sprite("laplage", "images/personnages/laplage/christmas/thumb_horizontal.png", 843, 1264)

# Variables locales d'arc : elles gardent la trace du sens donne aux cadeaux et aux limites posees.
default arc4_cadeau_jessy = ""
default arc4_reaction_cadeau_theo = ""
default arc4_limite_ilona = ""
default arc4_fin_minecraft = ""
default arc4_carte_sofiane_lue = False
default arc4_mochi_cosmique = False
default arc4_ilona_avec_theo = False


label arc_4_noel:
    scene bg arc4 train inside
    with fade

    systeme "Arc IV - Noël : le cadeau qui dit trop de choses."
    systeme "Décembre arrive sans demander si quelqu'un a fini de comprendre septembre."
    systeme "Dans le train du matin, les vitres gardent la buée des souffles, et les annonces de soldes de Noël collent aux fenêtres comme des promesses mal placées."

    show jessy neutral at char_left
    show ilona neutral at char_right

    if arc3_fin_minecraft == "destruction":
        systeme "Depuis le festival, la maison Minecraft a un trou que personne n'a réparé."
        systeme "Jessy l'a regardé plusieurs soirs sans poser un bloc."
        i "Tu t'es connecté hier ?"
        j "Oui."
        i "Tu n'as rien touché."
        j "Non."
        systeme "Ilona garde les yeux sur la vitre. Elle ne dit pas merci. Elle ne dit pas que c'était important non plus."
    elif arc3_fin_minecraft == "porte_fermee":
        systeme "Depuis le festival, la porte inutile est fermée dans la maison Minecraft."
        systeme "Elle ne menait nulle part. C'est exactement pour ça que sa fermeture se voit."
        i "La porte est toujours fermée ?"
        j "Oui."
        i "Bien."
        j "Pour ce soir, ou pour plus longtemps ?"
        i "Je ne sais pas encore."
    elif arc3_fin_minecraft == "panneau_finir_phrase":
        systeme "Le panneau posé près de la salle moyennement importante est devenu un détour habituel."
        i "Tu as relu le panneau hier ?"
        j "Deux fois."
        i "Tu sais que ce n'est pas un règlement intérieur ?"
        j "Je l'ai pris comme un avertissement municipal."
        i "Très sérieux."
    elif arc3_fin_minecraft == "rangement_silencieux":
        systeme "La cuisine d'été rangée a moins de coffres, moins de lanternes, et plus de place pour respirer."
        i "J'ai ajouté un tapis hier."
        j "Dans la cuisine ?"
        i "Oui. Elle avait l'air trop punie."
        j "C'est une expression étrange."
        i "C'est une cuisine étrange."
    else:
        systeme "La maison Minecraft garde la trace du festival comme elle peut : une lanterne, une porte inutile, un souvenir qui éclaire sans expliquer."
        i "Je crois que la lanterne tient toujours."
        j "Elle éclaire une porte qui ne sert à rien."
        i "Donc elle fait très bien son travail."

    systeme "Le train ralentit près de la grande galerie commerciale. Des guirlandes clignotent déjà au-dessus des escalators."
    
    if jalousie >= 3:
        systeme "Jessy regarde Ilona. Elle regarde la vitre. Il y a trois mois, il aurait demandé à quoi elle pense."
        systeme "Maintenant, il a peur de la réponse."
    elif confiance >= 3 and communication >= 3:
        systeme "Le silence entre eux tient sans se casser. Pas toujours confortable. Mais moins dangereux qu'avant."
    
    i "Allan a envoyé le planning ?"
    j "Oui. Marché de Noël après les cours. Alexandre a répondu avec un plan d'évacuation des stands de nourriture."
    i "Priorité raisonnable."
    j "Il a aussi écrit : si Monsieur Laplage est Père Noël, je veux savoir qui valide les listes."
    i "Je ne veux pas savoir."
    systeme "Elle sourit, puis regarde les illuminations qui passent derrière la vitre."
    
    if pression_stream >= 2:
        systeme "Le sourire ne monte pas jusqu'aux yeux. Ilona est fatiguée. Jessy le voit. Il ne sait pas encore quoi en faire."
    
    i "Tu viens ce soir ?"
    j "Oui."
    
    if arc2_choix_activite_theo == "suivre":
        systeme "Jessy pense à la plage. Au moment où il a suivi au lieu de faire confiance."
        systeme "Il n'a pas refait cette erreur depuis. Mais le souvenir pèse encore."
    
    systeme "Jessy a presque ajouté : j'ai quelque chose pour toi."
    systeme "Il garde la phrase. Elle devient plus lourde dans sa poche que le petit paquet qu'il transporte depuis le matin."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc4 shopping gallery
    with fade

    show alex neutral at char_left
    show jessy embarrassed at char_right

    systeme "Après les cours, Jessy retrouve Alexandre devant une boutique de papeterie. Dans le sac de Jessy, le paquet menace de ressembler à une décision."
    x "Montre."
    j "Non."
    x "Tu m'as demandé de t'aider à choisir le papier. J'ai acquis un droit de regard historique."
    j "C'est un très mauvais droit."
    x "Comme toutes les architectures importantes."
    systeme "Jessy finit par sortir une petite boîte emballée dans un papier bleu sombre."
    x "C'est la miniature ?"
    j "Oui."
    x "Avec le couloir sans sortie ?"
    j "Oui."
    x "La cuisine trop grande ?"
    j "Oui."
    x "La pièce que personne ne comprend ?"
    j "Il y en a plusieurs."
    x "Respect du matériau source."

    if arc3_fin_minecraft == "destruction":
        j "J'ai aussi laissé une partie cassée."
        x "Celle qu'elle a détruite ?"
        j "Oui."
        x "Tu lui offres un souvenir ou une preuve que tu as retenu la leçon ?"
    elif arc3_fin_minecraft == "porte_fermee":
        j "J'ai mis la porte fermée."
        x "Tu lui offres une porte fermée à Noël."
        j "Dit comme ça, c'est terrible."
        x "Dit autrement aussi. Mais ça peut être juste."
    else:
        x "Tu lui offres un souvenir ou une réponse ?"

    systeme "La question d'Alexandre tombe sans sourire. Il ne cherche pas à être profond. C'est parfois comme ça qu'il y arrive."
    j "Je ne sais pas."
    x "Alors décide avant ce soir."
    j "Tu dis ça comme si c'était facile."
    x "Non. Je dis ça parce que si tu ne décides pas, ta peur le fera à ta place."
    
    if "jessy_nomme_sa_peur" in souvenirs and souvenirs["jessy_nomme_sa_peur"]:
        systeme "Jessy se souvient. La plage. Le festival. Les moments où il a nommé sa peur au lieu de la laisser décider."
        systeme "Ça n'a pas toujours marché. Mais c'était mieux que le silence."
    
    systeme "Jessy regarde le paquet. Il est léger. Beaucoup trop léger pour porter tout ça."

    menu:
        "Alexandre attend. La miniature pèse dans le sac de Jessy. Il doit décider ce qu'elle porte."

        "Offrir la miniature avec ses erreurs, comme témoin de ce qui a existé.":
            $ arc4_cadeau_jessy = "miniature_souvenir"
            $ lien_jessy_ilona += 1
            $ confiance += 1
            $ communication += 1
            $ jalousie += 1
            $ remember("maison_respectee")
            j "Je vais lui offrir ce qu'on a construit. Avec le couloir inutile. Avec la pièce cassée."
            x "Donc un souvenir, pas une promesse."
            j "Oui. Mais j'ai quand même peur qu'elle voie une promesse."
            x "Elle verra ce qu'elle verra. Tu ne peux pas contrôler ça."
            j "C'est ça qui me terrifie."
            systeme "Alexandre regarde la boîte. Il ne dit pas que c'est une bonne idée. Il ne dit pas que c'est une mauvaise."
            x "Au moins, c'est honnête."

        "Offrir la miniature mais en blague, pour désamorcer le poids.":
            $ arc4_cadeau_jessy = "blague_interne"
            $ lien_jessy_ilona += 2
            $ communication += 2
            $ pression_stream -= 1
            $ confiance += 1
            j "Je vais ajouter un panneau ridicule. Pièce moyennement importante, édition neige."
            x "Tu transformes un souvenir lourd en connivence."
            j "Oui."
            x "C'est lâche ou malin ?"
            j "Les deux. Surtout lâche."
            x "Mais elle va rire."
            j "J'espère. Et j'espère que le rire cache pas juste que j'ai eu trop peur de dire un truc sérieux."
            systeme "Alexandre sourit. Petit."
            x "Bienvenue dans l'humanité, Jessy."

        "Paniquer et acheter un cadeau neutre à la place.":
            $ arc4_cadeau_jessy = "cadeau_couteux"
            $ lien_jessy_ilona -= 1
            $ confiance -= 1
            $ jalousie += 2
            $ influence_theo += 2
            $ pression_stream += 2
            systeme "Jessy range la miniature au fond de son sac. Trop fort. Comme pour l'étouffer."
            j "Je vais prendre autre chose."
            x "Comme quoi ?"
            j "Quelque chose de bien. De cher. Qui fait adulte."
            x "Jessy."
            j "Quoi ?"
            x "Tu viens de décider d'avoir peur."
            systeme "Jessy achète une écharpe. Belle. Chère. Vide."
            systeme "Alexandre ne dit rien. Son silence pèse plus lourd que le prix du cadeau."

        "Ne rien offrir ce soir et miser sur la conversation seule.":
            $ arc4_cadeau_jessy = "discussion_honnete"
            $ communication += 3
            $ confiance += 2
            $ autonomie_ilona += 2
            $ jalousie -= 1
            $ remember("jessy_nomme_sa_peur")
            j "Je crois que j'ai fait cette miniature pour éviter de parler."
            x "Et ?"
            j "Je vais parler. Sans objet entre nous."
            x "C'est le choix le moins rassurant."
            j "Ouais."
            x "Donc probablement le plus juste."
            systeme "Jessy range la boîte. Elle reste dans le sac. Pas jetée. Juste... en attente."

        "Offrir la miniature en avouant qu'elle porte trop de choses.":
            $ arc4_cadeau_jessy = "miniature_aveu"
            $ lien_jessy_ilona += 2
            $ communication += 2
            $ confiance += 1
            $ jalousie += 1
            $ pression_stream += 1
            $ remember("maison_respectee")
            j "Je vais lui donner. Mais je vais aussi lui dire que je sais que ça veut trop dire."
            x "Tu vas offrir un cadeau avec un avertissement ?"
            j "Oui. Parce que je refuse de faire comme si c'était juste un objet mignon."
            x "C'est honnête. C'est aussi un peu flippant."
            j "Tout est flippant ce soir."
            systeme "Alexandre acquiesce. Il ne peut pas le contredire."

    hide alex
    hide jessy
    with dissolve

    scene bg arc4 illuminations
    with fade

    systeme "En sortant de la galerie, Jessy traverse la rue illuminée vers le marché avec l'impression que chaque guirlande souligne ce qu'il n'a pas encore su dire."
    systeme "Les lumières rendent la ville plus douce. Elles ne rendent pas les choix plus simples."

    scene bg arc4 christmas market
    with fade

    show allan neutral at char_left
    show ilona smile at char_midleft
    show theo neutral at char_midright
    show jessy neutral at char_right

    systeme "Une heure plus tard, le marché de Noël du quartier ouvre sous des guirlandes blanches."
    systeme "Les stands vendent du chocolat chaud, des porte-clés, des gâteaux trop décorés, et des souvenirs dont personne n'a besoin avant de les voir."
    a "Objectif du soir : manger quelque chose en forme d'étoile avant Ilona."
    i "Trop tard mentalement."
    t "Le stand près de l'entrée a des mochi au sucre pailleté."
    i "Tu as déjà repéré les snacks ?"
    t "Tu regardais les affiches en arrivant."
    systeme "Il le dit doucement, comme si c'était seulement une attention."
    systeme "Jessy remarque qu'Ilona sourit. Il remarque aussi qu'elle cherche immédiatement quelque chose à manger, comme si le sourire devait s'occuper la bouche."
    
    if influence_theo >= 2:
        systeme "Théo sait toujours ce qu'Ilona regarde. Ce qu'elle veut. Jessy le sait aussi."
        systeme "La différence, c'est que Théo le transforme en geste avant que Jessy ait fini de réfléchir."
    elif lien_ilona_theo >= 2:
        systeme "Ilona sourit à Théo différemment qu'aux autres. Pas beaucoup. Juste assez pour que Jessy le voie."
    
    i "Je vais prendre un mochi."
    a "Défaite stratégique."

    hide allan
    with dissolve

    show theo reassuring at char_midright
    systeme "Théo sort un petit paquet plat de la poche de son manteau."
    t "Avant que la foule devienne impossible."
    i "Qu'est-ce que c'est ?"
    t "Un rien."
    systeme "Ilona défait le papier avec prudence."
    systeme "À l'intérieur, un carnet de croquis minuscule, couverture noire, coins renforcés, avec une petite étiquette collée à l'intérieur."
    t "Tu avais dit à la plage que tu oubliais toujours les idées qui venaient quand tu étais dehors."
    t "Il est assez petit pour tenir dans ta poche."
    systeme "Ilona ne répond pas tout de suite."
    systeme "Elle avait effectivement dit ça. Une seule fois. En juillet, entre deux phrases, juste avant de regarder les mares."
    systeme "Jessy sent quelque chose se tordre dans son ventre. Un souvenir qu'il avait aussi. Théo l'a transformé en objet."
    i "Je ne pensais pas que tu t'en souviendrais."
    t "Je fais attention."
    systeme "La phrase a déjà existé. Elle revient avec un papier plus joli."
    systeme "Jessy regarde les doigts d'Ilona sur le carnet. Ils ne bougent pas exactement comme quand elle tient quelque chose de neutre."

    menu:
        "Théo vient d'offrir à Ilona un cadeau très précis. Jessy sent quelque chose se déchirer entre rester digne et hurler."

        "Reconnaître le cadeau mais nommer sa propre douleur.":
            $ arc4_reaction_cadeau_theo = "reconnaitre"
            $ communication += 2
            $ confiance += 1
            $ jalousie += 2
            $ autonomie_ilona += 1
            j "C'est un beau cadeau."
            systeme "Théo tourne la tête vers lui, surpris."
            j "Et ça fait mal de voir quelqu'un d'autre se souvenir aussi bien."
            systeme "La phrase sort sans fard. Ilona reste immobile."
            i "Jessy..."
            j "Non, c'est vrai. Tu oublies tes idées dehors. Il s'en est souvenu. C'est juste."
            j "Ça reste douloureux."
            systeme "Théo ne sourit plus. Ilona regarde Jessy différemment. Pas avec pitié. Avec quelque chose de plus direct."
            i "Merci d'être honnête."
            systeme "Elle ne dit pas 'ne sois pas triste'. Elle accepte juste que la douleur existe."

        "Rester silencieux et encaisser seul.":
            $ arc4_reaction_cadeau_theo = "laisser_repondre"
            $ autonomie_ilona += 2
            $ ilona_peut_finir_ses_phrases += 1
            $ jalousie += 2
            $ communication -= 1
            $ pression_stream += 1
            systeme "Jessy serre la sangle de son sac. Ses jointures blanchissent."
            systeme "Il voudrait dire quelque chose. N'importe quoi. Mais sa gorge refuse de lâcher un mot qui ne sera pas une accusation."
            systeme "Alors il se tait. Et le silence fait plus mal que prévu."
            i "Merci, Théo."
            i "C'est... vraiment attentif."
            show theo smirk at char_midright
            t "Je suis content que ça te plaise."
            systeme "Le sourire de Théo dure un peu plus longtemps que nécessaire."
            systeme "Jessy détourne les yeux. Il a l'impression que tout le marché vient de voir qu'il ne sait plus comment être celui qui compte."
            systeme "Mais Ilona regarde Jessy. Elle a vu le silence. Elle ne sait pas encore quoi en faire."

        "Faire une remarque acide qui déborde.":
            $ arc4_reaction_cadeau_theo = "blague_acide"
            $ jalousie += 3
            $ communication -= 2
            $ pression_stream += 2
            $ influence_theo += 1
            $ lien_jessy_ilona -= 1
            j "Pratique. On pourra noter tous les détails qu'on rate pendant qu'on vit les moments."
            show ilona frustrated at char_midleft
            systeme "La phrase claque. Théo se fige."
            t "C'est juste un carnet, Jessy."
            j "Oui. Et moi je suis juste quelqu'un qui regarde quelqu'un d'autre gagner avec mes propres souvenirs."
            i "Arrête."
            systeme "Le mot d'Ilona sort tranchant. Jessy se tait, mais il vibre encore de tout ce qu'il n'a pas dit."
            systeme "Théo ne sourit plus. Ilona ne regarde personne."

        "Poser une question simple à Ilona.":
            $ arc4_reaction_cadeau_theo = "demander_ressenti"
            $ communication += 2
            $ autonomie_ilona += 2
            $ jalousie += 1
            $ confiance += 1
            j "Ça te touche ?"
            systeme "La question ne vise pas Théo. Elle ne vise qu'Ilona."
            i "Oui."
            $ renpy.pause(0.5)
            i "Ça me touche."
            j "D'accord."
            systeme "Jessy ne demande pas 'plus que mes cadeaux'. Il ne demande pas 'tu vas sortir avec lui maintenant'. Il écoute juste."
            systeme "Ilona garde le carnet contre elle. Moins comme une preuve que comme un objet qu'elle veut comprendre."
            systeme "Théo regarde la scène sans intervenir. Pour une fois."

        "Dire une vérité crue sans filtre.":
            $ arc4_reaction_cadeau_theo = "verite_crue"
            $ jalousie += 2
            $ communication += 1
            $ pression_stream += 1
            $ confiance += 1
            j "Je viens de réaliser que je connais tes horaires mais pas tes besoins."
            systeme "La phrase tombe sans préparation. Ilona tourne la tête vers lui."
            j "Et lui vient de me le montrer en deux phrases."
            show theo neutral at char_midright
            systeme "Théo ne dit rien. Il ne savoure pas. Il attend."
            i "Jessy..."
            j "Non, c'est bon. Je ne t'en veux pas. Je m'en veux à moi."
            systeme "Ilona ne sait pas quoi répondre. Le carnet pèse différemment maintenant."

    if arc4_reaction_cadeau_theo in ("blague_acide", "verite_crue"):
        show theo disappointed at char_midright
        t "Tu sais, Jessy, tu pourrais juste accepter qu'on puisse penser à elle autrement que toi."
        if arc4_reaction_cadeau_theo == "blague_acide":
            j "Et toi, tu pourrais arrêter de jouer au mec parfait qui se souvient de tout."
            systeme "Les mots sortent plus chauds que Jessy ne l'avait prévu."
            t "Je ne joue pas."
            j "Alors pourquoi ça ressemble toujours à une audition ?"
        else:
            j "C'est pas ça que j'ai dit."
            t "C'est ce que j'ai entendu."
            j "Alors t'as mal entendu. Je disais juste que tu as vu quelque chose que j'ai raté."
            systeme "Théo reste silencieux un instant."
        show ilona frustrated at char_midleft
        i "Stop."
        systeme "Le mot d'Ilona coupe net. Mais cette fois, elle regarde les deux."
        i "Vous allez arrêter de transformer chaque putain de cadeau en duel."
        systeme "Le juron tombe rare. Il pèse."
        i "Je ne suis pas un trophée qu'on gagne avec des souvenirs bien placés."
        systeme "Elle regarde Théo."
        i "Et je ne suis pas une victime qu'on sauve en posant des questions au bon moment."
        systeme "Elle regarde Jessy."
        systeme "Puis elle s'éloigne vers le stand voisin, le carnet encore dans sa main."
    elif arc4_reaction_cadeau_theo == "laisser_repondre":
        show theo neutral at char_midright
        t "Je vais aider Allan à chercher les boissons."
        t "Il a l'air de négocier avec un distributeur."
        i "Ça lui ressemble."
        systeme "Théo s'éloigne. Mais avant de partir, il jette un regard vers Jessy."
        systeme "Pas de triomphe. Juste une constatation. Il a donné quelque chose que Jessy ne peut pas égaler ce soir."
        hide theo
        with dissolve
        systeme "Le carnet reste dans les mains d'Ilona. Jessy regarde ses propres mains. Vides."
        systeme "Ilona sent le poids du silence de Jessy. Elle ne sait pas encore si c'est du respect ou de la peur."
    elif arc4_reaction_cadeau_theo == "demander_ressenti":
        show theo neutral at char_midright
        t "Je vais vous laisser."
        systeme "Théo recule d'un pas. Pas vexé. Pas triomphant. Juste conscient que la scène n'est plus à lui."
        hide theo
        with dissolve
        systeme "Ilona regarde Jessy. Le carnet entre eux. Pas comme un mur. Comme un objet qui existe et qu'on peut nommer."
    else:
        show theo neutral at char_midright
        t "Je vais aider Allan à chercher les boissons."
        i "D'accord."
        systeme "Théo part sans ajouter de phrase. La scène ne lui appartient pas entièrement, mais il a laissé quelque chose dedans."
        hide theo
        with dissolve

    hide jessy
    hide ilona
    with dissolve

    # Micro-scène Théo-Laplage
    scene bg arc4 christmas market
    with fade
    show theo neutral at char_left
    
    systeme "Théo s'éloigne du stand, les mains dans les poches. Il ne sourit pas. Il ne sourit jamais vraiment après ces moments."
    systeme "Il pense déjà à ce qu'il dira la prochaine fois. Quel détail il sortira. Quel silence il remplira."
    
    show laplage christmas neutral at char_right
    with dissolve
    
    systeme "Monsieur Laplage se tient devant un stand de cartes postales. Il ne vend rien. Il ne fait rien. Il observe."
    laplage "Théo."
    t "Le Messi."
    systeme "Théo dit toujours ça. Personne ne sait si c'est du respect ou de l'ironie."
    laplage "Tu te souviens de beaucoup de choses."
    t "C'est une qualité."
    laplage "Souvent."
    systeme "Laplage ne sourit pas. Il regarde Théo comme on regarde une carte qu'on ne peut pas encore lire."
    laplage "Mais un souvenir bien placé, c'est comme une clé."
    laplage "Elle peut ouvrir une porte."
    laplage "Ou verrouiller quelqu'un dedans."
    systeme "Théo ne répond pas tout de suite. Il regarde Laplage. Puis le marché. Puis le carnet qu'Ilona tient, au loin."
    t "Je ne force personne à rester."
    laplage "Non. Mais tu gardes la clé."
    systeme "Le silence s'installe. Théo ne se défend pas. Laplage ne l'accuse pas non plus."
    show laplage christmas thumb_horizontal at char_right
    systeme "Laplage lève le pouce. Ni levé. Ni baissé. Juste... horizontal. Comme une question."
    systeme "Théo reste immobile. Puis il s'éloigne sans un mot."
    
    hide theo
    hide laplage
    with dissolve

    scene bg arc4 christmas market
    with fade
    show allan doubt at char_left
    show alex concerned at char_right

    systeme "Un peu plus loin, Allan tient deux chocolats chauds et l'air de quelqu'un qui commence enfin à trouver sa neutralité fatigante."
    a "Théo vient de parler à Monsieur Laplage."
    x "Il l'a appelé 'le Messi' ?"
    a "Probablement."
    systeme "Alexandre sourit à moitié. C'est toujours étrange quand Théo utilise ce surnom."
    x "Rappelle-moi pourquoi il dit ça."
    a "Parce qu'une fois, Théo a dit que Laplage était 'le GOAT des conseils cryptiques'."
    a "Puis il a décidé que ça sonnait mieux si c'était Messi."
    x "Logique Théo : zéro sens, mais cohérent avec lui-même."
    a "Exactement."
    systeme "Ils restent silencieux quelques secondes."
    a "Mais ouais. Il se souvient de tout."
    x "Théo ?"
    a "Oui."
    x "C'est une qualité."
    a "Je sais."
    systeme "Allan regarde vers le stand où Théo vient de disparaître dans la file."
    
    if "theo_utilise_une_verite" in souvenirs and souvenirs["theo_utilise_une_verite"]:
        a "Mais il range ses souvenirs comme des arguments. Toujours prêts. Toujours justes au bon moment."
        x "Il a fait ça au festival."
        a "Oui. Et à la plage avant. Et il va recommencer ce soir si on le laisse."
    else:
        a "Mais parfois, on dirait qu'il garde les souvenirs comme des preuves."
        x "Des preuves de quoi ?"
        a "Qu'il a compris avant les autres."
    
    x "Et comprendre quelqu'un, c'est pas forcément avoir raison sur lui."
    a "Voilà."
    systeme "Ils restent silencieux quelques secondes. C'est rare, donc presque solennel."

    show sofiane observation at char_center
    with dissolve
    s "Les lumières ne disent pas où aller. Elles disent juste qu'il fait nuit."
    a "Sofiane."
    x "Tu distribues des phrases maintenant ?"
    systeme "Sofiane tient une petite enveloppe sans nom. Il regarde l'heure sur son téléphone."
    s "J'ai trouvé ça près du stand de cartes."
    a "Elle est à qui ?"
    s "Question trop petite."
    systeme "Il pose l'enveloppe sur le banc entre eux."
    s "Quelqu'un la lira au moment exact où il pensera qu'elle n'était pas pour lui."
    
    if lien_jessy_ilona >= 6 and communication >= 5 and confiance >= 4:
        systeme "Sofiane regarde encore son téléphone. Puis le marché."
        s "Je dois partir. Le service m'appelle."
        a "Quel service ?"
        s "Celui qui nourrit la route."
        systeme "Il repart avant qu'Alexandre puisse demander plus de détails."
    
    hide sofiane
    with dissolve
    $ arc4_carte_sofiane_lue = True

    if lien_jessy_ilona >= 6 and communication >= 5 and confiance >= 4:
        x "Il a dit 'le service'."
        a "Oui."
        x "Sofiane a un job ?"
        a "Apparemment. Et il refuse d'expliquer."
        x "Évidemment."
    else:
        x "Je vote pour qu'il travaille officiellement dans la météo émotionnelle."
        a "Je vais garder la carte."
        x "Tu viens de tomber dans sa prophétie."
        a "Je sais. C'est humiliant."

    hide allan
    hide alex
    with dissolve

    scene bg arc4 riverside winter
    with fade
    show ilona neutral at char_left

    systeme "La foule pousse Ilona vers la rambarde qui longe la rivière."
    systeme "Elle n'a pas fui. Pas vraiment. Elle a juste suivi l'endroit où sa poitrine pourrait se desserrer."
    systeme "Dans une main, elle tient le carnet de Théo. Dans l'autre, un mochi brillant acheté par réflexe."
    systeme "Elle regarde les deux objets. Celui qu'on lui a donné. Celui qu'elle s'est donné."
    i "Tu as l'air trop cosmique pour un dessert."
    systeme "Elle parle au mochi. C'est moins dangereux que de parler au carnet."

    menu:
        "Ilona regarde le mochi pailleté."

        "Le manger pour gagner du temps.":
            $ arc4_mochi_cosmique = True
            $ ilonanium_points += 1
            i "Désolée, univers."
            systeme "Le mochi disparaît avec une dignité limitée."

        "Le garder pour plus tard.":
            i "Tu attendras que je comprenne deux ou trois choses."
            systeme "Elle range le mochi dans son sac, entre le carnet et ses clés."

    show laplage christmas neutral at char_right
    with dissolve

    systeme "Un homme en manteau rouge se tient près d'un petit stand de cartes postales. Sa barbe blanche est beaucoup trop majestueuse pour une mission intérimaire."
    i "..."
    i "Monsieur Laplage ?"
    laplage "Père Noël intérimaire. Service des horizons froids."
    i "Vous travaillez vraiment quelque part, un jour ?"
    laplage "Je travaille surtout entre les endroits."
    i "C'est une réponse qui refuse son métier."
    laplage "Très professionnel."
    systeme "Ilona regarde le carnet, puis la rivière."
    i "Si quelqu'un se souvient de ce que j'ai dit, je devrais être contente."
    laplage "Souvent, oui."
    i "Mais j'ai aussi envie de jeter ce carnet dans la rivière pour voir s'il se souvient comment nager."
    systeme "Laplage ne sourit pas. Il acquiesce."
    laplage "Parce que tu n'as pas encore décidé si le souvenir est un cadeau ou une preuve que quelqu'un collectionne tes morceaux."
    i "Voilà."
    i "Et en plus, je me sens conne de ne pas juste dire merci et être heureuse."
    
    if confidences_laplage >= 1:
        laplage "Tu m'as déjà dit que tu étais en colère. Au festival."
        i "Je m'en souviens."
        laplage "Tu l'es encore ?"
        i "Je ne sais pas. Peut-être. Contre moi, surtout."
        laplage "Parce que tu ne sais pas encore ce que tu veux."
        i "Exactement."
    
    laplage "Poser une limite n'est pas casser le cadeau."
    systeme "Cette fois, la phrase reste."
    i "Même si la limite fait mal à quelqu'un qui ne voulait pas mal faire ?"
    laplage "Surtout là."
    systeme "Ilona serre le carnet. Pas pour le garder précieusement. Pour sentir qu'elle a encore le choix de ce qu'il signifie."
    systeme "Laplage se retourne vers son stand. Il revient avec un gobelet de café chaud."
    laplage "Les décisions froides méritent une main chaude."
    systeme "Il tend le gobelet."
    i "Vous vendez du café maintenant ?"
    laplage "Je vends surtout des pauses."
    show laplage christmas thumb_up at char_right
    systeme "Il lève le pouce. Ilona prend le café. Il réchauffe ses doigts engourdis par le froid."
    i "Merci."
    show laplage thumb_up at char_center
    systeme "Laplage acquiesce. Puis repart vers son stand."
    systeme "Ilona reste avec le carnet dans une main, le café dans l'autre."
    systeme "Le café ne résout rien. Mais il lui donne quelques secondes où elle peut juste respirer."
    $ confidences_laplage += 1
    $ jugement_laplage += 1

    hide laplage
    with dissolve

    systeme "Quand Ilona se retourne, Jessy est à quelques mètres. Il n'a pas entendu toute la conversation. Assez pour savoir qu'il doit demander avant d'approcher."

    show jessy embarrassed at char_right
    with dissolve

    j "Je peux venir ?"
    i "Oui."
    systeme "Il avance jusqu'à la rambarde. Sa main se pose sur le métal froid. Trop fort. Comme s'il devait s'empêcher de bouger autrement."
    j "Tu es partie vite."
    i "Je sais."
    j "Je ne te le reproche pas."
    i "Bien."
    systeme "Le silence s'installe. Jessy voudrait qu'il soit confortable. Il est juste lourd."
    systeme "Ilona regarde toujours la rivière. Jessy regarde Ilona."
    j "Il t'a offert quelque chose que j'aurais dû voir."
    i "Jessy..."
    j "Laisse-moi finir."
    systeme "La phrase sort plus dure qu'il ne voulait. Ilona se tourne vers lui."
    j "Désolé. Je veux dire... j'ai besoin de dire ça."
    i "D'accord."
    j "Je t'ai vue oublier des idées dehors une dizaine de fois. Peut-être plus."
    j "Et je ne t'ai jamais donné de carnet."
    systeme "Il serre la rambarde."
    j "Je pensais que c'était mignon. Que tu étais comme ça. Je n'ai pas pensé que c'était quelque chose que tu voulais changer."
    i "Ce n'est pas un concours, Jessy."
    j "Si. Ça l'est devenu."
    systeme "La franchise coupe. Ilona reste silencieuse."
    j "Et j'ai l'impression de perdre sans même savoir qu'on jouait."
    
    if arc2_choix_activite_theo == "suivre":
        systeme "Ilona se souvient. La plage. Les mares. Jessy qui la suit au lieu de lui faire confiance."
        systeme "Elle avait dit 'test de fidélité'. Il ne l'a pas oublié non plus."
        i "Tu as déjà perdu une fois en essayant de gagner."
        j "Je sais."
        i "Alors pourquoi tu recommences ?"
        systeme "Jessy n'a pas de réponse. Ou trop de réponses."
    elif arc2_choix_activite_theo == "dix_minutes":
        systeme "Ilona se souvient. La plage. Jessy qui dit 'j'ai peur' au lieu de la retenir."
        systeme "Ça n'avait pas tout réglé. Mais ça avait compté."
        i "Tu sais nommer ta peur. Tu l'as déjà fait."
        j "Oui."
        i "Alors fais-le maintenant. Sans transformer ça en concours."

    menu:
        "Jessy vient d'avouer qu'il se sent en compétition. Ilona peut l'accueillir, le rejeter, ou montrer qu'elle aussi a peur."

        "Offrir la miniature en avouant qu'elle porte trop de sens." if arc4_cadeau_jessy in ("miniature_souvenir", "blague_interne", "miniature_aveu"):
            $ arc4_limite_ilona = "cadeau_respirant"
            $ lien_jessy_ilona += 2
            $ confiance += 2
            $ communication += 2
            $ autonomie_ilona += 1
            $ jalousie += 1
            $ remember("maison_respectee")
            systeme "Jessy sort enfin la petite boîte. Sa main tremble légèrement."
            j "J'ai préparé ça."
            if arc4_cadeau_jessy == "miniature_aveu":
                j "Et je sais que ça va vouloir dire trop de choses."
                j "Mais je refuse de faire comme si c'était juste un objet mignon."
            elif arc4_cadeau_jessy == "blague_interne":
                j "C'est... compliqué. Je vais te laisser voir."
            else:
                j "Mais maintenant j'ai peur que ce soit juste ma version à moi du carnet de Théo."
                j "Un souvenir bien emballé pour prouver que je compte encore."
            systeme "Ilona prend la boîte. Elle ne l'ouvre pas tout de suite."
            i "Qu'est-ce que c'est ?"
            j "La maison. Notre maison Minecraft. En miniature."
            systeme "Elle tire le ruban. À l'intérieur, la maison garde ses erreurs : couloir inutile, cuisine trop grande, pièce cachée."
            if arc4_cadeau_jessy == "blague_interne":
                systeme "Un minuscule panneau indique : PIÈCE MOYENNEMENT IMPORTANTE, ÉDITION NEIGE."
                show ilona smile at char_left
                i "C'est complètement idiot."
                j "Oui."
                i "J'aime ça."
                systeme "Mais le sourire s'estompe vite."
                i "Et j'ai aussi peur de ce que ça signifie vraiment."
            elif arc4_cadeau_jessy == "miniature_aveu":
                i "Tu n'as pas corrigé les erreurs."
                j "Non. Je voulais que tu voies ce qui a vraiment existé."
                i "Même en sachant que ça veut dire trop de choses ?"
                j "Surtout en sachant ça."
            else:
                i "Tu n'as pas corrigé les erreurs."
                j "Non."
                j "Je voulais garder ce qui a existé. Même les parties cassées."
            i "Jessy..."
            systeme "Elle pose la boîte sur la rambarde. Puis elle regarde Jessy."
            i "Je ne sais pas quoi faire avec deux cadeaux qui veulent dire des choses."
            j "Tu n'es pas obligée de décider ce soir."
            i "Je sais. Mais j'ai l'impression que vous attendez tous les deux une réponse."
            if arc4_cadeau_jessy == "miniature_aveu":
                j "Moi, je veux juste que tu saches ce que j'ai voulu dire. Pas que tu me rendes une réponse parfaite."
            else:
                j "Moi, je veux juste que tu gardes la maison si elle te fait du bien. Pas si elle te donne une dette."
            systeme "Ilona regarde la miniature. Puis le carnet. Puis la rivière."
            i "Je vais les garder tous les deux."
            i "Mais je ne promets pas de les aimer de la même manière."
            i "Ou au même moment."
            j "C'est honnête."
            i "Oui."

        "Offrir le cadeau neutre en essayant de sauver la face." if arc4_cadeau_jessy == "cadeau_couteux":
            $ arc4_limite_ilona = "cadeau_preuve"
            $ lien_jessy_ilona -= 1
            $ confiance -= 2
            $ communication -= 1
            $ influence_theo += 2
            $ pression_stream += 2
            systeme "Jessy sort l'écharpe avec une urgence mal cachée."
            j "Tiens."
            i "Qu'est-ce que c'est ?"
            j "Un cadeau. Pour toi."
            systeme "Ilona regarde l'écharpe. Elle est belle. Chère. Impersonnelle."
            i "Elle est belle."
            j "Mais ?"
            i "Je n'ai pas dit mais."
            j "Ton visage l'a dit."
            systeme "Ilona prend l'écharpe. Le tissu glisse entre ses doigts."
            i "Elle est belle, Jessy. Vraiment."
            i "Mais j'ai l'impression que tu viens de paniquer dans une boutique en pensant à Théo."
            systeme "Jessy ne répond pas. Ilona plie l'écharpe lentement."
            i "Merci. Je vais la garder."
            systeme "Le 'merci' sonne comme une politesse funéraire. Jessy l'entend. Il ne dit rien."

        "Ne rien offrir et avouer la peur sans filtre." if arc4_cadeau_jessy == "discussion_honnete":
            $ arc4_limite_ilona = "parole_sans_verdict"
            $ communication += 3
            $ confiance += 2
            $ autonomie_ilona += 2
            $ jalousie += 1
            $ remember("jessy_nomme_sa_peur")
            j "J'ai un cadeau dans mon sac."
            i "Ah."
            j "Je ne vais pas te le donner."
            i "Pourquoi ?"
            j "Parce que je le donnerais pour les mauvaises raisons."
            systeme "Ilona attend. Jessy inspire."
            j "Je veux que tu préfères mon cadeau à celui de Théo."
            j "Je veux que tu me regardes comme tu l'as regardé quand il a sorti ce putain de carnet."
            j "Je veux gagner."
            systeme "Les mots sortent crus. Jessy grimace."
            j "Et je déteste tout ce que je viens de dire."
            systeme "Ilona reste silencieuse longtemps. Puis elle pose le carnet de Théo sur la rambarde."
            i "Moi aussi, des fois, je veux que tu m'aimes plus que ton jeu. Plus qu'Alexandre. Plus que ta peur de mal faire."
            systeme "La phrase tombe sans préparation."
            i "Et je déteste vouloir ça."
            systeme "Jessy la regarde. Vraiment."
            j "On est beaux."
            i "Catastrophiques."
            j "Ça aussi."
            systeme "Le rire arrive inattendu. Douloureux, mais réel."

        "Demander ce que le cadeau de Théo signifie vraiment pour elle.":
            $ arc4_limite_ilona = "demande_theo"
            $ jalousie += 3
            $ communication -= 2
            $ autonomie_ilona -= 2
            $ influence_theo += 2
            $ pression_stream += 2
            $ lien_jessy_ilona -= 2
            j "Son cadeau... ça veut dire quelque chose pour toi ?"
            show ilona frustrated at char_left
            i "Jessy."
            j "Je demande juste."
            i "Non."
            i "Tu demandes si je dois te rassurer avant même que j'aie le temps de comprendre ce que moi je ressens."
            j "Ce n'est pas..."
            i "Si."
            systeme "Ilona serre le carnet."
            i "Et tu sais ce qui est terrible ?"
            i "C'est que je ne sais pas encore ce que ce cadeau signifie."
            i "Mais maintenant, je ne peux plus le découvrir tranquillement parce que tu viens de transformer ça en épreuve de loyauté."
            systeme "Jessy recule d'un pas."
            j "Je voulais pas..."
            i "Je sais ce que tu voulais."
            i "Mais ce que tu fais, c'est différent."

        "Proposer de marcher ensemble sans parler de cadeaux.":
            $ arc4_limite_ilona = "marche_silencieuse"
            $ communication += 1
            $ lien_jessy_ilona += 1
            $ autonomie_ilona += 1
            $ pression_stream -= 1
            j "On pourrait marcher un peu ?"
            i "Pour aller où ?"
            j "Nulle part. Juste marcher."
            systeme "Ilona regarde le carnet dans sa main. Puis Jessy."
            i "Sans parler de qui a offert quoi ?"
            j "Ouais."
            i "D'accord."
            systeme "Ils marchent le long de la rivière. Le silence entre eux n'est pas confortable. Mais il n'est pas violent non plus."
            if arc4_cadeau_jessy in ("miniature_souvenir", "blague_interne", "miniature_aveu"):
                systeme "Parfois, Ilona regarde le carnet. Parfois, Jessy regarde son sac où la miniature attend."
            elif arc4_cadeau_jessy == "cadeau_couteux":
                systeme "Parfois, Ilona regarde le carnet. Parfois, Jessy pense à l'écharpe qu'il a achetée par panique."
            else:
                systeme "Parfois, Ilona regarde le carnet. Parfois, Jessy regarde ses mains vides et se demande si c'était le bon choix."
            systeme "Personne ne gagne. Personne ne perd. Ça reste juste suspendu."

    systeme "Ilona pose le carnet de Théo sur la rambarde. Pas pour le rejeter. Pour faire de la place."
    if arc4_limite_ilona == "cadeau_respirant":
        systeme "Elle pose aussi la miniature à côté. Les deux objets se touchent presque."
    elif arc4_limite_ilona == "marche_silencieuse":
        systeme "La marche les a ramenés ici. Face à la conversation qu'ils ont évitée."
    
    show ilona determined at char_left
    i "J'ai besoin de dire une chose."
    j "D'accord."
    
    if arc4_limite_ilona == "demande_theo":
        i "Et tu vas écouter sans m'interrompre cette fois."
        systeme "Le 'cette fois' fait mal. Jessy hoche la tête."
    else:
        i "Et j'ai besoin que tu écoutes sans essayer de te défendre ou de réparer tout de suite."
        systeme "Jessy hoche la tête. Sa mâchoire se serre."

    if arc4_reaction_cadeau_theo in ("laisser_repondre", "reconnaitre", "demander_ressenti"):
        $ ilona_peut_finir_ses_phrases += 1
    elif arc4_reaction_cadeau_theo in ("blague_acide", "verite_crue"):
        $ interruptions_ilona += 1

    i "Ce n'est pas parce que quelqu'un connaît mes goûts qu'il sait ce que je veux."
    systeme "Pause."
    i "Et ce n'est pas parce que je reçois un cadeau que je dois décider immédiatement ce qu'il signifie."
    $ remember("ilona_pose_une_limite")
    systeme "La phrase traverse la soirée entière. Elle touche Théo même absent. Elle touche Jessy même silencieux."
    i "J'ai le droit de garder des objets et de ne pas encore savoir si je les aime."
    systeme "Jessy regarde ses mains sur la rambarde."
    i "Et j'ai le droit de vous aimer tous les deux différemment sans que ce soit un classement."
    if arc4_limite_ilona == "demande_theo":
        i "Mais si tu me forces à choisir tout de suite, je vais choisir aucun des deux."
        systeme "La menace n'en est pas une. C'est une limite posée dans le béton."

    menu:
        "Ilona vient de poser sa limite. Jessy doit choisir comment l'accueillir."

        "Accueillir la limite sans se défendre.":
            $ communication += 3
            $ confiance += 2
            $ autonomie_ilona += 2
            $ ilona_peut_finir_ses_phrases += 1
            if interruptions_ilona > interruptions_reconnues:
                $ interruptions_reconnues += 1
                $ interruptions_reparees += 1
                $ remember("jessy_repare")
            show jessy listening at char_right
            j "Tu as raison."
            systeme "Pause."
            j "Je peux retenir tous les détails du monde et quand même me tromper sur ce dont tu as besoin."
            i "Oui."
            j "Je veux apprendre à demander au lieu de deviner et offrir la réponse comme une preuve."
            systeme "Ilona expire. Le froid rend son souffle visible entre eux."
            i "Ça, je peux l'entendre."
            systeme "Elle tend la main. Pas pour prendre celle de Jessy. Juste pour la poser à côté sur la rambarde."
            systeme "Leurs petits doigts se touchent. Pas s'enlacent. Se touchent."

        "Nommer sa peur sans s'effondrer.":
            $ communication += 2
            $ confiance += 2
            $ jalousie += 1
            $ autonomie_ilona += 1
            $ remember("jessy_nomme_sa_peur")
            j "J'entends."
            systeme "Jessy regarde la rivière."
            j "Et j'ai peur quand je vois quelqu'un d'autre se souvenir aussi bien de toi."
            i "Je sais."
            j "Je ne te dis pas ça pour que tu le repousses ou que tu me rassures."
            j "Je dis ça parce que ma peur existe. Et que je refuse qu'elle commande à ma place."
            systeme "Ilona tourne la tête vers lui."
            i "C'est la chose la plus honnête que tu m'aies dite ce soir."
            j "Ouais. Ça fait bizarre."
            systeme "Elle sourit. Petit. Fatigué."
            i "Garde ta peur de ton côté de la rambarde."
            j "D'accord."
            i "Et moi je garde la mienne du mien."

        "Demander ce qu'elle attend de lui, concrètement.":
            $ communication += 2
            $ confiance += 1
            $ autonomie_ilona += 1
            $ jalousie += 1
            j "Qu'est-ce que tu veux que je fasse ?"
            i "Rien."
            j "Rien ?"
            i "Rien tout de suite. Juste... entendre ce que je viens de dire."
            systeme "Jessy serre la rambarde."
            j "J'ai peur que 'rien' veuille dire que c'est déjà fini."
            i "Et j'ai peur que 'quelque chose' veuille dire que je dois décider maintenant."
            systeme "Ils se regardent. Deux peurs face à face."
            j "Ok. Je peux vivre avec rien pour ce soir."
            i "Merci."

        "Dire qu'elle a raison mais que Théo joue quand même.":
            $ jalousie += 3
            $ communication -= 1
            $ influence_theo += 2
            $ pression_stream += 2
            $ confiance -= 1
            j "Tu as raison."
            systeme "Pause."
            j "Mais Théo sait exactement ce qu'il fait."
            show ilona frustrated at char_left
            i "Jessy, je viens de..."
            j "Non, écoute. Je t'écoute. Mais tu dois aussi voir qu'il joue un jeu."
            i "Et toi, tu viens de décider que ma limite comptait moins que ton besoin de me prouver quelque chose."
            systeme "La phrase claque. Jessy se tait."
            i "C'est exactement ce dont je parlais."

        "Accepter la limite en silence, juste acquiescer.":
            $ communication += 1
            $ confiance += 1
            $ autonomie_ilona += 2
            $ jalousie += 1
            show jessy listening at char_right
            systeme "Jessy hoche la tête. Il ne dit rien."
            systeme "Pas parce qu'il n'a rien à dire. Parce qu'il sait que les mots maintenant transformeraient la limite en négociation."
            systeme "Ilona regarde Jessy. Elle attend une défense. Un 'mais'. Une justification."
            systeme "Rien ne vient."
            i "C'est tout ?"
            j "Oui."
            i "Tu ne vas pas expliquer ?"
            j "Non. Tu as posé une limite. Je l'entends."
            systeme "Ilona reste immobile un instant. Puis elle expire lentement."
            i "D'accord."
            systeme "Le mot sonne différent. Presque soulagé."

    if arc4_limite_ilona in ("cadeau_respirant", "parole_sans_verdict", "marche_silencieuse") and communication >= 5:
        show ilona smile at char_left
        if arc4_cadeau_jessy in ("miniature_souvenir", "blague_interne", "miniature_aveu"):
            systeme "Ilona ramasse le carnet. Puis la miniature."
        else:
            systeme "Ilona ramasse le carnet."
        i "Je vais garder le carnet."
        j "D'accord."
        if arc4_limite_ilona == "cadeau_respirant":
            if arc4_cadeau_jessy in ("miniature_souvenir", "blague_interne", "miniature_aveu"):
                i "Et je vais garder ta miniature aussi."
                i "Mais je ne promets pas de les aimer pareil."
                i "Ou de décider ce soir lequel compte le plus."
                j "Je comprends."
            else:
                i "Et ton cadeau, je le veux."
                i "Mais je ne promets pas de décider ce soir ce qu'il signifie."
                j "Je comprends."
        elif arc4_limite_ilona == "parole_sans_verdict":
            i "Et un jour, peut-être, tu me donneras ton cadeau quand il ne portera plus autant de peur."
            j "Je peux attendre."
        else:
            i "Et ton cadeau, je le veux. Mais pas ce soir."
            j "Quand tu voudras."
        systeme "Ce n'est pas une victoire. C'est mieux : une chose qui n'appartient qu'à elle."
        $ lien_jessy_ilona += 1
        $ confiance += 1
    elif arc4_limite_ilona == "cadeau_preuve" or arc4_limite_ilona == "demande_theo":
        show ilona fatigue at char_left
        i "Je crois que je vais rentrer avec Allan."
        j "Tu veux que je vienne ?"
        i "Non."
        systeme "Pas 'pas ce soir'. Juste 'non'."
        systeme "La phrase est une porte qu'Ilona ferme. Pas en claquant. En respirant enfin de l'autre côté."
        j "D'accord."
        if arc4_limite_ilona == "cadeau_preuve":
            i "Merci pour l'écharpe. Vraiment."
            systeme "Mais le 'merci' ne répare rien."
        else:
            systeme "Ilona part sans ajouter de merci. Jessy reste planté là, le poids de ses questions dans les mains."
        $ pression_stream += 2
        $ lien_jessy_ilona -= 1
    else:
        show ilona neutral at char_left
        i "Je ne sais pas encore quoi faire de tout ça."
        j "Du carnet ?"
        i "Du carnet. De ta miniature si tu me la donnes un jour. De toi. De Théo. De moi."
        systeme "Elle rit sans joie."
        i "Ambiance très festive."
        j "Le Père Noël va porter plainte."
        i "Il a déjà les preuves."
        systeme "Le rire aide. Un peu. Pas assez."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc4 christmas market
    with fade
    show allan support at char_left
    show alex neutral at char_midleft
    show jessy neutral at char_midright
    show ilona neutral at char_right

    systeme "Le groupe se retrouve près de la sortie du marché. Les sacs sont plus petits que les silences."
    a "J'ai acheté quatre chocolats chauds. Un exploit logistique, pas une invitation à parler de sentiments devant la caisse."
    x "Je confirme. La caisse n'a pas signé pour ça."
    if arc4_carte_sofiane_lue:
        systeme "Allan sort l'enveloppe trouvée par Sofiane."
        a "Au fait, on a une carte non identifiée."
        i "De Sofiane ?"
        x "De Sofiane par l'intermédiaire du destin, probablement."
        systeme "Ilona lit la phrase écrite d'une main étonnamment nette."
        i "Les lumières ne disent pas où aller. Elles disent juste qu'il fait nuit."
        j "C'est... très lui."
        a "Et un peu utile, malheureusement."

    show theo neutral at char_center
    with dissolve

    t "Tu rentres ?"
    systeme "Théo pose la question à Ilona. Ses yeux passent brièvement sur Jessy, puis reviennent."
    if arc4_limite_ilona in ("cadeau_respirant", "parole_sans_verdict", "marche_silencieuse"):
        i "Oui."
        i "Avec le groupe."
        systeme "Le mot 'groupe' remet une distance nette là où Théo aurait préféré un 'nous' plus flou."
        t "D'accord."
        systeme "Il ne sourit pas. Il acquiesce. Comme quelqu'un qui sait quand ne pas insister."
    elif arc4_limite_ilona in ("cadeau_preuve", "demande_theo"):
        i "Oui. Avec Allan."
        a "Je marche lentement, mais avec fiabilité émotionnelle."
        t "Je peux t'accompagner aussi, si tu veux."
        show ilona frustrated at char_right
        systeme "Ilona regarde Théo. Pas méchamment. Mais fermement."
        i "Théo."
        t "Oui ?"
        i "J'ai dit avec Allan."
        show theo innocent at char_center
        t "Je proposais juste."
        i "Je sais ce que tu proposais."
        systeme "Allan pose une main sur l'épaule d'Ilona. Pas pour la défendre. Pour signaler qu'il a entendu."
        a "Elle a répondu, Théo."
        systeme "Théo regarde Allan. Puis Ilona. Puis il recule d'un pas."
        t "D'accord. Bonne soirée."
        systeme "Il part sans insister plus. Mais Jessy voit la tension dans ses épaules."
    else:
        i "Oui. Je crois."
        t "Si tu veux marcher un peu avant, je peux..."
        i "Pas maintenant."
        systeme "Théo hoche la tête."
        t "D'accord."
        systeme "Il ne force pas. Mais le 'pas maintenant' laisse une porte."

    hide theo
    with dissolve

    # Arc 4.5 alternatif - Ilona accepte de marcher avec Théo (route Théo)
    if influence_theo >= 5 and confiance <= 2 and arc4_limite_ilona == "demande_theo":
        systeme "Mais quelque chose change."

        show ilona neutral at char_right

        i "Attends."

        systeme "Théo s'arrête. Il ne se retourne pas tout de suite. Comme s'il savait déjà."

        show theo neutral at char_center
        with dissolve

        i "Finalement... je veux bien marcher un peu. Avant de rentrer."

        systeme "Jessy sent quelque chose se glacer dans sa poitrine."

        j "Ilona..."

        show ilona frustrated at char_right

        i "Jessy, je suis fatiguée. De tout ça."
        i "J'ai besoin de parler à quelqu'un qui ne me demande pas de le rassurer."

        systeme "Le mot 'rassurer' claque."

        t "On ne va pas loin. Juste jusqu'à la station."

        systeme "Théo ne triomphe pas. Mais il ne refuse pas non plus."

        a "Ilona, tu es sûre que..."
        i "Allan. S'il te plaît."

        systeme "Elle prend son sac. Théo attend près de la sortie."

        systeme "Jessy reste immobile. Alexandre le regarde sans savoir quoi dire."
        systeme "Allan pose une main sur son épaule. C'est la seule chose qu'il puisse faire."

        i "On se voit demain."

        systeme "Elle part avec Théo. Pas main dans la main. Mais côte à côte."
        systeme "Quelque chose vient de se déplacer. Jessy ne sait pas encore si c'est réparable."

        $ influence_theo += 2
        $ pression_stream += 2
        $ confiance -= 1
        $ arc4_ilona_avec_theo = True

        hide ilona
        hide theo
        with dissolve

    systeme "La soirée se termine sans grande scène. C'est presque pire, parce que les vraies conséquences aiment parfois partir en marchant normalement."

    hide allan
    hide alex
    with dissolve
    
    # Arc 4.5 - Scène secrète Maid Café (si synergie bonne)
    if lien_jessy_ilona >= 6 and communication >= 5 and confiance >= 4:
        call arc_4_5_maid_cafe from _call_arc_4_5_maid_cafe

    # Arc 4.5 - Scène marche Théo/Ilona (si route Théo)
    if arc4_ilona_avec_theo:
        call arc_4_5_theo from _call_arc_4_5_theo
    
    hide jessy
    hide ilona
    with dissolve

    scene bg arc4 minecraft winter night
    with Dissolve(2.0)
    show jessy minecraft at char_left
    show ilona minecraft at char_right

    systeme "Plus tard, la maison Minecraft apparaît sous une neige carrée."
    systeme "Noël n'existe pas vraiment dans ce monde, sauf si quelqu'un décide de poser des blocs blancs sur le toit et d'appeler ça une intention."

    if arc4_limite_ilona in ("cadeau_respirant", "parole_sans_verdict", "marche_silencieuse"):
        $ arc4_fin_minecraft = "miniature_trace"
        $ lien_jessy_ilona += 1
        $ confiance += 1
        if arc4_cadeau_jessy in ("miniature_souvenir", "blague_interne", "miniature_aveu"):
            $ maison_minecraft_ajouts.append("miniature_noel_arc4")
            
            if arc3_fin_minecraft == "destruction":
                systeme "Ilona regarde la maison. Le trou de la cuisine d'été est toujours là. Jessy l'a laissé."
                i "Tu veux qu'on répare d'abord ?"
                j "On peut."
                i "Ou on construit la miniature à côté du trou."
                j "Comme une réponse ?"
                i "Comme une continuation."
                systeme "Jessy comprend. L'erreur fait partie de l'histoire. La cacher ne la réparerait pas."
            
            i "Je vais construire une version de ton cadeau dans la salle secrète."
            j "Tu veux que j'aide ?"
            i "Oui."
            if arc4_cadeau_jessy == "blague_interne":
                i "Mais si tu corriges une seule erreur, je détruis tout et je pose un panneau 'JESSY A RUINÉ NOËL'."
            else:
                i "Mais les erreurs restent. C'est non négociable."
            j "Message reçu."
            systeme "Ils construisent petit. Lentement. La miniature dans la miniature devient absurde."
            i "On est en train de faire de l'art conceptuel malgré nous."
            j "Je crois qu'on fait de la mise en abyme émotionnelle."
            i "Encore pire."
            systeme "Elle rit. Il rit aussi. La maison grandit."
        else:
            $ maison_minecraft_ajouts.append("espace_calme_arc4")
            i "On pourrait juste... construire quelque chose ensemble ?"
            j "Sans que ça signifie quelque chose de lourd ?"
            i "Exactement."
            systeme "Ils posent des blocs. Rien de précis. Juste un espace un peu plus calme que le reste."
            systeme "Parfois, ne rien dire ensemble vaut tous les cadeaux du monde."
    elif arc4_limite_ilona == "cadeau_preuve":
        $ arc4_fin_minecraft = "echarpe_coffre"
        $ pression_stream += 1
        systeme "Ilona ouvre un coffre près de l'entrée. Elle y dépose un bloc de laine bleu."
        i "Je mets l'écharpe là."
        j "Tu ne la gardes pas ?"
        i "Je la garde."
        i "Mais pas sur moi."
        systeme "Jessy comprend. L'objet n'est pas refusé. Son poids l'est."
        j "D'accord."
        systeme "Il ne demande pas quand elle la portera. Il a peur de la réponse."
        $ maison_minecraft_ajouts.append("echarpe_coffre_arc4")
    elif arc4_limite_ilona == "demande_theo":
        $ arc4_fin_minecraft = "carnet_hors_maison"
        $ influence_theo += 1
        $ pression_stream += 1
        systeme "Ilona reste devant l'entrée sans entrer."
        j "Tu viens ?"
        i "Pas maintenant."
        systeme "Son avatar tient un livre. Le jeu ne peut pas afficher un carnet. Mais l'intention est là."
        i "Je vais construire dehors ce soir."
        j "Pourquoi dehors ?"
        i "Parce que la maison a trop entendu de choses aujourd'hui."
        systeme "Jessy ne répond pas. Il la regarde partir vers un coin vide de la map."
        systeme "Il reste seul dans la maison. Elle a raison. Les murs ont trop entendu."
        $ maison_minecraft_ajouts.append("coin_dehors_carnet_arc4")
    else:
        $ arc4_fin_minecraft = "neige_sur_toit"
        $ lien_jessy_ilona += 1
        i "On met de la neige sur le toit ?"
        j "Il va fuir."
        i "C'est Minecraft. Rien ne fuit."
        j "Émotionnellement, il va fuir."
        systeme "Elle rit. Il rit aussi."
        systeme "Rien n'est réglé. Mais le rire n'est pas faux."
        $ maison_minecraft_ajouts.append("neige_toit_arc4")

    if arc4_mochi_cosmique:
        systeme "Sur le bureau d'Ilona, le papier du mochi pailleté reflète la lumière de l'écran."
        i "J'ai peut-être mangé un astre ce soir."
        j "Encore ?"
        i "Ne juge pas mon rapport à l'univers."
        j "Je ne juge jamais tes choix cosmiques."

    if arc4_fin_minecraft in ("miniature_trace", "echarpe_coffre", "carnet_hors_maison"):
        systeme "La nuit avance. La maison ne guérit pas d'un coup."
        if arc4_fin_minecraft == "miniature_trace":
            systeme "Mais pour la première fois depuis le festival, elle contient un endroit où quelque chose peut attendre sans suffoquer."
        else:
            systeme "Elle est traversée par des objets qu'on ne sait plus porter. Ou pas encore."
    else:
        systeme "La nuit avance. La neige carrée adoucit les angles."
        systeme "Demain, elle fondra peut-être. Ce soir, elle laisse assez de lumière pour voir où on marche."

    jump arc_5_examens


# --- Recapitulatif Arc IV ---
# Variables modifiees :
# - lien_jessy_ilona, confiance, communication, jalousie, autonomie_ilona
# - influence_theo, pression_stream, jugement_laplage, confidences_laplage
# - interruptions_ilona, interruptions_reconnues, interruptions_reparees, ilona_peut_finir_ses_phrases
# - ilonanium_points
# - souvenirs["jessy_nomme_sa_peur"], souvenirs["jessy_repare"], souvenirs["ilona_pose_une_limite"], souvenirs["maison_respectee"]
# - arc4_cadeau_jessy, arc4_reaction_cadeau_theo, arc4_limite_ilona, arc4_fin_minecraft
# - arc4_carte_sofiane_lue, arc4_mochi_cosmique
#
# Choix ayant des consequences futures :
# - Le sens donne au cadeau de Jessy determine s'il devient un souvenir partage, une preuve anxieuse ou une conversation plus honnete.
# - La reaction au cadeau precis de Theo modifie la confiance, l'autonomie d'Ilona et l'influence de Theo.
# - La facon d'accueillir la limite d'Ilona prepare directement l'Arc V, notamment la question peur/confiance.
# - Le mochi cosmique peut ajouter un point a la route cachee de l'Ilonanium.
#
# Fils ouverts pour l'Arc V :
# - Ilona a formule que connaitre ses gouts ne suffit pas a savoir ce qu'elle veut.
# - Théo reste utile et attentif, mais Allan commence a intervenir quand son aide cherche a prendre la place de la reponse d'Ilona.
# - Jessy peut avoir appris a laisser un cadeau respirer, ou avoir renforce l'idee qu'il cherche une garantie.
# - La maison Minecraft contient une trace de Noel : miniature, coffre d'attente, objet trop lourd, coin dehors ou neige fragile.
