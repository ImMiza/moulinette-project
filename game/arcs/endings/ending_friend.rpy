# GOOD ENDING (FRIEND) — LE DERNIER ÉTÉ
# Scénario : agents/friend_ending ; continuité : agents/cartographies.
# Neuf scènes, puis générique. Aucun nouveau choix ni changement de score.
# Décors dédiés et photos de groupe intégrés.

# Affichage plein écran sans déformer les proportions des illustrations.
image bg friend chambre jessy = Transform("images/scenes/backgrounds/friend/bg_friend_chambre_jessy.png", xysize=(1920, 1080), fit="cover")
image bg friend chambre ilona = Transform("images/scenes/backgrounds/friend/bg_friend_chambre_ilona.png", xysize=(1920, 1080), fit="cover")
image bg friend appel = Transform("images/scenes/backgrounds/friend/bg_friend_appel_alexandre.png", xysize=(1920, 1080), fit="cover")
image bg friend discord cinq = Transform("images/scenes/backgrounds/friend/bg_friend_discord_cinq.png", xysize=(1920, 1080), fit="cover")
image bg friend discord six = Transform("images/scenes/backgrounds/friend/bg_friend_discord_six.png", xysize=(1920, 1080), fit="cover")
image bg friend appartement = Transform("images/scenes/backgrounds/friend/bg_friend_appartement_allan.png", xysize=(1920, 1080), fit="cover")
image bg friend appartement repas = Transform("images/scenes/backgrounds/friend/bg_friend_appartement_allan_repas.png", xysize=(1920, 1080), fit="cover")
image bg friend gare matin = Transform("images/scenes/backgrounds/friend/bg_friend_gare_matin.png", xysize=(1920, 1080), fit="cover")
image bg friend promenade depart = Transform("images/scenes/backgrounds/friend/bg_friend_promenade_depart.png", xysize=(1920, 1080), fit="cover")
image bg friend promenade arrivee = Transform("images/scenes/backgrounds/friend/bg_friend_promenade_arrivee.png", xysize=(1920, 1080), fit="cover")
image bg friend minecraft ouvert = Transform("images/scenes/backgrounds/minecraft/bg_friend_minecraft_trou_ouvert.png", xysize=(1920, 1080), fit="cover")
image bg friend minecraft ferme = Transform("images/scenes/backgrounds/minecraft/bg_friend_minecraft_trou_ferme.png", xysize=(1920, 1080), fit="cover")
image jessy home neutral = speaker_sprite("jessy", "images/personnages/Jessy/home/neutral_attentiveness.png", 842, 1264)
image alex home grin = speaker_sprite("alex", "images/personnages/Alexandre/home/playful_grin.png", 842, 1264)
image allan beach embarrassed = speaker_sprite("allan", "images/personnages/Allan/beach/awkward_embarrassment.png")
image alex beach neutral = speaker_sprite("alex", "images/personnages/Alexandre/beach/neutral.png")
image alex beach awkward = speaker_sprite("alex", "images/personnages/Alexandre/beach/akward_realization.png")
image alex beach support = speaker_sprite("alex", "images/personnages/Alexandre/beach/supportive_encouragement.png")
image sofiane beach smirk = speaker_sprite("sofiane", "images/personnages/Sofiane/beach/cryptic_smirk.png")
image theo beach smirk = speaker_sprite("theo", "images/personnages/Théo/beach/knowing_smirk.png", 842, 1264, THEO_CROP_BOTTOM)

# Photos prises par Ilona ; le même cadrage permet le comparatif final.
image cg friend premier ete = Transform("images/scenes/cg/friend/cg_friend_photo_premier_ete.png", xysize=(1920, 1080), fit="cover")
image cg friend retrouvailles = Transform("images/scenes/cg/friend/cg_friend_photo_retrouvailles.png", xysize=(1920, 1080), fit="cover")

image cg friend chateau = Transform("images/scenes/cg/friend/cg_friend_chateau_sable.png", xysize=(1920, 1080), fit="cover")
image cg friend salut brindille = Transform("images/scenes/cg/friend/cg_friend_salut_brindille.png", xysize=(1920, 1080), fit="cover")
image cg friend raquettes = Transform("images/scenes/cg/friend/cg_friend_raquettes.png", xysize=(1920, 1080), fit="cover")


label ending_friend:
    $ record_ending("friend")
    stop music fadeout 1.5
    stop ambiant1 fadeout 1.5
    stop sound fadeout 0.5
    $ fade_channel("music", 1.0, 0.0)
    $ fade_channel("ambiant1", 1.0, 0.0)
    scene black with fade
    centered "LE DERNIER ÉTÉ"
    jump ending_friend_distance


# 1. APRÈS LA RANDONNÉE
label ending_friend_distance:
    scene bg arc2 minecraft house summer night with fade
    play music audio.mcnight loop volume 0.5 fadein 1.5
    show jessy minecraft at char_left with dissolve

    systeme "Le soir du retour, Jessy se connecte. Il apparaît devant la maison, son inventaire encore rempli de choses dont il a oublié l'usage."
    systeme "Il ouvre un coffre. Du bois, du verre bleu. De quoi construire une petite terrasse au-dessus de l'eau. Ilona aimerait sûrement ça."
    systeme "Il compte les blocs, en prend deux piles. Puis il s'arrête devant la porte."
    systeme "Au bivouac, il a promis de ne pas essayer de réparer sa peine en étant partout autour d'elle."
    systeme "Il remet le verre dans le coffre. Le bois aussi. Il se déconnecte sans laisser de panneau."

    scene bg friend chambre jessy with fade
    show jessy home neutral at char_left with dissolve
    systeme "Quelques jours plus tard, il lui écrit depuis sa chambre."
    j "{i}« Ça te dit une partie ce soir ? »{/i}"
    systeme "La réponse arrive pendant qu'il range son bureau."
    i "{i}« Je préfère rester seule ce soir. »{/i}"
    j "{i}« D'accord. Bonne soirée, Ilona. »{/i}"
    systeme "Il pose le téléphone sur l'étagère. Sous une tasse, il retrouve enfin la feuille qu'il cherchait depuis le matin. Le rond de thé tombe exactement sur son nom."
    j "Bon. Ça se voit que c'est à moi."

    scene bg arc2 minecraft house summer night with fade
    show jessy minecraft at char_left
    show alex minecraft at char_right
    with dissolve
    play music audio.mc loop volume 0.55 fadeout 1.0 fadein 1.0
    play sound audio.discord volume 0.3
    systeme "Le vendredi, Alexandre l'appelle. Son personnage attend devant la maison avec une pelle et absolument aucune provision."
    x "J'ai trouvé un endroit."
    j "Quel genre d'endroit ?"
    x "Un trou. Mais très loin."
    j "On en a déjà ici."
    x "Tu comprendras sur place."
    systeme "Jessy regarde le coffre près de la porte, puis prend du pain pour deux."
    j "Bon. Montre-moi ton trou."

    scene bg friend minecraft ouvert with fade
    show jessy minecraft at char_left
    show alex minecraft at char_right
    with dissolve
    systeme "Ils marchent vingt minutes. Au milieu d'une étendue de pierre, Alexandre s'arrête devant une cavité large de deux blocs."
    j "C'est ça ?"
    x "Descends."
    systeme "Jessy saute dedans. À hauteur de ses yeux : de la pierre. Au-dessus : un carré de ciel."
    j "Je comprends mieux."
    x "Tu vois ?"
    j "Non."
    systeme "Alexandre descend à son tour, puis pose un bloc au-dessus d'eux. Le ciel disparaît."
    scene bg friend minecraft ferme
    show jessy minecraft at char_left
    show alex minecraft at char_right
    with dissolve
    x "J'ai amélioré l'acoustique."
    j "On sort comment ?"
    x "Il faudrait casser quelque chose."
    j "Dans Minecraft ? T'es sûr ?"
    systeme "Jessy rit dans son micro. Alexandre essaie de poser une pancarte dans le noir et leur condamne le peu d'espace qui restait."
    x "Attends. Bouge pas."
    j "Ça devrait aller."
    systeme "Ils y restent jusqu'à ce que le pain manque."

    stop music fadeout 1.5
    scene bg friend chambre ilona with fade
    show ilona house neutral at char_center with dissolve
    systeme "Chez elle, Ilona remplit une page de petites maisons. Elle efface un toit, troue presque le papier, tourne la page."
    systeme "Sur l'ordinateur, son logiciel de diffusion est ouvert. Elle vérifie le micro, rapproche sa lampe, puis éloigne la tasse du bord du bureau."
    i "Bon. Une heure. On essaie."
    play music audio.stream loop volume 0.4 fadein 1.0
    show ilona house smile at char_center with dissolve
    i "Salut ! Ce soir, je dessine. Vous pouvez proposer des idées, mais je vous préviens, je sais surtout faire des fenêtres de travers."
    tchat "pixel_ramen : on voit ton écran d'attente"
    show ilona house embarrassed at char_center with dissolve
    i "Ah. C'est une fenêtre très droite, du coup. Profitez."
    systeme "Elle change de scène. Le dessin apparaît, minuscule, dans un coin."
    tchat "kiwi_no_kimi : elle est loin la maison"
    show ilona house smile at char_center with dissolve
    i "Quartier calme. Très calme. Attendez, je vous rapproche."
    systeme "Une heure plus tard, elle rit encore en essayant de dessiner un escalier pour une limace. Il n'y a que quelques pseudos dans le tchat ; chacun a son avis sur la rampe."
    stop music fadeout 1.5
    show ilona house neutral at char_center with dissolve
    systeme "Après avoir coupé la diffusion, elle photographie la page. Son pouce ouvre la conversation de Jessy avant qu'elle y pense."
    systeme "Elle reste devant son dernier « Bonne soirée ». Puis elle ferme la conversation et envoie le dessin dans le groupe."
    i "{i}« Voilà ce qu'on a fait. La limace prendra finalement l'ascenseur. »{/i}"

    scene black with fade
    play music audio.mornPiano loop volume 0.45 fadein 1.0
    systeme "Les semaines passent. Allan envoie des photos de repas. Alexandre signale une fuite dans son appartement en précisant qu'il n'a touché à aucun mur."
    systeme "Théo revient dans les échanges par petites touches : une réponse à Allan, une photo de Tokyo, le titre d'un film. Parfois, personne ne répond avant le lendemain."
    systeme "Un soir, Ilona partage un extrait de son dernier stream. Cette fois, le son et le dessin ont commencé en même temps."
    j "{i}« J'ai regardé. Le phare avec les jambes m'a achevé. »{/i}"
    i "{i}« Il déménage quand la vue lui plaît plus. »{/i}"
    j "{i}« Il a raison. Bravo pour le live. »{/i}"
    systeme "Ilona répond avec un petit phare dessiné dans la marge. Jessy sourit, puis reprend le jeu qu'il avait lancé."
    jump ending_friend_invitation


# 2. UNE JOURNÉE AVANT LES DÉPARTS
label ending_friend_invitation:
    scene bg friend chambre ilona with fade
    show ilona house neutral at char_right with dissolve
    systeme "Vers la fin de l'été, Ilona cherche un soir pour jouer avec tout le monde. La conversation se remplit de jours barrés."
    a "{i}« Mardi, j'ai mes nouveaux horaires. Pour l'instant, même mon responsable sait pas. »{/i}"
    x "{i}« Jeudi, visite d'appartement. Vendredi, probablement visite d'un autre appartement. »{/i}"
    s "{i}« Service du soir toute la semaine. »{/i}"
    j "{i}« Lundi, je commence ma formation. Je vous dirai pour les soirées. »{/i}"
    systeme "Ilona ouvre son propre agenda, puis revient aux messages."
    i "{i}« Et dimanche ? La plage. Celle où Alexandre a essayé de construire une ville. »{/i}"
    x "{i}« C'était un château. »{/i}"
    a "{i}« Avec une zone industrielle. »{/i}"
    i "{i}« J'ai envie de vous voir avant qu'il faille réserver trois semaines pour manger des chips ensemble. »{/i}"
    j "{i}« Dimanche, je peux. »{/i}"
    show ilona house smile at char_right with dissolve
    a "{i}« Je prends le repas. »{/i}"
    x "{i}« Est-ce qu'une vraie pelle entre dans un train ? »{/i}"
    s "{i}« Je prends la voiture et les affaires encombrantes. La pelle voyagera dans une housse. »{/i}"
    x "{i}« Elle a sa housse. »{/i}"
    a "{i}« Évidemment qu'elle a sa housse. »{/i}"
    systeme "Théo répond un peu plus tard."
    t "{i}« Vous passez par quelle gare ? Je peux vous rejoindre à la correspondance depuis Tokyo. »{/i}"
    systeme "Ilona lui transmet le trajet."
    i "{i}« On se retrouve devant le panneau des départs. Ça te laisse assez de temps ? »{/i}"
    t "{i}« Oui. Je serai là. Merci pour l'invitation. »{/i}"
    systeme "Elle ajoute son prénom à la liste, puis pose le téléphone contre son verre. Six."

    systeme "Un message privé de Jessy apparaît."
    j "{i}« Tu te rappelles le nom du stand de glaces ? »{/i}"
    i "{i}« Non. Mais il y avait trois drapeaux bleus et une fraise qui regardait les clients comme s'ils lui devaient quelque chose. »{/i}"
    j "{i}« Celui à gauche de l'escalier. »{/i}"
    i "{i}« Exactement. »{/i}"
    j "{i}« Description très efficace. »{/i}"
    i "{i}« J'aurais dû guider la randonnée. »{/i}"
    systeme "Dans le groupe, le rendez-vous est enfin fixé : neuf heures dix, devant le panneau. Chacun confirme."
    a "{i}« Petite question. On sera combien ? »{/i}"
    x "{i}« Six. C'est écrit juste au-dessus. »{/i}"
    a "{i}« D'accord. J'ai peut-être acheté large. »{/i}"
    i "{i}« Large comment ? »{/i}"
    a "{i}« À dimanche ! »{/i}"
    jump ending_friend_trajet


# 3. LE TRAIN POUR LA MER
label ending_friend_trajet:
    stop music fadeout 1.0
    scene black with fade
    centered "DIMANCHE"
    scene bg friend gare matin with fade
    play ambiant1 audio.foule loop volume 0.2 fadein 1.0
    show jessy beach neutral at char_left with dissolve
    systeme "Neuf heures deux. Jessy attend sous le panneau des départs. Il vérifie le quai, range son billet, puis le ressort pour vérifier où il l'a rangé."
    show ilona beach neutral at char_right with dissolve
    i "Tu fais l'inventaire ?"
    j "Billet, téléphone, clés. J'ai tout."
    i "Et tes lunettes. Sur ta tête."
    j "J'allais commencer à les chercher."
    systeme "Elle pose son sac près de ses pieds. Ils regardent ensemble le panneau."
    show ilona beach smile at char_right with dissolve
    i "J'ai pris de la crème solaire. Tu pourras en prendre."
    j "Merci. J'ai de l'eau."
    i "Bien. À nous deux, on peut sortir dehors."

    hide ilona
    show allan beach smirk at char_center
    show alex beach concerned at char_right
    with dissolve
    systeme "Allan arrive avec deux grands sacs. Alexandre porte le troisième, les bras tendus pour l'empêcher de lui cogner les genoux."
    x "Il a dit que celui-là était léger."
    a "Comparativement."
    j "Y a quoi dedans ?"
    a "Le complément."
    x "Le complément de quoi ? D'un autre groupe ?"
    play sound audio.trainstop volume 0.25
    hide jessy
    show theo beach neutral at char_left
    with dissolve
    systeme "Théo descend du train de Tokyo avec un sac à dos. Allan l'aperçoit et lève une main ; le sac qu'il tenait glisse aussitôt le long de son bras."
    a "Salut ! Tu peux prendre ça ?"
    t "Bonjour à toi aussi."
    systeme "Ils se serrent brièvement dans les bras, gênés par les anses. Alexandre donne un petit coup d'épaule à Théo."
    x "T'as pensé à prendre une correspondance sans escalier ?"
    t "Non. Je pensais voyager avec des gens."
    a "C'est le cas. Des gens qui auront à manger."

    stop ambiant1 fadeout 1.0
    scene bg shared train inside with fade
    play music audio.plage loop volume 0.45 fadein 1.0
    play ambiant1 audio.trainInside loop volume 0.2 fadein 1.0
    show allan beach smirk at char_left
    show alex beach teasing at char_right
    show theo beach neutral at char_center
    with dissolve
    systeme "Ils trouvent des places voisines. Les provisions occupent les espaces sous les sièges. Alexandre commence à parler avant même que le train reparte."
    x "J'ai vu ce que tu as fait au pont."
    a "Il était pas fini."
    x "Il manque maintenant davantage de pont."
    t "Quel pont ?"
    a "Une construction qu'Alexandre refusait de rendre pratique."
    x "Il a retiré les marches pour faire passer un bateau."
    a "Et le bateau passe."
    t "Les gens passent encore ?"
    x "En bateau."
    systeme "Théo regarde un instant les deux autres, puis ouvre sa bouteille d'eau."
    show theo beach smirk at char_center with dissolve
    t "Je vais éviter la prochaine question."
    a "Tu pourrais parler de ton dîner, plutôt."
    t "Tu as gardé la photo."
    a "Tu me l'as envoyée."
    systeme "Allan montre son téléphone. Une casserole floue occupe presque tout l'écran. Au fond, quelque chose de sombre colle au métal."
    x "C'est pris avant ou après avoir mangé ?"
    t "J'avais mis le feu trop fort."
    a "Et le couvercle ?"
    t "Sur l'autre casserole."
    systeme "Jessy se penche depuis le siège voisin. Ilona aussi."
    j "Celle-là avait quoi dedans ?"
    t "Rien. C'est ce qui m'a permis de comprendre l'erreur."
    i "Tu as mangé quoi, finalement ?"
    t "Un sandwich. Debout, à la fenêtre. Il fallait aérer."
    a "Je lui ai dit que je pouvais commander un extincteur."
    t "Il m'a envoyé trois liens."

    hide allan
    hide alex
    hide theo
    show jessy beach neutral at char_left
    show ilona beach neutral at char_right
    with dissolve
    systeme "Le train quitte les immeubles les plus serrés. Ilona coince son sac entre ses chevilles."
    i "C'est loin, ta formation ?"
    j "Trois arrêts de plus que l'école. J'ai fait le trajet hier."
    i "Et ?"
    j "J'ai raté la bonne sortie. Mais j'ai trouvé une boulangerie."
    show ilona beach smile at char_right with dissolve
    i "Le plus important est réglé."
    j "Maintenant, il faut que j'apprenne quelque chose."
    systeme "Elle sourit. Un silence arrive pendant que le train longe des jardins. Jessy regarde un drap qui gonfle sur un balcon."
    show ilona beach neutral at char_right with dissolve
    systeme "Ilona suit le paysage un moment, puis se tourne vers lui."
    i "J'ai essayé de dessiner dehors, cette semaine."
    j "Quoi ?"
    i "Une fontaine. Puis le monsieur assis devant. Puis son sac, parce qu'il est parti."
    j "Et le sac est resté ?"
    i "Non. J'ai dessiné de mémoire. Très beau sac, à la fin."
    show jessy beach happy at char_left
    show ilona beach smile at char_right
    with dissolve
    systeme "Elle lui montre la page. Ils cherchent ensemble où elle a bien pu dessiner la fontaine."

    stop music fadeout 1.0
    stop ambiant1 fadeout 1.0
    scene bg arc2 beach main with fade
    play ambiant1 audio.wave loop volume 0.3 fadein 1.0
    show sofiane beach neutral at char_left
    show alex beach grin at char_right
    with dissolve
    systeme "Sofiane les attend au bord du parking. Le parasol, la glacière et la pelle gainée sont posés près de la Trueno."
    x "Tu l'as couchée sur une couverture ?"
    show sofiane beach smirk at char_left with dissolve
    s "La carrosserie n'oublie rien."
    systeme "Alexandre tend la main vers sa pelle. Sofiane attend qu'il soit suffisamment loin de la portière pour la lui donner."
    s "Maintenant."
    show allan beach neutral at char_center with dissolve
    a "Je sais pas pourquoi on s'inquiète. Elle est mieux traitée que nous."
    x "C'est du bon matériel."
    systeme "Ils descendent vers le sable. Alexandre désigne une bande humide, à bonne distance de leurs affaires."
    x "Là. On sera bien."
    a "Pour manger ?"
    x "Pour bâtir."
    a "J'aimerais qu'on travaille la formulation des invitations."
    jump ending_friend_chateau


# 4. LA GRANDE CATASTROPHE COLLECTIVE
label ending_friend_chateau:
    scene bg arc2 group parasol with fade
    play music audio.plage loop volume 0.55 fadein 1.0
    show sofiane beach neutral at char_left
    show ilona beach smile at char_right
    show allan beach smirk at char_center
    with dissolve
    systeme "Sofiane enfonce le parasol et vérifie qu'il tient. Ilona étale sa serviette à l'ombre, pose son sac dessus et retire ses chaussures."
    i "Voilà. Je suis arrivée."
    a "Attends de voir le buffet."
    systeme "Allan sort des onigiri, des sandwichs, deux boîtes de fruits, des crackers et trois paquets de biscuits. Il cherche quelque chose dans le dernier sac."
    s "Une septième personne ?"
    show allan beach embarrassed at char_center with dissolve
    a "Les serviettes."
    i "Tu les as mises où ?"
    a "Sur la table. Pour pas les oublier."
    systeme "Il regarde la mer, puis ses mains."
    show allan beach smirk at char_center with dissolve
    a "Techniquement, on a une très grande quantité d'eau."
    i "Salée. Avec du sable."
    a "J'en achèterai."

    scene bg arc2 beach main with dissolve
    show alex beach grin at char_center
    show jessy beach neutral at char_left
    show ilona beach smile at char_right
    with dissolve
    systeme "Quelques mètres plus bas, Alexandre trace un rectangle dans le sable avec le manche de sa pelle. Il recule encore de deux pas pour terminer le quatrième côté."
    x "Cette fois, je reste raisonnable."
    j "On est à l'intérieur ou à l'extérieur ?"
    x "Dans la première cour."
    i "Combien de cours ?"
    x "Ça dépendra du relief."
    systeme "Jessy s'accroupit pour remplir un seau. Ilona lui passe une petite pelle."
    i "Moi, je veux une cuisine par là. Vue sur mer."
    j "Une seule ?"
    i "On verra après la visite."
    hide ilona
    show allan beach smirk at char_right
    with dissolve
    a "Il faut une réserve à biscuits."
    x "Dans la tour nord."
    a "Trop loin."
    x "De quoi ?"
    a "De moi."
    systeme "Alexandre lui désigne un carré à bâtir près de l'entrée. Allan y pose directement un paquet."
    x "Il faut construire autour."
    a "Ah. Je trouvais ça efficace."

    hide allan
    show sofiane beach neutral at char_right
    with dissolve
    systeme "Sofiane tasse une route sinueuse entre deux petites buttes. Il souffle sur les grains qui dépassent dans le virage."
    j "Tu fais une route de montagne sur la plage ?"
    s "Le terrain manquait d'ambition."
    systeme "Jessy plante deux bâtonnets dans le sable et pose une brindille en travers."
    x "C'est quoi ?"
    j "La porte."
    x "Le mur sera où ?"
    j "On n'en a pas encore discuté."
    s "L'accès est fluide."

    hide jessy
    hide sofiane
    show theo beach neutral at char_left
    show alex beach concerned at char_right
    with dissolve
    play sound audio.sandnoise volume 0.3
    systeme "Un pan de la tour s'affaisse sur le pied d'Alexandre. Il regarde le tas sans bouger."
    show alex beach awkward at char_right with dissolve
    x "Elle avait pourtant tenu pendant la présentation."
    t "Si tu élargis la base, tu peux..."
    systeme "Théo s'accroupit, la main déjà tendue. Il la pose sur son genou."
    show theo beach reassuring at char_left with dissolve
    t "Tu veux un coup de main ?"
    x "Pour le côté mer, oui. Celui-ci, je veux réessayer."
    t "D'accord. Je prends ce seau ?"
    x "Le bleu. Le rouge fait des tours ovales."
    t "Il est rond."
    x "Je sais. C'est incompréhensible."
    systeme "Théo prend le bleu. Ils travaillent chacun d'un côté."

    hide theo
    hide alex
    show jessy beach embarrassed at char_left
    show ilona beach neutral at char_right
    with dissolve
    systeme "À l'autre bout, Jessy retire sa main d'un tunnel. Le plafond vient avec."
    j "J'ai fait une tranchée."
    i "Attends. Laisse comme ça."
    systeme "Elle lisse le fond, pose trois coquillages plats le long d'un bord."
    i "Restaurant pour crabes. Les tables sont prêtes."
    j "Il leur faut une entrée."
    i "Sur le côté."
    j "Parce qu'ils marchent..."
    i "Oui."
    show jessy beach happy at char_left
    show ilona beach smile at char_right
    with dissolve
    systeme "Il creuse un passage latéral, beaucoup trop large. Ilona ajoute un petit caillou à chaque table."
    j "C'est le menu ?"
    i "Le pain."
    j "On va avoir des réclamations."
    i "Ils peuvent pincer le serveur."
    j "On a un serveur ?"
    systeme "Elle lui tend un coquillage."
    i "Félicitations."

    scene cg friend chateau with Dissolve(1.0)
    window hide
    pause 3.0
    window show

    scene bg arc2 beach main with dissolve
    show jessy beach happy at char_left
    show alex beach grin at char_right
    show allan beach neutral at char_center
    with dissolve
    systeme "Quand Alexandre annonce la fin des fondations, Allan est couché sous le parasol. Il lève un doigt."
    a "Est-ce qu'on peut visiter la réserve ?"
    x "On n'a pas posé les remparts."
    a "C'est justement le bon moment pour y entrer."
    systeme "Une vague s'étale au pied de la route de Sofiane. Ilona récupère aussitôt ses chaussures."
    i "On remonte les affaires. L'eau arrive."
    systeme "Sofiane saisit la glacière. Théo et Jessy déplacent les sacs ; Ilona replie la serviette qui dépassait. Allan revient chercher les biscuits."
    show alex beach concerned at char_right with dissolve
    x "Je peux retenir celle-là."
    j "Alexandre."
    x "Juste celle-là."
    play sound audio.sandnoise volume 0.35
    systeme "Il plante sa pelle devant le mur. L'eau passe des deux côtés, remplit les douves et emporte la moitié de la cour."
    systeme "La porte de Jessy reste debout. Alexandre la regarde, trempé jusqu'aux chevilles."
    x "Pourquoi elle tient, elle ?"
    j "Elle a moins de responsabilités."
    systeme "La vague suivante couche la brindille. Ilona éclate de rire en voyant Jessy saluer son ouvrage."

    scene cg friend salut brindille with Dissolve(0.8)
    window hide
    pause 3.0
    window show

    scene bg arc2 group parasol with dissolve
    show allan beach smirk at char_left
    show alex beach concerned at char_right
    show sofiane beach neutral at char_center
    with dissolve
    systeme "Ils s'installent enfin pour manger. Alexandre essuie le manche de sa pelle avec le bord de sa propre serviette."
    a "La réserve a été évacuée à temps."
    x "Tu as ouvert le paquet."
    a "Il fallait alléger le transport."
    s "Tu peux me passer un sandwich ?"
    a "Lequel ?"
    systeme "Sofiane regarde les trois rangées qu'Allan vient d'aligner."
    s "Je ne savais pas qu'il fallait préparer cette réponse."
    jump ending_friend_promenade


# 5. LES BOISSONS ET LE RESTE
label ending_friend_promenade:
    hide alex
    hide sofiane
    show ilona beach neutral at char_right
    show jessy beach neutral at char_left
    show allan beach smirk at char_center
    with dissolve
    systeme "Après le repas, Ilona secoue une bouteille vide."
    i "Je vais chercher à boire. Et les serviettes."
    j "Je viens porter."
    a "Pour moi, citron. Avec des glaçons, mais pas trop, sinon il y a moins de citron."
    x "Un thé froid. Pas glacé."
    t "De l'eau, simplement."
    s "Du café. S'il y en a."
    i "Sofiane veut du café si le café existe. Ça, je peux retenir."
    j "Attends, je note."
    systeme "Allan se penche sur son téléphone."
    a "Tu peux écrire « assez de citron » ?"
    j "Je vais montrer ton message au vendeur."
    a "Il comprendra."

    scene bg arc2 kakigori counter with fade
    show jessy beach happy at char_left
    show ilona beach smile at char_right
    with dissolve
    play music audio.mornPiano loop volume 0.4 fadeout 1.0 fadein 1.0
    systeme "Ils remontent vers les stands, les pieds encore mouillés. Ilona essaie de remettre sa sandale en marchant."
    i "La prochaine fois, je demande juste « qui veut de l'eau ? »."
    j "Alexandre voudra savoir à quelle température."
    i "Celle qu'on trouve."
    j "Il dira que ça dépend de l'endroit."
    systeme "Elle rit, abandonne sa sandale et la prend à la main. Jessy s'arrête le temps qu'elle retire l'autre."
    i "Ça m'avait manqué, ça."
    j "Marcher avec tes chaussures dans les mains ?"
    i "Dire des bêtises avec toi. Sans préparer le début."
    show ilona beach neutral at char_right
    show jessy beach listening at char_left
    with dissolve
    systeme "Le stand n'est plus qu'à quelques pas. Ilona ralentit."
    i "J'ai failli pas proposer la journée."
    j "À cause de moi ?"
    i "Un peu. J'avais envie de voir tout le monde. Toi aussi. Et j'avais peur de rentrer en ayant encore mal."
    systeme "Jessy passe son téléphone dans l'autre main."
    i "Pendant un moment, je prenais une photo d'un truc idiot, et je savais déjà ce que tu allais répondre. J'avais envie de te l'envoyer."
    i "Puis je pensais au message d'après. À attendre que tu m'en envoies un. À regarder si t'étais connecté."
    j "Je savais pas que c'était comme ça."
    i "C'est pour ça que je t'ai presque rien envoyé. Même les jours où j'allais bien."
    j "J'avais peur que tu croies que je m'en fichais, en te laissant tranquille."
    systeme "Il cherche la suite en regardant le sable qui colle à ses doigts."
    j "Et dès que j'écrivais quelque chose, je me demandais si je revenais trop vite. J'ai gardé beaucoup de messages dans les brouillons."
    i "Moi aussi."
    pause 0.5
    show ilona beach smile at char_right
    show jessy beach smile at char_left
    with dissolve
    i "Je suis contente d'être venue. Je peux dire ça aujourd'hui."
    j "Moi aussi. Ça me fait plaisir de te voir."
    systeme "Elle hoche la tête. Devant eux, quelqu'un replie le menu d'un stand et quitte la file."

    show jessy beach neutral at char_left
    show ilona beach neutral at char_right
    with dissolve
    "La vendeuse" "C'est à vous."
    i "Bonjour. Alors... six boissons et des serviettes, s'il vous plaît."
    systeme "Jessy lui montre la liste. Ilona la lit deux fois avant de commander."
    "La vendeuse" "Le citron, grand ou petit ?"
    j "Grand. Il a écrit « assez » en majuscules."
    systeme "La vendeuse leur donne un porte-gobelets en carton, puis des pailles. Ilona compte les boissons ; Jessy coince les serviettes sous son bras."
    i "Et voilà. Mission réussie."
    j "Il faut encore faire le trajet retour."

    scene bg arc2 beach main with dissolve
    show jessy beach neutral at char_left
    show ilona beach smile at char_right
    with dissolve
    systeme "Ils marchent plus lentement avec la commande. Ilona goûte une boisson, puis regarde Jessy."
    i "J'ai une idée pour les prochains lives."
    j "Une autre maison qui marche ?"
    i "Un rendez-vous où les gens proposent des bâtiments impossibles. Je les dessine, on essaie de comprendre comment on vivrait dedans."
    j "Le phare avait des toilettes ?"
    i "Tu vois, c'est exactement le genre de question."
    systeme "Elle évite une dalle soulevée, sans quitter son histoire."
    show ilona beach neutral at char_right with dissolve
    i "Je sais pas si je dois annoncer un thème, faire voter... J'ai pas envie de passer trois soirées à préparer un truc que je ferai deux fois."
    j "Qu'est-ce qui te plaît le plus ? Le dessin ou les idées qui arrivent ?"
    i "Le moment où quelqu'un ajoute un truc et où je dois me débrouiller avec."
    show ilona beach smile at char_right with dissolve
    j "Tu devrais prévenir Alexandre. Il a un château sinistré à reloger."
    i "Je vais l'interdire de sous-sols."
    j "Il va creuser quand même."
    i "Alors j'en ferai un aquarium."
    systeme "Elle prend une autre gorgée, puis baisse les yeux sur le gobelet."
    show ilona beach embarrassed at char_right with dissolve
    i "Oh. C'est celui d'Allan."
    j "Il reste assez de citron ?"
    i "Beaucoup moins."
    systeme "Ils regardent le parasol, encore à une trentaine de mètres."
    j "On pourrait dire que..."
    i "Non. Il va m'entendre inventer."
    j "Oui."

    scene bg arc2 group parasol with dissolve
    show allan beach neutral at char_left
    show ilona beach embarrassed at char_right
    show jessy beach embarrassed at char_center
    with dissolve
    i "J'ai bu dans ton citron. Pardon."
    a "Combien ?"
    systeme "Elle lui tend le gobelet. Allan évalue le niveau."
    a "T'as suivi mes instructions sur les glaçons ?"
    i "Oui."
    show allan beach smirk at char_left with dissolve
    a "Bon. Au moins, c'était un bon citron."
    systeme "Il lui prend une serviette, s'essuie les doigts et ouvre la dernière boîte de fruits."
    jump ending_friend_promesse


# 6. TOUS LES ANS, LE MÊME JOUR
label ending_friend_promesse:
    scene bg arc2 beach main with dissolve
    show alex beach grin at char_left
    show theo beach reassuring at char_right
    with dissolve
    systeme "L'après-midi s'étire. Théo et Alexandre jouent aux raquettes. Ils réussissent onze échanges."
    scene cg friend raquettes with Dissolve(0.8)
    window hide
    pause 3.0
    window show
    scene bg arc2 beach main with dissolve
    show alex beach grin at char_left
    show theo beach reassuring at char_right
    with dissolve
    systeme "Alexandre commence à expliquer pourquoi ils progressent. Au douzième, la balle tombe."
    x "J'étais en train de parler."
    t "J'ai remarqué."
    systeme "Ilona trempe ses pieds dans l'eau. Jessy cherche une pierre plate et revient avec une pierre ronde qu'il défend longtemps. Sofiane finit son café à l'ombre."

    stop music fadeout 2.0
    scene bg arc2 beach sunset with fade
    show allan beach neutral at char_left
    show alex beach neutral at char_center
    show ilona beach neutral at char_right
    with dissolve
    systeme "Quand le sable refroidit, ils rapprochent les serviettes. Alexandre dessine du bout du doigt le plan de l'appartement qu'il va visiter."
    x "La pièce principale est petite. Mais j'aurais un balcon."
    i "Tu l'as déjà mesuré ?"
    x "Sur la photo. C'est provisoire."
    a "Tu seras loin ?"
    x "Un peu. Je pourrai plus rentrer à pied après une soirée chez toi."
    systeme "Allan ramène ses genoux contre lui."
    a "Faudra rester dormir."
    x "T'as toujours la table au milieu de la pièce ?"
    a "On la poussera."
    i "Moi, j'ai commencé à chercher un petit boulot pour les week-ends. J'attends des réponses."
    j "Et lundi, j'aurai enfin mon emploi du temps."
    s "Le mien change la semaine prochaine."
    systeme "Théo vérifie l'heure de son train, puis range son téléphone. Allan regarde la mer."
    show allan beach smirk at char_left with dissolve
    a "Bon. On revient l'année prochaine. Tous. Même jour, même plage."
    x "Je garde les plans."
    i "Je prends les serviettes."
    j "On pourra manger avant les travaux ?"
    a "Tous les ans. Comme ça, c'est réglé."

    hide ilona
    show theo beach neutral at char_right
    with dissolve
    t "J'aimerais bien. Mais je ne peux pas te promettre ce jour précis."
    a "C'est dans un an. On le bloque maintenant."
    t "Je n'ai pas encore les dates des tournages."
    s "Je ne sais pas non plus si je travaillerai."
    a "Alors on prend le dimanche d'à côté. Mais on décide."
    x "On peut regarder quand on en saura plus."
    show allan beach doubt at char_left with dissolve
    a "C'est ce qu'on dit à chaque fois. Et après, on trouve pas."
    systeme "Alexandre lève les yeux de son dessin. Une vague efface la pointe d'une empreinte, loin devant leurs pieds."
    show alex beach support at char_center with dissolve
    x "Allan ?"
    a "Quoi ?"
    x "On a envie de revenir."
    a "Je sais."
    systeme "Allan tire un fil qui dépasse de sa serviette. Il n'arrive pas à le casser."
    a "Mon frère avait un groupe comme nous. Ils disaient tout le temps « faut qu'on se fasse un truc »."
    a "Deux sorties reportées. Après, juste des anniversaires dans la conversation. Il les aime toujours, hein. Il les voit plus."
    systeme "Il laisse le fil tranquille."
    a "J'ai pas envie qu'on passe notre temps à s'expliquer pourquoi on peut pas venir."
    systeme "Personne ne répond tout de suite. Alexandre remet le bouchon sur une bouteille. Le plastique craque sous ses doigts."
    t "Avec toi, j'ai déjà laissé passer beaucoup de temps. Avant que tu viennes à Tokyo."
    a "C'était compliqué."
    t "Oui. J'aurais quand même pu appeler."
    systeme "Allan regarde son ami, puis baisse les yeux."
    a "Je te demande pas de revenir exprès chaque fois."
    t "Je sais. Mais je ne veux pas te dire oui aujourd'hui et te laisser attendre."
    x "Moi non plus. Et ça va me manquer, de débarquer chez toi juste parce que je m'ennuie."
    a "Tu pourras toujours t'ennuyer au téléphone."
    x "C'est moins bien. Tu me donnes rien à manger."
    systeme "Allan souffle un petit rire. Puis il reprend le fil entre ses doigts."
    show allan beach neutral at char_left with dissolve

    hide theo
    show ilona beach neutral at char_right
    with dissolve
    i "Quand est-ce que quelqu'un repasse dans le coin ? Bientôt, je veux dire."
    t "Dans trois semaines. Je viens voir ma mère. Le samedi, en fin d'après-midi, je pourrais rester un peu."
    a "Tu repars le soir ?"
    t "Le lendemain matin."
    i "Moi, le samedi, je peux. Pour l'instant."
    j "Je suis libre après quatre heures."
    x "Je déménage, ce week-end-là."
    s "Et je travaille."
    systeme "Allan regarde les deux autres. Alexandre hausse une épaule."
    x "Vous me raconterez. Je vous enverrai une photo du balcon avec un vrai mètre."
    a "On peut manger chez moi. Je vous enverrai l'heure quand j'aurai mes horaires."
    t "Ça me va."
    systeme "Allan sort son téléphone. Il écrit le rendez-vous, reste un moment sur la case de l'heure, puis met simplement « fin d'après-midi »."
    play music audio.plagesunset loop volume 0.45 fadein 2.0
    hide ilona
    show sofiane beach neutral at char_right
    with dissolve
    s "Ce rendez-vous nécessite une pelle ?"
    x "Chez Allan ?"
    s "Je préfère demander."
    x "Ça dépend du balcon."
    a "J'ai pas de balcon."
    x "Pour l'instant."
    systeme "Ils rient. Allan range son téléphone, puis s'allonge sur les coudes. Personne ne propose encore de partir."
    show allan beach smirk at char_left with dissolve
    jump ending_friend_photo


# 7. PERSONNE N'EST PRÊT
label ending_friend_photo:
    hide sofiane
    hide alex
    show jessy beach neutral at char_center
    show ilona beach smile at char_right
    with dissolve
    i "Avant qu'il fasse trop sombre, je veux une photo."
    a "Attends, je termine ça."
    i "Tu dis ça depuis midi."
    systeme "Ilona pose son téléphone sur la glacière, calé contre un sac bien au sec. Elle recule, revient régler l'angle, puis fait signe aux autres."
    i "Mettez-vous là."
    x "On voit le château ?"
    j "On voit de la plage."
    x "C'est l'emplacement du château. Ça compte."
    systeme "En s'écartant pour laisser passer Sofiane, Jessy se retrouve au bout du groupe. Ilona regarde l'écran. Une moitié de son bras sort du cadre."
    show jessy beach smile at char_center with dissolve
    j "Attendez. Vous me faites une place ? Je dépasse."
    systeme "Allan se décale aussitôt. Théo fait un pas de côté ; Alexandre retire son coude. Jessy se glisse entre eux."
    i "Là, c'est bon. Je te vois."
    systeme "Elle lance le retardateur et les rejoint."
    a "Combien de secondes ?"
    i "Dix. Enfin, je crois."
    x "Regardez, il reste une tour ! Là-bas !"
    t "Où ?"
    s "La serviette. Attrapez la serviette."
    play sound audio.photo volume 0.4
    scene cg friend premier ete with Dissolve(0.2)
    window hide
    pause 2.0
    window show
    systeme "Sur la photo, Allan parle encore, un biscuit à la main. Alexandre montre quelque chose qui n'est pas dans l'image. Théo regarde dans la mauvaise direction."
    systeme "Sofiane retient la serviette par un coin. Jessy rit, les yeux presque fermés. Ilona n'a pas fini de se retourner vers l'objectif."
    a "On en refait une."
    i "Je garde celle-là."
    a "On dirait que je mange le vent."
    j "Il restait que ça."
    systeme "Ils se serrent autour du téléphone. Ilona envoie déjà l'image dans la conversation."
    x "La tour est coupée."
    t "Elle était tombée avant le déclenchement."
    x "Je préfère ma version."

    scene bg arc2 beach sunset with dissolve
    show allan beach smirk at char_left
    show alex beach concerned at char_right
    show sofiane beach neutral at char_center
    with dissolve
    systeme "Ranger prend longtemps. Une chaussure manque, puis réapparaît sous un sac. Sofiane replie le parasol pendant qu'Allan distribue les restes."
    a "Deux sandwichs pour le retour."
    s "J'en ai mangé trois."
    a "Ça, c'était pour ici."
    systeme "Alexandre soulève un petit bloc de sable compact dans sa paume. Le bloc se fend avant même qu'il l'ait montré."
    x "Je vais garder les plans."
    systeme "Il lisse le sable avec la main, récupère sa pelle et suit les autres."
    scene bg friend promenade depart with fade
    show allan beach smirk at char_left
    show sofiane beach neutral at char_center
    show ilona beach smile at char_right
    with dissolve
    systeme "Au bout de la promenade, le chemin se sépare entre la gare et le parking. Ilona tend la glacière à Sofiane."
    i "Merci pour tout le matériel. Tu nous diras quand t'es rentré ?"
    s "Oui."
    a "Et toi, tu me rends les boîtes quand elles sont vides. Pas avant."
    s "C'était mon intention."
    systeme "Sofiane serre les mains, accepte une accolade maladroite autour du parasol, puis part vers la voiture. Il se retourne encore une fois pour lever la main."
    hide sofiane with dissolve

    stop music fadeout 1.5
    stop ambiant1 fadeout 1.0
    scene bg arc5 train station with fade
    play ambiant1 audio.foule loop volume 0.15 fadein 1.0
    show allan beach neutral at char_left
    show theo beach reassuring at char_right
    with dissolve
    systeme "À la gare de correspondance, Théo reprend son sac. Allan lui donne le dernier paquet fermé."
    t "Je vais finir par croire que tu manges moins que tu le dis."
    a "J'ai commencé avant de venir."
    systeme "Ils s'enlacent. Théo salue les autres, puis traverse le quai."
    t "Dans trois semaines. Je te confirme quand j'ai mon billet."
    a "D'accord. Bon retour."
    hide theo with dissolve
    systeme "Allan reste près de la porte jusqu'à ce que son ami disparaisse dans l'escalier. Jessy lui fait signe de venir s'asseoir."

    stop ambiant1 fadeout 1.0
    scene bg shared train inside with fade
    play ambiant1 audio.trainInside loop volume 0.2 fadein 1.0
    show allan beach smirk at char_center with dissolve
    systeme "Allan rouvre la photo. Il agrandit son propre visage et l'envoie dans le groupe."
    a "{i}« Je précise que le vent était délicieux. »{/i}"
    systeme "Alexandre répond depuis le siège d'en face. Ilona ajoute un biscuit. Théo réagit un peu plus tard, une fois assis dans son train."
    systeme "Allan range le téléphone. Son front touche presque la vitre quand il se penche pour apercevoir une dernière bande de mer entre les maisons."
    stop ambiant1 fadeout 1.5
    scene cg friend premier ete with Dissolve(1.0)
    window hide
    pause 2.0
    scene black with Dissolve(1.5)
    window show
    jump ending_friend_annees


# 8. PARFOIS CINQ, PARFOIS TROIS
label ending_friend_annees:
    centered "L'ANNÉE SUIVANTE"
    scene bg arc5 cafe with fade
    play music audio.cafe loop volume 0.45 fadein 1.0
    play ambiant1 audio.rainInside loop volume 0.25 fadein 1.0
    show allan beach neutral at char_left
    show alex beach neutral at char_center
    show ilona beach neutral at char_right
    with dissolve
    systeme "La plage était prévue. La pluie a commencé pendant le trajet. Allan, Alexandre et Ilona ont fini dans un café près de la gare, avec un sac de serviettes qui n'a jamais été aussi utile."
    systeme "Jessy travaille ce jour-là. Sofiane n'a pas pu changer son service ; Théo est resté à Tokyo. Ils ont prévenu dans la semaine."
    systeme "Le serveur retire les couverts inutilisés. Allan suit des yeux les deux chaises vides à l'autre bout de la table."
    a "On a de la place."
    x "Avec ce toit, le château aurait tenu."
    systeme "Alexandre lève les yeux vers les poutres."
    x "Il faudrait juste protéger les pieds des tables."
    i "Bonjour. Je voudrais le gâteau de la vitrine, s'il vous plaît."
    a "Lequel ?"
    i "Je vais vous demander de me laisser finir ma commande."
    show allan beach smirk at char_left
    show ilona beach smile at char_right
    with dissolve
    systeme "Elle en choisit deux. Alexandre dessine sur un coin de serviette en papier ; Allan le déplace chaque fois que la théière menace de mouiller son plan."
    systeme "Ils envoient une photo des assiettes et de la fenêtre ruisselante."
    i "{i}« Plage couverte. Très bon sable au chocolat. »{/i}"
    systeme "Jessy répond pendant sa pause. Théo demande l'adresse pour une prochaine visite."
    a "On prend une autre théière ?"
    x "On avait dit qu'on attendait que ça se calme."
    systeme "La pluie frappe plus fort contre la vitre. Ilona tend sa tasse."
    i "On a le temps."

    stop ambiant1 fadeout 1.0
    stop music fadeout 1.0
    scene black with fade
    centered "DEUX ANS APRÈS LA PLAGE"
    scene bg friend appel with fade
    play music audio.mornPiano loop volume 0.4 fadein 1.0
    show alex home grin at char_center with dissolve
    systeme "Trois jours après son anniversaire, Alexandre est chez lui, devant la webcam. Il a posé un petit gâteau rond sur son bureau ; une bougie penche vers le bord."
    systeme "Sur l'écran, Allan appelle de son appartement, Jessy et Ilona chacun de chez soi, et Théo depuis Tokyo. Sofiane termine encore son service ; il les rejoindra plus tard."
    scene bg friend discord cinq with dissolve
    systeme "Alexandre approche le gâteau de la caméra."
    x "J'ai vérifié. Le pâtissier aurait pu le faire plus haut avec exactement la même quantité."
    i "On peut te souhaiter bon anniversaire avant l'étude ?"
    x "Oui. Mais ça aurait changé la répartition de la crème."
    systeme "Ils commencent à chanter. Le décalage de l'appel produit trois débuts différents et une fin à laquelle Jessy arrive seul."
    j "... versaire."
    a "Magnifique."
    play sound audio.discord volume 0.25
    scene bg friend discord six with dissolve
    systeme "Une sixième fenêtre s'ouvre : Sofiane vient de rentrer et rejoint l'appel depuis son téléphone."
    s "J'ai raté quelque chose ?"
    x "Pas l'essentiel. Regarde cette coupe."
    systeme "Alexandre plonge son couteau dans le gâteau pour montrer l'épaisseur des couches. Chez elle, Ilona jette un œil vers son four : son propre repas est presque prêt."
    a "Tu as ouvert notre cadeau ?"
    x "Oui ! Merci. Les feutres sont incroyables. J'ai testé le gris sur toute une page."
    a "On a mis du temps à se décider. Théo avait apporté les échantillons chez moi lors de son dernier passage."
    t "Et oublié ma batterie externe. Tu l'as encore ?"
    a "Sur l'étagère. Je te la rends la prochaine fois."
    t "D'accord."
    systeme "Alexandre lève un feutre devant l'objectif. La caméra fait la mise au point sur son rideau."
    x "Celui-là, c'est un gris chaud."
    s "Je vois surtout un rideau froid."
    systeme "Dans sa fenêtre, Théo consulte l'heure."
    t "Je dois y aller. Alexandre, tu me montreras la suite ?"
    x "J'en suis au troisième gris. Il en reste cinq."
    t "Je t'appelle dimanche."
    scene bg friend appel with dissolve
    show alex home grin at char_center with dissolve
    systeme "Théo salue tout le monde et quitte l'appel. Les autres restent : Allan va chercher son chargeur ; Ilona leur montre l'assiette qu'elle vient de sortir du four."
    scene black with fade
    centered "LE DIMANCHE SUIVANT"
    scene bg friend appel with fade
    show alex home grin at char_center with dissolve
    systeme "Alexandre s'est de nouveau installé devant son ordinateur. Théo le rappelle depuis Tokyo ; cette fois, ils sont seuls dans l'appel. Alexandre a préparé une nouvelle page."
    t "Tu en as acheté d'autres ?"
    x "Il manquait un gris."
    systeme "Alexandre lui envoie la page terminée le soir même. D'autres images suivent au fil des mois : des repas, des dessins, des morceaux de leur monde Minecraft."

    stop music fadeout 1.0
    scene black with fade
    systeme "Les appels changent parfois d'heure et les rencontres réunissent rarement tout le monde. Leurs messages continuent de circuler."
    centered "TROIS ANS APRÈS LA PLAGE"
    scene bg arc2 minecraft house summer night with fade
    play music audio.mcnight loop volume 0.5 fadein 1.0
    show jessy minecraft at char_left
    show ilona minecraft at char_right
    with dissolve
    systeme "Un mardi soir, Jessy voit le pseudo d'Ilona apparaître. Elle entre dans le vocal pendant qu'il vérifie le contenu d'un coffre."
    i "J'ai une heure."
    j "Moi aussi. Tu sais où on a mis le bois ?"
    i "Dans le coffre à bois."
    j "Il y a des œufs."
    i "Ah. Donc on l'a déplacé."
    systeme "Ils ouvrent celui de la cuisine, celui sous l'escalier, puis celui qu'une porte empêche d'ouvrir entièrement."
    j "Tu as fait ton dessin pour l'affiche ?"
    i "Oui. Ils l'ont accrochée hier."
    j "Celle de l'atelier ?"
    i "Oui. J'y suis passée en sortant du boulot. Je suis restée devant la vitre comme si je savais pas ce qu'il y avait dessus."
    j "T'as une photo ?"
    i "Je te l'envoie après. Et toi, la visite ?"
    j "J'ai dit oui pour l'appartement."
    i "Celui avec la fenêtre au-dessus de l'évier ?"
    j "Oui. Ça me raccourcit le trajet. Par contre, je sais toujours pas si mon bureau entre."
    i "Mesure-le avant de le mettre dans l'escalier."
    j "Alexandre me l'a dit aussi. Avec un dessin de moi coincé dedans."
    play sound audio.mcdoor volume 0.25
    systeme "Ilona ouvre une porte au fond du couloir. Derrière, un coffre porte une pancarte : « BOIS, POUR LE RETROUVER »."
    i "C'est ton écriture."
    j "C'est la police du jeu."
    i "C'est quand même ton écriture."
    systeme "Ils récupèrent le bois et commencent une passerelle. Quand Ilona regarde l'heure, ils n'en ont posé que la moitié."
    i "Il faut que j'arrête. Je me lève tôt."
    j "Moi aussi. On laisse ça là."
    i "Je vais mettre une torche. Qu'Alexandre tombe pas dedans."
    j "Il va croire que c'est une invitation."
    systeme "Elle en pose une deuxième, hésite, puis les laisse toutes les deux."
    i "Bonne nuit, Jessy."
    j "Bonne nuit. Envoie-moi l'affiche quand tu peux."
    hide ilona with dissolve
    systeme "Son personnage disparaît. Jessy quitte à son tour. Sur le téléphone, la photo de la vitrine arrive pendant qu'il éteint son bureau."

    stop music fadeout 1.0
    scene black with fade
    centered "CINQ ANS APRÈS LA PLAGE"
    scene bg friend appartement with fade
    play music audio.cafe loop volume 0.45 fadein 1.0
    show allan beach neutral at char_left
    show theo tokyo neutral at char_right
    with dissolve
    systeme "Théo est de passage pour le week-end. Chez Allan, la table a changé de place. Il y a enfin assez d'espace pour s'asseoir sans la déplacer."
    systeme "Allan sort un petit objet d'un tiroir et le pose devant lui."
    a "Tiens."
    t "Ma batterie."
    a "La prochaine fois. Comme promis."
    t "On s'est vus depuis."
    a "Mais pas ici."
    t "Je suis venu ici l'hiver dernier."
    a "Elle était pas chargée."
    systeme "Théo appuie sur le bouton. Trois voyants s'allument."
    show allan beach smirk at char_left with dissolve
    t "Trois ans. Tu as eu le temps."
    a "Elle a vécu des choses. Un déménagement, deux coupures de courant..."
    show theo tokyo smirk at char_right with dissolve
    t "Tu as déménagé de l'autre côté du palier."
    a "Il a fallu traverser."
    show sofiane beach neutral at char_center with dissolve
    systeme "La sonnette les interrompt. Sofiane entre avec un sac de plats à emporter et referme la porte avec son pied."
    s "Qui a commandé pour six ?"
    a "Les habitudes."
    t "Je dois repartir dans une heure. Ma mère m'attend."
    systeme "Allan va chercher trois assiettes. Sofiane débarrasse la place devant Théo ; la batterie finit entre la sauce et les baguettes."
    scene bg friend appartement repas
    show allan beach smirk at char_left
    show theo tokyo neutral at char_right
    show sofiane beach neutral at char_center
    with dissolve
    a "Alors on commence. Tu veux nous raconter le trajet ?"
    t "Pas particulièrement. J'ai passé quarante minutes à côté d'un homme qui regardait des vidéos de perceuses."
    show sofiane beach smirk at char_center with dissolve
    s "Quel modèle ?"
    systeme "Théo ferme les yeux. Allan commence à rire avant la réponse."

    stop music fadeout 1.5
    scene black with fade
    systeme "Certaines invitations restent sans date. D'autres finissent par tenir dans une pause déjeuner, un détour après le travail, une soirée sur le serveur."
    systeme "L'été suivant, dans la conversation du groupe, Ilona propose de nouveau la plage. Les réponses arrivent sur deux jours. Cette fois, les six prénoms se retrouvent sous le même dimanche."
    jump ending_friend_retrouvailles


# 9. UNE AUTRE JOURNÉE
label ending_friend_retrouvailles:
    centered "L'ÉTÉ SUIVANT"
    scene bg arc2 group parasol with fade
    play music audio.plage loop volume 0.45 fadein 1.5
    play ambiant1 audio.wave loop volume 0.3 fadein 1.0
    show ilona beach smile at char_right
    show jessy beach smile at char_left
    with dissolve
    systeme "Ilona a déjà installé sa serviette à l'ombre quand Jessy descend sur le sable. Elle lève la main sans se redresser."
    i "Alors ? La porte du placard ?"
    j "Elle ferme."
    i "Depuis quand ?"
    j "Hier."
    i "Félicitations."
    j "Maintenant, il faut réussir à l'ouvrir."
    systeme "Elle éclate de rire. Jessy pose son sac et étale sa serviette."
    show jessy beach happy at char_left with dissolve
    i "Tu demanderas à Alexandre."
    j "Il veut déjà les dimensions. Je commence à regretter d'en avoir parlé."

    hide jessy
    show allan beach smirk at char_left
    show alex beach grin at char_center
    with dissolve
    systeme "Allan arrive avec les provisions. Alexandre le suit, sa pelle sur l'épaule. La housse a été recousue près de la poignée."
    a "J'ai fait une liste."
    i "Montre."
    a "Pas besoin."
    systeme "Il sort un gros paquet de serviettes en papier et le pose au centre, bien en évidence."
    x "Il nous l'a montré dans le train."
    a "On reconnaît jamais assez les efforts."
    hide alex
    show sofiane beach neutral at char_center
    with dissolve
    systeme "Sofiane arrive à son tour avec les derniers sacs. Il dépose les boissons à l'ombre et s'assoit pour retirer ses chaussures."
    s "Il manque Théo ?"
    i "Sa correspondance a du retard. Il vient d'écrire."
    a "On commence à s'installer. Je lui garde une place."
    systeme "Allan pousse un sac au bout de sa serviette. Alexandre a déjà ressorti une vieille feuille pliée."

    scene bg arc2 beach main with dissolve
    show alex beach grin at char_center
    show jessy beach neutral at char_left
    show ilona beach smile at char_right
    with dissolve
    x "J'ai apporté quelques corrections."
    j "Au château ?"
    x "La réserve sera accessible depuis la serviette d'Allan."
    a "J'avais fait remonter cette demande."
    i "Et le restaurant pour crabes ?"
    x "Il reste. J'ai agrandi la terrasse."
    j "Il faudra embaucher."
    systeme "Sofiane s'accroupit devant le plan. Il suit du doigt une ligne entre les deux tours."
    hide ilona
    show sofiane beach neutral at char_right
    with dissolve
    s "Le virage est trop serré."
    x "C'est une gouttière."
    s "Ça explique la largeur."

    scene bg friend promenade arrivee with dissolve
    show allan beach smirk at char_left
    show theo beach neutral at char_right
    with dissolve
    systeme "Théo apparaît au bout de la promenade alors qu'ils sortent le repas. Il descend les marches, une main sur la bretelle de son sac."
    t "Désolé. J'ai fini par connaître toutes les annonces de la gare."
    a "Viens. Il y a encore de l'ombre ici."
    scene bg arc2 group parasol with dissolve
    show allan beach smirk at char_left
    show theo beach neutral at char_right
    with dissolve
    systeme "Allan lui tend une bouteille fraîche. Théo s'assoit en soufflant."
    show allan beach neutral at char_left with dissolve
    t "Je dois quand même reprendre celui de quinze heures quarante. Je ne pourrai pas rester jusqu'au soir."
    a "On mange maintenant. Et on fera la photo avant que tu partes."
    show theo beach reassuring at char_right with dissolve
    t "Merci."
    a "T'as faim ?"
    t "Oui."
    show allan beach smirk at char_left with dissolve
    a "Bonne réponse."
    systeme "Les autres viennent le saluer entre deux allers-retours vers les sacs. Alexandre lui montre le plan avec une main déjà couverte de sable."
    x "Cette fois, la tour devrait tenir."
    t "Tu veux que je fasse le même côté ?"
    x "Oui. Après avoir mangé."
    a "Vous avez entendu ? Il l'a dit."

    scene bg arc2 beach main with fade
    show jessy beach neutral at char_left
    show ilona beach neutral at char_right
    with dissolve
    systeme "Après le repas, Ilona retrouve l'ancienne photo dans la conversation. Elle la montre à Jessy pendant qu'ils marchent vers les premiers murs du nouveau château."
    i "On l'avait prise ici, non ?"
    j "Plus près de l'eau, je crois."
    i "La glacière aurait été dans la pente."
    j "Peut-être plus haut, alors."
    systeme "Elle agrandit l'image. La rambarde derrière eux porte encore la même peinture claire."
    i "Je me souvenais que tu regardais Alexandre."
    j "Je regardais Sofiane courir après la serviette."
    i "Il courait ?"
    j "Sur deux pas. Un événement."
    show jessy beach smile at char_left
    show ilona beach smile at char_right
    with dissolve
    systeme "Ils se penchent sur l'écran. Derrière eux, Alexandre lève les deux bras."
    x "On a besoin d'un avis !"
    j "Sur quoi ?"
    x "Le pont-levis du restaurant."
    i "Pourquoi il y a un pont-levis ?"
    x "C'est précisément le débat."
    systeme "Ilona range son téléphone. Elle tend la petite pelle à Jessy et prend le seau."
    i "Viens. Ils vont nous faire une entrée par le toit."

    scene bg arc2 group parasol with dissolve
    show theo beach reassuring at char_right
    show allan beach smirk at char_left
    show alex beach grin at char_center
    with dissolve
    systeme "Un peu avant le départ de Théo, Ilona réclame tout le monde pour la photo. Cette fois, son téléphone tient sur un petit trépied."
    a "On progresse."
    i "Attends le résultat."
    systeme "Théo a remis sa chemise correctement. Alexandre s'essuie les mains. Sofiane vérifie que le sac à ses pieds est fermé."
    systeme "Jessy vient se placer au milieu et laisse assez de place pour qu'Ilona le rejoigne. Elle lance le retardateur."
    i "Dix secondes. C'est sûr, cette fois."
    a "Tout le monde regarde là."
    x "Attends. Je mets la pelle où ?"
    t "Par terre."
    x "Elle va cacher le château."
    a "Alexandre, baisse cette..."
    play sound audio.photo volume 0.4
    scene cg friend retrouvailles with Dissolve(0.2)
    stop music fadeout 2.0
    play music audio.springHope loop volume 0.55 fadein 2.0
    window hide
    pause 3.0
    window show
    systeme "Allan vient de lever le bras pour attraper la pelle. Théo s'écarte en riant. Sofiane regarde enfin l'objectif, pendant qu'Ilona arrive à sa place."
    systeme "Jessy a du sable sur la manche. Alexandre tient toujours son outil. Ils sont tous dans le cadre."
    i "Celle-là aussi, je la garde."
    window hide
    pause 2.0
    scene cg friend premier ete with Dissolve(1.5)
    pause 2.5
    scene cg friend retrouvailles with Dissolve(1.5)
    pause 2.0
    window show
    x "Bon. On a encore le temps pour le pont-levis."
    a "On a surtout le temps de manger une glace."
    i "La fraise nous regarde toujours aussi mal ?"
    j "On va vérifier."
    scene bg arc2 group parasol with dissolve
    show jessy beach smile at char_left
    show ilona beach smile at char_right
    with dissolve
    systeme "Ils reviennent avec six glaces. Théo regarde l'heure de son train, puis range son téléphone pour prendre la sienne."
    systeme "Une tour du château s'affaisse pendant qu'Alexandre mange. Il la regarde, hésite, puis reste assis avec les autres."
    j "On pourra la refaire."
    x "Oui. Quand on reviendra."
    systeme "La nouvelle photo arrive sur leurs téléphones. Jessy la regarde encore un instant, puis pose le sien entre les serviettes et reprend sa glace."
    stop ambiant1 fadeout 2.0
    scene black with Dissolve(2.0)
    jump ending_friend_generique


label ending_friend_generique:
    centered "GOOD ENDING\n\nFRIEND"
    centered "[config.name!t]\n\nLe dernier été"
    centered "Avec\n\nJessy et Ilona\nAllan, Alexandre, Sofiane et Théo"
    scene bg arc5 cafe with dissolve
    centered "Une table près de la gare."
    scene bg friend discord six with dissolve
    centered "Un anniversaire avec quelques jours de retard."
    scene bg arc2 minecraft house summer night with dissolve
    centered "Une heure pour jouer."
    scene cg friend retrouvailles with Dissolve(1.0)
    window hide
    pause 3.0
    scene black with Dissolve(1.5)
    centered "Merci d'avoir partagé leur histoire."
    stop music fadeout 2.0
    stop ambiant1 fadeout 1.0
    scene black with fade
    return
