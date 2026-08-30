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

init python:
    def fade_channel(channel, volume, time=2.0):
        renpy.music.set_volume(volume, delay=time, channel=channel)


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
define audio.trainstop = "audio/fx/train-stop.mp3"
define audio.maidcafe = "audio/music/maidCafe.mp3"
define audio.citynight = "audio/music/night-walk.mp3"

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


label arc_6_diplomes:
    scene bg graduation
    with fade
    show jessy determined at char_left
    show ilona neutral at char_right

    systeme "Arc VI - Remise des diplômes : après aujourd'hui."

    menu:
        "Le cadre scolaire disparaît. Quelle question Jessy pose-t-il ?"

        "Tu veux continuer avec moi après l'école ?":
            $ lien_jessy_ilona += 1
            $ jalousie += 1
            j "Tu veux continuer avec moi après l'école ?"
            i "Je veux répondre. Mais j'ai besoin que la question ne soit pas seulement ta peur."

        "Qu'est-ce que tu veux vraiment pour la suite ?":
            $ lien_jessy_ilona += 1
            $ communication += 2
            $ autonomie_ilona += 2
            $ ilona_peut_finir_ses_phrases += 1
            j "Qu'est-ce que tu veux vraiment pour la suite ?"
            i "Je crois que c'est la première fois que la question a assez de place."

        "Éviter la conversation.":
            $ communication -= 2
            $ pression_stream += 1
            systeme "Aucun cri. Juste une phrase qui reste coincée."

        "Partir avant sa réponse.":
            $ communication -= 2
            $ confiance -= 1
            $ influence_theo += 1
            $ pression_stream += 1
            $ interruptions_ilona += 1
            systeme "Ilona ouvre la bouche. Jessy est déjà trop loin pour entendre."

    jump arc_7_randonnee


label arc_7_randonnee:
    scene bg mountain
    with fade
    show sofiane intense at char_center

    systeme "Arc VII - Randonnée : le chemin sans itinéraire."
    systeme "Le bus est annulé. Sofiane sort silencieusement des clés."
    s "La route ne vous a pas abandonnés. Elle vérifie seulement si vous êtes prêts à la suivre."

    show laplage thumb_up at char_right
    laplage "Bonne trajectoire émotionnelle."
    hide laplage

    show allan surprise at char_left
    show alex awkward at char_right
    a "Il avait une voiture d'anime depuis tout ce temps ?"
    x "Je révise mentalement toute notre hiérarchie de mystères."
    hide allan
    hide alex
    hide sofiane

    show jessy listening at char_left
    show ilona fatigue at char_right
    systeme "Sans public, sans réseau et sans échappatoire immédiate, la conversation arrive enfin."

    menu:
        "Comment Jessy choisit-il de parler ?"

        "Nommer sa peur et écouter.":
            $ lien_jessy_ilona += 1
            $ communication += 2
            $ confiance += 2
            $ autonomie_ilona += 1
            $ remember("jessy_nomme_sa_peur")
            j "J'ai peur de te perdre. Mais je veux t'entendre avant de me défendre."

        "Accuser Théo.":
            $ jalousie += 2
            $ communication -= 1
            $ influence_theo += 1
            $ pression_stream += 1
            j "C'est lui qui a mis tout ça entre nous."
            i "Il n'a pas créé tous nos silences."

        "Exiger une réponse immédiate.":
            $ jalousie += 2
            $ autonomie_ilona -= 2
            $ confiance -= 1
            $ influence_theo += 1
            $ pression_stream += 1
            j "J'ai besoin que tu me répondes maintenant."
            i "Moi, j'ai besoin de respirer."

        "Faire semblant que tout va bien.":
            $ communication -= 2
            $ pression_stream += 1
            j "Non, ça va. Tout va bien."
            i "Je crois que c'est exactement ce qui me fatigue."

        "Laisser Ilona finir sans l'interrompre.":
            $ lien_jessy_ilona += 1
            $ communication += 2
            $ autonomie_ilona += 2
            $ confiance += 1
            $ ilona_peut_finir_ses_phrases += 2
            i "Ne réponds pas tout de suite. J'ai besoin de finir."
            j "D'accord. Je t'écoute."

    if interruptions_ilona > interruptions_reconnues:
        jump scene_reparation_interruption

    jump choose_ending


label scene_reparation_interruption:
    show jessy listening at char_left
    show ilona neutral at char_right

    j "L'autre jour, je t'ai coupée. Je crois que j'ai répondu à ma peur au lieu de t'écouter."

    menu:
        "Réparer l'interruption ?"

        "Te laisser reprendre, sans te demander de me rassurer.":
            $ interruptions_reconnues += 1
            $ interruptions_reparees += 1
            $ communication += 1
            $ autonomie_ilona += 1
            $ ilona_peut_finir_ses_phrases += 1
            $ remember("jessy_repare")
            j "Tu peux reprendre, si tu en as encore envie. Et tu n'as pas besoin de faire attention à ma réaction."

        "Expliquer immédiatement pourquoi Jessy avait peur.":
            $ interruptions_reconnues += 1
            j "Je sais que je t'ai coupée, mais tu comprends aussi pourquoi ça m'a fait peur, non ?"
            i "Oui. Mais tu viens encore de déplacer la conversation vers toi."

    jump choose_ending


label choose_ending:
    $ ecoute_reelle = ilona_peut_finir_ses_phrases + interruptions_reparees
    $ controle_repetitif = interruptions_ilona - interruptions_reparees

    if ilonanium_points >= 6:
        jump ending_ilonanium

    if autonomie_ilona >= 5 and communication >= 6 and ecoute_reelle >= 4:
        jump evaluate_ilona_route
    else:
        jump evaluate_separation_route


label evaluate_ilona_route:
    if confiance >= 7 and lien_jessy_ilona >= 8 and souvenirs["jessy_nomme_sa_peur"] and controle_repetitif <= 1:
        jump route_festival_ilona
    else:
        jump ending_jessy_ilona


label route_festival_ilona:
    scene bg festival
    with fade
    show jessy smile at char_left
    show ilona smile at char_right

    systeme "Route Ilona - Festival d'été : les lanternes ne choisissent pas."
    systeme "Il ne s'agit pas d'une relation sans erreur, mais d'une relation où les erreurs ne prennent pas toute la place."

    menu:
        "Conclusion du festival."

        "Faire une promesse immense, mais reconnaître l'incertitude.":
            $ lien_jessy_ilona += 1
            $ confiance += 1
            j "Je ne sais pas tout ce qu'on deviendra. Je sais juste que je veux continuer à construire sans t'enfermer."

        "Dire simplement : je veux continuer avec toi.":
            $ communication += 1
            j "Je veux continuer avec toi."

        "Rater une déclaration parfaite et l'accepter.":
            $ lien_jessy_ilona += 1
            j "J'avais préparé une phrase. Elle était trop longue et probablement illégale."
            i "Celle-là est mieux."

        "Prendre sa main avec réciprocité visible.":
            $ confiance += 1
            systeme "Ilona serre la main de Jessy avant qu'il ait besoin de demander une preuve."

    if lien_jessy_ilona >= 10 and confiance >= 9 and communication >= 8 and souvenirs["jessy_repare"] and souvenirs["maison_respectee"] and interruptions_reparees >= 1 and controle_repetitif <= 0:
        jump ending_family
    else:
        jump ending_jessy_ilona


label evaluate_separation_route:
    if influence_theo >= 6 and pression_stream >= 6:
        jump ending_theo_vtuber
    elif confidences_laplage >= 3 and influence_theo <= 3:
        jump ending_monsieur_laplage
    else:
        jump ending_no_contact


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
