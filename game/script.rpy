# Base narrative pour "moulinette".
# Source: game/agents/projet moulinette scenario.pdf + flow scenario.pdf


init -10 python:
    def speaker_callback(tag):
        def callback(event, interact=True, **kwargs):
            if event == "begin" and interact:
                store.current_speaker = tag or ""
        return callback

    def speaker_sprite(tag, path, width=None, height=None):
        if width is not None and height is not None:
            base = im.Scale(path, width, height)
        else:
            base = path

        return ConditionSwitch(
            "current_speaker == '' or current_speaker == '{}'".format(tag), base,
            "True", Transform(base, alpha=0.45)
        )


define j = Character("Jessy", color="#8fb7ff", callback=speaker_callback("jessy"))
define i = Character("Ilona", color="#ffb0d0", callback=speaker_callback("ilona"))
define t = Character("Théo", color="#c8b6ff", callback=speaker_callback("theo"))
define a = Character("Allan", color="#ffd08a", callback=speaker_callback("allan"))
define x = Character("Alexandre", color="#b9f2c8", callback=speaker_callback("alex"))
define s = Character("Sofiane", color="#d6d6d6", callback=speaker_callback("sofiane"))
define laplage = Character("Monsieur Laplage", color="#f6e38d", callback=speaker_callback("laplage"))
define systeme = Character(None, what_italic=True, callback=speaker_callback(""))

define m_inconnu = Character("???", color="#f6e38d", callback=speaker_callback("laplage"))


image bg minecraft = Solid("#18241d")
image bg prologue house afternoon = im.Scale("images/scenes/prologue/bg_prologue_house_afternoon.png", 1920, 1080)
image bg prologue house entrance = im.Scale("images/scenes/prologue/bg_prologue_house_entrance.png", 1920, 1080)
image bg prologue weird interior = im.Scale("images/scenes/prologue/bg_prologue_weird_interior.png", 1920, 1080)
image bg prologue accident floor = im.Scale("images/scenes/prologue/bg_prologue_accident_floor.png", 1920, 1080)
image bg prologue greenhouse branch = im.Scale("images/scenes/prologue/bg_prologue_greenhouse_branch.jpg", 1920, 1080)
image bg prologue pool branch = im.Scale("images/scenes/prologue/bg_prologue_pool_branch.png", 1920, 1080)
image bg prologue slide branch = im.Scale("images/scenes/prologue/bg_prologue_slide_branch.png", 1920, 1080)
image bg prologue chicken roof branch = im.Scale("images/scenes/prologue/bg_prologue_chicken_roof_branch.png", 1920, 1080)
image bg prologue secret room = im.Scale("images/scenes/prologue/bg_prologue_secret_room.png", 1920, 1080)
image bg prologue roof night = im.Scale("images/scenes/prologue/bg_prologue_roof_night.png", 1920, 1080)
image bg prologue river laplage = im.Scale("images/scenes/prologue/bg_prologue_river_laplage.png", 1920, 1080)
image bg school = Solid("#1b2330")
image bg beach = Solid("#24445b")
image bg festival = Solid("#2b1b32")
image bg winter = Solid("#263142")
image bg library = Solid("#20202a")
image bg graduation = Solid("#25242b")
image bg mountain = Solid("#1d2c28")
image bg stream = Solid("#15151f")
image bg ending = Solid("#111217")
image bg shared school corridor = im.Scale("images/scenes/shared/bg_shared_school_corridor.jpg", 1920, 1080)
image bg shared train inside = im.Scale("images/scenes/shared/bg_shared_train_inside.jpg", 1920, 1080)


image jessy minecraft = speaker_sprite("jessy", "images/personnages/Jessy/minecraft.png")
image jessy embarrassed = speaker_sprite("jessy", "images/personnages/Jessy/nervous_embarrassment.png")
image jessy neutral = speaker_sprite("jessy", "images/personnages/Jessy/neutral_attentiveness.png")
image jessy listening = speaker_sprite("jessy", "images/personnages/Jessy/regretful_listening.png")
image jessy smile = speaker_sprite("jessy", "images/personnages/Jessy/shy_warm_smile.png")
image jessy determined = speaker_sprite("jessy", "images/personnages/Jessy/vulnerable_determination.png")

image ilona minecraft = speaker_sprite("ilona", "images/personnages/Ilona/minecraft.png")
image ilona embarrassed = speaker_sprite("ilona", "images/personnages/Ilona/awkward_embarrassment.png")
image ilona determined = speaker_sprite("ilona", "images/personnages/Ilona/clear_determination.png")
image ilona frustrated = speaker_sprite("ilona", "images/personnages/Ilona/frustrated_restraint.png")
image ilona neutral = speaker_sprite("ilona", "images/personnages/Ilona/neutral.png")
image ilona smile = speaker_sprite("ilona", "images/personnages/Ilona/playful_warm_smile.png")
image ilona fatigue = speaker_sprite("ilona", "images/personnages/Ilona/quiet_fatigue.png")

image theo disappointed = speaker_sprite("theo", "images/personnages/Théo/cold_disappointment.png", 842, 1264)
image theo annoyed = speaker_sprite("theo", "images/personnages/Théo/controlled_annoyance.png", 842, 1264)
image theo defensive = speaker_sprite("theo", "images/personnages/Théo/defense_frustration.png", 842, 1264)
image theo innocent = speaker_sprite("theo", "images/personnages/Théo/feigned_innocence.png", 842, 1264)
image theo smirk = speaker_sprite("theo", "images/personnages/Théo/knowing_smirk.png", 842, 1264)
image theo neutral = speaker_sprite("theo", "images/personnages/Théo/neutral.png", 842, 1264)
image theo jealousy = speaker_sprite("theo", "images/personnages/Théo/quiet_jalousy.png", 842, 1264)
image theo reassuring = speaker_sprite("theo", "images/personnages/Théo/reassuring_smile.png", 842, 1264)

image allan embarrassed = speaker_sprite("allan", "images/personnages/Allan/awkward_embarrassment.png")
image allan excited = speaker_sprite("allan", "images/personnages/Allan/cheerful_excitement.png")
image allan neutral = speaker_sprite("allan", "images/personnages/Allan/neutral.png")
image allan smirk = speaker_sprite("allan", "images/personnages/Allan/playful_smirk.png")
image allan support = speaker_sprite("allan", "images/personnages/Allan/quiet_support.png")
image allan doubt = speaker_sprite("allan", "images/personnages/Allan/throughtful_doubt.png")
image allan silence = speaker_sprite("allan", "images/personnages/Allan/uncomfortable_silence.png")
image allan surprise = speaker_sprite("allan", "images/personnages/Allan/wide_eye_surprise.png")

image alex awkward = speaker_sprite("alex", "images/personnages/Alexandre/akward_realization.png")
image alex serious = speaker_sprite("alex", "images/personnages/Alexandre/blunt_seriousness.png")
image alex concerned = speaker_sprite("alex", "images/personnages/Alexandre/concerned_look.png")
image alex laugh = speaker_sprite("alex", "images/personnages/Alexandre/genuine_laughter.png")
image alex minecraft = speaker_sprite("alex", "images/personnages/Alexandre/minecraft.png")
image alex neutral = speaker_sprite("alex", "images/personnages/Alexandre/neutral.png")
image alex grin = speaker_sprite("alex", "images/personnages/Alexandre/playful_grin.png")
image alex support = speaker_sprite("alex", "images/personnages/Alexandre/supportive_encouragement.png")
image alex teasing = speaker_sprite("alex", "images/personnages/Alexandre/teasing_skepticism.png")

image sofiane awkward = speaker_sprite("sofiane", "images/personnages/Sofiane/akward_silence.png")
image sofiane smirk = speaker_sprite("sofiane", "images/personnages/Sofiane/cryptic_smirk.png")
image sofiane intense = speaker_sprite("sofiane", "images/personnages/Sofiane/dramatic_intensity.png")
image sofiane maid = speaker_sprite("sofiane", "images/personnages/Sofiane/maid.png")
image sofiane observation = speaker_sprite("sofiane", "images/personnages/Sofiane/quiet_observation.png")
image sofiane smile = speaker_sprite("sofiane", "images/personnages/Sofiane/relieved_smile.png")
image sofiane neutral = speaker_sprite("sofiane", "images/personnages/Sofiane/reserved_neutral.png")
image sofiane shy = speaker_sprite("sofiane", "images/personnages/Sofiane/shy_embarrassment.png")

image laplage neutral = speaker_sprite("laplage", "images/personnages/laplage/neutral.png")
image laplage thumb_up = speaker_sprite("laplage", "images/personnages/laplage/thumb_up.png")
image laplage thumb_horizontal = speaker_sprite("laplage", "images/personnages/laplage/thumb_horizontal.png")
image laplage minecraft = speaker_sprite("laplage", "images/personnages/laplage/minecraft.png")

init python:
    renpy.music.register_channel("ambiant1", mixer="sfx", loop=True)


define audio.ecole = "audio/music/ecole-music.mp3"
define audio.mcnight = "audio/music/Subwoofer-Lullaby.mp3"
define audio.ecoleroof = "audio/music/ecole-roof.ogg"
define audio.ecolenight = "audio/music/ecole-nuit.mp3"
define audio.windBirds = "audio/ambience/breeze-birds.mp3"
define audio.trainInside = "audio/ambience/tram-inside.mp3"
define audio.eating = "audio/fx/aaughmp3.mp3"
define audio.sadPiano = "audio/music/sad-piano.mp3"
define audio.melanPiano = "audio/music/melancolique-piano.mp3"
define audio.tensePiano = "audio/music/tense-piano.mp3"
define audio.mornPiano = "audio/music/morning-piano.mp3"
define audio.foule = "audio/ambience/crowd-noise.mp3"

transform char_left:
    xalign 0.18
    yalign 1.0
    zoom 0.50

transform char_midleft:
    xalign 0.34
    yalign 1.0
    zoom 0.50

transform char_center:
    xalign 0.50
    yalign 1.0
    zoom 0.50

transform char_midright:
    xalign 0.66
    yalign 1.0
    zoom 0.50

transform char_right:
    xalign 0.82
    yalign 1.0
    zoom 0.50


default lien_jessy_ilona = 0
default current_speaker = ""
default confiance = 0
default communication = 0
default jalousie = 0
default autonomie_ilona = 0
default lien_ilona_theo = 0
default influence_theo = 0
default pression_stream = 0
default jugement_laplage = 0
default confidences_laplage = 0
default ilonanium_points = 0

default interruptions_ilona = 0
default interruptions_reconnues = 0
default interruptions_reparees = 0
default ilona_peut_finir_ses_phrases = 0

# Compteurs de recidive : incrementes par les choix de tier C (evitement)
# et de tier D (controle). Lus uniquement par la porte de l'arc 6.
default evitements = 0
default controles = 0

# Tracker état maison Minecraft pour cohérence arcs futurs
default maison_minecraft_destructions = []
default maison_minecraft_ajouts = []

default souvenirs = {
    "ilona_libre_sans_abandon": False,
    "jessy_nomme_sa_peur": False,
    "jessy_repare": False,
    "theo_utilise_une_verite": False,
    "ilona_pose_une_limite": False,
    "maison_respectee": False,
    "ilona_veut_streamer_serieusement": False,
}

default endings_seen = []
default derniere_route = ""

# Etat central du prologue, utilise ensuite comme memoire relationnelle.
default prologue_reaction = ""
default maison_minecraft_detail = ""
default maison_minecraft_transformation = ""
default prologue_appel_discord = ""


init python:
    def remember(key):
        store.souvenirs[key] = True

    def record_ending(key):
        if key not in store.endings_seen:
            store.endings_seen.append(key)


label start:
    scene bg minecraft
    with fade

    systeme "Une année scolaire, une maison Minecraft beaucoup trop grande, et des choix qui ne classent personne en bon ou mauvais."
    systeme "La base actuelle pose les arcs, les variables et les embranchements majeurs. Les scènes pourront ensuite être enrichies dialogue par dialogue."

    jump prologue_minecraft

# Arc IV complet : arcs/arc_4/arc_4_noel.rpy
# Arc V complet : arcs/arc_5/arc_5_examens.rpy


# =============================================================================
# ARC VI - REMISE DES DIPLOMES
# Le contenu complet est dans arcs/arc_6/arc_6_diplomes.rpy
# (labels arc_6_diplomes, arc_6_calcul, arc_6_debug_score)
# =============================================================================

# Seuils du turning point de l'arc 6.
# Calibres empiriquement sur le code reel (38 menus, prologue -> arc 6).
# Reperes de mesure :
#   score max theorique  572   (que du tier S, lien 18)
#   run "premiere option" 246  (lien 46)
#   run "derniere option" -395
#   parties aleatoires    mediane -104, p95 92
# Frontiere score/lien : environ -7 points de score par point de lien gagne
# (le tier B ne donne que du lien). La fenetre romance est lien 35..64.
define SEUIL_JESSY = 180     # sous ce score -> arc_7_theo
define SEUIL_ROMANCE = 320   # au-dessus -> option romance debloquee en arc 7
define SEUIL_LIEN = 35       # complicite minimale requise pour la romance


# =============================================================================
# ARC VII - DEUX ARCS DISTINCTS
# La bascule est calculee en fin d'arc 6 (label arc_6_calcul).
#
#   arc_7_jessy = Ilona reste dans un endroit ou elle peut parler.
#   arc_7_theo  = Ilona part vers un endroit ou on lui epargne de parler.
#
# TODO : ces deux labels sont des SQUELETTES. Ils portent la logique de
# routage definitive vers les fins, mais pas encore le contenu narratif
# (festival d'ete + sequence AE86 pour la route Jessy, "le monde apres la
# maison" en POV alterne pour la route Theo).
# =============================================================================

label arc_7_jessy:
    $ derniere_route = "Route Jessy"

    scene bg festival
    with fade
    show jessy smile at char_left
    show ilona smile at char_right

    systeme "Arc VII - Festival d'ete : les lanternes ne choisissent pas."
    systeme "Ilona a choisi un endroit ou elle peut parler. Ce n'est pas une victoire de Jessy. C'est une place qu'elle a prise."

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


label arc_7_theo:
    $ derniere_route = "Route Theo"

    scene bg stream
    with fade
    show jessy listening at char_center

    systeme "Arc VII - Le monde apres la maison."
    systeme "Ilona n'a pas choisi Theo. Elle est partie vers l'endroit ou on lui epargnait de parler. Ce n'est pas la meme chose, et c'est pire."

    menu:
        "Ce qui se passe apres le depart."

        "Ilona s'extrait elle-meme." if confidences_laplage >= 3 and influence_theo <= 6:
            jump ending_monsieur_laplage

        "La dette se referme.":
            jump ending_theo_vtuber


label ending_family:
    scene bg ending
    with fade
    $ record_ending("family")
    $ derniere_route = "Ils ont bien grandi, les petits"

    systeme "Fin 1 - Ils ont bien grandi, les petits."
    show laplage neutral at char_center
    laplage "Le temps passe comme les vagues. Certaines emportent les châteaux de sable. D'autres apprennent aux enfants à en construire de nouveaux."
    show laplage thumb_up at char_center
    laplage "Ils ont bien grandi, les petits."
    jump post_generique


label ending_jessy_ilona:
    scene bg ending
    with fade
    $ record_ending("jessy_ilona")
    $ derniere_route = "Juste Jessy et Ilona"

    systeme "Fin 2 - Juste Jessy et Ilona."
    i "On pourrait réparer cette pièce maintenant."
    j "Non. C'est là que tout a commencé."
    jump post_generique


label ending_no_contact:
    scene bg stream
    with fade
    $ record_ending("no_contact")
    $ derniere_route = "La maison silencieuse"

    systeme "Fin 3 - La maison silencieuse."
    systeme "Jessy se connecte à leur ancien monde. La maison est vide, mais elle n'a jamais été fausse."
    x "Je suis là si tu veux juste jouer sans parler."
    jump post_generique


label ending_monsieur_laplage:
    scene bg beach
    with fade
    $ record_ending("laplage")
    $ derniere_route = "La plage ne répond plus"

    show laplage neutral at char_left
    systeme "Fin 4 - La plage ne répond plus."
    i "C'est la première fois depuis longtemps que personne ne me demande de choisir vite."
    show laplage thumb_up at char_left
    laplage "Ne détruis pas ce qui t'a appris à construire."
    jump post_generique


label ending_theo_vtuber:
    scene bg stream
    with fade
    $ record_ending("theo_vtuber")
    $ derniere_route = "La route de Théo"

    systeme "Fin 5 - La route de Théo."
    t "Je ne t'empêche pas de choisir. Je t'aide à ne pas gâcher ce que tu as construit."
    show laplage neutral at char_center
    laplage "Quand quelqu'un te promet le monde, regarde d'abord s'il ne t'enlève pas le ciel."
    systeme "Pouce baissé, lentement."
    jump post_generique


label ending_ilonanium:
    scene bg ending
    with fade
    $ record_ending("ilonanium")
    $ derniere_route = "L'Ilonanium"

    systeme "Fin 6 - Easter egg : L'Ilonanium."
    i "Non. J'ai juste fini ce qu'il restait."
    show laplage thumb_up at char_center
    laplage "Laisser digérer."
    jump post_generique


label post_generique:
    scene bg beach
    with fade

    systeme "Post-générique - Le prochain, c'est toi."
    show laplage neutral at char_left
    show theo disappointed at char_right
    t "Pourquoi moi ? Après tout ce que j'ai fait..."
    laplage "Comprendre quelqu'un ne te donne pas le droit de choisir pour lui."
    show laplage thumb_up at char_left
    laplage "Le prochain choix sera le tien."
    systeme "Écran noir. À suivre... peut-être."

    return
