# Arc III - Rentree : les regards.
# Les variables importantes restent centralisees dans script.rpy.

image bg arc3 festival hallway = im.Scale("images/scenes/arc_3/bg_arc3_festival_hallway.jpg", 1920, 1080)
image bg arc3 festival stand = im.Scale("images/scenes/arc_3/bg_arc3_festival_stand.jpg", 1920, 1080)
image bg arc3 festival courtyard = im.Scale("images/scenes/arc_3/bg_arc3_festival_courtyard.jpg", 1920, 1080)
image bg arc3 classroom evening = im.Scale("images/scenes/arc_3/bg_arc3_classroom_evening.jpg", 1920, 1080)
image bg arc3 minecraft night = im.Scale("images/scenes/arc_2/bg_arc2_minecraft_house_summer_night.jpg", 1920, 1080)

default arc3_reaction_rumeur = ""
default arc3_aide_stand = ""
default arc3_reaction_laplage = ""
default arc3_fin_minecraft = ""
default arc3_ilona_a_choisi_theme = False
default arc3_rumeur_aggravee = False
default arc3_theo_message_festival = False


label arc_3_rentree:
    scene bg shared train inside
    with fade

    systeme "Arc III - Rentrée : les regards."
    systeme "Septembre commence dans un train plus rempli que ceux de l'été."
    systeme "Les uniformes sont revenus, les cartables aussi, et avec eux cette façon qu'a l'école de transformer les petits silences en sujets collectifs."

    show jessy neutral at char_left
    show ilona neutral at char_right

    if arc2_choix_activite_theo == "confiance":
        i "J'ai encore du sable dans mes chaussures."
        j "Depuis juillet ?"
        i "C'est un sable engagé."
        j "Je respecte son implication."
        systeme "Ils rient doucement. La plage n'a pas disparu, mais elle ne prend pas toute la place."
    elif arc2_choix_activite_theo == "dix_minutes":
        i "Tu es revenu, ce jour-là."
        j "Oui."
        i "Je crois que j'y ai repensé plus que je voulais."
        j "Moi aussi."
        systeme "La phrase reste entre eux, pas lourde, pas légère. Présente."
    elif arc2_choix_activite_theo in ("suivre", "disparaitre"):
        systeme "Depuis la plage, leurs messages ont continué."
        systeme "Pas froids. Pas vraiment proches non plus."
        i "Tu as fini par retrouver ta serviette ?"
        j "Oui."
        i "C'est bien."
        systeme "Le silence qui suit n'est pas méchant. Il sait seulement trop bien où s'installer."
    else:
        i "La rentrée devrait être interdite avant midi."
        j "L'école entière ?"
        i "Surtout l'école entière."
        systeme "Leur humour revient, mais avec prudence, comme s'il vérifiait le sol avant d'avancer."

    systeme "À la station suivante, Allan monte avec un sac rempli de rouleaux de papier et l'air d'un homme vaincu par la colle."

    show allan excited at char_center
    with dissolve

    a "Bonne nouvelle : le festival culturel approche."
    j "Pourquoi tu annonces ça comme une catastrophe administrative ?"
    a "Parce que ma classe tient un café temporaire, votre classe aide sur la déco, et Théo est dans le comité de coordination."
    i "Donc il y aura des horaires."
    a "Il y aura des horaires, des listes et Alexandre avec des idées de portes inutiles."
    j "On est condamnés."

    if jalousie >= 2:
        systeme "Le prénom de Théo accroche Jessy un peu plus fort qu'il ne voudrait."
    elif souvenirs["jessy_nomme_sa_peur"]:
        systeme "Jessy sent la gêne monter, mais il la reconnaît assez tôt pour ne pas lui laisser toute la phrase."
    else:
        systeme "Le prénom de Théo passe dans la conversation. Il ne devrait pas changer l'air du wagon. Il le change quand même."

    i "On aide quel jour ?"
    a "Toute la semaine après les cours. Le thème n'est pas encore fixé."
    i "Alors je propose Blocky House Café."
    j "Pardon ?"
    i "Un café tout carré, avec des monstres en papier, des portes qui ne mènent pas tout à fait où on pense, et des menus beaucoup trop sérieux."
    a "Je note : café cubique juridiquement instable."
    j "Notre maison Minecraft est devenue un concept scolaire."
    i "Elle avait besoin d'un diplôme."

    $ arc3_ilona_a_choisi_theme = True
    $ lien_jessy_ilona += 1

    systeme "Ilona dit ça simplement, sans demander la permission à personne."
    systeme "Jessy devrait seulement être heureux de reconnaître leur souvenir dans sa voix."
    systeme "Il l'est."
    systeme "Et il remarque quand même que Théo va aider à construire ce souvenir avec eux."

    hide allan
    hide jessy
    hide ilona
    with dissolve

    scene bg arc3 festival hallway
    with fade
    show jessy neutral at char_left
    show alex grin at char_midleft
    show allan smirk at char_midright
    show ilona smile at char_right

    systeme "Le lendemain, le couloir du deuxième étage ressemble déjà à un chantier qui a perdu son responsable légal."
    x "J'ai dessiné un plan."
    j "Pourquoi il y a une cuisine au milieu de l'entrée ?"
    x "Référence culturelle."
    i "Validé."
    a "Je rappelle que les visiteurs doivent pouvoir acheter du café sans résoudre une énigme immobilière."
    x "Tu manques de foi dans le public."

    show theo reassuring at char_center
    with dissolve

    t "Si vous mettez la caisse ici, les gens bloqueront la porte."
    a "Il a raison."
    x "Je déteste quand la géométrie gagne."
    t "On peut garder l'idée de la porte inutile. Il suffit qu'elle ne soit pas sur le chemin principal."
    i "Donc une fausse porte importante."
    t "Exactement."
    i "J'aime bien."

    systeme "Théo ne vole pas l'idée. Il l'ajuste."
    systeme "C'est précisément ce qui rend la gêne plus difficile à nommer : il aide vraiment."

    hide alex
    hide allan
    with dissolve

    scene bg arc3 festival stand
    with fade
    show jessy neutral at char_left
    show ilona smile at char_center
    show theo neutral at char_right

    systeme "Trois jours plus tard, après les cours, Ilona colle les menus sur le panneau du stand."
    systeme "Le Blocky House Café a survécu aux réunions, ce qui tient presque du miracle."
    i "On devrait ajouter un menu : salle moyennement importante."
    j "C'est beaucoup trop intime comme référence."
    i "Justement. Personne ne comprendra, donc personne ne pourra contester."
    t "Je peux peindre le panneau si vous voulez."
    i "Oui, merci."

    systeme "Dans le couloir, deux élèves ralentissent en passant."
    systeme "Leur voix est assez basse pour prétendre ne rien dire, assez haute pour être entendue."
    systeme "\"C'est celle qui s'est fait ramener son porte-clés par l'autre, à la plage.\""
    systeme "\"Ouais. Apparemment Jessy regardait ailleurs. Pathétique.\""
    systeme "\"Elle va le larguer ou juste le faire attendre ?\""

    show ilona fatigue at char_center
    $ renpy.pause(0.8, hard=True)

    systeme "La colle continue de sécher. Le pinceau de Théo s'immobilise au-dessus du panneau."
    systeme "Jessy sent sa nuque chauffer. Pas de colère. De honte pure."
    systeme "Parce que la rumeur parle du porte-clés. Parce qu'ils savent. Parce qu'ils ont vu."
    if arc2_choix_activite_theo == "suivre":
        systeme "Et pire : quelqu'un a dû voir Jessy suivre Ilona ce jour-là."
    elif arc2_choix_activite_theo == "disparaitre":
        systeme "Et pire : quelqu'un a dû voir Jessy partir comme un lâche."

    menu:
        "La rumeur vient de tomber devant Ilona, Jessy et Théo."

        "Faire une blague pour désamorcer.":
            $ arc3_reaction_rumeur = "blague_desarm"
            $ communication += 1
            $ jalousie += 1
            $ lien_jessy_ilona += 1
            j "Techniquement, je suis surtout en train d'hésiter entre fuir et m'enterrer sous les menus."
            systeme "Ilona le regarde. Puis elle souffle un petit rire."
            show ilona smile at char_center
            i "Option trois : finir les panneaux et ignorer les cons."
            j "Validé."
            systeme "La blague a marché. Mais Jessy voit bien qu'Ilona sourit un peu trop fort."
            systeme "Ils viennent d'éviter la confrontation. Pas la blessure."

        "Regarder Ilona d'abord.":
            $ arc3_reaction_rumeur = "demander_ilona"
            $ communication += 2
            $ autonomie_ilona += 2
            $ ilona_peut_finir_ses_phrases += 1
            systeme "Jessy se tourne vers Ilona. Pas vers les élèves."
            j "Tu veux que je dise quelque chose ?"
            show ilona neutral at char_center
            systeme "Ilona serre le panneau dans ses mains."
            i "Non."
            i "Ils veulent une réaction. Je refuse de leur donner."
            systeme "Jessy hoche la tête. Ça lui coûte. Sa mâchoire travaille. Mais il se tait."
            systeme "Théo observe la scène. Il note que Jessy a écouté."
            t "Bonne décision."
            systeme "Ilona tourne la tête vers Théo."
            i "Je n'ai pas demandé ton avis."
            systeme "Théo cligne des yeux. Surpris. Puis il baisse les yeux vers son pinceau."
            t "Pardon."

        "Se taire et laisser passer.":
            $ arc3_reaction_rumeur = "silence_paralysie"
            $ communication -= 1
            $ pression_stream += 1
            $ arc3_rumeur_aggravee = True
            systeme "Jessy baisse les yeux sur les menus."
            systeme "Il pourrait parler. Il devrait peut-être."
            systeme "Mais la honte lui coupe les jambes."
            systeme "Ilona attend une seconde. Elle n'attend pas qu'il la sauve. Elle attend seulement qu'il soit là."
            systeme "Puis elle colle le dernier panneau avec un soin trop précis."
            systeme "Théo voit le silence. Il le range soigneusement dans sa mémoire."

        "Défendre Ilona immédiatement.":
            $ arc3_reaction_rumeur = "defendre_immediat"
            $ communication += 1
            $ jalousie += 1
            j "Hé."
            systeme "Les deux élèves se retournent."
            j "Si vous voulez inventer une histoire, au moins ayez le courage de la dire en face."
            show ilona neutral at char_center
            systeme "Ilona pose la main sur son bras."
            i "Jessy..."
            j "Quoi ? Ils parlent de toi comme si t'étais un trophée."
            i "Je sais. Mais tu viens de leur donner exactement ce qu'ils voulaient."
            systeme "Les deux élèves s'éloignent en ricanant. Jessy a défendu Ilona. Il l'a aussi confirmé comme spectacle."
            t "Sur le fond, t'as raison. Sur la forme..."
            j "Je sais."
            systeme "Jessy a défendu Ilona. Mais il a aussi parlé pour elle sans demander."

    systeme "Théo reprend le pinceau. Son regard reste sur Ilona."
    t "Ils sont bêtes."
    i "..."
    systeme "Ilona ne répond pas tout de suite. Elle colle le panneau. Théo attend."
    t "Mais ils voient quand même qu'on te met une pression que tu n'as pas demandée."
    systeme "Ilona s'arrête. Elle le regarde."
    i "..."
    systeme "Elle devrait le remettre à sa place. Elle le sait."
    systeme "Mais une partie d'elle entend ce qu'il dit. Et cette partie-là est fatiguée de devoir tout gérer seule."
    $ renpy.pause(1.2, hard=True)
    i "Oui. Ils me mettent une pression."
    systeme "Elle dit ça doucement. Puis elle se reprend."
    i "Mais là, c'est toi qui es en train de me la remettre dans les mains."
    t "Je voulais juste..."
    i "Je sais."
    systeme "Elle soupire."
    i "C'est souvent le problème."
    if arc3_reaction_rumeur in ("blague_desarm", "silence_paralysie"):
        $ influence_theo += 1
        $ remember("theo_utilise_une_verite")
        systeme "Même repris, Théo a réussi à créer un moment entre eux. Ilona a baissé sa garde deux secondes."
        systeme "Deux secondes, c'est déjà beaucoup."
    else:
        systeme "Cette fois, Ilona refuse la douceur qui arrive avec une facture."

    hide theo
    hide jessy
    hide ilona
    with dissolve

    scene bg arc3 festival stand
    with fade
    show jessy neutral at char_left
    show ilona smile at char_midleft
    show theo neutral at char_midright
    show allan neutral at char_right

    systeme "Le jour du festival arrive avec une file beaucoup trop longue pour un café monté par des lycéens fatigués."
    systeme "Allan prend les commandes. Théo gère la circulation. Ilona ajuste les panneaux du thème qu'elle a choisi."
    a "Table deux : deux cafés, un melon soda, et une question sur la porte inutile."
    i "Dis que la porte inutile est en réflexion."
    t "La porte inutile est en pause."
    systeme "Allan s'arrête. Il regarde Théo."
    systeme "Théo vient de répondre à la place d'Ilona. Encore."
    a "... Oui. Ça."
    systeme "Allan ne dit rien de plus. Mais quelque chose vient de se fissurer dans sa neutralité."
    systeme "Le client accepte cette réponse avec une inquiétante facilité."

    show alex teasing at char_center
    with dissolve

    x "Je confirme : le public respecte l'architecture narrative."
    t "Le public cherche surtout les toilettes."
    i "Deux choses peuvent être vraies."

    systeme "Pendant quelques minutes, le stand fonctionne presque."
    systeme "Puis la file s'allonge, les rumeurs reviennent par fragments, et chaque déplacement met quelqu'un trop près ou trop loin de quelqu'un d'autre."

    hide alex
    hide allan
    with dissolve

    menu:
        "Ilona et Théo travaillent côte à côte au stand. Comment Jessy choisit-il d'être présent ?"

        "Aider sans se mettre au centre.":
            $ arc3_aide_stand = "aider_retrait"
            $ lien_jessy_ilona += 1
            $ autonomie_ilona += 1
            $ communication += 1
            $ confiance += 1
            j "Dis-moi où tu as besoin de moi."
            show ilona smile at char_midleft
            i "La caisse déborde. Prends les commandes avec Allan."
            j "Reçu."
            systeme "Jessy s'éloigne de deux mètres. Chaque mètre pique. Il le fait quand même."
            systeme "Il a choisi d'être utile plutôt que d'être visible."
            systeme "Mais il sait aussi qu'il recule parce qu'il a peur de ce qu'il pourrait dire s'il restait."

        "Annoncer besoin d'air et revenir.":
            $ arc3_aide_stand = "distance_honnete"
            $ jalousie += 1
            $ communication += 2
            $ confiance += 1
            $ remember("jessy_nomme_sa_peur")
            j "Je suis jaloux."
            systeme "Ilona lève les yeux. Théo arrête de bouger."
            j "Voilà. C'est dit, c'est moche, et je ne veux pas te le jeter dessus."
            j "Je vais aider au couloir dix minutes. Je reviens."
            show ilona neutral at char_midleft
            i "D'accord."
            systeme "Elle ne sourit pas. Mais elle le regarde comme si elle venait de voir quelque chose de vrai."
            i "Reviens vraiment."
            j "Oui."
            systeme "Jessy a été honnête. Mais il sait aussi qu'il vient de mettre sa jalousie dans l'espace entre eux."

        "Demander franchement ce qu'elle ressent.":
            $ arc3_aide_stand = "demande_directe"
            $ lien_jessy_ilona += 1
            $ communication += 1
            $ jalousie += 1
            $ autonomie_ilona += 1
            j "J'ai l'impression de te perdre dans une pièce où je suis juste à côté de toi."
            systeme "Théo s'écarte légèrement. Ilona pose son panneau."
            show ilona neutral at char_midleft
            j "Dis-moi si je deviens fou."
            i "Tu ne deviens pas fou."
            $ renpy.pause(0.8, hard=True)
            i "Mais quand tu me regardes comme si j'avais déjà choisi de partir, ça me donne envie de sortir."
            j "Ça fait mal à entendre."
            i "Je sais."
            systeme "La réponse n'est pas douce. Elle est vivante."
            systeme "Mais Jessy vient aussi de demander une réponse émotionnelle au milieu d'un stand bondé."

        "Faire blague acide pour cacher blessure.":
            $ arc3_aide_stand = "blague_defense"
            $ jalousie += 2
            $ communication -= 1
            $ autonomie_ilona -= 1
            $ pression_stream += 1
            j "Je peux mettre une pancarte : attention, rivalité servie avec supplément malaise ?"
            show ilona frustrated at char_midleft
            i "Tu crois vraiment que j'avais besoin de ça ?"
            systeme "Jessy ouvre la bouche. La referme."
            t "Si tu veux faire rire, choisis une cible qui peut répondre."
            j "Merci, professeur."
            systeme "La phrase de Jessy part sèchement. Elle ne fait pas rire."
            systeme "Mais elle dit au moins une vérité : il est jaloux, il souffre, et il ne sait pas comment le dire autrement."

    hide jessy
    hide ilona
    hide theo
    with dissolve

    scene bg arc3 festival hallway
    with fade
    show allan doubt at char_left
    show alex grin at char_midleft

    systeme "En milieu d'après-midi, Allan et Alexandre se retrouvent au bout du couloir avec une caisse de gobelets et une enquête qui n'a demandé l'autorisation de personne."

    a "Information importante : Monsieur Laplage tient le stand de takoyaki dans la cour."
    x "Faux. Information plus importante : je l'ai aussi vu entrer dans un couloir fermé."
    a "Peut-être qu'il a une clé."
    x "Ou peut-être que le couloir a peur de lui refuser l'entrée."
    a "Je refuse cette hypothèse parce qu'elle me plaît trop."

    show sofiane observation at char_right
    with dissolve

    s "Les preuves ne mentent pas. Elles choisissent juste leur témoin."
    x "Tu étais là depuis quand ?"
    s "Depuis le début de votre erreur."
    a "Tu as un takoyaki ?"
    s "Il m'a choisi."
    systeme "Sofiane regarde le takoyaki comme si c'était un artefact cosmique."
    systeme "Puis il lève les yeux vers Allan."
    s "Vous cherchez à comprendre Monsieur Laplage."
    a "Oui ?"
    s "Mauvaise quête. Cherchez plutôt pourquoi vous avez besoin de comprendre."
    systeme "Allan et Alexandre échangent un regard."
    x "C'est... profond ?"
    a "Ou complètement vide."
    s "Les deux. Comme un parking souterrain."
    systeme "Sofiane mord dans son takoyaki. Puis il ajoute :"
    s "Certaines personnes parlent pour remplir le silence. D'autres pour le creuser."
    systeme "Il regarde vers le couloir où Théo vient de passer."
    s "Faites attention à ceux qui creusent."
    hide sofiane
    with dissolve

    systeme "Sofiane repart sans expliquer."
    systeme "Allan et Alexandre restent bouche bée."
    x "Il parlait de Laplage ou de Théo ?"
    a "... Je sais pas."
    systeme "Le rire revient. Mais quelque chose vient d'être planté."

    hide allan
    hide alex
    with dissolve

    scene bg arc3 festival courtyard
    with fade
    show ilona fatigue at char_left

    systeme "Un peu plus tard, Ilona quitte le stand avec un plateau vide."
    systeme "Elle a dit qu'elle allait rapporter des serviettes."
    systeme "En vérité, elle suit surtout l'odeur des takoyaki et l'idée vague d'un endroit où personne ne lui demande de trancher sa propre vie entre deux commandes."
    systeme "La cour du lycée a pris des airs de petite ville provisoire."
    systeme "À gauche, un stand de tir promet des lots beaucoup trop grands pour ses étagères. Plus loin, des lanternes rouges tremblent au-dessus des bancs."
    systeme "Des élèves passent avec des brochettes, des sacs en papier, des bracelets fluorescents. Personne ne la regarde vraiment."
    systeme "Ce détail devrait être banal. Aujourd'hui, il lui fait presque du bien."
    systeme "Ilona s'arrête devant un petit étal de sucreries. Entre deux sachets de konpeitō, elle achète une étoile en sucre simplement parce qu'elle brille."
    i "Toi, tu as l'air de savoir ne rien décider."
    systeme "Elle glisse l'étoile dans son sac, puis reprend sa marche jusqu'au stand de takoyaki."

    show laplage neutral at char_center
    with dissolve

    $ confidences_laplage += 1
    $ jugement_laplage += 1

    laplage "Takoyaki."
    i "Vous travaillez ici ?"
    laplage "Aujourd'hui, je tourne les sphères."
    i "C'est une réponse ou une menace ?"
    laplage "Une cuisson."
    systeme "Ilona regarde les boulettes tourner dans leurs moules. Elles ont le droit d'être retournées sans que personne n'appelle ça une trahison."

    $ renpy.pause(1.0, hard=True)
    i "Je suis..."
    systeme "Elle s'arrête. Cherche le mot."
    i "Je suis en colère."
    laplage "Contre qui ?"
    i "Jessy. Les gens. Moi."
    systeme "Elle serre son plateau."
    i "Et Théo... quand Théo est gentil, ça..."
    systeme "Elle ne finit pas. Elle ne sait pas comment finir."
    i "Ça me repose. Et après je m'en veux."
    laplage "Les gens confondent souvent le repos avec une destination."
    i "Vous pouvez parler normalement une fois dans votre vie ?"
    laplage "Non."
    $ renpy.pause(1.2, hard=True)
    systeme "Ilona respire. Puis elle lâche."
    i "Je ne veux pas choisir devant tout le monde."
    i "Mais je ne veux pas non plus... faire comme si..."
    systeme "Elle cherche encore. Les mots ne viennent pas propres."
    i "Comme si ça me plaisait pas quand quelqu'un me regarde comme si j'étais facile à comprendre."
    systeme "Monsieur Laplage retourne un takoyaki."
    laplage "Deux voix fortes ne font pas une vérité."
    laplage "Elles font surtout du bruit."
    i "Et si celle dans ma tête crie aussi ?"
    laplage "Alors mange un takoyaki avant de lui répondre."
    show laplage thumb_up at char_center
    laplage "Un cœur vide prend de mauvaises décisions."
    show laplage neutral at char_center

    i "C'est frustrant, vos phrases."
    laplage "C'est offert avec la sauce."
    i "Je ne voulais pas une réponse toute faite."
    laplage "Alors excellent service."

    hide laplage
    with dissolve

    systeme "Quand Ilona se retourne, le stand de takoyaki est toujours là."
    systeme "Monsieur Laplage, lui, discute maintenant avec une cliente qui jure qu'il était au stand de tir il y a trente secondes."
    systeme "Ilona respire une fois, puis reprend le chemin du café."

    scene bg arc3 festival hallway
    with fade
    show jessy neutral at char_left

    if arc3_aide_stand == "distance_honnete":
        systeme "Jessy revient du couloir avec une pile de serviettes et dix minutes vraiment tenues."
        systeme "Il a compté les minutes comme on compte les battements quand on veut vérifier que quelque chose vit encore."
    elif arc3_aide_stand == "aider_retrait":
        systeme "Jessy a passé l'après-midi à prendre des commandes. Il a vu Ilona rire de loin avec Théo, puis rire avec Allan, puis rire toute seule devant un menu mal collé."
        systeme "Le rire avec Théo n'était pas une preuve. C'est fou comme une absence de preuve peut quand même brûler."
    elif arc3_aide_stand == "demande_directe":
        systeme "Jessy n'a pas obtenu de réponse claire."
        systeme "Il tourne autour de cette absence comme autour d'une porte fermée dont il connaît déjà trop bien la poignée."
    else:
        systeme "Jessy a essayé de redevenir utile après sa blague."
        systeme "Le problème, c'est qu'une phrase maladroite continue souvent à travailler même quand les mains font autre chose."

    show theo neutral at char_right
    with dissolve

    t "Elle est sortie prendre l'air."
    j "J'ai vu."
    t "Non. Tu as vu qu'elle n'était plus là."
    t "Ce n'est pas pareil."
    j "Tu fais ça avec tout le monde ?"
    t "Quoi ?"
    j "Transformer une phrase simple en diagnostic."
    t "Seulement quand la phrase simple sert à éviter la vraie."
    $ renpy.pause(0.8, hard=True)
    t "Et parce que je crois que certaines personnes écoutent Ilona seulement quand elles ont peur de la perdre."

    $ arc3_theo_message_festival = True
    $ remember("theo_utilise_une_verite")

    systeme "Jessy sent la phrase entrer exactement là où elle voulait entrer."
    systeme "Ce n'est pas une insulte. C'est pire : une vérité utilisée comme une lame."

    menu:
        "Théo vient de toucher juste, et Jessy le sait."

        "Admettre la blessure sans baisser les yeux.":
            $ communication += 1
            $ confiance += 1
            j "Oui."
            j "Parfois je l'écoute mal parce que j'ai peur."
            j "Mais toi, tu l'écoutes comme si chaque silence était une place à prendre."
            show theo neutral at char_right
            t "Tu dis ça parce que ça t'arrange de me voir comme le problème."
            j "Non."
            j "Je dis ça parce que tu attends toujours le moment où j'ai honte pour devenir indispensable."
            systeme "Le visage de Théo ne change presque pas. Ses doigts, eux, se referment sur le bord de la table."

        "Lui rentrer dedans.":
            $ jalousie += 2
            $ influence_theo += 1
            $ communication -= 1
            j "Tu préparais cette phrase depuis combien de temps ?"
            show theo annoyed at char_right
            t "Depuis que je t'ai vu la regarder comme si elle te devait une preuve."
            j "Et toi, depuis quand tu fais semblant de l'aider alors que tu veux juste être celui qu'elle choisit quand elle est fatiguée ?"
            t "Attention, Jessy."
            j "Non. Toi, attention."
            j "Arrête de parler doucement comme si ça rendait tes coups plus propres."
            systeme "Cette fois, le ton monte. Deux élèves se retournent au bout du couloir."

        "Se taire pour ne pas exploser.":
            $ communication -= 1
            $ pression_stream += 1
            $ influence_theo += 1
            systeme "Jessy serre la mâchoire."
            systeme "Il pourrait répondre. Il a même trois phrases prêtes, toutes trop violentes, toutes un peu vraies."
            systeme "Théo le regarde se retenir. Puis il sourit. Pas beaucoup. Juste assez."
            t "Tu vois ? Même là, tu préfères qu'elle devine."
            systeme "Jessy ne bouge pas."
            t "Et tu sais ce qui est drôle ?"
            systeme "Théo se rapproche d'un pas."
            t "C'est que tu penses que te taire, c'est être respectueux. Mais en vrai, tu la laisses juste seule avec ses questions."
            systeme "Il marque une pause."
            t "Alors elle vient chercher des réponses ailleurs."
            systeme "Jessy sent quelque chose se fissurer dans sa poitrine."
            if arc2_choix_activite_theo in ("suivre", "disparaitre"):
                t "Comme à la plage."
                systeme "Théo dit ça sans hausser la voix. Il n'a pas besoin. Le coup est déjà parti."
            systeme "Le silence ne protège personne. Il laisse juste Théo remplir le vide."

        "Refuser le duel, mais pas la colère.":
            $ communication += 2
            $ autonomie_ilona += 1
            $ ilona_peut_finir_ses_phrases += 1
            j "J'ai envie de te répondre."
            j "J'ai très envie."
            j "Mais ce serait encore deux gars qui règlent leur fierté sur son dos."
            show theo neutral at char_right
            t "C'est pratique, la morale, quand on perd l'avantage."
            j "Ce n'est pas de la morale."
            j "C'est moi qui essaie de ne pas devenir exactement ce que tu attends."

    systeme "Pendant une seconde, le couloir paraît trop petit pour eux deux."
    systeme "Jessy déteste Théo à cet instant."
    systeme "Il le déteste d'autant plus qu'une partie de ce qu'il a dit restera vraie même si Théo disparaissait."

    hide theo
    with dissolve

    systeme "Théo s'éloigne. Jessy reste seul dans le couloir."
    systeme "Ses mains tremblent. Pas de colère. D'épuisement."

    show sofiane observation at char_center
    with dissolve

    systeme "Sofiane apparaît au bout du couloir. Il tient deux cannettes de thé vert."
    systeme "Il en tend une à Jessy sans un mot."
    j "... Merci."
    systeme "Jessy ouvre la cannette. Boit. Le silence s'installe."
    systeme "Sofiane ne dit rien. Il regarde le couloir comme s'il observait une route de nuit."
    $ renpy.pause(1.5, hard=True)
    s "Tu cherches à comprendre pourquoi il a raison."
    j "Quoi ?"
    s "Théo. Tu cherches la part de vérité dans ce qu'il a dit."
    systeme "Jessy serre la cannette."
    j "Et alors ?"
    s "Alors c'est bien. Ça veut dire que tu écoutes encore."
    systeme "Sofiane boit une gorgée."
    s "Mais fais attention."
    j "À quoi ?"
    s "À ceux qui disent la vérité seulement quand ça te met à genoux."
    systeme "Jessy lève les yeux. Sofiane le regarde."
    s "La vérité peut être une main tendue. Ou un poing fermé."
    s "Théo sait très bien laquelle il utilise."
    systeme "Jessy reste silencieux. Sofiane hoche la tête."
    s "Les routes de montagne apprennent une chose : ralentir n'est pas reculer."
    systeme "Il froisse sa cannette vide."
    s "Prends ton temps. Mais ne t'arrête pas."
    hide sofiane
    with dissolve

    systeme "Sofiane repart sans attendre de réponse."
    systeme "Jessy reste seul avec sa cannette et une phrase qui pèse moins lourd que la colère."

    show ilona neutral at char_right
    with dissolve

    systeme "Ilona revient avec les serviettes, même si personne ne sait très bien quand elle les a récupérées."
    systeme "Elle s'arrête une seconde en voyant leurs visages."
    systeme "Jessy comprend trop tard qu'un duel laisse toujours une odeur dans la pièce, même quand personne n'a crié assez fort pour l'avouer."
    i "J'ai croisé Monsieur Laplage."
    j "Au stand de takoyaki ?"
    i "Oui."
    j "Logique."
    i "Non."
    j "C'est vrai."
    i "Il a dit une phrase de Monsieur Laplage."
    j "Donc frustrante ?"
    i "Très."

    systeme "Elle serre les serviettes contre elle, puis regarde Jessy, puis l'endroit où Théo était encore une seconde plus tôt."
    i "Vous vous êtes disputés ?"
    j "Pas vraiment."
    i "Jessy."
    $ renpy.pause(0.8, hard=True)
    j "Oui."
    i "Merci."
    j "Merci ?"
    i "De ne pas me mentir plus longtemps que ça."
    systeme "Sa voix tremble à peine. C'est presque ce qui inquiète le plus Jessy."
    i "Je ne veux pas que notre thème devienne un spectacle."
    j "Comment ça ?"
    i "Le Blocky House Café. C'était notre maison Minecraft."
    i "Une blague à nous, cachée dans un concept scolaire."
    i "Je l'ai proposée parce que je pensais à nous."
    i "Et maintenant, quand je regarde les panneaux, j'ai l'impression que tout le monde a mis ses doigts dans un souvenir qui n'était pas à eux."
    if jalousie >= 3 or arc3_reaction_rumeur == "silence_paralysie" or arc3_aide_stand == "blague_defense":
        i "Je suis en colère contre toi."
        i "Je suis aussi contente quand tu me cherches dans une foule."
    elif jalousie >= 1 or arc3_reaction_rumeur == "defendre_immediat":
        i "Je suis frustrée."
        i "Parce que tu fais des efforts, mais parfois tes efforts ressemblent à de la surveillance."
        i "Et je suis aussi contente quand tu me cherches dans une foule."
    else:
        i "Je suis perdue."
        i "Tu essaies de me laisser respirer, et ça me rassure."
        i "Mais en même temps, ça me fait peur que tu recules trop loin."
    i "Et je déteste que Théo remarque quand je fatigue, parce qu'une partie de moi trouve ça agréable."
    i "Voilà. Ce n'est pas propre. Ce n'est pas une belle réponse."
    i "Mais c'est ce que j'ai."

    menu:
        "Ilona vient de lâcher une vérité désordonnée, presque trop intime pour le couloir."

        "Lui dire qu'il l'aime trop pour faire semblant.":
            $ arc3_reaction_laplage = "demander_besoin"
            $ communication += 2
            $ autonomie_ilona += 1
            $ confiance += 1
            $ ilona_peut_finir_ses_phrases += 1
            j "Je ne peux pas faire semblant que ça ne me tue pas un peu."
            j "Quand tu ris avec lui, quand il voit ce que je rate, quand tu reviens avec cet air que je ne sais plus lire..."
            j "Je déteste ça."
            j "Mais je t'aime assez pour ne pas transformer cette haine en laisse."
            show ilona smile at char_right
            i "C'est la première phrase honnête qui ne me demande pas de te sauver."
            j "Je ne sais pas si je vais réussir tout le temps."
            i "Je ne te demande pas d'être parfait."
            i "Je te demande de ne pas me punir parce que tu as peur."

        "S'excuser sans se rendre petit.":
            $ arc3_reaction_laplage = "excuse_precise"
            $ communication += 2
            $ autonomie_ilona += 2
            $ confiance += 1
            if arc3_aide_stand == "blague_defense" or arc3_reaction_rumeur == "blague_desarm":
                $ remember("jessy_repare")
            if interruptions_ilona > interruptions_reconnues:
                $ interruptions_reconnues += 1
                $ interruptions_reparees += 1
            show jessy listening at char_left
            if arc3_aide_stand == "blague_defense" or arc3_reaction_rumeur == "blague_desarm":
                j "Désolé pour la blague. Et pour les silences."
            else:
                j "Désolé pour les silences. Pour les regards qui accusent."
            j "Pas désolé d'être jaloux. Je le suis."
            j "Mais désolé de t'avoir laissée seule avec ce que ma jalousie fabriquait."
            i "Ça, je peux l'entendre."
            i "Même si j'ai encore envie de te secouer."
            j "Mérité."
            i "Un peu."

        "Promettre que Théo ne compte pas.":
            $ arc3_reaction_laplage = "promesse_theo"
            $ jalousie += 1
            $ communication -= 1
            $ autonomie_ilona -= 1
            j "Théo ne compte pas. Je te le promets."
            show ilona frustrated at char_right
            i "Tu ne peux pas promettre ça à ma place."
            j "Je voulais dire que je te fais confiance."
            i "Non."
            i "Tu voulais que je dise que rien ne tremble."
            i "Et je ne peux pas te donner ça juste pour que tu respires."

        "Demander une réponse sur ses sentiments.":
            $ arc3_reaction_laplage = "demande_reponse"
            $ jalousie += 2
            $ confiance -= 1
            $ autonomie_ilona -= 1
            $ influence_theo += 1
            $ pression_stream += 1
            j "Et moi ?"
            j "Je suis où, là-dedans ?"
            show ilona fatigue at char_right
            i "Je ne sais pas."
            j "Tu ne sais pas ?"
            i "Non."
            i "Et si je mens pour te rassurer maintenant, tu vas le sentir. Puis tu vas me le reprocher. Puis je vais t'en vouloir de m'avoir forcée à choisir une phrase fausse."
            j "Je te force ?"
            i "Là ? Oui."

    if arc3_reaction_laplage == "demander_besoin":
        systeme "Ilona baisse les yeux sur les serviettes qu'elle serre encore contre elle."
        i "Reste à côté de moi pour les dernières commandes."
        j "Tu es sûre ?"
        i "Non."
        i "Mais j'en ai envie maintenant. C'est déjà assez compliqué comme ça."
        systeme "Jessy prend une partie de la pile. Leurs doigts se touchent à peine."
        systeme "Ce n'est pas une réconciliation. C'est plus fragile, plus dangereux peut-être : une envie maintenue malgré la peur."
        $ lien_jessy_ilona += 1
    elif arc3_reaction_laplage == "excuse_precise":
        systeme "Ilona expire, comme si elle posait enfin un sac trop lourd sans savoir s'il va tomber."
        i "Viens."
        j "Où ?"
        i "Ranger les tasses."
        j "C'est une punition ?"
        i "C'est une activité où tu peux être utile sans faire de discours."
        systeme "Il sourit malgré lui. Elle aussi, une seconde trop courte pour appeler ça du pardon."
        systeme "Mais quand elle lui tend une pile de tasses, elle ne retire pas sa main tout de suite."
        $ confiance += 1
    elif arc3_reaction_laplage == "promesse_theo":
        systeme "Ilona regarde vers le stand, puis vers la cour où Théo a disparu."
        i "Le problème, c'est que tu veux effacer son nom pour te rassurer."
        j "Je veux juste qu'il arrête d'être entre nous."
        i "Il est entre nous parce qu'on lui laisse une place dans chaque phrase."
        systeme "Cette fois, elle ne lui donne pas les serviettes. Elle les garde contre elle et reprend la marche la première."
        systeme "Jessy la suit avec l'impression absurde d'avoir perdu deux pas dans un couloir de trois mètres."
        $ influence_theo += 1
        $ pression_stream += 1
    else:
        systeme "Ilona ne bouge pas tout de suite."
        systeme "Dans le bruit du festival, son silence a quelque chose de presque violent."
        i "Je ne peux pas te répondre là."
        j "Je sais."
        i "Non. Tu ne sais pas. Si tu savais, tu ne me l'aurais pas demandé comme ça."
        systeme "Elle pose une partie des serviettes dans ses bras."
        i "Tiens. Aide-moi au moins à finir la journée."
        systeme "Le geste ressemble à une confiance. Il ressemble aussi à une distance : elle lui donne quelque chose à porter parce qu'elle ne peut plus porter sa question."
        $ pression_stream += 1

    systeme "Derrière eux, Allan annonce qu'il manque deux cafés et qu'Alexandre a écrit \"porte en réflexion\" sur une vraie porte de secours."
    i "Il faut y retourner."
    j "Oui."
    i "Pas pour faire comme si tout allait bien."
    j "Non."
    i "Pour finir ce qu'on a commencé aujourd'hui."
    j "D'accord."

    hide jessy
    hide ilona
    with dissolve

    scene bg arc3 classroom evening
    with fade
    show allan neutral at char_left
    show alex grin at char_midleft
    show jessy neutral at char_midright
    show ilona neutral at char_right

    systeme "Le soir tombe sur la salle de classe vidée de ses visiteurs."
    systeme "Les nappes sont tachées, les panneaux se décollent aux coins, et la porte inutile tient encore debout par pure conviction."

    a "Bilan : on a vendu tout le café."
    x "Et trois personnes ont demandé si la porte inutile menait à une quête secrète."
    i "On aurait dû facturer l'accès au mystère."
    j "Le mystère aurait contenu un placard."
    x "Parfait. Réalisme brutal."

    show sofiane smirk at char_center
    with dissolve

    s "Les placards sont des portes qui ont renoncé au voyage."
    a "Sofiane, tu as aidé aujourd'hui ?"
    s "J'ai empêché un takoyaki de connaître le sol."
    x "Héros discret."
    a "Sérieusement, t'as fait quoi ?"
    systeme "Sofiane sort son téléphone. Montre une photo."
    systeme "C'est une liste. Parfaitement organisée. Tous les horaires de nettoyage, de rangement, et de récupération du matériel."
    x "... Tu as fait un planning ?"
    s "Quelqu'un devait conduire le chaos vers une sortie."
    a "Depuis quand tu fais ça ?"
    s "Depuis que j'ai remarqué que personne ne savait où étaient les clés de la réserve."
    systeme "Il range son téléphone."
    s "Les festivals sont comme les virages en épingle. Si personne ne freine avant, tout le monde sort de la route."
    systeme "Allan et Alexandre se regardent."
    a "Merci, Sofiane."
    s "Les routes ne remercient pas. Elles attendent juste qu'on les respecte."
    systeme "Il hoche la tête. Puis il regarde Jessy."
    s "Ça va ?"
    j "... Oui."
    s "Bien."
    systeme "Sofiane ne demande rien de plus. Il repart vers la sortie."
    hide sofiane
    with dissolve

    systeme "Le groupe reste silencieux une seconde."
    x "Sofiane a organisé tout le rangement sans qu'on le sache."
    a "Et il a donné une leçon de conduite métaphorique à Jessy."
    i "C'est son super-pouvoir."
    systeme "Le groupe rit. La fatigue rend le rire un peu fragile, mais il existe."

    if arc3_reaction_laplage == "demander_besoin":
        show ilona smile at char_right
        systeme "Ilona décroche le panneau principal avec soin."
        i "On garde celui-là ?"
        j "Oui."
        j "Si tu veux."
        i "Je veux."
        $ lien_jessy_ilona += 1
        $ confiance += 1
    elif arc3_reaction_laplage == "excuse_precise":
        show ilona neutral at char_right
        systeme "Ilona décroche le panneau principal avec soin."
        i "On le garde."
        j "D'accord."
        i "Pas parce que tout va bien."
        j "Je sais."
        i "Parce que je ne veux pas jeter une journée entière juste parce qu'elle a fait mal."
        systeme "Jessy prend le panneau par l'autre côté. Cette fois, ils le portent vraiment à deux."
        $ lien_jessy_ilona += 1
        $ confiance += 1
    elif arc3_reaction_laplage == "promesse_theo":
        show ilona fatigue at char_right
        systeme "Ilona décroche le panneau principal, hésite, puis le tend à Allan."
        i "Tu peux le garder avec le matériel de classe ?"
        a "Oui. Bien sûr."
        systeme "Jessy comprend qu'elle ne veut pas le ramener avec eux ce soir."
        systeme "Pas le jeter. Pas le sauver non plus."
        $ pression_stream += 1
    else:
        show ilona fatigue at char_right
        systeme "Ilona décroche le panneau principal sans demander si quelqu'un veut le garder."
        systeme "Elle le pose contre le mur, face cachée."
        systeme "Alexandre ouvre la bouche, puis la referme. Même lui comprend que ce panneau-là n'appelle pas une blague."
        $ pression_stream += 1

    hide allan
    hide alex
    hide jessy
    hide ilona
    with dissolve

    scene bg arc3 minecraft night
    with Dissolve(2.0)
    show jessy minecraft at char_left
    show ilona minecraft at char_right

    systeme "Le soir même, la maison Minecraft se charge lentement."
    systeme "Elle n'a pas connu le festival, mais elle semble en porter les traces : une cuisine de trop, une porte inutile, un couloir qui attend encore qu'on décide s'il mène quelque part."

    if arc3_reaction_laplage == "demander_besoin":
        $ arc3_fin_minecraft = "panneau_finir_phrase"
        $ communication += 1
        $ autonomie_ilona += 1
        i "Je vais poser un panneau."
        j "Où ?"
        i "Près de la salle moyennement importante."
        systeme "Elle écrit lentement, comme si chaque mot devait avoir assez de place."
        i "ICI, LES PHRASES ONT LE DROIT DE TREMBLER."
        j "C'est une règle ?"
        i "Un avertissement."
        j "Alors je vais essayer de ne pas faire semblant de savoir lire trop vite."
        $ maison_minecraft_ajouts.append("panneau_phrases_tremblent_arc3")
    elif arc3_reaction_laplage == "excuse_precise":
        $ arc3_fin_minecraft = "rangement_silencieux"
        $ confiance += 1
        i "Je vais ranger la cuisine d'été."
        j "Ranger ?"
        i "Pas casser. Pas réparer. Ranger."
        systeme "Elle déplace trois coffres, enlève une table de trop, remet une lanterne droite."
        systeme "Le geste est petit, presque domestique. Il dit pourtant quelque chose que Jessy entend très clairement : je ne pars pas, mais je ne fais pas comme si rien n'avait bougé."
        j "Je peux aider ?"
        i "Oui."
        i "Mais doucement."
        $ maison_minecraft_ajouts.append("cuisine_ete_rangee_arc3")
    elif arc3_reaction_laplage == "promesse_theo":
        $ arc3_fin_minecraft = "porte_fermee"
        $ pression_stream += 1
        systeme "Ilona avance jusqu'à la porte inutile."
        systeme "Elle pose un bouton à côté, puis un bloc devant."
        j "Tu la fermes ?"
        i "Pour ce soir."
        j "Elle ne menait nulle part."
        i "Justement."
        systeme "Jessy comprend qu'elle ne parle pas seulement de la porte."
        $ maison_minecraft_ajouts.append("porte_inutile_fermee_arc3")
    elif arc3_reaction_laplage == "demande_reponse":
        $ arc3_fin_minecraft = "destruction"
        systeme "Ilona reste devant la maison."
        $ renpy.pause(1.5, hard=True)
        systeme "Puis elle entre dans la cuisine d'été. Celle qu'elle avait construite après la plage."
        systeme "Elle regarde les blocs. Les murs. Le toit."
        $ renpy.pause(1.0, hard=True)
        systeme "Elle détruit le premier bloc."
        j "Qu'est-ce que tu fais ?"
        i "Je détruis."
        j "Pourquoi ?"
        i "Parce que j'en ai besoin."
        systeme "Elle détruit le deuxième. Le troisième. Tout le mur."
        j "Ilona—"
        i "Tais-toi."
        systeme "Jessy se tait. Il regarde Ilona effacer la cuisine qu'elle avait construite avec soin."
        systeme "Quand elle a fini, il ne reste qu'un trou dans la maison."
        $ renpy.pause(1.5, hard=True)
        i "Voilà."
        systeme "Elle se déconnecte."
        $ pression_stream += 2
        $ lien_jessy_ilona -= 1
        $ maison_minecraft_destructions.append("cuisine_ete_arc3")
        $ souvenirs["maison_respectee"] = False
    else:
        $ arc3_fin_minecraft = "lanterne_cour"
        $ lien_jessy_ilona += 1
        i "Je mets une lanterne devant la porte inutile."
        j "Pour qu'on la voie mieux ?"
        i "Pour qu'on arrête de faire semblant qu'elle n'existe pas."
        j "D'accord."
        systeme "La lanterne éclaire une sortie qui ne sort nulle part. Pour ce soir, c'est déjà une information."
        $ maison_minecraft_ajouts.append("lanterne_porte_inutile_arc3")

    if arc3_fin_minecraft == "destruction":
        systeme "La maison reste ouverte sur le trou qu'Ilona vient de laisser."
        systeme "Jessy ne touche à rien."
        systeme "Pour la première fois depuis longtemps, il comprend qu'une construction peut survivre à une explosion et quand même devenir inhabitable."
    else:
        menu:
            "Ilona retrouve dans son sac une petite étoile en sucre achetée au festival."

            "La laisser la manger pendant qu'elle réfléchit.":
                $ ilonanium_points += 1
                i "Elle a survécu à toute la journée."
                j "Elle mérite le repos éternel ?"
                i "Elle mérite d'être mangée."
                systeme "L'univers perd encore un fragment de prudence."

            "Proposer d'en garder une trace dans la salle secrète.":
                $ remember("maison_respectee")
                $ lien_jessy_ilona += 1
                j "On ne peut pas mettre la vraie étoile dans Minecraft."
                i "Oui, merci, je connais les frontières élémentaires de l'univers."
                j "Mais on peut en refaire une trace avec des blocs lumineux, dans la salle secrète."
                i "Comme preuve du festival ?"
                j "Comme preuve qu'une journée bizarre peut laisser autre chose qu'une rumeur."
                i "D'accord. La vraie reste sur mon bureau."

    systeme "La rentrée n'a rien tranché."
    systeme "Elle a seulement rendu les regards visibles."
    systeme "Et maintenant que tout le monde a vu quelque chose, il va devenir plus difficile de prétendre que rien ne change."

    jump arc_4_noel


# --- Recapitulatif Arc III ---
# Variables modifiees :
# - lien_jessy_ilona, confiance, communication, jalousie, autonomie_ilona
# - influence_theo, pression_stream, jugement_laplage, confidences_laplage
# - ilona_peut_finir_ses_phrases, interruptions_reconnues, interruptions_reparees
# - ilonanium_points
# - souvenirs["jessy_nomme_sa_peur"], souvenirs["jessy_repare"], souvenirs["theo_utilise_une_verite"], souvenirs["maison_respectee"]
# - arc3_reaction_rumeur, arc3_aide_stand, arc3_reaction_laplage, arc3_fin_minecraft
# - arc3_ilona_a_choisi_theme, arc3_rumeur_aggravee, arc3_theo_message_festival
#
# Choix ayant des consequences futures :
# - La reaction de Jessy a la rumeur colore la suite : dignite, blague nerveuse, silence ou attention reelle.
# - La maniere d'aider au stand fait monter ou retomber la jalousie avant le clash avec Theo.
# - La reponse a Theo determine si sa lucidite devient une emprise ou une blessure que Jessy regarde en face.
# - La scene avec Ilona prepare Noel : passion assumee, excuse adulte, effacement maladroit de Theo ou demande de garantie.
# - L'etoile en sucre reste un objet reel ; seule sa trace peut etre reconstruite dans Minecraft.
#
# Fils ouverts pour l'Arc IV :
# - Ilona sait qu'elle est troublee par l'attention de Theo, sans que cela efface ce qu'elle ressent pour Jessy.
# - Jessy et Theo se sont affrontes ; chacun a dit une part vraie et une part violente.
# - La maison Minecraft reflete l'etat du lien : panneau fragile, rangement prudent, porte fermee, destruction, sortie ou lanterne.
# - Noel devra tester si les personnages savent offrir quelque chose sans s'en servir comme preuve d'amour.
