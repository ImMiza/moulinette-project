# screens.rpy - moulinette UI v1.0

init offset = -1

transform menu_hover:
    on idle:
        zoom 1.0
    on hover:
        ease .15 zoom 1.04

screen main_menu():
    tag menu

    add gui.main_menu_background

    if gui.main_menu_logo:
        add gui.main_menu_logo:
            xpos 90
            ypos 70

    frame:
        background None
        xalign 0.08
        yalign 0.58

        vbox:
            spacing 22

            textbutton _("Nouvelle partie") action Start() style "main_menu_button" at menu_hover
            textbutton _("Continuer") action ShowMenu("load") style "main_menu_button" at menu_hover
            textbutton _("Charger") action ShowMenu("load") style "main_menu_button" at menu_hover
            textbutton _("Galerie") action ShowMenu("gallery") style "main_menu_button" at menu_hover
            textbutton _("Paramètres") action ShowMenu("preferences") style "main_menu_button" at menu_hover
            textbutton _("Quitter") action Quit(confirm=True) style "main_menu_button" at menu_hover

screen say(who, what):

    window:
        style "say_window"

        if who is not None:
            frame:
                style "namebox"

                text who id "who"

        text what id "what"

screen choice(items):
    modal True

    window:
        style "choice_window"

        vbox:
            spacing 18

            for i in items:
                textbutton i.caption action i.action style "choice_button"

screen quick_menu():

    zorder 100

    if quick_menu:

        frame:
            style "quick_menu_frame"

            xalign .5
            yalign 1.0

            hbox:
                spacing 30

                textbutton _("Retour") action Rollback()
                textbutton _("Historique") action ShowMenu("history")
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Skip") action Skip()
                textbutton _("Sauver") action ShowMenu("save")
                textbutton _("Menu") action ShowMenu("preferences")

screen save():
    tag menu
    add gui.main_menu_background
    use file_slots(_("Sauvegarder"))

screen load():
    tag menu
    add gui.main_menu_background
    use file_slots(_("Charger"))

screen file_slots(title):

    frame:
        style "menu_frame"

        vbox:
            spacing 25

            text title style "menu_title"

            grid gui.file_slot_cols gui.file_slot_rows:
                spacing 30

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    button:
                        style "slot_button"
                        action FileSave(i + 1)

                        has vbox

                        add gui.slot_idle_background

                        text FileTime(i + 1, empty="Vide") style "slot_time"

screen preferences():
    tag menu

    add gui.main_menu_background

    frame:
        style "menu_frame"

        vbox:
            spacing 30

            text _("Préférences") style "menu_title"

            text _("Musique")
            bar value Preference("music volume")

            text _("Ambiance")
            bar value Preference("sound volume")

            text _("Effets")
            bar value Preference("voice volume")

            null height 20

            textbutton _("Plein écran") action Preference("display", "fullscreen")
            textbutton _("Fenêtré") action Preference("display", "window")

screen history():

    tag menu
    add gui.main_menu_background

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
                        background "#FFFFFF80"
                        xfill True

                        vbox:
                            spacing 6

                            if h.who:
                                text h.who style "history_name"

                            text h.what style "history_text"

screen gallery():

    tag menu
    add gui.main_menu_background

    frame:
        style "menu_frame"

        vbox:
            spacing 25

            text _("Galerie") style "menu_title"

            grid 4 3:
                spacing 25

                for i in range(12):

                    button:
                        background "#FFFFFF40"
                        xysize gui.gallery_thumb_size
                        action NullAction()

                        text _("CG [i+1]")

screen confirm(message, yes_action, no_action):
    modal True

    add "#00000088"

    frame:
        style "confirm_frame"

        xalign .5
        yalign .5

        vbox:
            spacing 25

            text message style "confirm_text"

            hbox:
                spacing 30
                xalign .5

                textbutton _("Oui") action yes_action
                textbutton _("Non") action no_action

style main_menu_button is button:
    background None
    xminimum 520
    yminimum 72

style main_menu_button_text is button_text:
    font gui.interface_text_font
    size gui.main_menu_text_size
    color gui.main_menu_text_color
    hover_color gui.main_menu_text_hover_color
    selected_color gui.main_menu_text_selected_color
    outlines [(2, "#1E3A8A", 0, 0)]

style say_window:
    background gui.textbox
    xfill True
    ysize gui.textbox_height
    yalign gui.textbox_yalign
    left_padding 120
    right_padding 120
    top_padding 60
    bottom_padding 50

style namebox:
    background gui.namebox
    padding (25, 12)

style say_label:
    font gui.name_text_font
    size gui.name_text_size
    color gui.name_color

style say_dialogue:
    font gui.text_font
    size gui.text_size
    color gui.dialogue_color
    line_spacing 5

style choice_window:
    background None
    xalign .5
    yalign .75

style choice_button is button:
    background gui.choice_button_idle_background
    hover_background gui.choice_button_hover_background
    xsize gui.choice_button_width
    ysize gui.choice_button_height

style choice_button_text is button_text:
    font gui.interface_text_font
    size gui.choice_button_text_size
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    xalign .5
    yalign .5

style menu_frame:
    background "#FFFFFF55"
    xalign .5
    yalign .5
    padding (50, 50)

style menu_title:
    font gui.name_text_font
    size 48
    color gui.accent_color

style slot_button:
    background gui.slot_idle_background
    hover_background gui.slot_hover_background
    xysize (gui.slot_button_width, gui.slot_button_height)

style slot_time:
    size 24
    color gui.text_color

style quick_menu_frame:
    background "#FFFFFF33"
    padding (25, 18)

style history_name:
    color gui.accent_color
    size 30

style history_text:
    color gui.text_color
    size 28

style confirm_frame:
    background "#FFFFFFEE"
    padding (60, 50)
    xmaximum 900

style confirm_text:
    size 34
    color gui.text_color
