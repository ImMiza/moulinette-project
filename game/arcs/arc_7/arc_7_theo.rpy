# =============================================================================
# ARC VII - ROUTE THEO : LE MONDE APRES LA MAISON
# =============================================================================
# Mapping depuis arc 6 :
#   controle_repetitif >= 3         -> entree forcee ici
#   arc6_score < SEUIL_JESSY        -> entree ici
#   confidences_laplage >= 3        -> sortie Laplage possible si influence basse
#   influence_theo                  -> poids de la route Theo
#
# L'entree se fait TOUJOURS via arc_6_bascule_theo (fin de arc_6_diplomes.rpy),
# qui joue les onze jours du 26 mars au 6 avril et le depart en gare.
# Ne pas sauter ici directement depuis arc_6_calcul : la bascule ne serait
# plus jouee, seulement affirmee par la narration ci-dessous.
# =============================================================================

label arc_7_theo:
    $ derniere_route = "Route Theo"
    $ controle_repetitif = interruptions_ilona - interruptions_reparees

    scene bg stream
    with fade
    show jessy listening at char_center

    systeme "Arc VII - Le monde apres la maison."
    systeme "Ilona n'a pas choisi Theo. Elle est partie vers l'endroit ou on lui epargnait de parler. Ce n'est pas la meme chose, et c'est pire."

    # Rappel lisible du point de bascule de l'arc 6, sans afficher de jauge.
    if controle_repetitif >= 3:
        systeme "A la fin du diplome, ce ne sont pas les grandes erreurs qui ont tranche. Ce sont les petites coupures repetees."
    elif arc6_score < SEUIL_JESSY:
        systeme "A la fin du diplome, il n'y avait pas assez d'espace autour d'Ilona pour qu'elle reste sans se reduire."
    else:
        systeme "La route a garde une trace fausse. Quelque chose a ete force avant d'arriver ici."

    if arc6_offre_theo == "laisse":
        systeme "Jessy s'etait tu devant l'offre de Theo. Meme ca n'a pas suffi a defaire toute la dette."
    elif arc6_offre_theo == "accusation":
        systeme "Jessy avait accuse Theo de vouloir Ilona pour lui. Theo avait repondu avec une verite partielle. Elle a continue de mordre."
    elif arc6_offre_theo == "question":
        systeme "Jessy avait pose la bonne question trop tard : pourquoi aujourd'hui ? La reponse etait deja dans le train du 6 avril."
    elif arc6_offre_theo == "aveu_vide":
        systeme "Jessy avait dit qu'il n'avait rien a proposer. C'etait vrai. Le probleme, c'est que quelqu'un d'autre proposait deja tout."

    menu:
        "Ce qui se passe apres le depart."

        "Ilona s'extrait elle-meme." if confidences_laplage >= 3 and influence_theo <= 6:
            jump ending_monsieur_laplage

        "La dette se referme.":
            jump ending_theo_vtuber
