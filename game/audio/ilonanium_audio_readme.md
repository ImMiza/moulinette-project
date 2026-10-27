**Ilonanium — audio integre le 27 octobre 2026**

Les dix sources deposees dans `audio/to_work` produisent 27 fichiers OGG Vorbis stereo, 48 kHz. Tous les noms suivent `lowercase_underscore`. Les masters et les extraits destines au montage ont des noms distincts. Le manifeste JSON contient la provenance, les empreintes, les durees et les mesures apres encodage.

**Niveaux**

Les nouvelles musiques visent environ -20 LUFS integres ; Reprise conserve une reserve de crete, autour de -21 LUFS. Le gain est constant, sans compression dynamique supplementaire. Les ambiances visent environ -29 a -32 LUFS ; certaines restent plus basses pour proteger leurs transitoires. Les effets courts sont ajustes individuellement, avec reserves de crete et niveaux par scene. Les fichiers deja partages par les autres arcs sont calibres dans le controleur de cette fin par un gain local.

**Declenchements**

- Quotidien : Subwoofer Lullaby ; meme vibration de telephone aux deux premieres scenes.
- Chambre et catastrophe : verre, gravite, bois ; les grincements s'effacent en 0.8 s avant le dialogue avec Laplage, puis des l'entree du plan de sauvetage. Across The Void entre au plan de la maison. Le ressac remplace les bruits de destruction au refuge.
- Laissez digerer : fondu de tous les canaux sur 1.2 s apres la question de Jessy, pendant la pause conservee de 1.5 s ; reponse a sec.
- Plage quarante ans plus tard : ressac et Majula ; retrait de la musique pendant l'aveu de Laplage.
- Bilan des quarante ans : the-sunset.ogg, deja utilise au bivouac de la randonnee, remplace spring-hope.ogg ; Majula reste sur la plage precedente.
- Conseil : entree du piano au projet TAIKUN, retrait pendant le conflit ; silence sur Je monte pas dans le TARDIS, puis piano des J'ai peur de rester, avant le soutien des amis.
- Adieux : foule attenuee au calin ; TARDIS a l'appel de Theo et au depart.
- Retrouvailles : apparition de Jessy sans musique ; tenue de Reprise a l'etreinte, ouverture distincte a la revelation du TAIKUN.
- Reconquete : Vanir's Legacy au vaisseau devant l'astre ; ambiance de passerelle et trace transformee de l'AE86.
- Alexandre : lecture libre sans musique ; Roundabout demarre a la fermeture de sa replique. L'accent repere dans le master fourni est a **45.440 s** ; le cue commence a **42.440 s**. La fleche et le sepia attendent **3.000 s de lecture audio**. Un repli temporel gere le son coupe ; le mode passer reste utilisable.
- Retour au menu : arret explicite des sept canaux locaux.

**TARDIS**

Le master complet fourni dure 85.240 s. Le depart utilise un montage de 6.2 s. L'arrivee est un montage inverse de cette meme source de takeoff ; il ne s'agit pas d'un enregistrement BBC d'atterrissage distinct. Les deux sons mecaniques provisoires crees avant reception du TARDIS ont ete remplaces.

**Controleur et tests**

`arcs/endings/ending_ilonanium_audio.rpy` centralise les ressources, niveaux et fondus. Deux canaux sur le melangeur `music` permettent les chevauchements ; trois lits de lieu/matiere/moteur et deux canaux ponctuels utilisent `sfx`. Les reglages musique et effets du joueur restent applicables.

`tests/ilonanium.rpy` parcourt les images et les deux relations. Il suit le declenchement automatique actuellement ecrit dans l'arc 7. `tests/ilonanium_audio.rpy` controle les silences, les entrees de musique, le repere de la fleche et le nettoyage final. Commandes SDK sur une copie isolee : `renpy.py <projet> lint` puis `renpy.py <projet> test global --report-detailed`.

**Sources et credits**

- Across The Void et Vanir's Legacy : Guillaume David, IXION, Kasedo Games.
- Reprise : Joe Hisaishi, version du fichier fourni.
- Roundabout : Yes, master intitule Original 1971 fourni.
- TARDIS Takeoff 1963 : Brian Hodgson / BBC Radiophonic Workshop.
- Power Down et Sc-Fi ship background sound : [peepholecircus](https://freesound.org/people/peepholecircus/).
- Scraping_Glass : [wjb_88](https://freesound.org/people/wjb_88/sounds/828862/).
- Wood Creaking : [laft2k, publication Pixabay](https://pixabay.com/sound-effects/household-wood-creaking-30692/).
- Cell Phone Vibration : [Vlatko Blazek](https://freesound.org/people/VlatkoBlazek/sounds/187600/), Varazdin, Croatia ; contact publie : vlatkoblazek@gmail.com. Attribution egalement au generique.
- Rippling heartbeat : Kamaboko Sachiko ; Subwoofer Lullaby : C418 ; Majula : Dark Souls II.
- Les textures de gravite, lien d'Ilona, transmission, moteur et telephone sont des montages/traitements des sources indiquees dans le manifeste, ou une synthese neutre de retour d'appel.

**Mesures apres encodage**

| Fichier | Duree | LUFS integres | Crete vraie dBTP |
|---|---:|---:|---:|
| `audio/music/ilonanium_across_the_void.ogg` | 260.813 s | -20.01 | -11.21 |
| `audio/music/ilonanium_vanirs_legacy.ogg` | 271.433 s | -20.08 | -11.31 |
| `audio/music/ilonanium_reprise.ogg` | 285.733 s | -20.96 | -2.75 |
| `audio/music/ilonanium_roundabout.ogg` | 516.110 s | -20.15 | -8.72 |
| `audio/music/ilonanium_roundabout_cue.ogg` | 473.670 s | -20.15 | -8.95 |
| `audio/music/ilonanium_reprise_attente.ogg` | 15.250 s | -25.03 | -12.03 |
| `audio/music/ilonanium_reprise_retrouvailles.ogg` | 219.733 s | -20.28 | -2.75 |
| `audio/ambience/ilonanium_ocean.ogg` | 70.208 s | -29.30 | -11.31 |
| `audio/ambience/ilonanium_crowd.ogg` | 63.392 s | -29.64 | -10.90 |
| `audio/ambience/ilonanium_street.ogg` | 21.464 s | -32.41 | -20.25 |
| `audio/ambience/ilonanium_ship.ogg` | 34.683 s | -28.99 | -21.20 |
| `audio/ambience/ilonanium_wood_stress.ogg` | 59.480 s | -33.06 | -10.19 |
| `audio/fx/ilonanium_wood_crack.ogg` | 2.500 s | -28.24 | -8.03 |
| `audio/fx/ilonanium_phone_vibration.ogg` | 0.680 s | -26.95 | -21.52 |
| `audio/fx/ilonanium_glass_scrape.ogg` | 3.189 s | -30.14 | -10.13 |
| `audio/fx/ilonanium_power_down.ogg` | 4.415 s | -22.95 | -16.62 |
| `audio/fx/ilonanium_ilona_link.ogg` | 1.402 s | -30.09 | -14.59 |
| `audio/fx/ilonanium_power_transfer.ogg` | 1.990 s | -28.39 | -12.40 |
| `audio/ambience/ilonanium_gravity.ogg` | 23.000 s | -30.96 | -20.17 |
| `audio/ambience/ilonanium_taikun_engine.ogg` | 23.000 s | -29.00 | -15.50 |
| `audio/fx/ilonanium_laplage_arrival.ogg` | 1.515 s | -25.03 | -13.80 |
| `audio/fx/ilonanium_debris.ogg` | 2.088 s | -25.15 | -11.48 |
| `audio/fx/ilonanium_sand_steps.ogg` | 1.437 s | -34.88 | -12.09 |
| `audio/fx/ilonanium_phone_call.ogg` | 2.400 s | -27.94 | -22.43 |
| `audio/fx/ilonanium_tardis_takeoff.ogg` | 85.240 s | -23.34 | -15.05 |
| `audio/fx/ilonanium_tardis_departure.ogg` | 6.200 s | -25.25 | -9.14 |
| `audio/fx/ilonanium_tardis_arrival.ogg` | 6.200 s | -24.02 | -13.14 |
