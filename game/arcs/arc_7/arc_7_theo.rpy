# ARC VII - ROUTE THÉO
# Mapping depuis arc 6 :
#   controle_repetitif >= 3         -> entrée forcée ici
#   arc6_score < SEUIL_JESSY        -> entrée ici
#   confidences_laplage >= 3        -> sortie Laplage possible si influence basse
#   influence_theo                  -> poids de la route Théo
#   arc6_offre_theo                 -> manière dont l'offre de Théo s'est imposée
#   arc6_stylo                      -> présence et place du stylo à Tokyo
#   arcs 2-6                        -> ce que Théo a fait, observé ou appris
#                                      de la plage jusqu'au départ
# L'entrée se fait TOUJOURS via arc_6_bascule_theo (fin de arc_6_diplomes.rpy),
#
# Choix final (scènes déplacées depuis bad_ending.rpy) :
#   Théo écoute Ilona    -> jump ending_neutre (game/arcs/endings/ending_neutre.rpy)
#   Théo priorise le business -> jump bad_ending (game/arcs/endings/bad_ending.rpy)
# Remplace l'ancien dispatch par stats (ending_monsieur_laplage / ending_theo_vtuber),
# désormais mort code : ces deux labels restent en stub dans script.rpy si besoin
# de les réutiliser ailleurs.

# --- Personnage local (tchat Twitch, anonyme) ---
define tchat = Character("Tchat", color="#7fd6ff", callback=speaker_callback(""))

# --- Audio local ---
define audio.stream = "audio/music/ecole-nuit.ogg"

# --- Décors propres à la route Théo ---
image bg arc7 intro stream = im.Scale("images/scenes/arc_7/bg_arc7_intro_stream.jpg", 1920, 1080)
image bg arc7 tokyo studio = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_streaming_studio_night.jpg", 1920, 1080)
image bg arc7 tokyo morning = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_morning.jpg", 1920, 1080)
image bg arc7 tokyo house night = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_night.png", 1920, 1080)
image bg arc7 tokyo house night nolight = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_house_night_nolight.jpg", 1920, 1080)
image bg arc7 tokyo konbini night = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_konbini_night.png", 1920, 1080)
image bg arc7 tokyo arrival = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_arrival_station.jpg", 1920, 1080)
image bg arc7 tokyo restaurant = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_restaurant_night.jpg", 1920, 1080)
image bg arc7 tokyo park = im.Scale("images/scenes/arc_7/bg_arc7_tokyo_park_night.jpg", 1920, 1080)

# --- Tenues Tokyo propres à la route Théo ---
image ilona tokyo embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/awkward_embarrassment.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo neutral = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/neutral.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo smile = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/playful_warm_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo fatigue = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/quiet_fatigue.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona tokyo sad = speaker_sprite("ilona", "images/personnages/Ilona/tokyo/sad.png", ILONA_SIZE[0], ILONA_SIZE[1])

# À partir du 6 décembre, Ilona porte les cheveux courts hors stream.
image ilona short neutral = speaker_sprite("ilona", "images/personnages/Ilona/short_hair/neutral.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona short sad = speaker_sprite("ilona", "images/personnages/Ilona/short_hair/sad.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona short sad_alt = speaker_sprite("ilona", "images/personnages/Ilona/short_hair/sad_alt.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona short crying = speaker_sprite("ilona", "images/personnages/Ilona/short_hair/Crying.png", ILONA_SIZE[0], ILONA_SIZE[1])

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
# La même expression sert ici à une hésitation sincère, sans sous-entendre qu'elle est feinte.
image theo tokyo hesitant = speaker_sprite("theo", "images/personnages/Théo/tokyo/feigned_innocence.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo smirk = speaker_sprite("theo", "images/personnages/Théo/tokyo/knowing_smirk.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo neutral = speaker_sprite("theo", "images/personnages/Théo/tokyo/neutral.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo jealousy = speaker_sprite("theo", "images/personnages/Théo/tokyo/quiet_jalousy.png", 842, 1264, THEO_CROP_BOTTOM)
image theo tokyo reassuring = speaker_sprite("theo", "images/personnages/Théo/tokyo/reassuring_smile.png", 842, 1264, THEO_CROP_BOTTOM)

label arc_7_theo:
    $ derniere_route = "Route Théo"
    $ controle_repetitif = interruptions_ilona - interruptions_reparees

    scene black
    with fade

    systeme "Arc VII - Le monde après le départ."

    # Rappel lisible du point de bascule de l'arc 6, sans afficher de jauge.
    if controle_repetitif >= 3:
        systeme "À la fin du diplôme, ce ne sont pas les grandes erreurs qui ont tranché. Ce sont les petites coupures répétées."
    elif arc6_score < SEUIL_JESSY:
        systeme "À la fin du diplôme, il n'y avait pas assez d'espace autour d'Ilona pour qu'elle reste sans se réduire."
    else:
        systeme "La route a gardé une trace fausse. Quelque chose a été forcé avant d'arriver ici."

    if arc6_offre_theo == "laisse":
        systeme "Théo avait regardé le silence autour de son offre devenir une réponse. Il n'avait pas demandé à Ilona si elle avait choisi, ou simplement cessé de résister."
    elif arc6_offre_theo == "accusation":
        systeme "Quelqu'un avait nommé tout haut la place que Théo voulait dans le futur d'Ilona. Théo ne l'avait pas niée. Il avait seulement rangé cette envie derrière une opportunité réelle."
    elif arc6_offre_theo == "question":
        systeme "Dans le couloir, Ilona avait demandé à Théo s'il proposait une opportunité ou s'il lui demandait de venir avec lui. Il avait répondu : les deux."
    elif arc6_offre_theo == "aveu_vide":
        systeme "Ce jour-là, le studio, l'équipe et Tokyo avaient rempli tout l'espace de la conversation. Théo avait pris ce vide pour une preuve que son offre était la seule assez concrète."

    # ------------------------------------------------------------------
    # 1. Arrivée à Tokyo, colocation et premiers streams
    # ------------------------------------------------------------------

    scene bg arc7 tokyo arrival
    with fade

    systeme "Le 6 avril, les portes de la gare s'ouvrent sur Tokyo. Ilona s'arrête si brusquement que sa valise cogne l'arrière de ses jambes."

    show theo tokyo neutral at char_right
    show ilona tokyo embarrassed at char_left
    with dissolve

    i "C'est... beaucoup."
    t "La gare ?"
    i "La gare, les écrans, les gens, les immeubles... Comment ils savent tous où aller ?"
    t "Ils habitent ici."
    i "Argument injuste."

    systeme "Un flot de voyageurs les contourne. Ilona lève la tête vers un écran géant, puis vers un autre, et perd Théo de vue pendant une seconde. Sa main attrape aussitôt sa manche."

    t "Je suis là."
    i "Je savais. Je vérifiais la solidité de ton pull."
    t "Diagnostic ?"
    i "Acceptable. Ne marche pas aussi vite."
    t "Donne-moi ta valise."
    i "Elle pèse vingt-trois kilos."
    t "Vingt-deux virgule huit. Je l'ai pesée avant de partir."
    i "Bien sûr que tu as vérifié."

    show ilona tokyo smile at char_left
    with dissolve

    systeme "Dans la rue, Ilona photographie une enseigne, un distributeur de boissons et un taxi qu'elle trouve trop propre pour être réel. Théo attend chaque fois qu'elle s'arrête."

    i "On vit vraiment ici, maintenant ?"
    t "À deux rues du studio."
    i "Tu réponds avec une distance."
    t "Je réponds avec une information utile."
    i "Essaie avec de l'enthousiasme."
    t "On vit vraiment ici, maintenant."
    i "C'était terrible. Mais merci."

    hide theo
    hide ilona
    with dissolve

    systeme "Le trajet jusqu'à l'appartement prend vingt minutes et trois nouveaux arrêts photo. Pour Ilona, même se tromper de sortie ressemble encore au début d'une aventure."

    # ------------------------------------------------------------------
    # 1A. Leur appartement : le rêve commence
    # ------------------------------------------------------------------
    scene bg arc7 tokyo morning
    with fade

    systeme "Le studio a loué pour eux un appartement clair, avec deux chambres, une cuisine ouverte et un salon encore presque vide."

    show theo tokyo neutral at char_right
    show ilona tokyo neutral at char_left
    with dissolve

    i "Attends. Tout ça, c'est chez nous ?"
    t "Pour huit mois au moins. Si tout se passe bien, plus longtemps."
    i "Il y a un vrai salon."
    t "C'est souvent fourni avec l'appartement."
    i "Et une vraie cuisine."
    t "Je commence à m'inquiéter de l'endroit où tu vivais avant."

    show ilona tokyo smile at char_left
    with dissolve

    systeme "Ilona traverse chaque pièce comme si elle ouvrait des cadeaux. Elle teste le canapé, ouvre tous les placards et finit devant la fenêtre du salon."

    i "On voit les lumières de la rue."
    t "Et un morceau de la station, entre les deux immeubles."
    i "Le soir, ça va être magnifique."
    t "Le matin aussi, si tu te lèves assez tôt."
    i "N'abîme pas mon avenir avec des menaces."

    t "La chambre du fond est plus calme. Prends-la."
    i "Tu viens de monter ma valise devant l'autre."
    t "Je peux la redescendre."
    i "Non. Garde la chambre calme. Tu te lèves avant moi et tu parles au téléphone comme un présentateur du journal."
    t "Je ne parle pas comme un présentateur du journal."
    i "Bonjour Tokyo, aujourd'hui au programme : contrats, tableaux et café sans sucre."
    t "Mon imitation est meilleure."
    i "C'était une imitation de toi."
    t "J'avais compris. C'est ça qui est vexant."

    systeme "Ilona rit. La pièce cesse aussitôt de ressembler à un logement loué par une entreprise."

    i "Il nous faut des règles de colocation."
    t "Chacun sa chambre. On frappe avant d'entrer."
    i "Ou on envoie un message."
    t "Alors qu'on partage le même couloir ?"
    i "On a traversé des centaines de kilomètres pour vivre comme sur Discord. Respecte le concept."
    t "D'accord. Message avant intrusion."
    i "Et pas de réunion de travail pendant les repas."
    t "Ça me paraît raisonnable."
    i "Celui qui finit le café en rachète."
    t "Ça me paraît beaucoup plus dangereux."

    systeme "La régie vit dans une autre colocation, plus près de la gare. La cuisine et le salon ne sont qu'à Ilona et Théo. Pour Ilona, cette adresse n'est pas seulement pratique : c'est la première pièce d'une vie qu'elle a choisie."

    i "J'adore."
    t "L'appartement ?"
    i "L'appartement. Tokyo. Le fait qu'on soit là. Pour l'instant, j'adore tout."
    t "Alors ne défais pas toutes tes affaires."
    i "Pourquoi ?"
    t "Je dois encore te montrer le studio."
    i "Maintenant ?"
    t "Tu peux attendre demain."
    i "Absolument pas."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1B. La visite du studio
    # ------------------------------------------------------------------
    scene bg arc7 tokyo studio
    with fade

    systeme "Deux rues plus loin, Théo ouvre une porte insonorisée. Derrière, deux écrans, un micro suspendu et des panneaux de lumière attendent déjà Ilona."

    show theo tokyo reassuring at char_right
    show ilona tokyo embarrassed at char_left
    with dissolve

    i "C'est la pièce de qui ?"
    t "La tienne."
    i "Non, sérieusement."
    t "Sérieusement. La régie est derrière la vitre. Le monteur travaille dans la salle d'à côté. Et ça..."

    systeme "Théo allume les panneaux. Une lumière violette glisse sur le bureau."

    t "...c'est encore modifiable. On a gardé tes couleurs, mais tu pourras tout changer."
    i "Il y a mon pseudo sur l'écran."
    t "C'est plus pratique pour savoir qui doit s'asseoir là."
    i "Théo."
    t "Quoi ?"
    i "Laisse-moi être impressionnée correctement."

    show ilona tokyo smile at char_left
    with dissolve

    i "C'est incroyable."
    t "Tu commences demain soir."
    i "Demain, genre demain demain ?"
    t "C'est généralement ce que veut dire demain."
    i "Je pensais avoir une semaine pour paniquer."
    t "Tu peux paniquer ce soir. Demain, tu streams."
    i "Combien de personnes vont savoir que j'existe ?"
    t "Difficile à dire. L'équipe a préparé un teaser, quelques comptes partenaires vont le relayer et le compte du studio annoncera ton lancement demain matin."
    i "Vous avez déjà fait tout ça ?"
    t "On voulait que tu n'arrives pas devant une salle vide. Si tu préfères repousser, je peux encore leur dire."
    i "Non ! Enfin... non. Je veux le faire."
    t "Tu es sûre ?"
    i "Je vais être terrifiée. Mais je suis sûre."

    systeme "Ilona s'assoit, approche le micro et regarde son reflet dans l'écran encore noir. Pour la première fois, son projet ressemble à un vrai travail sans cesser de ressembler à son rêve."

    i "Tu crois que je peux dire quelque chose ?"
    t "Le micro est coupé."
    i "Je sais. C'est pour m'entraîner."
    t "Alors vas-y."
    i "Coucou tout le monde..."

    show ilona tokyo embarrassed at char_left
    with dissolve

    i "Non. C'était nul."
    t "C'était une phrase de quatre mots."
    i "Quatre mots nuls."
    t "Demain, tu en auras de meilleurs."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1C. Le premier stream
    # ------------------------------------------------------------------
    scene bg arc7 tokyo studio
    with fade

    systeme "Le lendemain soir, le compte à rebours descend devant plusieurs centaines de personnes. Ilona fixe le bouton qui doit la mettre en direct."

    show theo tokyo reassuring at char_right
    show ilona streaming smile at char_left
    with dissolve

    i "Il y a déjà huit cents personnes."
    t "Huit cent trente-deux."
    i "Ne rends pas le problème plus précis."
    t "Tu n'as pas besoin de leur plaire à tous. Parle à une personne. Puis à la suivante."
    i "Et si je bloque ?"
    t "Tu respires. La régie peut remplir dix secondes. Après, tu reprends."
    i "Tu restes derrière la vitre ?"
    t "Tout le long."

    systeme "Le compte à rebours atteint zéro. Théo rejoint la régie. Ilona inspire et ouvre le direct."

    hide theo
    show ilona streaming smile at char_center
    with dissolve
    play music audio.stream loop volume 0.45

    i "Coucou tout le monde... Bienvenue sur la première vraie soirée d'IlonaGaming."
    tchat "sakura_mod : BIENVENUE ILONA !!!"
    tchat "pixel_ramen : le setup est trop beau"
    tchat "misterclip : force pour le premier live"
    i "Vous êtes beaucoup trop nombreux. Je vais faire comme si vous étiez douze."
    tchat "kiwi_no_kimi : nous sommes tous douze ce soir"
    i "Parfait. Bonjour aux douze personnes réparties sur huit cents comptes."

    systeme "Les premières minutes tremblent. Puis Ilona rate le tutoriel d'un jeu qu'elle avait affirmé connaître, accuse la manette et oublie d'avoir laissé le micro ouvert pendant qu'elle cherche son chargeur. Le tchat transforme chaque erreur en blague."

    show ilona streaming joy at char_center
    with dissolve

    i "Je vous entends rire en texte, c'est vraiment humiliant."
    tchat "darkflame92 : LA MANETTE EST INNOCENTE"
    i "La manette sera jugée dans une procédure équitable."
    tchat "sakura_mod : pic à 2400 viewers !!!"
    i "Pardon ? Non, ne me dites pas les chiffres, j'étais presque détendue."

    systeme "Quand elle cesse de chercher la bonne façon de streamer, Ilona trouve la sienne. Deux heures passent plus vite que les cinq secondes avant le direct."

    i "Merci d'être restés pour ce premier stream. Je reviens très vite, avec une manette qui fonctionne. Ou du talent. Selon ce qu'on trouve en premier."

    stop music fadeout 1.0
    show ilona streaming smile at char_center
    with dissolve

    systeme "L'écran de fin apparaît. Ilona retire son casque et reste une seconde immobile, le sourire encore accroché au visage."

    systeme "La porte s'ouvre. Théo quitte la régie et entre dans la pièce pendant qu'Ilona essaie encore de comprendre ce qui vient de se passer."

    show theo tokyo reassuring at char_right
    with dissolve

    t "Alors ?"
    i "J'ai adoré."
    t "Même le tutoriel ?"
    i "Surtout le tutoriel. Deux mille personnes ont pris le parti d'une manette contre moi. C'est une communauté très saine."
    t "Pic à deux mille quatre cent dix-sept. Une excellente rétention, et le studio veut déjà découper trois extraits."
    i "Je comprends aucun des mots après deux mille."
    t "Ça veut dire que c'est un très bon début."
    i "Je veux recommencer demain."
    t "Pas demain. Tu dois dormir."
    i "C'est toi qui viens de me lancer avec vingt-quatre heures de préparation."
    t "Et maintenant, je protège mon investissement."
    i "Très romantique."

    systeme "Le mot leur échappe comme une plaisanterie. Aucun des deux ne le ramasse, mais Théo sourit en baissant les yeux vers les statistiques."

    i "Merci d'avoir fait venir du monde."
    t "L'équipe les a fait venir. Toi, tu les as fait rester."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1D. Leur premier soir après le stream
    # ------------------------------------------------------------------
    scene bg arc7 tokyo house night
    with fade

    systeme "Ils rentrent trop tard pour cuisiner. Deux boîtes de nouilles ouvertes sur la table basse deviennent leur premier repas dans le salon."

    show theo tokyo neutral at char_right
    show ilona tokyo smile at char_left
    with dissolve

    i "Première infraction au règlement."
    t "Laquelle ?"
    i "On parle du travail pendant le repas."
    t "Tu parles de ton stream depuis qu'on a quitté le studio."
    i "Je suis autorisée. C'est mon règlement."
    t "Très pratique."

    i "J'aimerais tester un jeu d'horreur. Et faire un stream dehors, un jour. Montrer Tokyo aux gens qui la connaissent pas."
    t "Pour l'extérieur, il faudra les autorisations, une connexion mobile fiable et probablement deux personnes de plus."
    i "C'était juste une idée."
    t "Les idées servent à devenir des projets."
    i "Laisse-la être une idée jusqu'à demain."

    show theo tokyo reassuring at char_right
    with dissolve

    t "D'accord. Jusqu'à demain."
    i "Et toi ? Tu nous vois où dans six mois ?"
    t "Avec une chaîne installée, une équipe stable et assez de revenus pour que tu choisisses vraiment ce que tu veux faire."
    i "Moi, je nous vois avec un tapis. Le salon fait vide."
    t "Mes objectifs sont peut-être un peu plus ambitieux."
    i "Tu sous-estimes la puissance d'un bon tapis."
    t "Alors une chaîne installée et un tapis."
    i "Là, je signe."

    systeme "Ils trinquent avec deux canettes achetées en bas. Pour Ilona, l'avenir tient dans une pièce encore vide, un studio à deux rues et la certitude nouvelle qu'elle a eu raison de venir."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1E. Dix jours plus tard : l'invitation
    # ------------------------------------------------------------------
    systeme "Pendant dix jours, ils apprennent le quartier et leur rythme. Théo frappe avant d'entrer. Ilona laisse parfois une tasse devant sa porte quand il travaille trop tard. Les streams rassemblent désormais entre mille cinq cents et trois mille spectateurs ; l'extrait de la manette, lui, circule bien au-delà des directs. Le salon gagne un tapis et plusieurs cartons restent fermés."

    show theo tokyo neutral at char_right
    show ilona tokyo neutral at char_left
    with dissolve

    systeme "Le dixième soir, Ilona est assise par terre devant la table basse, occupée à choisir quel extrait du premier stream elle déteste le moins. Théo relit trois fois le même message sur son téléphone."

    i "Tu sais que ton écran est éteint ?"
    t "Oui."
    i "Tu le fixes depuis une minute."
    t "Je réfléchis."
    i "Ça a l'air grave."
    t "Tu fais quelque chose ce soir ?"
    i "Je vis ici. Tu connais probablement mieux mon planning que moi."
    t "Justement. Tu es libre."
    i "Pourquoi ?"
    t "Je connais un bon restaurant."
    i "C'est professionnel ?"
    t "Non. Enfin... j'aimerais que ça ne le soit pas."

    show ilona tokyo embarrassed at char_left
    with dissolve

    i "D'accord."
    t "D'accord oui, ou d'accord tu as compris la phrase ?"
    i "D'accord, emmène-moi manger avant que tu recommences à réfléchir."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1F. Le trajet et le restaurant
    # ------------------------------------------------------------------
    scene bg arc7 tokyo konbini night
    with fade

    systeme "Dix jours plus tôt, Tokyo obligeait Ilona à regarder partout à la fois. Ce soir, elle reconnaît déjà le konbini, le feu trop long et la ruelle qui ramène chez eux. Théo, lui, vérifie l'heure pour la troisième fois."

    show theo tokyo neutral at char_right
    show ilona tokyo smile at char_left
    with dissolve

    i "On va rater la réservation ?"
    t "Non."
    i "Alors pourquoi tu regardes l'heure toutes les trente secondes ?"
    t "Je ne la regarde pas toutes les trente secondes."
    i "Tu as raison. La dernière fois, c'était vingt."
    t "J'aime être à l'heure."
    i "Tu parles aussi beaucoup plus que d'habitude."
    t "Tu veux que je me taise ?"
    i "Non. Je veux profiter du phénomène."

    hide theo
    hide ilona
    with dissolve

    scene bg arc7 tokyo restaurant
    with fade

    systeme "Le restaurant est petit et presque vide. Leur table est au fond de la salle, sous une lampe basse, assez loin de la cuisine pour qu'ils puissent parler sans hausser la voix."

    show theo tokyo neutral at char_right
    show ilona tokyo neutral at char_left
    with dissolve

    i "Tu avais vraiment réservé."
    t "On a marché vingt minutes pour venir. J'allais pas prendre le risque de manger debout."
    i "On aurait pu choisir au hasard."
    t "Tu détestes choisir au hasard quand tu as faim."
    i "Je déteste surtout attendre pendant que tu compares douze avis."
    t "J'en ai lu quatre."
    i "C'est déjà trois de trop."

    systeme "Ilona ouvre le menu, le referme, puis le retourne comme si une traduction pouvait apparaître au dos."

    t "Tu comprends quelque chose ?"
    i "Le prix. Et peut-être le mot poulet."
    t "Je reconnais le riz."
    i "Parfait. Un poulet hypothétique avec du riz presque certain."

    show ilona tokyo smile at char_left
    with dissolve

    systeme "Ils commandent en montrant deux photos. Pendant le repas, ils parlent du quartier, du tapis et de tout ce qui n'a pas besoin de devenir un projet. Théo laisse passer deux occasions de dire ce qu'il a préparé."

    i "Tu es bizarre, ce soir."
    t "Merci."
    i "C'était pas un compliment."
    t "J'avais compris."
    i "Tu voulais me parler de quelque chose ?"

    show theo tokyo hesitant at char_right
    show ilona tokyo embarrassed at char_left
    with dissolve

    t "Je veux pas faire comme si le train, l'appartement ou le studio avaient répondu à notre place."
    i "Répondu à quoi ?"
    t "À nous."
    i "C'est très précis."
    t "Ilona... est-ce que tu veux sortir avec moi ? Pour de vrai."

    systeme "Il ne parle ni de la chaîne, ni de ce qu'ils pourraient construire. Sans planning devant lui, Théo a l'air moins sûr de lui qu'au studio."

    i "Tu veux dire sortir maintenant ? Parce que techniquement, c'est déjà ce qu'on fait."
    t "Tu sais très bien ce que je veux dire."
    i "Oui, mais tu as l'air tellement stressé que j'en profite un peu."
    t "C'est cruel."
    i "Un peu."
    t "Alors ?"

    systeme "Théo garde les yeux sur elle. Toute l'assurance qu'il avait en réservant la table s'est arrêtée au bord de la question."

    show ilona tokyo smile at char_left
    with dissolve

    i "Alors oui. J'en ai envie."
    t "Oui ?"
    i "Oui, Théo. Je veux sortir avec toi."

    show theo tokyo reassuring at char_right
    with dissolve

    systeme "Ses épaules se relâchent enfin. Son sourire arrive avant les mots."

    t "D'accord."
    i "C'est tout ?"
    t "Non. Je suis heureux. Vraiment. J'arrive juste plus à retrouver la phrase que j'avais préparée."
    i "Tu avais préparé une phrase ?"
    t "J'avais surtout préparé ce que je dirais si tu refusais."
    i "Et si j'acceptais ?"
    t "Apparemment, rien."
    i "Pour une fois que tu n'as pas de plan."

    systeme "Ilona rit. Théo aussi, avec une seconde de retard, comme s'il venait seulement de comprendre qu'il pouvait respirer."

    i "Je veux juste qu'on garde une différence entre le travail et nous."
    t "D'accord."
    i "Tu réponds vite."
    t "Parce que je veux vraiment que ça marche. Au travail, tu peux me dire non."
    i "Je peux déjà te dire non."
    t "Oui. Mauvaise formulation. Je dois entendre ton non. Même si on sort ensemble."
    i "Là, c'est mieux."

    systeme "Deux petites coupes glacées arrivent entre eux. Ilona attend que le serveur reparte."

    i "Tu peux m'embrasser, si tu veux."
    t "Maintenant ?"
    i "C'était l'idée."
    t "Le dessert va fondre."
    i "Il survivra."

    systeme "Leur premier baiser a le goût d'un dessert qu'aucun des deux ne parvient ensuite à finir. Ils quittent le restaurant après la fermeture, officiellement ensemble et incapables de parler d'autre chose."

    scene bg arc7 tokyo house night
    with fade

    show theo tokyo reassuring at char_right
    show ilona tokyo smile at char_left
    with dissolve

    # ------------------------------------------------------------------
    # 1G. Le retour du restaurant
    # ------------------------------------------------------------------
    i "Je crois que je vais garder cette soirée dans mon top trois."
    t "Seulement troisième ?"
    i "Je laisse deux places libres pour te motiver."
    t "La pression commence tôt."
    i "Tu savais dans quoi tu t'engageais."

    systeme "Ilona abandonne ses chaussures près du canapé et se laisse tomber au milieu des coussins, encore trop heureuse pour avoir envie de dormir."

    t "On regarde quelque chose avant de se coucher ?"
    i "Tu proposes vraiment un film à cette heure-ci ?"
    t "Kung Pow."
    i "C'est quoi ?"
    t "Un film impossible à expliquer sans le rendre moins bien."
    i "Cette phrase ressemble à une menace."
    t "Tu me fais confiance ?"
    i "Depuis environ quarante minutes, officiellement."

    show theo tokyo smirk at char_right
    with dissolve

    t "Alors Kung Pow."
    i "D'accord. Mais si c'est nul, notre relation aura duré moins longtemps que le film."
    t "Risque accepté."

    systeme "Ils lancent le film avec le volume trop bas pour les voisins. Ilona rit d'abord de Théo qui connaît certaines répliques, puis du film lui-même. Aucun des deux ne regarde l'heure."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1H. Le lendemain : dix mille abonnés
    # ------------------------------------------------------------------
    scene bg arc7 tokyo studio
    with fade
    play music audio.stream loop volume 0.5

    systeme "Le lendemain soir, Ilona arrive en direct avec une énergie que ni le manque de sommeil ni le café ne suffisent à expliquer. Pendant le stream, le compteur franchit les dix mille abonnés."

    show ilona streaming celebration at char_center
    with dissolve

    i "Attendez... On vient vraiment de passer les dix mille ?"
    tchat "sakura_mod : 10K 10K 10K !!!"
    tchat "pixel_ramen : ELLE EST INARRÊTABLE CE SOIR"
    i "Je suis parfaitement normale. C'est vous qui avez l'air lents."
    tchat "kiwi_no_kimi : quelqu'un a gagné au loto hier"
    i "Pas du tout. J'ai juste passé une très bonne soirée."
    tchat "misterclip : CE SOURIRE EST SUSPECT"
    i "On se concentre sur les dix mille et on ne mène aucune enquête, merci."

    systeme "Elle enchaîne les parties, improvise un défi supplémentaire et oublie deux fois de regarder l'heure. Sa joie passe dans sa voix avant même que le tchat comprenne d'où elle vient."

    i "Merci pour les dix mille. Je pensais pas dire ce nombre aussi vite. On se retrouve au prochain stream !"

    stop music fadeout 1.0
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1I. Se retrouver après leurs journées
    # ------------------------------------------------------------------
    scene bg arc7 tokyo house night
    with fade

    show theo tokyo neutral at char_right
    show ilona tokyo smile at char_left
    with dissolve

    t "Dix mille."
    i "Tu regardais ?"
    t "Entre deux appels. Tu as débordé de vingt-sept minutes."
    i "Je préfère retenir la première partie de ta phrase."
    t "Tu as été excellente."
    i "Là, tu peux continuer."

    systeme "Ilona s'assoit près de lui. Pendant quelques minutes, ils échangent les morceaux ordinaires de leurs journées : une machine à café en panne, un train manqué et une blague du tchat que Théo n'a pas comprise."

    i "Et toi ? À part espionner mes horaires ?"
    t "Deux réunions. Une avec le studio, une avec une agence. Et j'ai mangé un sandwich tellement sec qu'il avait probablement un contrat avec eux."
    i "Journée difficile."
    t "Elle peut encore s'améliorer."
    i "Comment ?"
    t "On va marcher dans le parc."
    i "Maintenant ?"
    t "Tu as encore trop d'énergie pour dormir et moi, j'ai besoin de voir autre chose qu'un écran."
    i "Tu viens de proposer une activité sans ouvrir ton planning ?"
    t "Ne rends pas le moment bizarre."
    i "Trop tard. Je prends ma veste."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1J. La promenade et l'avertissement de Laplage
    # ------------------------------------------------------------------
    scene bg arc7 tokyo park
    with fade

    systeme "Le parc est presque vide. Les lampes dessinent un chemin pâle entre les arbres et le bruit de la ville arrive assourdi jusqu'à eux."

    show theo tokyo reassuring at char_right
    show ilona tokyo smile at char_left
    with dissolve

    i "Dix mille personnes."
    t "Abonnées. Elles ne seront jamais toutes là en même temps."
    i "Merci de réduire mon vertige avec des statistiques."
    t "C'est un service."
    i "Et si ça continue ?"
    t "On agrandit l'équipe. On améliore le studio. Tu choisis des projets plus ambitieux."
    i "Tu as déjà tout imaginé."
    t "Seulement les six prochains mois."
    i "Seulement."

    systeme "Une silhouette assise sur un banc lève vers eux un gobelet de café. Ilona ralentit la première."

    show laplage neutral at char_center
    with dissolve

    i "Monsieur Laplage ?"
    laplage "Bonsoir, Ilona. Théo."
    t "Qu'est-ce que vous faites à Tokyo ?"
    laplage "Je marche surtout entre les endroits. Tokyo en est un."
    i "Ça ne répond absolument pas à la question."
    laplage "Je voyage léger. Les réponses prennent beaucoup de place."

    show theo tokyo neutral at char_right
    with dissolve

    t "On allait continuer notre promenade."
    laplage "Alors continuez. Les promenades sont utiles quand personne ne choisit la destination pour l'autre."
    i "C'est une mise en garde ?"
    laplage "Une précaution. Les débuts heureux donnent envie de remplir tous les jours qui suivent."
    t "On va bien."
    laplage "Je le vois. C'est souvent quand tout va bien qu'on oublie de laisser une place au rien."
    i "Une place au rien ?"
    laplage "Une soirée sans objectif. Une idée qui ne devient pas un projet. Un non qui ne demande pas d'explication."

    systeme "Théo ne répond pas. Ilona pense au stream dehors, devenu en quelques secondes une liste d'autorisations. Ce souvenir ne lui fait pas encore mal. Il accroche seulement quelque part."

    laplage "Le bonheur peut parler très fort. Vérifiez seulement qu'il ne répond pas à votre place."
    i "Vous faites toujours ça ? Apparaître, dire quelque chose d'inquiétant et repartir ?"

    show laplage thumb_up at char_center
    with dissolve

    laplage "Pas toujours. Parfois, je vends des boissons."

    hide laplage
    with dissolve

    show ilona tokyo neutral at char_left
    with dissolve

    i "Il est vraiment venu jusqu'à Tokyo pour nous dire de ne rien faire."
    t "On peut ignorer le conseil."
    i "Pas ce soir."
    t "Tu veux rentrer ?"
    i "Non. Je veux finir la promenade. Sans destination."
    t "D'accord."

    systeme "Ils reprennent le chemin le plus long autour du parc. Théo ne consulte pas son téléphone. Ilona lui prend la main. L'avertissement reste derrière eux, sur un banc qui est vide lorsqu'elle se retourne."

    hide theo
    hide ilona
    with dissolve

    scene bg arc7 tokyo house night nolight
    with fade

    systeme "Pendant le premier mois, ils arrivent encore à séparer le stream et leur vie de couple : ramen après les directs, promenades au parc et séries regardées trop tard dans le salon."
    systeme "Puis un rendez-vous avec un sponsor remplace une promenade. Une VOD urgente fait sauter un dîner. Théo dit « on se rattrape demain », et demain arrive avec un nouveau mail."

    scene bg arc7 tokyo studio
    with fade

    # ------------------------------------------------------------------
    # 1K. Juin : cent mille abonnés
    # ------------------------------------------------------------------
    systeme "En juin, les extraits courts et les apparitions sur les chaînes partenaires touchent bien plus de monde que les directs. Ceux-ci réunissent maintenant six à huit mille spectateurs réguliers. Deux mois après le lancement, le compteur atteint cent mille abonnés en direct."

    play music audio.stream loop volume 0.5
    show ilona streaming victory at char_center
    with dissolve

    i "Cent mille... Vous êtes complètement malades."
    tchat "sakura_mod : ON L'A FAIT !!!"
    tchat "darkflame92 : 100K EN DEUX MOIS C'EST FOU"
    tchat "kiwi_no_kimi : discours discours discours"
    i "J'ai pas de discours. J'avais préparé quelque chose pour cinquante mille et vous m'avez même pas laissé le temps."
    tchat "misterclip : pleure pas ilona sinon on pleure"
    i "Je pleure pas. C'est la lumière violette qui attaque mes yeux."

    show ilona streaming celebration at char_center
    with dissolve

    i "Merci d'être là. Merci d'avoir transformé mes problèmes de manette en carrière. Je vous promets qu'on va continuer à faire des trucs incroyables ensemble."

    stop music fadeout 1.0
    show ilona streaming smile at char_center
    with dissolve

    systeme "Le direct coupe sur son sourire. Quelques secondes plus tard, Théo entre dans la pièce avec son téléphone à la main."

    show theo tokyo reassuring at char_right
    with dissolve

    t "Cent mille."
    i "Attends, actualise."
    t "Je viens de le faire."
    i "Encore. Ça peut être un bug."
    t "Tu veux que quatre mille personnes se désabonnent pour rendre le chiffre plus crédible ?"
    i "Deux mille suffiraient. Je suis pas exigeante."
    t "Regarde-moi. T'as réussi. Je suis fier de toi."
    i "Merci."
    t "Et j'ai un cadeau."

    show ilona streaming joy at char_center
    with dissolve

    i "Un cadeau ?"
    t "Une opération spéciale la semaine prochaine avec une grande marque. Deux heures de direct, le jeu en avant-première et une campagne sur leurs réseaux. J'ai obtenu leur meilleur tarif."

    show ilona streaming fatigue at char_center
    with dissolve

    i "Ah."
    t "C'est énorme, Ilona. Ils ont refusé deux chaînes plus anciennes pour te prendre."
    i "Non, oui. C'est super. Merci."
    t "Tu as dit merci comme si je venais de t'offrir une facture."
    i "Je pensais juste... Je sais pas ce que je pensais."
    t "On fêtera les cent mille tous les deux. Je connais un restaurant que tu vas adorer."
    i "Quand ?"
    t "Dès que l'opération est passée. Promis."

    systeme "Le cadeau est réel. L'opportunité aussi. Ilona voudrait réussir à les recevoir sans chercher ce qui, là-dedans, a été choisi pour elle plutôt que pour la chaîne."

    t "Je dois te laisser. J'ai des mails à envoyer et deux réunions à préparer pendant que les chiffres sont encore chauds."
    i "Tu rentres avec moi ?"
    t "Plus tard. Le dîner est déjà prêt dans le frigo. Tu n'auras rien à faire."
    i "À part le réchauffer."
    t "Deux minutes trente. J'ai testé."
    i "Bien sûr que tu as testé."
    t "Je t'écris quand je pars."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1L. Le repas qui attend
    # ------------------------------------------------------------------
    scene bg arc7 tokyo house night
    with fade

    systeme "À l'appartement, Ilona mange seule devant le film qu'ils avaient promis de regarder ensemble. Elle ne le lance pas."

    show ilona tokyo neutral at char_center
    with dissolve

    i "Tu rentres vers quelle heure ?"
    systeme "Le message reste lu pendant trois minutes. Puis la réponse de Théo apparaît."
    t "J'en ai encore pour un moment. Ne m'attends pas, je vais sûrement rentrer très tard."
    i "D'accord."
    t "Je te rejoins au lit dès que j'ai fini. Et encore bravo pour ce soir."
    i "Merci. Bon courage."

    show ilona tokyo fatigue at char_center
    with dissolve

    systeme "Ilona pose le téléphone face visible sur la table basse. Au bout d'une heure, elle lance le générique du film. Au bout de deux, elle ne regarde plus que les reflets de l'écran sur le plafond."
    systeme "Quand Théo rentre, elle dort sur le canapé. L'assiette vide est restée devant elle et le film attend toujours qu'on appuie sur lecture."

    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 1M. La semaine suivante : l'opération spéciale
    # ------------------------------------------------------------------
    scene bg arc7 tokyo studio
    with fade
    play music audio.stream loop volume 0.55

    systeme "La semaine suivante, l'opération spéciale dépasse les deux heures prévues. Ilona recommence une partie pour tenir une promesse faite au tchat, puis accepte un dernier défi alors que sa voix fatigue."

    show ilona streaming victory at char_center
    with dissolve

    i "Dernière tentative. Cette fois, on gagne pour de vrai."
    tchat "pixel_ramen : ça fait quatre dernières tentatives"
    i "Les trois premières étaient administratives."
    tchat "sakura_mod : le sponsor vient d'offrir 100 subs !!!"
    i "Merci ! Bon, maintenant je suis contractuellement obligée de réussir."

    systeme "Elle réussit. Le tchat explose, la marque publie déjà un extrait et la régie lui fait signe que les retours sont excellents."

    i "Merci à tous. C'était intense, mais j'ai adoré découvrir le jeu avec vous. Maintenant, je vais dormir environ trois jours."

    stop music fadeout 1.0
    show ilona streaming fatigue at char_center
    with dissolve

    systeme "Dès que le direct coupe, Ilona laisse retomber ses épaules. Ces derniers jours, chaque succès semble ajouter une nouvelle case au planning avant de lui laisser le temps de souffler."

    hide ilona
    with dissolve

    scene bg arc7 tokyo house night
    with fade

    # ------------------------------------------------------------------
    # 1N. Le film qui attend encore
    # ------------------------------------------------------------------
    show theo tokyo reassuring at char_right
    show ilona tokyo fatigue at char_left
    with dissolve

    t "Le sponsor est ravi. Ils parlent déjà d'une deuxième opération."
    i "J'ai bien aimé. Vraiment. Mais je suis lessivée."
    t "Ça ne s'est pas vu. Tu as tenu le rythme jusqu'à la fin."
    i "Justement, maintenant j'aimerais ne plus tenir de rythme du tout."
    t "Repos mérité."
    i "On pourrait regarder Shaolin Soccer. Tous les deux, sans téléphone."
    t "Tu veux encore tester la solidité de notre relation avec un film impossible à expliquer ?"
    i "Kung Pow a survécu. Nous aussi."
    t "C'est bien celui avec du kung-fu et du football ?"
    i "Oui. Un documentaire très sérieux sur le sport de haut niveau."
    t "Je ne crois pas que le mot documentaire veuille dire ce que tu crois."
    i "Il y a des équipes, un ballon et des ralentis. C'est scientifiquement suffisant."
    t "Ce soir ?"
    i "C'était l'idée."

    show theo tokyo neutral at char_right
    with dissolve

    t "Ça va être compliqué. Je pars en déplacement très tôt demain matin. Il faut que je dorme si je veux être en état."
    i "Tu me l'avais dit ?"
    t "C'était dans le planning commun."
    i "Ah."
    t "Toi aussi, tu as besoin de dormir. On mange et on va se coucher ?"
    i "Oui. D'accord."

    systeme "Théo réchauffe le repas pendant qu'Ilona range le téléphone qui devait servir à lancer le film. Après avoir mangé, ils vont se coucher."

    hide theo
    hide ilona
    with dissolve

    scene bg arc7 tokyo house night
    with fade

    systeme "Huit mois après le départ, ils vivent toujours dans la même maison et sortent toujours ensemble. Mais la chaîne est devenue leur travail, leur sujet de conversation et, trop souvent, leur seule activité à deux."
    systeme "Pendant les deux premiers mois, Ilona a dormi avec le carnet de planning sur la table de nuit, comme un passeport."
    systeme "Au troisième mois, elle l'a laissé plus souvent dans la cuisine, entre deux tasses et les notes de production."
    systeme "Au cinquième, elle a commencé à le retourner face contre table les soirs où elle ne voulait plus voir le lendemain. Théo l'a remarqué dès le premier matin."
    systeme "Il n'a rien demandé. Il a allégé deux rendez-vous, commandé le petit déjeuner qu'elle prend quand elle a mal dormi, puis remis le carnet face visible."

    scene black
    with fade

    systeme "Le 6 décembre, IlonaGaming est devenue un succès national. Les propositions arrivent chaque jour ; la charge de travail a grandi plus vite que l'espace disponible pour la porter."

    scene bg arc7 tokyo morning
    with fade

    systeme "Ce matin-là, la lumière blanche remplit la pièce commune. Sur la table, les tasses et les feuilles de production entourent le carnet de planning."

    # Le dernier emplacement du stylo est fixé par la décision de l'arc 6.
    if arc6_stylo == "garde":
        systeme "En défaisant ses affaires, Ilona n'avait trouvé aucun stylo violet. Il n'avait pas fait le voyage jusqu'à Tokyo."
    elif arc6_stylo == "rendu_explique":
        systeme "Le stylo violet avait voyagé dans la poche extérieure de son sac. Ilona l'y avait laissé plusieurs semaines : trop chargé pour redevenir tout de suite un objet ordinaire."
    elif arc6_stylo == "rendu":
        systeme "Le stylo violet avait voyagé dans la poche extérieure de son sac. Le premier matin, Ilona l'avait remis dans sa trousse. Depuis, il écrit comme les autres."
    elif arc6_stylo == "blague":
        systeme "Le stylo violet avait voyagé dans la poche extérieure de son sac. La blague du pain au lait n'avait pas voyagé avec lui."

    if souvenirs["ilona_veut_streamer_serieusement"]:
        systeme "Ilona avait dit un jour qu'elle voulait streamer sérieusement. Théo a pris cette phrase au sérieux. Peut-être plus qu'elle."

    if arc4_ilona_avec_theo:
        systeme "Au début, c'était reposant. Quelqu'un qui réserve, qui prévoit, qui sait toujours où il faut être et à quelle heure."
        systeme "L'écharpe de Théo, restée dans le sac d'Ilona le jour du diplôme, pend maintenant près de la porte de la maison. Elle ne la lui a jamais rendue."

    systeme "Le petit carnet de croquis offert à Noël avait lui aussi fait le voyage. Il était resté un carnet de croquis, avec des pages encore vides."
    if arc4_5_theo_proposition == "gestion_stream":
        systeme "À côté, un second carnet servait au planning du stream. La dette commencée par deux mots — « Bien sûr » — avait maintenant des horaires, des couleurs et des rappels."
    elif arc4_5_theo_proposition == "question":
        systeme "À Noël, Ilona avait demandé à Théo s'il voulait aider ou devenir celui qui aide. À Tokyo, il avait acheté un second carnet pour le planning, comme si mieux séparer les objets pouvait séparer les deux intentions."
    elif arc4_5_theo_proposition == "temps":
        systeme "À Noël, Ilona avait demandé du temps et refusé qu'on lui dise quoi vouloir. À Tokyo, un second carnet de planning avait transformé ce temps en cases colorées."
    else:
        systeme "Le carnet de planning était venu plus tard, après le départ. Théo appelait ce deuxième carnet la partie concrète du rêve."

    show theo tokyo neutral at char_right
    show ilona short sad at char_left
    with dissolve

    i "Tu as commandé le petit déjeuner ?"
    t "Les pancakes arrivent dans cinq minutes. Sans melon."
    i "Je t'ai jamais dit que j'aimais pas le melon."
    t "Tu le laisses toujours au bord de l'assiette."
    i "C'est un fruit qui a le goût d'eau parfumée."
    t "Je note l'argument pour la prochaine commande."

    systeme "Théo pose le téléphone, prend le carnet retourné et le remet face visible entre eux."

    i "Je l'avais mis comme ça exprès."
    t "Je sais."
    i "Alors pourquoi tu le retournes ?"
    t "Parce que j'ai déjà enlevé ce qui pouvait l'être. Regarde."

    show theo tokyo reassuring at char_right
    show ilona short sad_alt at char_left
    with dissolve

    t "Demain, on a le brief avec l'agence à dix heures, le tournage sponsor à quatorze, et ton stream le soir."
    i "Le tournage sponsor, c'était pas jeudi ?"
    t "Ils ont avancé. C'est une bonne nouvelle. Ça veut dire qu'ils te veulent vraiment."
    i "Ah."
    t "T'as dit « ah » comme mardi, quand t'avais plus l'énergie de me dire que c'était trop."
    t "J'ai déjà raccourci le brief et refusé le dîner après le tournage. Tu n'auras qu'à rentrer, manger et lancer le stream."
    i "Tu as enlevé quoi ?"
    t "Un essayage et une interview."
    i "Je savais même pas qu'ils étaient prévus."
    t "Justement. Tu n'as pas eu à t'en occuper."
    t "On arrive à un moment clé. Si on tient le rythme maintenant, après on pourra respirer."

    if arc2_choix_activite_theo == "suivre":
        systeme "À la plage, Théo avait retrouvé le porte-clés d'Ilona et indiqué le chemin le plus sûr vers les mares. La promenade avait tourné court avant qu'ils les regardent vraiment. Il avait surtout retenu la facilité avec laquelle son attention lui donnait le rôle de celui qui protège."
    elif arc2_choix_activite_theo == "disparaitre":
        systeme "À la plage, Théo avait retrouvé le porte-clés d'Ilona, puis l'avait accompagnée jusqu'aux mares. Quand elle lui avait demandé ce qu'il voulait, il avait choisi de ne pas répondre. Tokyo est devenu la réponse qu'il n'avait pas donnée ce jour-là."
    else:
        systeme "À la plage, Théo avait retrouvé le porte-clés d'Ilona, puis l'avait accompagnée jusqu'aux mares. Il s'était excusé de croire savoir ce que les gens voulaient avant qu'ils finissent. Il avait appris la bonne phrase avant d'apprendre le bon geste."

    systeme "Dans le parc, Monsieur Laplage leur avait conseillé de garder une place au rien. Le carnet de planning n'en contient plus."
    systeme "Après. Le mot est doux. C'est pour ça qu'il passe si bien."

    show ilona short sad at char_left
    with dissolve

    i "Et si j'ai besoin de respirer avant après ?"
    t "Alors on ajuste."
    t "Mais on ne va pas laisser une semaine difficile casser ce que tu prépares depuis des mois. L'élan, c'est rare."

    systeme "Il a vu juste. Ilona est épuisée. Il a même retiré ce qui pouvait l'être."
    systeme "Puis il a choisi, seul, ce qui devait rester. Avec Théo, être comprise et être conduite prennent souvent la même voix."

    hide theo
    hide ilona
    with dissolve

    $ renpy.pause(0.4, hard=True)

    scene bg arc7 tokyo studio
    with fade

    systeme "Le soir, les locaux du studio prennent le relais. En huit mois, la chance fragile est devenue une machine solide. Les miniatures changent. Les titres changent. La lumière du studio ne change jamais."
    systeme "Ilona apprend à dire « coucou tout le monde » même les soirs où sa voix voudrait commencer par autre chose."
    systeme "Théo avait compris depuis longtemps qu'Ilona trouvait les choses plus faciles en ligne, quand personne ne voyait ses blancs. À Tokyo, presque toute sa vie se passe en ligne. Lui voit chacun de ses blancs et les remplit quand même."

    if arc5_fin_minecraft == "theo_presence":
        systeme "Quelque part, sur un serveur qu'elle n'ouvre presque plus, la maison Minecraft garde un mot de passe qui n'a pas été choisi par elle."
    elif arc6_offre_theo == "question":
        systeme "Dans le couloir, Théo avait admis qu'il voulait à la fois aider Ilona et l'avoir près de lui. À Tokyo, les deux envies sont devenues impossibles à séparer."
    elif arc6_offre_theo == "aveu_vide":
        systeme "Le studio avait d'abord ressemblé à une réponse concrète. Il est maintenant la première question qui l'attend chaque matin."

    show ilona short sad_alt at char_left
    show theo tokyo neutral at char_right
    with dissolve

    systeme "À la fin août, la chaîne atteint deux cent cinquante mille abonnés et les directs rassemblent autour de douze mille spectateurs. Théo cadre une photo dans le studio avant leur départ pour un restaurant calme."

    t "Un peu plus à gauche."
    i "Mon gauche ou ton gauche ?"
    t "Le tien."
    i "Tu aurais dû dire ça avant que je sorte du cadre."
    t "Reviens d'un pas. Voilà. Souris."
    i "Attends, j'ai encore mon pull."
    t "La marque préfère un truc spontané."
    i "Rien ne dit « spontané » comme toi qui comptes jusqu'à trois."

    systeme "À la fin octobre, la chaîne atteint six cent mille abonnés et certains directs dépassent trente mille spectateurs. Ils ne vont plus au restaurant. Théo apporte un gâteau au studio et rédige le tweet pendant qu'Ilona remplace son pull par sa veste de stream. Dès que la caméra s'allume, elle sourit."

    show ilona streaming smile at char_left
    with dissolve

    t "Je mets : incroyable chemin parcouru grâce à vous."
    i "C'est pas moi, ça."
    t "D'accord. Qu'est-ce que tu veux dire ?"
    i "Je sais pas. Laisse-moi deux minutes."
    t "La photo doit partir maintenant pour profiter du palier. Je peux ajouter un cœur violet."
    i "Mets le cœur."

    systeme "À chaque palier, Théo trouve le lieu où elle supportera le bruit, le texte qu'elle n'aura pas besoin de réécrire et la bonne phrase pour les partenaires. À chaque palier, Ilona sourit sur les photos."

    hide ilona
    hide theo
    with dissolve

    if arc5_theo_proposition == "partiel":
        systeme "Avant même le diplôme, Théo avait proposé de gérer une partie de sa vie alors qu'Ilona n'était pas dans la pièce. On ne lui avait concédé que les notes. À Tokyo, le provisoire est devenu un emploi du temps entier."
    elif arc5_theo_proposition == "laisse":
        systeme "Avant même le diplôme, Théo avait dit : « Je gère. » Le projet d'Ilona avait changé de mains alors qu'elle n'était pas dans la pièce. À Tokyo, il n'a plus besoin d'intermédiaire."
    elif arc5_theo_proposition == "refuse":
        systeme "La première fois que Théo avait proposé de gérer son quotidien, on avait appelé ça une stratégie. Lui avait répondu : de l'efficacité. À Tokyo, la même efficacité a les clés de la maison."
    elif arc5_theo_proposition == "questionne":
        systeme "La première fois que Théo avait proposé de gérer son quotidien, on lui avait demandé pourquoi il ne parlait pas directement à Ilona. Pour Tokyo, il l'avait fait. Une offre directe n'était pas forcément une offre neutre."

    systeme "Cette semaine-là, la régie prépare un tournage extérieur depuis les locaux. Leurs caisses de matériel encombrent le studio ; ils partiront avant l'aube le lendemain du million et ne seront presque pas joignables avant le jour suivant."

    $ renpy.pause(1.0, hard=True)

    systeme "Puis vient le million."
    systeme "Il est 23 h passées."

    # ------------------------------------------------------------------
    # 2. Le stream, vu de l'extérieur puis vu d'elle
    # ------------------------------------------------------------------
    play music audio.stream loop volume 0.6

    systeme "Devant la caméra, Ilona a troqué le col roulé gris du matin pour la veste bleue et les longs cheveux blancs que le public associe à IlonaGaming."

    show ilona streaming celebration at char_center
    with dissolve

    systeme "Le compteur atteint un million d'abonnés après huit mois. Plus de quarante-six mille spectateurs suivent encore le direct, et les subs Twitch offerts ne s'arrêtent plus."

    tchat "xXShadow_JPxX : ENFIN LE MILLION ILONA ON T'AIME"
    tchat "kiwi_no_kimi : gg gg gg gg"
    tchat "darkflame92 : elle a jamais autant stream que cette semaine respect"
    tchat "sakura_mod : on spam les cœurs pour elle svp"
    tchat "misterclip : best vtubeuse fr jp no debate"

    show ilona streaming smile at char_center
    with dissolve

    i "Merci à vous, sincèrement... je suis trop contente de passer la soirée avec vous, j'ai grave kiffé ce stream."
    tchat "moon_walker21 : Ilona tu nous quittes jamais hein ??"
    i "Jamais !"

    systeme "Le mot sort trop vite. Il est parfait pour le tchat. Il est moins parfait pour elle."

    i "Bon... sur ce, gros bisous à tous, à demain pour un nouveau stream !"

    stop music fadeout 1.0
    show ilona streaming fatigue at char_center
    with dissolve
    systeme "Dès que le stream coupe, son visage se décompose. Fatigue physique. Fatigue de l'autre genre, aussi."
    $ renpy.pause(1.0, hard=True)
    i "..."

    systeme "Sur le deuxième écran, les statistiques continuent de bouger. Même éteint, le stream a encore l'air de demander quelque chose."

    if arc3_reaction_rumeur in ("blague_desarm", "silence_paralysie"):
        systeme "Au festival, Théo avait utilisé une rumeur pour créer deux secondes de proximité avec Ilona. Il avait appris qu'une douceur pouvait entrer avec une facture quand elle arrivait au bon moment."
    else:
        systeme "Au festival, Ilona avait refusé la douceur de Théo quand elle arrivait avec une facture. Plus tard, il avait tout de même utilisé une vérité comme une lame."
    systeme "Ce soir encore, Théo n'aura besoin de rien inventer : les chiffres, la fatigue et les contrats seront tous vrais."

    systeme "À Noël, Laplage avait prévenu Théo qu'un souvenir bien placé pouvait ouvrir une porte ou enfermer quelqu'un. Théo avait répondu qu'il ne forçait personne à rester."
    systeme "Laplage avait conclu : « Non. Mais tu gardes la clé. » À Tokyo, Théo la garde toujours."

    # ------------------------------------------------------------------
    # 3. Théo entre, félicitations "professionnelles"
    # ------------------------------------------------------------------
    show theo tokyo reassuring at char_right
    with dissolve

    systeme "Théo entre avec un verre d'eau sans glaçons. Ilona tousse quand elle boit trop froid après un stream ; elle ne se souvient pas de le lui avoir dit. Lui, si."

    t "Tu l'as fait."
    i "Apparemment."
    t "Pas apparemment. Un million."
    i "Ça ressemble pas à un vrai nombre."
    t "Tu veux que j'actualise ?"
    i "Non. À cent mille, c'était mignon. Là, s'il redescend, je vais pleurer."
    t "Alors on ne touche à rien."

    systeme "Théo pose le verre à portée de sa main. Il attend qu'Ilona lève les yeux vers lui."

    t "Je suis hyper fier de toi."
    i "Merci."
    t "Est-ce que je peux t'embrasser ? Cette fois, aucun dessert ne risque de fondre."

    show ilona streaming smile at char_center
    with dissolve

    i "Il y avait quarante-six mille personnes devant il y a dix secondes."
    t "Le stream est coupé."
    i "Alors vite. Avant que l'algorithme nous voie."

    systeme "Le baiser est bref. Quand Théo recule, son regard revient presque aussitôt sur le deuxième écran."

    t "T'as tenu deux heures quarante, t'as relancé le tchat chaque fois que ça retombait, et personne n'a vu que t'avais mal à la gorge sur la fin."
    t "La chaîne explose exactement comme je l'avais prévu. Les sponsors vont se battre pour toi."
    i "Ouais..."

    show ilona streaming fatigue at char_center
    with dissolve

    systeme "Théo voit ses doigts crispés autour du verre, le sourire tombe une demi-seconde trop tôt, le « ouais » sans air derrière."
    systeme "Il voit la fatigue avant qu'elle trouve le mot. Son erreur n'est pas de la manquer. C'est de croire qu'il sait déjà ce qu'elle signifie."

    show theo tokyo smirk at char_right
    with dissolve

    t "J'ai déjà trois mails. Un casque, une boisson énergisante, et une grosse marque qui veut une campagne sur six mois."
    i "Six mois ?"
    t "C'est énorme."
    i "C'est long."
    t "Long, oui. Mais stable. Plus besoin de te demander tous les matins si le mois prochain tient encore debout."
    t "Tu m'as dit que c'était l'incertitude qui t'épuisait le plus. Avec ça, je peux enfin t'en enlever une partie."

    i "Théo."
    t "Hm ?"
    i "Quand tu dis « on », tu parles de qui ?"

    show theo tokyo neutral at char_right
    with dissolve

    t "De nous."
    i "De nous deux, ou de la chaîne ?"
    t "Ilona..."
    t "La chaîne, c'est pas un truc à côté de nous. C'est ce qu'on construit ensemble."

    systeme "Il appuie à peine sur « ensemble ». Juste assez pour rappeler les nuits, les billets, les mails et tout ce qu'il a porté sans qu'elle ait à le demander. Ilona voudrait que le mot lui fasse du bien. Une partie d'elle y arrive encore."

    i "Ton carnet de Noël, tu te souviens ? T'avais pris une phrase que j'avais dite à la plage et t'en avais fait un cadeau."
    t "Je voulais te montrer que je faisais attention."
    i "Tu fais attention. C'est pas le problème. Le problème, c'est que connaître mes goûts, ça veut pas dire savoir ce que je veux."
    if arc4_reaction_cadeau_theo in ("blague_acide", "verite_crue"):
        i "Ce soir-là, je t'ai aussi dit que j'étais pas un trophée qu'on gagne avec des souvenirs bien placés."
        t "Je sais."
    i "Alors pourquoi j'ai l'impression que plus tu me connais, moins tu me poses la question ?"

    t "Parce que la plupart du temps, j'ai la bonne réponse."
    i "C'est pas la question."
    t "Je sais."
    i "Non. Tu sais ce que j'allais répondre. C'est différent."
    t "D'accord. Qu'est-ce que tu veux, là, maintenant ?"
    i "Que tu n'utilises pas cette question comme une technique pour réparer la conversation."

    show theo tokyo disappointed at char_right
    with dissolve

    t "Je sais pas quoi dire."
    i "On peut ne rien dire deux minutes."

    systeme "Sur le quai du 6 avril, Théo lui avait demandé si elle avait tout. Ilona avait répondu : « J'ai ce que j'ai décidé de prendre. » Il se souvenait de chaque mot. Il n'avait pas compris qu'elle parlait déjà du droit de choisir."

    systeme "Pendant deux minutes, aucun d'eux ne parle. Peu après minuit, ils éteignent les écrans, ferment les locaux et sortent."
    systeme "Avant de partir, Ilona retire sa perruque blanche et remet son pull gris. Son sourire de stream reste au studio."

    hide ilona
    hide theo
    with dissolve

    scene bg arc7 tokyo konbini night
    with fade

    systeme "Deux rues séparent le studio de leur maison. La lumière du konbini découpe le trottoir. Depuis huit mois, ils y sont passés assez souvent pour que Théo classe les onigiris par parfum."

    show ilona short sad at char_left
    show theo tokyo neutral at char_right
    with dissolve

    t "Tu veux prendre quelque chose ?"
    i "Non."
    t "Tu n'as presque pas mangé avant le stream."
    i "Je sais."
    t "Il reste peut-être les onigiris au saumon."
    i "Toujours premier de ton classement ?"
    t "Le thon-mayo a remonté."
    i "Trahison."

    systeme "Le mot pourrait être une blague. Aucun des deux ne sait comment le recevoir."

    t "Je peux aller t'en chercher un."
    i "J'ai pas faim, Théo."
    t "D'accord."

    systeme "Il ne traverse pas la rue. C'est une toute petite chose qu'elle n'a pas eu besoin de répéter. Ils repartent."

    hide ilona
    hide theo
    with dissolve

    scene bg arc7 tokyo house night
    with fade

    systeme "Quand ils entrent dans la pièce commune, la maison est éteinte et trop calme. Ilona pose son téléphone près du carnet de planning. Théo rallume la cuisine."

    show ilona short sad_alt at char_left
    show theo tokyo neutral at char_right
    with dissolve

    t "Tu veux du thé ?"
    i "Tu vas me demander jusqu'à ce que j'accepte quelque chose ?"
    t "Non. C'était juste du thé."
    i "Désolée."
    t "T'excuse pas."

    systeme "Théo range la bouilloire sans la remplir. Ilona tire sur le bord de sa manche."

    i "Tu te souviens de la série avec le type insupportable ?"
    t "Celui qui avait toujours un plan ?"
    i "On n'a jamais regardé la fin."
    t "Tu t'es endormie au milieu de la saison."
    i "Une fois."
    t "Trois fois."
    i "C'est pas le sujet."
    t "C'est quoi, le sujet ?"
    i "Nous. Enfin... le fait qu'il n'y ait presque plus de nous sans la chaîne au milieu."

    show ilona short sad at char_left
    with dissolve

    i "Ça fait un moment que j'y pense. J'aimerais qu'on passe du temps tous les deux. Une promenade dans un parc, un resto, un film, n'importe quoi."
    i "On n'a plus eu un seul moment rien qu'à nous depuis des semaines. Je me sens seule alors que je suis censée être entourée d'un million de personnes. C'est idiot, dit comme ça."
    t "C'est pas idiot."
    t "Tu tires sur ta manche depuis tout à l'heure. Tu fais ça quand tu cherches comment demander quelque chose sans déranger."
    t "T'aurais pas dû avoir besoin de chercher avec moi."
    t "On va se le prendre, ce moment. Promis. Juste... pas tout de suite, il y a encore beaucoup de boulot en ce moment."

    systeme "Une promesse de plus. Ilona a arrêté de les compter."

    i "C'est quand, pas tout de suite ?"
    t "Quand cette semaine sera passée."
    i "Et après, il y aura quoi ?"
    t "Je sais pas."
    i "Moi non plus. C'est pour ça que je te demande demain après-midi. On pourrait sortir à Tokyo, juste toi et moi. Ça me ferait vraiment du bien."

    show theo tokyo neutral at char_right
    with dissolve

    t "Demain après-midi..."
    systeme "Il connaît déjà la réponse. Il sort quand même son téléphone : les cases colorées donnent à son refus l'air d'un fait extérieur."
    t "J'ai les sponsors à quinze heures."
    i "Tu peux déplacer ?"
    t "Je peux essayer."

    systeme "Ilona entend la différence entre « je vais » et « je peux essayer ». Elle aurait voulu ne pas l'entendre."

    i "Et le stream du soir ?"
    t "On peut le raccourcir."
    i "Ou l'annuler."

    show theo tokyo defensive at char_right
    with dissolve

    t "Annuler le soir du million, ce serait un mauvais signal."
    i "À qui ?"
    t "Aux gens. Aux marques. À l'algorithme."
    i "Et à moi ?"

    $ renpy.pause(1.0, hard=True)

    systeme "Théo ne commence pas à la regarder. Il la regardait déjà."
    systeme "Il reprend mentalement le verre intact, la manche tirée, le mot « seule », et cherche la réponse qui pourra encore ressembler à une aide."

    # ------------------------------------------------------------------
    # Choix final : la réponse de Théo décide de la route
    # ------------------------------------------------------------------
    show theo tokyo defensive at char_right

    menu:
        "La réponse de Théo."

        "Annuler les sponsors, écouter Ilona.":
            t "T'as raison. Les sponsors, ça peut attendre. Toi, c'est maintenant que ça compte."

            show ilona short neutral at char_left
            i "Tu es sérieux ?"
            t "Sérieux."
            t "Demain après-midi, je décale les sponsors. Le soir, on peut annuler le stream si tu veux."
            t "Je peux prévenir l'équipe que tu as besoin de souffler."

            show theo tokyo neutral at char_right
            with dissolve

            i "Tu vois ?"
            t "Quoi ?"
            i "Je te demande du temps avec toi, et en dix secondes tu es déjà en train d'organiser ce que je dois annuler et ce que tu vas dire à ma place."

            show theo tokyo defensive at char_right
            with dissolve

            t "J'essaie de te faciliter les choses."
            i "Je sais. Mais quand je refuse ta solution, tu le prends comme si je refusais tout ce que tu fais pour moi."

            systeme "Il pourrait lui rappeler les nuits sans dormir, les contrats traduits, les repas posés à côté du clavier avant même qu'elle ait faim. Tout serait vrai."
            systeme "La liste monte jusqu'à sa gorge. Pour une fois, Théo ne s'en sert pas."

            t "D'accord. Qu'est-ce que tu veux que j'annule ?"
            i "Tout. Pour demain, tout. Et je veux écrire le message moi-même."
            t "D'accord."

            systeme "Le mot lui coûte. Pas à cause des sponsors. Parce qu'il ne contient aucune direction."

            show ilona short sad at char_left
            i "Théo... je crois que j'ai besoin de plus qu'une après-midi."
            i "J'ai besoin de faire une vraie pause sur le stream. Revenir à un jeu plus casual. Ou faire autre chose, je sais pas encore. Mais arrêter de me vider pour un million d'inconnus."

            show theo tokyo defensive at char_right
            with dissolve

            t "Une vraie pause, après un million, ça peut faire disparaître la moitié de ce qu'on a construit. Les marques ne vont pas attendre sans date, l'algorithme non plus. Ça me fait peur."
            i "Moi aussi."
            i "Mais si je continue comme ça, c'est moi qui disparais avant."

            $ renpy.pause(1.0, hard=True)

            show theo tokyo disappointed at char_right
            with dissolve

            t "J'allais te dire que j'avais porté toute la partie ingrate pour qu'on arrive jusque-là."
            t "Comme si ça te donnait l'obligation d'aimer l'endroit où je nous ai conduits."
            t "J'ai peur que si on ralentit, tout disparaisse. Mais c'est ma peur. Pas ta consigne."
            i "Au restaurant, tu m'avais dit que tu devais entendre mon non."
            t "Je m'en souviens."
            i "Tu l'as entendu quand ?"
            t "Beaucoup trop tard."
            i "Tu vas détester ça."
            t "Probablement."
            t "Mais je peux détester ça sans choisir à ta place. Je vais devoir apprendre."

            systeme "Théo a encore mémorisé chacune de ses hésitations. Il a encore envie d'en faire un plan."
            systeme "Mais pour la première fois, Ilona peut laisser un blanc sans qu'il le remplisse à sa place."
            systeme "Sur le quai, Ilona avait dit qu'elle emportait ce qu'elle avait décidé de prendre. Cette fois, Théo comprend enfin que la décision comptait plus que la destination. Le silence reste ouvert jusqu'à ce qu'elle choisisse quoi en faire."

            hide ilona
            hide theo
            with dissolve

            jump ending_neutre

        "Prioriser les sponsors, la chaîne avant tout.":
            t "Demain après-midi, tu ne vas pas traverser Tokyo épuisée pour faire semblant de profiter d'un parc. Tu vas dormir. Moi, je vois les sponsors."
            t "À vingt heures, tu fais un stream court. Une heure, pas plus. Je te libère tout le reste."

            show theo tokyo reassuring at char_right
            with dissolve

            t "Écoute, je sais que t'es fatiguée. Je le vois."
            systeme "Il le voit. C'est ce qui rend la phrase plus dure, pas moins."
            t "Tu as besoin de sommeil, de silence, et de ne pas avoir à prendre dix décisions ce soir. Pas de jeter six mois de sécurité parce que la journée était trop longue."
            t "Laisse-moi porter la partie lourde encore un peu. Les mails, les rendez-vous, les contrats. Toi, tu fais ce que tu fais mieux que tout le monde."
            t "Après cette vague, je te promets qu'on ralentit. J'ai toujours tenu mes promesses quand il fallait te protéger."

            show ilona short sad at char_left
            with dissolve

            i "Après."
            t "Oui."
            i "C'est toujours après."

            show theo tokyo defensive at char_right
            with dissolve

            t "Parce qu'on est dedans maintenant. Et parce que je sais ce que ça t'a coûté d'arriver là. J'étais là pour chaque nuit blanche, chaque mail, chaque fois où tu voulais tout supprimer le lendemain d'un mauvais stream."
            t "Je t'ai évité de regretter ces soirs-là. Fais-moi confiance pour celui-ci aussi."

            i "Au restaurant, tu m'avais dit que tu devais entendre mon non."
            t "Je l'entends."
            i "Et ?"
            t "Et je sais aussi dans quel état tu es quand tu le dis. Ce soir, je te demande de me faire confiance malgré tout."

            i "Je comprends."

            systeme "Elle comprend vraiment. C'est ça, le piège. Une cage dorée n'a pas besoin d'être absurde pour fermer."
            systeme "Théo n'a inventé ni sa fatigue, ni ses anciens regrets, ni tout ce qu'il a fait pour elle. Il a seulement rangé les faits dans l'ordre qui menait à sa réponse."

            if arc4_5_theo_proposition == "gestion_stream":
                systeme "Quand Ilona avait accepté que Théo gère le chat et le planning, deux mots avaient commencé la dette : « Bien sûr. » À Tokyo, la dette a une maison, un studio et six mois de contrats possibles."
            elif arc4_ilona_avec_theo:
                systeme "Elle s'était déjà demandé si elle ne remplaçait pas une cage par une autre. À l'époque, la seconde avait l'air confortable. Elle l'est toujours. Mais une cage quand même."

            i "Je vais me coucher, je suis crevée."
            t "Je sais. J'ai baissé le chauffage dans ta chambre et mis ton téléphone en mode nuit."
            t "Vas-y, je te rejoins. Faut que je prépare la journée de demain avec les sponsors."
            t "On a fait tout ça ensemble, Ilona. Laisse pas une mauvaise soirée te faire croire le contraire. Bonne nuit."

            hide theo
            with dissolve

            systeme "Théo sort de la pièce."
            play music audio.sadPiano loop volume 0.5 fadein 2.0
            i "..."
            systeme "Dans l'écran noir de son téléphone, son reflet reste pris entre le carnet de planning et les feuilles de production."
            systeme "Pendant quelques secondes, elle attend que quelqu'un dise son prénom sans le transformer en marque."
            systeme "Sa main se referme sur le porte-clés bloc que Théo avait retrouvé à la plage. La première preuve qu'il faisait attention. Il fait toujours attention. C'est justement pour ça qu'elle ne sait plus comment lui échapper."
            $ renpy.pause(1.5, hard=True)

            scene black
            with fade
            stop music fadeout 2.0

            jump bad_ending
