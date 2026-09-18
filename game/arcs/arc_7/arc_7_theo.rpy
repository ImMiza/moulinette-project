# ARC VII - ROUTE THEO
# Mapping depuis arc 6 :
#   controle_repetitif >= 3         -> entree forcee ici
#   arc6_score < SEUIL_JESSY        -> entree ici
#   confidences_laplage >= 3        -> sortie Laplage possible si influence basse
#   influence_theo                  -> poids de la route Theo
#   arc6_offre_theo                 -> maniere dont l'offre de Theo s'est imposee
#   arc6_stylo                      -> presence et place du stylo a Tokyo
#   arcs 2-6                        -> ce que Theo a fait, observe ou appris
#                                      de la plage jusqu'au depart
# L'entree se fait TOUJOURS via arc_6_bascule_theo (fin de arc_6_diplomes.rpy),
#
# Choix final (scenes deplacees depuis bad_ending.rpy) :
#   Theo ecoute Ilona    -> jump ending_neutre (game/arcs/endings/ending_neutre.rpy)
#   Theo priorise le business -> jump bad_ending (game/arcs/endings/bad_ending.rpy)
# Remplace l'ancien dispatch par stats (ending_monsieur_laplage / ending_theo_vtuber),
# desormais mort code : ces deux labels restent en stub dans script.rpy si besoin
# de les reutiliser ailleurs.

# --- Personnage local (tchat Twitch, anonyme) ---
define tchat = Character("Tchat", color="#7fd6ff", callback=speaker_callback(""))

# --- Audio local ---
define audio.stream = "audio/music/ecole-nuit.ogg"

# --- Decors propres a la route Theo ---
image bg arc7 intro stream = im.Scale("images/scenes/arc_7/bg_arc7_intro_stream.jpg", 1920, 1080)
image bg arc7 tokyo studio = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_streaming_studio_night.jpg", 1920, 1080)
image bg arc7 tokyo morning = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_morning.jpg", 1920, 1080)
image bg arc7 tokyo house night = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_night.png", 1920, 1080)
image bg arc7 tokyo konbini night = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_konbini_night.png", 1920, 1080)

# --- Tenues Tokyo propres a la route Theo ---
image ilona tokyo embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/awkward_embarrassment.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo neutral = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/neutral.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo smile = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/playful_warm_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo fatigue = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/quiet_fatigue.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo sad = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/sad.png", ILONA_SIZE[0], ILONA_SIZE[1])

# La tenue de stream constitue la persona publique d'IlonaGaming.
image ilona streaming victory = speaker_sprite("ilona", "images/personnages/Ilona/streaming/playful_excitement.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona streaming celebration = speaker_sprite("ilona", "images/personnages/Ilona/streaming/joyful_celebration.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona streaming joy = speaker_sprite("ilona", "images/personnages/Ilona/streaming/genuine_laughter.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona streaming smile = speaker_sprite("ilona", "images/personnages/Ilona/streaming/bright_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona streaming fatigue = speaker_sprite("ilona", "images/personnages/Ilona/streaming/quiet_fatigue.png", ILONA_SIZE[0], ILONA_SIZE[1])

image theo tokyo disappointed = speaker_sprite("theo", "images/personnages/Théo/tokyo/cold_disappointment.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo annoyed = speaker_sprite("theo", "images/personnages/Théo/tokyo/controlled_annoyance.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo defensive = speaker_sprite("theo", "images/personnages/Théo/tokyo/defense_frustration.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo innocent = speaker_sprite("theo", "images/personnages/Théo/tokyo/feigned_innocence.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo smirk = speaker_sprite("theo", "images/personnages/Théo/tokyo/knowing_smirk.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo neutral = speaker_sprite("theo", "images/personnages/Théo/tokyo/neutral.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo jealousy = speaker_sprite("theo", "images/personnages/Théo/tokyo/quiet_jalousy.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo reassuring = speaker_sprite("theo", "images/personnages/Théo/tokyo/reassuring_smile.png", 842, 1264, THEO_CROP_BOTTOM)

label arc_7_theo:
    $ derniere_route = "Route Theo"
    $ controle_repetitif = interruptions_ilona - interruptions_reparees

    scene bg arc7 intro stream
    with fade

    systeme "Arc VII - Le monde apres le depart."
    systeme "Dans la penombre, le studio attend que ses ecrans s'allument. Autour d'Ilona, tout est deja a sa place."

    # Rappel lisible du point de bascule de l'arc 6, sans afficher de jauge.
    if controle_repetitif >= 3:
        systeme "A la fin du diplome, ce ne sont pas les grandes erreurs qui ont tranche. Ce sont les petites coupures repetees."
    elif arc6_score < SEUIL_JESSY:
        systeme "A la fin du diplome, il n'y avait pas assez d'espace autour d'Ilona pour qu'elle reste sans se reduire."
    else:
        systeme "La route a garde une trace fausse. Quelque chose a ete force avant d'arriver ici."

    if arc6_offre_theo == "laisse":
        systeme "Theo avait regarde le silence autour de son offre devenir une reponse. Il n'avait pas demande a Ilona si elle avait choisi, ou simplement cesse de resister."
    elif arc6_offre_theo == "accusation":
        systeme "Quelqu'un avait nomme tout haut la place que Theo voulait dans le futur d'Ilona. Theo ne l'avait pas niee. Il avait seulement range cette envie derriere une opportunite reelle."
    elif arc6_offre_theo == "question":
        systeme "Dans le couloir, Ilona avait demande a Theo s'il proposait une opportunite ou s'il lui demandait de venir avec lui. Il avait repondu : les deux."
    elif arc6_offre_theo == "aveu_vide":
        systeme "Ce jour-la, le studio, l'equipe et Tokyo avaient rempli tout l'espace de la conversation. Theo avait pris ce vide pour une preuve que son offre etait la seule assez concrete."

    # ------------------------------------------------------------------
    # 1. Contexte : apres le 6 avril, couple, colocation et montee de la chaine
    # ------------------------------------------------------------------

    systeme "Le train du 6 avril ne les avait pas deposes directement dans une nouvelle vie. Il les avait deposes avec deux valises, une adresse envoyee par le studio et onze jours passes a preparer un depart plus vite que leur relation."
    scene bg arc7 tokyo morning
    with fade

    systeme "Tokyo a d'abord ressemble a une reponse. Des trains a l'heure, des rues qui ne dorment pas, et une maison louee par le studio a deux rues des locaux."
    systeme "La maison a quatre chambres. Ilona et Theo occupent les deux de l'etage ; deux autres membres de l'equipe du studio vivent en bas."
    systeme "L'un travaille surtout au montage, l'autre a la production. Ils restent hors du centre de cette histoire : des chaussures pres de l'entree, des etiquettes sur les boites du frigo, parfois une lumiere sous une porte apres minuit."
    systeme "La cuisine et le salon sont communs. Ilona et Theo ont chacun leur chambre. Au debut, cette distance d'un couloir leur parait saine."

    systeme "Dix jours apres leur arrivee, Theo demande a Ilona de marcher avec lui sans parler du studio."

    scene bg arc7 tokyo konbini night
    with fade

    systeme "Ils marchent jusqu'a ce que les locaux disparaissent derriere eux. Ils finissent devant un konbini ouvert toute la nuit, dans la lumiere blanche de la vitrine."

    show theo tokyo neutral at char_right
    show ilona tokyo neutral at char_left
    with dissolve

    t "Je veux pas faire comme si le train avait repondu a notre place."
    i "A quelle question ?"
    t "A nous. Je te demande pas si tu veux travailler avec moi. Je te demande si tu veux sortir avec moi. Pour de vrai."
    i "Et si je dis oui, ca devient pas une clause du studio."
    t "Non."
    i "Ca veut pas dire que j'ai choisi Tokyo pour toi."
    t "Je sais."
    i "Alors oui. On peut essayer."

    systeme "A partir de ce soir-la, Ilona et Theo sortent officiellement ensemble. Pas parce qu'ils partagent une adresse ou un projet : parce qu'ils se le sont demande et qu'Ilona a dit oui."
    systeme "Pendant le premier mois, ils arrivent encore a separer les deux. Ramen apres les repetitions, promenades sans telephone, series regardees trop tard dans le salon quand les deux autres colocataires dorment deja."
    systeme "Puis un rendez-vous remplace une promenade. Une miniature urgente mange un diner. Theo dit « on se rattrape demain », et demain arrive avec un nouveau mail."

    hide theo
    hide ilona
    with dissolve

    scene black
    with fade

    systeme "En mai, la chaine depasse les premiers paliers qu'Ilona imaginait encore depuis son ancienne chambre. En juillet, le studio lui attribue des horaires fixes et une equipe technique. A l'automne, les marques commencent a demander Theo avant meme de demander Ilona."
    systeme "Huit mois apres le depart, ils vivent toujours dans la meme maison et sortent toujours ensemble. La chaine « IlonaGaming » est devenue leur travail, leur sujet de conversation et, trop souvent, leur seule activite a deux."

    scene bg arc7 tokyo morning
    with fade

    systeme "Ce matin-la, la lumiere blanche remplit la piece commune. Sur la table, les tasses et les feuilles de production entourent le carnet de planning."

    # Le dernier emplacement du stylo est fixe par la decision de l'arc 6.
    if arc6_stylo == "garde":
        systeme "En defaisant ses affaires, Ilona n'avait trouve aucun stylo violet. Il n'avait pas fait le voyage jusqu'a Tokyo."
    elif arc6_stylo == "rendu_explique":
        systeme "Le stylo violet avait voyage dans la poche exterieure de son sac. Ilona l'y avait laisse plusieurs semaines : trop charge pour redevenir tout de suite un objet ordinaire."
    elif arc6_stylo == "rendu":
        systeme "Le stylo violet avait voyage dans la poche exterieure de son sac. Le premier matin, Ilona l'avait remis dans sa trousse. Depuis, il ecrit comme les autres."
    elif arc6_stylo == "blague":
        systeme "Le stylo violet avait voyage dans la poche exterieure de son sac. La blague du pain au lait n'avait pas voyage avec lui."

    if souvenirs["ilona_veut_streamer_serieusement"]:
        systeme "Ilona avait dit un jour qu'elle voulait streamer serieusement. Theo a pris cette phrase au serieux. Peut-etre plus qu'elle."

    if arc4_ilona_avec_theo:
        systeme "Au debut, c'etait reposant. Quelqu'un qui reserve, qui prevoit, qui sait toujours ou il faut etre et a quelle heure."
        systeme "L'echarpe de Theo, qu'Ilona portait encore le jour du diplome, pend maintenant pres de la porte de la maison. Elle ne la lui a jamais rendue."

    systeme "Le petit carnet de croquis offert a Noel avait lui aussi fait le voyage. Il etait reste un carnet de croquis, avec des pages encore vides."
    if arc4_5_theo_proposition == "gestion_stream":
        systeme "A cote, un second carnet servait au planning du stream. La dette commencee par deux mots — « Bien sur » — avait maintenant des horaires, des couleurs et des rappels."
    elif arc4_5_theo_proposition == "question":
        systeme "A Noel, Ilona avait demande a Theo s'il voulait aider ou devenir celui qui aide. A Tokyo, il avait achete un second carnet pour le planning, comme si mieux separer les objets pouvait separer les deux intentions."
    elif arc4_5_theo_proposition == "temps":
        systeme "A Noel, Ilona avait demande du temps et refuse qu'on lui dise quoi vouloir. A Tokyo, un second carnet de planning avait transforme ce temps en cases colorees."
    else:
        systeme "Le carnet de planning etait venu plus tard, apres le depart. Theo appelait ce deuxieme carnet la partie concrete du reve."

    systeme "Pendant les deux premiers mois, elle a dormi avec le carnet de planning sur la table de nuit, comme un passeport."
    systeme "Au troisieme mois, elle l'a laisse plus souvent dans la cuisine, entre deux tasses et les notes de production des colocataires."
    systeme "Au cinquieme, elle a commence a le retourner face contre table les soirs ou elle ne voulait plus voir le lendemain. Theo l'a remarque des le premier matin."
    systeme "Il n'a rien demande. Il a allege deux rendez-vous, commande le petit dejeuner qu'elle prend quand elle a mal dormi, puis remis le carnet face visible."

    show theo tokyo reassuring at char_right
    show ilona tokyo neutral at char_left
    with dissolve

    t "Demain, on a le brief avec l'agence a dix heures, le tournage sponsor a quatorze, et ton stream le soir."
    i "Le tournage sponsor, c'etait pas jeudi ?"
    t "Ils ont avance. C'est une bonne nouvelle. Ca veut dire qu'ils te veulent vraiment."
    i "Ah."
    t "T'as dit « ah » comme mardi, quand t'avais plus l'energie de me dire que c'etait trop."
    t "J'ai deja raccourci le brief et refuse le diner apres le tournage. Tu n'auras qu'a rentrer, manger et lancer le stream."
    t "On arrive a un moment cle. Si on tient le rythme maintenant, apres on pourra respirer."

    if arc2_choix_activite_theo == "suivre":
        systeme "A la plage, Theo avait retrouve le porte-cles d'Ilona et indique le chemin le plus sur vers les mares. La promenade avait tourne court avant qu'ils les regardent vraiment. Il avait surtout retenu la facilite avec laquelle son attention lui donnait le role de celui qui protege."
    elif arc2_choix_activite_theo == "disparaitre":
        systeme "A la plage, Theo avait retrouve le porte-cles d'Ilona, puis l'avait accompagnee jusqu'aux mares. Quand elle lui avait demande ce qu'il voulait, il avait choisi de ne pas repondre. Tokyo est devenu la reponse qu'il n'avait pas donnee ce jour-la."
    else:
        systeme "A la plage, Theo avait retrouve le porte-cles d'Ilona, puis l'avait accompagnee jusqu'aux mares. Il s'etait excuse de croire savoir ce que les gens voulaient avant qu'ils finissent. Il avait appris la bonne phrase avant d'apprendre le bon geste."

    systeme "Apres. Le mot est doux. C'est pour ca qu'il passe si bien."

    show ilona tokyo fatigue at char_left
    with dissolve

    i "Et si j'ai besoin de respirer avant apres ?"
    t "Alors on ajuste."
    t "Mais on ne va pas laisser une semaine difficile casser ce que tu prepares depuis des mois. L'elan, c'est rare."

    systeme "Il a vu juste. Ilona est epuisee. Il a meme retire ce qui pouvait l'etre."
    systeme "Puis il a choisi, seul, ce qui devait rester. Avec Theo, etre comprise et etre conduite prennent souvent la meme voix."

    hide theo
    hide ilona
    with dissolve

    $ renpy.pause(0.4, hard=True)

    scene bg arc7 tokyo studio
    with fade

    systeme "Le soir, les locaux du studio prennent le relais. Pendant ces huit mois, la chance fragile devient une machine solide."
    systeme "Les miniatures changent. Les titres changent. La lumiere du studio ne change jamais."
    systeme "Ilona apprend a dire « coucou tout le monde » meme les soirs ou sa voix voudrait commencer par autre chose."
    systeme "Theo avait compris depuis longtemps qu'Ilona trouvait les choses plus faciles en ligne, quand personne ne voyait ses blancs. A Tokyo, presque toute sa vie se passe en ligne. Lui voit chacun de ses blancs et les remplit quand meme."

    if arc5_fin_minecraft == "theo_presence":
        systeme "Quelque part, sur un serveur qu'elle n'ouvre presque plus, la maison Minecraft garde un mot de passe qui n'a pas ete choisi par elle."
    elif arc6_offre_theo == "question":
        systeme "Dans le couloir, Theo avait admis qu'il voulait a la fois aider Ilona et l'avoir pres de lui. A Tokyo, les deux envies sont devenues impossibles a separer."
    elif arc6_offre_theo == "aveu_vide":
        systeme "Le studio avait d'abord ressemble a une reponse concrete. Il est maintenant la premiere question qui l'attend chaque matin."

    systeme "Les chiffres montent."
    systeme "Cent mille."
    systeme "Deux cent cinquante mille."
    systeme "Six cent mille."
    systeme "A chaque palier, Theo trouve le restaurant ou elle supportera encore le bruit, le tweet qu'elle n'aura pas besoin de reecrire, la bonne phrase pour les partenaires."
    systeme "A chaque palier, Ilona sourit sur les photos."

    if arc5_theo_proposition == "partiel":
        systeme "Avant meme le diplome, Theo avait propose de gerer une partie de sa vie alors qu'Ilona n'etait pas dans la piece. On ne lui avait concede que les notes. A Tokyo, le provisoire est devenu un emploi du temps entier."
    elif arc5_theo_proposition == "laisse":
        systeme "Avant meme le diplome, Theo avait dit : « Je gere. » Le projet d'Ilona avait change de mains alors qu'elle n'etait pas dans la piece. A Tokyo, il n'a plus besoin d'intermediaire."
    elif arc5_theo_proposition == "refuse":
        systeme "La premiere fois que Theo avait propose de gerer son quotidien, on avait appele ca une strategie. Lui avait repondu : de l'efficacite. A Tokyo, la meme efficacite a les cles de la maison."
    elif arc5_theo_proposition == "questionne":
        systeme "La premiere fois que Theo avait propose de gerer son quotidien, on lui avait demande pourquoi il ne parlait pas directement a Ilona. Pour Tokyo, il l'avait fait. Une offre directe n'etait pas forcement une offre neutre."

    systeme "Cette semaine-la, les deux autres colocataires preparent un tournage exterieur. Leurs caisses de materiel encombrent l'entree ; ils partiront avant l'aube le lendemain du million et ne rentreront que le jour suivant."

    $ renpy.pause(1.0, hard=True)

    systeme "Puis vient le million."
    systeme "Il est 23h passees."

    # ------------------------------------------------------------------
    # 2. Le stream, vu de l'exterieur puis vu d'elle
    # ------------------------------------------------------------------
    play music audio.stream loop volume 0.6

    systeme "Devant la camera, Ilona a troque le col roule gris du matin pour la veste bleue et les longs cheveux blancs que le public associe a IlonaGaming."

    show ilona streaming celebration at char_center
    with dissolve

    systeme "Un million d'abonnes atteint en huit mois. Les subs Twitch ne s'arretent plus."

    tchat "xXShadow_JPxX : ENFIN LE MILLION ILONA ON T'AIME"
    tchat "kiwi_no_kimi : gg gg gg gg"
    tchat "darkflame92 : elle a jamais autant stream que cette semaine respect"
    tchat "sakura_mod : on spam les coeurs pour elle svp"
    tchat "misterclip : best vtubeuse fr jp no debate"

    show ilona streaming smile at char_center
    with dissolve

    i "Merci a vous, sincerement... je suis trop contente de passer la soiree avec vous, j'ai grave kiffe ce stream."
    tchat "moon_walker21 : Ilona tu nous quittes jamais hein ??"
    i "Jamais !"

    systeme "Le mot sort trop vite. Il est parfait pour le tchat. Il est moins parfait pour elle."

    i "Bon... sur ce, gros bisous a tous, a demain pour un nouveau stream !"

    stop music fadeout 1.0
    show ilona streaming fatigue at char_center
    with dissolve
    systeme "Des que le stream coupe, son visage se decompose. Fatigue physique. Fatigue de l'autre genre, aussi."
    $ renpy.pause(1.0, hard=True)
    i "..."

    systeme "Sur le deuxieme ecran, les statistiques continuent de bouger. Meme eteint, le stream a encore l'air de demander quelque chose."

    if arc3_reaction_rumeur in ("blague_desarm", "silence_paralysie"):
        systeme "Au festival, Theo avait utilise une rumeur pour creer deux secondes de proximite avec Ilona. Il avait appris qu'une douceur pouvait entrer avec une facture quand elle arrivait au bon moment."
    else:
        systeme "Au festival, Ilona avait refuse la douceur de Theo quand elle arrivait avec une facture. Plus tard, il avait tout de meme utilise une verite comme une lame."
    systeme "Ce soir encore, Theo n'aura besoin de rien inventer : les chiffres, la fatigue et les contrats seront tous vrais."

    systeme "A Noel, Laplage avait prevenu Theo qu'un souvenir bien place pouvait ouvrir une porte ou enfermer quelqu'un. Theo avait repondu qu'il ne forcait personne a rester."
    systeme "Laplage avait conclu : « Non. Mais tu gardes la cle. » A Tokyo, Theo la garde toujours."

    # ------------------------------------------------------------------
    # 3. Theo entre, felicitations "professionnelles"
    # ------------------------------------------------------------------
    show theo tokyo reassuring at char_right
    with dissolve

    systeme "Theo entre avec un verre d'eau sans glacons. Ilona tousse quand elle boit trop froid apres un stream ; elle ne se souvient pas de le lui avoir dit. Lui, si."

    t "Un million. Ilona, je suis hyper fier de toi. Du travail comme le tien, ca ne se voit pas deux fois dans une carriere."
    i "Merci, Theo."
    t "T'as tenu deux heures quarante, t'as relance le tchat chaque fois que ca retombait, et personne n'a vu que t'avais mal a la gorge sur la fin."
    t "La chaine explose exactement comme je l'avais prevu. Les sponsors vont se battre pour toi."
    i "Ouais..."

    systeme "Theo voit ses doigts crispes autour du verre, le sourire tombe une demi-seconde trop tot, le « ouais » sans air derriere."
    systeme "Il voit la fatigue avant qu'elle trouve le mot. Son erreur n'est pas de la manquer. C'est de croire qu'il sait deja ce qu'elle signifie."

    show theo tokyo smirk at char_right
    with dissolve

    t "J'ai deja trois mails. Un casque, une boisson energisante, et une grosse marque qui veut une campagne sur six mois."
    i "Six mois ?"
    t "C'est enorme."
    i "C'est long."
    t "Long, oui. Mais stable. Plus besoin de te demander tous les matins si le mois prochain tient encore debout."
    t "Tu m'as dit que c'etait l'incertitude qui t'epuisait le plus. Avec ca, je peux enfin t'en enlever une partie."

    show ilona streaming fatigue at char_center
    with dissolve

    i "Theo."
    t "Hm ?"
    i "Quand tu dis « on », tu parles de qui ?"

    show theo tokyo neutral at char_right
    with dissolve

    t "De nous."
    i "De nous deux, ou de la chaine ?"
    t "Ilona..."
    t "La chaine, c'est pas un truc a cote de nous. C'est ce qu'on construit ensemble."

    i "Ton carnet de Noel, tu te souviens ? T'avais pris une phrase que j'avais dite a la plage et t'en avais fait un cadeau."
    t "Je voulais te montrer que je faisais attention."
    i "Tu fais attention. C'est pas le probleme. Le probleme, c'est que connaitre mes gouts, ca veut pas dire savoir ce que je veux."
    if arc4_reaction_cadeau_theo in ("blague_acide", "verite_crue"):
        i "Ce soir-la, je t'ai aussi dit que j'etais pas un trophee qu'on gagne avec des souvenirs bien places."
        t "Je sais."
    i "Alors pourquoi j'ai l'impression que plus tu me connais, moins tu me poses la question ?"

    systeme "Il appuie a peine sur « ensemble ». Juste assez pour rappeler les nuits, les billets, les mails et tout ce qu'il a porte sans qu'elle ait a le demander."
    systeme "Ilona hoche la tete. Elle voudrait que cette phrase lui fasse du bien. Une partie d'elle y arrive encore."

    systeme "Sur le quai du 6 avril, Theo lui avait demande si elle avait tout. Ilona avait repondu : « J'ai ce que j'ai decide de prendre. » Il se souvenait de chaque mot. Il n'avait pas compris qu'elle parlait deja du droit de choisir."

    systeme "Ils ne poursuivent pas la conversation au studio. Peu apres minuit, ils eteignent les ecrans, ferment les locaux et sortent enfin."

    hide ilona
    hide theo
    with dissolve

    scene black
    with fade

    systeme "La colocation n'est pas dans le meme batiment. Deux rues separent le studio de la maison ; ils les parcourent cote a cote, sans trouver quoi ajouter."

    scene bg arc7 tokyo house night
    with fade

    systeme "Quand ils entrent dans la piece commune, les autres colocataires dorment deja. Ilona pose son telephone pres du carnet de planning. Theo rallume la cuisine."

    show ilona tokyo fatigue at char_left
    show theo tokyo neutral at char_right
    with dissolve

    i "Theo, ca fait un moment que j'y pense... j'aimerais qu'on passe du temps, tous les deux. Une promenade dans un parc, un resto, un film, n'importe quoi."
    i "On n'a plus eu un seul moment rien qu'a nous depuis des semaines. Je me sens seule, alors que je suis censee etre entouree de mille personnes chaque soir. C'est idiot, dit comme ca."
    t "C'est pas idiot."
    t "Tu tires sur ta manche depuis tout a l'heure. Tu fais ca quand tu cherches comment demander quelque chose sans deranger."
    t "T'aurais pas du avoir besoin de chercher avec moi."
    t "On va se le prendre, ce moment. Promis. Juste... pas tout de suite, il y a encore beaucoup de boulot en ce moment."

    systeme "Une promesse de plus. Ilona a arrete de les compter."

    i "Demain apres-midi, alors ? On pourrait sortir a Tokyo, juste toi et moi. Ca me ferait vraiment du bien."

    show theo tokyo neutral at char_right
    with dissolve

    t "Demain apres-midi..."
    systeme "Il connait deja la reponse. Il sort quand meme son telephone : les cases colorees donnent a son refus l'air d'un fait exterieur."
    t "J'ai les sponsors a quinze heures."
    i "Tu peux deplacer ?"
    t "Je peux essayer."

    systeme "Ilona entend la difference entre « je vais » et « je peux essayer ». Elle aurait voulu ne pas l'entendre."

    i "Et le stream du soir ?"
    t "On peut le raccourcir."
    i "Ou l'annuler."

    show theo tokyo defensive at char_right
    with dissolve

    t "Annuler le soir du million, ce serait un mauvais signal."
    i "A qui ?"
    t "Aux gens. Aux marques. A l'algorithme."
    i "Et a moi ?"

    $ renpy.pause(1.0, hard=True)

    systeme "Theo ne commence pas a la regarder. Il la regardait deja."
    systeme "Il reprend mentalement le verre intact, la manche tiree, le mot « seule », et cherche la reponse qui pourra encore ressembler a une aide."

    # ------------------------------------------------------------------
    # Choix final : la reponse de Theo decide de la route
    # ------------------------------------------------------------------
    show theo tokyo defensive at char_right

    menu:
        "La reponse de Theo."

        "Annuler les sponsors, ecouter Ilona.":
            t "T'as raison. Les sponsors, ca peut attendre. Toi, c'est maintenant que ca compte."

            show ilona tokyo smile at char_left
            i "Tu es serieux ?"
            t "Serieux."
            t "J'annule demain apres-midi. Et le stream du soir. Je vais leur expliquer que tu as besoin de souffler."

            show theo tokyo neutral at char_right
            with dissolve

            i "Tu vois ?"
            t "Quoi ?"
            i "Je te demande du temps avec toi, et en dix secondes tu as deja decide ce que j'annule et ce que tu vas dire a ma place."

            show theo tokyo disappointed at char_right
            with dissolve

            t "J'essaie de te faciliter les choses."
            i "Je sais. Mais quand je refuse ta solution, tu le prends comme si je refusais tout ce que tu fais pour moi."

            systeme "Il pourrait lui rappeler les nuits sans dormir, les contrats traduits, les repas poses a cote du clavier avant meme qu'elle ait faim. Tout serait vrai."
            systeme "La liste monte jusqu'a sa gorge. Pour une fois, Theo ne s'en sert pas."

            t "D'accord. Qu'est-ce que tu veux que j'annule ?"
            i "Tout. Pour demain, tout. Et je veux ecrire le message moi-meme."
            t "D'accord."

            systeme "Le mot lui coute. Pas a cause des sponsors. Parce qu'il ne contient aucune direction."

            show ilona tokyo fatigue at char_left
            i "Theo... je crois que j'ai besoin de plus qu'une apres-midi."
            i "J'ai besoin de faire une vraie pause sur le stream. Revenir a un jeu plus casual. Ou faire autre chose, je sais pas encore. Mais arreter de me vider pour un million d'inconnus."

            show theo tokyo defensive at char_right
            with dissolve

            t "Une vraie pause, apres un million, ca peut faire disparaitre la moitie de ce qu'on a construit. Les marques ne vont pas attendre sans date, l'algorithme non plus. Ca me fait peur."
            i "Moi aussi."
            i "Mais si je continue comme ca, c'est moi qui disparais avant."

            $ renpy.pause(1.0, hard=True)

            show theo tokyo disappointed at char_right
            with dissolve

            t "J'allais te dire que j'avais porte toute la partie ingrate pour qu'on arrive jusque-la."
            t "Comme si ca te donnait l'obligation d'aimer l'endroit ou je nous ai conduits."
            t "J'ai peur que si on ralentit, tout disparaisse. Mais c'est ma peur. Pas ta consigne."
            i "Tu vas detester ca."
            t "Probablement."
            t "Mais je peux detester ca sans choisir a ta place. Je vais devoir apprendre."

            systeme "Theo a encore memorise chacune de ses hesitations. Il a encore envie d'en faire un plan."
            systeme "Mais pour la premiere fois, Ilona peut laisser un blanc sans qu'il le remplisse a sa place."
            systeme "Sur le quai, Ilona avait dit qu'elle emportait ce qu'elle avait decide de prendre. Cette fois, Theo comprend enfin que la decision comptait plus que la destination. Le silence reste ouvert jusqu'a ce qu'elle choisisse quoi en faire."

            hide ilona
            hide theo
            with dissolve

            jump ending_neutre

        "Prioriser les sponsors, la chaine avant tout.":
            t "Demain apres-midi, tu ne vas pas traverser Tokyo epuisee pour faire semblant de profiter d'un parc. Tu vas dormir. Moi, je vois les sponsors."
            t "A vingt heures, tu fais un stream court. Une heure, pas plus. Je te libere tout le reste."

            show theo tokyo reassuring at char_right
            with dissolve

            t "Ecoute, je sais que t'es fatiguee. Je le vois."
            systeme "Il le voit. C'est ce qui rend la phrase plus dure, pas moins."
            t "Tu as besoin de sommeil, de silence, et de ne pas avoir a prendre dix decisions ce soir. Pas de jeter six mois de securite parce que la journee etait trop longue."
            t "Laisse-moi porter la partie lourde encore un peu. Les mails, les rendez-vous, les contrats. Toi, tu fais ce que tu fais mieux que tout le monde."
            t "Apres cette vague, je te promets qu'on ralentit. J'ai toujours tenu mes promesses quand il fallait te proteger."

            show ilona tokyo fatigue at char_left
            with dissolve

            i "Apres."
            t "Oui."
            i "C'est toujours apres."

            show theo tokyo defensive at char_right
            with dissolve

            t "Parce qu'on est dedans maintenant. Et parce que je sais ce que ca t'a coute d'arriver la. J'etais la pour chaque nuit blanche, chaque mail, chaque fois ou tu voulais tout supprimer le lendemain d'un mauvais stream."
            t "Je t'ai evite de regretter ces soirs-la. Fais-moi confiance pour celui-ci aussi."

            i "Je comprends."

            systeme "Elle comprend vraiment. C'est ca, le piege. Une cage doree n'a pas besoin d'etre absurde pour fermer."
            systeme "Theo n'a invente ni sa fatigue, ni ses anciens regrets, ni tout ce qu'il a fait pour elle. Il a seulement range les faits dans l'ordre qui menait a sa reponse."

            if arc4_5_theo_proposition == "gestion_stream":
                systeme "Quand Ilona avait accepte que Theo gere le chat et le planning, deux mots avaient commence la dette : « Bien sur. » A Tokyo, la dette a une maison, un studio et six mois de contrats possibles."
            elif arc4_ilona_avec_theo:
                systeme "Elle s'etait deja demande si elle ne remplacait pas une cage par une autre. A l'epoque, la seconde avait l'air confortable. Elle l'est toujours. Mais une cage quand meme."

            i "Je vais me coucher, je suis crevee."
            t "Je sais. J'ai baisse le chauffage dans ta chambre et mis ton telephone en mode nuit."
            t "Vas-y, je te rejoins. Faut que je prepare la journee de demain avec les sponsors."
            t "On a fait tout ca ensemble, Ilona. Laisse pas une mauvaise soiree te faire croire le contraire. Bonne nuit."

            hide theo
            with dissolve

            systeme "Theo sort de la piece."
            play music audio.sadPiano loop volume 0.5 fadein 2.0
            i "..."
            systeme "Dans l'ecran noir de son telephone, son reflet reste pris entre le carnet de planning et les feuilles de production."
            systeme "Pendant quelques secondes, elle attend que quelqu'un dise son prenom sans le transformer en marque."
            systeme "Sa main se referme sur le porte-cles bloc que Theo avait retrouve a la plage. La premiere preuve qu'il faisait attention. Il fait toujours attention. C'est justement pour ca qu'elle ne sait plus comment lui echapper."
            $ renpy.pause(1.5, hard=True)

            scene black
            with fade
            stop music fadeout 2.0

            jump bad_ending
