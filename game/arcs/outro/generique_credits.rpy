define generique_credits_roles = (
    ("Développement et conception des arcs et des calculs de jeu", "Allan"),
    ("Développement de la gestion des musiques et des effets sonores", "Alexandre"),
    ("Conception des décors et des sprites", "Allan et Théo"),
    ("Conception et écriture du scénario", "Allan, Alexandre et Théo"),
    ("Scribe", "Théo"),
    ("Soutien moral", "Allan"),
    ("Cascadeur pêcheur professionnel", "Alexandre"),
    ("Président-directeur général de Muchacho Company Corporation Industry & Co", "Allan"),
    ("Vice-président chargé de prononcer le nom de l’entreprise", "Sofiane"),
    ("Responsable des réunions qui auraient pu être un message Discord", "Jessy"),
    ("Responsable des messages Discord qui deviennent des réunions", "Théo"),
    ("Déesse titulaire", "Ilona"),
    ("Doublure d’Aphrodite pendant sa pause déjeuner", "Ilona"),
    ("Cousin officiel", "Sofiane"),
    ("Cousin par intérim en cas d’absence du cousin", "Sofiane"),
    ("Consultant en ancienneté", "Jessy"),
    ("Référent fertilité, résultats à l’appui", "Micka"),
    ("Expert en petits sauts qui passent à la caméra", "Lucy"),
    ("Naingénieux en chef du royaume", "Florentin"),
    ("Responsable du bruit quand l’armure tombe par terre", "Florentin"),
    ("Technicien en dérapage de CEO", "Allan"),
    ("Témoin oculaire à l’innocence irréprochable", "Théo"),
    ("Expert en guillemets autour du mot « innocent »", "Alexandre"),
    ("Direction du département « Par qui tout a commencé »", "Théo"),
    ("Service des archives compromettantes", "Toute la bande"),
    ("Archiviste de la photo que personne ne voulait revoir", "Allan"),
    ("Personne qui voulait revoir la photo", "Alexandre"),
    ("Contrôle qualité des captures prises au pire moment", "Ilona"),
    ("Spécialiste des yeux fermés sur les photos de groupe", "Jessy"),
    ("Gestionnaire du retardateur réglé sur deux secondes", "Micka"),
    ("Photobombeur en arrière-plan", "Monsieur Laplage"),
    ("Photobombeurs derrière le photobombeur", "Allan, Théo, Alexandre, Micka et Sofiane"),
    ("Responsable de la discrétion des cinq types derrière Laplage", "Poste vacant"),
    ("Maître-nageur des dix piscines olympiques", "Monsieur Laplage"),
    ("Responsable du comptage des piscines", "Allan"),
    ("Responsable du recomptage parce qu’il en manquait une", "Sofiane"),
    ("Figuration aquatique", "Les dix piscines olympiques"),
    ("DJ de la pêche à la feuille", "Alexandre"),
    ("Feuille pêchée dans le rôle de la prise du siècle", "Une feuille"),
    ("Bureau de vérification des mensurations de la feuille", "Micka"),
    ("Délégation chargée d’expliquer pourquoi ce n’est pas un poisson", "Ilona"),
    ("Consultant technique sur la tenue de maid", "Sofiane"),
    ("Évaluatrice des prestations au maid café", "Ilona"),
    ("Responsable du nombre de « maître » par commande", "Sofiane"),
    ("Préposé à la disparition des derniers takoyaki", "Alexandre"),
    ("Gestionnaire des cadeaux empilés trop haut", "Micka"),
    ("Responsable du papier cadeau coupé trop court", "Allan"),
    ("Contrôle douanier des cadeaux à l’entrée du salon", "Lucy"),
    ("Directeur des travaux sur Minecraft", "Jessy"),
    ("Responsable des coffres « à trier plus tard »", "Allan"),
    ("Inspectrice des maisons qu’on avait promis de ne pas casser", "Ilona"),
    ("Consultant en portes laissées ouvertes", "Théo"),
    ("Responsable du panneau « Ne pas toucher », juste à côté du levier", "Florentin"),
    ("Opérateur du levier", "Monsieur Laplage"),
    ("Pilote du projecteur qui coince", "Micka"),
    ("Technicien chargé de taper une fois sur le projecteur", "Alexandre"),
    ("Chef du service « Tape encore, mais moins fort »", "Sofiane"),
    ("Conseiller en dézoom de Chad", "Théo"),
    ("Responsable du maintien du menton pendant le dézoom", "Chad"),
    ("Chef de cabine du silence gênant", "Jessy"),
    ("Consultante sur les prénoms de la future fratrie", "Ilona"),
    ("Comité autoproclamé des prénoms de la future fratrie", "Allan, Théo, Alexandre, Micka et Sofiane"),
    ("Personne qui a demandé un générique un peu plus long", "Allan"),
    ("Personne qui trouvait déjà le générique trop long", "Allan, cinq minutes plus tard"),
    ("Soutien moral du soutien moral", "Allan"),
    ("Supervision du défilement des crédits", "Théo"),
    ("Contrôle du bon fonctionnement de la flèche droite", "Toi, si tu craques"),
    ("Responsable de la dernière ligne", "Jessy"),
    ("Responsable de la ligne après la dernière ligne", "Sofiane"),
    ("Responsable de nous rappeler qu’on avait dit « la dernière »", "Ilona"),
    ("Surveillance de la salle jusqu’à la fermeture", "Monsieur Laplage"),
    ("Extinction des lumières", "Toi, si tu es encore là"),
)

define generique_credits_hauteur = 140 + len(generique_credits_roles) * 100
define generique_credits_duree = (1080 + generique_credits_hauteur) / 48.0

transform generique_credits_defilement:
    subpixel True
    xalign 0.5
    yanchor 0.0
    ypos 1080
    linear generique_credits_duree ypos -generique_credits_hauteur

screen generique_credits():
    vbox at generique_credits_defilement:
        xsize 1680
        fixed:
            ysize 140
            text "Moulinette" style "generique_titre" color "#fff7e9" align (0.5, 0.5)
        for role, nom in generique_credits_roles:
            fixed:
                ysize 100
                vbox:
                    align (0.5, 0.5)
                    spacing 4
                    text role style "generique_texte" size 28 color "#e7b9c7"
                    text nom style "generique_texte" size 38 color "#fff7e9" bold True
