# Arc IV.5 - Maid Café Secret : Sofiane a trouvé un job.
# Scène bonus accessible seulement si synergie Jessy-Ilona bonne.

image bg arc4_city_night = im.Scale("images/scenes/arc_4/bg_arc4_5_maid_cafe_exterior.jpg", 1920, 1080)
image bg arc4_maid_cafe_exterior = im.Scale("images/scenes/arc_4/bg_arc4_5_maid_cafe_exterior.jpg", 1920, 1080)
image bg arc4_maid_cafe_interior = im.Scale("images/scenes/arc_4/bg_arc4_5_maid_cafe_interior.jpg", 1920, 1080)

define audio.wow = "audio/fx/WOW.mp3"

# Variable locale pour tracker accès scène
default arc4_5_maid_cafe_visite = False
default arc4_5_sofiane_maid = False

# La condition d'accès est évaluée inline dans arc_4_noel.rpy avant le call.
# L'ancien label arc_4_5_maid_cafe_check n'était appelé nulle part : supprimé.

label arc_4_5_maid_cafe:
    $ arc4_5_maid_cafe_visite = True
    
    scene bg arc4 christmas market
    with fade
    show jessy neutral at char_left
    show ilona neutral at char_right
    
    systeme "Après le marché de Noël, la soirée pourrait se terminer."
    systeme "Allan et Alexandre sont partis. Théo aussi. Le marché commence à ranger ses lumières."
    systeme "Mais quelque chose dans l'air — la neige qui commence, les illuminations qui ne s'éteignent pas encore — donne envie de prolonger."
    
    i "Tu fais quelque chose après ?"
    j "Non. Pourquoi ?"
    i "Je veux pas rentrer tout de suite."
    i "On pourrait marcher ?"
    j "Oui."
    systeme "Jessy ne demande pas pourquoi. Il accepte."
    
    stop ambiant1 fadeout 1.0
    play music audio.citynight loop volume 0.8 fadeout 1.0 fadein 1.0
    scene bg arc4_city_night
    with fade
    show jessy neutral at char_left
    show ilona neutral at char_right
    
    systeme "Ils marchent sans destination. Les rues sont plus calmes maintenant que le marché se vide."
    systeme "Parfois, Ilona regarde les vitrines. Parfois, Jessy regarde Ilona."
    systeme "Le silence entre eux n'est pas parfait. Mais il n'est pas dangereux non plus."
    
    hide jessy
    hide ilona
    with dissolve
    
    systeme "Ils passent devant une boulangerie fermée. Un marchand de journaux qui baisse son rideau."
    systeme "La neige tombe légèrement. Pas assez pour couvrir le sol. Juste assez pour ralentir le temps."
    
    show ilona neutral at char_left
    show jessy neutral at char_right
    
    i "On va où ?"
    j "Je sais pas."
    i "Moi non plus."
    systeme "Ils continuent quand même."
    
    scene bg arc4_maid_cafe_exterior
    with fade
    
    systeme "Au détour d'une rue, un café attire leur attention."
    systeme "Pas par sa taille. Pas par son enseigne lumineuse."
    systeme "Mais parce qu'il est ouvert, chaleureux, et qu'une pancarte annonce : « MAID CAFÉ — OUVERT JUSQU'À MINUIT »."
    
    show ilona neutral at char_left
    show jessy embarrassed at char_right
    
    i "Un maid café."
    j "Oui."
    i "Tu savais qu'il y en avait un ici ?"
    j "Non. Absolument pas."
    systeme "Ilona regarde la vitrine. À l'intérieur, quelques clients. Une décoration douce. Rien de tape-à-l'œil."
    i "Tu veux rentrer ?"
    j "Je... euh."
    systeme "Jessy hésite. Pas parce qu'il refuse. Parce qu'il ne sait pas si c'est bizarre de dire oui."
    i "Je vais prendre ça comme un oui."
    
    menu:
        "Jessy doit répondre."
        
        "Accepter avec curiosité honnête.":
            $ lien_jessy_ilona += 2
            j "Pourquoi pas. J'ai jamais vraiment vu ça en vrai."
            i "Moi non plus."
            i "Donc on va découvrir ensemble si c'est adorable ou terrifiant."
            j "Pari équitable."
            systeme "Ils poussent la porte."
        
        "Faire une blague pour désamorcer la gêne.":
            $ lien_jessy_ilona += 2
            j "Si Alexandre apprend qu'on est allés dans un maid café sans lui, il va théoriser notre disparition."
            show ilona smile at char_left
            i "Il va dessiner un schéma avec des flèches rouges."
            j "Et accuser Monsieur Laplage d'être le propriétaire secret."
            i "Bon. On rentre pour vérifier."
            systeme "Ils poussent la porte en riant."
        
        "Demander si Ilona est sûre.":
            $ autonomie_ilona += 2
            $ communication += 1
            $ confiance += 1
            $ pression_stream = max(0, pression_stream - 1)
            j "Tu es sûre ?"
            i "Pourquoi je serais pas sûre ?"
            j "Je sais pas. C'est... particulier ?"
            i "Jessy."
            j "Oui ?"
            i "J'ai proposé. Donc oui, je suis sûre."
            j "D'accord."
            systeme "Ils poussent la porte."
    
    play music audio.maidcafe volume 0.6 loop fadeout 1.0 fadein 1.0
    scene bg arc4_maid_cafe_interior
    with fade
    
    systeme "L'intérieur est plus calme que prévu. Quelques tables occupées. Une décoration soignée sans être kitsch."
    systeme "Et derrière le comptoir..."
    
    play sound audio.wow volume 1.0
    show sofiane maid at char_center
    with dissolve
    
    systeme "Sofiane."
    systeme "En tenue de maid."
    systeme "Tablier blanc impeccable. Bandeau à froufrous. Lunettes toujours en place."
    systeme "Il fait un cœur avec ses mains. Expression parfaitement sérieuse."
    
    s "Bienvenue, Maîtres. Votre table vous attend dans l'ombre de vos destins entrelacés."
    
    show jessy embarrassed at char_left
    show ilona embarrassed at char_right
    with dissolve
    
    systeme "Silence absolu."
    systeme "Jessy cligne des yeux. Une fois. Deux fois."
    systeme "Ilona ouvre la bouche. La referme."
    
    j "..."
    i "..."
    j "Sofiane ?"
    s "Oui, Maître Jessy. Votre reconnaissance traverse les dimensions du service."
    i "Tu... tu travailles ici ?"
    s "Depuis trois mois. Le salaire finance l'essence. La route a faim."
    systeme "Il dit ça en refaisant un cœur avec ses mains."
    systeme "Jessy essaie de ne pas rire. Il échoue."
    
    show jessy smile at char_left
    j "Sofiane. Tu es en train de nous servir en tenue de maid."
    s "Oui."
    j "Et tu le fais avec le même sérieux que quand tu conduis."
    s "Chaque rôle mérite sa trajectoire parfaite."
    systeme "Il pose deux menus sur la table avec une précision chirurgicale."
    s "Je recommande le chocolat chaud aux épices. Il réchauffe les cœurs gelés par l'incertitude."
    
    show ilona smile at char_right
    i "Je vais prendre ça."
    j "Pareil."
    s "Sagesse double."
    systeme "Sofiane acquiesce avec la gravité d'un chef d'orchestre. Puis repart vers la cuisine avec une grâce étonnamment fluide."
    
    hide sofiane
    with dissolve
    
    systeme "Jessy et Ilona restent assis en silence. Puis éclatent de rire."
    
    i "On vient de découvrir que Sofiane travaille dans un maid café."
    j "Et qu'il le prend plus au sérieux que sa propre vie."
    i "Je vais avoir cette image en tête pour toujours."
    j "Moi aussi."
    systeme "Le rire aide. Beaucoup."
    systeme "Pour la première fois de la soirée, quelque chose se détend vraiment entre eux."
    
    play sound audio.wow volume 0.5
    show sofiane maid at char_center
    with dissolve
    
    systeme "Sofiane revient avec deux chocolats chauds fumants. Il les pose avec une précision millimétrique."
    s "Vos boissons, Maîtres. Que la chaleur apaise les questions sans réponse."
    i "Merci, Sofiane."
    s "Vous ne raconterez rien à Allan et Alexandre."
    j "Pourquoi ?"
    if arc4_carte_sofiane_lue:
        s "Parce qu'ils savent que je travaille quelque part. Mais ils ne savent pas où."
        s "Garder le mystère, c'est préserver l'équilibre cosmique."
        i "Tu veux dire que tu veux pas qu'ils se moquent."
        s "Les deux vérités coexistent."
    else:
        s "Parce qu'Alexandre va théoriser. Et Allan va dessiner un schéma."
        systeme "Jessy et Ilona se regardent."
        i "On vient littéralement de dire ça avant de rentrer."
        s "Les esprits synchronisés traversent les mêmes vérités."
    systeme "Il repart vers une autre table."
    
    hide sofiane
    with dissolve
    
    # Seule soupape de pression du jeu. Récompense de complicité (tier B) :
    # pas de gain de communication, la scène ne résout rien.
    $ lien_jessy_ilona += 2
    $ pression_stream = max(0, pression_stream - 1)
    $ arc4_5_sofiane_maid = True
    
    systeme "Ils restent une demi-heure. Boivent leur chocolat. Parlent de tout sauf de Théo, des cadeaux, des décisions."
    systeme "Sofiane passe parfois avec une phrase dramatique. Parfois juste pour remplir leur eau avec un professionnalisme absurde."
    systeme "Quand ils partent, il les raccompagne jusqu'à la porte."
    
    play sound audio.wow volume 0.5
    show sofiane maid at char_center
    with dissolve
    
    s "Revenez quand vos cœurs auront besoin d'une pause entre deux virages."
    i "On reviendra."
    j "Promis."
    systeme "Sofiane fait un salut de maid impeccable."
    
    hide sofiane
    with dissolve
    
    play music audio.citynight volume 0.8 loop fadeout 1.0 fadein 1.0
    scene bg arc4_city_night
    with fade
    
    show jessy smile at char_left
    show ilona smile at char_right
    
    systeme "Dehors, la neige tombe légèrement. Jessy et Ilona marchent côte à côte."
    systeme "Rien n'est réglé. Mais quelque chose s'est allégé."
    
    i "Merci d'être venu."
    j "Merci d'avoir proposé."
    systeme "Ils rentrent chacun chez eux. Mais le souvenir du maid café — et de Sofiane faisant des cœurs avec ses mains — reste."
    systeme "Certaines soirées ne résolvent rien. Mais elles donnent assez de légèreté pour continuer."
    
    hide jessy
    hide ilona
    with dissolve
    stop music fadeout 1.0 
    stop ambiant1 fadeout 1.0
    return

# Note : Cette scène doit être appelée depuis arc_4_noel.rpy ligne 1022
