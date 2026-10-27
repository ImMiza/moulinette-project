# Audio local a la fin Ilonanium. Masters mesures, niveaux relatifs par scene.
# Les canaux utilisent les curseurs music/sfx existants et suivent les sauvegardes.
default ilonanium_music_channel = "ilon_music_a"
default ilonanium_music_cue = ""

init -4 python:
    for _ilon_channel in ("ilon_music_a", "ilon_music_b"):
        renpy.music.register_channel(_ilon_channel, mixer="music", loop=True)
    for _ilon_channel in ("ilon_place", "ilon_texture", "ilon_machine"):
        renpy.music.register_channel(_ilon_channel, mixer="sfx", loop=True, tight=True)
    for _ilon_channel in ("ilon_spot", "ilon_detail"):
        renpy.music.register_channel(_ilon_channel, mixer="sfx", loop=False)

    ILONANIUM_MUSIC = {
        "home": ("audio/music/Subwoofer-Lullaby.ogg", 1.0927),
        "tension": ("audio/music/tense-piano.ogg", 1.0292),
        "majula": ("audio/music/Majula.ogg", 1.05317),
        "hope": ("audio/music/spring-hope.ogg", 0.98288),
        "aftermath": ("audio/music/the-sunset.ogg", 0.98969),
        "bar": ("audio/music/bar_jazzy.ogg", 1.02094),
        "plan": ("audio/music/truth-piano.ogg", 0.9594),
        "promise": ("audio/music/melancolique-piano.ogg", 0.96939),
        "across": ("audio/music/ilonanium_across_the_void.ogg", 1.0),
        "vanir": ("audio/music/ilonanium_vanirs_legacy.ogg", 1.0),
        "reprise_wait": ("audio/music/ilonanium_reprise_attente.ogg", 1.0),
        "reprise": ("audio/music/ilonanium_reprise_retrouvailles.ogg", 1.0),
        "roundabout": ("audio/music/ilonanium_roundabout_cue.ogg", 1.0),
    }
    ILONANIUM_SFX = {
        "phone": "audio/fx/ilonanium_phone_vibration.ogg",
        "call": "audio/fx/ilonanium_phone_call.ogg",
        "glass": "audio/fx/ilonanium_glass_scrape.ogg",
        "crack": "audio/fx/ilonanium_wood_crack.ogg",
        "arrival": "audio/fx/ilonanium_tardis_arrival.ogg",
        "departure": "audio/fx/ilonanium_tardis_departure.ogg",
        "failure": "audio/fx/ilonanium_power_down.ogg",
        "ilona": "audio/fx/ilonanium_ilona_link.ogg",
        "transfer": "audio/fx/ilonanium_power_transfer.ogg",
        "laplage": "audio/fx/ilonanium_laplage_arrival.ogg",
        "debris": "audio/fx/ilonanium_debris.ogg",
        "steps": "audio/fx/ilonanium_sand_steps.ogg",
    }
    ILONANIUM_BEDS = {
        "street": "audio/ambience/ilonanium_street.ogg",
        "ocean": "audio/ambience/ilonanium_ocean.ogg",
        "crowd": "audio/ambience/ilonanium_crowd.ogg",
        "wood": "audio/ambience/ilonanium_wood_stress.ogg",
        "gravity": "audio/ambience/ilonanium_gravity.ogg",
        "ship": "audio/ambience/ilonanium_ship.ogg",
        "engine": "audio/ambience/ilonanium_taikun_engine.ogg",
    }

    def ilonanium_music(cue, level=0.8, fadein=1.5, fadeout=1.0, loop=True):
        old = store.ilonanium_music_channel
        new = "ilon_music_b" if old == "ilon_music_a" else "ilon_music_a"
        filename, gain = ILONANIUM_MUSIC[cue]
        renpy.music.stop(channel=new, fadeout=0)
        renpy.music.set_volume(level, delay=0, channel=new)
        renpy.music.play(filename, channel=new, loop=loop, fadeout=0,
            fadein=fadein, relative_volume=gain)
        renpy.music.stop(channel=old, fadeout=fadeout)
        store.ilonanium_music_channel = new
        store.ilonanium_music_cue = cue

    def ilonanium_music_level(level, seconds=0.8):
        renpy.music.set_volume(level, delay=seconds, channel=store.ilonanium_music_channel)

    def ilonanium_music_stop(seconds=1.0):
        for channel in ("ilon_music_a", "ilon_music_b"):
            renpy.music.stop(channel=channel, fadeout=seconds)
        store.ilonanium_music_cue = ""

    def ilonanium_bed(cue, level=0.7, channel="ilon_place", fade=1.0):
        # Garder la phase d'un ressac ou d'une foule deja en cours.
        delay = fade if renpy.music.get_playing(channel=channel) else 0
        renpy.music.set_volume(level, delay=delay, channel=channel)
        renpy.music.play(ILONANIUM_BEDS[cue], channel=channel, loop=True,
            fadeout=fade, fadein=fade, relative_volume=1.0, if_changed=True)

    def ilonanium_bed_stop(channel="ilon_place", seconds=1.0):
        renpy.music.stop(channel=channel, fadeout=seconds)

    def ilonanium_bed_level(level, channel="ilon_place", seconds=0.8):
        renpy.music.set_volume(level, delay=seconds, channel=channel)

    def ilonanium_effect(cue, level=0.8, channel=None):
        # Les machines ne doivent pas couper le verre, le bois ou les debris.
        if channel is None:
            channel = "ilon_machine" if cue in ("arrival", "departure", "failure") else "ilon_spot"
        renpy.music.set_volume(level, delay=0, channel=channel)
        renpy.music.play(ILONANIUM_SFX[cue], channel=channel, loop=False,
            fadeout=0.04, relative_volume=1.0)

    def ilonanium_effect_stop(seconds=0.15, channel="ilon_spot"):
        renpy.music.stop(channel=channel, fadeout=seconds)

    def ilonanium_silence(seconds=0.0):
        ilonanium_music_stop(seconds)
        for channel in ("ilon_place", "ilon_texture", "ilon_machine", "ilon_spot", "ilon_detail"):
            renpy.music.stop(channel=channel, fadeout=seconds)

    def ilonanium_wait_audio(position, channel, clock_fallback=False):
        # Attendre seulement la partie qui reste, meme si le joueur lit vite.
        import time
        if renpy.is_skipping():
            return
        renpy.music.pump()
        started = time.monotonic()
        while not renpy.is_skipping():
            clock = time.monotonic() - started
            elapsed = renpy.music.get_pos(channel=channel)
            if elapsed is None:
                # Un effet termine pendant la lecture n'impose pas une nouvelle attente.
                if not clock_fallback and not renpy.music.get_playing(channel=channel):
                    break
                elapsed = clock
            if elapsed >= position or clock >= position + 1.0:
                break
            renpy.pause(min(0.1, position - elapsed), hard=True)

    def ilonanium_wait_music(position):
        # Le riff est monte a 3.0 s dans le cue, pas dans la piste album.
        ilonanium_wait_audio(position, channel=store.ilonanium_music_channel, clock_fallback=True)

    # Nettoyer aussi un retour volontaire au menu pendant une scene.
    def ilonanium_menu_audio_reset(name, abnormal):
        if name in ("_main_menu", "main_menu_screen"):
            ilonanium_silence(0.0)

    config.label_callbacks.append(ilonanium_menu_audio_reset)
