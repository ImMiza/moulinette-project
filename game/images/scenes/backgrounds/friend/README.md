# Décors de la fin Friend

Créés le 17 octobre 2026 avec l'outil **imagegen intégré**, puis copiés dans le projet. Les sources de génération restent conservées sous `C:/Users/Allan/.codex/generated_images/01a14a1b-64ca-7572-92dd-2c353b1a626c/` et `C:/Users/Allan/.codex/generated_images/01a14a6f-5ef1-79c3-912e-5308c6260c00/`. Aucun ancien décor du jeu n'a été remplacé.

## Fichiers et intégration

| Fichier (depuis `images/scenes/backgrounds/`) | Dimensions | Nom Ren'Py | Source finale |
| --- | --- | --- | --- |
| `friend/bg_friend_chambre_jessy.png` | 1672 × 941 | `bg friend chambre jessy` | `exec-1b654f49-8858-42b5-b2e5-7352b037085b.png` |
| `friend/bg_friend_chambre_ilona.png` | 1671 × 941 | `bg friend chambre ilona` | `exec-66503c32-25c9-4649-95d7-91a1b7b8bc91.png` |
| `friend/bg_friend_appel_alexandre.png` | 1672 × 941 | `bg friend appel` | `exec-c55e34db-8423-484c-a305-f7c85d99402b.png` |
| `friend/bg_friend_discord_cinq.png` | 1672 × 941 | `bg friend discord cinq` | `exec-a858d7de-06e0-43e8-8ac1-0ab1e848c1e7.png` |
| `friend/bg_friend_discord_six.png` | 1672 × 941 | `bg friend discord six` | `exec-08afb128-fc8f-4fab-beab-6e724190275b.png` |
| `friend/bg_friend_appartement_allan.png` | 1672 × 941 | `bg friend appartement` | `exec-bc0ec155-8c19-4f60-80fa-d79d276ec3fc.png` |
| `friend/bg_friend_appartement_allan_repas.png` | 1672 × 941 | `bg friend appartement repas` | `exec-91243e63-ee62-488f-9a7b-7fa499493ad3.png` |
| `friend/bg_friend_gare_matin.png` | 1678 × 937 | `bg friend gare matin` | `exec-0a91a55c-534b-450a-a56e-b4cc71d029f5.png` |
| `friend/bg_friend_promenade_depart.png` | 1672 × 940 | `bg friend promenade depart` | `exec-5477f8dd-9dba-46ba-83fc-f3afb95edfcf.png` |
| `friend/bg_friend_promenade_arrivee.png` | 1672 × 940 | `bg friend promenade arrivee` | `exec-9fb0820f-49a3-4ac7-b6bf-e8cdebf72a25.png` |
| `minecraft/bg_friend_minecraft_trou_ouvert.png` | 1672 × 941 | `bg friend minecraft ouvert` | `exec-5663db33-c390-4d83-b82c-4f291f6d46ee.png` |
| `minecraft/bg_friend_minecraft_trou_ferme.png` | 1672 × 941 | `bg friend minecraft ferme` | `exec-8e57c3f0-50b1-4499-b41a-4c56c5dd0c05.png` |

Les sept décors initiaux sont opaques (RGB), sans personnage intégré. Les deux
images Discord sont également opaques, avec les participants intégrés en cases
vidéo. Ils sont déclarés dans `arcs/endings/ending_friend.rpy` avec
`Transform(..., xysize=(1920, 1080), fit="cover")` pour remplir l'écran en
préservant leurs proportions. Les chambres sont distinctes ; le décor d'appel
représente la pièce d'Alexandre avant et après la vue de groupe. La version à
cinq cases précède l'arrivée de Sofiane ; celle à six cases sert ensuite dans
l'appel et le générique. Alexandre y porte sa variante d'intérieur, également
utilisée comme sprite dans sa chambre. Les deux images Discord et le sprite
viennent de `C:/Users/Allan/.codex/generated_images/01a14a6f-5ef1-79c3-912e-5308c6260c00/`.
Le plafond du trou se referme après la pose du bloc. La table d'Allan se garnit
seulement après l'arrivée de Sofiane et la mise en place des assiettes.
Le quai du matin reprend le cadrage de `transport/bg_arc5_train_station.jpg`
avec ciel et lumière de jour, sans modifier l'image de nuit utilisée ailleurs.
La promenade du départ reprend la lumière et le paysage de
`beach/bg_arc2_beach_sunset.jpg` avec un nouveau point de vue : gare à gauche,
parking à droite. Elle apparaît dès l'arrivée du groupe à la bifurcation.
La promenade de jour reprend la même côte avec un cadrage sur les marches
qui descendent à la plage. Elle accompagne l'arrivée de Théo avant le retour
au décor du parasol.

Les photos de groupe et les apparences adultes sont hors du périmètre de cette série de backgrounds et restent provisoires.

## Références visuelles

Pour l'harmonisation des intérieurs, l'image 1 est la première génération de chaque pièce, l'image 2 est `family/bg_family_maison.jpg`, et l'image 3 est `city/bg_arc5_cafe.jpg`. Les retouches conservent le cadrage et les objets, mais rapprochent les contours, aplats, ombres et textures du dessin des décors existants. La première série, plus photographique, n'est pas utilisée dans le jeu.

Le rendu du trou reprend les volumes cubiques et textures pixelisées observés dans `minecraft/bg_prologue_weird_interior.png`. Sa variante fermée utilise l'image ouverte comme cible pour conserver le cadrage. L'appartement avant repas utilise sa version finale avec repas comme cible de retouche.

## Consignes exactes

### Chambre de Jessy — composition

```text
Use case: illustration-story. Asset type: opaque 16:9 landscape background plate for a French-language Ren'Py visual novel set in contemporary Japan. Generate a finished EMPTY bedroom belonging to Jessy, a young adult who plays Minecraft, in the exact visual vocabulary of a cozy Japanese anime visual-novel background: fine clean dark-brown ink contour lines, gently painterly cel shading, restrained watercolor-like surface texture, warm wood, cream plaster, muted blue and olive fabric, detailed but calm believable architecture. Not photorealistic, not 3D, not pixel art. Eye-level wide interior view from near the doorway. Compact ordinary bedroom: a modest single bed along one wall with rumpled muted-blue bedding, a wooden desk with computer monitor, keyboard and headset, a warm desk lamp, a mug sitting on some loose papers, a small nearby shelf where a phone can be set down, restrained book storage and a wardrobe. No readable writing on papers, no logos. Open walkable floor and uncluttered central space so character sprites can be overlaid at left, center and right; put storytelling objects in the middle-distance, away from the bottom 22 percent reserved for the dialogue box. Late afternoon into early evening, soft cool summer light through a small window and warm desk lamp, quiet lived-in mood, absolutely no dramatic sadness. One cohesive full-frame 1920x1080 or same 16:9 ratio image. No people, no silhouettes, no faces on screen, no poster characters, no speech bubbles, no UI, no borders, no watermark.
```

### Chambre d'Ilona — composition

```text
Use case: illustration-story. Asset type: opaque 16:9 landscape Ren'Py visual-novel background, contemporary Japan. A finished EMPTY modest bedroom and amateur drawing/streaming corner for Ilona, a creative young adult living in her home region, NOT a professional Tokyo studio. Match a cozy hand-drawn Japanese anime background aesthetic: precise thin warm dark contour lines, softly painted cel shading, subtle paper texture, realistic room proportions, warm wood and cream walls, muted sage curtains and a few dusty-rose accents, restrained saturation, detailed legible environment. Wide eye-level view from doorway. A small wooden desk holds ONE ordinary monitor with a softly glowing unreadable screen, inexpensive microphone on short stand, keyboard, small adjustable desk lamp, open sketchbook with simple incomplete whimsical house sketches, eraser and colored pencils; a tea mug is safely away from the desk edge. Adjacent simple single bed with folded pale bedding, a small shelf of notebooks and blank spines. Curtains frame a window with soft late-summer daylight. Cozy practical personal room, no extravagant RGB lighting, no acoustic foam, no studio ring light. Keep central foreground floor clear for overlay character sprites and lower 22 percent visually quiet for the game's dialogue box. Single cohesive image, 1920x1080 or same 16:9 ratio. No people, silhouettes or faces anywhere; no legible text, no logos, no UI panels, no watermark, no collage. Not photoreal, not 3D.
```

### Appels depuis le bureau d'Alexandre — composition

```text
Use case: illustration-story. Asset type: full-frame opaque 16:9 background plate for a Ren'Py visual novel. EMPTY Alexandre's small apartment workroom in contemporary Japan, the recurring backdrop for evening video calls among friends. Cozy hand-drawn anime background with thin precise dark-brown linework, gentle painterly cel shading, subtly textured cream walls, warm wooden furniture, muted navy curtains, warm lamp against cool evening window light. Eye-level wide room view. The middle-distance desk is set up for a casual call: open laptop at a natural slight angle, softly glowing screen with indistinct muted rectangles and NO visible faces, NO readable interface; small webcam, pair of headphones, a drinking glass, scattered marker pens in several greys, an open pad containing nonverbal little architectural sketches. A small shelf with plain books, a modest chair, cool blue curtain and ordinary wall clock without legible lettering. No birthday cake permanently baked into the scenery because this same room is reused for a call days later. Allow unobstructed staging space across foreground for three overlay sprites, keep lower quarter calm. Clearly an illustrated physical room, not a full-screen conferencing UI, not a split screen. No people, no characters, no photos of faces, no logos, no text, no watermark. 1920x1080 preferred or exact 16:9 landscape. Not photorealistic, not 3D.
```

### Appartement d'Allan avec le repas — composition

```text
Use case: illustration-story. Asset type: opaque 16:9 landscape background for a Ren'Py visual novel set in contemporary Japan. Generate the EMPTY modest living/dining room of Allan, now a young adult with his own apartment, ready for three friends sharing takeout on a weekend. Match classic cozy Japanese anime visual-novel background art: delicate precise dark linework, gently painted cel shading, subtle grain, warm brown wood and cream walls, calm muted colors, detailed believable small room, no photorealism and no 3D render. Wide eye-level view from the entrance. A low rectangular dining table has been moved comfortably out of the circulation path; three simple floor cushions or low seats, small two-seat sofa against the wall, modest kitchenette behind, a wooden sideboard with an accessible drawer, ordinary shelf with books and a small power bank resting by its charging cable. A takeout carry bag sits at the table edge, with a few closed plain containers and three empty plates, chopsticks not yet laid out. Soft late-afternoon sunlight through a window with light neutral curtains, no balcony and no lavish furnishings. The room feels welcoming, a little untidy but cared for. Keep central foreground open for overlay sprites, important props not obscured by bottom dialogue box, lower 22 percent simple. Full-frame 1920x1080 or exact 16:9 composition. No people, no silhouettes, no faces, no readable labels, no logos, no game UI, no collage, no watermark.
```

### Harmonisation finale des quatre intérieurs

```text
Use case: style-transfer. Image 1 is the EDIT TARGET, an empty visual-novel room. Image 2 and Image 3 are STYLE REFERENCES from this exact game. Re-render Image 1 to match the hand-drawn background style of Image 2 and Image 3 closely. Preserve Image 1's exact room layout, camera angle, furniture, prop placement, framing, color identities and time of day. Change only the rendering style: clearly visible fine dark-brown drawn outlines around furniture and architectural edges, flatter simplified painted color shapes, delicate cel-shaded shadows, gentle hand-painted texture, matte surfaces and restrained highlights, like the references. Remove photographic depth-of-field blur, glossy floor reflections, tiny hyperreal fabric texture, volumetric bloom and 3D-render appearance. Keep depth through perspective and drawn detail, not photorealistic material rendering. The result should sit seamlessly beside the reference game's old backgrounds, NOT a glossy anime-inspired architectural render. Keep the room empty with no humans, no faces on screens, no readable text, no logos or watermark. One opaque 16:9 landscape background, same framing and resolution as Image 1.
```

### Appartement d'Allan avant le repas — variante finale

```text
Use case: precise-object-edit. Image 1 is the exact edit target, Allan's illustrated apartment. Create the earlier moment immediately BEFORE his friend arrives with the takeout meal. Preserve every architectural line, the camera, framing, lighting, fine drawn anime style, furniture, cushions, books, plants and colors. Only remove the brown paper takeaway bag, the closed food containers and the three plates from the low table, leaving that tabletop completely clear with its same wood grain and perspective. Do not move the table or anything else. This is a continuity background pair: later the existing version will show the meal. No new objects, no people, no text, no watermark. Opaque same-resolution 16:9 image.
```

### Trou Minecraft ouvert — image finale

```text
Use case: stylized-concept. Asset type: opaque widescreen 16:9 visual-novel background inside Minecraft, matching the game's existing Minecraft environment plates: authentic cubic voxel geometry, clearly pixelated grey stone textures, attractive soft shader lighting, subtle ambient occlusion, crisp block edges and warm indirect light, absolutely NO smooth realistic stone and NO anime linework for this in-game world. Scene: an absurdly small empty square hole dug in a bare stone plateau, about two blocks wide and two blocks tall, camera inside near the floor looking slightly upward at the opposite stone wall and ceiling. Close grey stone block walls fill most of the frame. At the upper center, ONE square block-sized opening in the stone ceiling reveals a small patch of pale blue daytime sky; the surrounding ceiling is stone so placing exactly one more block would close the only opening. Faint daylight from this square illuminates the stone. The hole must feel small, ordinary and comically pointless, not a cavern or dungeon. Keep clear foreground for two Minecraft character sprites to be overlaid by the game. No characters, no mobs, no hands or tools, no ladder, no torch, no vegetation, no windows, no doorway, no treasure, no text, no HUD, no crosshair, no borders, no watermark. One single cohesive 1920x1080 or same 16:9 landscape image.
```

### Trou Minecraft refermé — variante finale

```text
Use case: precise-object-edit. The supplied image is the EDIT TARGET: the open Minecraft stone pit background. Create the immediately following frame after a character places ONE grey stone block into the square ceiling opening. Keep the EXACT same camera, perspective, geometry, crop, pixel-textured stone walls and floor. Change only the square opening and resulting light: replace the blue sky opening completely with the underside of a matching stone cube, flush with the adjacent ceiling. The sky and sunbeam disappear; the entire small chamber becomes dim, cool grey, with just enough low game-style ambient illumination to read the pixelated stone walls and their corners. It is now completely sealed with no gaps or windows. No torches or invented light source, no people, mobs, hands, tools, objects, sign or text. Preserve authentic Minecraft voxel rendering and subtle shader ambient occlusion. No horror effects. Single opaque 16:9 landscape background matching original resolution. The two frames must cut together without any camera movement or room redesign.
```


