# ENDING NEUTRE
# Route Theo, fin neutre apres le choix final d'ecouter Ilona.
# Attendu : le couple reste ensemble, mais Ilona reprend la main sur son projet.

label ending_neutre:
    scene bg arc7 tokyo morning
    with fade
    $ record_ending("neutre")

    systeme "Fin neutre - Une porte ouverte dans le planning."

    show ilona fatigue at char_left
    show theo neutral at char_right
    with dissolve

    systeme "Le lendemain, la cuisine de la maison est silencieuse. Les deux autres colocataires sont partis avant l'aube pour leur tournage exterieur ; leurs tasses sechent pres de l'evier."
    systeme "Il n'y a pas de stream. Pas de tweet programme. Pas de faux suspense pour expliquer l'absence."
    systeme "Ilona a ecrit elle-meme une notification courte : pause indefinie. Theo l'a lue seulement apres sa publication."

    i "Indefinie, ca veut dire quoi exactement ?"
    t "Ca veut dire que je n'ai pas mis de date de retour a ta place."

    show ilona neutral at char_left
    with dissolve

    i "Et si je reviens differemment ?"
    t "Alors ce sera different."
    i "Et si je ne reviens pas ?"

    show theo disappointed at char_right
    with dissolve

    t "..."
    t "Alors il faudra que j'apprenne a ne pas appeler ca un echec."

    systeme "Ilona ne sourit pas tout de suite. Elle garde la phrase dans ses mains, comme un objet qu'on lui rend sans demander de reponse immediate."

    hide theo
    hide ilona
    with dissolve

    scene bg beach
    with fade

    show laplage neutral at char_center
    with dissolve

    laplage "Une porte ouverte, ce n'est pas une garantie."
    show laplage thumb_up at char_center
    laplage "Mais c'est deja moins lourd qu'une cle gardee par quelqu'un d'autre."

    scene black
    with fade

    systeme "Ilona ne sait pas encore ce qu'elle veut devenir."
    systeme "Cette fois, personne ne remplit le blanc a sa place."

    return
