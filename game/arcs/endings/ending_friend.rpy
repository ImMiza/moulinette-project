# GOOD ENDING (FRIEND) - JESSY ET ILONA
# Route Jessy : ils restent amis, sans promesse de romance.

label ending_friend:
    $ record_ending("friend")

    scene bg arc2 minecraft house summer night
    with fade
    systeme "Après la randonnée, Ilona et Jessy se donnent du temps. Leur amitié reprend doucement, sans effacer ce qui s'est dit au bivouac."
    show jessy minecraft at char_left
    show ilona minecraft at char_right
    with dissolve
    i "Tu as laissé la porte ouverte dans notre monde ?"
    j "Oui. Pour qu'on puisse revenir quand on en aura envie."
    i "Je ne sais pas encore quand."
    j "T'as pas besoin de me donner une date."
    systeme "Les semaines passent. Ils s'écrivent, jouent parfois ensemble et apprennent à se retrouver sans attendre que leur amitié devienne autre chose."
    i "Tu veux qu'on reconstruise le pont samedi ?"
    j "Oui. Et je promets de ne pas dessiner le plan avant que tu arrives."
    i "Tu mens très mal."
    j "D'accord. Je promets de ne pas le suivre tout seul."
    systeme "Ilona rit. Ils restent amis, chacun libre de suivre sa propre route et heureux de pouvoir encore partager un bout du chemin."
    return
