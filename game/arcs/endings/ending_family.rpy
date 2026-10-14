# GOOD ENDING (FAMILY) - JESSY ET ILONA
# Suite de l'aveu réciproque et du choix de dormir avec Ilona dans la tente.
# Scénario : agents/Good ending.md ; continuité : agents/cartographies.
# Les décors dédiés et le plan du câlin sont intégrés. Les pistes Undertale gardent leurs secours.

init -5 python:
    def family_music(chemin, secours):
        return chemin if renpy.loadable(chemin) else secours

# Les originaux (2752 x 1536) remplissent l'écran sans déformer leur perspective.
image bg family rendezvous = Transform("images/scenes/ending/family/bg_family_rendezvous.jpg", xysize=(1920, 1080), fit="cover")
image bg family restaurant jour = Transform("images/scenes/ending/family/bg_family_restaurant_jour.jpg", xysize=(1920, 1080), fit="cover")
image cg family laplage adieux = Transform("images/scenes/ending/family/cg_family_laplage_adieux.png", xysize=(1920, 1080), fit="cover")
image bg family salle = Transform("images/scenes/ending/family/bg_family_salle.jpg", xysize=(1920, 1080), fit="cover")
image bg family maison = Transform("images/scenes/ending/family/bg_family_maison.jpg", xysize=(1920, 1080), fit="cover")
image bg family pancakes rate = Transform("images/scenes/ending/family/cg_family_pancakes_01.png", xysize=(1920, 1080), fit="cover")
image bg family pancakes reussi = Transform("images/scenes/ending/family/cg_family_pancakes_02.png", xysize=(1920, 1080), fit="cover")
image bg family restaurant soir = Transform("images/scenes/ending/family/bg_family_restaurant_soir.jpg", xysize=(1920, 1080), fit="cover")
image bg family restaurant nuit = Transform("images/scenes/ending/family/bg_family_restaurant_nuit.png", xysize=(1920, 1080), fit="cover")
image cg family entrance kiss = Transform("images/scenes/ending/family/cg_family_entrance_kiss.png", xysize=(1920, 1080), fit="cover")
image bg family fete = Transform("images/scenes/ending/family/bg_family_fete.jpg", xysize=(1920, 1080), fit="cover")
image bg family fete fin = Transform("images/scenes/ending/family/bg_family_fete_fin.png", xysize=(1920, 1080), fit="cover")
image bg family fete rangement = Transform("images/scenes/ending/family/bg_family_fete_rangement.png", xysize=(1920, 1080), fit="cover")
image cg family toast = Transform("images/scenes/ending/family/cg_family_toast.png", xysize=(1920, 1080), fit="cover")
image bg family karaoke = Transform("images/scenes/ending/family/bg_family_karaoke.png", xysize=(1920, 1080), fit="cover")
image bg family jardin jour = Transform("images/scenes/ending/family/bg_family_jardin_jour.jpg", xysize=(1920, 1080), fit="cover")
image bg family jardin soir = Transform("images/scenes/ending/family/bg_family_jardin_soir.jpg", xysize=(1920, 1080), fit="cover")
image cg family lucy hug = Transform("images/scenes/ending/family/cg_family_lucy_hug.png", xysize=(1920, 1080), fit="cover")
image cg family homecoming = Transform("images/scenes/ending/family/cg_family_homecoming.png", xysize=(1920, 1080), fit="cover")

# Tenues disponibles : pas de summer/house pour Jessy, qui conserve beach
# au quotidien. Les tailles et le suivi du locuteur restent ceux du jeu.
image ilona summer neutral = speaker_sprite("ilona", "images/personnages/Ilona/summer/neutral.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona summer smile = speaker_sprite("ilona", "images/personnages/Ilona/summer/playful_warm_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona summer embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/summer/awkward_embarrassment.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona house neutral = speaker_sprite("ilona", "images/personnages/Ilona/house/neutral.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona house smile = speaker_sprite("ilona", "images/personnages/Ilona/house/playful_warm_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona house embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/house/awkward_embarrassment.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona house pregnant = speaker_sprite("ilona", "images/personnages/Ilona/house/pregnant.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona party neutral = speaker_sprite("ilona", "images/personnages/Ilona/party/neutral.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona party smile = speaker_sprite("ilona", "images/personnages/Ilona/party/playful_warm_smile.png", ILONA_SIZE[0], ILONA_SIZE[1])
image ilona party embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/party/awkward_embarrassment.png", ILONA_SIZE[0], ILONA_SIZE[1])
image jessy party neutral = speaker_sprite("jessy", "images/personnages/Jessy/party/neutral_attentiveness.png", 842, 1264)
image jessy party smile = speaker_sprite("jessy", "images/personnages/Jessy/party/shy_warm_smile.png", 842, 1264)
image jessy party happy = speaker_sprite("jessy", "images/personnages/Jessy/party/happy.png", 842, 1264)
image allan party neutral = speaker_sprite("allan", "images/personnages/Allan/party/neutral.png", 847, 1264)
image allan party smirk = speaker_sprite("allan", "images/personnages/Allan/party/playful_smirk.png", 847, 1264)
image alex party grin = speaker_sprite("alex", "images/personnages/Alexandre/party/playful_grin_party.png", 842, 1264)
image alex party awkward = speaker_sprite("alex", "images/personnages/Alexandre/party/akward_realization_party.png", 842, 1264)
image alex party concerned = speaker_sprite("alex", "images/personnages/Alexandre/party/concerned_look_party.png", 842, 1264)
image sofiane party neutral = speaker_sprite("sofiane", "images/personnages/Sofiane/party/reserved_neutral.png", 842, 1264)
image theo party neutral = speaker_sprite("theo", "images/personnages/Théo/party/neutral.png", 842, 1264, THEO_CROP_BOTTOM)
image theo party reassuring = speaker_sprite("theo", "images/personnages/Théo/party/reassuring_smile.png", 842, 1264, THEO_CROP_BOTTOM)
image theo party smirk = speaker_sprite("theo", "images/personnages/Théo/party/knowing_smirk.png", 842, 1264, THEO_CROP_BOTTOM)
image jessy papa neutral = speaker_sprite("jessy", "images/personnages/Jessy/papa/neutral.png", 842, 1264)
image jessy beach smile = speaker_sprite("jessy", "images/personnages/Jessy/beach/shy_warm_smile.png", 842, 1264)
image jessy beach determined = speaker_sprite("jessy", "images/personnages/Jessy/beach/vulnerable_determination.png", 842, 1264)
image jessy beach surprised = speaker_sprite("jessy", "images/personnages/Jessy/beach/surprised.png", 842, 1264)
image micka party neutral = speaker_sprite("micka", "images/personnages/micka/party/neutral.png", 842, 1264)
image micka party flowers = speaker_sprite("micka", "images/personnages/micka/party/flowers.png", 842, 1264)

# Canvas réduit pour que Lucy reste à hauteur d'enfant auprès de ses parents.
image lucy neutral = speaker_sprite("lucy", "images/personnages/lucy/neutral.png", 576, 864)
image lucy happy = speaker_sprite("lucy", "images/personnages/lucy/happy.png", 576, 864)
define family_lucy = Character("Lucy", color="#f4d183", callback=speaker_callback("lucy"))

transform family_jessy_centre:
    xalign 0.18
    yalign 1.0
    zoom 0.50
    ease 1.2 xalign 0.50


label ending_family:
    $ record_ending("family")
    stop ambiant1 fadeout 1.0
    stop music fadeout 1.0
    scene black with fade
    centered "QUELQUES JOURS APRÈS LA RANDONNÉE"
    jump ending_family_restaurant


# 1. DEUX RECHERCHES, UNE ADRESSE
label ending_family_restaurant:
    scene bg family rendezvous with fade
    play music audio.restojazz loop volume 0.65 fadein 1.5
    show jessy beach happy at char_left
    show ilona summer smile at char_right
    with dissolve

    systeme "Ilona arrive au restaurant avec sept minutes d'avance. Entre les plantes et les grandes fenêtres, Jessy a trouvé une table pour deux. Devant lui, les menus et une corbeille de pain intacte."
    i "T'es là depuis longtemps ?"
    j "J'ai vu installer la terrasse."
    i "Ah oui."
    systeme "Elle se penche pour l'embrasser avant de s'asseoir. Jessy sourit encore quand elle lui prend un morceau de pain."
    i "Tu vas faire cette tête à chaque fois ?"
    j "Pour l'instant, oui."
    i "Bon. Je préviens, je compte recommencer."
    systeme "Ils commandent. Sous la table, le pied d'Ilona vient chercher le sien."
    j "C'est bizarre de te raccompagner et de repartir chez moi."
    i "Hier, j'ai commencé à te raconter un truc dans l'entrée. J'ai dû te rappeler pour finir."
    j "L'histoire de la bouilloire ?"
    i "Elle avait une suite."
    j "Une suite de quarante minutes."
    i "On pourrait vivre ensemble. Comme ça, tu profiterais de la version longue."
    show jessy beach smile at char_left with dissolve
    systeme "Jessy pose sa carte. Ilona aussi."
    j "J'aimerais bien. Vraiment."
    i "Moi aussi."
    j "Tu voudrais chercher où ?"
    systeme "Elle regarde par la fenêtre. Des vélos sont garés devant les maisons de la petite rue ; les fils électriques découpent le ciel."
    i "Là-haut. Dans les montagnes."
    i "Depuis qu'on est redescendus, je repense au matin devant la tente. Au lac. Même à tes chaussettes qui séchaient sur la branche."
    j "Un élément essentiel du paysage."
    i "Cette randonnée... je crois que c'est le plus beau moment de ma vie."
    systeme "Elle tourne son verre entre ses mains, puis relève les yeux."
    i "J'ai envie d'y avoir des journées normales, aussi. Aller chercher du pain. Rentrer quand il pleut. Te retrouver le soir."
    j "Et oublier pourquoi on est descendus à la cave."
    i "Ça, tu peux déjà le faire ici."
    j "J'ai envie de ça avec toi. Là-haut."
    systeme "Il attrape son téléphone."
    j "D'ailleurs, j'ai trouvé un..."
    i "Attends, faut que je te montre ! Je cherchais des maisons et du boulot, et j'ai reçu une annonce ce matin."
    systeme "Elle lui tend son écran, puis s'arrête."
    i "Pardon. Tu voulais dire quoi ?"
    systeme "Jessy compare les deux photos. La même façade crème et bois. Le même rideau vert au-dessus des portes coulissantes. Une table sous un grand arbre."
    j "Ça. Très exactement ça."
    i "Non !"
    j "Petit restaurant de montagne. Maison attenante. Recherche repreneurs."
    i "Cuisine équipée, jardin, vue sur les sommets ?"
    j "Et une photo prise avec le doigt devant l'objectif."
    systeme "Ils éclatent de rire. Sur les deux écrans, un pouce flou cache le coin du toit."
    i "C'est un signe."
    j "Ou on a mis les mêmes filtres."
    i "Laisse-moi mon signe."
    show jessy beach neutral at char_left
    show ilona summer neutral at char_right
    with dissolve
    j "D'accord. Mais un restaurant... on a surtout de l'expérience pour vider les assiettes."
    i "On a tenu le café du festival."
    j "Une journée. Avec six personnes pour faire du thé."
    i "Je sais. On pourrait commencer petit. Quelques plats qu'on sait vraiment faire. Apprendre le reste."
    j "Ça me fait un peu peur."
    i "Moi aussi. J'ai quand même envie de visiter."
    show jessy beach determined at char_left with dissolve
    j "Alors on visite."

    systeme "Il compose le numéro. Ilona se penche au-dessus de la table pour écouter."
    j "Bonjour, je vous appelle pour le restaurant. L'annonce est toujours disponible ?"
    "La voix au téléphone" "Elle vous attendait."
    j "Pardon ?"
    "La voix au téléphone" "Elle attendait des appels. Demain, quatorze heures ?"
    j "On peut, oui. Nous serons deux."
    "La voix au téléphone" "Très bien. Sonnez. Même si vous me voyez déjà par la fenêtre."
    systeme "L'appel se termine. Jessy regarde le numéro."
    show jessy beach neutral at char_left with dissolve
    j "Je connais cette voix."
    i "C'est qui ?"
    j "J'arrive pas à la remettre. Il a une façon de dire bonjour... comme s'il savait la fin de la conversation."
    i "On saura demain. Quatorze heures !"
    show ilona summer smile at char_right with dissolve
    systeme "Elle tape déjà un message à Sofiane."
    systeme "{i}« On a trouvé un resto avec une maison près du départ de la rando. Visite demain à 14 h. Tu pourrais nous emmener ? »{/i}"
    systeme "La réponse arrive pendant le plat."
    systeme "{i}« Aucun souci. La Trueno réclame une promenade. Je passe vous prendre devant chez vous. »{/i}"
    i "Merci merci merci. Avec trois cœurs."
    j "Tu lui as écrit ça ?"
    i "Oui."
    systeme "Une seconde réponse apparaît."
    systeme "{i}« Elle accepte vos remerciements. »{/i}"
    j "Il parle toujours de la voiture ?"
    i "Je pense. J'ai trop hâte d'être demain."
    systeme "Ils restent jusqu'au dessert. Ilona raconte enfin la suite de l'histoire de la bouilloire. Jessy commande un deuxième thé."
    jump ending_family_visite


# 2. LE PROPRIÉTAIRE
label ending_family_visite:
    stop music fadeout 1.5
    scene black with fade
    centered "LE LENDEMAIN"
    scene bg arc7 jessy route with fade
    play music audio.rando loop volume 0.55 fadein 1.0
    show sofiane beach neutral at char_center with dissolve
    systeme "La Trueno monte entre les sapins. À l'arrière, Ilona suit les virages sur la carte ; Jessy tient un sac de viennoiseries sur ses genoux."
    s "Vous avez pris des provisions pour la visite."
    j "On voulait vous remercier. Enfin, te remercier. Toi et la voiture, apparemment."
    s "Elle prend du sans-plomb. Je prends celui aux amandes."
    i "Celui-là a survécu, oui."
    s "Vous connaissez les gens qui vendent ?"
    j "Non. Mais j'ai l'impression d'avoir déjà parlé au monsieur."
    s "La montagne fait revenir certaines voix."
    systeme "Un silence. Sofiane met son clignotant."
    s "Et le GPS dit de tourner ici."

    scene bg family restaurant jour with fade
    show jessy beach neutral at char_left
    show ilona summer smile at char_right
    show sofiane beach neutral at char_center
    with dissolve
    systeme "Au bout de la route, un portillon ouvre sur une cour entourée d'arbres. Le restaurant a un toit de tuiles grises, un rideau vert à l'entrée et une enseigne encore vierge."
    systeme "Des tables en bois occupent la cour, jusqu'à l'ombre du grand arbre. À droite, un chemin de pierres rejoint une petite maison. Entre les deux bâtiments, le sentier remonte vers la forêt."
    i "C'est encore plus joli que sur la photo."
    j "On voit tout le toit, surtout."
    s "Je reste dans le coin. Appelez quand vous avez fini."
    i "Merci, Sofiane. Vraiment."
    s "Prenez votre temps. J'ai quelques virages à saluer."
    play sound audio.carGo volume 0.4
    hide sofiane with dissolve
    systeme "La Trueno redescend vers la route. Jessy et Ilona franchissent le portillon."
    systeme "À côté de la porte coulissante, ils trouvent la sonnette. Une silhouette vient de bouger derrière les carreaux."
    j "Ça commence à me revenir."
    play sound audio.bell volume 0.3
    show laplage neutral at char_center with dissolve
    stop music fadeout 1.0
    laplage "Bonjour. Vous êtes à l'heure."
    i "Monsieur Laplage ?!"
    j "Bien sûr."
    laplage "Vous pouvez entrer. Aujourd'hui, je suis propriétaire."
    i "Aujourd'hui ?"
    laplage "Depuis longtemps, en réalité. Mais j'essaie de me diversifier moins."
    play music audio.mornPiano loop volume 0.6 fadein 1.5

    scene bg family salle with fade
    show jessy beach neutral at char_left
    show laplage neutral at char_center
    show ilona summer neutral at char_right
    with dissolve
    systeme "Il fait coulisser la porte. La salle sent le bois ciré. À gauche, les fenêtres donnent sur les montagnes ; à droite, des tabourets bordent un long comptoir. Du linge plié attend près d'un cahier de recettes ouvert."
    laplage "Des amis tenaient cet endroit. Quand ils sont partis à la retraite, je leur ai promis de lui retrouver une vie."
    laplage "J'ai gardé la maison, entretenu la cuisine. Fait coulisser les portes pour aérer le matin. Ça finit par faire beaucoup de matins."
    i "Il est fermé depuis longtemps ?"
    laplage "Quelques années. Les voisins me demandent encore quand ils pourront revenir manger."
    j "Et vous avez gardé tout ça prêt ?"
    laplage "On m'a laissé les clés. J'en ai pris soin."
    systeme "Il passe la main sur le comptoir. La cuisine est juste derrière, ouverte sur la salle : four, plaques, réfrigérateur, cuiseur à riz et vaisselle rangée sur les étagères."
    laplage "Tout fonctionne. Les notices sont dans ce tiroir."
    i "Même celle de la machine à café ?"
    laplage "Surtout celle de la machine à café. Nous avons eu des différends."
    systeme "Ilona s'approche des étagères. Des bols sont empilés près des assiettes ; des ustensiles pendent au-dessus du plan de travail. Elle trouve aussi de petites cuillères dépareillées dans un tiroir."
    show ilona summer smile at char_right
    show jessy beach smile at char_left
    with dissolve
    i "On pourrait faire une soupe le midi. Des tartes, un plat chaud..."
    j "Une petite carte qui change."
    i "Et des portions pour les gens qui viennent de marcher six heures."
    j "Donc tes portions habituelles."
    i "Tu commences à comprendre le projet."

    scene bg family maison with fade
    show jessy beach happy at char_left
    show ilona summer smile at char_right
    show laplage neutral at char_center
    with dissolve
    systeme "Le chemin de pierres les mène à la maison. Ils retirent leurs chaussures avant d'entrer. Le séjour réunit un petit canapé, une table basse et une cuisine ; derrière les panneaux coulissants, une pièce en tatamis prend le soleil."
    systeme "Un escalier de bois monte vers l'étage. Sur la gauche, la grande ouverture donne sur une galerie couverte, puis sur le jardin."
    i "Là, je mettrais mon bureau. La lumière est trop belle."
    j "Pour dessiner ?"
    i "Dessiner. Jouer. Faire mes streams quand j'en ai envie. Je veux garder ça aussi."
    j "Alors faut vérifier la connexion."
    laplage "La fibre arrive dans le salon."
    j "Vous venez de vendre la maison à toute notre génération."
    systeme "Ilona s'approche de l'ouverture sur le jardin. Au-delà de la galerie, les pierres du chemin traversent l'herbe jusqu'aux arbres."
    i "Et celle-là... on verra."
    j "On verra."
    systeme "Elle glisse sa main dans la sienne. Ils restent quelques secondes devant le jardin avant de rejoindre Monsieur Laplage."

    scene bg family salle with fade
    show jessy beach neutral at char_left
    show laplage neutral at char_center
    show ilona summer neutral at char_right
    with dissolve
    systeme "Ils reviennent dans la salle du restaurant. Monsieur Laplage les invite à s'asseoir à une table, près des fenêtres."
    laplage "Alors ?"
    i "J'ai déjà choisi où mettre mes chaussures dans l'entrée."
    j "Moi, je nous ai vus en train de fermer la terrasse le soir."
    i "On voudrait vivre ici. Mais... combien ça coûte ? Le restaurant et la maison ?"
    systeme "Monsieur Laplage pose une chemise cartonnée sur la table."
    laplage "Je vous les donne."
    j "Vous nous..."
    i "Attendez. Les deux ?"
    laplage "Avec les petites cuillères."
    systeme "Ilona attend qu'il sourie. Il ouvre simplement la chemise."
    laplage "Je cherche des repreneurs depuis des années. Des gens qui auront envie d'allumer ici quand je serai parti."
    j "Mais pourquoi nous ?"
    laplage "Je vous ai entendus dans la cuisine. Vous aviez déjà faim de demain."
    laplage "Et vous avez le droit de réfléchir. Les clés seront encore là la semaine prochaine."
    systeme "Jessy regarde Ilona. Elle s'assoit lentement."
    show ilona summer embarrassed at char_right with dissolve
    i "Je pensais qu'on allait demander le prix et repartir en disant que c'était joli."
    j "Moi aussi."
    i "J'en ai envie, Jessy. Même en sachant qu'on va devoir apprendre plein de choses."
    show jessy beach determined at char_left with dissolve
    j "On commencera par ouvrir le midi. On se fera aider pour démarrer."
    i "Et on garde un jour fermé. Pour nous."
    j "Le lundi ?"
    i "Le lundi."
    systeme "Ils parcourent ensemble les documents préparés pour la cession. Posent des questions. Reviennent sur deux paragraphes. Monsieur Laplage attend."
    systeme "Puis Jessy signe. Il tourne la chemise vers Ilona, qui inscrit son nom à côté du sien."
    i "J'ai signé de travers."
    show jessy beach embarrassed at char_left with dissolve
    j "Moi aussi. Ça va bien avec la maison Minecraft."
    systeme "Elle rit en essuyant une larme du bout du doigt."
    laplage "Les formalités restantes sont indiquées ici. Et voici les clés."
    systeme "Le trousseau tombe dans la paume de Jessy. Monsieur Laplage garde un instant sa main sur la sienne."
    laplage "J'ai beaucoup de respect pour le chemin que vous avez fait, Jessy. Prenez soin d'elle."
    show jessy beach smile at char_left
    show ilona summer smile at char_right
    with dissolve
    j "Je l'aime. Je vais faire de mon mieux."
    i "Et moi, je prends soin de lui. Il sait pas encore où on range les petites cuillères."
    show laplage thumb_up at char_center with dissolve
    laplage "Alors je pars rassuré."
    systeme "Ilona tend la main vers le trousseau. Jessy en détache une clé et la lui donne."

    stop music fadeout 2.0
    scene bg family restaurant jour with fade
    show jessy beach neutral at char_left
    show laplage neutral at char_center
    show ilona summer neutral at char_right
    with dissolve
    play ambiant1 audio.windBirds loop volume 0.3 fadein 1.0
    systeme "Les documents rangés, ils raccompagnent Monsieur Laplage dans la cour. Il s'arrête près du portillon."
    laplage "Il est temps de vous dire au revoir."
    i "Vous reviendrez manger ? On vous garde une table."
    systeme "Monsieur Laplage regarde les tables de la cour, puis le rideau vert qui bouge légèrement devant l'entrée."
    laplage "C'est très gentil. Mais cette fois, je ne reviendrai pas."
    j "Vous partez où ?"
    laplage "Me reposer."
    scene cg family laplage adieux with Dissolve(1.2)
    systeme "Il paraît soudain fatigué. Ilona s'approche et le serre dans ses bras. Après un instant de surprise, il l'entoure d'un bras et pose une main sur sa tête."
    i "Merci. Pour cet endroit. Et pour le reste."
    laplage "Vous en ferez de belles choses."
    scene bg family restaurant jour
    show jessy beach neutral at char_left
    show laplage neutral at char_center
    show ilona summer neutral at char_right
    with Dissolve(1.2)
    systeme "Jessy lui serre la main. Il voudrait lui poser toutes les questions accumulées depuis la rivière de Minecraft."
    j "Au revoir, Monsieur Laplage."
    laplage "Au revoir, Jessy. Au revoir, Ilona."
    systeme "Il franchit le portillon. Avant de prendre le sentier, il se retourne vers la maison."
    laplage "Je peux me reposer en paix, désormais."
    show laplage thumb_up at char_center with dissolve
    hide laplage with Dissolve(1.5)
    systeme "Ils le regardent s'éloigner jusqu'au tournant. Il lève une dernière fois le pouce, puis les arbres le cachent."
    systeme "Ils ne reverront jamais Monsieur Laplage."
    pause 1.5
    jump ending_family_chez_nous


# 3. UNE ENSEIGNE ET DU TRAVAIL
label ending_family_chez_nous:
    play music audio.love loop volume 0.6 fadein 2.0
    show jessy beach happy at char_left
    show ilona summer smile at char_right
    with dissolve
    systeme "Ilona referme ses doigts autour de sa clé. Jessy passe un bras autour de ses épaules."
    i "On a une maison."
    j "Et un restaurant."
    i "Redis le premier."
    j "On a une maison."
    systeme "Elle se tourne pour l'embrasser. Le trousseau tinte entre eux."
    i "Il lui faut un nom. Au restaurant."
    j "La Salle Moyennement Importante."
    i "Ça donne envie de réserver moyennement."
    j "Le Creeper Gourmand."
    i "On va éviter de promettre une explosion en cuisine."
    systeme "Elle regarde la terrasse, puis le chemin qui remonte vers le lac."
    i "Les Petits Sommets."
    j "Les Petits Sommets..."
    i "C'est mignon. Et on peut y arriver même quand on est nuls avec une carte."
    j "Je me sens visé par mon propre établissement."
    i "Tu t'y feras."
    systeme "Sur son téléphone, Jessy écrit à Sofiane qu'ils ont terminé. Il efface « la visite » et remplace par « on a les clés »."
    jump ending_family_premier_matin


# Leur premier matin ensemble, avant l'ouverture du restaurant.
label ending_family_premier_matin:
    stop ambiant1 fadeout 1.0
    stop music fadeout 1.5
    scene black with fade
    systeme "Quelques jours plus tard, leurs affaires arrivent dans la maison. Le dernier carton reste dans l'entrée. Ils le videront demain."
    scene bg family maison with fade
    play music audio.mornPiano loop volume 0.55 fadein 1.5
    play ambiant1 audio.windBirds loop volume 0.2 fadein 1.0
    show jessy beach neutral at char_left with dissolve
    systeme "Le lendemain, le soleil traverse déjà le séjour. Dans la cuisine, Jessy tient une poêle d'une main et son téléphone de l'autre."
    j "Retourner délicatement. Oui. Merci."
    systeme "Il pose le téléphone, glisse la spatule sous la pâte et retient son souffle."
    show ilona house neutral at char_right with dissolve
    i "Tu parles à qui ?"
    j "Au petit déjeuner."
    systeme "Ilona s'arrête au pied de l'escalier. Elle regarde la poêle, puis l'assiette posée à côté."
    i "Il t'a répondu quoi ?"
    j "Pour l'instant, il résiste."
    systeme "Elle s'approche, encore à moitié endormie. Un pancake plié sur lui-même occupe le milieu de l'assiette."
    i "Oh. Un petit coussin."
    j "C'était censé être rond."
    i "Il a changé de projet."
    show jessy beach embarrassed at char_left
    j "Je voulais que ce soit prêt quand tu descendrais."
    i "C'est pour ça que t'as quitté le lit sans faire de bruit ?"
    j "J'ai essayé. La troisième marche a tout raconté."
    i "J'ai entendu. J'ai cru que tu te battais avec le carton."
    scene bg family pancakes rate with dissolve
    systeme "Elle passe les bras autour de sa taille et pose le front entre ses omoplates. Jessy garde la poêle bien à plat."
    j "Bonjour, au fait."
    i "Bonjour."
    pause 0.7
    i "Ça sent un peu fort, ton bonjour."
    j "Ah."
    scene bg family maison
    show jessy beach embarrassed at char_left
    show ilona house neutral at char_right
    with dissolve
    systeme "Il baisse le feu. Ilona le lâche juste assez pour regarder par-dessus son bras."
    i "Tu veux que je mette la table ou que je t'aide ?"
    j "Tu peux tenter le prochain ? Je crois que je le retourne trop tôt."
    i "Passe-moi la spatule."
    show ilona house smile at char_right with dissolve
    systeme "Elle verse une petite louche de pâte. Jessy ouvre un placard, puis le referme. Il en ouvre un autre."
    i "Tu cherches quoi ?"
    j "Les tasses."
    i "T'en as une juste à côté de toi."
    j "Je cherchais la tienne."
    i "On les a rangées ensemble, hier."
    systeme "Il baisse les yeux. Deux tasses attendent près de la bouilloire."
    j "Oui. C'est vrai."
    systeme "Il en prend une dans chaque main et reste une seconde devant le plan de travail."
    i "Jessy ?"
    j "D'habitude, je me demande à quelle heure on va se voir."
    systeme "Ilona tourne la tête vers lui."
    j "Là, je me suis réveillé et t'étais là. Et maintenant, tes tasses sont avec les miennes."
    show ilona house embarrassed at char_right with dissolve
    i "Et mes chaussettes sont quelque part dans ton carton de câbles."
    j "Ça, c'est moins romantique."
    i "C'est quand même chez nous."
    show jessy beach happy at char_left with dissolve
    systeme "Il sourit en remplissant la bouilloire. Ilona attend que de petites bulles apparaissent à la surface de la pâte."
    i "Regarde. Je crois que c'est maintenant."
    scene bg family pancakes reussi with dissolve
    systeme "Elle retourne le pancake. Il retombe bien à plat. Tous les deux se penchent pour inspecter le résultat."
    j "Ah oui. Nettement plus rond."
    scene bg family maison
    show jessy beach happy at char_left
    show ilona house smile at char_right
    with dissolve
    i "Merci. J'ouvre un restaurant prochainement."
    j "J'ai entendu dire que ton associé avait du potentiel."
    i "Il fait des coussins comestibles. C'est assez rare."
    systeme "Ils terminent la pâte ensemble. Jessy s'occupe du thé ; Ilona surveille la cuisson. Ils se gênent deux fois en cherchant le même tiroir et finissent par laisser la confiture sur la table basse."
    systeme "Quelques minutes plus tard, ils s'installent sur le canapé avec leurs assiettes. Par l'ouverture sur le jardin, une petite brise fait bouger le rideau."
    j "Attends, je prends le raté."
    i "Trop tard."
    systeme "Ilona coupe un morceau du premier pancake. Elle le goûte avec un sérieux qui inquiète Jessy."
    show jessy beach neutral at char_left
    show ilona house neutral at char_right
    with dissolve
    j "Alors ?"
    i "Ça a le goût d'un pancake."
    j "Tu dis ça pour me rassurer ?"
    i "Non. Pour te rassurer, j'aurais dit qu'il était beau."
    show ilona house smile at char_right
    show jessy beach happy at char_left
    with dissolve
    systeme "Il rit. Elle lui tend une bouchée au bout de sa fourchette."
    i "Tiens."
    systeme "Jessy goûte. Puis il prend le pot de confiture et en ajoute un peu sur le morceau suivant."
    j "D'accord. Ça se défend."
    systeme "Ils mangent un moment sans parler. Dehors, un oiseau se pose au bord du chemin, puis disparaît dans l'herbe."
    i "On fait quoi aujourd'hui ?"
    j "Les cartons. L'enseigne. Les courses. Je voulais mesurer le coin pour ton bureau aussi."
    i "Ça fait beaucoup pour quelqu'un qui a pas fini son thé."
    j "J'ai fait une liste."
    i "Je m'en doute."
    systeme "Elle pose son assiette sur la table basse et ramène ses jambes sur le canapé."
    i "On peut rester là un peu, avant ?"
    systeme "Jessy regarde son téléphone, posé près des tasses. Puis il s'adosse et lui fait une place contre lui."
    j "Oui. Les cartons vont pas partir."
    i "Dommage. J'espérais beaucoup du dernier."
    systeme "Elle se blottit contre son épaule. Il lui embrasse le front."
    i "Il était bien, ton petit déjeuner."
    j "Même le coussin ?"
    i "Surtout le coussin. Mais demain, je fais les œufs."
    j "Et moi ?"
    i "Tu restes avec moi. Et tu fais le thé."
    systeme "Jessy pose sa main sur la sienne. Sur la table basse, leurs deux clés sont restées à côté du pot de confiture."
    pause 1.0
    jump ending_family_preparatifs


label ending_family_preparatifs:

    stop ambiant1 fadeout 1.0
    play music audio.love loop volume 0.6 fadeout 1.0 fadein 1.5
    scene black with fade
    systeme "Les jours suivants sentent la peinture, le café et les premières tartes un peu trop cuites."
    scene bg family salle with fade
    show jessy beach embarrassed at char_left
    show ilona house neutral at char_right
    with dissolve
    systeme "Ils terminent les démarches, suivent les formations nécessaires et font vérifier la cuisine avant l'ouverture. Une ancienne restauratrice du village les aide à préparer leurs premiers services."
    systeme "L'enseigne repeinte sèche dans la cour. Dans la cuisine, Ilona teste les recettes du cahier pendant que Jessy écrit la carte au feutre violet."
    j "J'ai mis six desserts."
    i "On sait en faire trois."
    j "Les trois autres étaient des objectifs."
    i "Mets-les dans un carnet. Là, c'est ce que les gens vont commander."
    j "C'est juste."
    systeme "Le premier samedi, une commande se perd entre le comptoir et la cuisine. Jessy commence à répondre à Ilona sans la regarder."
    i "Jessy. Pose l'assiette deux secondes."
    systeme "Il la pose. Elle lui montre les deux tickets. Ils reprennent depuis le début."
    scene bg family maison with fade
    show jessy beach happy at char_left
    show ilona house neutral at char_right
    with dissolve
    systeme "Après leur premier service du midi, ils s'affalent sur le canapé. Leurs assiettes attendent sur la table basse ; la lumière du jardin traverse encore le séjour."
    i "On a servi vingt-trois personnes."
    j "Et mangé debout quatre fois. Ça fait vingt-sept."
    i "Demain, tu me laisses dormir dix minutes de plus ?"
    j "Je m'occupe du petit déjeuner."
    i "Je t'aime."
    j "Même si c'est du pain ?"
    i "Surtout si c'est du pain."
    systeme "Elle s'endort contre son épaule avant la fin de son thé."
    hide ilona with dissolve
    scene bg arc7 jessy route with fade
    systeme "Le lundi, ils laissent le restaurant fermé et vont marcher sans leurs téléphones."
    jump ending_family_retrouvailles


# 4. UNE GRANDE TABLE
label ending_family_retrouvailles:
    stop ambiant1 fadeout 1.0
    stop music fadeout 1.5
    scene black with fade
    centered "UN MOIS PLUS TARD"
    scene bg family restaurant soir with fade
    play music audio.barjazz loop volume 0.6 fadein 1.5
    show jessy party happy at char_left
    show ilona party smile at char_right
    with dissolve
    systeme "Des guirlandes courent sous les toits. Au-dessus du rideau vert, l'enseigne porte désormais leur nom : Les Petits Sommets. La lumière de la maison éclaire le chemin de pierres."
    systeme "Les Petits Sommets ont déjà leurs habitués. Les voisins viennent pour le plat du jour ; les marcheurs, pour les parts de tarte dont ils parlent au refuge suivant."
    systeme "Ce soir, une feuille couvre les horaires : « Fermé pour une grande occasion. On retrouve nos amis. »"
    i "T'as mis combien d'assiettes ?"
    j "Sept. J'ai recompté."
    i "Moi aussi."
    systeme "Ils attendent devant la terrasse, côte à côte. Ilona essuie une trace de farine sur la joue de Jessy."
    play sound audio.engine volume 0.4
    systeme "Les phares de la Trueno apparaissent au tournant. Allan agite déjà un sac par la fenêtre. Alexandre tient un paquet à plat sur ses genoux. Théo est assis à côté de Sofiane."
    hide jessy
    hide ilona
    show allan party smirk at char_left
    show alex party grin at char_right
    show sofiane party neutral at char_center
    with dissolve
    a "LIVRAISON DE GENS QUI ONT FAIM !"
    x "Tu peux attendre qu'on soit sortis ? Le paquet a pris ton coude dans le dernier virage."
    a "C'est un cadeau solide."
    x "C'est du verre."
    s "Je redescends chercher Micka à la gare. Il arrive par le train suivant."
    j "Tu fais deux voyages ?"
    s "Quatre places. Cinq invités. J'ai consulté l'arithmétique."
    i "Je te mets une assiette de côté."
    s "Une grande."
    hide sofiane with dissolve
    systeme "Allan serre Jessy dans ses bras, puis Ilona, sans poser son sac. Deux bouteilles s'entrechoquent dangereusement."
    a "Regardez-moi ça. Vous avez une enseigne !"
    x "Droite, en plus. J'ai apporté un niveau pour rien."
    j "Tu plaisantes ?"
    systeme "Alexandre sort un petit niveau de sa poche."
    x "Je connais ton travail."

    hide allan
    hide alex
    show jessy party neutral at char_left
    show ilona party neutral at char_right
    show theo party neutral at char_center
    with dissolve
    systeme "Théo reste près du portillon, un paquet de thé dans les mains. Depuis Tokyo, il a repris contact avec Ilona. Quelques messages, puis des excuses, sans lui demander de venir ni de répondre tout de suite."
    systeme "L'invitation pour ce soir, c'est elle qui la lui a envoyée. Après en avoir parlé avec Jessy."
    t "Salut."
    i "Salut, Théo. T'as trouvé une place dans ton planning ?"
    t "J'en ai fait une. Trois jours. Le studio survivra."
    j "Et le trajet depuis Tokyo ?"
    t "Debout depuis cinq heures pour le train. Je vous présente mes excuses à l'avance pour tout ce que je dirai après vingt-deux heures."
    systeme "Il tend le paquet à Ilona."
    t "Pour la maison. J'espère qu'il vous plaira."
    show ilona party smile at char_right with dissolve
    i "Merci. Viens, on va te montrer."
    systeme "Théo regarde Jessy avant de franchir le portillon."
    t "Merci de m'avoir invité."
    show jessy party smile at char_left
    show theo party reassuring at char_center
    with dissolve
    j "Je suis content que tu sois venu."
    systeme "Ils se serrent la main. Allan appelle déjà depuis l'intérieur pour savoir si les biscuits sur le comptoir sont décoratifs."
    scene bg family fete with fade
    show allan party smirk at char_left
    show alex party grin at char_right
    with dissolve
    systeme "Jessy, Ilona et Théo rejoignent les autres dans la salle. Sous les guirlandes, les tables rapprochées forment une longue tablée près des fenêtres. Le pain, la tarte et les théières attendent déjà."
    a "J'en ai goûté un. Pour vérifier."
    x "Trois. Il a vérifié trois fois."
    systeme "Ils posent les cadeaux près du comptoir et commencent à se raconter le voyage en attendant Sofiane et Micka."
    jump ending_family_repas


# 5. CE QU'ILS SONT DEVENUS
label ending_family_repas:
    # On reste dans la salle : Sofiane et Micka rejoignent le groupe à l'intérieur.
    systeme "Un peu plus tard, la porte coulisse. Sofiane entre avec Micka, qui tient un bouquet presque aussi large que lui. Les conversations s'arrêtent pour les accueillir."
    hide alex
    show sofiane party neutral at char_right
    show micka party flowers at char_center
    with dissolve
    systeme "Micka tend les fleurs à Ilona, qui les pose dans un vase sur le comptoir."
    show micka party neutral at char_center with dissolve
    mi "J'ai demandé quelque chose de discret."
    a "Le fleuriste a compris quoi ?"
    mi "Je sais pas. Il m'a souhaité beaucoup de courage."
    systeme "Près du comptoir, Jessy rassemble les cadeaux : du thé, des bouteilles, un tablier. Il déballe le paquet d'Alexandre."
    hide allan
    hide sofiane
    hide micka
    show jessy party smile at char_left
    show alex party grin at char_center
    show ilona party smile at char_right
    with dissolve
    systeme "Dans un cadre, une petite maison colorée faite de blocs. Alexandre l'a dessinée d'après leur première construction Minecraft."
    x "Pour comparer avec les normes actuelles."
    i "On l'accroche ici. Au-dessus du comptoir."
    j "À côté de la carte des desserts ?"
    i "Comme ça, les gens sauront à qui ils ont affaire."
    systeme "Le cadre trouve sa place au-dessus de la cuisine ouverte, à côté des autres maisons en blocs."
    systeme "Ils s'installent. Sofiane remplit son verre de coca ; Ilona choisit le thé. Les autres font circuler les bouteilles."
    hide jessy
    hide ilona
    show allan party neutral at char_left
    show alex party grin at char_right
    with dissolve
    a "Aux retrouvailles ! Et ensuite, chacun raconte. On s'est quittés avec des diplômes, je veux savoir ce que vous en avez fait."
    a "Moi, j'ai trouvé un boulot dans une boutique d'informatique. Je dis aux gens de redémarrer, ils me regardent comme si j'avais inventé l'électricité."
    j "Et Tokyo ?"
    a "J'ai visité. J'ai mangé. J'ai prouvé à Théo qu'on pouvait rater une correspondance en restant dans la bonne gare."
    t "Deux correspondances."
    a "Il vérifie toujours mes exploits."
    x "Moi, je prépare ma rentrée. Et j'ai passé du temps chez mes grands-parents."
    i "À pêcher ?"
    x "Entre autres."
    j "T'as attrapé quelque chose depuis la feuille ?"
    x "Une deuxième feuille. Je commence à comprendre le cycle des saisons."
    show sofiane party neutral at char_center with dissolve
    systeme "Sofiane découpe tranquillement sa part de tarte salée."
    s "Mon cousin m'a laissé la Trueno encore un an."
    a "Il te fait confiance."
    s "Il demande des photos du moteur. Jamais de moi."
    # Seuls Jessy et Ilona connaissent le maid café, et seulement après l'arc IV.5.
    if arc4_5_sofiane_maid:
        hide allan
        hide alex
        show jessy party smile at char_left
        show ilona party neutral at char_right
        with dissolve
        systeme "Pendant qu'Allan et Alexandre discutent des trains avec Théo, Ilona se penche vers Sofiane et baisse la voix."
        i "Tu travailles toujours au café ?"
        s "Oui. J'ai eu une augmentation."
        show ilona party smile at char_right with dissolve
        i "On repassera prendre un chocolat chaud, tous les deux."
        s "Avec plaisir. Et toujours la même discrétion."
        j "Promis."
        systeme "Ils échangent un sourire. À l'autre bout de la table, personne n'a entendu leur aparté."
        hide jessy
        hide ilona
    else:
        a "Et ton boulot, ça se passe bien ?"
        s "J'ai eu une augmentation. La Trueno approuve."
        x "Tu vas finir par nous dire ce que tu fais ?"
        s "Je finance de l'essence."
        systeme "Sofiane boit une longue gorgée de coca. Son lieu de travail reste un mystère pour toute la tablée."
    hide allan
    hide alex
    hide sofiane
    show allan party smirk at char_left
    show ilona party neutral at char_right
    show theo party reassuring at char_center
    with dissolve
    t "Au studio, on a embauché quelqu'un pour les plannings."
    a "Et tu lui laisses faire les plannings ?"
    t "J'ai supprimé deux de mes tableaux."
    a "Combien il en reste ?"
    t "Ce n'est pas le sujet."
    systeme "Il sourit, puis se ressert."
    t "J'aime le travail là-bas. Et je commence à connaître des gens en dehors. On a trouvé un petit cinéma."
    i "Vous y avez vu quoi ?"
    t "Un film vraiment mauvais. J'ai pensé que tu aurais aimé."
    i "Probablement. Envoie-moi le titre."
    t "D'accord."
    hide theo
    hide ilona
    show alex party grin at char_right
    show micka party neutral at char_center
    with dissolve
    mi "Moi, je me suis marié."
    systeme "Le couteau d'Alexandre s'arrête au-dessus de son assiette."
    show alex party awkward at char_right with dissolve
    x "Pardon ?"
    mi "Avec Claire."
    a "Claire... On la connaît ?"
    mi "Claire Martin. Notre ancienne prof d'anglais."
    x "LA PROF D'ANGLAIS ?"
    mi "Ancienne, oui. On a tous fini le lycée en même temps."
    a "On avait suivi cette partie."
    mi "On s'est revus après les diplômes. Et puis voilà."
    j "« Et puis voilà », c'est une manière assez courte de raconter un mariage."
    mi "Il y avait des papiers. J'ai les photos, si vous voulez."
    i "Et elle n'a pas pu venir ?"
    mi "Elle est chez sa sœur ce week-end. Elle vous embrasse. Elle veut venir goûter la tarte."
    x "J'ai passé un oral avec ta partenaire."
    mi "Elle t'avait trouvé très tendu."
    x "ÇA S'ARRANGE PAS."
    systeme "Ilona manque de renverser son thé en riant. Micka lui passe une serviette avec le plus grand sérieux."

    hide micka
    hide allan
    hide alex
    show jessy party happy at char_left
    show ilona party smile at char_right
    with dissolve
    a "Bon. À vous deux. La montagne, la maison, le restaurant. On veut la version avec les détails."
    i "On s'est perdus."
    j "On a légèrement débordé de l'itinéraire."
    i "Tu tenais la carte à l'envers."
    a "Ça arrive aux meilleurs."
    systeme "Ils racontent la rivière, le lac et le bivouac. Ilona raconte aussi le moment où elle a dit à Jessy qu'elle l'aimait."
    i "Il a cherché quoi répondre. J'ai cru qu'il allait m'expliquer un truc avec des blocs."
    j "J'ai failli."
    i "Finalement, c'était bien."
    systeme "Sous la table, elle serre sa main."
    j "Puis on a reçu la même annonce. On a appelé, on est venus... et Monsieur Laplage a ouvert la porte."
    t "Le Messi. Évidemment."
    a "J'avais une théorie sur lui."
    x "Tu en avais un classeur."
    a "Oui, mais aucune avec un acte de propriété."
    systeme "Les rires s'apaisent quand Ilona raconte les clés et le départ."
    show jessy party neutral at char_left
    show ilona party neutral at char_right
    with dissolve
    i "Il a dit qu'on le reverrait plus."
    j "Cette fois, je crois que c'était vraiment un au revoir."
    systeme "Allan baisse les yeux vers le bois de la table. Alexandre fait tourner son verre sans boire."
    s "Alors il a choisi un bel endroit à laisser derrière lui."
    systeme "Ilona regarde ses amis, les plats entamés, le cadre accroché au-dessus du comptoir."
    i "On veut que ça reste comme ça. Un endroit où les gens ont envie de revenir."
    j "On va garder une petite carte. Prendre le temps d'apprendre."
    i "Et vivre dans la maison. Vraiment. J'ai déjà installé mon bureau."
    show jessy party smile at char_left
    show ilona party embarrassed at char_right
    with dissolve
    j "Un jour, on aimerait avoir des enfants. On en parle."
    i "On s'entraîne d'abord avec les plantes. Il y en a une qui nous fait pas confiance."
    a "Elle vous a vus construire sur Minecraft."
    show ilona party smile at char_right
    show allan party smirk at char_center
    with dissolve
    systeme "Allan lève son verre."
    a "À Jessy et Ilona. À votre maison, à votre resto... et à la plante, qui va devoir s'accrocher."
    x "Aux Petits Sommets !"
    t "À vous deux."
    mi "Et à Claire, qui aurait vraiment aimé cette tarte."
    scene cg family toast with Dissolve(1.0)
    systeme "Les sept verres se rejoignent au-dessus de la table."
    jump ending_family_fete


# 6. UNE PISTE DE DANSE IMPROVISÉE
label ending_family_fete:
    scene bg family fete fin with dissolve
    systeme "Le repas dure. Les plats vides laissent place aux desserts, puis aux photos sur les téléphones."
    hide jessy
    hide ilona
    show allan party smirk at char_left
    show theo party reassuring at char_center
    show alex party grin at char_right
    with dissolve
    a "Attends, c'est la photo de Tokyo ? Pourquoi vous êtes flous tous les deux ?"
    t "Parce que tu as bougé."
    a "Tu as littéralement rejoint la photo après son départ."
    x "Artistiquement, c'est très cohérent avec votre sens de l'orientation."
    systeme "Ilona réchauffe de l'eau. Sofiane repousse la bouteille de vin qu'Allan lui tend par réflexe et désigne son verre de coca."
    hide theo
    hide alex
    show sofiane party neutral at char_center
    show ilona party smile at char_right
    with dissolve
    s "Je ramène tout le monde."
    a "Exact. Pardon, capitaine."
    hide allan
    hide sofiane
    show jessy party smile at char_left
    with dissolve
    j "Et toi, toujours au thé ?"
    i "Quelqu'un doit pouvoir vous arrêter quand vous allez décider de pousser les meubles."
    systeme "Une heure plus tard, elle aide Jessy à décaler une chaise pour dégager le passage entre la grande table et les tabourets du comptoir."
    i "Doucement. J'ai dit doucement !"
    j "C'est étroit pour une carrière dans la danse."
    systeme "Les bouteilles sont presque vides. Jessy a les joues rouges ; Théo et Micka rient depuis deux minutes d'une blague dont ils ont oublié le début. Allan rejoint le petit poste posé au fond de la salle."
    systeme "Alexandre annonce qu'il connaît un branchement qui va améliorer l'acoustique ; Sofiane lui retire une rallonge des mains."
    hide jessy
    hide ilona
    show sofiane party neutral at char_left
    show alex party awkward at char_right
    with dissolve
    s "C'est le réfrigérateur."
    x "Ah."

    # Le fond de soirée accompagne le montage ; Baka Mitai attend le tour de Théo.
    hide sofiane
    show allan party smirk at char_left
    show alex party grin at char_right
    with dissolve
    systeme "Allan ouvre le karaoké avec un générique d'anime qu'il connaît surtout par ses cris. Alexandre enchaîne sur du rock et remercie un public qui se trouve à un mètre cinquante."
    a "Un mot pour tes fans ?"
    x "Éloignez-vous des enceintes."
    hide allan
    show micka party neutral at char_center
    show alex party awkward at char_right
    with dissolve
    systeme "Micka choisit une chanson d'amour en anglais. Sa prononciation provoque un silence admiratif, puis un regard collectif vers Alexandre."
    x "Je ne dirai rien."
    mi "Vous avez reconnu ?"
    x "Je ne dirai. Rien."
    hide micka
    hide alex
    show sofiane party neutral at char_center
    with dissolve
    systeme "Sofiane accepte un tour au micro. Il chante assis, les mains posées comme sur un volant, et ne rate aucune entrée."
    hide sofiane
    show ilona party smile at char_right
    with dissolve
    systeme "Ilona chante ensuite son morceau préféré, une petite chanson pop que Jessy l'a souvent entendue fredonner en construisant."
    show jessy party smile at char_left with dissolve
    systeme "Il la rejoint au dernier refrain, beaucoup trop bas."
    i "Tu peux monter un peu."
    j "Je suis déjà à mon sommet."
    hide ilona
    hide jessy
    show allan party smirk at char_left
    show theo party neutral at char_center
    with dissolve
    # Un extrait chanté laisse le temps au gag d'exister sans imposer le morceau entier.
    play music "<from 22 to 58>audio/music/Baka_Mitai.ogg" noloop volume 0.55 fadeout 1.0 fadein 1.0
    scene bg family karaoke with dissolve
    systeme "Théo prend enfin le micro. Pour Baka Mitai, il redresse une chaise, remonte ses manches et se tourne vers un verre comme s'il avait ruiné sa vie."
    a "Il a répété."
    t "Chut."
    window hide
    pause 8.0
    window show
    systeme "Il n'en faut pas davantage à Jessy pour perdre tout contrôle de son rire. Théo tient encore trois secondes avant de rire aussi."
    scene bg family fete fin with dissolve
    show jessy party happy at char_left
    show theo party smirk at char_right
    with dissolve
    t "Jessy. Une dernière épreuve."
    j "Je sens que ça va me faire regretter d'avoir mangé."
    t "Battle de danse. Yakuza 0. Toi, Kiryu. Moi, Majima."
    j "Pourquoi t'as déjà choisi le personnage le plus souple ?"
    t "Parce que je tiens encore debout."
    show ilona party neutral at char_center with dissolve
    i "Sofiane, tu surveilles les chaises. Je surveille les deux idiots."
    play music audio.barjazz loop volume 0.6 fadein 1.0
    systeme "Allan remet le fond musical de la soirée. Les deux adversaires décident que ça fera parfaitement l'affaire."
    systeme "Allan annonce le combat dans une cuillère. Sous les guirlandes, Micka applaudit comme si la salle était immense. Alexandre compte un rythme qui ne correspond à aucune musique présente."
    systeme "Jessy prend une pose héroïque. Théo pivote, rate son demi-tour et se rattrape au dossier d'une chaise."
    j "Esquive parfaite."
    t "Élément du décor. C'était prévu."
    systeme "Jessy tente de répondre par un pas glissé. Sa chaussette accroche le sol. Il finit accroupi devant Ilona, une main tendue comme s'il avait voulu faire ça depuis le début."
    show ilona party smile at char_center with dissolve
    i "Très jolie demande d'aide."
    systeme "Elle le relève. Théo applaudit avec les autres, essoufflé."
    a "Verdict du jury ?"
    show ilona party neutral at char_center with dissolve
    i "La salle gagne. Vous arrêtez avant de casser quelque chose."
    systeme "Ils finissent tous par danser ensemble, sauf Sofiane qui filme douze secondes à la demande générale, puis range son téléphone pour taper dans ses mains."
    show ilona party smile at char_center with dissolve
    jump ending_family_depart


# 7. À LA PROCHAINE
label ending_family_depart:
    stop music fadeout 2.0
    scene bg family restaurant nuit with fade
    play ambiant1 audio.forestNight loop volume 0.3 fadein 1.0
    show allan party smirk at char_left
    show sofiane party neutral at char_center
    show alex party grin at char_right
    with dissolve
    systeme "La cuisine est rangée. Ils ont laissé les lumières et les guirlandes allumées pour les départs. Devant le restaurant, les au revoir prennent plus de temps que prévu."
    a "Je vais vous mettre cinq étoiles."
    x "Tu peux commencer par mettre tes chaussures."
    a "Je préservais le parquet."
    hide allan
    hide alex
    show micka party neutral at char_center
    hide sofiane
    show jessy party smile at char_left
    show ilona party smile at char_right
    with dissolve
    mi "On revient avec Claire. Elle me demande déjà la recette."
    i "Vous venez quand vous voulez. On vous garde une vraie part, pas les miettes d'Allan."
    hide micka
    show theo party reassuring at char_center
    with dissolve
    t "Merci pour ce soir. C'était... ça m'a fait du bien."
    j "À nous aussi. Bon retour à Tokyo."
    t "Je vous envoie le titre du film demain."
    i "J'attends ça."
    systeme "Théo leur fait un signe de la main. Sofiane ouvre la voiture."
    hide theo
    show sofiane party neutral at char_center
    with dissolve
    s "Premier voyage : Allan, Alexandre et Théo. Micka, je reviens te chercher."
    mi "Je vais aider pour la vaisselle."
    i "Tu vas surtout repartir avec le reste du gâteau."
    mi "Je peux faire les deux."
    s "Dernière chose."
    systeme "Sofiane se tourne vers ses passagers avec un calme redoutable."
    hide jessy
    hide ilona
    show alex party concerned at char_right
    with dissolve
    s "Si l'un de vous vomit dans ma Trueno, il ne reverra plus la lumière du jour."
    systeme "Alexandre déglutit."
    x "Tu pourrais ouvrir ma fenêtre ?"
    s "Elle est déjà ouverte."
    x "Davantage."
    play sound audio.engineStart volume 0.35
    hide sofiane
    hide alex
    with dissolve
    systeme "La Trueno s'éloigne doucement. À la première courbe, Allan passe la main par la fenêtre pour un dernier salut."
    stop ambiant1 fadeout 1.0
    scene bg family fete rangement with fade
    show micka party neutral at char_left
    show ilona party smile at char_right
    with dissolve
    systeme "Ils rentrent dans la salle. Micka essuie les derniers verres pendant qu'Ilona emballe le gâteau."
    scene bg family restaurant nuit with fade
    play ambiant1 audio.forestNight loop volume 0.3 fadein 1.0
    show sofiane party neutral at char_left
    show micka party neutral at char_right
    with dissolve
    systeme "Au retour de Sofiane, ils ressortent avec les paquets. Le chauffeur reçoit le sien, puis emmène le dernier invité."
    hide sofiane
    hide micka
    with dissolve

    play music audio.realLove loop volume 0.55 fadein 1.5
    show jessy party happy at char_left
    show ilona party smile at char_right
    with dissolve
    systeme "Ilona verrouille le restaurant. Jessy reste une seconde devant l'enseigne."
    i "Tu viens ?"
    j "Oui. Je regardais."
    i "Quoi ?"
    j "Tout ça. Ce matin, je cherchais encore les serviettes. Et là, j'ai l'impression qu'on habite ici depuis toujours."
    systeme "Ilona pose sa tête contre son épaule."
    i "Elles étaient où, finalement ?"
    j "Dans le tiroir des serviettes."
    i "T'as bien fait de m'emmener vivre avec toi."
    scene cg family entrance kiss with Dissolve(1.0)
    systeme "Il l'embrasse sous les guirlandes de l'entrée. Puis ils empruntent le chemin de pierres jusqu'à la maison."
    stop ambiant1 fadeout 1.5
    stop music fadeout 2.0
    scene black with fade
    jump ending_family_annonce


# 8. « JE VAIS ÊTRE PAPA ? »
label ending_family_annonce:
    centered "QUELQUES JOURS PLUS TARD"
    scene bg family jardin jour with fade
    play music audio.love loop volume 0.55 fadein 1.5
    play ambiant1 audio.windBirds loop volume 0.3 fadein 1.0
    show jessy beach happy at char_left
    show ilona house smile at char_right
    with dissolve
    systeme "Lundi. Jessy et Ilona sont assis dans l'herbe, sous le grand arbre, près du banc. À côté du chemin, une petite parcelle de terre attend leurs premières plantations. Un catalogue de graines est ouvert sur les genoux de Jessy."
    i "Tu prépares quoi ?"
    j "Des tomates. Peut-être des fraises."
    i "Des fraises. Beaucoup."
    j "J'avais deviné."
    systeme "Elle pose sa joue sur son épaule. Il lui embrasse les cheveux."
    j "Ça te plaît, ici ? Maintenant qu'on a vu la montagne du linge sale ?"
    i "Oui. Même avec tes chaussettes."
    j "Je t'aime aussi."
    systeme "Ilona rit tout bas. Puis elle lui prend le catalogue des mains et le pose dans l'herbe."
    i "J'ai une bonne nouvelle."
    show jessy beach neutral at char_left
    show ilona house embarrassed at char_right
    with dissolve
    j "Qu'est-ce qu'il y a ?"
    systeme "Elle inspire. Ses yeux brillent avant qu'elle arrive à parler."
    i "Tu vas être papa."
    show jessy beach surprised at char_left with dissolve
    pause 0.6
    systeme "Jessy se fige, les yeux grands ouverts. Sa bouche s'entrouvre, mais aucun son ne sort. Il regarde Ilona, puis son ventre, puis Ilona de nouveau."
    j "Attends... quoi ? Toi... on va avoir un bébé ?"
    i "Oui."
    j "Un bébé. Nous deux. Vraiment ?"
    i "Vraiment."
    show jessy beach smile at char_left
    show ilona house smile at char_right
    with dissolve
    systeme "Il commence à sourire, porte une main à sa bouche et laisse échapper un rire tremblant. Ilona se rapproche de lui."
    i "Viens là."
    systeme "Il la serre contre lui. Quand elle se recule un peu, il garde ses mains dans les siennes."
    stop music fadeout 1.5
    hide ilona with Dissolve(1.2)
    show jessy beach smile at family_jessy_centre
    pause 1.2
    j "Je vais être papa ?"
    # Révélation en une seule coupe : nouveau décor et sprite papa ensemble.
    stop ambiant1
    scene bg family jardin soir
    show jessy papa neutral at char_center
    with None
    pause 1.5
    play music family_music("audio/music/family_save_the_world.ogg", audio.springHope) loop volume 0.65
    jump ending_family_lucy


# 9. LUCY ET OLIVER
label ending_family_lucy:
    systeme "Plusieurs années plus tard. Le même arbre ombrage le banc. De l'autre côté du chemin, des légumes et des fraisiers remplissent maintenant la petite parcelle. Le ciel rosit derrière les montagnes."
    systeme "Au pied de la galerie en bois, deux bottes roses minuscules attendent près des chaussures des parents. Sur la porte du cabanon, Lucy a dessiné une porte plus petite à la craie rose."
    j "Les soirées commencent à se rafraîchir..."
    family_lucy "Papa !"
    show jessy papa neutral at char_left
    show lucy neutral at char_center
    with dissolve
    systeme "Lucy traverse le jardin en courant. Elle cache quelque chose derrière son dos avec une discrétion qui la fait marcher de travers."
    j "Oh. Une visite."
    family_lucy "Ferme les yeux."
    j "C'est fait."
    family_lucy "Les deux."
    systeme "Il ferme le deuxième. De petites mains déposent un bouquet dans les siennes."
    family_lucy "Voilà !"
    systeme "Des fleurs sauvages, trois brins d'herbe et une pâquerette presque sans tige. Un peu de terre lui tombe sur le pantalon."
    j "C'est pour moi ?"
    show lucy happy at char_center with dissolve
    family_lucy "Oui. Parce que je t'aime."
    scene cg family lucy hug with Dissolve(1.0)
    systeme "Jessy s'accroupit. Lucy se jette contre lui avant même qu'il ait fini d'ouvrir les bras."
    j "Merci, ma chérie. Elles sont magnifiques."
    scene bg family jardin soir
    show jessy papa neutral at char_left
    show lucy neutral at char_center
    with dissolve
    family_lucy "La petite, elle s'est cassée. Je l'ai prise quand même."
    j "On lui trouvera un tout petit verre."
    family_lucy "Celui avec le canard !"
    j "Parfait. Il attendait une mission importante."
    systeme "Elle pose un doigt sur une fleur jaune."
    family_lucy "Celle-là, c'est un soleil. Et celle-là, c'est toi."
    j "Je suis celle qui a perdu un pétale ?"
    family_lucy "Oui. T'es décoiffé."
    j "Ressemblance troublante."
    systeme "Lucy essaie de lui aplatir les cheveux. Ils se redressent aussitôt. Elle recommence, très concentrée."

    # Ilona apparaît seulement lorsqu’elle sort de la maison, enceinte d’Oliver.
    show jessy papa neutral at char_left
    show ilona house pregnant at char_right
    with dissolve
    systeme "Ilona sort de la maison, une main posée sur son ventre rond. Elle traverse la galerie en bois et descend la marche pour les rejoindre."
    i "Vous êtes mignons, tous les deux."
    show lucy happy at char_center with dissolve
    family_lucy "Non ! C'est toi la plus belle, maman !"
    i "Ah. Je vais accepter la correction."
    j "Moi, je suis décoiffé. Le classement est très précis."
    show lucy neutral at char_center with dissolve
    systeme "Lucy court embrasser sa mère, puis revient prendre la main de Jessy. Elle tient à rester entre eux."
    j "Et Oliver ? Il est calme ?"
    i "Il fait sa randonnée dans mon ventre. Je crois qu'il a trouvé la montée."
    j "Il a une carte ?"
    i "Vu la direction des coups de pied, une des tiennes."
    systeme "Jessy éclate de rire. Lucy regarde le ventre de sa mère avec sérieux."
    family_lucy "Oliver ! La sortie, c'est pas par là !"
    systeme "Ilona rit à son tour, puis guide la petite main de Lucy sur son ventre."
    i "Attends... là."
    systeme "Lucy écarquille les yeux."
    family_lucy "Il m'a répondu !"
    show lucy happy at char_center with dissolve
    j "Il a peut-être entendu les indications."
    show lucy neutral at char_center with dissolve
    family_lucy "Quand il arrive, je lui prête mes cubes. Mais pas le rouge."
    i "Il faudra lui laisser un peu de temps avant de construire. Au début, il dormira beaucoup."
    family_lucy "Je lui ferai la maison pendant qu'il dort."
    j "Avec une porte ?"
    family_lucy "Deux. Pour quand on veut sortir en même temps."
    systeme "Jessy regarde Ilona au-dessus de leur fille. Elle lui adresse le sourire qu'il connaît depuis leur première maison."
    i "Bonne idée, deux portes."
    family_lucy "Et une chambre pour vous. Comme ça, vous pouvez venir."
    j "Alors on viendra."
    systeme "Une brise soulève les cheveux de Lucy. Jessy lui frotte doucement les bras pour la réchauffer."
    j "On va rentrer avant d'avoir froid."
    i "C'est justement pour ça que je venais. Le repas est prêt."
    family_lucy "Y a de la tarte ?"
    j "Tu veux savoir ce qu'il y a avant ?"
    family_lucy "Pourquoi ?"
    systeme "Ilona se mord la lèvre pour ne pas rire. Jessy lui tend le bouquet pendant qu'il récupère son propre gilet, oublié sur le banc."
    i "Il y a de la tarte. Après."
    family_lucy "Alors on rentre vite."
    systeme "Lucy prend une main de chaque côté. Tous les trois remontent le chemin de dalles. À chaque troisième pas, elle essaie de se balancer entre eux."
    systeme "La fenêtre de la cuisine est éclairée. Sur la table, le petit verre au canard attend les fleurs."
    scene cg family homecoming with Dissolve(1.5)
    systeme "Jessy tient la porte. Ilona entre avec Lucy, puis se retourne vers lui."
    i "Tu viens ?"
    j "Oui."
    pause 1.0
    stop music fadeout 2.0
    stop ambiant1 fadeout 2.0
    scene black with Dissolve(2.0)
    pause 0.5
    systeme "Ils vécurent heureux et eurent beaucoup d'enfants."
    jump ending_family_generique


label ending_family_generique:
    play music family_music("audio/music/family_hopes_dreams_save_last_goodbye.ogg", audio.realLove) noloop volume 0.65 fadein 1.0
    centered "GOOD ENDING\n\nFAMILY"
    centered "[config.name!t]\n\nJessy et Ilona\nLes Petits Sommets"
    centered "Avec\n\nAllan, Alexandre, Sofiane\nThéo et Micka\n\nMonsieur Laplage\n\nLucy et Oliver"
    # Cartons cliquables : le générique n'impose pas la durée de la piste.
    if renpy.loadable("audio/music/family_hopes_dreams_save_last_goodbye.ogg"):
        centered "Musique du générique\n\nUNDERTALE — Toby Fox\nHopes and Dreams / SAVE the World / Last Goodbye"
    centered "Merci d'avoir partagé leur histoire."
    stop music fadeout 2.0
    scene black with fade
    return
