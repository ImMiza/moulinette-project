# SPECIAL ENDING - ILONANIUM
# Source : agents/illonanium/Fin ilonanium.md. Quatorze scènes, puis générique.
# Le fruit est déjà mangé à l'arc 7 ; les symptômes arrivent après le retour.

init -5 python:
    def ilonanium_asset(chemin, secours):
        # ponytail: secours jusqu'à livraison des décors et pistes dédiés ci-dessous.
        return chemin if renpy.loadable(chemin) else secours

# Le depart de randonnee montre le quartier residentiel, avant le sentier.
image bg ilonanium rue = Transform("images/scenes/backgrounds/hiking/bg_arc7_jessy_depart.jpg", xysize=(1920, 1080), fit="cover")
# Meme chambre que les premiers CG : bureau a gauche, lit a droite.
image bg ilonanium chambre = Transform("images/scenes/backgrounds/friend/bg_friend_chambre_ilona.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium astre = Transform("images/scenes/cg/ilonanium/12_ilonanium.png", xysize=(1920, 1080), fit="cover")
# Plage sauvage a deux soleils, avant la reconstruction de la civilisation.
image bg ilonanium plage = Transform("images/scenes/backgrounds/ilonanium/plage_deux_soleils.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium plage reconstruite = Transform("images/scenes/illonanium/plage_exoplanete.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium exoplanete = Transform("images/scenes/illonanium/plage_exoplanete.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium bar = Transform("images/scenes/illonanium/bar.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium conseil = Transform("images/scenes/illonanium/governor_office.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium capitole = Transform("images/scenes/illonanium/capitole_depart.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium retour = Transform("images/scenes/illonanium/capitole_retour.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium taikun = Transform("images/scenes/illonanium/taikun_orbite.png", xysize=(1920, 1080), fit="cover")
# Le TAIKUN devant l'Ilonanium est reserve a l'arrivee, apres le voyage spatial.
image bg ilonanium reconquete = Transform("images/scenes/illonanium/fin_ilonanium0.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium passerelle = Transform("images/scenes/illonanium/passerelle_taikun.png", xysize=(1920, 1080), fit="cover")
image bg ilonanium maison alex = Transform("images/scenes/illonanium/fin_ilonanium1.jpg", xysize=(1920, 1080), fit="cover")
# CG 1920 x 1080 affiche directement a sa taille native, sans transformation.
image bg ilonanium alex = "images/scenes/illonanium/fin_ilonanium2.jpg"

# Transformation : personnages deja peints dans les CG, sans sprites superposes.
# Le douzieme plan est aussi le decor « bg ilonanium astre », repris a la reconquete.
image cg ilonanium attraction = Transform("images/scenes/cg/ilonanium/01_attraction.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium gravite = Transform("images/scenes/cg/ilonanium/02_gravite.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium laplage = Transform("images/scenes/cg/ilonanium/03_laplage.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium echec = Transform("images/scenes/cg/ilonanium/04_echec.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium adieu = Transform("images/scenes/cg/ilonanium/05_adieu.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium maison = Transform("images/scenes/cg/ilonanium/06_maison.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium arrachement = Transform("images/scenes/cg/ilonanium/07_arrachement.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium catastrophe = Transform("images/scenes/cg/ilonanium/08_catastrophe.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium sauvetage = Transform("images/scenes/cg/ilonanium/09_sauvetage.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium terre = Transform("images/scenes/cg/ilonanium/10_terre.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium naissance astre = Transform("images/scenes/cg/ilonanium/11_naissance_astre.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium reconquete espoir = Transform("images/scenes/cg/ilonanium/13_reconquete_espoir.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium transmission = Transform("images/scenes/cg/ilonanium/14_transmission_adieux.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium depart tardis = Transform("images/scenes/cg/ilonanium/15_depart_tardis.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium survivants = Transform("images/scenes/cg/ilonanium/16_jessy_survivants.png", xysize=(1920, 1080), fit="cover")

# Adieux : personnages peints dans les CG, sans sprites superposes.
image cg ilonanium adieux laplage = Transform("images/scenes/cg/ilonanium/13_adieux_laplage.png", xysize=(1920, 1080), fit="cover")
image cg ilonanium calin = Transform("images/scenes/cg/ilonanium/14_calin_jessy_theo.png", xysize=(1920, 1080), fit="cover")

# Retirer les marges transparentes du PNG, en conservant tout le tirage papier.
image ilonanium_photo = Transform("images/scenes/cg/ilonanium/theo_ilona_picture.png", crop=(18, 314, 811, 919), ysize=620, fit="contain")

# Photo lancee depuis Laplage, puis posee de biais au centre, au-dessus du texte.
transform ilonanium_photo_lancer:
    subpixel True
    anchor (0.5, 0.5)
    pos (1.12, 0.16)
    zoom 0.72
    rotate 24
    alpha 0.0
    parallel:
        linear 0.12 alpha 1.0
    parallel:
        easeout 0.55 pos (0.5, 0.40) zoom 1.03 rotate -7
        ease 0.15 zoom 1.0 rotate -3

# Vue plongeante du conseil : les six personnages sont integres au CG.
image cg ilonanium preparatifs = "images/scenes/cg/ilonanium/15_preparatifs_taikun.png"

# Ancrages identiques pour tous les canevas harmonises de cet ending.
transform ilonanium_left:
    xpos 0.25
    xanchor 0.5
    yalign 1.0
    zoom 0.50

transform ilonanium_center:
    xpos 0.50
    xanchor 0.5
    yalign 1.0
    zoom 0.50

transform ilonanium_right:
    xpos 0.75
    xanchor 0.5
    yalign 1.0
    zoom 0.50

# Sepia progressif sur le dernier plan, sans affecter le carton ni le generique.
transform ilonanium_jojo_sepia:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    ease 0.9 matrixcolor TintMatrix("#ffe3ad") * SaturationMatrix(0.0)

# Carton JoJo : arrive par la droite et se pose en bas a gauche du dernier plan.
transform ilonanium_to_be_continued_slide:
    subpixel True
    xpos 1.0
    xanchor 0.0
    ypos 0.92
    yanchor 1.0
    easeout 0.6 xpos 0.04

screen ilonanium_to_be_continued():
    zorder 200
    fixed at ilonanium_to_be_continued_slide:
        xysize (780, 112)
        add "images/ui/ilonanium_to_be_continued.svg"
        text "TO BE CONTINUED":
            xpos 117
            yalign 0.5
            font "DejaVuSans.ttf"
            size 48
            bold True
            italic True
            color "#f6e7c9"
            outlines [(2, "#171311", 0, 0)]

define ilonanium_florentin = Character("Florentin", color="#cf8671", callback=speaker_callback("florentin"))

# Canevas communs 1280 x 1280 ; proportions et cadrage fixes par tenue.
# Le rognage bas de Theo est deja applique dans les PNG harmonises.
image ilona ilonanium sick = speaker_sprite("ilona", "images/personnages/Ilona/illonanium/sick.png")

image laplage ilonanium exhausted = speaker_sprite("laplage", "images/personnages/Laplage/illonanium/exhausted.png")
image laplage ilonanium farewell = speaker_sprite("laplage", "images/personnages/Laplage/illonanium/farewell.png")
# Apres la transmission : meme echelle que le canevas d'origine, sans porte-cles.
image laplage ilonanium farewell_no_creeper = speaker_sprite("laplage", "images/personnages/Laplage/illonanium/farewell_no_creeper.png", 1280, 1280)
image laplage ilonanium neutral = speaker_sprite("laplage", "images/personnages/Laplage/illonanium/neutral.png")
image laplage ilonanium thumb_up = speaker_sprite("laplage", "images/personnages/Laplage/illonanium/thumb_up.png")

image allan ilonanium ceo = speaker_sprite("allan", "images/personnages/Allan/illonanium/ceo.png")
image allan ilonanium ceo_surprised = speaker_sprite("allan", "images/personnages/Allan/illonanium/ceo_surprised.png")
image allan ilonanium ceo_supportive = speaker_sprite("allan", "images/personnages/Allan/illonanium/ceo_supportive.png")
image allan ilonanium commander = speaker_sprite("allan", "images/personnages/Allan/illonanium/military_commander.png")

image micka ilonanium governor = speaker_sprite("micka", "images/personnages/Micka/illonanium/governor_suit.png")
image micka ilonanium governor_serious = speaker_sprite("micka", "images/personnages/Micka/illonanium/governor_serious.png")
image micka ilonanium governor_emotional = speaker_sprite("micka", "images/personnages/Micka/illonanium/governor_emotional.png")
image micka ilonanium armor = speaker_sprite("micka", "images/personnages/Micka/illonanium/sci_fi_armor.png")
image micka ilonanium armor_commanding = speaker_sprite("micka", "images/personnages/Micka/illonanium/armor_commanding.png")

image jessy ilonanium priest = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/priest.png")
image jessy ilonanium priest_listening = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/priest_listening.png")
image jessy ilonanium priest_determined = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/priest_determined.png")
image jessy ilonanium priest_emotional = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/priest_emotional.png")
image jessy ilonanium priest_smile = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/priest_smile.png")
image jessy ilonanium prophet = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/prophet_with_gem.png")
image jessy ilonanium prophet_emotional = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/prophet_emotional.png")
image jessy ilonanium prophet_determined = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/prophet_determined.png")
image jessy ilonanium beach_neutral = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/beach_neutral.png")
image jessy ilonanium beach_angry = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/beach_angry.png")
image jessy ilonanium beach_determined = speaker_sprite("jessy", "images/personnages/Jessy/illonanium/beach_determined.png")

image sofiane ilonanium civilian_neutral = speaker_sprite("sofiane", "images/personnages/Sofiane/illonanium/older_civilian_neutral.png")
image sofiane ilonanium civilian_smirk = speaker_sprite("sofiane", "images/personnages/Sofiane/illonanium/older_civilian_smirk.png")
image sofiane ilonanium armor = speaker_sprite("sofiane", "images/personnages/Sofiane/illonanium/tactical_sci_fi_armor.png")
image sofiane ilonanium armor_focused = speaker_sprite("sofiane", "images/personnages/Sofiane/illonanium/armor_focused.png")

image florentin ilonanium armor = speaker_sprite("florentin", "images/personnages/Florentin/illonanium/futuristic_armor.png")
image florentin ilonanium armor_angry = speaker_sprite("florentin", "images/personnages/Florentin/illonanium/armor_angry.png")
image florentin ilonanium armor_resolved = speaker_sprite("florentin", "images/personnages/Florentin/illonanium/armor_resolved.png")

image theo ilonanium older = speaker_sprite("theo", "images/personnages/Theo/illonanium/older_neutral.png")
image theo ilonanium older_regretful = speaker_sprite("theo", "images/personnages/Theo/illonanium/older_regretful.png")
image theo ilonanium older_surprised = speaker_sprite("theo", "images/personnages/Theo/illonanium/older_surprised.png")
image theo ilonanium laplage = speaker_sprite("theo", "images/personnages/Theo/illonanium/laplage_neutral.png")
image theo ilonanium laplage_determined = speaker_sprite("theo", "images/personnages/Theo/illonanium/laplage_determined.png")
image theo ilonanium laplage_emotional = speaker_sprite("theo", "images/personnages/Theo/illonanium/laplage_emotional.png")
image theo ilonanium thumb_up = speaker_sprite("theo", "images/personnages/Theo/illonanium/laplage_thumb_up.png")

# 1. LE LENDEMAIN — CA DOIT ETRE LA RANDONNEE
label ending_ilonanium:
    $ record_ending("ilonanium")
    $ ilonanium_silence(0.0)
    stop ambiant1 fadeout 1.0
    stop sound
    stop music fadeout 1.0
    scene black with fade
    centered "LE LENDEMAIN DU RETOUR"
    scene bg friend chambre jessy with fade
    $ ilonanium_music("home", level=0.70, fadein=2.0)
    show jessy ilonanium beach_neutral at ilonanium_left with dissolve

    systeme "Le sac de randonnée est encore contre le bureau. Une chaussure sèche mieux que l'autre. Sur l'écran de Jessy, leur maison Minecraft attend ses habitants."
    $ ilonanium_effect("phone", level=0.75, channel="ilon_detail")
    systeme "Son téléphone vibre. Un message d'Ilona."
    i "Je vais pas jouer ce soir. Je suis malade."
    j "Malade comment ?"
    i "Mal au ventre. Nausée. Et j'ai l'impression d'avoir encore toute la montagne dans les jambes."
    j "Tu veux que je t'apporte quelque chose ?"
    i "Non, merci. J'ai de l'eau et de quoi manger. Je vais dormir un peu."
    if arc7_jessy_relation == "amour":
        j "Premier rendez-vous après la randonnée : annulé pour cause de mollets."
        i "Mes mollets présentent leurs excuses. Moi aussi."
        j "Repose-toi. On a le temps."
    else:
        i "Et c'est pas une excuse pour éviter de te parler. Je suis vraiment malade."
        j "T'as pas besoin de te justifier. Repose-toi."
    $ ilonanium_music_level(0.48, 2.0)
    i "C'est bizarre. J'ai mangé deux fois et j'ai toujours faim. Mais rien passe."
    j "On a peut-être abusé des biscuits d'Allan."
    i "Accuse pas les biscuits sans preuve."
    systeme "Jessy sourit. Il efface le « tu es sûre que ça va ? » qu'il était en train de taper."
    i "On joue demain."
    j "Je laisse la maison debout jusque-là."
    i "Touche pas au toit."
    systeme "Il retire le bloc qu'il venait de poser. Puis il quitte le serveur."
    jump ending_ilonanium_silence


# 2. LE SILENCE — ELLE REPOND PLUS
label ending_ilonanium_silence:
    $ ilonanium_music_stop(2.0)
    scene black with fade
    centered "MARDI"
    scene bg friend chambre jessy with fade
    systeme "À neuf heures, Jessy demande si elle a mieux dormi. À midi, son message n'a toujours pas été lu."
    systeme "Il prépare à manger. Revient devant son téléphone."
    $ ilonanium_effect("call", level=0.65, channel="ilon_detail")
    systeme "Lance un appel."
    $ ilonanium_wait_audio(2.4, channel="ilon_detail")
    $ ilonanium_effect_stop(seconds=0.0, channel="ilon_detail")
    "Messagerie" "Votre correspondant n'est pas disponible. Veuillez laisser un message."
    j "C'est moi. Je voulais prendre de tes nouvelles. Rappelle-moi quand tu peux."
    systeme "Il ouvre la conversation du groupe."
    j "Quelqu'un a eu Ilona aujourd'hui ? Elle était malade hier."
    a "Non. Rien depuis votre retour."
    s "Moi non plus."
    systeme "Alexandre ne répond pas. Théo écrit depuis Tokyo : il n'a pas eu de nouvelles non plus."
    systeme "Jessy pose le téléphone à côté de son assiette."
    $ ilonanium_effect("phone", level=0.85, channel="ilon_detail")
    systeme "Il vibre avant qu'il ait touché ses baguettes. Un message d'Ilona."
    i "Je crois que ça va pas."
    $ ilonanium_effect("call", level=0.75, channel="ilon_detail")
    systeme "Il rappelle tout de suite. Une sonnerie. Deux."
    $ ilonanium_wait_audio(2.4, channel="ilon_detail")
    $ ilonanium_effect_stop(seconds=0.0, channel="ilon_detail")
    systeme "La messagerie."
    j "Ilona, je viens."
    systeme "Il envoie l'adresse au groupe, avec un dernier message : {i}« Je vous tiens au courant. »{/i} Il prend ses clés."
    jump ending_ilonanium_chez_elle


# 3. CHEZ ELLE — ILONA ?
label ending_ilonanium_chez_elle:
    scene bg ilonanium rue with fade
    $ ilonanium_bed("street", level=0.75)
    systeme "Devant chez Ilona, un vélo passe. Une fenêtre se ferme dans la maison voisine. Rien ne semble avoir changé."
    systeme "Jessy sonne. Attend. Frappe à la porte."
    j "Ilona ? C'est Jessy."
    i "Entre... C'est ouvert."
    stop ambiant1 fadeout 1.0
    scene bg ilonanium chambre with fade
    $ ilonanium_bed_stop(seconds=0.8)
    show jessy ilonanium beach_neutral at ilonanium_left
    show ilona ilonanium sick at ilonanium_right
    with dissolve
    systeme "Les rideaux sont tirés. Ilona est assise contre son lit, les genoux ramenés vers elle. Un bol presque plein refroidit sur la table. Son téléphone est au sol, près de la porte."
    j "Tu es toute seule ?"
    i "Oui. J'ai essayé de me lever pour ouvrir. J'ai lâché le téléphone. J'arrivais plus à le reprendre."
    systeme "Il s'accroupit près d'elle. Elle tend la main avant qu'il ait demandé."
    j "Depuis quand tu peux plus te lever ?"
    i "Je sais pas. J'ai dormi. Après... j'ai perdu l'heure."
    j "Je vais appeler les secours."
    i "Oui. S'il te plaît."
    systeme "Il compose le 119 et donne l'adresse."
    $ ilonanium_effect("glass", level=0.70, channel="ilon_detail")
    systeme "Pendant qu'il décrit son état, un verre glisse sur la table."
    systeme "Jessy tend la main pour le rattraper. Le verre s'arrête au bord. Puis il tombe, de travers, en direction d'Ilona."
    i "Ça l'a déjà fait."
    j "Quoi ?"
    $ ilonanium_bed("gravity", level=0.30, channel="ilon_texture", fade=2.0)
    scene cg ilonanium attraction with dissolve
    systeme "Une cuillère rejoint le verre. Sur le sol, le téléphone bouge à son tour. La table est droite. Le plancher aussi."
    i "Les choses viennent vers moi."
    $ ilonanium_music("tension", level=0.55, fadein=2.0)
    systeme "Dans le combiné, une voix demande à Jessy de répéter. Il regarde la cuillère, maintenant suspendue au-dessus du tapis."
    j "Il faut venir vite."
    jump ending_ilonanium_bascule


# 4. LA BASCULE — C'EST PAS UNE INDIGESTION
label ending_ilonanium_bascule:
    systeme "Ilona serre sa main. Les rideaux se tendent vers l'intérieur, alors que la fenêtre est fermée."
    i "J'ai l'impression que ça tire. Partout. Mais de dedans."
    j "On va sortir. Tu peux t'appuyer sur moi ?"
    $ ilonanium_bed("wood", level=0.55, channel="ilon_place")
    $ ilonanium_bed_level(0.60, channel="ilon_texture")
    scene cg ilonanium gravite with dissolve
    systeme "Elle essaie. Ses pieds quittent le sol avant qu'elle soit debout. Jessy l'attrape à la taille."
    with hpunch
    $ ilonanium_effect("crack", level=0.80, channel="ilon_detail")
    systeme "La poignée s'arrache de la porte. Le bois se courbe vers eux. Jessy recule, entraîné malgré lui. Son téléphone lui échappe et disparaît dans une lumière pâle."
    # Le bois cesse avant le dialogue : la gravite garde seule la tension.
    $ ilonanium_bed_stop(seconds=0.8)
    $ ilonanium_effect("laplage", level=0.75)
    scene cg ilonanium laplage with Fade(0.1, 0.0, 0.4, color="#fff")
    laplage "Ne tirez pas sur elle. Prenez ma main."
    j "Monsieur Laplage ? Comment vous..."
    systeme "Il s'arrête. Laplage ne sourit pas. Une fissure remonte le mur derrière son épaule."
    j "Vous pouvez faire quelque chose ?"
    laplage "Pour vous faire sortir, oui."
    j "Et pour elle ?"
    systeme "Laplage regarde Ilona. Puis le sac de randonnée posé près du lit. Le noyau étoilé traverse lentement le tissu et flotte entre eux."
    laplage "Le fruit de la montagne. Vous l'avez mangé ?"
    i "Samedi. Mais c'est pas le premier truc bizarre que je mange."
    laplage "Non. C'est le dernier qu'il manquait."
    j "Il manquait pour quoi ?"
    laplage "Pour que tout ce qu'elle a mangé se réveille ensemble."
    i "Arrêtez-le."
    scene cg ilonanium echec with dissolve
    systeme "Laplage tend la main vers le noyau, les doigts écartés. Des filaments de lumière se tendent entre sa paume et celle d'Ilona, autour de l'étoile. Pendant une seconde, le verre redescend."
    with vpunch
    systeme "Puis la fenêtre entière se détache. Laplage retire sa main, brûlée."
    $ ilonanium_music_level(0.20, 0.4)
    $ ilonanium_bed_level(0.20, channel="ilon_texture", seconds=0.4)
    laplage "Je n'y arrive pas."
    $ ilonanium_music_stop(0.8)
    scene cg ilonanium adieu with dissolve
    i "Jessy. Recule."
    j "Je vais pas te laisser là."
    i "Regarde-moi. J'arrive plus à retenir les choses. Je vais pas réussir à te retenir, toi."
    if arc7_jessy_relation == "amour":
        i "On devait avoir tout l'été."
        j "Je suis là. Je suis encore là."
    else:
        i "Je voulais pas que notre dernière soirée soit celle de la tente."
        j "C'est pas notre dernière soirée. Tu m'entends ?"
    systeme "Elle desserre ses doigts. Jessy garde sa main ouverte devant la sienne."
    i "Va avec lui. Et m'oublie pas."
    systeme "Le mur disparaît. Au-delà, les façades de la rue se penchent dans la même direction. Une lumière étoilée traverse les fondations de la maison."
    jump ending_ilonanium_catastrophe


# 5. L'ILONANIUM — LAISSER DIGERER
label ending_ilonanium_catastrophe:
    systeme "Jessy voit encore le visage d'Ilona au milieu de la lumière. Elle cherche ses yeux."
    j "Ilona !"
    $ ilonanium_music("across", level=0.80, fadein=1.0)
    $ ilonanium_bed_level(0.80, channel="ilon_texture", seconds=1.5)
    scene cg ilonanium maison with Dissolve(1.5)
    systeme "La maison se courbe autour de la lumière. Dans la rue, les toitures et les câbles se tendent vers Ilona."
    scene cg ilonanium arrachement with dissolve
    systeme "Laplage saisit Jessy par l'épaule et l'entraîne dans le TARDIS. Derrière la porte de la cabine bleue, l'espace s'ouvre sur une salle immense. Jessy tend encore la main vers Ilona quand la porte se referme."
    # Le moteur part apres la fermeture de la porte, puis cede au refuge.
    $ ilonanium_effect("departure", level=0.75)
    scene black with Fade(0.1, 0.1, 0.5, color="#fff")
    $ ilonanium_wait_audio(3.0, channel="ilon_machine")
    $ ilonanium_effect_stop(seconds=0.6, channel="ilon_machine")
    scene bg ilonanium plage with Dissolve(1.0)
    show jessy ilonanium beach_neutral at ilonanium_left
    show laplage ilonanium neutral at ilonanium_right
    with dissolve
    $ ilonanium_bed("ocean", level=0.72)
    $ ilonanium_bed_level(0.22, channel="ilon_texture")
    $ ilonanium_effect("arrival", level=0.65)
    systeme "Quand la porte du TARDIS se rouvre, une plage inconnue s'étend devant eux. Au-dessus, deux soleils. Jessy descend sur le sable."
    systeme "Sur Terre, la lumière a avalé la maison. Puis le quartier."
    show jessy ilonanium beach_angry at ilonanium_left
    j "Ramenez-moi !"
    laplage "Chaque seconde ici, c'est quelqu'un que je ne pourrai plus atteindre là-bas."
    systeme "Jessy lâche son bras. Laplage remonte dans la cabine. Le TARDIS disparaît."
    hide laplage with dissolve
    $ ilonanium_bed("wood", level=0.80)
    $ ilonanium_bed_level(0.90, channel="ilon_texture")
    $ ilonanium_effect("debris", level=0.80)
    scene cg ilonanium catastrophe with fade
    systeme "Des quartiers entiers se soulèvent. Les routes se plient, les immeubles s'inclinent et des masses d'eau remontent vers le même centre."
    $ ilonanium_bed_stop(seconds=0.8)
    $ ilonanium_effect("arrival", level=0.80)
    scene cg ilonanium sauvetage with dissolve
    systeme "Le TARDIS apparaît au milieu des rues qui se défont. Laplage ouvre sa porte, fait entrer les habitants et repart chercher ceux qu'il peut encore atteindre."
    systeme "Des immeubles et leurs habitants. Des morceaux de forêt. De l'eau, de la terre, des bêtes. La cabine emporte ce qu'elle peut vers des rivages qui n'ont pas de nom."
    $ ilonanium_bed_level(0.65, channel="ilon_texture")
    scene cg ilonanium terre with Dissolve(1.5)
    systeme "Sur Terre, les continents se replient. Les océans montent vers le ciel. La forme qui grandit à leur place n'est plus humaine."
    scene bg ilonanium plage with fade
    systeme "Allan et Théo sortent ensemble du TARDIS, encore secoués par leur départ de Tokyo. Plus loin, Sofiane retrouve sa voiture devant une mer qui n'était pas au bout de sa route."
    $ ilonanium_music_level(0.48, 1.0)
    $ ilonanium_bed("ocean", level=0.72)
    $ ilonanium_bed_stop(channel="ilon_texture", seconds=1.0)
    scene cg ilonanium survivants with Dissolve(1.0)
    systeme "Jessy avance lentement parmi les rescapés. Avec un autre homme, il porte un blessé sur un brancard."
    systeme "Il scrute les nouveaux arrivants, reconnaît peu à peu les visages de ses amis. Mais celui d'Alexandre manque toujours."
    j "Alexandre ! Quelqu'un a vu Alexandre ?"
    scene bg ilonanium plage
    show jessy ilonanium beach_determined at ilonanium_left
    with dissolve
    $ ilonanium_effect("arrival", level=0.58)
    systeme "La cabine bleue réapparaît une dernière fois. Laplage en sort à genoux."
    show laplage ilonanium exhausted at ilonanium_right with dissolve
    show jessy ilonanium beach_neutral at ilonanium_left
    j "J'ai vu tous mes amis sauf Alexandre ! Il est où ?!"
    laplage "Je n'ai pas pu le ramener. Il est encore là-bas."
    j "Alors retournez le chercher !"
    $ ilonanium_effect("failure", level=0.85)
    systeme "Laplage retourne au poste de commande. Le moteur gémit, puis s'éteint. Il essaie encore. La cabine ne bouge plus."
    laplage "Je ne peux plus repartir."
    $ ilonanium_effect_stop(seconds=0.5, channel="ilon_machine")
    $ ilonanium_bed_stop(seconds=1.0)
    $ ilonanium_bed("gravity", level=0.45, channel="ilon_texture", fade=2.0)
    scene cg ilonanium naissance astre with Dissolve(2.0)
    systeme "La sphère se stabilise. Les nuages et les reliefs se mêlent à une surface nouvelle. Deux yeux gigantesques s'ouvrent à l'échelle du monde."
    scene bg ilonanium astre with Dissolve(2.0)
    systeme "Le nouvel astre achève de prendre forme. Sous ses traits, le berceau de l'humanité a disparu."
    systeme "Parmi les survivants, un nom passe de bouche en bouche pour désigner ce monde de cauchemar : l'Ilonanium."
    systeme "Plus tard, on comptera. Un dixième de la Terre et de ses habitants a traversé. Tout le reste est demeuré dans l'Ilonanium."
    pause 1.5
    j "Monsieur Laplage, on fait quoi ?"
    $ ilonanium_silence(1.2)
    $ renpy.pause(1.5, hard=True)
    laplage "Laissez digérer."
    scene black with fade
    systeme "Le TARDIS reste immobile. Ce qui reste de l'humanité apprend à vivre sous un autre ciel."
    jump ending_ilonanium_deux_soleils


# 6. DEUX SOLEILS — LE PROCHAIN, C'EST TOI
label ending_ilonanium_deux_soleils:
    $ ilonanium_bed("ocean", level=0.72, fade=2.0)
    centered "QUARANTE ANS PLUS TARD"
    scene bg ilonanium plage reconstruite with fade
    $ ilonanium_music("majula", level=0.80, fadein=3.0)
    show theo ilonanium older_regretful at ilonanium_left with dissolve
    systeme "Le premier soleil touche l'eau. Le second éclaire encore les cheveux gris de Théo. Assis dans le sable, il regarde deux ombres s'allonger devant lui."
    t "Quarante ans. Et je reviens toujours au même endroit."
    show laplage ilonanium farewell at ilonanium_right with dissolve
    laplage "Il y a de la place."
    systeme "Monsieur Laplage s'assoit à côté de lui. Il a l'air plus mince. Le vent traverse presque le bord de sa chemise."
    t "Vous savez ce que je me demande ?"
    laplage "Ce que vous auriez pu faire."
    t "Parler à Ilona. Rester. Être quelqu'un d'autre avant qu'il soit trop tard."
    laplage "Vous auriez pu lui faire moins de mal. Cela ne veut pas dire que vous auriez su arrêter ça."
    t "Vous, vous saviez des choses. Vous apparaissiez partout. Pourquoi ?"
    show ilonanium_photo at ilonanium_photo_lancer zorder 20
    systeme "Laplage sort une vieille photo. Un jeune homme et Ilona, serrés dans le cadre. Théo reconnaît son propre visage. Pas le lieu."
    show theo ilonanium older_surprised at ilonanium_left with dissolve
    t "Cette photo n'existe pas."
    laplage "Pas dans votre vie. Dans la mienne, si."
    $ ilonanium_music_level(0.45, 1.0)
    t "Qui êtes-vous ?"
    laplage "Vous. Avec beaucoup de retard."
    systeme "Théo regarde de nouveau la photo. Il n'a jamais vécu cet instant avec elle."
    t "J'étais avec elle ?"
    show theo ilonanium older_regretful at ilonanium_left with dissolve
    $ ilonanium_music_stop(1.0)
    laplage "Oui. Je décidais de tout. De ses horaires, de ce qu'elle devait vouloir, de ce qu'elle avait le droit de trouver difficile."
    laplage "Quand elle n'a plus supporté cette vie, je lui ai encore demandé d'attendre. Ilona a fini par se donner la mort."
    pause 1.5
    systeme "Théo ne dit rien. Laplage laisse la photo entre eux, sur le sable."
    hide ilonanium_photo with Dissolve(0.25)
    laplage "Je suis revenu pour changer cela. Pas pour la récupérer. Pour qu'elle puisse vivre sans moi."
    t "Et vos pouvoirs ?"
    laplage "Un vieil homme me les a donnés sur une plage. Il avait mon visage. Mais c'était encore sur Terre."
    t "Vous."
    laplage "Moi aussi, j'ai trouvé l'explication peu pratique."
    systeme "Théo laisse passer un rire très court. Laplage détache de son manteau le porte-clés creeper."
    laplage "Mon corps arrive au bout. Bientôt, il ne restera ici que du sable. Ça, en revanche, peut encore servir."
    systeme "Laplage se relève lentement. Théo se lève avec lui."
    # Le geste et les adieux sont peints dans le CG, sans sprites superposes.
    $ ilonanium_music("majula", level=0.65, fadein=2.0)
    $ ilonanium_effect("transfer", level=0.70, channel="ilon_detail")
    scene cg ilonanium transmission with Dissolve(1.5)
    systeme "Il pose le porte-clés dans la paume de Théo. Une chaleur remonte jusqu'à son coude."
    laplage "Réussis là où j'ai échoué. Le prochain, c'est toi."
    laplage "Ce porte-clés commande aussi le TARDIS. Il te reconnaîtra quand tu l'appelleras."
    scene bg ilonanium plage reconstruite
    show theo ilonanium laplage at ilonanium_left
    show laplage ilonanium farewell_no_creeper at ilonanium_right
    with Dissolve(1.5)
    t "Attendez. Qu'est-ce que je peux faire avec ça ?"
    laplage "Dans l'espace, ton pouvoir ne te portera que de quelques mètres. Le sauvetage a presque tout pris."
    laplage "Le TARDIS a mis quarante ans à retrouver assez d'énergie pour repartir. Il pourra vous transporter dans le temps, mais ses moteurs sont trop abîmés pour franchir les distances entre les étoiles."
    laplage "Dans le temps, les passages existent encore. Mais seulement aux croisements des lignes temporelles. Des nœuds de convergence."
    t "Je peux choisir une date ?"
    laplage "Tu peux sauter d'un nœud à un autre. Pas t'arrêter entre les deux. Passé ou futur, chaque voyage est un aller simple. Le passage se ferme derrière toi."
    t "Vous savez déjà où ils mènent ? Vous aviez vécu tout ça avant de revenir ?"
    laplage "Non. Dans ma vie, j'ai attendu dix ans de plus avant de repartir vers la rentrée. La Terre existait encore. L'Ilonanium, je l'ai découvert avec vous."
    t "Alors comment vous trouvez les passages ?"
    laplage "Le pouvoir permet de les sentir, même ceux qui ne se sont pas encore ouverts. Tu peux en percevoir la date. Pas ce qui t'attend de l'autre côté."
    systeme "Théo baisse les yeux vers le porte-clés. Au creux de sa main, la chaleur pulse à intervalles irréguliers."
    laplage "Ferme les yeux. Ne cherche pas un lieu. Cherche quand."
    $ ilonanium_effect("ilona", level=0.60, channel="ilon_detail")
    systeme "Théo ferme les yeux. Il sent une première résistance, proche. Puis une autre, beaucoup plus loin. Il rouvre les yeux, le souffle court."
    t "Le dernier ?"
    laplage "Avant notre dernière rentrée des classes. Il y a plus de quarante et un ans. Aucun depuis."
    t "Et les prochains ?"
    laplage "Un dans un mois. Un dans dix ans. Puis plus rien avant neuf cent quatre-vingt-dix-neuf ans et un mois."
    systeme "Théo referme ses doigts sur le creeper. Le deuxième soleil atteint enfin la mer."
    show theo ilonanium laplage_determined at ilonanium_left with dissolve
    $ ilonanium_music_level(0.82, 2.0)
    t "Revenir avant n'a pas suffi. Alors je vais partir après."
    laplage "Après ?"
    t "Le nœud qui s'ouvre dans un mois. Je l'emprunte pour ressortir neuf cent quatre-vingt-dix-neuf ans plus tard."
    t "Un millénaire pour construire un vaisseau. Je prépare le projet maintenant, et je vais le chercher quand il est prêt."
    laplage "Tu ne sais pas ce que tu trouveras."
    t "Non. Mais Ilona est là-bas. Et notre monde avec elle. Je vais réunir les autres."
    laplage "Audacieux. Pense aussi à Florentin. Il commande une milice. Tu pourrais avoir besoin de lui."
    t "Vous venez avec moi ?"
    systeme "Laplage secoue la tête. Théo se baisse pour ramasser la photo."
    laplage "Garde-la. Et cette fois, demande aux autres ce qu'ils sont prêts à faire."
    t "Vous allez où ?"
    laplage "Marcher un peu."
    $ ilonanium_effect("steps", level=0.55, channel="ilon_detail")
    scene cg ilonanium adieux laplage with Dissolve(1.5)
    systeme "Il s'éloigne au bord de l'eau. Les vagues effacent ses traces presque aussitôt."
    laplage "Bon courage, Théo. Tous mes espoirs sont dans ta poche."
    systeme "Théo reste debout jusqu'à ce que la silhouette disparaisse."
    scene bg ilonanium plage reconstruite
    show theo ilonanium thumb_up at ilonanium_left
    with Dissolve(2.0)
    systeme "Puis il lève le pouce. Pour quelqu'un qui ne le voit plus."
    $ ilonanium_music_stop(3.0)
    scene black with fade
    pause 2.0
    jump ending_ilonanium_survivants


# 7. CE QU'ILS SONT DEVENUS
label ending_ilonanium_survivants:
    $ ilonanium_bed_stop(seconds=1.5)
    scene bg ilonanium exoplanete with fade
    # Rappel du bivouac, plus intime pour le bilan des quarante annees.
    $ ilonanium_music("aftermath", level=0.64, fadein=2.5)
    systeme "Quarante ans après la catastrophe, des villes bordent les archipels de l'exoplanète. Des ponts relient les îles. Au centre des grands atolls, les ports ne dorment jamais."
    systeme "Et pendant tout ce temps..."
    scene black with dissolve
    centered "MICKA"
    scene bg ilonanium conseil with dissolve
    show micka ilonanium governor at ilonanium_center with dissolve
    systeme "Micka est devenu gouverneur de l'humanité. Il a réuni les colonies, imposé la paix et fait construire un Capitole dont il trouve encore le balcon trop petit."
    systeme "Ses recherches sur ses propres gènes ont permis de traiter l'infertilité et de repousser les limites de la ménopause. La démographie s'est remise. Son ego aussi."
    systeme "Meilleur combattant de la planète, il a reçu le rang de gigachad de la Légion d'honneur refondée. Personne n'a osé proposer un rang au-dessus."
    mi "Le problème du balcon, c'est qu'on me voit pas assez depuis les côtés."
    scene black with dissolve
    centered "JESSY"
    scene bg ilonanium exoplanete with dissolve
    show jessy ilonanium priest at ilonanium_center with dissolve
    systeme "Jessy a fondé le culte de Laplage. Le sauveur de l'humanité est devenu son Messi ; lui, son prophète. En quarante ans, sa religion est devenue majoritaire."
    systeme "Son visage, lui, est resté celui du garçon revenu de randonnée. Il cache quelque chose de plus étrange encore."
    $ ilonanium_music_level(0.20, 0.5)
    $ ilonanium_effect("ilona", level=0.75, channel="ilon_detail")
    i "Jessy... Retrouve-moi."
    systeme "La voix ne vient d'aucune pièce. Elle est là quand il ferme les yeux, quand il marche, quand il essaie de dormir."
    j "Je cherche."
    systeme "Il dit aux fidèles qu'il attend le retour du Messi. Ce qu'il attend vraiment, c'est un chemin vers Ilona."
    scene black with dissolve
    $ ilonanium_music_level(0.64, 1.5)
    centered "SOFIANE"
    scene bg ilonanium exoplanete with dissolve
    show sofiane ilonanium civilian_neutral at ilonanium_center with dissolve
    systeme "Sofiane a tracé les routes qui relient les communautés humaines. On l'appelle l'ange de la route. Il trouve le titre un peu chargé pour quelqu'un qui fait aussi les ronds-points."
    systeme "Il a fini par affronter Monsieur Laplage dans une course. Et par gagner."
    systeme "Pour récompense, Laplage a confié à la Trueno AE86, que le cousin n'a jamais réclamée, un fragment de son pouvoir. Depuis, ni la rouille ni les années ne semblent trouver la voiture."
    show sofiane ilonanium civilian_smirk at ilonanium_center with dissolve
    s "On m'a demandé pourquoi je gardais toujours la même. J'ai demandé pourquoi ils changeaient."
    scene black with dissolve
    centered "ALLAN"
    scene bg ilonanium bar with dissolve
    show allan ilonanium ceo at ilonanium_center with dissolve
    systeme "Muchacho Corporation a reconstruit les villes. Gringos Industry les a équipées. À la tête des deux entreprises, Allan signe des contrats avec Micka et mange encore au-dessus des dossiers."
    systeme "Une fois par an, il réserve une table pour Théo. Ils parlent de ce qui va, de ce qui manque, et de la retraite qu'Allan annonce depuis quinze ans."
    a "Cette fois, je délègue. Enfin, après le prochain contrat."
    scene black with fade
    systeme "Tout ce beau monde s'apprête à changer l'histoire. Aucun d'eux ne le sait encore. Sauf un."
    jump ending_ilonanium_bar


# 8. LE BAR D'ALLAN
label ending_ilonanium_bar:
    scene bg ilonanium bar with fade
    show theo ilonanium laplage at ilonanium_left
    show allan ilonanium ceo at ilonanium_right
    with dissolve
    $ ilonanium_music("bar", level=0.50, fadein=1.5)
    systeme "Dans la salle privée de son bar, Allan commande deux verres. Théo est déjà assis. Il a posé un porte-clés entre les sous-verres."
    a "Un an sans te voir, et tu m'apportes un creeper. Tu pouvais venir les mains vides."
    t "J'ai vu Monsieur Laplage."
    a "Ah. Il est revenu ?"
    t "Il est parti. Et je crois que cette fois, il ne reviendra pas."
    systeme "Allan laisse le serveur fermer la porte. Théo raconte la plage, la photo, les passages. Allan l'écoute jusqu'au bout, son verre intact."
    show allan ilonanium ceo_surprised at ilonanium_right with dissolve
    a "Attends. Le vendeur de takoyaki, le type des objets trouvés, le Père Noël... Tout ça, c'était toi ?"
    t "Une autre version de moi. Oui."
    a "Avec Alex, on cherchait comment il entrait dans les couloirs fermés. On aurait dû te demander."
    t "J'aurais été aussi perdu que vous."
    a "Ça fait beaucoup d'informations à encaisser d'un coup."
    systeme "Théo avance la main. Son verre disparaît et réapparaît à l'autre bout de la table. Allan regarde sous la table. Puis dans le verre."
    a "D'accord. Le budget démonstration est convaincant."
    show theo ilonanium laplage_determined at ilonanium_left with dissolve
    t "Dans un mois, un nœud de convergence s'ouvre. Je peux l'emprunter pour partir neuf cent quatre-vingt-dix-neuf ans dans le futur. Je veux qu'un vaisseau nous y attende."
    a "Un vaisseau pour retrouver l'Ilonanium."
    t "Et ramener ce qu'on peut. Ilona. La Terre. Les autres, s'ils sont encore là."
    a "On travaille déjà sur des fusées. En mille ans, Gringos peut construire plus gros. Une arche autonome, pas une boîte avec six sièges."
    t "Tu acceptes ?"
    show allan ilonanium ceo_supportive at ilonanium_right with dissolve
    a "Je t'ai jamais vu aussi sérieux. Et j'ai pas construit tout ça pour fabriquer des grille-pain jusqu'à ma mort."
    t "Il nous faut Micka, Jessy et Sofiane. Laplage m'a aussi donné un nom : Florentin."
    a "Le commandant de la milice ? Je le connais. Gringos équipe ses hommes."
    a "Au début, ils protégeaient les campements contre les créatures de cette planète. Aujourd'hui, c'est la plus grande armée de l'humanité."
    t "Il accepterait de partir ?"
    a "Sa femme est restée sur Terre. Il a jamais cessé de vouloir y retourner."
    a "Il commande toujours comme si la guerre commençait jeudi. Cette fois, on a peut-être une destination à lui donner."
    a "Je préviens Micka. Réunion de crise, bureau du gouverneur. Je m'occupe de convaincre Florentin."
    t "Merci. D'être encore là."
    a "J'avais prévu ma retraite. Mais bon. Apparemment, mon prochain rendez-vous est dans mille ans."
    systeme "Ils lèvent leurs verres. Allan rappelle le serveur : cette fois, ils vont manger."
    $ ilonanium_music_stop(2.0)
    scene black with fade
    centered "TROIS JOURS PLUS TARD"
    jump ending_ilonanium_conseil


# 9. LE CONSEIL DU CAPITOLE
label ending_ilonanium_conseil:
    scene bg ilonanium conseil with fade
    show micka ilonanium governor at ilonanium_left
    show florentin ilonanium armor_resolved at ilonanium_center
    show allan ilonanium ceo at ilonanium_right
    with dissolve
    $ ilonanium_music_stop(0.5)
    $ ilonanium_bed_stop(seconds=0.6)
    systeme "Micka les accueille dans le bureau ovale du Capitole. Allan a apporté des plans. Florentin, une mallette fermée. Sofiane, ses clés de voiture."
    mi "Ça fait du bien de vous revoir. Asseyez-vous."
    systeme "Avant de prendre place, Micka désigne l'homme en armure près d'Allan."
    mi "Le commandant Florentin nous rejoint pour cette réunion. Certains d'entre vous ne l'ont pas encore rencontré."
    systeme "Florentin se lève, se met au garde-à-vous et adresse un salut militaire au gouverneur. Puis il se tourne vers les autres."
    ilonanium_florentin "Allan m'a expliqué votre projet. Mes forces sont disponibles."
    a "Il a dit oui avant que je finisse la phrase."
    hide micka
    hide florentin
    hide allan
    show theo ilonanium laplage at ilonanium_left
    show jessy ilonanium priest_listening at ilonanium_right
    with dissolve
    systeme "Jessy entre le dernier. Il s'arrête devant Théo."
    j "Le Messi."
    t "Tu es au courant ?"
    j "Je le sens. C'est toi, maintenant."
    show micka ilonanium governor at ilonanium_center with dissolve
    systeme "Théo baisse les yeux vers le porte-clés accroché à son manteau. Micka regarde Jessy, puis les visages marqués par le temps autour de la table."
    mi "Avant qu'on commence : on peut enfin parler du fait que tu as toujours vingt ans ?"
    a "Cinq fruits et légumes par jour ?"
    s "Une vidange régulière."
    t "Tu peux nous le dire, Jessy."
    $ ilonanium_effect("ilona", level=0.50, channel="ilon_detail")
    j "Ilona me parle. Depuis le jour où on l'a perdue."
    systeme "Personne ne cherche une autre blague."
    j "Elle me demande de la retrouver. Je crois que c'est elle qui m'empêche de vieillir. Pour que je puisse arriver jusqu'à elle."
    if arc7_jessy_relation == "amour":
        j "On venait de se choisir. J'ai pas eu le temps d'apprendre à vivre avec elle."
    else:
        j "Je lui avais demandé de rester mon amie. Ça voulait pas dire que j'allais l'abandonner."
    j "Ce lien, je sais pas l'expliquer. Mais sa voix, je la reconnaîtrais partout."
    systeme "Florentin baisse les yeux vers sa mallette. Il ne dit rien."
    t "Alors tu comprends pourquoi on est là. Dans vingt-sept jours, le prochain nœud de convergence s'ouvrira. Je pourrai nous emmener neuf cent quatre-vingt-dix-neuf ans dans le futur."
    t "Ce millénaire, on va le laisser à l'humanité pour construire notre vaisseau. Voilà ce que je vous propose."
    scene cg ilonanium preparatifs with Dissolve(1.5)
    systeme "Théo désigne une date sur le calendrier étalé devant lui. À ses côtés, Allan pointe du stylo le plan d'une immense station annulaire."
    systeme "Vingt-sept jours pour transmettre une mission. Neuf cent quatre-vingt-dix-neuf ans pour la rendre possible. Un rendez-vous au même endroit, de l'autre côté du temps."
    $ ilonanium_music("plan", level=0.60, fadein=2.0)
    a "Le projet s'appelle TAIKUN. Une station autonome. Logements, cultures, usines, réserves. De quoi faire le voyage et vivre une fois là-bas."
    s "Il y a un garage ?"
    a "Je peux en prévoir un."
    mi "Tu as encore ta Trueno ? Ma deudeuche a rendu l'âme il y a des années."
    s "La mienne a reçu un fragment du pouvoir de Monsieur Laplage. Après notre course. Depuis, elle reste comme neuve."
    t "Elle peut peut-être agir sur l'espace-temps. Tu as essayé ?"
    s "Non. Quand je prends la route, le plus important, c'est le voyage."
    a "Sofiane. Tu conduis peut-être un moteur supraluminique pour aller acheter du pain."
    s "Le pain arrive chaud."
    a "Alors on laisse ta voiture aux ingénieurs. Ils auront un millénaire pour comprendre le fragment et en faire le moteur du TAIKUN."
    s "Ma Trueno en V8000. Une condition : c'est moi qui conduis."
    a "Accordé."
    scene bg ilonanium conseil
    show theo ilonanium laplage_determined at ilonanium_left
    show jessy ilonanium priest_determined at ilonanium_center
    show florentin ilonanium armor_angry at ilonanium_right
    with dissolve
    j "Je peux vous guider. Quand je l'entends, je sens aussi d'où ça vient. Là-bas, je trouverai le chemin."
    ilonanium_florentin "Et moi, j'ouvre la route une fois arrivés. J'attends de rendre les coups depuis quarante ans."
    j "On part pas faire une croisade contre elle."
    $ ilonanium_music_stop(0.8)
    ilonanium_florentin "Ma femme est restée sur Terre. Tu me demandes de regarder ça comme un rendez-vous ?"
    j "Ta femme est restée là-bas. Ilona aussi. Si tu tires sur l'Ilonanium, tu tires sur tout ce qu'on a laissé."
    ilonanium_florentin "Et si c'est elle qui me l'a prise ?"
    systeme "Jessy ne répond pas. Pour la première fois, il n'a pas de réponse prête."
    t "On part libérer Ilona et retrouver notre monde. On ignore ce qui nous attend. Nous aurons besoin de soldats, pas d'un tir à l'aveugle."
    t "Si tu veux appeler ça une croisade, ce sera une reconquête. Pas une exécution."
    systeme "Florentin regarde Théo, puis Jessy. Il finit par hocher la tête."
    show florentin ilonanium armor_resolved at ilonanium_right with dissolve
    j "D'accord. Pardon, Florentin. Je sais ce que tu as perdu."
    ilonanium_florentin "Je préparerai la relève. Quand nous arriverons, leurs descendants seront prêts."
    mi "Le vaisseau, le moteur, le guide, l'armée. Nous avons un plan. Il reste son plus gros problème."
    jump ending_ilonanium_celui_qui_reste


# 10. CELUI QUI RESTE
label ending_ilonanium_celui_qui_reste:
    hide theo
    hide florentin
    show micka ilonanium governor_serious at ilonanium_left
    show jessy ilonanium priest_listening at ilonanium_center
    show allan ilonanium ceo at ilonanium_right
    with dissolve
    mi "Comment être certains que dans neuf cent quatre-vingt-dix-neuf ans, quelqu'un suivra encore nos consignes ?"
    a "Des institutions. Des archives. Un financement protégé."
    mi "Et presque un millénaire de gens qui auront leurs propres urgences. Les archives peuvent brûler. Un gouvernement peut changer d'avis."
    systeme "Allan repose son stylo. Le calendrier prend soudain beaucoup plus de place que les plans."
    j "Vous aurez quelqu'un ici."
    hide micka
    show theo ilonanium laplage at ilonanium_left
    with dissolve
    t "Jessy..."
    systeme "Jessy regarde les cinq autres, un par un."
    show jessy ilonanium priest_determined at ilonanium_center with dissolve
    $ ilonanium_music_stop(0.0)
    j "Je monte pas dans le TARDIS."
    show allan ilonanium ceo_surprised at ilonanium_right with dissolve
    a "Tu attends ici ? Tout ce temps ?"
    j "Oui."
    mi "Neuf cent quatre-vingt-dix-neuf ans. Pas un mandat. Pas une vie."
    j "Je sais compter. J'ai eu du temps pour apprendre."
    systeme "La plaisanterie ne fait rire personne. Jessy pose ses mains à plat sur la table."
    j "Les gens connaissent le culte de Laplage. Ils attendent déjà son retour. Je peux leur donner quelque chose à construire pendant cette attente."
    j "Le TAIKUN. Une flotte. De quoi retrouver notre monde. Je serai là pour rappeler pourquoi on a commencé."
    t "J'arrive pas à croire que tu sois prêt à faire ça."
    j "Tu avais compris avant que je le dise. Digne de l'omniscience du Messi."
    t "Ne m'appelle pas comme ça pour éviter ma question. Tu as le droit de venir avec nous."
    systeme "Jessy baisse les yeux. Pendant quelques secondes, il ne répond pas."
    $ ilonanium_music("promise", level=0.78, fadein=2.5)
    show jessy ilonanium priest_emotional at ilonanium_center with dissolve
    j "J'ai peur de rester. Je sais même pas ce que ça fait, cent ans."
    show jessy ilonanium priest_determined at ilonanium_center with dissolve
    j "Mais si on arrive devant un terrain vide, on aura tout perdu. Je peux faire quelque chose ici. Alors je reste."
    systeme "Sofiane pose ses clés à côté des plans. Allan pousse vers Jessy le dossier du TAIKUN."
    show allan ilonanium ceo_supportive at ilonanium_right with dissolve
    a "On te laisse pas seulement une promesse. Les équipes commencent aujourd'hui."
    ilonanium_florentin "Je signerai les ordres de transmission avec toi. L'armée saura à qui répondre."
    j "J'entretiendrai la prophétie. Le retour du Messi et de ses apôtres. La reconquête du berceau. Chaque génération aura sa part à faire."
    a "C'était pas dans mon bingo que je devienne un apôtre de Laplage."
    t "Félicitations pour votre promotion, monsieur le PDG."
    a "J'aurai plus de place sur mon CV si ça continue."
    show jessy ilonanium priest_smile at ilonanium_center with dissolve
    systeme "Cette fois, ils rient. Jessy aussi. Il n'a pas retiré ses mains de la table."
    hide theo
    show micka ilonanium governor at ilonanium_left
    with dissolve
    mi "Je vais annoncer la mission et préparer la passation. Jessy, tu auras le destin de l'humanité entre les mains. Tu crois pouvoir tenir ?"
    j "Je tiendrai. Et je prendrai des gens capables de me dire quand je fais n'importe quoi."
    mi "Bien. Après mon discours, j'irai dire au revoir à mes femmes."
    t "Nous partons dans vingt-sept jours. Tu as le temps."
    mi "Ça va prendre beaucoup de temps."
    j "Si Alex était là, il dirait : je veux pas savoir."
    a "Oui... Il dirait ça."
    systeme "Un silence passe entre les fauteuils. Personne ne cherche à le chasser."
    s "Je vais rouler un peu. Avant qu'on mette ma voiture en orbite."
    hide micka
    show theo ilonanium laplage at ilonanium_left
    with dissolve
    t "Rendez-vous dans vingt-sept jours. Place d'armes du Capitole. Venez seulement si vous voulez toujours partir."
    systeme "Ils se lèvent. Un à un, les fauteuils se vident."
    scene bg ilonanium conseil
    show jessy ilonanium priest_determined at ilonanium_center
    with Dissolve(1.5)
    systeme "Jessy récupère les plans. Il reste un instant seul devant le calendrier."
    jump ending_ilonanium_adieux


# 11. LES ADIEUX
label ending_ilonanium_adieux:
    $ ilonanium_music_stop(2.0)
    scene black with fade
    centered "VINGT-SEPT JOURS PLUS TARD"
    scene bg ilonanium capitole with fade
    $ ilonanium_bed("crowd", level=0.75)
    $ ilonanium_music("hope", level=0.64, fadein=2.0)
    systeme "La place d'armes déborde jusque dans les rues voisines. Des bannières passent au-dessus de la foule. Une parade s'immobilise devant les marches du Capitole."
    systeme "Théo, Allan, Micka, Sofiane et Florentin se retrouvent autour de Jessy. Ils n'ont que quelques sacs."
    show micka ilonanium governor at ilonanium_left
    show allan ilonanium ceo_supportive at ilonanium_right
    with dissolve
    mi "Il fallait bien qu'on parte en grande pompe."
    a "Tu as fait imprimer ton visage sur les deux côtés des drapeaux."
    mi "Pour les gens derrière."
    show sofiane ilonanium civilian_smirk at ilonanium_center with dissolve
    s "Ma voiture est au laboratoire. J'ai laissé les consignes sur le siège."
    a "Le dossier de huit cents pages ?"
    s "Les consignes courtes."
    hide micka
    hide sofiane
    show florentin ilonanium armor_resolved at ilonanium_left
    with dissolve
    ilonanium_florentin "La relève a reçu ses ordres. On peut partir."
    hide florentin
    hide allan
    show theo ilonanium laplage at ilonanium_left
    show jessy ilonanium priest_emotional at ilonanium_right
    with dissolve
    systeme "Théo se tourne vers Jessy. Pendant une seconde, ni l'un ni l'autre ne trouve quoi faire de ses mains."
    $ ilonanium_music_stop(1.0)
    $ ilonanium_bed_level(0.20, seconds=0.8)
    scene cg ilonanium calin with Dissolve(1.5)
    systeme "Puis ils se prennent dans les bras."
    t "Pour toi, mille ans. Pour nous, quelques secondes."
    j "Alors faites-le bien. J'aurai le temps de vous juger."
    scene bg ilonanium capitole
    show theo ilonanium laplage at ilonanium_left
    show jessy ilonanium priest_emotional at ilonanium_right
    with dissolve
    systeme "Allan les rejoint. Puis les autres. La foule continue d'acclamer quelque chose qu'ils n'entendent plus très bien."
    t "C'est l'heure."
    systeme "Théo détache le porte-clés de son manteau. Pour la première fois, il essaie d'appeler le TARDIS."
    $ ilonanium_effect("arrival", level=0.80)
    systeme "Il serre le creeper dans sa main. Un grondement monte entre les acclamations. La cabine bleue se dessine sur les dalles, d'abord transparente, puis bien réelle."
    systeme "Théo reste un instant immobile devant elle, puis pose la main sur la porte. La serrure cède."
    t "Il m'a reconnu."
    j "On vous accueillera avec le TAIKUN. Moi et l'humanité."
    t "Merci, Jessy."
    systeme "Les cinq voyageurs montent dans le TARDIS. Avant de refermer la porte, ils se tournent une dernière fois vers Jessy."
    # Les cinq voyageurs sont dans la cabine ; Jessy reste sur la place.
    scene cg ilonanium depart tardis with Dissolve(1.5)
    systeme "Théo lève le pouce. Allan, Micka, Sofiane et Florentin adressent un dernier signe à Jessy. Il leur répond, un sourire tremblant aux lèvres."
    window hide dissolve
    $ renpy.pause(2.0)
    $ ilonanium_bed_stop(seconds=2.0)
    scene black with Dissolve(2.0)
    window auto
    $ ilonanium_effect("departure", level=0.75)
    systeme "La porte se referme. Jessy reste sur la place jusqu'à ce que la cabine disparaisse."
    # Un clic rapide ne coupe plus le depart avant le carton temporel.
    $ ilonanium_wait_audio(6.2, channel="ilon_machine")
    jump ending_ilonanium_promesse


# 12. LA PROMESSE TENUE
label ending_ilonanium_promesse:
    $ ilonanium_silence(0.0)
    centered "NEUF CENT QUATRE-VINGT-DIX-NEUF ANS PLUS TARD"
    scene bg ilonanium retour with Dissolve(2.0)
    $ ilonanium_music_stop(0.0)
    $ ilonanium_bed("crowd", level=0.85, fade=2.0)
    $ ilonanium_effect("arrival", level=0.45)
    systeme "Allan sort le premier du TARDIS. À l'intérieur, le voyage a duré quelques instants. Sur la place, neuf cent quatre-vingt-dix-neuf ans ont passé."
    show allan ilonanium ceo at ilonanium_left
    show micka ilonanium governor at ilonanium_right
    with dissolve
    systeme "La place est immense. Des parades s'étendent jusqu'à l'horizon. Sur les façades, le même symbole : un pouce levé."
    "La foule" "La prophétie s'est réalisée ! Le Messi et ses apôtres sont là !"
    "Une voix" "Ça doit être lui, l'apôtre Micka ! Marie-moi !"
    mi "L'humanité a gardé ses priorités."
    $ ilonanium_bed_level(0.22, seconds=1.0)
    systeme "Devant eux, un homme en robe blanche attend. Une longue barbe lui descend sur la poitrine. Ses yeux n'ont pas changé."
    hide allan
    hide micka
    show jessy ilonanium prophet_emotional at ilonanium_center
    with dissolve
    t "Jessy ?"
    j "Vous avez mis le temps."
    show allan ilonanium ceo_supportive at ilonanium_left
    show jessy ilonanium prophet_emotional at ilonanium_center
    show micka ilonanium governor_emotional at ilonanium_right
    with dissolve
    $ ilonanium_music("reprise_wait", level=0.85, fadein=2.0)
    systeme "Allan ouvre la bouche, puis serre Jessy contre lui sans rien dire. Micka regarde au-dessus de son épaule. Son sourire s'efface, remplacé par autre chose."
    mi "Levez les yeux."
    $ ilonanium_music("reprise", level=0.75, fadein=2.0, fadeout=2.0)
    scene bg ilonanium taikun with Dissolve(2.0)
    systeme "Dans le ciel, une arche dessine un gigantesque anneau de métal. Des lumières courent sur sa coque. Même depuis le sol, on distingue ses structures concentriques. Le TAIKUN est en orbite."
    show theo ilonanium laplage_emotional at ilonanium_left
    show jessy ilonanium prophet_emotional at ilonanium_center
    show allan ilonanium ceo_supportive at ilonanium_right
    with dissolve
    a "Ils l'ont construit."
    j "Ils l'ont construit. Réparé. Agrandi. Parfois presque abandonné. Puis repris. J'ai beaucoup d'histoires à vous raconter."
    t "J'y crois pas. Tu as vraiment réussi."
    systeme "Jessy passe une main dans sa barbe. Sa main tremble un peu."
    $ ilonanium_music_level(0.48, 1.2)
    j "J'ai gardé vos chambres. J'avais oublié le bruit de vos voix quand vous êtes tous ensemble."
    hide allan
    show sofiane ilonanium civilian_smirk at ilonanium_right
    with dissolve
    s "Et le moteur ?"
    j "Il attend son conducteur."
    hide sofiane
    show florentin ilonanium armor_resolved at ilonanium_right
    with dissolve
    ilonanium_florentin "Et la relève ?"
    j "Ils vous attendent à bord. Ils connaissent tous ton nom."
    systeme "Théo pose sa main sur l'épaule de Jessy. Cette fois, il n'est plus question de repartir sans lui."
    j "Ravi de vous revoir, les amis. Le TAIKUN nous attend."
    $ ilonanium_bed_stop(seconds=2.0)
    $ ilonanium_music_stop(3.0)
    scene black with fade
    systeme "Ils embarquent à bord du TAIKUN. Après les derniers essais et préparatifs, l'arche quitte l'exoplanète. La traversée vers l'Ilonanium dure cinq ans."
    jump ending_ilonanium_reconquete


# 13. LA RECONQUETE
label ending_ilonanium_reconquete:
    centered "MILLE QUARANTE-QUATRE ANS APRÈS LA CATASTROPHE"
    scene bg ilonanium astre with Dissolve(2.0)
    $ ilonanium_bed("gravity", level=0.35, channel="ilon_texture", fade=2.0)
    systeme "L'Ilonanium tourne dans le vide. Des nuages couvrent ses reliefs. Sous eux, quelque part, se trouve ce qu'il reste de la Terre."
    $ ilonanium_music("vanir", level=0.78, fadein=0.8)
    $ ilonanium_bed_stop(channel="ilon_texture", seconds=2.0)
    scene bg ilonanium reconquete with Dissolve(2.0)
    systeme "Une lumière fend l'espace. Après cinq ans de traversée, l'arche de l'humanité ralentit devant le monde qui a englouti son berceau. Mille quarante-quatre ans après la catastrophe, les exilés sont revenus."
    $ ilonanium_bed("ship", level=0.45)
    $ ilonanium_bed("engine", level=0.32, channel="ilon_machine")
    scene bg ilonanium passerelle with fade
    systeme "Sur la passerelle du TAIKUN, six silhouettes font face à la baie. Aucun écran ne suffit à contenir l'astre."
    show jessy ilonanium prophet_determined at ilonanium_left
    show florentin ilonanium armor_resolved at ilonanium_right
    with dissolve
    j "Ilona. Je t'entends. Cette fois, je suis là."
    ilonanium_florentin "Les troupes sont prêtes. Cette fois, on ne laissera personne derrière."
    hide jessy
    show sofiane ilonanium armor_focused at ilonanium_left
    with dissolve
    s "Trajectoire stabilisée. Au bout de toutes les routes, il fallait bien qu'il y en ait une pour rentrer."
    hide florentin
    show micka ilonanium armor_commanding at ilonanium_right
    with dissolve
    mi "À tous les ponts : ici Micka. Aujourd'hui, l'humanité retrouve son horizon."
    hide sofiane
    show allan ilonanium commander at ilonanium_left
    with dissolve
    a "Gringos Industry vous remercie d'avoir voyagé à bord. Maintenant, évitez de casser mille ans de travail au premier virage."
    hide micka
    show theo ilonanium laplage_determined at ilonanium_right
    with dissolve
    $ ilonanium_music_level(0.92, 1.2)
    scene cg ilonanium reconquete espoir with Dissolve(1.8)
    t "Nous sommes venus chercher ceux qu'on a perdus. Tous les postes, préparez-vous : c'est l'heure de la bataille de reconquête du berceau de l'humanité."
    window hide dissolve
    # Laisser respirer le groupe reuni avant l'epilogue, sans calage musical.
    $ renpy.pause(3.0)
    $ ilonanium_music_stop(2.5)
    $ ilonanium_bed_stop(seconds=2.5)
    $ ilonanium_bed_stop(channel="ilon_machine", seconds=2.5)
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    window auto
    jump ending_ilonanium_alexandre


# 14. QUELQUE PART SUR L'ILONANIUM...
label ending_ilonanium_alexandre:
    $ ilonanium_silence(0.0)
    systeme "Quelque part sur l'Ilonanium..."
    scene bg ilonanium maison alex with fade
    systeme "Une maison tient debout au milieu des champs. Au soleil couchant, la fumée monte encore de sa cheminée."
    scene bg ilonanium alex with dissolve
    systeme "À l'abri de son toit de chaume, Alexandre contemple l'horizon, une main posée sur sa canne."
    x "N'est-ce pas magnifique ?"
    window hide
    # Extrait monte : attaque du groupe exactement 3.0 s apres le depart.
    $ ilonanium_music("roundabout", level=0.85, fadein=0.04, fadeout=0.0, loop=False)
    $ ilonanium_wait_music(3.0)
    show bg ilonanium alex at ilonanium_jojo_sepia
    show screen ilonanium_to_be_continued
    $ renpy.pause(3.0, hard=True)
    hide screen ilonanium_to_be_continued
    scene black with fade
    $ ilonanium_music_level(0.65, 1.5)
    centered "SPECIAL ENDING\n\nILONANIUM{w=3.0}{nw}"
    centered "[config.name!t]\n\nLe berceau de l'humanité{w=3.0}{nw}"
    centered "Avec\n\nIlona et Jessy\nThéo et Monsieur Laplage\nAllan, Micka, Sofiane et Florentin\n\nEt Alexandre. Toujours là.{w=4.0}{nw}"
    centered "Musique\n\nMajula — DARK SOULS II{w=3.0}{nw}"
    centered "Reprise — Joe Hisaishi\nLe Voyage de Chihiro{w=3.0}{nw}"
    centered "Rippling heartbeat — Kamaboko Sachiko\nSubwoofer Lullaby — C418{w=3.0}{nw}"
    if renpy.loadable("audio/music/ilonanium_across_the_void.ogg"):
        centered "Across the Void — IXION{w=2.5}{nw}"
    if renpy.loadable("audio/music/ilonanium_vanirs_legacy.ogg"):
        centered "Vanir's Legacy — IXION{w=2.5}{nw}"
    if renpy.loadable("audio/music/ilonanium_roundabout.ogg"):
        centered "Roundabout — Yes{w=2.5}{nw}"
    centered "Effets sonores\n\nBrian Hodgson — TARDIS\npeepholecircus · wjb_88 · laft2k\nVlatko Blažek — Varaždin, Croatia\nfreesound.org/people/VlatkoBlazek/\nvlatkoblazek@gmail.com{w=4.0}{nw}"
    centered "Merci d'avoir fait tout ce chemin."
    $ ilonanium_silence(2.0)
    stop ambiant1 fadeout 1.0
    scene black with Dissolve(2.0)
    $ ilonanium_silence(0.0)
    return
