# =============================================================================
# ARC V - EXAMENS, SAINT-VALENTIN ET WHITE DAY : CE QU'ON NE DIT PAS
# =============================================================================
# Thème central : Connaître les goûts de quelqu'un ne veut pas dire savoir ce qu'il veut.
# Question centrale : "Est-ce que tu as peur de me perdre… ou est-ce que tu ne me fais pas confiance ?"
# =============================================================================

# --- Variables locales Arc V ---
default arc5_sortie_annulee = ""          # Réaction à l'annulation
default arc5_theo_proposition = ""         # Comment Jessy gère Théo
default arc5_valentin_choix = ""          # Approche Saint-Valentin
default arc5_question_reponse = ""        # Réponse à LA question
default arc5_white_day_reponse = ""       # Approche White Day
default arc5_fin_minecraft = ""           # État final
default arc5_laplage_deuxieme_confidence = False
default arc5_allan_voit_theo = False
default arc5_allan_parti_cafe = False
default arc5_ilona_a_pleure = False       # Si Ilona craque
default arc5_jessy_a_menti = False        # Si Jessy ment sur sa peur
default arc5_tension_accumulee = 0        # Tension narrative
default arc5_theo_dans_maison = False     # Théo a accès à la maison Minecraft
default arc5_cinema_ensemble = False      # Ils sont allés au cinéma

# --- Images Arc V ---
image bg arc5 library = im.Scale("images/scenes/arc_5/bg_arc5_library.jpg", 1920, 1080)
image bg arc5 library night = im.Scale("images/scenes/arc_5/bg_arc5_library_night.jpg", 1920, 1080)
image bg arc5 cafe = im.Scale("images/scenes/arc_5/bg_arc5_cafe.jpg", 1920, 1080)
image bg arc5 rain street = im.Scale("images/scenes/arc_5/bg_arc5_rain_street.jpg", 1920, 1080)
image bg arc5 classroom = im.Scale("images/scenes/arc_5/bg_arc5_classroom.jpg", 1920, 1080)
image bg arc5 rooftop = im.Scale("images/scenes/arc_5/bg_arc5_rooftop.jpg", 1920, 1080)
image bg arc5 cinema = im.Scale("images/scenes/arc_5/bg_arc5_cinema.jpg", 1920, 1080)
image bg arc5 park spring = im.Scale("images/scenes/arc_5/bg_arc5_park_spring.jpg", 1920, 1080)
image bg arc5 minecraft night = im.Scale("images/scenes/arc_2/bg_arc2_minecraft_house_summer_night.jpg", 1920, 1080)
image bg arc5 train station = im.Scale("images/scenes/arc_5/bg_arc5_train_station.jpg", 1920, 1080)

# --- Personnage temporaire Arc V : Micka ---
define mi = Character("Micka", color="#e91e63", callback=speaker_callback("micka"))

image micka happy = speaker_sprite("micka", "images/personnages/micka/happy.png", 842, 1264)
image micka gifts = speaker_sprite("micka", "images/personnages/micka/happy_with_gifts.png", 842, 1264)

# =============================================================================
# SCENE 1 : REVISIONS EN BIBLIOTHEQUE - LA FATIGUE QUI S'ACCUMULE
# =============================================================================

label arc_5_examens:

    scene bg arc5 library
    with fade

    systeme "Arc V : Janvier mange les gens de l'intérieur."
    systeme "La bibliothèque empeste le café froid et la sueur d'angoisse. Dehors, la neige garde une lumière pâle. Dedans, les néons transforment tout le monde en brouillon de lui-même."

    show jessy neutral at char_left
    show ilona fatigue at char_midleft
    show allan neutral at char_center
    show alex serious at char_midright
    with dissolve

    systeme "Ilona n'a pas dormi. Ça se voit à la façon dont ses yeux ne se posent sur rien. Elle feuillette les mêmes pages depuis une heure sans les lire."
    
    x "Si quelqu'un m'explique encore la différence entre corrélation et causalité, je bouffe mes notes et je fais passer ça pour un accident."
    a "La corrélation, c'est quand tu révises et que tu réussis. La causalité, c'est quand tu révises et que tu réussis à cause des révisions."
    x "..."
    a "C'était clair ?"
    x "C'était techniquement correct et émotionnellement insupportable."
    
    systeme "Alexandre sort un schéma de son sac. On dirait un plan d'architecte pour une structure impossible."
    
    x "C'est quoi ça ?"
    a "Mon planning de révisions. J'ai organisé ça comme un bâtiment."
    x "Un bâtiment qui tient pas debout."
    a "Techniquement inhabitable. Donc parfait."
    
    systeme "Jessy reconnaît la logique. C'est la même qu'Alexandre applique à tout : si ça ne fait pas sens, c'est que ça a un sens supérieur."

    systeme "Jessy regarde Ilona. Elle a maigri. Pas beaucoup. Juste assez pour que ses pulls flottent un peu plus qu'avant."
    
    if arc4_fin_minecraft == "miniature_trace":
        systeme "Depuis Noël, elle sourit plus souvent. Mais ses sourires ont quelque chose de fatigué. Comme si elle les portait au lieu de les avoir."
    elif arc4_fin_minecraft == "echarpe_coffre":
        systeme "L'écharpe de Noël est rangée quelque part chez Ilona. Elle ne l'a jamais portée. Jessy n'a jamais demandé pourquoi."
        systeme "Il a peur de la réponse. C'est plus facile de ne pas savoir."
    elif arc4_fin_minecraft == "carnet_hors_maison":
        systeme "Depuis Noël, Ilona construit dehors dans Minecraft. Jamais dans la maison. Toujours à côté."
        systeme "Elle dit que c'est pour avoir de l'espace. Jessy entend qu'elle a besoin de distance."
    else:
        systeme "La neige a fondu sur le toit de la maison Minecraft. Le temps passe. Certaines choses ne se réparent pas en attendant."

    if arc4_ilona_avec_theo:
        if arc4_5_ilona_reaction == "accepte":
            systeme "Depuis la marche après Noël, Théo est devenu plus présent. Pas brutalement. Juste assez pour que son aide fasse partie du décor."
            if arc4_5_theo_proposition == "gestion_stream":
                $ pression_stream += 1
                systeme "Ilona a aussi parlé de stream. Pas comme une blague lancée entre deux messages. Comme quelque chose qu'elle pourrait construire pour de vrai."
        elif arc4_5_ilona_reaction == "prudente":
            systeme "Depuis la marche après Noël, Ilona garde une distance prudente avec Théo. Elle accepte parfois l'aide. Jamais le volant."
        elif arc4_5_ilona_reaction == "directe":
            systeme "Depuis la marche après Noël, quelque chose a changé dans la façon dont Ilona regarde Théo. Elle l'écoute encore. Mais elle l'interroge aussi."

    j "Tu veux faire une pause ?"
    
    systeme "Ilona lève les yeux. Il y a quelque chose de vitreux dedans. Quelque chose qui fait mal à regarder."
    
    i "Non."
    
    systeme "Pas 'ça va'. Juste 'non'. Comme si elle n'avait plus l'énergie de mentir."
    
    a "Pour info, quand quelqu'un dit 'non' avec cette tête-là, ça veut dire 'oui mais je refuse de l'admettre'."
    
    show ilona frustrated at char_midleft
    
    i "Allan, je t'aime bien, mais si tu continues à me psychanalyser, je te noie dans ton café."
    a "Message reçu."
    
    systeme "Elle replonge dans ses notes. Ses mains tremblent légèrement. Jessy ne sait pas si c'est la caféine ou autre chose."

    show theo neutral at char_right
    with dissolve

    systeme "Théo arrive. Quatre gobelets dans les mains. Il se déplace avec cette assurance tranquille qui donne envie de lui faire confiance ou de le détester, selon les jours."
    
    t "Café pour les condamnés. Thé pour Ilona."
    
    systeme "Il pose le gobelet devant elle. C'est le bon thé. Celui qu'elle prend quand elle est à bout mais qu'elle refuse de le montrer."
    systeme "Jessy le sait parce qu'il l'a remarqué il y a trois mois. Théo le sait parce qu'il remarque tout."

    if arc4_ilona_avec_theo:
        if arc4_5_ilona_reaction == "accepte":
            systeme "Depuis l'autre soir, il n'a même plus besoin de demander. Ilona avait choisi du thé au maid café. Théo l'a rangé dans sa mémoire comme une information utile."
        elif arc4_5_ilona_reaction == "prudente":
            systeme "Ilona regarde l'étiquette avant de le prendre. Un détail minuscule. Mais c'est elle qui vérifie, pas quelqu'un à sa place."
        elif arc4_5_ilona_reaction == "directe":
            systeme "Théo hésite une demi-seconde avant de poser le gobelet. Depuis Noël, il fait attention à ne pas avoir l'air d'avoir déjà décidé pour elle."
    
    show ilona neutral at char_midleft
    
    i "Merci."
    
    systeme "Elle boit une gorgée. Ferme les yeux une seconde. Quand elle les rouvre, quelque chose s'est détendu dans ses épaules."
    systeme "Théo a fait ça. En trente secondes. Avec un thé."
    systeme "Jessy sent quelque chose de froid dans sa poitrine. Pas de la jalousie. Quelque chose de pire : l'impression d'être inutile."

    menu:
        systeme "Le gobelet de thé est là, entre les mains d'Ilona. Théo attend, détendu, comme quelqu'un qui sait qu'il a fait la bonne chose."
        
        "Ne rien dire. Avaler la pilule.":
            $ confiance += 1
            $ jalousie += 2
            $ arc5_tension_accumulee += 1
            systeme "Jessy prend son café. Le goût est amer. Pas seulement à cause du café."
            systeme "Il pourrait dire quelque chose. Remercier Théo. Faire une blague. N'importe quoi."
            systeme "Mais les mots restent coincés. Parce que dire quelque chose maintenant, ce serait admettre que le geste de Théo l'a touché."
            systeme "Alors il se tait. Et le silence dit tout ce qu'il ne dit pas."
            show ilona neutral at char_midleft
            systeme "Ilona le regarde par-dessus son gobelet. Elle a vu. Elle voit toujours."

        "Remercier Théo sincèrement.":
            $ confiance += 2
            $ jalousie -= 1
            $ lien_jessy_ilona += 1
            j "Merci pour le café, Théo."
            systeme "Les mots sortent. Ils sont vrais. C'est peut-être pour ça qu'ils font un peu mal."
            show theo neutral at char_right
            t "De rien."
            systeme "Théo hoche la tête. Pas de triomphe dans ses yeux. Juste de la normalité."
            systeme "Et c'est presque pire. Parce que ça veut dire qu'il ne joue même pas. Il est juste... comme ça."
            show ilona smile at char_midleft
            systeme "Ilona sourit. Un vrai sourire. Le premier depuis des jours."
            systeme "Il n'est pas pour Jessy. Mais il existe. C'est quelque chose."

        "Demander à Ilona si elle voulait vraiment ce thé-là.":
            $ jalousie += 3
            $ confiance -= 2
            $ autonomie_ilona -= 1
            $ arc5_tension_accumulee += 2
            j "C'était celui que tu voulais ?"
            systeme "La question sort avant qu'il puisse la retenir."
            show ilona frustrated at char_midleft
            systeme "Ilona pose son gobelet. Lentement. Le geste dit tout."
            i "Jessy."
            j "Quoi ? Je demande juste."
            i "Tu ne demandes pas. Tu vérifies."
            systeme "Le mot 'vérifies' claque comme une gifle."
            i "Oui, c'était celui que je voulais. Et non, tu n'as pas besoin de t'assurer que Théo n'a pas mieux deviné que toi."
            systeme "Allan tousse. Alexandre devient très intéressé par ses notes."
            systeme "Théo ne dit rien. Son silence est pire qu'une réponse."
            $ interruptions_ilona += 1

        "Proposer d'aller chercher autre chose, quelque chose de personnel.":
            $ jalousie += 2
            $ pression_stream += 1
            $ confiance -= 1
            j "Tu veux autre chose ? Je peux aller chercher ce truc que tu aimes, là, avec la..."
            show ilona frustrated at char_midleft
            i "Jessy. J'ai déjà un thé."
            j "Je sais, mais..."
            i "Mais quoi ?"
            systeme "Elle le regarde. Il n'y a pas de colère dans ses yeux. Il y a quelque chose de pire : de la lassitude."
            i "Le thé est là. Théo l'a apporté. C'est fait. Tu n'as pas besoin de... compenser."
            systeme "Le mot 'compenser' reste suspendu dans l'air."
            j "Je ne..."
            i "Si. C'est exactement ce que tu fais."
            systeme "Elle boit son thé. La conversation est terminée."

    hide theo
    with dissolve

    systeme "Théo s'installe à une table voisine. Ni trop près ni trop loin. La distance parfaite pour être disponible sans envahir."
    systeme "Jessy se demande si c'est calculé ou naturel. Les deux réponses lui font peur."

    show laplage neutral at char_right
    with dissolve

    systeme "Monsieur Laplage traverse la bibliothèque. Il porte un badge qui dit 'Consultant en Entropie Émotionnelle' et trois livres dont les titres sont illisibles."
    
    laplage "La concentration a une odeur. Aujourd'hui, elle sent le désespoir."
    a "Vous travaillez ici maintenant ?"
    laplage "Je travaille là où les gens oublient de respirer."
    
    systeme "Il regarde Ilona. Longuement. Comme s'il lisait quelque chose écrit sur son front."
    
    laplage "Les étoiles qui ne se reposent jamais finissent par s'effondrer sur elles-mêmes."
    
    show ilona embarrassed at char_midleft
    
    i "C'est censé me motiver ?"
    laplage "Non. C'est censé te faire peur."
    
    show laplage thumb_up at char_right
    systeme "Il lève le pouce. Puis il disparaît dans les rayons, entre les sciences humaines et les romans d'horreur."

    hide laplage
    with dissolve

    x "Un jour, quelqu'un devra m'expliquer comment il fait pour apparaître et disparaître comme ça."
    a "J'ai arrêté de chercher. La réponse me ferait probablement remettre en question ma conception de la réalité."
    
    systeme "Ilona range ses affaires. Ses gestes sont lents. Mécaniques."
    
    i "Je rentre."
    j "Tu veux qu'on..."
    i "Non."
    
    systeme "Pas de justification. Pas d'excuse. Juste 'non'."
    systeme "Elle part. Les autres regardent la porte se refermer."
    
    hide ilona
    with dissolve
    
    a "Elle dort combien ces derniers temps ?"
    j "Je ne sais pas."
    a "Tu ne lui as pas demandé ?"
    
    systeme "La question est simple. La réponse ne l'est pas."

    menu:
        systeme "Allan attend. Alexandre aussi. Même Théo, de sa table, semble écouter."
        
        "Admettre qu'il ne lui a pas demandé parce qu'il avait peur de la réponse.":
            $ communication += 2
            $ confiance += 1
            j "Non. Je n'ai pas demandé."
            a "Pourquoi ?"
            j "Parce que si elle me dit qu'elle va mal, je vais vouloir réparer."
            j "Et elle m'a dit à Noël qu'elle ne voulait pas être réparée."
            systeme "Le silence qui suit est lourd."
            show allan support at char_center
            a "Tu sais que 'demander comment ça va' et 'essayer de réparer' c'est pas la même chose ?"
            j "En théorie, oui."
            a "Et en pratique ?"
            j "En pratique, je ne sais pas faire la différence."
            systeme "C'est peut-être la chose la plus honnête qu'il ait dite depuis des semaines."

        "Dire qu'il lui fait confiance pour gérer.":
            $ confiance += 1
            $ arc5_jessy_a_menti = True
            j "Je lui fais confiance. Elle gère."
            show allan doubt at char_center
            a "Tu lui fais confiance ou tu évites le sujet ?"
            j "C'est quoi la différence ?"
            a "La première version, tu l'as décidée. La deuxième, c'est elle qui l'a subie."
            systeme "Jessy ne répond pas. La réponse est trop claire pour être dite à voix haute."

        "Changer de sujet. Parler des examens.":
            $ communication -= 1
            $ arc5_tension_accumulee += 1
            j "On devrait se remettre au travail. Les examens..."
            show allan silence at char_center
            a "Jessy."
            j "Quoi ?"
            a "Tu viens de faire exactement ce qu'elle fait."
            j "C'est-à-dire ?"
            a "Éviter en faisant semblant que tout va bien."
            systeme "Jessy ouvre la bouche pour répondre. Puis il la referme."
            systeme "Allan a raison. C'est pour ça que ça fait mal."

    hide allan
    hide alex
    hide jessy
    with dissolve

# =============================================================================
# SCENE 2 : SORTIE ANNULEE - CE QU'ON ENTEND DANS LE SILENCE
# =============================================================================

    scene black
    with fade
    
    systeme "Une semaine passe. Les révisions continuent. La fatigue s'accumule."
    
    scene bg arc5 rain street
    with fade

    systeme "La pluie transforme la ville en aquarium gris."

    show jessy neutral at char_center
    with dissolve

    systeme "Jessy attend sous l'auvent du cinéma. Ils avaient prévu ça depuis dix jours. Un film, puis manger quelque chose. Simple. Normal."
    
    # Si bonnes conditions, Ilona vient quand même
    if lien_jessy_ilona >= 8 and confiance >= 5 and communication >= 5:
        show ilona fatigue at char_right
        with dissolve
        
        systeme "Ilona arrive. Elle a des cernes. Son pas est lourd. Mais elle est là."
        
        i "Désolée du retard. J'ai failli annuler."
        j "Mais tu es venue."
        i "Oui."
        
        systeme "Pas d'explication. Juste sa présence."
        
        j "Tu veux vraiment qu'on reste ? On peut rentrer si tu préfères."
        
        show ilona smile at char_right
        
        i "Non. J'ai besoin de penser à autre chose pendant deux heures."
        j "Le film est censé être nul."
        i "Parfait. Je veux du nul. Du prévisible. Du reposant."
        
        scene black
        with Dissolve(1.0)
        
        systeme "Ils entrent dans le cinéma."
        
        $ renpy.pause(0.5, hard=True)
        
        scene bg arc5 cinema
        with Dissolve(1.5)
        
        show jessy neutral at char_left
        show ilona fatigue at char_right
        with dissolve
        
        systeme "La salle est presque vide. Cinq personnes, peut-être six. Les bandes-annonces ont déjà commencé."
        systeme "Ils trouvent deux places au milieu. Pas devant. Pas derrière. Juste là où on peut oublier qu'on regarde un écran."
        
        systeme "Ilona pose son sac. S'enfonce dans le siège. Ferme les yeux une seconde."
        
        show ilona neutral
        
        i "Merci."
        j "Pour quoi ?"
        i "D'avoir pas insisté. Pour savoir pourquoi je suis fatiguée."
        
        show jessy smile
        
        j "Tu me diras quand tu voudras. Ou pas."
        
        systeme "Elle tourne la tête vers lui. Un demi-sourire. Le premier depuis qu'elle est arrivée."
        
        show ilona smile
        
        i "Le film commence."
        j "Il est vraiment nul, on peut partir."
        i "Non. Je veux voir à quel point c'est nul."
        
        systeme "Le générique démarre. Les lumières s'éteignent complètement."
        
        scene black
        with Dissolve(2.0)
        
        systeme "Dans le noir, l'écran devient la seule source de lumière."
        systeme "Ilona respire plus lentement. Ses épaules se détendent."
        systeme "Jessy ne regarde pas vraiment le film. Il regarde les reflets sur le visage d'Ilona."
        systeme "À un moment, elle bouge sa main. Cherche l'accoudoir."
        systeme "Elle trouve celle de Jessy à la place."
        systeme "Ils ne se tiennent pas vraiment la main. Juste leurs doigts qui se touchent. Leurs paumes qui se frôlent."
        systeme "Pas besoin de serrer. Pas besoin de revendiquer."
        systeme "Juste se rappeler que l'autre est là."
        
        $ lien_jessy_ilona += 1
        $ confiance += 1
        $ arc5_cinema_ensemble = True
        
        hide jessy
        hide ilona
        with dissolve
        
        jump arc_5_scene_3
    
    systeme "Son téléphone vibre."

    systeme "{i}Message d'Ilona :{/i}"
    systeme "{i}\"Je suis désolée. Je peux pas ce soir. Je suis crevée.\"{/i}"

    systeme "Trois phrases. Vingt-sept caractères si on compte les espaces."
    systeme "Jessy les relit. Une fois. Deux fois. Comme si les relire allait changer ce qu'elles disent."

    systeme "La pluie tombe plus fort. Les gens courent vers les abris. Jessy reste là, son téléphone à la main."

    menu:
        systeme "Le curseur clignote. Le message attend une réponse."
        
        "\"D'accord. Repose-toi bien. Je suis là si tu as besoin.\"":
            $ arc5_sortie_annulee = "accepte"
            $ confiance += 2
            $ autonomie_ilona += 2
            $ remember("ilona_libre_sans_abandon")
            systeme "Les mots sont simples. Pas de reproche caché. Pas de question déguisée."
            systeme "Jessy appuie sur envoyer. L'écran redevient noir."
            systeme "Trois minutes passent. Puis :"
            systeme "{i}\"Merci. Vraiment.\"{/i}"
            systeme "Le 'vraiment' dit tout ce que le reste du message ne dit pas."
            systeme "Elle s'attendait à autre chose. Une question. Une insistance. Une déception mal cachée."
            systeme "Elle n'a eu que de l'espace."

        "\"Tu es sûre que ça va ? Tu annules beaucoup ces derniers temps.\"":
            $ arc5_sortie_annulee = "inquiet"
            $ jalousie += 1
            $ communication += 1
            $ arc5_tension_accumulee += 1
            systeme "La question part avant qu'il puisse la retenir. Elle est vraie. C'est peut-être pour ça qu'elle est dangereuse."
            systeme "La réponse met du temps à arriver."
            systeme "{i}\"Je suis fatiguée, Jessy. C'est tout.\"{/i}"
            systeme "Le point à la fin est une porte qui se ferme."
            systeme "Il pourrait insister. Demander ce que 'fatiguée' veut vraiment dire. Creuser."
            systeme "Mais creuser ressemble parfois à envahir."
            j "D'accord. Repose-toi."
            systeme "Il n'ajoute pas 'je suis là'. Ça sonnerait comme une demande maintenant."

        "\"C'est la troisième fois ce mois-ci. Je commence à me demander si c'est vraiment la fatigue.\"":
            $ arc5_sortie_annulee = "confronte"
            $ jalousie += 3
            $ confiance -= 2
            $ communication -= 1
            $ arc5_tension_accumulee += 3
            $ pression_stream += 1
            systeme "Les mots sortent. Ils sont vrais. Ils sont aussi injustes."
            systeme "Parce que oui, c'est la troisième fois. Mais compter, c'est déjà accuser."
            systeme "La réponse arrive vite. Trop vite."
            systeme "{i}\"Tu tiens un tableau de mes annulations maintenant ?\"{/i}"
            systeme "Puis, immédiatement après :"
            systeme "{i}\"Je suis fatiguée. Vraiment. Et là, tu me fatigues encore plus.\"{/i}"
            systeme "Jessy fixe l'écran. Il a voulu dire quelque chose d'honnête. Il a dit quelque chose de blessant."
            systeme "La différence entre les deux n'est pas dans l'intention. Elle est dans l'impact."

        "Ne pas répondre tout de suite. Attendre. Réfléchir.":
            $ arc5_sortie_annulee = "silence"
            $ arc5_tension_accumulee += 2
            systeme "Jessy fixe l'écran. Les mots se forment dans sa tête, puis se défont."
            systeme "Répondre vite, c'est risquer de dire quelque chose de stupide."
            systeme "Répondre tard, c'est la laisser avec son message sans retour."
            systeme "Il attend cinq minutes. Puis dix."
            systeme "Son téléphone vibre à nouveau."
            systeme "{i}\"T'es fâché ?\"{/i}"
            systeme "Elle a interprété son silence comme une réponse. Et peut-être qu'elle a raison."
            j "Non. Je réfléchissais."
            systeme "{i}\"À quoi ?\"{/i}"
            j "À ce que je voulais vraiment dire."
            systeme "Trois points. Elle tape quelque chose. S'arrête. Recommence."
            systeme "{i}\"Et tu veux dire quoi ?\"{/i}"
            systeme "La question est une porte ouverte. Jessy ne sait pas s'il doit y entrer."

    if arc5_sortie_annulee == "silence":
        menu:
            systeme "Elle attend. La pluie continue."
            
            "\"Que je comprends. Et que ça me fait chier quand même.\"":
                $ communication += 2
                $ confiance += 1
                $ lien_jessy_ilona += 1
                systeme "Honnêteté. Pas polie. Pas agressive. Juste vraie."
                systeme "{i}\"...\"{/i}"
                systeme "{i}\"C'est con, mais ça me soulage.\"{/i}"
                systeme "Puis :"
                systeme "{i}\"Ça me fait chier aussi. Mais je peux vraiment pas.\"{/i}"
                j "Je sais."
                systeme "{i}\"Tu m'en veux ?\"{/i}"
                j "Un peu. Mais je préfère ça à faire semblant."
                systeme "Le message suivant met du temps à arriver."
                systeme "{i}\"Moi aussi.\"{/i}"
                $ arc5_sortie_annulee = "honnetete"
            
            "\"Rien de spécial. Repose-toi bien.\"":
                $ communication -= 1
                $ confiance -= 1
                systeme "Mensonge. Petit. Mais mensonge quand même."
                systeme "{i}\"Ok.\"{/i}"
                systeme "Un seul mot. Sec. Elle a compris qu'il n'a pas dit la vérité."
                systeme "Mais elle est trop fatiguée pour creuser. Ou peut-être qu'elle s'en fiche."
                systeme "Les deux options font mal."

    hide jessy
    with dissolve

    scene bg arc5 cafe
    with fade

    systeme "Jessy entre dans le premier café qu'il trouve. Il a besoin de s'asseoir quelque part où il ne pleut pas sur ses pensées."
    
    systeme "En s'installant, il remarque quelque chose sous la chaise voisine. Un stylo. Violet. Avec des étoiles dessus."
    systeme "C'est celui d'Ilona. Elle le cherchait depuis deux semaines."
    
    if arc2_photo_reaction == "reste_bord":
        systeme "Jessy repense à la plage. Au porte-clés qu'elle avait perdu. C'était Théo qui l'avait retrouvé."
        systeme "Cette fois, c'est lui. C'est stupide, mais ça compte."
    
    systeme "Il range le stylo dans sa poche. Il le lui rendra. Sans en faire un événement."

    show jessy neutral at char_left
    show allan neutral at char_right
    with dissolve

    systeme "Allan est là. Parce qu'Allan est toujours quelque part quand les choses vont mal. C'est un talent ou une malédiction, selon les jours."
    
    a "Laisse-moi deviner. Elle a annulé."
    j "Comment tu..."
    a "Tu as la tête de quelqu'un qui vient de recevoir un message de trois mots avec un point à la fin."
    j "C'était vingt-sept caractères."
    a "Tu as compté ?"
    j "Apparemment, oui."

    systeme "Allan ferme son livre. C'est un traité sur les étoiles naines. Ou peut-être sur les relations toxiques. La couverture ne précise pas."
    
    a "Tu lui as répondu quoi ?"

    if arc5_sortie_annulee == "accepte":
        j "Que c'était d'accord. Qu'elle pouvait se reposer."
        show allan support at char_right
        a "C'est tout ?"
        j "C'est tout."
        a "Pas de 'mais tu vas bien ?' Pas de 'on peut se voir demain quand même ?' Pas de 'je passe déposer un truc' ?"
        j "Non."
        systeme "Allan hoche la tête lentement."
        a "Progrès."
        j "Progrès ?"
        a "Tu apprends à laisser les gens tranquilles quand ils en ont besoin."
        j "C'est censé être un compliment ?"
        a "C'est censé être une observation. Fais-en ce que tu veux."
    elif arc5_sortie_annulee == "honnetete":
        j "Que je comprenais. Et que ça me faisait chier quand même."
        show allan surprise at char_right
        a "Tu as dit ça ?"
        j "Oui."
        a "Et elle ?"
        j "Elle a dit que ça la soulageait."
        systeme "Allan reste silencieux un moment."
        a "C'est... inattendu."
        j "De sa part ou de la mienne ?"
        a "Des deux."
    elif arc5_sortie_annulee == "confronte":
        j "Que c'était la troisième fois ce mois-ci."
        show allan silence at char_right
        a "..."
        j "Quoi ?"
        a "Rien."
        j "Allan."
        a "Tu veux que je te dise quoi ? Que c'était bien ? Que tu avais raison de compter ?"
        j "Je n'ai pas compté, j'ai juste..."
        a "Tu as juste remarqué. C'est pareil."
        systeme "Jessy se tait."
        a "Écoute. Peut-être qu'elle annule parce qu'elle va mal. Ou peut-être qu'elle annule parce qu'elle a besoin d'espace. Les deux existent."
        j "Et la différence ?"
        a "La différence, c'est que dans un cas tu dois t'inquiéter, et dans l'autre tu dois la laisser tranquille."
        j "Et comment je sais ?"
        a "Tu lui demandes. Mais pas comme tu viens de le faire."
    else:
        j "Rien de spécial."
        show allan doubt at char_right
        a "Tu mens."
        j "Non, je..."
        a "Jessy. Je te connais depuis suffisamment longtemps pour savoir quand tu dis 'rien de spécial' alors que tout est très spécial."
        systeme "Jessy regarde son café. Il est froid. Il ne l'a pas touché."
        j "Je ne savais pas quoi dire."
        a "Alors tu n'as rien dit."
        j "C'est mal ?"
        a "C'est pas bien ou mal. C'est juste... pas une réponse."

    show theo neutral at char_center
    with dissolve

    systeme "Théo entre. Parce que l'univers a un sens de l'humour cruel."
    
    t "Jessy. Allan."
    systeme "Il s'assoit sans demander. Comme quelqu'un qui sait qu'il a sa place partout."
    
    a "On a vu Laplage à la biblio tout à l'heure."
    t "Le Messi ?"
    a "Tu l'appelles encore comme ça ?"
    t "Le GOAT des conseils cryptiques. Ça lui va bien."
    a "Il t'a encore sorti une phrase incompréhensible ?"
    t "Pas aujourd'hui. Il surveillait les gens qui oubliaient de respirer."
    
    systeme "Théo change de sujet."
    
    t "Ilona t'a envoyé un message aussi ?"
    
    systeme "Le 'aussi' reste suspendu dans l'air."
    
    j "Elle t'a contacté ?"
    t "Elle m'a demandé si je pouvais lui apporter ses notes de cours. Elle a raté deux jours cette semaine."
    
    systeme "Deux jours. Jessy ne le savait pas. Il aurait dû le savoir."

    if arc4_ilona_avec_theo:
        if arc4_5_ilona_reaction == "accepte":
            systeme "Après la marche de Noël, la phrase semble presque logique. Ilona demande à Théo parce que Théo est déjà là, dans les interstices."
        elif arc4_5_ilona_reaction == "prudente":
            systeme "Jessy remarque le détail malgré la morsure : elle a demandé des notes, pas une présence. Même fatiguée, Ilona a choisi la taille exacte de l'aide."
        elif arc4_5_ilona_reaction == "directe":
            systeme "Théo dit ça calmement. Mais Jessy croit voir la même prudence que depuis Noël, comme si une question d'Ilona continuait de lui tenir la manche."
    
    show theo reassuring at char_center
    
    t "Je vais passer chez elle tout à l'heure."
    
    systeme "La phrase est neutre. Informationnelle. Mais quelque chose dedans griffe."

    menu:
        systeme "Théo attend. Allan observe. Le café est presque vide à cette heure."
        
        "\"Elle t'a demandé à toi ?\"":
            $ jalousie += 2
            $ arc5_tension_accumulee += 1
            j "Elle t'a demandé à toi ?"
            systeme "La question sort. Elle sonne plus accusatoire que prévu."
            show theo innocent at char_center
            t "Oui. J'ai les notes les plus complètes du groupe."
            systeme "C'est vrai. Et c'est peut-être pour ça que ça fait mal."
            j "Je pourrais lui apporter."
            t "Elle m'a demandé à moi."
            systeme "Pas de triomphe dans sa voix. Juste un fait."
            show allan silence at char_right
            a "Jessy."
            j "Quoi ?"
            a "Elle vient de t'envoyer un message pour dire qu'elle était fatiguée. Si tu débarques avec les notes, tu penses que ça dit quoi ?"
            systeme "Jessy ne répond pas. La réponse est trop claire."

        "\"Tant mieux qu'elle ait quelqu'un pour l'aider.\"":
            $ confiance += 2
            $ jalousie += 1
            j "Tant mieux qu'elle ait quelqu'un pour l'aider."
            systeme "Les mots sortent. Ils sont vrais. Ils font quand même mal à dire."
            show theo neutral at char_center
            t "Je lui dépose les notes. Je ne reste pas."
            j "Je sais."
            systeme "Il ne sait pas. Mais il fait confiance. Ou il essaie."
            show allan support at char_right
            a "On devrait faire des t-shirts 'Progrès émotionnel en cours'."
            j "Ferme-la, Allan."
            a "Avec amour."

        "Rester silencieux. Observer Théo.":
            $ jalousie += 1
            systeme "Jessy ne dit rien. Il regarde Théo. Théo le regarde aussi."
            systeme "Quelque chose passe entre eux. Pas de l'hostilité. Pas de la complicité non plus. Quelque chose de plus compliqué."
            t "Tu veux que je lui dise quelque chose de ta part ?"
            j "Non."
            t "Tu es sûr ?"
            j "Oui."
            systeme "Le 'oui' est sec. Peut-être trop."
            t "D'accord."
            systeme "Théo n'insiste pas. C'est peut-être le pire."

        "\"Tu passes beaucoup de temps avec elle ces derniers temps.\"":
            $ jalousie += 3
            $ influence_theo += 1
            $ arc5_tension_accumulee += 2
            $ arc5_allan_parti_cafe = True
            j "Tu passes beaucoup de temps avec elle ces derniers temps."
            systeme "Ce n'est pas une question. C'est une accusation déguisée."
            show theo defensive at char_center
            t "Elle a besoin d'aide. Je l'aide."
            j "Et c'est tout ?"
            t "Qu'est-ce que tu veux que ça soit d'autre ?"
            show allan silence at char_right
            systeme "Allan se lève."
            a "Je vais chercher un autre café. Prenez votre temps pour... ça."
            hide allan
            with dissolve
            systeme "Il s'éloigne. Lâche."
            t "Jessy. Je ne suis pas ton ennemi."
            j "Je n'ai pas dit ça."
            t "Tu n'as pas besoin de le dire. Ça se voit."
            systeme "Le silence qui suit est lourd comme du plomb."

    if arc5_sortie_annulee == "confronte" or jalousie >= 5:
        show theo reassuring at char_center
        t "Je peux te poser une question ?"
        j "Vas-y."
        t "Est-ce que tu lui fais confiance ?"
        systeme "La question est simple. La réponse ne l'est pas."
        j "Bien sûr que oui."
        t "Alors pourquoi tu réagis comme ça quand quelqu'un d'autre l'aide ?"
        systeme "Jessy ouvre la bouche. La referme."
        t "Ce n'est pas un reproche. C'est une vraie question."
        
        if arc2_choix_activite_theo == "suivre":
            systeme "Jessy repense à la plage. À cet été où il avait suivi Ilona quand elle s'était éloignée avec Théo."
            systeme "Il avait eu tort. Il le savait. Et pourtant, quelque chose en lui n'avait pas changé."
            t "Tu l'as déjà fait, non ? La suivre. Vérifier."
            systeme "Théo se souvient aussi."
            j "C'était différent."
            t "C'était pareil. Et tu le sais."
        
        systeme "Théo se lève."
        t "Je vais lui apporter ses notes. Si tu veux lui envoyer un message après, fais-le."
        t "Mais peut-être... pas ce soir."
        systeme "Il part. La phrase reste."
        $ arc5_allan_voit_theo = True

    hide theo
    with dissolve

    if (arc5_allan_voit_theo or influence_theo >= 4) and not arc5_allan_parti_cafe:
        show allan doubt at char_right
        a "Je peux te dire un truc ?"
        j "Depuis quand tu demandes la permission ?"
        a "Depuis que c'est sur Théo."
        systeme "Jessy se tourne vers lui."
        a "Je le connais depuis longtemps. Depuis le collège."
        j "Je sais."
        a "Il est vraiment utile. Vraiment attentif. Il voit des trucs que les autres ne voient pas."
        j "Mais ?"
        show allan doubt at char_right
        a "Mais parfois, je me demande s'il supporte que les gens fassent autrement que ce qu'il avait prévu."
        j "C'est-à-dire ?"
        a "C'est-à-dire que quand quelqu'un refuse son aide, il ne s'énerve pas. Il ne part pas. Il trouve un autre angle."
        systeme "Jessy réfléchit."
        j "Et c'est mal ?"
        a "C'est pas mal. C'est... je sais pas. C'est comme quelqu'un qui ne perd jamais."
        a "Parfois, on devrait perdre. On devrait accepter que la réponse soit non."
        systeme "Le silence s'installe."
        a "Je ne dis pas qu'il est méchant. Je dis que je ne sais pas toujours ce qu'il veut vraiment."

    hide allan
    hide jessy
    with dissolve

# =============================================================================
# SCENE 3 : THEO PROPOSE DE "GERER" - LE PIÈGE DOUX
# =============================================================================

label arc_5_scene_3:

    scene black
    with fade
    
    systeme "Les semaines passent. Janvier devient février. Les examens s'achèvent enfin."
    
    scene bg arc5 library night
    with fade

    systeme "Les résultats sont tombés. Certains ont réussi. D'autres ont survécu. Tout le monde est épuisé."

    show jessy neutral at char_left
    show theo neutral at char_right
    with dissolve

    systeme "Théo attrape Jessy à la sortie de la bibliothèque. Le timing est trop précis pour être accidentel."
    
    t "Tu as cinq minutes ?"
    j "Ça dépend pour quoi."
    t "Pour Ilona."
    
    systeme "Jessy s'arrête."
    
    j "Qu'est-ce qu'il y a ?"
    t "Rien de grave. Mais je pense qu'on devrait parler."

    systeme "Ils s'installent près des casiers, à l'écart des autres. La lumière des néons projette des ombres froides."

    t "Elle est épuisée. Tu le sais."
    j "Oui."
    t "Et elle ne demande pas d'aide. Elle ne sait pas comment."
    j "Où tu veux en venir ?"
    
    show theo reassuring at char_right
    
    t "Je peux prendre certaines choses en charge pour elle."
    t "Les notes de cours, les messages du club, les gens qui la sollicitent pour le festival de printemps."
    if arc4_5_theo_proposition == "gestion_stream":
        t "Et son stream, si elle veut s'y mettre sérieusement. Les horaires, le chat, les messages qui fatiguent."
        systeme "Jessy sent la phrase arriver trop tard. Comme si une partie de la conversation avait commencé sans lui depuis Noël."
    j "Et tu me dis ça à moi parce que... ?"
    
    systeme "Théo le regarde. Ses yeux sont calmes. Trop calmes."
    
    t "Parce que si c'est toi qui lui proposes, elle acceptera."
    t "Venant de moi, elle pourrait se sentir... infantilisée."
    t "Venant de toi, c'est différent."
    
    systeme "La logique est parfaite. C'est peut-être pour ça qu'elle sonne faux."

    if arc4_ilona_avec_theo:
        if arc4_5_ilona_reaction == "prudente":
            systeme "Jessy repense à ce qu'Allan lui a dit : Ilona accepte parfois l'aide, mais elle garde la main sur la porte."
        elif arc4_5_ilona_reaction == "directe":
            systeme "Jessy repense à la question qu'Ilona a posée à Théo : aider quelqu'un, ou devenir celui qui aide ?"
    
    j "Tu veux que je lui propose quelque chose que tu ferais à ma place ?"
    t "Je veux qu'elle accepte de l'aide. Le reste, c'est de la logistique."
    if arc4_5_theo_proposition == "gestion_stream":
        systeme "Le mot 'logistique' englobe soudain les cours, les messages, et peut-être même le rêve qu'Ilona n'a pas encore osé appeler un projet."

    menu:
        systeme "Théo attend. Sa proposition est raisonnable. Peut-être trop."
        
        "Refuser net. Ce n'est pas à eux de décider pour elle.":
            $ arc5_theo_proposition = "refuse"
            $ autonomie_ilona += 3
            $ influence_theo -= 2
            $ confiance += 1
            $ jugement_laplage += 1
            j "Non."
            show theo disappointed at char_right
            t "Non ?"
            j "Ce n'est pas à moi de décider ce qu'elle peut porter. Et ce n'est pas à toi non plus."
            t "Je n'essaie pas de décider. J'essaie d'aider."
            j "Alors propose-lui directement. Sans passer par moi. Sans stratégie."
            systeme "Le mot 'stratégie' fait mouche. Théo cille."
            t "Ce n'est pas une stratégie."
            j "Alors c'est quoi ?"
            systeme "Silence."
            t "C'est... de l'efficacité."
            j "C'est la même chose avec un meilleur emballage."
            if arc4_5_ilona_reaction == "directe":
                j "Et je crois qu'Ilona t'a déjà posé une version de cette question."
                systeme "Théo ne répond pas. Cette fois, son silence n'a rien de rassurant."
            systeme "Théo se lève."
            t "Tu te trompes sur moi, Jessy."
            j "Peut-être. Mais je préfère me tromper que décider à sa place."

        "Accepter partiellement. Certaines choses peuvent être gérées.":
            $ arc5_theo_proposition = "partiel"
            $ autonomie_ilona -= 1
            $ influence_theo += 2
            $ confiance -= 1
            j "Les notes, peut-être. Le reste, non."
            show theo reassuring at char_right
            t "Les notes, c'est déjà bien."
            j "Mais on lui demande avant. Ensemble."
            t "Bien sûr."
            systeme "Le 'bien sûr' est trop rapide. Trop lisse."
            systeme "Jessy se demande s'il vient de céder quelque chose d'important."
            if arc4_5_theo_proposition == "gestion_stream":
                $ pression_stream += 1
                systeme "Et il se demande si 'les notes' ne sont pas seulement le premier étage d'une aide plus grande, plus douce, plus difficile à refuser."
            j "Et Théo ?"
            t "Oui ?"
            j "Si elle dit non, c'est non. Pas 'non pour l'instant'. Non."
            systeme "Théo hoche la tête. Mais quelque chose dans ses yeux dit qu'il entend autre chose."

        "Demander pourquoi il ne propose pas à Ilona directement.":
            $ arc5_theo_proposition = "questionne"
            $ communication += 2
            $ influence_theo -= 1
            j "Pourquoi tu ne lui proposes pas directement ?"
            show theo innocent at char_right
            t "Je te l'ai dit. Venant de moi..."
            j "Non. La vraie raison."
            systeme "Théo se tait."
            if arc4_5_ilona_reaction == "directe":
                j "Est-ce que tu veux l'aider, ou est-ce que tu veux être celui qui l'aide ?"
                systeme "La phrase ne vient pas de Jessy. Pas vraiment. Elle vient d'Ilona, et Théo le reconnaît."
            j "Si tu voulais juste l'aider, tu aurais proposé. Tu n'aurais pas fait un détour par moi."
            t "Tu crois que j'ai une arrière-pensée ?"
            j "Je crois que tu calcules tout. Même l'aide."
            systeme "Le silence entre eux devient électrique."
            t "Ce n'est pas calculer. C'est optimiser."
            j "C'est la même chose."
            t "Non. Calculer, c'est pour soi. Optimiser, c'est pour le résultat."
            j "Et le résultat, c'est quoi pour toi ?"
            systeme "Théo ne répond pas tout de suite."
            t "Qu'elle aille mieux."
            j "C'est tout ?"
            t "C'est tout."
            systeme "Jessy ne le croit pas. Mais il ne peut pas prouver le contraire."

        "Accepter. Laisser Théo gérer.":
            $ arc5_theo_proposition = "laisse"
            $ influence_theo += 3
            $ autonomie_ilona -= 2
            $ confiance -= 2
            $ pression_stream += 1
            $ arc5_theo_dans_maison = True
            j "Fais ce que tu veux."
            show theo neutral at char_right
            t "Tu es sûr ?"
            j "Si ça peut l'aider."
            systeme "Jessy sait que ce n'est pas la bonne réponse. Mais il est fatigué aussi."
            systeme "Fatigué de surveiller. De s'inquiéter. De mesurer chaque geste de Théo."
            t "D'accord. Je gère."
            if arc4_5_theo_proposition == "gestion_stream":
                $ pression_stream += 1
                t "Pour les cours. Pour le stream aussi, si elle veut continuer à en parler."
                systeme "Jessy hoche la tête trop tard. Le projet d'Ilona vient de changer de mains sans qu'elle soit dans la pièce."
            systeme "Le 'je gère' reste dans l'air comme une promesse ou une menace."
            systeme "Jessy ne sait pas encore laquelle."

    hide theo
    hide jessy
    with dissolve

# =============================================================================
# SCENE 4 : SAINT-VALENTIN - L'AMOUR ET SES PIÈGES
# =============================================================================

    scene bg arc5 classroom
    with fade

    systeme "14 février. La classe empeste le chocolat, le parfum bon marché et les rêves adolescents."

    show jessy neutral at char_left
    show alex teasing at char_right
    with dissolve

    x "Alors ? Tu as préparé quoi ?"
    j "Pour ?"
    x "Pour la fête des gens qui s'aiment en public."
    j "Je ne sais pas si c'est le bon moment."
    
    show alex serious at char_right
    
    x "Pourquoi ?"
    j "Elle est épuisée. Je ne veux pas ajouter de pression."
    x "Et ne rien faire, ça dit quoi ?"
    j "Que je respecte son espace ?"
    x "Ou que tu as peur."
    
    systeme "La phrase fait mouche."
    
    j "C'est pas pareil."
    x "C'est exactement pareil, Jessy. Tu appelles ça du respect, mais en vrai, t'as juste peur de te planter."

    if arc5_sortie_annulee == "confronte" or arc5_tension_accumulee >= 4:
        x "Et après la dernière fois..."
        j "Quelle dernière fois ?"
        x "Quand tu lui as dit que c'était la troisième annulation."
        j "Elle t'en a parlé ?"
        x "Non. Allan."
        systeme "Jessy serre les dents."
        x "Je ne te juge pas. Mais peut-être que la Saint-Valentin, c'est l'occasion de... pas empirer les choses."

    # --- INTERLUDE COMIQUE : MICKA ---
    
    systeme "La porte de la classe s'ouvre. Micka entre."
    systeme "Ou plutôt, Micka essaie d'entrer. Difficile quand on croule sous une montagne de chocolats."
    
    show micka gifts at char_center
    with dissolve
    
    mi "Quelqu'un peut m'aider ? Je vois plus mes pieds."
    
    show alex teasing at char_right
    
    x "...C'est quoi tout ça ?"
    mi "Les chocolats de ce matin."
    x "De CE MATIN ?"
    mi "Ouais. J'ai pas encore fait le tour des autres classes."
    
    systeme "Jessy compte les boîtes. Il arrête à quinze."
    
    j "Y'en a des roses avec des rubans dorés..."
    mi "Ça c'est Madame Tanaka. Prof de maths."
    x "UNE PROF T'A DONNÉ DES CHOCOLATS ?"
    mi "Trois profs. Mais Madame Tanaka, elle a mis une carte."
    
    show alex serious at char_right
    
    x "Une carte qui dit quoi ?"
    mi "J'ai pas eu le temps de lire. Y'avait la queue devant mon casier."
    
    systeme "Alexandre regarde Jessy. Jessy regarde Alexandre."
    
    x "La queue."
    mi "Ben oui. Faut organiser, sinon c'est le chaos."
    
    systeme "Micka pose sa montagne sur un bureau. Trois chocolats tombent. Il ne les ramasse pas."
    
    mi "Vous avez reçu quoi, vous ?"
    j "Trois. D'Alexandre."
    mi "Ah. C'est mignon."
    
    show alex teasing at char_right
    
    x "C'était ironique !"
    mi "L'ironie, c'est de l'affection mal exprimée."
    x "C'est pas..."
    mi "Je dois y aller. La prof d'anglais veut me voir à la pause."
    j "Pour des cours particuliers ?"
    mi "Non, elle a dit qu'elle voulait 'discuter de mon avenir'. Avec un clin d'œil."
    
    systeme "Il repart avec la moitié de ses chocolats. L'autre moitié reste sur le bureau."
    systeme "Personne n'ose y toucher."
    
    hide micka
    with dissolve
    
    x "Je... je comprends plus rien à ce lycée."
    j "Tu veux un chocolat de Madame Tanaka ?"
    x "NON."

    hide alex
    with dissolve

    scene bg arc5 rooftop
    with fade

    systeme "À la pause, Jessy monte sur le toit. L'air est frais, le ciel gris, et un reste de neige s'accroche aux bords du béton. Quelque part en bas, des gens s'offrent des chocolats et font semblant que l'amour est simple."

    show jessy neutral at char_left
    show ilona fatigue at char_right
    with dissolve

    systeme "Ilona est là. Appuyée contre la rambarde. Elle regarde le vide avec cette expression qu'elle a quand elle réfléchit à quelque chose qu'elle ne veut pas dire."
    
    i "Tu me cherchais ?"
    j "Non. Mais je suis content de te trouver."
    
    systeme "Un demi-sourire traverse son visage. Comme un soleil derrière les nuages."
    
    i "Tu as reçu des chocolats ?"
    j "Trois. Tous d'Alexandre sous des pseudonymes différents."
    i "Comment tu sais que c'est lui ?"
    j "Le troisième était signé 'Ta fan mystérieuse, bisous, Alexandre, PS: c'est moi'."
    
    show ilona smile at char_right
    
    i "Il n'a pas le sens du mystère."
    j "Il a le sens de l'absurde. C'est pas pareil."

    systeme "Le silence s'installe. Pas inconfortable. Juste... plein."
    systeme "Jessy sent le poids de ce qu'il a préparé. Ou de ce qu'il n'a pas préparé. Les deux sont lourds."

    if arc5_tension_accumulee >= 3:
        systeme "Quelque chose flotte entre eux. Les messages. Les annulations. Les mots mal choisis."
        show ilona neutral at char_right
        i "On devrait peut-être parler."
        j "De quoi ?"
        i "De ce qui se passe."
        systeme "La phrase est simple. Elle fait quand même mal."
        j "Il se passe quelque chose ?"
        i "Jessy."
        systeme "Son nom dans sa bouche sonne comme un reproche."
        i "Tu sais très bien de quoi je parle."

    menu:
        systeme "Le toit. Le vent. Elle. Lui. Le moment demande quelque chose."
        
        "Offrir quelque chose de simple. Sans attente. Sans message caché.":
            $ arc5_valentin_choix = "simple"
            $ lien_jessy_ilona += 1
            $ confiance += 1
            systeme "Jessy sort une petite boîte de sa poche."
            j "Tiens."
            show ilona embarrassed at char_right
            i "Qu'est-ce que c'est ?"
            j "Du chocolat. Pas de message secret. Pas de métaphore. Juste... du chocolat."
            systeme "Elle ouvre la boîte. Regarde. Ferme."
            i "Pourquoi j'ai l'impression que c'est rare ?"
            j "Quoi ?"
            i "Un cadeau qui ne demande rien."
            systeme "La phrase fait mal. Parce qu'elle dit quelque chose sur tous les autres cadeaux."
            j "Je ne veux rien en retour."
            i "Je sais."
            systeme "Elle mange un chocolat. Lentement. Comme si elle voulait que le moment dure."
            i "Merci."

        "Offrir quelque chose lié à leur histoire. Prendre le risque du sens.":
            $ arc5_valentin_choix = "souvenir"
            $ lien_jessy_ilona += 2
            $ jalousie += 1
            $ pression_stream += 1
            systeme "Jessy sort une boîte. Dedans, des chocolats en forme de cube."
            j "Ils ressemblent à des blocs Minecraft."
            show ilona embarrassed at char_right
            systeme "Ilona fixe les chocolats. Puis Jessy. Puis les chocolats."
            i "Tu as fait faire des chocolats custom."
            j "Oui."
            i "En forme de blocs de terre."
            j "Oui."
            i "C'est..."
            systeme "Elle ne finit pas sa phrase."
            j "Trop ?"
            i "C'est beaucoup."
            systeme "Pas 'trop'. 'Beaucoup'. La différence est importante."
            i "Jessy..."
            j "Oui ?"
            i "Tu penses que je vais les aimer parce qu'ils représentent quelque chose pour nous ?"
            j "Je... oui ?"
            i "Ou tu espères que le souvenir va compenser... autre chose ?"
            systeme "La question est douce. Elle fait mal quand même."

        "Ne rien offrir. Lui demander ce qu'elle veut vraiment.":
            $ arc5_valentin_choix = "demande"
            $ communication += 3
            $ confiance += 2
            $ autonomie_ilona += 2
            $ jugement_laplage += 1
            j "Je peux te poser une question ?"
            show ilona neutral at char_right
            i "Vas-y."
            j "Tu veux quelque chose pour la Saint-Valentin ?"
            systeme "Elle cille. Comme si la question était incongrue."
            i "Tu me demandes ?"
            j "Oui."
            i "Au lieu de deviner ?"
            j "Au lieu de deviner."
            systeme "Le silence dure. Puis quelque chose change dans son visage."
            i "C'est la première fois qu'on me pose la question."
            j "Et la réponse ?"
            i "Honnêtement..."
            systeme "Elle réfléchit. Vraiment. Pas pour faire plaisir."
            i "Je veux juste qu'on reste là. Sans chocolat. Sans déclaration. Juste... ça."
            j "D'accord."
            systeme "Ils restent sur le toit. Le vent est froid. Mais l'espace entre eux est chaud."
            $ remember("ilona_libre_sans_abandon")

        "Rien. Parce qu'il n'a pas su quoi préparer et qu'il a peur.":
            $ arc5_valentin_choix = "rien_peur"
            $ confiance -= 1
            $ arc5_tension_accumulee += 1
            systeme "Jessy reste là. Les mains dans les poches. Vides."
            show ilona neutral at char_right
            i "Tu n'as rien préparé ?"
            j "Non."
            i "Pourquoi ?"
            systeme "La vraie réponse serait : parce que j'avais peur de me tromper encore."
            systeme "Mais la vraie réponse est trop vraie."
            j "Je ne savais pas quoi prendre."
            i "Ah."
            systeme "Le 'ah' est plat. Déçu peut-être. Ou juste fatigué."
            i "C'est pas grave."
            systeme "C'est grave. Mais elle ne le dira pas."

    if arc5_valentin_choix == "demande":
        show ilona smile at char_right
        i "Jessy ?"
        j "Oui ?"
        i "Tu as changé."
        j "Comment ça ?"
        i "Avant, tu aurais essayé de deviner. Tu aurais fait un geste symbolique."
        j "Et c'était mal ?"
        i "C'était... beaucoup. Tout le temps beaucoup."
        i "Et parfois, j'avais juste besoin que quelqu'un me demande ce que je voulais au lieu de décider pour moi."
        systeme "La phrase reste dans l'air. Elle parle de plus que de chocolats."
        j "Je peux être honnête ?"
        i "Oui."
        j "J'ai failli acheter quelque chose. Quelque chose de symbolique. De pensé."
        i "Et tu ne l'as pas fait ?"
        j "Non. Parce que je me suis demandé si je le faisais pour toi ou pour me rassurer."
        systeme "Le silence qui suit est différent. Plus doux."
        i "Continue à te poser cette question."
        $ confiance += 1

    if arc5_theo_proposition == "laisse":
        systeme "Le téléphone d'Ilona vibre. Elle regarde l'écran."
        show ilona neutral at char_right
        i "C'est Théo."
        j "Qu'est-ce qu'il veut ?"
        i "Il me rappelle qu'il a trié les messages du club. Et que je n'ai pas besoin de m'en occuper."
        systeme "Elle range son téléphone."
        j "C'est... bien ?"
        i "C'est pratique."
        j "Mais ?"
        i "Mais parfois j'ai l'impression qu'il gère ma vie mieux que moi."
        systeme "La phrase devrait rassurer. Elle fait l'inverse."

    hide ilona
    hide jessy
    with dissolve

# =============================================================================
# SCENE 5 : CONFIDENCE A LAPLAGE - CE QUE PERSONNE NE DEMANDE
# =============================================================================

    scene bg arc5 library night
    with fade

    systeme "Quelques jours plus tard. La bibliothèque est presque vide. Le soir tombe."

    show ilona fatigue at char_left
    with dissolve

    systeme "Ilona est assise au fond. Seule. Son livre est fermé. Ses yeux sont ouverts mais ne regardent rien."

    show laplage neutral at char_right
    with dissolve

    systeme "Monsieur Laplage apparaît. Il porte un badge qui dit 'Archiviste des Non-dits'. Personne ne lui a donné ce badge. Il l'a probablement fabriqué lui-même."
    
    laplage "Tu attends quelque chose ou tu évites quelque chose ?"
    
    show ilona embarrassed at char_left
    
    i "Je ne sais pas."
    laplage "C'est déjà une réponse."
    
    systeme "Il s'assoit en face d'elle. Sans demander. Mais sans envahir non plus."
    
    laplage "Qu'est-ce qui pèse ?"
    
    systeme "Ilona reste silencieuse un moment. Puis :"
    
    show ilona frustrated at char_left
    
    i "Tout le monde me demande ce que je vais choisir."
    laplage "Choisir quoi ?"
    i "Tout. L'université. Un garçon. Une direction."
    laplage "Et toi ?"
    
    systeme "Elle lève les yeux. Il y a quelque chose de mouillé dedans."
    
    i "Personne ne me demande si je suis fatiguée."
    
    $ confidences_laplage += 1
    $ arc5_laplage_deuxieme_confidence = True
    
    laplage "Les gens confondent souvent être proche et être propriétaire."
    i "C'est censé m'aider ?"
    laplage "Non. C'est censé nommer quelque chose que tu ressens sans savoir comment l'appeler."
    
    systeme "Elle rit. Un rire sec. Sans joie."
    
    i "Jessy veut me protéger. Théo veut m'aider. Tout le monde veut quelque chose pour moi."
    laplage "Et toi, tu veux quoi ?"
    i "Qu'on me foute la paix."
    
    systeme "Les mots sortent. Crus. Vrais."
    
    laplage "Tu l'as dit à quelqu'un ?"
    i "Non."
    laplage "Pourquoi ?"
    i "Parce que si je le dis, ils vont vouloir m'aider à avoir la paix. Et c'est exactement le problème."
    
    systeme "Laplage hoche la tête."
    
    laplage "Les gens qui t'aiment te laissent-ils ne pas choisir ?"
    
    systeme "La question reste suspendue."
    
    i "Je ne sais pas."
    laplage "C'est peut-être la question à poser. Pas à moi. À eux."
    
    systeme "Il se lève."
    
    laplage "Les étoiles qui demandent la permission avant de briller... ne brillent jamais."
    
    show laplage thumb_horizontal at char_right
    systeme "Pouce horizontal. Ni approbation ni désapprobation. Juste une observation."
    
    hide laplage
    with dissolve
    
    systeme "Il disparaît entre les rayons."

    systeme "Ilona reste seule. Le livre est toujours fermé. Mais quelque chose dans sa posture a changé."
    systeme "Elle sort son téléphone. Tape un message. Efface. Tape. Efface."
    systeme "Finalement, elle envoie :"
    systeme "{i}\"On peut se voir ? J'ai quelque chose à te demander.\"{/i}"

    hide ilona
    with dissolve

# =============================================================================
# SCENE 6 : LA QUESTION - PEUR OU CONFIANCE
# =============================================================================

    scene black
    with fade
    
    systeme "Le lendemain. Ilona a donné rendez-vous à Jessy. Un endroit neutre, a-t-elle dit."
    
    scene bg arc5 train station
    with fade

    systeme "La gare. Un quai désert. Le bruit des trains au loin."

    show jessy neutral at char_left
    show ilona determined at char_right
    with dissolve

    i "Merci d'être venu."
    j "Tu avais l'air... sérieuse."
    i "Je suis sérieuse."
    
    systeme "Elle ne sourit pas. Pas de préambule. Pas de bavardage."
    
    i "J'ai une question à te poser. Et je veux une vraie réponse."
    j "D'accord."
    i "Pas une réponse polie. Pas une réponse qui me fait plaisir. La vraie."
    j "D'accord."
    
    systeme "Un train passe. Le bruit couvre tout pendant quelques secondes. Puis le silence revient, plus lourd."
    
    systeme "Jessy se souvient. Un autre train. Une autre gare. Une phrase qu'il n'avait jamais finie."
    systeme "\"Ilona, je voulais te dire que—\" Et puis le train. Et puis le silence."
    systeme "Des mois ont passé depuis. La phrase est toujours là, quelque part, coincée entre eux."
    
    i "Est-ce que tu as peur de me perdre..."
    
    systeme "Elle le regarde droit dans les yeux."
    
    i "...ou est-ce que tu ne me fais pas confiance ?"

    systeme "La question reste là. Entre eux. Comme un mur ou comme une porte."
    systeme "Jessy sent son cœur battre dans sa gorge. Il n'y a pas de bonne réponse facile."
    systeme "Seulement la vraie. Ou les mensonges."

    menu:
        systeme "Elle attend. Le train suivant passera dans huit minutes. Il a huit minutes pour trouver les mots."
        
        "\"J'ai peur. Et je ne sais pas si je te fais confiance. Les deux sont vrais.\"":
            $ arc5_question_reponse = "honnete"
            $ remember("jessy_nomme_sa_peur")
            $ confiance += 3
            $ communication += 3
            $ jalousie -= 2
            $ jugement_laplage += 2
            $ lien_jessy_ilona += 2
            show jessy listening at char_left
            j "J'ai peur."
            systeme "Les mots sortent. Ils font mal."
            j "J'ai peur de te perdre. De ne pas être assez. De faire des conneries que je ne peux pas réparer."
            show ilona neutral at char_right
            systeme "Elle l'écoute. Elle ne l'interrompt pas."
            j "Et je ne sais pas si je te fais confiance."
            i "Qu'est-ce que tu veux dire ?"
            j "Je veux dire que... quand tu parles avec Théo, une partie de moi se demande si tu préfères pas être avec lui."
            j "Quand tu annules, une partie de moi se demande si c'est vraiment la fatigue ou si tu m'évites."
            j "Et ces parties-là... elles ne te font pas confiance. Même si je voudrais."
            systeme "Le silence dure longtemps."
            show ilona smile at char_right
            i "Merci."
            j "Merci de quoi ?"
            i "De ne pas avoir fait semblant."
            systeme "Elle s'approche. Pas pour l'embrasser. Juste pour être plus près."
            i "C'est la première fois que quelqu'un me répond vraiment à cette question."
            j "Les autres mentent ?"
            i "Les autres disent ce qu'ils pensent que je veux entendre."

        "\"Bien sûr que je te fais confiance. C'est Théo le problème.\"":
            $ arc5_question_reponse = "theo"
            $ jalousie += 3
            $ influence_theo += 2
            $ communication -= 2
            $ confiance -= 2
            $ remember("theo_utilise_une_verite")
            show jessy neutral at char_left
            j "Je te fais confiance. Complètement."
            show ilona frustrated at char_right
            i "Alors c'est quoi le problème ?"
            j "Théo."
            systeme "Le nom tombe comme une pierre."
            i "Je ne t'ai pas demandé ce que tu pensais de Théo."
            j "Mais il est toujours là ! À t'apporter du thé, à gérer tes trucs, à..."
            i "À quoi ? À m'aider ?"
            j "À prendre ma place !"
            systeme "Le cri sort avant qu'il puisse le retenir."
            systeme "Ilona recule d'un pas."
            i "Je ne t'ai pas posé une question sur Théo, Jessy."
            i "Je t'ai posé une question sur toi."
            j "C'est lié !"
            i "Non. Ce n'est pas lié. Et le fait que tu penses que c'est lié, c'est exactement le problème."
            systeme "Elle se détourne."
            i "Tu viens de me prouver que tu ne me fais pas confiance. Pas en disant la vérité. En l'évitant."

        "\"J'ai peur. Mais ma peur ne devrait pas devenir ton problème.\"":
            $ arc5_question_reponse = "responsable"
            $ remember("jessy_nomme_sa_peur")
            $ confiance += 2
            $ communication += 2
            $ autonomie_ilona += 2
            $ lien_jessy_ilona += 1
            show jessy listening at char_left
            j "J'ai peur."
            systeme "Pause."
            j "J'ai peur tout le temps. De te perdre. De mal faire. De ne pas être ce que tu mérites."
            show ilona neutral at char_right
            i "Et ?"
            j "Et je me rends compte que ma peur... ça devient ton fardeau."
            j "À chaque fois que tu annules, tu dois gérer ma déception. À chaque fois que Théo t'aide, tu dois me rassurer."
            j "C'est injuste."
            systeme "Elle le regarde. Quelque chose change dans ses yeux."
            i "Continue."
            j "Je ne sais pas encore comment arrêter d'avoir peur. Mais je sais que ça ne devrait pas être toi qui portes ça."
            systeme "Le train passe. Le bruit couvre tout."
            systeme "Quand le silence revient, elle est plus proche."
            i "C'est pas parfait comme réponse."
            j "Non."
            i "Mais c'est honnête."
            j "Oui."
            i "C'est suffisant pour aujourd'hui."

        "\"Je ne sais pas. J'ai besoin de temps pour réfléchir.\"":
            $ arc5_question_reponse = "temps"
            $ communication -= 1
            if communication >= 5:
                $ confiance += 1
                show jessy listening at char_left
                j "Je ne sais pas comment répondre."
                j "Pas parce que je veux éviter. Parce que la vraie réponse... je ne la connais pas encore."
                show ilona neutral at char_right
                i "C'est honnête au moins."
                j "Mais insuffisant."
                i "Oui. Insuffisant."
                systeme "Elle hoche la tête."
                i "Tu as jusqu'à White Day."
                j "Pourquoi White Day ?"
                i "Parce qu'il me faut une deadline. Et parce que si tu n'as pas trouvé d'ici là..."
                systeme "Elle ne finit pas sa phrase. Elle n'a pas besoin."
            else:
                $ confiance -= 2
                $ autonomie_ilona += 1
                $ arc5_tension_accumulee += 2
                show jessy neutral at char_left
                j "J'ai besoin de temps."
                show ilona frustrated at char_right
                i "Tu as eu du temps. Depuis Noël. Depuis avant."
                j "Ilona..."
                i "Non. Je t'ai posé une question simple. Et tu me demandes du temps."
                i "C'est une réponse aussi."
                systeme "Elle recule."
                i "Le temps que tu me demandes, c'est du temps que je passe à attendre."
                i "Et je suis fatiguée d'attendre."
                systeme "Elle part. Le train suivant arrive. Elle monte."
                systeme "Jessy reste sur le quai."

    if arc5_question_reponse in ("honnete", "responsable"):
        show ilona determined at char_right
        i "Je peux te dire quelque chose aussi ?"
        j "Oui."
        i "Théo... n'est pas le problème. Pas vraiment."
        j "Qu'est-ce que tu veux dire ?"
        i "Théo est là parce qu'il est utile. Parce qu'il remarque des choses. Parce qu'il agit."
        i "Le problème, c'est pas qu'il soit là. C'est que toi, tu le regardes comme une menace au lieu de te demander ce que tu pourrais faire différemment."
        systeme "La phrase est dure. Mais pas injuste."
        j "Je..."
        i "Je ne te demande pas d'être comme lui. Je te demande d'arrêter de le voir comme un ennemi."
        systeme "Un autre train passe."
        i "Tu peux faire ça ?"
        j "Je peux essayer."
        i "Essayer, c'est déjà beaucoup."

    hide ilona
    hide jessy
    with dissolve

# =============================================================================
# SCENE 7 : WHITE DAY - LA REPONSE
# =============================================================================

    scene black
    with fade
    
    systeme "Un mois passe. Février cède la place à mars. Le froid recule lentement."
    
    scene bg arc5 classroom
    with fade
    
    systeme "14 mars. White Day. Le jour où les garçons doivent 'rendre' les chocolats de la Saint-Valentin."

    # --- INTERLUDE COMIQUE : MICKA WHITE DAY ---
    
    show jessy neutral at char_left
    show alex teasing at char_right
    with dissolve
    
    x "T'as vu Micka ce matin ?"
    j "Non. Pourquoi ?"
    x "Il a pas dormi de la nuit."
    j "Insomnie ?"
    x "Pâtisserie."
    
    systeme "La porte s'ouvre. Micka entre. Des cernes jusqu'au menton. De la farine dans les cheveux."
    
    show micka happy at char_center
    with dissolve
    
    mi "Je vais mourir."
    x "T'as fait combien de gâteaux ?"
    mi "Trente-sept."
    j "TRENTE-SEPT ?"
    mi "White Day, tu dois rendre le triple de ce que t'as reçu. C'est la tradition."
    x "Mais t'avais reçu combien de chocolats ?"
    mi "J'ai arrêté de compter à quarante-deux."
    
    systeme "Jessy fait le calcul mental. Puis abandonne."
    
    mi "Et le pire c'est les profs."
    j "Les profs ?"
    mi "Madame Tanaka veut un gâteau fait maison. Madame Yamamoto veut des macarons."
    mi "Et la prof d'anglais..."
    x "Elle veut quoi ?"
    mi "Elle a dit 'surprends-moi'."
    
    systeme "Silence."
    
    x "T'as fait quoi ?"
    mi "Un opéra au chocolat avec son prénom en ganache."
    j "Tu connais son prénom ?"
    mi "Elle me l'a donné. À la Saint-Valentin. Avec son numéro."
    
    show alex serious at char_right
    
    x "SON NUMÉRO ?"
    mi "Pour les 'questions sur les cours', elle a dit."
    j "Et tu l'as appelée ?"
    mi "Non. Elle m'appelle."
    x "Elle t'APPELLE ?"
    mi "Pour vérifier que j'ai bien compris les exercices."
    
    systeme "Alexandre se tourne vers Jessy."
    
    x "Je... je comprends plus rien à ce monde."
    
    mi "Bon, faut que j'y aille. J'ai rendez-vous avec la prof de sport dans dix minutes."
    j "Pour lui donner son gâteau ?"
    mi "Non, elle m'a rien donné à la Saint-Valentin. Elle veut juste 'discuter de ma forme physique'."
    
    systeme "Il repart. Toujours aussi épuisé. Toujours aussi inconscient."
    
    hide micka
    with dissolve
    
    x "Je... je vais aller réviser. Loin. Très loin de tout ça."
    j "T'as pas envie de savoir comment ça finit ?"
    x "NON."
    
    hide jessy
    hide alex
    with dissolve
    
    # --- FIN INTERLUDE ---
    
    scene bg arc5 park spring
    with fade

    systeme "Plus tard. Les cerisiers commencent à fleurir. Le monde se réveille après l'hiver."

    show jessy neutral at char_left
    show ilona neutral at char_right
    with dissolve

    systeme "Ils se retrouvent dans le parc près de la gare. Les cerisiers commencent à perdre leurs premiers pétales."
    
    if arc5_question_reponse == "honnete":
        systeme "Depuis la gare, quelque chose a changé. Pas résolu. Changé."
        systeme "Ils se parlent plus. Ou plutôt, ils se parlent mieux."
    elif arc5_question_reponse == "theo":
        systeme "Depuis la gare, les choses sont tendues. Pas cassées. Tendues."
        systeme "Ilona n'évite pas Jessy. Mais elle ne cherche pas sa présence non plus."
    elif arc5_question_reponse == "temps":
        systeme "La deadline est là. Jessy a eu un mois pour trouver une réponse."
    else:
        systeme "Un mois a passé. Les questions sont restées les mêmes."

    if arc4_cadeau_jessy == "miniature_souvenir":
        systeme "Jessy repense à la miniature de Noël. Ilona l'a posée sur son bureau. Il l'a vue une fois, en passant."
        systeme "Elle n'en a jamais reparlé. Mais elle ne l'a pas rangée non plus."
    elif arc4_cadeau_jessy == "cadeau_couteux":
        systeme "L'écharpe de Noël est rangée quelque part. Ilona ne l'a jamais portée."
        systeme "Jessy n'a jamais demandé pourquoi. Certaines questions ne veulent pas de réponse."
    
    if arc4_limite_ilona == "demande_theo":
        systeme "Depuis Noël, quelque chose s'est déplacé. Ilona passe plus de temps avec Théo."
        systeme "Pas par choix, peut-être. Par fatigue. Par habitude. Par facilité."

    if arc4_ilona_avec_theo:
        if arc4_5_ilona_reaction == "accepte":
            systeme "Il y a aussi cette soirée dont Jessy ne connaît que les bords : une marche, un café ouvert tard, et Théo qui a écouté un rêve avant lui."
        elif arc4_5_ilona_reaction == "prudente":
            systeme "Mais Ilona n'a pas disparu dans l'aide de Théo. Elle a appris à dire 'pas maintenant' sans s'excuser."
        elif arc4_5_ilona_reaction == "directe":
            systeme "Et depuis cette marche, une question flotte autour d'eux : est-ce qu'aider quelqu'un suffit, si on a besoin d'être celui qui aide ?"

    i "Alors ?"
    j "Alors quoi ?"
    i "Tu sais quoi."
    
    systeme "White Day. Le jour de la réponse."

    menu:
        systeme "Le parc est presque vide. Les pétales tombent lentement. C'est maintenant."
        
        "Lui offrir de l'espace. Vraiment. Sans condition.":
            $ arc5_white_day_reponse = "espace"
            $ autonomie_ilona += 3
            $ confiance += 2
            $ remember("ilona_libre_sans_abandon")
            j "Je ne t'ai rien apporté."
            show ilona neutral at char_right
            i "Rien ?"
            j "J'ai réfléchi à ce que je pouvais t'offrir. Des chocolats. Un truc symbolique. Quelque chose qui dirait ce que je ressens."
            j "Et puis je me suis rendu compte que... t'en avais peut-être marre qu'on t'offre des trucs."
            i "Qu'est-ce que tu veux dire ?"
            j "Je veux dire que tout le monde t'apporte des choses. Du thé. Des notes. De l'aide. Des cadeaux."
            j "Et moi, j'ai failli faire pareil. Compenser avec un objet."
            show ilona embarrassed at char_right
            i "Et à la place ?"
            j "À la place, je te donne... de l'espace. Si tu en veux."
            i "De l'espace ?"
            if arc4_5_ilona_reaction == "prudente":
                j "Le même espace que celui que tu as gardé quand tu as dit que tu voulais du temps. Je crois que j'ai enfin compris que ce n'était pas une menace."
            elif arc4_5_ilona_reaction == "accepte":
                j "Pas un espace que quelqu'un organise pour toi. Un espace qui reste à toi, même si je ne sais pas quoi en faire."
            j "Le droit de ne pas répondre. De ne pas choisir. De juste... être fatiguée si tu l'es."
            systeme "Le silence dure longtemps."
            i "Tu n'as pas peur que je m'en aille ?"
            j "Si. Mais j'ai encore plus peur de t'étouffer."
            show ilona smile at char_right
            i "C'est... pas mal comme réponse."

        "Lui dire ce qu'il a compris. Sans cadeau. Avec des mots.":
            $ arc5_white_day_reponse = "mots"
            $ communication += 3
            $ confiance += 2
            $ lien_jessy_ilona += 1
            j "J'ai quelque chose à te dire. Pas un cadeau. Des mots."
            show ilona neutral at char_right
            i "Je t'écoute."
            j "J'ai passé le dernier mois à réfléchir. À ce que tu m'as demandé à la gare."
            j "Et je me suis rendu compte que... tu avais raison."
            i "Sur quoi ?"
            j "Sur le fait que ma peur te pesait. Que chaque fois que je vérifiais, que je m'inquiétais, que je comparais..."
            j "Je te demandais de me rassurer. Au lieu de juste... te faire confiance."
            if arc4_5_ilona_reaction == "directe":
                j "Et je crois que ta question à Théo m'a fait comprendre autre chose aussi."
                j "On peut aider quelqu'un pour de vraies raisons, et quand même avoir besoin d'être indispensable."
                j "Je ne veux pas devenir ça. Même avec de bonnes intentions."
            show ilona embarrassed at char_right
            i "Et maintenant ?"
            j "Maintenant, je ne suis pas guéri. J'ai encore peur. Mais je sais que cette peur est mon problème. Pas le tien."
            systeme "Elle le regarde longuement."
            i "Tu le penses vraiment ?"
            j "Je ne sais pas si je peux le vivre tout le temps. Mais je veux essayer."
            i "C'est déjà beaucoup."

        "Tenter de réparer avec un grand geste. Parce qu'il ne sait pas faire autrement.":
            $ arc5_white_day_reponse = "grand_geste"
            $ pression_stream += 2
            $ jalousie += 1
            $ confiance -= 1
            systeme "Jessy sort quelque chose de son sac. C'est emballé. C'est gros."
            j "Je t'ai préparé quelque chose."
            show ilona neutral at char_right
            i "Jessy..."
            j "Ouvre."
            systeme "Elle ouvre. C'est un album photo. Avec tous leurs moments ensemble. Imprimés. Annotés."
            show ilona frustrated at char_right
            i "C'est..."
            j "Je sais que c'est beaucoup. Mais je voulais te montrer que..."
            i "Jessy."
            j "Quoi ?"
            i "On a parlé de ça. À la gare. Je t'ai dit que j'étais fatiguée qu'on m'apporte des choses."
            if arc4_5_theo_proposition == "gestion_stream":
                i "Théo propose de gérer. Toi tu proposes de compenser. Vous appelez ça différemment, mais moi je sens surtout le poids."
            j "Ce n'est pas une chose. C'est un souvenir."
            i "C'est un souvenir qui pèse trois kilos et qui me demande de réagir d'une certaine façon."
            systeme "Elle ferme l'album."
            i "Je ne dis pas que c'est pas touchant. Je dis que c'est... beaucoup."
            i "Et que 'beaucoup', en ce moment, c'est exactement ce dont je n'ai pas besoin."

        "Lui poser la question en retour. Parce qu'il a le droit de savoir aussi.":
            $ arc5_white_day_reponse = "retour"
            $ communication += 2
            if arc5_question_reponse == "honnete" or arc5_question_reponse == "responsable":
                $ confiance += 1
                $ lien_jessy_ilona += 1
                j "Je peux te poser une question aussi ?"
                show ilona neutral at char_right
                i "Vas-y."
                j "Est-ce que tu me fais confiance ?"
                systeme "La question reste dans l'air."
                i "C'est... une bonne question."
                j "Tu ne sais pas ?"
                i "Je sais que je veux te faire confiance. Je sais que des fois, c'est difficile."
                j "Pourquoi ?"
                i "Parce que des fois, j'ai l'impression que tu me vois comme quelque chose à protéger. Pas comme quelqu'un de capable."
                systeme "La phrase fait mal. Parce qu'elle est vraie."
                j "Je ne..."
                i "Tu le fais sans le vouloir. Mais tu le fais."
                systeme "Elle soupire."
                i "On a du travail. Tous les deux."
            else:
                $ confiance -= 1
                j "Et toi, tu me fais confiance ?"
                show ilona frustrated at char_right
                i "Tu me retournes la question maintenant ?"
                j "Pourquoi pas ? Tu voulais de l'honnêteté. Alors sois honnête aussi."
                i "Ce n'est pas pareil."
                j "Pourquoi ?"
                i "Parce que moi, j'ai posé ma question. Et toi, tu n'as toujours pas vraiment répondu."
                systeme "Le silence est lourd."
                i "On ne peut pas avancer si tu transformes chaque conversation en match de tennis."

    if arc5_white_day_reponse in ("espace", "mots") and arc5_question_reponse in ("honnete", "responsable"):
        $ confiance += 1
        $ lien_jessy_ilona += 1
        show ilona smile at char_right
        i "Jessy ?"
        j "Oui ?"
        i "Je crois qu'on peut y arriver."
        j "À quoi ?"
        i "À... ça. Nous. Malgré tout."
        systeme "Elle ne précise pas ce que 'ça' veut dire. Mais quelque chose dans l'air dit qu'elle parle d'avenir."
        j "Je veux y arriver."
        i "Moi aussi."
        systeme "Ce n'est pas une déclaration d'amour. C'est mieux : une déclaration d'intention."

    hide ilona
    hide jessy
    with dissolve

# =============================================================================
# SCENE 8 : ALLAN ET ALEXANDRE - CE QU'ILS VOIENT
# =============================================================================

    scene bg arc5 cafe
    with fade

    show allan doubt at char_left
    show alex serious at char_right
    with dissolve

    systeme "Ailleurs. Le même café qu'au début du mois."
    
    x "Alors, verdict sur la journée ?"
    a "Micka a survécu. C'est déjà ça."
    x "Les profs aussi ?"
    a "Madame Tanaka avait l'air... satisfaite."
    x "Je veux pas savoir."
    
    systeme "Allan remue son café."
    
    x "Et pour Jessy et Ilona ?"
    a "Ils étaient dans le parc. Je les ai croisés."
    x "Ça avait l'air comment ?"
    a "Moins tendu qu'avant. Mais pas réglé."
    
    show alex neutral at char_right
    
    x "Tu crois que c'est Théo le problème ?"
    
    show allan doubt at char_left
    
    a "Le problème avec Théo, c'est qu'il n'est jamais le problème."
    x "Comment ça ?"
    a "Il aide. Il remarque. Il agit. Tout ça, c'est vrai."
    a "Mais j'ai jamais vu quelqu'un qui accepte aussi mal qu'on lui dise non."
    x "Il s'énerve ?"
    a "Pire. Il trouve un autre chemin. Comme si 'non' voulait juste dire 'pas encore'."
    
    systeme "Alexandre réfléchit."
    
    x "C'est pas forcément méchant."
    a "Non. Mais c'est pas normal non plus."
    a "Les gens normaux, quand on leur dit non, ils s'arrêtent. Ou ils s'énervent. Lui, il... optimise."

    hide allan
    hide alex
    with dissolve

# =============================================================================
# SCENE 9 : SOFIANE - LA ROUTE
# =============================================================================

    scene bg arc5 rain street
    with fade

    systeme "En sortant du café, la nuit commence à tomber. L'air sent la pluie passée."

    show allan neutral at char_left
    show alex neutral at char_center
    with dissolve

    systeme "Sofiane surgit de nulle part. Comme d'habitude."
    
    show sofiane smirk at char_right
    with dissolve
    
    s "Les chemins convergent."
    x "Tu pourrais dire 'salut' comme une personne normale ?"
    s "Les personnes normales n'ont pas de vision."
    a "Quelle vision ?"
    
    systeme "Sofiane sort un trousseau de sa poche. Une seule clé. Le porte-clé représente une voiture."
    
    s "Mon cousin part à l'armée. Il m'a confié sa voiture."
    x "Une vraie voiture ?"
    s "Une AE86. Comme dans Initial D."
    a "Tu sais conduire ?"
    s "J'ai le permis depuis six mois. Je n'en ai jamais parlé."
    x "Pourquoi ?"
    s "Parce que les gens posent des questions quand on a une voiture."
    
    systeme "Il range les clés."
    
    s "Cet été. Les montagnes. Loin de tout ça."
    x "Loin de quoi ?"
    s "Des choix. Des questions. Des regards qui attendent des réponses."
    
    show allan support at char_left
    
    a "On en aurait tous besoin."
    s "Certains plus que d'autres."
    
    systeme "Il regarde vers le ciel. Comme s'il voyait quelque chose que les autres ne voient pas."
    
    s "Les étoiles parlent à ceux qui savent se taire."
    
    systeme "Puis il s'éloigne. Ses pas ne font presque pas de bruit."
    
    hide sofiane
    with dissolve
    
    x "Un jour, quelqu'un m'expliquera ce type."
    a "Peut-être que l'explication n'est pas le but."

    hide allan
    hide alex
    with dissolve

# =============================================================================
# SCENE 10 : MINECRAFT - L'ÉTAT DES LIEUX
# =============================================================================

    scene bg arc5 minecraft night
    with Dissolve(2.0)

    show jessy minecraft at char_left
    show ilona minecraft at char_right
    with dissolve

    systeme "Plus tard. La maison Minecraft. Elle existe toujours. Avec ses couches. Ses ajouts. Ses cicatrices."

    if arc3_fin_minecraft == "destruction":
        systeme "La salle moyennement importante n'a jamais été reconstruite depuis le festival. Son absence laisse un vide."
        systeme "Jessy n'en a jamais reparlé. Ilona non plus. Certains silences sont des conversations."
    elif arc3_fin_minecraft == "panneau_finir_phrase":
        systeme "Le panneau de l'Arc 3 est toujours là. 'Laisse-la finir ses phrases.' Un rappel silencieux."
        systeme "Jessy ne sait pas si Ilona l'a vu. Il ne lui a jamais demandé."
    elif arc3_fin_minecraft == "lanterne_cour":
        systeme "La lanterne bleue de la cour brille toujours. Un point fixe dans le chaos des mois passés."

    if arc5_question_reponse == "honnete" and arc5_white_day_reponse in ("espace", "mots"):
        $ arc5_fin_minecraft = "salle_repos"
        $ lien_jessy_ilona += 2
        $ confiance += 1
        $ remember("maison_respectee")
        
        i "Je veux construire quelque chose."
        j "Quoi ?"
        i "Une pièce. Pour moi."
        j "Dans la maison ?"
        i "À côté. Reliée, mais séparée."
        systeme "Jessy ne demande pas pourquoi."
        j "D'accord."
        i "Tu ne veux pas savoir à quoi ça sert ?"
        j "Si tu veux me le dire, tu me le diras."
        systeme "Silence."
        show ilona minecraft at char_right
        i "C'est une salle de repos."
        j "Pour quand tu es fatiguée ?"
        i "Pour quand j'ai besoin d'être seule. Mais pas loin."
        j "Je peux t'aider ?"
        i "Non."
        systeme "Pause."
        i "Mais tu peux rester. Dans la maison. Pendant que je construis."
        systeme "C'est une permission. Une façon de dire : je veux mon espace, mais je veux aussi que tu sois là."
        j "D'accord."
        $ maison_minecraft_ajouts.append("salle_repos_arc5")

    elif arc5_question_reponse == "theo":
        $ arc5_fin_minecraft = "distance"
        $ pression_stream += 1
        
        systeme "Ilona est en ligne. Mais pas dans la maison."
        systeme "Son avatar est à plusieurs chunks de distance. Elle construit quelque chose."
        j "Tu viens ?"
        i "Pas maintenant."
        j "Qu'est-ce que tu fais ?"
        i "Je réfléchis."
        j "En construisant ?"
        i "C'est ma façon de réfléchir."
        systeme "Jessy reste dans la maison. Il regarde par la fenêtre."
        systeme "Elle n'est pas partie. Mais elle n'est pas là non plus."
        $ maison_minecraft_ajouts.append("construction_loin_arc5")

    elif arc5_theo_proposition == "laisse" and arc5_theo_dans_maison:
        $ arc5_fin_minecraft = "theo_presence"
        $ influence_theo += 1
        
        systeme "En se connectant, Jessy remarque quelque chose."
        systeme "Un coffre qu'il n'a pas posé. Des panneaux avec des instructions. Un système de classement."
        j "C'est quoi tout ça ?"
        i "Théo m'a aidée à organiser."
        j "Théo a accès à la maison ?"
        i "Je lui ai donné le mot de passe du serveur."
        systeme "Les mots restent suspendus."
        j "Tu lui as... pourquoi ?"
        i "Parce qu'il voulait m'aider. Et que toi, tu avais dit de le laisser faire."
        systeme "La phrase fait mal. Parce que c'est vrai."
        systeme "Quelque chose dans la maison ne lui appartient plus."
        $ maison_minecraft_ajouts.append("coffres_theo_arc5")

    elif arc5_white_day_reponse == "grand_geste":
        $ arc5_fin_minecraft = "panneau"
        
        systeme "Ilona a posé un panneau devant la porte de la salle secrète."
        systeme "Le panneau dit : 'BESOIN D'AIR'."
        j "Tu veux que je parte ?"
        i "Non. Juste... n'entre pas là ce soir."
        j "D'accord."
        systeme "Ils construisent ailleurs. Des choses sans importance."
        systeme "Ce n'est pas une réconciliation. C'est une cohabitation."
        $ maison_minecraft_ajouts.append("panneau_air_arc5")

    else:
        $ arc5_fin_minecraft = "neutre"
        $ confiance += 1
        
        systeme "Jessy pose un coffre près de l'entrée."
        j "Tiens."
        i "C'est quoi ?"
        j "Des matériaux. Pour toi."
        i "Pour construire quoi ?"
        j "Ce que tu veux."
        show ilona minecraft at char_right
        i "Tu ne veux pas décider ensemble ?"
        j "Non. C'est pour toi. Sans attente."
        systeme "Elle ouvre le coffre. Regarde. Ne prend rien."
        i "Merci."
        systeme "Elle sait qu'il est là. C'est suffisant pour l'instant."
        $ maison_minecraft_ajouts.append("coffre_libre_arc5")

    # Easter egg Ilonanium
    if ilonanium_points >= 3 and arc5_valentin_choix == "demande":
        systeme "Dans un coin de l'écran, quelque chose scintille."
        i "Tu vois ça ?"
        j "Le truc qui brille ?"
        i "On dirait une traînée cosmique."
        j "Dans Minecraft ?"
        i "Peut-être que ce n'est pas vraiment Minecraft."
        systeme "Elle ne développe pas. Jessy non plus."
        systeme "Mais pendant une seconde, ils regardent tous les deux la même chose."
        $ ilonanium_points += 1

    systeme "La nuit avance dans le monde carré."
    
    if arc5_fin_minecraft == "salle_repos":
        systeme "Quelque part à côté de la maison, une nouvelle structure prend forme."
        systeme "Quatre murs. Un toit. Une porte. Simple."
        systeme "Elle n'est pas terminée. Elle ne le sera peut-être jamais."
        systeme "Mais l'espace existe. Et c'est suffisant."
    elif arc5_fin_minecraft == "distance":
        systeme "Au loin, la construction d'Ilona grandit."
        systeme "Jessy ne sait pas ce que c'est. Elle ne lui a pas dit."
        systeme "Et pour la première fois, il n'a pas demandé."
    elif arc5_fin_minecraft == "theo_presence":
        systeme "La maison est plus organisée. Plus efficace."
        systeme "Mais quelque chose manque. Quelque chose de chaotique et de vivant."
        systeme "L'espace est optimisé. L'âme, peut-être pas."
    else:
        systeme "La maison contient une trace de plus."
        systeme "Un coffre. Un panneau. Une question sans réponse."
        systeme "Le lien est un chantier. Toujours en construction."

    hide jessy
    hide ilona
    with dissolve

    scene black
    with fade

    systeme "Le printemps s'installe. Les examens sont passés."
    systeme "Des questions ont trouvé des réponses. D'autres attendent encore."
    
    if arc5_question_reponse == "honnete" and souvenirs.get("jessy_nomme_sa_peur", False):
        systeme "Jessy a nommé sa peur. C'est un début. Pas une fin."
    elif arc5_question_reponse == "theo":
        systeme "Théo reste un fantôme entre eux. Une présence qu'ils n'ont pas su régler."
    elif arc5_question_reponse == "temps":
        systeme "Le temps demandé n'a rien résolu. Juste reporté."
    
    if arc5_laplage_deuxieme_confidence:
        systeme "Ilona a dit à voix haute ce que personne ne demandait : elle est fatiguée."
        systeme "La question maintenant, c'est qui l'écoutera."

    systeme "L'Arc VI approche. Les diplômes. Les choix d'orientation."
    systeme "Le moment où 'plus tard' devient 'maintenant'."

    jump arc_6_diplomes


# =============================================================================
# RECAPITULATIF ARC V
# =============================================================================
# 
# Variables modifiées :
# - lien_jessy_ilona : +1 à +4 selon parcours
# - confiance : -3 à +6 selon honnêteté des réponses
# - communication : -2 à +6 selon qualité des échanges
# - jalousie : +2 à +8 selon réactions à Théo
# - autonomie_ilona : -2 à +8 selon respect de ses choix
# - influence_theo : -2 à +6 selon acceptation de son aide
# - pression_stream : +0 à +4 selon accumulation de tension
# - confidences_laplage : +1 (deuxième confidence obligatoire)
# - jugement_laplage : +0 à +4 selon qualité des choix
# - ilonanium_points : +1 possible si route active
#
# Souvenirs modifiés :
# - jessy_nomme_sa_peur : True si réponse honnête à la question centrale
# - ilona_libre_sans_abandon : True si espace respecté
# - theo_utilise_une_verite : True si Jessy accuse Théo au lieu de répondre
# - maison_respectee : True si construction collaborative
#
# Variables locales Arc V :
# - arc5_sortie_annulee : réaction à l'annulation (impact sur tension)
# - arc5_theo_proposition : réponse à la proposition de Théo (impact sur influence)
# - arc5_valentin_choix : approche Saint-Valentin (impact sur relation)
# - arc5_question_reponse : réponse à LA question (définit le ton de l'arc)
# - arc5_white_day_reponse : comportement White Day (test si apprentissage)
# - arc5_fin_minecraft : état de la maison (reflet de la relation)
# - arc5_tension_accumulee : indicateur de fragilité
# - arc5_theo_dans_maison : Théo a accès au serveur Minecraft
# - arc5_allan_voit_theo : Allan exprime ses doutes
# - arc5_ilona_a_pleure : si elle craque
# - arc5_jessy_a_menti : si mensonge sur sa peur
#
# Choix cornéliens et conséquences :
# - "J'ai peur mais je ne te fais pas confiance" = honnêteté totale, risque d'effrayer
# - Laisser Théo gérer = facilité immédiate, perte de contrôle future
# - Demander ce qu'elle veut = respect mais abandon du rôle protecteur
# - Confronter sur les annulations = vérité blessante
# - Offrir de l'espace = perdre du terrain vs respecter l'autonomie
#
# Fils narratifs ouverts pour Arc VI :
# - Allan identifie un malaise chez Théo (préparation confrontation)
# - Sofiane a les clés de voiture (Arc VII - road trip)
# - Ilona construit son espace personnel (besoin d'autonomie)
# - Question de l'avenir devient concrète (orientation)
# - Théo peut avoir gagné l'accès à la maison Minecraft (invasion symbolique)
# - La deuxième confidence Laplage pose la question : "Qui t'écoute vraiment ?"
