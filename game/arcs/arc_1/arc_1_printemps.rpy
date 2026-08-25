# Arc I - Printemps : la vie hors ecran.
# Les variables importantes restent centralisees dans script.rpy.

image bg arc1 school corridor = im.Scale("images/scenes/shared/bg_shared_school_corridor.jpg", 1920, 1080)
image bg arc1 rooftop = im.Scale("images/scenes/arc_1/bg_arc1_rooftop_lunch.jpg", 1920, 1080)
image bg arc1 train platform = im.Scale("images/scenes/arc_1/bg_arc1_train_platform.jpg", 1920, 1080)
image bg arc1 train inside = im.Scale("images/scenes/shared/bg_shared_train_inside.jpg", 1920, 1080)
image bg arc1 konbini = im.Scale("images/scenes/arc_1/bg_arc1_konbini_snacks.jpg", 1920, 1080)
image bg arc1 cafeteria = im.Scale("images/scenes/arc_1/bg_arc1_school_cafeteria.jpg", 1920, 1080)


label arc_1_printemps:
    scene bg arc1 school corridor
    with fade

    systeme "Arc I - Printemps : la vie hors écran."
    systeme "Avril. Depuis la maison Minecraft, Jessy et Ilona se parlent presque tous les soirs sur Discord."
    systeme "Pas de caméra. Pas de photo. Juste leurs voix, leurs pseudos, et des messages envoyés trop tard."
    systeme "Le jour de la rentrée, Jessy cherche son nom sur un panneau trop rempli."

    show jessy embarrassed at char_left
    j "Alors... première B, deuxième étage..."

    show ilona neutral at char_right
    with dissolve
    systeme "Derrière lui, quelqu'un s'arrête."
    i "Attends..."
    i "Jessy ?"
    j "Ilona ?"
    i "Attends. C'est vraiment toi ?"
    j "Je crois."
    i "Tu crois ?"
    j "Je vérifie encore."
    i "Je t'ai reconnu à ta voix."
    j "Je parlais tout seul ?"
    i "Un peu."
    j "Super première impression."
    i "C'était très Discord, en vrai."

    systeme "Ils se regardent une seconde. En vocal, il y avait toujours un bruit de clavier, un clic de souris, quelque chose à faire avec les mains. Là, il n'y a que le couloir."
    i "On est dans la même école."
    j "Oui."
    i "C'est bizarre."
    j "Un peu."
    i "Bizarre bien, hein."
    j "Oui. Bizarre bien."

    if maison_minecraft_transformation == "serre":
        i "Au fait, j'ai montré la serre suspendue à personne."
        j "Merci."
        i "Je garde nos crimes d'architecture privés."
    elif maison_minecraft_transformation == "piscine":
        i "J'ai repensé à la piscine dans le couloir."
        j "Elle était utile."
        i "Jessy, elle bloquait deux portes."
        j "Utile émotionnellement."
    elif maison_minecraft_transformation == "toboggan":
        i "Le toboggan devant le coffre vide existe encore ?"
        j "Oui."
        i "Parfait."
        j "Il ne sert toujours à rien."
        i "Justement."
    else:
        i "La maison a toujours autant de pièces inutiles ?"
        j "Oui."
        i "Bien."
        j "Tu dis ça comme si c'était normal."
        i "Ça l'est, pour nous."

    systeme "La sonnerie coupe la suite."
    i "Je dois y aller."
    j "Moi aussi."
    i "On se voit à midi ?"
    j "Oui. Si je trouve la salle avant l'année prochaine."
    i "Je t'enverrai une carte."

    systeme "Le reste de la matinée passe lentement. Jessy lit deux fois le même exercice sans vraiment le comprendre."
    systeme "À chaque sonnerie, il regarde vers la porte avant de se rappeler qu'il ne sait même pas dans quelle classe est Ilona."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc1 rooftop
    with fade
    show jessy neutral at char_left
    show ilona smile at char_right

    systeme "À midi, Ilona l'attend près de l'escalier du toit avec deux boissons à la main."
    i "J'ai pris melon. Si tu n'aimes pas, tu peux souffrir en silence."
    j "J'aime bien melon."
    i "Bon. Ça commence trop facilement."

    systeme "Ils s'assoient près du grillage. Le vent bouge un peu les emballages. Personne ne parle pendant quelques secondes."
    j "C'est plus simple en vocal."
    i "Oui."
    j "Là, je sais pas quoi faire de mon visage."
    i "Il fait de son mieux."
    j "C'est gentil et inquiétant."

    systeme "Ilona ouvre son bentô, hésite, puis pousse un morceau d'omelette vers lui."
    i "Tu veux goûter ?"
    j "Tu es sûre ?"
    i "C'est une omelette, Jessy. Pas mon héritage familial."

    menu:
        "Ilona lui propose un morceau de son repas."

        "Faire une blague sur Minecraft.":
            $ lien_jessy_ilona += 1
            j "Après mon plafond, tu attaques mon repas."
            i "Je partage, là."
            j "C'est vrai. Pardon à l'omelette."
            i "Elle accepte."

        "Lui demander si elle en a vraiment envie.":
            $ communication += 1
            $ confiance += 1
            $ autonomie_ilona += 1
            j "Tu le proposes parce que tu veux, ou parce que tu te sens obligée ?"
            i "Parce que je veux."
            j "D'accord."
            i "Mais merci de demander."

        "Accepter et partager ses biscuits.":
            $ lien_jessy_ilona += 1
            $ communication += 1
            j "Merci. J'ai des biscuits, si tu veux."
            i "Ils ont survécu au trajet ?"
            j "Plus ou moins."
            i "Je prends les morceaux les moins tristes."
            systeme "Ils mangent en silence. Cette fois, le silence gêne moins."

        "Refuser trop vite.":
            $ communication -= 1
            j "Non, non, garde."
            i "D'accord."
            systeme "Ilona reprend le morceau sans faire d'histoire."
            j "Je voulais pas être impoli."
            i "Tu peux juste dire non. C'est pas grave."
            j "D'accord. Je m'entraîne."

    systeme "Après ce midi-là, ils ne deviennent pas soudain naturels."
    systeme "Ils se croisent surtout par petits morceaux : un salut dans l'escalier, un message envoyé trop tard, une blague Minecraft pendant une pause."
    systeme "Au bout de quelques jours, ces petits morceaux commencent à ressembler à une habitude."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc1 train platform
    with fade
    show jessy neutral at char_left
    show ilona smile at char_right

    systeme "Un après-midi, ils se retrouvent sur le quai après les cours."
    i "Tu prends aussi ce train ?"
    j "Oui."
    i "Donc on aurait pu se croiser depuis des mois."
    j "Et on a choisi Minecraft."
    i "Très bon choix, honnêtement."

    systeme "Le train arrive. Ils montent sans trop savoir s'ils doivent continuer la conversation ou regarder par la fenêtre."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc1 train inside
    with dissolve
    show jessy neutral at char_left
    show ilona smile at char_right

    systeme "Dans le wagon, Ilona sort son téléphone."
    i "Bouge pas."
    j "Pourquoi ?"
    systeme "Elle prend une photo avant qu'il ait le temps de comprendre."
    j "Oh non."
    i "Oh si."
    j "J'avais quelle tête ?"
    i "La tête de quelqu'un qui vient d'être pris en photo."
    j "Donc mauvaise."
    i "Vivante."

    menu:
        "Ilona regarde la photo en souriant."

        "Lui demander de la garder si elle l'aime bien.":
            $ communication += 1
            $ confiance += 1
            j "Tu peux la garder si elle est pas trop horrible."
            i "Elle est bien."
            j "Vraiment ?"
            i "Oui. On voit que tu réfléchis trop."
            j "C'est mon expression de base."

        "Lui demander de supprimer.":
            $ communication -= 1
            j "Tu peux supprimer ?"
            i "Oui."
            systeme "Elle le fait tout de suite."
            j "Merci."
            i "Pas besoin de faire cette tête. Je te demanderai la prochaine fois."
            j "Désolé."

        "Poser pour une deuxième photo.":
            $ lien_jessy_ilona += 1
            show jessy determined at char_left
            j "Attends. Refais. Je peux faire pire."
            i "C'est ambitieux."
            j "Je crois en moi."
            i "Magnifique. On dirait une photo de carte de club refusée."

    systeme "La photo reste un sujet pendant deux jours."
    systeme "Ilona menace de l'utiliser comme preuve que Jessy existe en dehors de Minecraft. Jessy négocie des droits d'auteur imaginaires."
    systeme "Un soir, alors qu'ils sont encore dans le train, Jessy essaie de dire quelque chose d'important."
    j "Ilona, je voulais te dire que—"
    systeme "Le train s'arrête brutalement. La sonnerie de fermeture des portes couvre la fin de sa phrase."
    i "Quoi ?"
    j "Rien. Laisse tomber."
    systeme "Ilona le regarde avec un sourire mi-amusé, mi-frustré."
    i "Tu recommenceras plus tard ?"
    j "Peut-être. Si je retrouve le courage."
    systeme "Puis la semaine avance, et avec elle une chose simple : ils cherchent moins une raison pour se parler."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc1 konbini
    with fade
    show jessy neutral at char_left
    show ilona neutral at char_right

    systeme "Le vendredi, Ilona propose de passer au konbini avant de rentrer."
    i "J'ai faim."
    j "Tu as mangé il y a deux heures."
    i "Oui. Et maintenant j'ai faim."
    j "Argument solide."

    systeme "Ils traînent devant les snacks beaucoup trop longtemps."
    i "Celui-là a une étoile sur le paquet."
    j "Ça veut sûrement dire sucre."
    i "Ou destin."
    j "Je parie sur sucre."
    i "Tu manques de foi."

    systeme "Ils sortent avec des chips, deux boissons, et un bonbon en forme d'étoile qu'Ilona ouvre déjà."
    i "Je teste."
    j "Tu testes quoi ?"
    i "Si ça donne des pouvoirs."
    j "Évidemment."

    show laplage neutral at char_center
    with dissolve

    systeme "Un homme au calme impossible se tient devant le rayon des boissons, comme si c'était l'endroit le plus normal du monde pour attendre."
    systeme "Cette fois, il n'est pas au bord d'une rivière Minecraft. Il est là, entre les sodas et les étiquettes de promotion."
    laplage "Le pouvoir vient rarement du sucre."
    i "..."
    j "..."
    i "Jessy."
    j "Oui."
    i "C'est lui."
    j "Le type de la rivière."
    laplage "Monsieur Laplage."
    j "C'est votre nom ?"
    laplage "Aujourd'hui, oui."
    i "Vous travaillez ici ?"
    laplage "Je surveille les horizons. Et parfois les offres deux pour un."
    show laplage thumb_up at char_center
    laplage "Choisir un bonbon, c'est déjà choisir une petite catastrophe."
    hide laplage
    with dissolve

    i "Il vient de partir vers les lessives."
    j "Je crois qu'il n'y avait pas de sortie de ce côté."
    i "Donc on est d'accord : ce n'était pas juste un souvenir bizarre du serveur."
    j "On est d'accord, et je déteste que ça soit une phrase raisonnable."
    i "On paie et on rentre ?"
    j "Oui. Très bonne idée."

    menu:
        "Ilona lève le bonbon étoile comme si c'était très sérieux."

        "Mentionner Monsieur Laplage.":
            $ ilonanium_points += 1
            $ lien_jessy_ilona += 1
            j "Attention. Monsieur Laplage a peut-être un avis sur les étoiles."
            i "Il sait déjà trop de choses."
            j "C'est vrai."
            i "Donc on la garde pour plus tard."
            j "Stratégie raisonnable."
            systeme "Le bonbon rejoint la poche d'Ilona. Ils ne savent pas encore ce qu'ils font de cette petite chose."

        "La laisser manger l'étoile.":
            $ ilonanium_points += 1
            $ lien_jessy_ilona += 1
            i "Trop tard."
            j "Et ?"
            i "Sucre."
            j "Pas destin ?"
            i "Pas encore."
            systeme "Ilona garde un air sérieux beaucoup trop longtemps."

        "Proposer de la garder pour la maison Minecraft.":
            $ lien_jessy_ilona += 1
            j "On pourrait la mettre dans la salle secrète."
            i "Comme décoration ?"
            j "Comme objet important sans utilité."
            i "Ça va très bien avec la pièce."
            systeme "Jessy propose de garder une petite chose ensemble. Ce n'est pas encore un serment, juste un geste qui dit : ce qu'on construit compte."

    systeme "Le week-end passe avec cette histoire coincée quelque part entre eux."
    systeme "Ils en reparlent par messages, puis arrêtent, puis recommencent."
    systeme "Le lundi, au premier intercours, ils finissent par résumer l'histoire d'une façon très simple : un monsieur sorti de nulle part a donné son avis sur un bonbon."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc1 school corridor
    with fade
    show jessy embarrassed at char_left
    show ilona smile at char_right

    systeme "Ils reprennent ensuite leur trajet habituel entre deux salles."
    systeme "Ils ne disent pas qu'ils marchent ensemble. Ils se retrouvent juste aux mêmes endroits."

    show allan neutral at char_midleft
    with dissolve
    a "Attendez."
    a "C'est vous, la maison Minecraft bizarre ?"
    j "Ça dépend. Qui demande ?"
    i "Et à quel point bizarre ?"

    show alex grin at char_midright
    with dissolve
    x "Moi je l'ai vue. Elle est incroyable."
    j "Elle est pas finie."
    x "Ça se voit."
    i "C'était pas un compliment ?"
    x "Si. Chez moi, si."
    i "On a aussi recroisé le type bizarre du serveur."
    j "Au konbini."
    a "Pardon ?"
    i "Le monsieur au pouce levé. Dans le rayon boissons."
    x "Cette école devient intéressante."
    a "Donc... vous sortez ensemble ?"

    systeme "Jessy ouvre la bouche, puis la referme."
    $ renpy.pause(0.8, hard=True)

    menu:
        "Allan vient de poser la question un peu trop fort."

        "Répondre sincèrement : \"J'aimerais bien.\"":
            $ lien_jessy_ilona += 1
            $ communication += 1
            j "J'aimerais bien."
            $ renpy.pause(0.8, hard=True)
            show ilona embarrassed at char_right
            systeme "Ilona rougit, mais elle ne recule pas."
            j "Enfin... je veux pas répondre pour toi."
            $ autonomie_ilona += 1
            $ ilona_peut_finir_ses_phrases += 1
            $ renpy.pause(0.5, hard=True)
            show ilona smile at char_right
            i "Merci."
            i "Je sais pas encore. Mais merci."
            if lien_jessy_ilona >= 3:
                systeme "Allan et Alexandre échangent un regard entendu, puis reprennent leur conversation comme si de rien n'était."

        "Faire une blague pour détendre l'atmosphère.":
            $ lien_jessy_ilona += 1
            j "On partage une maison impossible. C'est déjà beaucoup."
            i "Il esquive."
            j "Un peu."
            j "Mais je veux pas te mettre dans une réponse devant tout le monde."
            $ communication += 1
            $ autonomie_ilona += 1
            i "Ça, je prends."

        "Laisser Ilona répondre.":
            $ autonomie_ilona += 1
            $ ilona_peut_finir_ses_phrases += 1
            $ communication += 1
            j "Je te laisse répondre si tu veux."
            i "Je sais pas trop."
            j "C'est une réponse aussi."
            i "Oui. Pour l'instant, c'est celle-là."

        "Nier trop vite.":
            $ communication -= 1
            $ jalousie += 1
            j "Non, non. Pas du tout."
            show ilona neutral at char_right
            i "Ah."
            systeme "La réponse est sortie trop vite. Tout le monde le sent, même Jessy."
            j "Je voulais dire..."
            i "C'est bon."
            systeme "Elle sourit un peu, mais le sujet reste là."

    systeme "Le reste de la journée se déroule avec cette question au-dessus d'eux."
    systeme "Personne ne la repose. C'est presque pire."
    systeme "Quand les cours se terminent, Ilona lui envoie seulement : \"toit ?\""

    hide allan
    hide alex
    with dissolve

    hide jessy
    hide ilona
    with dissolve

    scene bg arc1 rooftop
    with fade
    show jessy neutral at char_left
    show ilona neutral at char_right

    systeme "Après les cours, Ilona l'attend encore sur le toit."
    j "Tu voulais me parler ?"
    i "Un peu."
    j "D'accord."
    $ renpy.pause(0.8, hard=True)
    i "En ligne, c'est plus facile."
    j "Oui."
    i "Quand je réfléchis trop longtemps, personne ne le voit."
    j "Moi aussi, je préfère quand on peut cacher les blancs avec le bruit du jeu."
    $ renpy.pause(1.0, hard=True)
    i "Là, on les entend."

    menu:
        "Ilona parle doucement, sans chercher la bonne phrase."

        "Lui dire qu'elle peut prendre son temps.":
            $ communication += 1
            $ confiance += 1
            $ autonomie_ilona += 1
            $ ilona_peut_finir_ses_phrases += 1
            j "Tu peux prendre ton temps avec moi."
            j "Même si je suis maladroit."
            show ilona smile at char_right
            i "Tu l'es un peu."
            j "Je sais."
            i "Mais c'est mieux quand tu le sais."

        "Se défendre.":
            $ communication -= 1
            j "Je fais pas exprès d'être bizarre."
            i "Je sais."
            i "Je disais pas ça contre toi."
            systeme "Jessy hoche la tête, gêné. Il a répondu trop vite."

        "Faire une petite blague, puis répondre vraiment.":
            $ lien_jessy_ilona += 1
            $ communication += 1
            j "On peut mettre un panneau : silence en travaux."
            i "Comme dans ta maison."
            j "Exactement."
            systeme "Il sourit, puis reprend plus doucement."
            j "Mais je comprends. Je veux pas que tu te sentes pressée."
            i "Merci."

        "Lui demander ce qui l'aiderait.":
            $ communication += 2
            $ confiance += 1
            $ autonomie_ilona += 1
            $ ilona_peut_finir_ses_phrases += 1
            j "Tu veux que je parle plus ? Ou juste que je reste là ?"
            i "Je sais pas encore."
            j "Alors on verra."
            i "Oui. On verra."

    systeme "Cette fois, ils ne repartent pas tout de suite."
    systeme "Ils restent jusqu'à ce que le toit se vide, sans trouver une conclusion parfaite."
    systeme "Le lendemain midi, Allan arrive à la cantine avec l'air de quelqu'un qui a gardé une information beaucoup trop longtemps."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc1 cafeteria
    with fade
    show jessy neutral at char_left
    show ilona smile at char_right
    show allan neutral at char_midleft
    show alex grin at char_midright

    systeme "À midi, Allan et Alexandre les rejoignent à la cantine."
    a "J'ai vu le type dont vous avez parlé."
    j "Quel type ?"
    a "Pouce levé. Regard de vieux sage devant les distributeurs."
    i "Monsieur Laplage."
    x "Donc il a vraiment un nom."
    a "J'ai réfléchi."
    x "Il a réfléchi fort. Ça m'a inquiété."
    a "Soit c'est un prof, soit c'est un employé, soit c'est un type qui apparaît quand il veut."
    i "La troisième option est très précise."
    j "Et pas rassurante."
    x "J'ai aussi une capture de la maison."
    j "Pourquoi ?"
    x "Pour la science."

    systeme "Allan fouille dans son sac, puis abandonne sans avoir trouvé ce qu'il cherchait."
    a "Je demanderai à Théo. Il a toujours une réponse."
    i "C'est qui ?"
    a "Un ami. Il parle comme s'il avait déjà lu la fin."
    j "Ça a l'air pratique."
    x "Ou fatigant."
    if maison_minecraft_transformation == "poulet":
        x "Au fait, le poulet géant surveille toujours la cuisine ?"
        j "Il a gagné en autorité."
        i "On lui a donné un nom."
        a "...vous avez nommé un poulet géant ?"
        i "Bien sûr. Il s'appelle Monsieur Plume."
    elif maison_minecraft_transformation == "serre":
        x "La serre suspendue produit quelque chose de comestible maintenant ?"
        i "Elle intimide toujours les tomates."
        j "C'est sa fonction principale."
    elif maison_minecraft_transformation == "piscine":
        x "Le couloir nage toujours ?"
        j "Pire. Il a des vagues maintenant."
        i "On a ajouté un toboggan aquatique."
        a "Vous réparez rien, en fait."

    show sofiane observation at char_center
    with dissolve
    s "Les premiers liens font beaucoup de bruit quand personne ne sait encore quoi dire."
    systeme "Sofiane dit ça depuis la table derrière eux, puis reprend son repas."
    a "Il était là depuis le début ?"
    x "Je crois qu'il est toujours là depuis le début."
    hide sofiane
    with dissolve

    systeme "Ilona rit. Jessy aussi."
    systeme "Ce n'est pas encore simple entre eux. Mais maintenant, ce n'est plus seulement dans Minecraft."

    jump arc_2_plage
