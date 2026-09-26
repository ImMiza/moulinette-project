# ENDING NEUTRE
# Route Théo, fin neutre après le choix final d'écouter Ilona.
# Attendu : Ilona reprend la main sur sa vie et le couple se sépare sans effacer
# ce qu'il a partagé.

label ending_neutre:
    $ record_ending("neutre")

    # ------------------------------------------------------------------
    # 1. La première soirée sans solution
    # ------------------------------------------------------------------
    scene bg arc7 tokyo house night
    with dissolve

    show ilona short sad at char_left
    show theo tokyo disappointed at char_right
    with dissolve

    systeme "Le silence tient encore quelques secondes. Puis le téléphone de Théo vibre contre la table, juste à côté du carnet de planning."
    systeme "Son regard tombe sur l'écran avant même qu'il ait le temps de choisir de ne pas le faire."

    t "C'est le studio."
    i "Je sais."
    t "Tu veux que je réponde ?"
    i "Non."
    t "D'accord."

    systeme "Théo maintient le bouton enfoncé. L'écran devient noir. Il pose le téléphone face contre la table, sans lire la suite de la notification."
    systeme "Ses yeux reviennent au carnet. Il pourrait déjà y barrer le stream, le rendez-vous sponsors, les appels du lendemain. Sa main ne bouge pas."

    show theo tokyo hesitant at char_right
    with dissolve

    t "Tu veux mon avis sur le message, ou tu veux juste que je reste là ?"
    i "Reste là. Sans réparer."
    t "D'accord."

    systeme "Ilona reprend son propre téléphone. Son pouce reste suspendu au-dessus de l'écran, puis elle ouvre elle-même le compte d'IlonaGaming."
    systeme "Elle écrit une phrase. L'efface. En écrit une autre, plus rassurante pour tout le monde, puis l'efface aussi."

    show ilona short sad_alt at char_left
    with dissolve

    systeme "La troisième version répète deux fois qu'elle ne sait pas. Elle la garde précisément pour ça."
    systeme "{i}« Je fais une pause. Je ne sais pas combien de temps. Je ne sais pas encore si je reviendrai. Merci de me laisser chercher la réponse loin des caméras. »{/i}"

    systeme "Théo relit le mot « réponse ». La formulation accroche un peu. Il inspire pour proposer mieux."

    t "Tu pourrais..."

    systeme "Il s'arrête avant la fin de la phrase."

    i "Tu allais corriger quelque chose ?"
    t "Oui."
    i "Et ?"
    t "Ce sont tes mots. Ils n'ont pas besoin d'être les meilleurs."

    systeme "Ilona regarde encore le message. Elle ne lui tend pas le téléphone pour obtenir une validation. Théo ne tend pas la main pour le prendre."
    systeme "Elle appuie elle-même sur « Publier »."

    $ renpy.pause(1.0, hard=True)

    systeme "La publication apparaît aussitôt sur son écran. Pendant une seconde, rien ne change dans la cuisine. Puis les premières notifications arrivent, serrées les unes contre les autres."
    systeme "Ilona coupe le son."

    i "C'est fait."
    t "Oui."

    $ renpy.pause(0.6, hard=True)

    systeme "Ses épaules redescendent enfin. Ce n'est pas du bonheur. Seulement la fin provisoire d'un effort qu'elle ne pouvait plus soutenir."
    systeme "Théo tire une chaise et s'assoit à l'autre bout de la table. Il ne cherche ni sa main, ni un baiser, ni la phrase qui prouverait qu'il a compris assez vite."

    i "Je suis toujours en colère."
    t "Je sais."
    i "Et soulagée. Les deux en même temps."
    t "D'accord."

    systeme "D'ordinaire, il aurait demandé ce qu'il pouvait faire de cette colère. Ce soir, il accepte qu'elle ne soit pas une tâche à terminer."
    systeme "Ils restent dans la cuisine, sans musique et sans solution. Entre eux, le carnet demeure fermé."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 2. Le prix du silence
    # ------------------------------------------------------------------
    #changement music 
    scene bg arc7 tokyo morning
    with fade

    show ilona short sad_alt at char_left
    show theo tokyo neutral at char_right
    with dissolve

    systeme "Le lendemain, Ilona se réveille à l'heure exacte où Théo ouvrait d'habitude les volets avant un tournage. Aucun réveil n'a sonné. Son corps, lui, n'a pas encore reçu l'information."
    systeme "Elle reste au lit jusqu'à midi. À quinze heures, elle s'assoit dans le salon avec un jeu lancé sur son ordinateur, puis le referme avant l'écran-titre. Même jouer ressemble encore à quelque chose qu'une caméra pourrait lui réclamer."
    systeme "Théo reçoit les appels dans sa chambre. Lorsqu'une question concerne Ilona, il vient frapper et attend qu'elle réponde avant d'entrer. Deux fois, elle dit non. Deux fois, il repart sans transmettre à sa place ce qu'il croit avoir compris."

    $ renpy.pause(0.6, hard=True)

    systeme "Pendant quatre jours, le studio ne répond pas publiquement. Il n'essaie ni de contredire Ilona, ni de transformer sa pause en événement."
    systeme "Le silence protège sa décision, mais il ne suspend ni le bail, ni les contrats, ni le travail de ceux qui attendaient le prochain direct."
    systeme "Le cinquième matin, les conséquences arrivent dans trois courriers très polis."
    systeme "La marque retire sa proposition de campagne sur six mois. Le studio confirme que le bail ira jusqu'à son terme, comme prévu, mais qu'il ne sera pas renouvelé sans reprise de la chaîne."
    systeme "La régie est répartie sur d'autres productions. Le monteur récupère une autre chaîne, les techniciens d'autres tournages. Personne n'est renvoyé. L'entreprise continue simplement sans IlonaGaming."
    systeme "Une dernière ligne précise que la marque accepterait de rouvrir les négociations si Ilona confirmait elle-même le premier stream sponsorisé."

    systeme "Ilona ouvre elle-même chaque courrier. Théo reste assis en face d'elle et ne traduit que les passages qu'elle lui demande."

    i "Donc ils ne nous mettent pas dehors aujourd'hui."
    t "Non. Ils vont au bout des huit mois prévus. On a jusqu'à la fin du mois."
    i "Trois semaines."
    t "À peu près."

    systeme "Sur l'écran, la proposition de la marque est encore visible sous le message qui la retire. Six mois de sécurité pourraient revenir avec un seul oui."

    show ilona short sad at char_left
    with dissolve

    i "Si je fais seulement le stream sponsorisé, on pourrait garder l'appartement."
    t "Probablement."
    i "Et l'équipe."
    t "Peut-être."
    i "Alors je devrais le faire."

    show theo tokyo hesitant at char_right
    with dissolve

    t "Tu en as envie ?"
    i "Non. Mais ce serait raisonnable."

    systeme "Le mot frappe Théo parce qu'il reconnaît sa propre voix à l'intérieur. « Raisonnable », c'est ce qu'il disait quand la peur avait déjà choisi et qu'il ne restait plus qu'à présenter ce choix comme une évidence."

    show theo tokyo disappointed at char_right
    with dissolve

    t "Si tu reprends parce que tu as peur de nous faire perdre l'appartement, ce sera encore une décision prise par le planning."
    i "Tu me dis de refuser ?"
    t "Non. J'essaie de ne plus te dire quoi répondre."

    systeme "Ilona regarde une dernière fois les chiffres de la campagne. Elle ferme la pièce jointe, mais pas le courrier."
    systeme "Le téléphone de Théo vibre sur la table. Cette fois, il lit seulement le nom affiché avant de lever les yeux vers elle."

    t "Le studio."
    i "Réponds."

    systeme "Théo décroche et active le haut-parleur. Après quelques formules prudentes, la direction lui demande ce qu'Ilona compte faire de la campagne et si elle pense reprendre."

    show theo tokyo neutral at char_right
    with dissolve

    t "Je ne sais pas. Il faut lui demander."

    systeme "Il retire le haut-parleur et tend le téléphone à Ilona. Il ne résume pas la situation pour elle. Il ne prépare pas non plus la réponse."
    systeme "Ilona prend l'appareil. Ses doigts tremblent assez pour qu'elle doive s'y reprendre à deux fois avant de l'approcher de son oreille."

    i "Bonjour. Oui, je suis là."
    i "J'ai bien reçu votre message."

    $ renpy.pause(0.8, hard=True)

    i "Non. Je ne ferai pas la campagne."

    $ renpy.pause(0.8, hard=True)

    i "Je comprends pour l'appartement et pour l'équipe."
    i "Et je n'ai pas de date de retour à vous donner, parce que je ne vais pas reprendre la chaîne."
    i "IlonaGaming va s'arrêter. Je vous enverrai ma décision par écrit."
    i "Merci de me l'avoir demandé directement."

    systeme "C'est la première fois qu'Ilona prononce la décision à voix haute. Ses doigts tremblent toujours lorsqu'elle rend le téléphone à Théo."
    systeme "La réponse coûte un appartement, une équipe et une sécurité qu'elle n'a jamais eue avant Tokyo. Le prix est réel. Cela ne transforme pas son refus en erreur."

    systeme "Avant de raccrocher, le studio demande à reprendre Théo. Il lui propose de rester, sur un autre poste : coordonner les tournages, le matériel, les transports et les plannings de plusieurs productions."
    systeme "Ce n'est ni une promotion, ni une consolation. L'appartement n'est pas compris et le salaire est celui d'un poste de production ordinaire. Mais le périmètre est clair : organiser le travail, pas décider de la vie de quelqu'un."

    t "Oui. Ça m'intéresse."

    systeme "Il pose quelques questions sur les horaires et les responsabilités, puis accepte. Cette décision-là lui appartient."

    i "Tu vas continuer à faire des plannings."
    t "Oui."
    i "Ça ne te fait pas peur ?"
    t "Non. J'aime organiser les choses."
    t "Le problème, ce n'était pas le carnet. C'était de croire qu'il pouvait répondre à ta place."
    i "Tu crois que tu sauras faire la différence ?"
    t "Pas toujours. Mais je vais devoir l'apprendre."

    systeme "Ilona pose les yeux sur le carnet resté fermé depuis cinq jours."

    i "Il va falloir chercher un autre appartement."
    t "Oui."
    t "Tu veux qu'on commence aujourd'hui ?"
    i "Non. Pas aujourd'hui."
    t "D'accord."

    systeme "Théo ne sort pas son téléphone. Tokyo continuera d'exister demain, avec ses annonces, ses cautions et ses loyers trop élevés. Aujourd'hui, le refus d'Ilona a le droit de ne produire aucune nouvelle tâche."

    show ilona short neutral at char_left
    with dissolve

    i "Je croyais que la pause me laisserait le temps de trouver une réponse."
    t "Et tu l'as trouvée ?"
    i "Je crois."
    i "Je ne veux plus être IlonaGaming."

    show theo tokyo disappointed at char_right
    with dissolve

    t "Alors il faudra que j'apprenne à ne pas appeler ça un échec."
    i "Moi aussi."

    systeme "Ilona ne sourit pas. Elle garde la décision entre ses mains, comme un objet encore lourd mais qui lui appartient enfin."
    systeme "Dans la cuisine, rien n'est réglé. Pour la première fois, ce qui reste à régler n'efface pas la réponse qu'elle vient de donner."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 3. La fin d'IlonaGaming
    # ------------------------------------------------------------------
    scene bg arc7 tokyo morning
    with fade

    systeme "Le lendemain, Ilona annonce un dernier direct. Pas de compte à rebours, pas d'horaire choisi pour l'algorithme, pas d'événement construit autour de son départ. Seulement quelques minutes pour dire elle-même au revoir."
    systeme "Elle choisit un mur clair de l'appartement et pose son téléphone contre deux livres. Puis elle ressort la veste bleue et la longue perruque blanche d'IlonaGaming."
    systeme "Personne ne lui a demandé de les remettre. Elle veut que le public reconnaisse celle qui lui parle une dernière fois — et décider elle-même du moment où elle cessera de l'être."

    show ilona streaming fatigue at char_left
    show theo tokyo hesitant at char_right
    with dissolve

    systeme "Théo reste près de la porte. Il n'a préparé ni texte, ni lumière, ni liste des choses à ne pas oublier."

    t "Tu veux que je sorte ?"
    i "Non. Mais reste derrière la caméra."
    t "D'accord."

    hide theo
    show ilona streaming fatigue at char_center
    with dissolve

    systeme "Ilona vérifie elle-même le cadre. Une mèche blanche dépasse. Elle la laisse. Puis elle lance le direct et revient s'asseoir pendant que le compteur grimpe."

    i "Bonjour."

    $ renpy.pause(0.8, hard=True)

    i "Ce sera mon dernier stream. Je voulais vous le dire moi-même, sans compte à rebours et sans événement autour."
    i "J'ai aimé streamer. J'ai aimé vous rencontrer et construire cette chaîne. Puis, à un moment, j'ai continué parce que tout le monde savait mieux que moi pourquoi je devais continuer."
    i "À force d'entendre toutes ces raisons, je n'entendais plus la mienne."
    i "IlonaGaming a été une partie de moi. Mais je ne veux plus qu'elle prenne toute la place. Alors je ne reviendrai pas."

    i "Je vais laisser les anciennes vidéos en ligne. Je ne veux pas effacer ce qu'on a fait ensemble. Je veux seulement empêcher ce passé de décider de la suite."
    i "Merci d'avoir été là. Prenez soin de vous."

    systeme "Ilona se penche vers le téléphone et coupe elle-même le direct. Il a duré moins de trois minutes. Le chat défilait trop vite pour être lu ; elle n'a essayé de retenir aucun dernier message."
    systeme "Elle retire la perruque blanche, puis plie la veste bleue sur le dossier de la chaise. Cette fois, personne ne lui indique quand changer de costume."

    show theo tokyo neutral at char_right
    show ilona short sad_alt at char_left
    with dissolve

    t "Tu veux revoir le replay ?"
    i "Non."
    t "D'accord."

    systeme "Elle laisse le replay en ligne sans coupe et sans miniature fabriquée pour retenir le regard. Puis elle annule les directs programmés et ferme les abonnements qui promettaient encore des contenus à venir."
    systeme "Dans les réglages, Ilona passe devant l'option qui supprimerait définitivement la chaîne. Elle ne l'ouvre pas. Les premiers directs maladroits, les parties ratées et les soirées heureuses restent accessibles."
    systeme "Elle ne détruit pas son passé. Elle lui retire seulement le droit de décider de son avenir."

    i "C'est fini."
    t "Oui."

    $ renpy.pause(0.8, hard=True)

    systeme "Théo pense que le plus dur est terminé. La campagne est refusée, le studio prévenu, le dernier direct achevé. Il ne reste, croit-il, que des problèmes concrets : des cartons, un logement et une nouvelle fiche de poste."
    systeme "Il sait résoudre les problèmes concrets. Une part de lui recommence déjà à respirer."

    i "Théo."
    t "Hm ?"
    i "Il faut que je te dise autre chose."
    t "Je t'écoute."

    show ilona short sad at char_left
    show theo tokyo disappointed at char_right
    with dissolve

    play music audio.sadness volume 0.7 loop fadeout 1.0 fadein 3.0
    i "Je vais partir."

    $ renpy.pause(1.2, hard=True)

    systeme "Cette fois, Théo n'a pas de réponse prête."

    # ------------------------------------------------------------------
    # 4. Ce que l'écoute ne répare pas
    # ------------------------------------------------------------------
    play music audio.apartsad volume 0.45 loop fadein 3.0

    t "Partir où ?"
    i "Je ne sais pas encore. Mais je vais quitter Tokyo."

    systeme "Le regard de Théo glisse vers le téléphone. Horaires de vol, prix des billets, date de fin du bail : les premières cases d'un nouveau plan apparaissent déjà dans sa tête. Il ne touche pas l'appareil."

    t "Pour combien de temps ?"
    i "Je ne sais pas. Peut-être longtemps."
    t "À cause de la chaîne ?"
    i "Pas seulement."
    i "Je ne crois pas qu'une autre ville me donnera toutes les réponses. Mais j'ai besoin d'arriver quelque part dans une vie que tu n'auras pas organisée avant moi."

    show ilona short sad_alt at char_left
    with dissolve

    i "Quand on est arrivés, tout était déjà prêt. L'appartement, le studio, les rendez-vous, même le chemin entre les trois."
    i "J'ai aimé ça. J'ai aimé que tu rendes les choses possibles avant même que je sache comment les demander."
    i "Mais maintenant, je ne sais plus quelle partie de cette vie j'ai choisie et quelle partie était simplement assez bien organisée pour que je la suive."

    show theo tokyo hesitant at char_right
    with dissolve

    t "On peut trouver un autre appartement. Plus petit. Je peux rester en dehors de tes projets."
    i "Je sais."
    t "Alors pourquoi tu pars ?"
    i "Parce que même quand tu ne décides plus, je cherche encore ton avis avant de savoir ce que je pense."
    i "J'ai besoin de découvrir qui je suis quand tu n'es pas dans la pièce."

    systeme "Théo baisse les yeux vers la chaise qu'il occupait pendant l'enregistrement. Il était hors du cadre. Il était tout de même la première personne qu'Ilona avait regardée une fois la caméra coupée."

    t "Je pourrais te laisser plus d'espace."
    i "Tu le fais déjà. Depuis quelques jours, tu le fais vraiment."
    t "Mais ça ne suffit pas."
    i "Pas pour réparer ce qui s'est installé en moi. Pas ici. Pas avec toi juste à côté."

    show theo tokyo disappointed at char_right
    with dissolve

    t "Tu regrettes d'être venue avec moi ?"
    i "Non."
    i "Je suis venue parce que je le voulais. Je suis restée parce qu'une partie de moi le voulait encore. Et une autre partie a fini par ne plus savoir partir. Les trois peuvent être vrais."

    systeme "Cette réponse ne désigne aucun coupable assez simple pour être détesté. Elle ne rend pas non plus les mois heureux mensongers."

    t "Tu veux qu'on essaie à distance ?"
    i "Non."
    t "Tu veux que je t'attende ?"
    i "Non plus. Je ne veux pas que mon départ devienne une nouvelle promesse à tenir."

    $ renpy.pause(1.0, hard=True)

    systeme "Théo pourrait proposer une durée. Trois mois séparés, puis un appel. Six mois, puis une décision. Il pourrait donner à l'incertitude des étapes et à l'espoir une date de révision."
    systeme "Ce serait encore un planning. Seulement plus tendre."

    t "D'accord."
    i "Tu as le droit de ne pas être d'accord."
    t "Je ne le suis pas."
    t "Je trouve ça horrible."

    show ilona short sad at char_left
    with dissolve

    i "Moi aussi."

    systeme "Il n'y a pas de colère dans sa réponse. Seulement la fatigue d'aimer encore quelqu'un qu'elle doit quitter pour réussir à s'entendre elle-même."

    t "J'ai envie de te dire que je peux encore réparer ça."
    i "Je sais."
    t "J'ai arrêté de répondre à ta place. J'ai rendu le téléphone. J'ai accepté que la chaîne s'arrête..."

    systeme "Les preuves sortent malgré lui. Elles sont vraies. Elles commencent déjà à prendre la forme d'un prix qu'Ilona devrait payer en restant. Théo s'interrompt."

    t "Mais tu ne me le demandes pas."
    i "Non."
    t "Alors je ne vais pas le faire."

    systeme "Son changement ne rachète rien. Il ne lui donne aucun droit sur la suite. Pour la première fois, Théo accepte que faire mieux puisse seulement empêcher une dernière blessure, pas annuler toutes les précédentes."

    i "Je ne veux pas que tu penses que je n'ai rien aimé."
    t "Je ne le pense pas."
    i "Je t'aime encore."

    $ renpy.pause(0.8, hard=True)

    t "Moi aussi."

    systeme "Aucun des deux n'ajoute que cela devrait suffire."

    t "Est-ce que je peux te prendre dans mes bras ?"
    i "Oui."
    i "Mais ça ne change pas ma réponse."
    t "Je sais."

    systeme "Théo traverse enfin l'espace entre eux. Ilona pose son front contre son épaule et ferme les yeux. Ils ne s'embrassent pas. Ils ne promettent pas de se retrouver."
    systeme "Ils restent enlacés assez longtemps pour reconnaître ce qu'ils perdent, puis Ilona recule la première."

    i "Je n'ai pas encore choisi où aller."
    t "Tu veux de l'aide ?"
    i "Pas pour choisir."
    t "D'accord."

    systeme "La réponse lui fait mal. Théo la respecte quand même."
    systeme "Ils se séparent sans colère. Ils s'aiment encore, et c'est précisément ce qui empêche la scène de leur offrir un soulagement facile."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 5. Ce qu'on emporte
    # ------------------------------------------------------------------
    scene bg arc7 tokyo morning
    with fade

    systeme "Les deux jours suivants, l'appartement change de fonction. Les cartons ne préparent plus leur prochain projet. Ils séparent ce qu'Ilona emporte, ce que Théo garde et ce qui n'appartenait réellement qu'au studio."
    systeme "Ils dorment derrière deux portes fermées. Le matin, chacun attend d'entendre l'autre bouger avant d'entrer dans la cuisine. Leur séparation est décidée ; leurs habitudes, elles, continuent encore quelques heures par inertie."

    show ilona short neutral at char_left
    show theo tokyo neutral at char_right
    with dissolve

    systeme "Ilona réserve seule son billet. Elle choisit la ville, l'heure et une chambre pour les premières nuits. Quand elle pose son téléphone sur la table, il n'y a pas de trajet retour affiché à l'écran."
    systeme "Elle donne à Théo le nom de la ville et l'heure du départ. Pas pour obtenir son avis ; seulement parce qu'ils partagent encore un toit et qu'elle ne veut pas disparaître sans un mot."

    i "Je pars vendredi matin."
    t "D'accord."

    systeme "Théo connaît la ligne, la durée du trajet et les correspondances possibles. Il pourrait vérifier en quelques secondes si elle a choisi le départ le plus simple."

    t "Tu as tout ce qu'il te faut ?"
    i "Pour commencer, oui."
    t "D'accord."

    systeme "Il ne demande pas à voir le billet. Ilona ne lui montre pas la réservation pour être rassurée. Entre eux, ce petit silence ressemble moins à un vide qu'à une frontière neuve, encore fragile."

    show ilona short sad_alt at char_left
    with dissolve

    systeme "Dans la chambre, sa valise se remplit mal. Les vêtements roulés par Ilona prennent plus de place que lorsqu'ils étaient pliés par Théo. Elle recommence une fois, s'agace, puis garde son propre désordre."
    systeme "Sur le lit restent une veste trop chaude, le petit carnet de croquis et le porte-clés bloc que Théo avait retrouvé à la plage."

    t "Tu peux encore prendre la veste."
    i "Je sais."
    t "Pardon."
    i "Non. Là, tu me donnes juste ton avis. C'est à moi de décider ce que j'en fais."

    systeme "Ilona glisse le carnet et le porte-clés dans la poche intérieure de la valise. Elle laisse la veste sur le lit."

    i "Tu peux m'aider à fermer ?"
    t "Oui."

    systeme "Théo appuie sur le couvercle pendant qu'Ilona tire elle-même la fermeture. Il retire ses mains dès que les deux curseurs se rejoignent."

    t "Tu veux que je t'accompagne vendredi ?"
    i "Jusqu'au quai."
    t "D'accord."

    $ renpy.pause(0.8, hard=True)

    systeme "Le dernier soir, ils mangent dans la cuisine au milieu des cartons. Ilona boit dans le mug bleu qu'elle compte ranger après l'avoir lavé. Théo ne lui rappelle pas de le faire."
    systeme "Ils parlent peu. Ce n'est plus le silence de quelqu'un qui attend la bonne réponse. C'est celui de deux personnes qui savent qu'il reste une nuit et refusent de la transformer en discours."

    hide theo
    hide ilona
    with dissolve

    # ------------------------------------------------------------------
    # 6. Jusqu'au quai
    # ------------------------------------------------------------------
    scene bg arc7 tokyo arrival
    with fade

    play ambiant1 audio.foule volume 0.35 loop fadein 2.0

    systeme "Quelques jours plus tard, la gare avale les voyageurs par centaines. Ilona garde son billet dans la poche de son manteau. Le nom de la ville où elle va est un choix qui n'appartient qu'à elle."
    systeme "Huit mois plus tôt, sa valise avait cogné l'arrière de ses jambes dès l'ouverture des portes. Théo en connaissait le poids au gramme près et la lui avait presque aussitôt prise des mains."
    systeme "Aujourd'hui, la poignée reste dans la main d'Ilona."

    show ilona short sad_alt at char_left
    show theo tokyo neutral at char_right
    with dissolve

    t "Tu veux que je la prenne ?"
    i "Jusqu'au quai. Après, je la reprends."
    t "D'accord."

    systeme "Ilona lui tend la poignée. Théo attend qu'elle ait complètement lâché avant de tirer la valise."
    systeme "Ils traversent la gare côte à côte. Il ne marche pas devant elle. Elle n'a pas besoin de lui demander de ralentir."

    t "Le thon-mayo est officiellement passé premier."
    i "Tu changes ton classement le jour où je pars ?"
    t "L'onigiri au saumon était sec."
    i "Trahison confirmée."

    systeme "Ils dépassent le konbini sans s'arrêter. Un peu plus loin, Ilona désigne le badge neuf accroché à la veste de Théo."

    i "C'est ta photo pour le nouveau poste ?"
    t "Oui."
    i "On dirait qu'on vient de t'annoncer qu'un tableur pouvait mentir."
    t "La photographe m'a demandé d'avoir l'air sérieux."
    i "Elle doit être très fière."

    show theo tokyo hesitant at char_right
    with dissolve

    t "Elle a fait trois prises."
    i "Et c'était la meilleure ?"
    t "Je préférais quand on parlait des onigiris."

    systeme "Ilona laisse échapper un rire bref. Il s'arrête presque aussitôt, mais il a existé."

    $ renpy.pause(0.5, hard=True)

    systeme "Après, ils parlent de la pluie annoncée, d'une fermeture de ligne et du mug bleu qu'Ilona a oublié dans un placard. Pas de leur relation. Pas de ce qu'ils auraient pu faire autrement."
    systeme "Le silence entre les phrases fait déjà suffisamment mal."

    scene bg arc7 tokyo arrival
    with dissolve

    show ilona short sad at char_left
    show theo tokyo disappointed at char_right
    with dissolve

    systeme "Sur le quai, une ligne claire marque l'endroit où attendre. Théo arrête la valise juste derrière et tourne la poignée vers Ilona."

    t "Voilà."
    i "Merci."

    systeme "Ses doigts se referment sur la poignée encore tiède. Le geste ne prend qu'une seconde. Aucun des deux ne trouve pourtant quelque chose à faire de ses mains ensuite."
    systeme "Le mot « reviens » monte jusqu'à la gorge de Théo. Il ne le prononce pas. Son téléphone reste dans sa poche ; il ne demande ni promesse d'écrire, ni fréquence d'appel, ni date à laquelle ils devront se reparler."

    t "Est-ce que je peux te prendre dans mes bras ?"
    i "Oui. Mais pas pour me retenir."
    t "D'accord."

    systeme "Théo s'approche. Ilona passe les bras autour de lui et, pendant quelques secondes, la gare disparaît derrière le bruit des manteaux froissés et de leurs respirations mal tenues."
    play sound audio.trainstop volume 0.6
    systeme "Une annonce retentit. Le train entre en gare. Les portes s'ouvrent devant eux."

    $ renpy.pause(0.6, hard=True)

    systeme "Théo lâche prise le premier."

    show ilona short neutral at char_left
    with dissolve

    systeme "Ilona reprend sa valise. Elle avance d'un pas, puis se retourne."

    i "Tu vas t'en sortir ?"
    t "Je ne sais pas encore."
    i "C'est nouveau."

    show theo tokyo hesitant at char_right
    with dissolve

    t "J'apprends."

    systeme "Le coin de la bouche d'Ilona tremble comme s'il hésitait entre un sourire et autre chose. Elle hoche la tête."
    systeme "Puis elle monte. La valise franchit les portes après elle."

    hide ilona
    show theo tokyo disappointed at char_center
    with dissolve

    systeme "Les portes se referment. À travers la vitre, Ilona lève une main. Théo fait le même geste. Aucun des deux ne transforme cet adieu en promesse."
    play sound audio.trainPassing volume 0.6
    systeme "Le train démarre. Théo reste sur le quai jusqu'à ce que la dernière voiture disparaisse."
    systeme "L'écran des départs affiche déjà le prochain horaire. Il ne le regarde pas."

    stop ambiant1 fadeout 2.0
    stop music fadeout 2.5

    $ renpy.pause(1.0, hard=True)

    scene black
    with fade

    systeme "Ilona ne sait pas encore ce qu'elle veut devenir."

    $ renpy.pause(0.5, hard=True)

    systeme "Théo ne sait pas encore qui il sera sans elle."

    $ renpy.pause(0.8, hard=True)

    systeme "Cette fois, personne ne remplit le blanc à sa place."

    return
