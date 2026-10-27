# Depuis le SDK : lib/py3-windows-x86_64/python.exe renpy.py <projet> test ilonanium
# Executer sur une copie isolee : Ren'Py utilise aussi game/saves.
# RENPY_PATH_TO_SAVES permet en plus d'isoler les sauvegardes et backups utilisateur.
testsuite global:
    teardown:
        exit

testcase ilonanium:
    parameter relation = ["amour", "amitie"]
    $ _test.transition_timeout = 0.05
    $ _preferences.skip_unseen = True
    $ _preferences.text_cps = 0
    advance until screen "main_menu" timeout 15
    run Start()
    $ store.arc7_jessy_relation = relation
    $ store.arc7_jessy_fruit = "goute"
    $ store.ilonanium_points = 6
    run Jump("arc_7_jessy_scene_8")
    # Le declenchement actuel est automatique apres les six aliments.
    skip until "Je vais pas jouer ce soir." timeout 30
    if eval (relation == "amour"):
        skip until "Premier rendez-vous après la randonnée" timeout 30
    else:
        skip until "Et c'est pas une excuse" timeout 30
    # Verifier les plans affiches, y compris l'absence de sprites sur les CG peints.
    skip until eval (renpy.showing("cg ilonanium attraction")) timeout 60
    assert eval (not any(renpy.showing(tag) for tag in ("jessy", "ilona", "laplage")))
    skip until eval (renpy.showing("cg ilonanium gravite")) timeout 30
    skip until eval (renpy.showing("cg ilonanium laplage")) timeout 30
    skip until eval (renpy.showing("cg ilonanium echec")) timeout 30
    skip until eval (renpy.showing("cg ilonanium adieu")) timeout 30
    skip until eval (renpy.showing("cg ilonanium maison")) timeout 30
    skip until eval (renpy.showing("cg ilonanium arrachement")) timeout 30
    skip until eval (renpy.showing("cg ilonanium catastrophe")) timeout 30
    skip until eval (renpy.showing("cg ilonanium sauvetage")) timeout 30
    assert eval (not any(renpy.showing(tag) for tag in ("jessy", "ilona", "laplage")))
    skip until eval (renpy.showing("cg ilonanium terre")) timeout 30
    skip until eval (renpy.showing("cg ilonanium naissance astre")) timeout 30
    skip until eval (renpy.showing("bg ilonanium astre")) timeout 30
    assert eval (not any(renpy.showing(tag) for tag in ("jessy", "ilona", "laplage")))
    assert eval (arc7_jessy_relation == relation and ilonanium_points == 6)
    # La suite et le carton final sont verifies, pour les deux relations,
    # dans ilonanium_audio. Ce parcours garde l'entree et tous les CG peints.
    run MainMenu(confirm=False)
    pause until screen "main_menu" timeout 15
    assert eval (not any(renpy.music.get_playing(channel=c) for c in ("ilon_music_a", "ilon_music_b", "ilon_place", "ilon_texture", "ilon_machine", "ilon_spot", "ilon_detail")))
