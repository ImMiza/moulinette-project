# Arc prologue - Minecraft : une maison beaucoup trop grande.
# Les variables importantes restent centralisees dans script.rpy.
# Ces alias de chat sont propres au prologue Minecraft.

define pmj = Character("jessyCube", color="#8fb7ff", callback=speaker_callback("jessy"))
define pmi = Character("IlonaGaming", color="#ffb0d0", callback=speaker_callback("ilona"))
define pmx = Character("lorddarktime", color="#b9f2c8", callback=speaker_callback("alex"))

label prologue_minecraft:

    play music "music/Haggstrom.mp3" loop
    scene bg prologue house afternoon
    with fade
    show jessy minecraft at char_left

    systeme "Prologue - Minecraft : une maison beaucoup trop grande."
    systeme "Fin d'après-midi. Sur un serveur public, Jessy pose le dernier bloc d'une petite base qui a cessé d'être petite depuis longtemps."
    pmj "C'est encore un chantier."
    pmj "Mais un chantier avec du potentiel."
    systeme "La maison s'étale sur la colline comme si plusieurs idées avaient signé le même bail sans se parler."
    $ maison_minecraft_detail = "couloir"
    systeme "Il y a trop de fenêtres, trop de toits, une passerelle qui semble avoir une opinion, et une tour construite pour justifier l'existence d'une autre tour."
    systeme "Jessy refuse d'appeler cela une erreur. Il préfère le mot 'développement'."

    systeme "Il descend finalement jusqu'à l'entrée, comme si le bâtiment pouvait encore recevoir des visiteurs sans les perdre."
    play sound "fx/minecraft-walking-on-grass.mp3"
    scene bg prologue house entrance
    with dissolve
    show jessy minecraft at char_left
    play sound "fx/minecraft-wood-break-place.mp3"
    systeme "Devant l'entrée, Jessy plante une pancarte."
    systeme "NE PAS ENTRER. SAUF SI TU AS UNE BONNE IDÉE."

    play sound "fx/minecraft-walking-on-grass.mp3"
    show ilona minecraft at char_right
    with dissolve
    
    systeme "Quelques minutes plus tard, une joueuse s'arrête devant la maison."
    pmi "c'est chez toi ?"
    pmj "techniquement"
    pmi "ça veut dire oui, ou ça veut dire que je vais être expulsée du serveur ?"
    pmj "ça veut dire que les fondations sont légales"
    pmi "inquiétant comme réponse"
    pmi "j'ai une idée"
    pmj "laquelle ?"
    pmi "je vais entrer"

    systeme "Jessy hésite. La pancarte ne prévoyait pas qu'une personne la lise littéralement."
    pmj "d'accord"
    pmj "mais si tu trouves une pièce inutile, c'est probablement qu'elle est en cours de réflexion"
    pmi "promis, je respecte la vie intérieure des pièces inutiles"

    systeme "Ilona passe le seuil. De l'intérieur, la maison ressemble moins à un plan qu'à une conversation interrompue plusieurs fois."
    play sound "fx/minecraft-door.mp3"
    scene bg prologue weird interior
    with dissolve
    show jessy minecraft at char_left
    show ilona minecraft at char_right

    systeme "Ilona visite sans cruauté. Elle s'arrête devant les escaliers, les portes et le coffre ouvert comme devant des œuvres dont le musée aurait perdu les cartels explicatifs."
    pmi "pourquoi cet escalier change d'avis au milieu ?"
    pmj "il est en cours de réflexion"
    pmi "c'est un escalier très philosophe alors"

    pmi "et cette porte, là-haut ?"
    pmj "elle attend son étage"
    pmi "elle a l'air très patiente"

    systeme "En montant, Ilona arrive dans une zone encore moins terminée que les autres. Il y a là des blocs qui donnent l'impression de tenir par politesse."
    scene bg prologue accident floor
    with Dissolve(0.8)
    play sound "fx/stones-falling.mp3"
    with hpunch
    show jessy minecraft at char_left
    show ilona minecraft at char_right
    systeme "À l'étage, Ilona retire un bloc qu'elle pense décoratif."
    systeme "Le mur interprète ce geste comme une invitation à tomber. Une partie du plafond suit. Une poule tombe aussi, avec l'air de n'avoir signé aucun formulaire."
    $ renpy.pause(0.5, hard=True)

    pmi "oh non"
    pmi "j'ai cassé un truc"
    pmj "quel truc ?"
    pmi "une partie importante du concept"
    pmj "ça ne répond pas à la question"
    pmi "le mur"
    pmi "et peut-être le plafond"
    pmi "et une poule"

    menu:
        "La maison vient de perdre un mur, un bout de plafond et une certaine dignité. Comment Jessy réagit-il ?"

        "Déclarer une guerre de poulets.":
            $ prologue_reaction = "poulets"
            $ lien_jessy_ilona += 2
            pmj "très bien. Guerre de poulets."
            pmi "c'est une sanction ?"
            pmj "c'est une procédure officielle"
            pmi "je refuse de perdre contre quelqu'un qui vit dans un couloir sans sortie"
            systeme "La première guerre de poulets commence dans une dignité inexistante. La poule survivante refuse de choisir un camp."
            systeme "L'humour transforme l'accident en complicité. Ce n'est pas encore une réparation, mais c'est déjà une façon de parler."


        "Réagir trop vite.":
            $ prologue_reaction = "trop_vite"
            $ communication -= 2
            $ confiance -= 1
            $ pression_stream += 1
            $ evitements += 1
            pmj "attends, ne touche plus à rien deux secondes"
            pmi "...d'accord"
            $ renpy.pause(1.2, hard=True)
            systeme "Le silence dure juste assez longtemps pour que Jessy entende sa propre phrase."
            pmj "je voulais dire : attends, je vais regarder comment on peut arranger ça ensemble"
            pmi "d'accord"
            pmi "mais je peux aider"
            pmj "oui"
            pmj "cette fois, on regarde les blocs avant de les casser"
            pmi "je ne promets rien"

        "Faire une blague avant de regarder les dégâts.":
            $ prologue_reaction = "blague"
            $ lien_jessy_ilona += 2
            pmj "je crois que la maison vient de choisir une nouvelle personnalité"
            pmi "elle avait déjà une personnalité ?"
            pmj "elle est compliquée"
            pmi "comme tous les bâtiments qui ont trois cuisines"

        "Réparer ensemble.":
            $ prologue_reaction = "reparer"
            $ communication += 2
            $ confiance += 1
            $ jalousie = max(0, jalousie - 1)
            $ lien_jessy_ilona += 1
            $ remember("maison_respectee")
            pmj "ce n'est pas grave. On répare ensemble."
            pmi "tu dis ça parce que tu es gentil, ou parce que tu n'as pas encore vu les dégâts ?"
            pmj "les deux peuvent être vrais"
            systeme "Ilona cesse de reculer. Ce n'est pas encore de la confiance. C'est une première planche posée au-dessus du vide."
    systeme "Jessy pense reconstruire le mur. Ilona regarde le trou dans le plafond avec une gêne qui essaie déjà de devenir une idée."
    pmi "on peut réparer le mur"
    pmi "ou faire un truc mieux qu'un mur"
    pmj "un mur qui marche ?"
    pmi "non. Un mur, c'est triste."
    pmj "c'est exactement la phrase de quelqu'un qui va casser d'autres murs"
    pmi "je préfère architecte de conséquences"

    menu:
        "Ilona veut transformer les dégâts au lieu de les effacer. Quelle place Jessy lui laisse-t-il ?"

        "La laisser essayer son idée de serre.":
            $ maison_minecraft_transformation = "serre"
            $ autonomie_ilona += 2
            $ communication += 1
            $ confiance += 1
            $ pression_stream = max(0, pression_stream - 1)
            pmj "vas-y"
            pmj "je ne comprends pas encore, mais vas-y"
            pmi "parfait. L'incompréhension, c'est une très bonne fondation."
            systeme "Ils déplacent les blocs cassés au lieu de les effacer. Petit à petit, le trou devient une idée."
            scene bg prologue greenhouse branch
            play sound "fx/construction.mp3"
            with dissolve
            show jessy minecraft at char_left
            show ilona minecraft at char_right
            systeme "Ils suspendent de la terre, des fleurs et une lanterne au-dessus du vide. Rien n'est optimal. Tout paraît soudain volontaire."
            pmi "si quelqu'un demande ce que c'est, on dira que c'est une serre aérienne"
            pmj "et si quelqu'un demande pourquoi elle existe ?"
            pmi "on se déconnecte"

        "Répondre par une idée encore plus stupide.":
            $ maison_minecraft_transformation = "poulet"
            $ lien_jessy_ilona += 2
            pmj "il faut un gardien"
            pmi "un gardien ?"
            pmj "un poulet géant"
            pmi "tu viens de dire ça avec beaucoup trop de sérieux"
            systeme "Le projet quitte alors la catégorie des réparations pour entrer dans une zone administrative inconnue."
            scene bg prologue chicken roof branch
            play sound "fx/big-Chicken.mp3"
            with dissolve
            show jessy minecraft at char_left
            show ilona minecraft at char_right
            systeme "Le poulet géant surveille la maison avec une autorité discutable. Sa tête est légèrement trop large, ce qui augmente son charisme."
            pmj "il nous juge"
            pmi "il protège la cuisine"


        "Chercher avec elle une solution franchement inutile.":
            $ maison_minecraft_transformation = "toboggan"
            $ lien_jessy_ilona += 2
            pmj "et si on faisait quelque chose qui ne répare rien, mais qui explique pourquoi c'est cassé ?"
            pmi "tu viens d'inventer l'architecture narrative"
            pmj "j'aurais préféré l'inventer dans une pièce moins trouée"
            systeme "Ils testent des angles, ratent deux arrivées, puis décident que l'inutilité doit au moins être pratique."
            scene bg prologue slide branch
            play sound "fx/construction.mp3"
            with dissolve
            show jessy minecraft at char_left
            show ilona minecraft at char_right
            systeme "Le toboggan part d'une chambre inachevée et arrive devant un coffre vide. Ilona affirme que c'est une expérience narrative."
            pmi "on descend littéralement vers le mystère"
            pmj "le mystère contient trois graines"

        "Proposer d'assumer le désastre jusqu'au bout.":
            $ maison_minecraft_transformation = "piscine"
            $ lien_jessy_ilona += 2
            pmj "si le plafond est déjà ouvert, on peut arrêter de faire semblant que cette maison est normale"
            pmi "j'aime beaucoup cette phrase dangereuse"
            pmj "je regretterai peut-être dans quatre seaux d'eau"
            systeme "Ils commencent par poser une petite source. La petite source gagne rapidement un statut politique."
            scene bg prologue pool branch
            play sound "fx/water-minecraft.mp3"
            with dissolve
            show jessy minecraft at char_left
            show ilona minecraft at char_right
            systeme "La piscine traverse deux pièces, condamne un escalier et transforme une partie de la maison en station balnéaire non homologuée."
            pmj "il y a de l'eau dans le couloir"
            pmi "maintenant il mène quelque part"
            pmj "vers une assurance habitation"
    systeme "Quand la grande idée cesse de prendre toute la place, Ilona remarque un coin plus discret, caché derrière les escaliers et les murs ajoutés trop vite."
    play sound "fx/minecraft-door.mp3"
    scene bg prologue secret room
    with fade
    show jessy minecraft at char_left
    show ilona minecraft at char_right

    systeme "Après plusieurs détours, ils transforment ce renfoncement en petite salle secrète."
    play sound "fx/minecraft-wood-break-place.mp3"
    systeme "Ilona ajoute une porte inutile, posée presque pour le principe."
    pmj "cette porte sert à quoi ?"
    pmi "à garder le mystère"
    pmj "derrière, il y a surtout un coffre vide."
    pmi "exactement"

    systeme "La petite salle secrète ne contient rien d'utile : un coffre, des fleurs, une pancarte et l'impression étrange que quelque chose vient de commencer."
    pmi "on écrit quoi sur la pancarte ?"
    pmj "salle très importante"
    pmi "trop officiel"
    pmj "salle moyennement importante ?"
    pmi "parfait. Ça met la pression à personne."

    systeme "Ils ressortent ensuite de leur cachette improvisée. La maison n'est pas vraiment plus logique, mais elle commence à avoir des souvenirs dans les murs."
    play sound "fx/minecraft-walking-on-grass.mp3"
    if maison_minecraft_transformation == "serre":
        scene bg prologue greenhouse branch
    elif maison_minecraft_transformation == "piscine":
        scene bg prologue pool branch
    elif maison_minecraft_transformation == "toboggan":
        scene bg prologue slide branch
    else:
        scene bg prologue chicken roof branch
    with dissolve
    show jessy minecraft at char_left
    show ilona minecraft at char_right

    systeme "Le soleil descend encore. Entre les réparations et les idées dangereuses, le chat Minecraft devient trop lent pour leurs plans de portes, de murs et de cascades illégales."
    pmi "attends non pas CE mur"
    pmi "l'autre mur"
    pmi "celui qui est derrière le mur"
    pmj "il y a trois murs derrière le mur"
    pmi "exactement"
    pmi "on passe en vocal ?"
    pmi "ça ira plus vite que d'écrire non pas ce mur quarante fois"

    menu:
        "Comment Jessy répond-il à la proposition d'appel vocal ?"

        "Accepter tout de suite.":
            $ prologue_appel_discord = "direct"
            $ communication += 2
            $ confiance += 1
            $ jalousie = max(0, jalousie - 1)
            $ lien_jessy_ilona += 1
            pmj "oui"
            pmj "enfin oui, bonne idée"

        "Faire une blague avant d'accepter.":
            $ prologue_appel_discord = "blague"
            $ lien_jessy_ilona += 2
            pmj "seulement si tu promets de ne pas casser ma voix aussi"
            pmi "je ne promets rien"
            pmj "alors oui"

        "Demander une minute pour se préparer.":
            $ prologue_appel_discord = "minute"
            $ communication += 2
            $ confiance += 1
            $ jalousie = max(0, jalousie - 1)
            $ lien_jessy_ilona += 1
            pmj "oui"
            pmj "juste une minute, je dois retrouver mon casque et mon courage"
            pmi "prends le casque d'abord. Le courage peut arriver après."

    play sound "fx/discord-call-sound.mp3" volume 0.6
    $ renpy.pause(1.8, hard=True)
    systeme "Le premier appel commence avec une maladresse simple."
    j "Salut. Enfin... re-salut."
    i "Tu as une voix moins carrée que ton bâtiment."
    j "C'est très personnel comme attaque."
    i "J'ai cassé ton plafond. Je crois qu'on a dépassé le stade des politesses."
    systeme "Ils rient. Le silence qui suit n'est pas lourd. Il cherche juste où s'asseoir."
    i "Tu fais souvent ça ?"
    j "Construire des maisons trop grandes ?"
    i "Éviter les questions avec des détails techniques."
    j "..."
    j "Peut-être."
    i "C'est pas grave. C'est juste drôle."
    systeme "Elle ne force pas la porte. Lui ne prétend pas être déjà à l'aise. Ils continuent simplement à construire."

    play sound "fx/villager.mp3"
    show alex minecraft at char_center
    with dissolve
    if maison_minecraft_transformation == "poulet":
        pmx "Jessy, pourquoi il y a un poulet géant sur ton toit ?"
        pmj "c'est temporaire"
        pmi "c'est le gardien"
        pmx "de quoi ?"
        pmi "de la cuisine"
    elif maison_minecraft_transformation == "serre":
        pmx "Jessy, pourquoi il y a une serre suspendue dans ton mur cassé ?"
        pmj "c'est temporaire"
        pmi "c'est botanique"
        pmx "ça veut dire dangereux ?"
        pmi "c'est pour intimider les tomates"
    elif maison_minecraft_transformation == "piscine":
        pmx "Jessy, pourquoi il y a une piscine dans une pièce qui avait déjà des escaliers ?"
        pmj "c'est temporaire"
        pmi "c'est une amélioration du couloir"
        pmx "le couloir nage maintenant ?"
    else:
        pmx "Jessy, pourquoi il y a un toboggan qui arrive devant un coffre vide ?"
        pmj "c'est temporaire"
        pmi "c'est une descente vers le mystère"
        pmx "le mystère est vide ?"
    pmx "techniquement inhabitable."
    pmx "donc parfaite."
    play sound "fx/minecraft-wood-break-place.mp3"
    systeme "Alexandre pose une pancarte à l'entrée, comme s'il venait de rendre un verdict technique."
    systeme "NE SURTOUT PAS RENDRE ÇA NORMAL."
    hide alex
    with dissolve

    systeme "Alexandre se déconnecte aussi vite qu'il est arrivé. Sa pancarte reste, beaucoup trop convaincue d'avoir raison."
    play music audio.mcnight volume 0.8 fadeout 1.0
    scene bg prologue roof night
    with Dissolve(2.5)
    show jessy minecraft at char_left
    show ilona minecraft at char_right

    systeme "La nuit a fini de tomber. La maison est trop grande, mal équilibrée, et pleine de traces de leur première soirée."
    systeme "Sur le toit, les torches dessinent des coins chauds dans les murs irréguliers."
    $ renpy.pause(1.0, hard=True)
    i "Elle est vraiment trop grande."
    j "On peut enlever des pièces."
    i "Non. Ce serait triste."
    j "Même le couloir sans sortie ?"
    i "Surtout lui."

    systeme "Un mouvement près de la rivière attire leur attention. La distance rend la silhouette presque irréelle."
    scene bg prologue river laplage
    with dissolve
    show jessy minecraft at char_left
    show ilona minecraft at char_right
    $ renpy.pause(0.5, hard=True)
    play sound "fx/re-zero-return.mp3"
    show laplage minecraft at char_center
    with dissolve
    $ jugement_laplage += 1
    systeme "Au bord de la rivière, un personnage apparaît. Aucun message serveur ne l'annonce. Aucun pseudo ne flotte au-dessus de sa tête."
    systeme "Pendant une seconde, Jessy cherche l'explication la plus simple : un mod, un administrateur, une blague d'Alexandre. Rien ne colle vraiment."
    $ renpy.pause(0.8, hard=True)
    m_inconnu "Construire ensemble, c'est facile."
    $ renpy.pause(0.6, hard=True)
    m_inconnu "Le plus difficile, c'est de ne pas casser ce que l'autre construit."
    i "C'est un mod ?"
    j "J'espère que non."
    i "Il a un costume ?"
    j "Je ne veux pas savoir."
    hide laplage
    with dissolve

    systeme "Quand ils regardent de nouveau vers la rivière, le personnage a disparu. Les torches continuent de brûler comme si le monde refusait de confirmer ce qu'ils viennent de voir."
    i "On la finira un jour ?"
    j "Oui."
    j "On finira cette maison un jour."
    $ renpy.pause(2.0, hard=True)
    systeme "La dernière image reste sur la maison éclairée dans la nuit : maladroite, immense, inutile par endroits, mais désormais construite à deux."

    stop music fadeout 1.0
    jump arc_1_printemps
