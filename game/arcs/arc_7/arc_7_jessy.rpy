# =============================================================================
# ARC VII - ROUTE JESSY : FESTIVAL D'ETE
# =============================================================================
# Mapping depuis arc 6 :
#   arc6_score >= SEUIL_JESSY       -> entree ici
#   arc6_score >= SEUIL_ROMANCE     -> option romance possible si lien suffisant
#   arc6_conversation               -> posture du toit
#   arc6_derniere_construction      -> dernier geste Minecraft
#   arc6_gateau_planete             -> 5e objet cosmique valide
# =============================================================================

label arc_7_jessy:
    $ derniere_route = "Route Jessy"

    scene bg festival
    with fade
    show jessy smile at char_left
    show ilona smile at char_right

    systeme "Arc VII - Festival d'ete : les lanternes ne choisissent pas."
    systeme "Ilona a choisi un endroit ou elle peut parler. Ce n'est pas une victoire de Jessy. C'est une place qu'elle a prise."

    # Rappel lisible du point de bascule de l'arc 6, sans afficher de jauge.
    if arc6_score >= SEUIL_ROMANCE and lien_jessy_ilona >= SEUIL_LIEN:
        systeme "Le soir du diplome, Jessy n'a pas gagne une reponse. Il a laisse assez de place pour qu'elle puisse exister."
    elif arc6_conversation in ("que_veux_tu", "aveu_interruptions"):
        systeme "Le soir du diplome, une question est restee ouverte au lieu de se refermer sur elle. C'est peu. C'est exactement assez."
    else:
        systeme "Le soir du diplome n'a rien resolu. Il a seulement evite de tout casser."

    if arc6_derniere_construction == "porte_ouverte":
        systeme "Dans la maison, la porte inutile a une sortie. Elle ne sert toujours a rien. C'est pour ca qu'Ilona la garde."
    elif arc6_derniere_construction == "panneau_partir":
        systeme "Dans la maison, deux panneaux tiennent encore debout : finir ses phrases, et avoir le droit de partir."
    elif arc6_derniere_construction == "silence":
        systeme "Dans la maison, il n'y a pas eu de derniere construction. Seulement du temps passe sans remplir le silence."
    elif arc6_derniere_construction == "cadenas":
        systeme "Dans la maison, le cadenas existe encore. Jessy sait que certaines protections ressemblent trop a des portes fermees."

    # Le 6e objet cosmique (bloc-lune) se collecte ici, juste avant le menu final.
    if ilonanium_points >= 5:
        systeme "Sur un stand, entre deux masques, il y a un bloc qui ressemble beaucoup trop a un morceau de lune."
        i "Je le prends."
        j "C'est un bonbon."
        i "C'est un bloc-lune, Jessy."
        $ ilonanium_points += 1

    menu:
        "Comment se termine le festival ?"

        "Rester ensemble, sans se mettre ensemble.":
            jump ending_no_contact

        "Laisser Ilona finir la planete." if ilonanium_points >= 6:
            jump ending_ilonanium

        "Dire ce qu'il veut, en la laissant repondre non." if arc6_score >= SEUIL_ROMANCE and lien_jessy_ilona >= SEUIL_LIEN:
            if souvenirs["jessy_repare"] and souvenirs["maison_respectee"] and interruptions_reparees >= 1:
                jump ending_family
            else:
                jump ending_jessy_ilona
