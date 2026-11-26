# Les portraits 3 fournis pour le casting correspondent à ces sprites du jeu.
# Pour Lucy, le deuxième fichier est déjà le sprite.
define generique_distribution = (
    ("allan", "Allan", "CEO of Muchacho Company Corporation Industry & Co", 2),
    ("theo", "Théo", "« « « L’innocent » » » par qui tout a commencé", 2),
    ("alexandre", "Alexandre", "DJ pêcheur qui a pécho une feuille", 2),
    ("sofiane", "Sofiane", "Le cousin", 2),
    ("ilona", "Ilona", "Notre sublime déesse, Aphrodite", 2),
    ("florentin", "Florentin", "La naingénieux du royaume", 2),
    ("jessy", "Jessy", "Le vieux", 2),
    ("micka", "Micka", "L’homme fertile", 2),
    ("lucy", "Lucy", "La descendance de Jessy s’il avait des couilles", 1),
)

image generique merci = Transform("images/generic/merci_moulinette.png", xysize=(1920, 1080), fit="contain")
image generique chad = "images/generic/le_chad.png"

define generique_arcs_laplage = ("arc0", "arc1", "arc2", "arc3", "arc4", "arc5_1", "arc5_2", "arc6", "arc7_1", "arc7_2")

define generique_fins_casting = {"florentin": "ilonanium", "lucy": "family"}
default persistent.generique_fins_terminees = set()

transform generique_plouf:
    subpixel True
    alpha 0.0
    yoffset -220
    pause 0.55
    alpha 1.0
    easein 0.24 yoffset 18
    easeout 0.15 yoffset -12
    ease 0.13 yoffset 0

transform generique_tirage(numero):
    subpixel True
    alpha 0.0
    xoffset (180 if numero == 2 else -180)
    pause (0.34 if numero == 2 else 0.05)
    alpha 1.0
    easeout 0.25 xoffset (-14 if numero == 2 else 14)
    ease 0.14 xoffset 0

# Théo vérifie d'abord si quelqu'un le regarde.
transform generique_theo_discret:
    subpixel True
    yoffset 990
    easeout 0.30 yoffset 745
    pause 0.25
    easein 0.13 yoffset 990
    easeout 0.36 yoffset 0

transform generique_allan_derapage:
    subpixel True
    xoffset -920
    easeout 0.42 xoffset 155
    pause 0.20
    easein 0.24 xoffset -12
    ease 0.12 xoffset 0

transform generique_alexandre_hamecon:
    subpixel True
    yoffset 820
    easeout 0.30 yoffset 240 xoffset 45
    easein 0.19 yoffset 420 xoffset -25
    easeout 0.24 yoffset -55 xoffset 15
    easein 0.18 yoffset 0 xoffset 0

transform generique_sofiane_incruste:
    subpixel True
    xoffset -700
    easeout 0.32 xoffset -320
    pause 0.33
    ease 0.16 xoffset -360
    easeout 0.27 xoffset 0

transform generique_ilona_apparition:
    subpixel True
    alpha 0.0 yoffset -145
    parallel:
        linear 0.38 alpha 1.0
    parallel:
        easeout 0.54 yoffset -32
        pause 0.22
        easein 0.14 yoffset 8
        ease 0.14 yoffset 0

transform generique_florentin_armure:
    subpixel True
    yoffset -1050
    easein 0.48 yoffset 0
    linear 0.09 yzoom 0.88
    easeout 0.16 yzoom 1.02
    ease 0.14 yzoom 1.0

transform generique_jessy_petits_pas:
    subpixel True
    xoffset -310
    easeout 0.12 xoffset -260 yoffset -12
    easein 0.13 xoffset -210 yoffset 0
    pause 0.20
    easeout 0.14 xoffset -165 yoffset -10
    easein 0.13 xoffset -120 yoffset 0
    pause 0.28
    ease 0.17 xoffset 0

transform generique_micka_cadeaux:
    subpixel True
    rotate_pad False
    xoffset -360
    easeout 0.34 xoffset 0 rotate 9
    ease 0.22 rotate -7
    ease 0.18 rotate 4
    ease 0.15 rotate 0

transform generique_lucy_pousse:
    subpixel True
    zoom 0.12
    pause 0.35
    easeout 0.24 zoom 0.52
    pause 0.18
    easeout 0.28 zoom 1.06
    ease 0.16 zoom 1.0

define generique_entrees = {
    "allan": generique_allan_derapage,
    "theo": generique_theo_discret,
    "alexandre": generique_alexandre_hamecon,
    "sofiane": generique_sofiane_incruste,
    "ilona": generique_ilona_apparition,
    "florentin": generique_florentin_armure,
    "jessy": generique_jessy_petits_pas,
    "micka": generique_micka_cadeaux,
    "lucy": generique_lucy_pousse,
}

# De temps en temps, la diapo entre du mauvais côté et dépasse sa butée.
transform generique_dia_coincee:
    subpixel True
    align (0.5, 0.5)
    on show, replace:
        xoffset 700
        easeout 0.25 xoffset -75
        pause 0.16
        linear 0.09 xoffset -85
        easeout 0.17 xoffset 0

transform generique_dezoom_chad:
    subpixel True
    pos (0.5, 0.5)
    anchor (0.44, 0.145)
    zoom 2.45
    pause 0.8
    ease 5.5 zoom 0.70 anchor (0.5, 0.5)

style generique_texte is gui_text:
    color "#35242d"
    outlines []
    textalign 0.5
    xalign 0.5
    xmaximum 1640

style generique_titre is generique_texte:
    color "#98234b"
    size 76
    bold True

screen generique_piscines():
    add Solid("#fff7e9")
    vbox:
        align (0.5, 0.5)
        spacing 28
        text "Mais surtout, merci aux" style "generique_texte" size 46
        text "10 piscines olympiques" style "generique_titre" size 100 at generique_plouf
        text "qui ont permis de produire ce chef-d’œuvre." style "generique_texte" size 48
        null height 58
        text "Mention spéciale à l’Afrique. On pense à vous." style "generique_texte" size 40 italic True

screen generique_casting(fiche, role=False):
    $ identifiant, nom, titre, nb_photos = fiche[:4]
    add Solid("#fff7e9")

    if role:
        add Transform("images/generic/casting/%s_sprite.png" % identifiant, xysize=(930, 970), fit="contain"):
            align (0.14, 1.0)
            at generique_entrees[identifiant]
        vbox:
            xcenter 1370
            yalign 0.5
            spacing 12
            text "Dans le rôle de…" style "generique_texte" size 52 italic True
            text nom style "generique_titre" size 104
    else:
        hbox:
            xalign 0.5
            ypos 45
            spacing 28
            for numero in range(1, nb_photos + 1):
                frame:
                    at generique_tirage(numero)
                    background Solid("#fffdf8")
                    padding (12, 12)
                    add Transform("images/generic/casting/%s%d.webp" % (identifiant, numero), xysize=(820, 730), fit="contain") align (0.5, 0.5)
        vbox:
            xalign 0.5
            ycenter 922
            spacing 6
            text nom style "generique_titre"
            text titre style "generique_texte" size 44

screen generique_dedicace(message):
    text message:
        style "generique_texte"
        align (0.5, 0.5)
        xmaximum 1390
        size 48
        line_spacing 12
        color "#fff7e9"

init python:
    def generique_preparer_diapos():
        diapos = [("merci", None, 5.0, dissolve), ("piscines", None, 7.0, dissolve)]
        for fiche in generique_distribution:
            fin_requise = generique_fins_casting.get(fiche[0])
            if fin_requise and fin_requise not in persistent.generique_fins_terminees:
                continue
            diapos.append(("photos", fiche, 5.0, Dissolve(0.3)))
            diapos.append(("role", fiche, 2.5, Dissolve(0.3)))

        for arc in generique_arcs_laplage:
            photo = "images/generic/laplage/laplage_irl_%s.webp" % arc
            diapos.append(("photo", photo, 6.0, Dissolve(0.35)))

        album = sorted(p for p in renpy.list_files() if p.rpartition("/")[0] == "images/generic/album" and p.endswith(".webp"))
        renpy.random.shuffle(album)
        for index, photo in enumerate(album):
            if (len(album) - index - 1) % 4 == 2:
                diapos.append(("photo_coincee", photo, 4.0, None))
            else:
                diapos.append(("photo", photo, 4.0, Dissolve(0.3)))

        diapos.extend([
            ("chad", None, 8.0, None),
            ("noir", None, 1.2, Dissolve(0.8)),
            ("dedicace", "Après toutes ces années, on pense toujours à toi, Ilona. On te souhaite un merveilleux mariage et une vie à deux pleine d’amour, de rires et, inchallah, de plein de petits bouts de chou.\n\nPour les prénoms, tu as bien sûr le dernier mot… mais avoue qu’Allan, Théo, Alexandre, Micka et Sofiane, ça ferait une sacrée fratrie !", 23.0, dissolve),
            ("dedicace", "Encore merci pour toutes ces aventures !\nOn se revoit dans notre prochain projet.", 6.0, dissolve),
        ])
        diapos.append(("credits", None, generique_credits_duree, None))
        return diapos

screen generique_diapo(genre, contenu):
    add Solid("#000")
    if genre == "merci":
        add "generique merci" align (0.5, 0.5)
    elif genre == "piscines":
        use generique_piscines
    elif genre in ("photos", "role"):
        use generique_casting(contenu, role=(genre == "role"))
    elif genre in ("photo", "photo_coincee"):
        add Transform(contenu, xysize=(1920, 1080), fit="contain"):
            align (0.5, 0.5)
            if genre == "photo_coincee":
                at generique_dia_coincee
    elif genre == "chad":
        add "generique chad" at generique_dezoom_chad
    elif genre == "dedicace":
        use generique_dedicace(contenu)
    elif genre == "credits":
        use generique_credits

screen generique_commandes(duree, premiere):
    zorder 110
    key "K_LEFT" action (NullAction() if premiere else Return(-1))
    key "K_RIGHT" action Return(1)
    key "dismiss" action Return(1)
    timer duree action Return(1)

label generique:
    $ renpy.dynamic("quick_menu", "generique_diapos", "generique_index", "generique_genre", "generique_contenu", "generique_duree", "generique_transition", "generique_musique", "generique_piste", "fins_terminees")
    $ quick_menu = False
    $ fins_terminees = persistent.generique_fins_terminees.union(fin for fin in endings_seen if fin in generique_fins_casting.values())
    if fins_terminees != persistent.generique_fins_terminees:
        $ persistent.generique_fins_terminees = fins_terminees
        $ renpy.save_persistent()
    $ generique_diapos = generique_preparer_diapos()
    $ generique_index = 0
    $ generique_musique = None
    window hide
    scene black
    while generique_index < len(generique_diapos):
        $ generique_genre, generique_contenu, generique_duree, generique_transition = generique_diapos[generique_index]
        if generique_genre in ("dedicace", "credits"):
            $ generique_piste = "audio/music/love-piano.ogg"
        elif generique_genre in ("chad", "noir"):
            $ generique_piste = None
        else:
            $ generique_piste = "<from 40.00>audio/music/ilonanium_roundabout.ogg"

        if generique_piste != generique_musique:
            if generique_piste is None:
                stop music fadeout 0.0
            elif generique_genre == "dedicace":
                play music generique_piste loop volume 0.65 fadeout 0.0 fadein 0.5
            else:
                play music generique_piste loop volume 0.65 fadeout 0.0 fadein 0.0
            $ generique_musique = generique_piste

        show screen generique_diapo(generique_genre, generique_contenu) with generique_transition
        call screen generique_commandes(generique_duree, generique_index == 0)
        $ generique_index += _return
        hide screen generique_diapo

    stop music fadeout 0.5
    with dissolve
    return
