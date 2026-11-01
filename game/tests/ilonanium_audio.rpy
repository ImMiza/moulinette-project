# Verification des entrees musicales et des respirations, sur copie isolee.
testcase ilonanium_audio:
    parameter relation = ["amour", "amitie"]
    $ _test.transition_timeout = 0.05
    $ _preferences.skip_unseen = True
    advance until screen "main_menu" timeout 15
    run Start()
    $ store.arc7_jessy_relation = relation
    $ store.ilonanium_points = 6
    run Jump("ending_ilonanium")
    skip until "Je vais pas jouer ce soir." timeout 30
    assert eval (ilonanium_music_cue == "home")
    skip until "Il prépare à manger. Revient devant son téléphone." timeout 30
    $ renpy.stop_skipping()
    advance until "Lance un appel." timeout 10
    $ _ilon_call_started = __import__("time").monotonic()
    advance until "Votre correspondant n'est pas disponible." timeout 10
    assert eval (__import__("time").monotonic() - _ilon_call_started >= 1.9)
    assert eval (renpy.music.get_playing(channel="ilon_detail") is None)
    skip until "Je crois que ça va pas." timeout 30
    $ renpy.stop_skipping()
    advance until "Il rappelle tout de suite. Une sonnerie. Deux." timeout 10
    pause 2.6
    $ _ilon_call_finished = __import__("time").monotonic()
    advance until "La messagerie." timeout 5
    assert eval (__import__("time").monotonic() - _ilon_call_finished < 1.0)
    skip until "Pour vous faire sortir, oui." timeout 60
    $ renpy.stop_skipping()
    pause 0.9
    assert eval (renpy.music.get_playing(channel="ilon_place") is None)
    skip until "Laplage saisit Jessy par l'épaule" timeout 30
    assert eval (renpy.music.get_playing(channel="ilon_machine") is None)
    skip until "Des immeubles et leurs habitants." timeout 30
    $ renpy.stop_skipping()
    pause 0.9
    assert eval (renpy.music.get_playing(channel="ilon_place") is None)
    skip until "Monsieur Laplage, on fait quoi ?" timeout 60
    $ renpy.stop_skipping()
    advance until "Laissez digérer." timeout 10
    assert eval (ilonanium_music_cue == "")
    assert eval (not any(renpy.music.get_playing(channel=c) for c in ("ilon_music_a", "ilon_music_b", "ilon_place", "ilon_texture", "ilon_machine", "ilon_spot", "ilon_detail")))
    skip until "Quarante ans. Et je reviens toujours" timeout 45
    $ renpy.stop_skipping()
    pause 0.35
    $ _ilon_ocean_pos = renpy.music.get_pos(channel="ilon_place")
    $ ilonanium_bed("ocean", level=0.72, fade=0.2)
    pause 0.35
    assert eval (_ilon_ocean_pos is not None and renpy.music.get_pos(channel="ilon_place") > _ilon_ocean_pos + 0.15)
    skip until "Quarante ans après la catastrophe, des villes" timeout 90
    assert eval (ilonanium_music_cue == "aftermath")
    skip until "Je monte pas dans le TARDIS." timeout 90
    assert eval (ilonanium_music_cue == "")
    skip until "J'ai peur de rester." timeout 30
    assert eval (ilonanium_music_cue == "promise")
    skip until "On te laisse pas seulement une promesse." timeout 30
    assert eval (ilonanium_music_cue == "promise")
    skip until "Merci, Jessy." timeout 60
    $ renpy.stop_skipping()
    advance until "La porte se referme. Jessy reste sur la place" timeout 15
    pause 0.2
    assert eval (renpy.music.get_playing(channel="ilon_machine") == ILONANIUM_SFX["departure"])
    $ _ilon_depart_started = __import__("time").monotonic()
    advance until "NEUF CENT QUATRE-VINGT-DIX-NEUF ANS PLUS TARD" timeout 12
    assert eval (__import__("time").monotonic() - _ilon_depart_started >= 5.5)
    assert eval (renpy.music.get_playing(channel="ilon_machine") is None)
    skip until "Vous avez mis le temps." timeout 60
    assert eval (ilonanium_music_cue == "")
    skip until "Levez les yeux." timeout 30
    assert eval (ilonanium_music_cue == "reprise_wait")
    skip until "Ils l'ont construit." timeout 30
    assert eval (ilonanium_music_cue == "reprise")
    skip until "Ilona. Je t'entends." timeout 45
    assert eval (ilonanium_music_cue == "vanir")
    skip until "N'est-ce pas magnifique ?" timeout 30
    assert eval (ilonanium_music_cue == "")
    $ renpy.stop_skipping()
    keysym "dismiss"
    pause until screen "ilonanium_to_be_continued" timeout 15
    assert eval (ilonanium_music_cue == "roundabout")
    assert eval (renpy.showing("bg ilonanium alex") and arc7_jessy_relation == relation and ilonanium_points == 6)
    assert eval (renpy.music.get_pos(channel=ilonanium_music_channel) is None or renpy.music.get_pos(channel=ilonanium_music_channel) >= 2.8)
    skip until screen "main_menu" timeout 45
    assert eval (not any(renpy.music.get_playing(channel=c) for c in ("ilon_music_a", "ilon_music_b", "ilon_place", "ilon_texture", "ilon_machine", "ilon_spot", "ilon_detail")))


# Le repere JoJo doit aussi avancer quand le lecteur coupe le son.
testcase ilonanium_audio_muted:
    $ _test.transition_timeout = 0.05
    $ _preferences.skip_unseen = True
    advance until screen "main_menu" timeout 15
    run Start()
    $ _ilon_muted_music = _preferences.get_mute("music")
    $ _ilon_muted_sfx = _preferences.get_mute("sfx")
    $ _preferences.set_mute("music", True)
    $ _preferences.set_mute("sfx", True)
    run Jump("ending_ilonanium_alexandre")
    skip until "N'est-ce pas magnifique ?" timeout 20
    $ renpy.stop_skipping()
    $ _ilon_muted_started = __import__("time").monotonic()
    keysym "dismiss"
    pause until screen "ilonanium_to_be_continued" timeout 10
    assert eval (2.8 <= __import__("time").monotonic() - _ilon_muted_started < 5.5)
    assert eval (renpy.music.get_pos(channel=ilonanium_music_channel) is None)
    assert eval (renpy.showing("bg ilonanium alex"))
    $ _preferences.set_mute("music", _ilon_muted_music)
    $ _preferences.set_mute("sfx", _ilon_muted_sfx)
    run MainMenu(confirm=False)
    pause until screen "main_menu" timeout 15
    assert eval (not any(renpy.music.get_playing(channel=c) for c in ("ilon_music_a", "ilon_music_b", "ilon_place", "ilon_texture", "ilon_machine", "ilon_spot", "ilon_detail")))
