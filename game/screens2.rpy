################################################################################
## screens.rpy — Notre Histoire UI v2.0 (Ren'Py 8.5.3)
################################################################################

init offset = -1

###############################################################################
## TRANSFORMATIONS
###############################################################################

transform menu_hover:
    on idle:
        zoom 1.0 alpha 0.95
    on hover:
        ease .15 zoom 1.03 alpha 1.0

###############################################################################
## MENU PRINCIPAL
###############################################################################

screen main_menu():

    tag menu

    # Fond (temporaire tant que ton PNG Figma n'est pas ajouté)
    add Solid("#FFF7FB")

    frame:
        background None
        xpos 120
        ypos 240

        vbox:
            spacing 18

            textbutton _("Nouvelle partie"):
                style "main_menu_button"
                action Start()

            textbutton _("Continuer"):
                style "main_menu_button"
                action ShowMenu("load")

            textbutton _("Charger"):
                style "main_menu_button"
                action ShowMenu("load")

            textbutton _("Galerie"):
                style "main_menu_button"
                action ShowMenu("gallery")

            textbutton _("Paramètres"):
                style "main_menu_button"
                action ShowMenu("preferences")

            textbutton _("Quitter"):
                style "main_menu_button"
                action Quit(confirm=True)

###############################################################################
## DIALOGUE
###############################################################################

screen say(who, what):

    window:
        style "say_window"

        if who is not None:

            text who:
                style "say_label"

        text what:
            style "say_dialogue"

    use quick_menu

###############################################################################
## CHOIX
###############################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

###############################################################################
## QUICK MENU
###############################################################################

screen quick_menu():

    zorder 100

    if quick_menu:

        frame:
            style "quick_menu_frame"

            xalign 0.5
            yalign 1.0

            hbox:
                spacing 22

                textbutton _("Retour") action Rollback()
                textbutton _("Historique") action ShowMenu("history")
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Skip") action Skip()
                textbutton _("Sauver") action ShowMenu("save")
                textbutton _("Menu") action ShowMenu("preferences")

###############################################################################
## SAUVEGARDE / CHARGER
###############################################################################

screen save():

    tag menu

    use file_slots(_("Sauvegarder"), "save")

screen load():

    tag menu

    use file_slots(_("Charger"), "load")


screen file_slots(title, mode):

    add Solid("#F8FAFC")

    frame:
        style "menu_frame"

        xalign 0.5
        yalign 0.5

        vbox:
            spacing 25

            text title style "menu_title"

            grid 3 2:
                spacing 24

                for i in range(1, 7):

                    button:

                        style "slot_button"

                        if mode == "save":
                            action FileSave(i)
                        else:
                            action FileLoad(i)

                        has vbox

                        frame:
                            background "#DBEAFE55"
                            xsize 500
                            ysize 220

                        text FileTime(i, empty="Emplacement vide"):
                            style "slot_time"

###############################################################################
## PREFERENCES
###############################################################################

screen preferences():

    tag menu

    add Solid("#FFF7FB")

    frame:
        style "menu_frame"

        xalign .5
        yalign .5

        viewport:
            mousewheel True
            draggable True

            vbox:
                spacing 28

                text _("Préférences") style "menu_title"

                text _("Musique") style "pref_label"
                bar value Preference("music volume")

                text _("Effets") style "pref_label"
                bar value Preference("sound volume")

                text _("Voix") style "pref_label"
                bar value Preference("voice volume")

                null height 15

                text _("Affichage") style "pref_label"

                textbutton _("Fenêtré"):
                    style "pref_button"
                    action Preference("display", "window")

                textbutton _("Plein écran"):
                    style "pref_button"
                    action Preference("display", "fullscreen")

###############################################################################
## HISTORIQUE
###############################################################################

screen history():

    tag menu

    add Solid("#F8FAFC")

    frame:
        style "menu_frame"

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:
                spacing 18

                for h in _history_list:

                    frame:
                        background "#FFFFFFBB"
                        xfill True
                        padding (20,20)

                        vbox:
                            spacing 8

                            if h.who:

                                text h.who:
                                    style "history_name"

                            text h.what:
                                style "history_text"

###############################################################################
## GALERIE
###############################################################################

screen gallery():

    tag menu

    add Solid("#FFF7FB")

    frame:
        style "menu_frame"

        vbox:
            spacing 20

            text _("Galerie") style "menu_title"

            grid 4 3:
                spacing 24

                for i in range(12):

                    button:

                        style "gallery_button"
                        action NullAction()

                        frame:
                            background "#FFFFFF66"
                            xsize 300
                            ysize 170

                        text _("CG [i+1]"):
                            xalign .5
                            yalign .5

###############################################################################
## CONFIRMATION
###############################################################################

screen confirm(message, yes_action, no_action):

    modal True

    add "#0008"

    frame:
        style "confirm_frame"

        xalign .5
        yalign .5

        vbox:
            spacing 25

            text message style "confirm_text"

            hbox:
                spacing 25
                xalign .5

                textbutton _("Oui"):
                    style "pref_button"
                    action yes_action

                textbutton _("Non"):
                    style "pref_button"
                    action no_action

###############################################################################
## STYLES
###############################################################################

style main_menu_button is button:
    background None
    xminimum 520
    yminimum 70
    left_padding 0

style main_menu_button_text is button_text:
    font gui.interface_text_font
    size gui.main_menu_text_size
    idle_color gui.main_menu_text_color
    hover_color gui.main_menu_text_hover_color
    selected_idle_color gui.main_menu_text_selected_color
    outlines [(2, "#243B53", 0, 0)]

style say_window is window:
    background Null()
    xfill True
    ysize gui.textbox_height
    top_padding 55
    bottom_padding 45
    left_padding 110
    right_padding 110

style say_label is default:
    font gui.name_text_font
    size gui.name_text_size
    color gui.name_color

style say_dialogue is default:
    font gui.text_font
    size gui.text_size
    color gui.dialogue_color
    line_spacing 5

style choice_window is frame:
    background "#FFFFFFAA"
    xalign .5
    yalign .78
    padding (35,35)

style choice_button is button:
    background "#FCE7F3"
    hover_background "#60A5FA"
    xsize gui.choice_button_width
    ysize gui.choice_button_height
    xpadding 25
    ypadding 15

style choice_button_text is button_text:
    font gui.interface_text_font
    size gui.choice_button_text_size
    idle_color "#243B53"
    hover_color "#FFFFFF"
    xalign .5

style quick_menu_frame is frame:
    background "#FFFFFF44"
    padding (20,16)

style menu_frame is frame:
    background "#FFFFFFDD"
    padding (45,45)

style menu_title is default:
    font gui.name_text_font
    size 48
    color gui.accent_color

style slot_button is button:
    background "#FFFFFF88"
    hover_background "#FCE7F3"

style slot_time is default:
    size 24
    color "#243B53"

style pref_label is default:
    size 30
    color "#243B53"

style pref_button is button:
    background "#DBEAFE"

style pref_button_text is button_text:
    color "#243B53"
    hover_color "#F472B6"

style history_name is default:
    size 30
    color gui.accent_color

style history_text is default:
    size 28
    color "#243B53"

style gallery_button is button:
    background "#FFFFFF88"
    hover_background "#FCE7F3"

style confirm_frame is frame:
    background "#FFFFFFEE"
    padding (50,50)
    xmaximum 800

style confirm_text is default:
    size 34
    color "#243B53"
    text_align 0.5
    xalign .5