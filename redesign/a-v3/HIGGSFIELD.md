# Storytelling con Higgsfield (prueba, hasta el 27 de noviembre de 2026)

## Por qué se trabaja en dos lugares

La prueba ilimitada de Higgsfield **no funciona en Claude Code** (respuesta de su servidor, 24 de noviembre de 2026). Funciona en un chat normal de Claude, en Claude Cowork o en ChatGPT. Por eso:

| Paso | Dónde | Quién |
|---|---|---|
| 1. Referencias subidas | Proyecto de Higgsfield "Portfolio storytelling (nicolasmb.com)" | Hecho desde Claude Code |
| 2. Generar | Chat de Claude con Higgsfield conectado | Tú, pegando los mensajes de abajo |
| 3. Elegir | El mismo chat | Tú: cuál queda y por qué descartas las otras |
| 4. Bajar, optimizar e integrar | Claude Code (este repo) | Claude: lee el proyecto de Higgsfield, baja los videos, los comprime y los pone en el sitio |

El proyecto de Higgsfield es el puente: todo lo que generes ahí lo puedo leer y bajar desde aquí. No hace falta descargar ni volver a subir archivos.

## Datos del proyecto (para pegar en el chat)

- Workspace: `5c1a64f1-6561-4d59-bd0a-1943cfe7eb69`
- Proyecto: `f583b208-3bef-49c8-8b24-e278a2a235e0` (carpeta por defecto: el mismo id)
- Referencias ya subidas (media_id):
  - Pieza principal de Vende Digital: `a59db8dd-fca7-4ff5-9219-1329f7cedda5`
  - Valla de Vende Digital: `d987b2e8-e621-4983-938b-ea4efcb66c62`
  - Pieza "Bogotá se vive con propósito" (Invest in Bogotá): `a21c561a-052c-4f1c-aa4f-35db7c3d0468`

## Reglas para todo lo que se genere

- **Sin texto ni logos dentro del video.** Los textos y logos reales los pone el sitio encima, en HTML. La IA deforma letras y marcas.
- **Sin la cara de la modelo de la campaña.** La foto de Vende Digital es de banco de imágenes; su licencia cubría la campaña, no videos nuevos con su cara. Se usa solo como referencia de color y estilo.
- **Sin sonido**, 16:9, 6 segundos, cámara lenta y estable (debe poder repetirse en bucle sin molestar).
- **Formas de la marca:** nada orgánico añadido. El cierre de cada video es una línea de horizonte limpia, donde el sitio hace subir el título.
- **Etiqueta en el sitio:** "Video hecho con IA a partir de mi pieza original (2026)".
- **Guardar todo**, también lo descartado: es el material de "detrás de la pieza".

---

## Ejemplo 1: Vende Digital, "un pedido que conecta"

**Historia:** una tienda pequeña de pueblo al atardecer recibe un pedido en línea; la caja sale hacia otra ciudad. Es la promesa del programa ("Hechos que conectan") contada sin palabras.

### Mensaje para pegar en el chat de Claude

```text
Use Higgsfield. Workspace 5c1a64f1-6561-4d59-bd0a-1943cfe7eb69, project f583b208-3bef-49c8-8b24-e278a2a235e0; save every generation in folder f583b208-3bef-49c8-8b24-e278a2a235e0. Use my unlimited trial generations (use_unlim: true). Do not spend credits.

Generate 3 variants with model seedance_2_0, mode std, 720p, 16:9, duration 6, generate_audio false. Use media a59db8dd-fca7-4ff5-9219-1329f7cedda5 as image_references (color and style only; do not reproduce the woman in it).

Prompt:
"Dusk in a small Colombian town. Inside a modest corner shop, warm light. Close shot on the wooden counter: a shop owner's hands (no face visible) fold and tape a cardboard shipping box. A smartphone lying on the counter lights up with a soft glow, a new order. The hands lift the box and carry it out of frame. Slow, steady push-in, shallow depth of field. Palette inspired by the reference: soft pink, electric blue and a warm yellow accent. Final second: the frame settles on the open shop door with a calm, flat street horizon at dusk. Photorealistic, natural light, no text, no logos, no signage, no letters anywhere."

When done, show me the three videos side by side and wait for me to pick one.
```

### Si el resultado no convence (segundo intento)

```text
Same settings and folder. Change only the prompt: make the camera move slower, keep the hands always in focus, and remove anything that looks like text on the box, the phone screen or the walls. 2 variants.
```

---

## Ejemplo 2: Invest in Bogotá, "detrás de la pieza"

**Historia:** el proceso real de una exploración nueva, hecha hoy con IA a partir de tu pieza "Bogotá se vive con propósito": la pieza original → una versión limpia sin texto → tres videos → el elegido, y qué descartaste y por qué. Es honesto porque el proceso ocurre ahora y queda registrado.

### Cómo se arma

Las tres opciones parten de la misma foto limpia (paso 0). Generas las tres; la que elijas va al caso, y las dos descartadas, con tu razón, son el contenido de "detrás de la pieza".

En cada mensaje para el chat, pon primero esta línea:

```text
Use Higgsfield. Workspace 5c1a64f1-6561-4d59-bd0a-1943cfe7eb69, project f583b208-3bef-49c8-8b24-e278a2a235e0; save every generation in folder f583b208-3bef-49c8-8b24-e278a2a235e0. Use my unlimited trial generations only (use_unlim: true); never spend credits.
```

### Paso 0: la plaza limpia (para las tres opciones)

Adjuntar en este orden: 1. la pieza original (media `a21c561a-052c-4f1c-aa4f-35db7c3d0468`).

```text
ONE ORDINARY, ULTRA-REALISTIC NIGHT AERIAL PHOTOGRAPH, taken from a real drone.

=== 4 HARD REQUIREMENTS ===
1. ABSOLUTELY NO TEXT: no letters, no words, no numbers, no logos, no white frame, no graphic layout. A clean photograph only.
2. THE SAME BUILDING as @Image1: a round brick bullring with an open sand arena, rising rows of stone seating, a ring of warm lights along the top edge and a row of tall arched openings around the outside wall.
3. WIDE 16:9 FRAME. The bullring sits in the lower-middle of the frame and fills about half the frame width. The city continues on every side.
4. ONLY THE LIGHT THAT IS ALREADY THERE: the bullring's own warm lamps, street lamps and windows. No added light.

INPUTS
@Image1 — THE PLACE, THE ONLY SOURCE OF THE BUILDING, THE CAMERA ANGLE AND THE COLOUR: take the bullring, its brick and sand, the warm golden light, the surrounding streets, trees and buildings, and the high, steep drone angle. TAKE NOTHING ELSE FROM @Image1 — not the white rectangle, not any text, not the logos, not the black bands at the top and bottom.

THE CAMERA
A real drone about 120 metres up and slightly to the south-west, looking down at about 50 degrees, wide lens with no distortion. Level horizon.

THE LAYOUT
Lower-middle: the full ring of the bullring, the sand arena lit warm and even, the seating in clean concentric rows.
Around it: small apartment blocks with lit windows, dark tree canopies, a few streets with amber street lamps.
Top quarter: the city fades into darkness and the dark, smooth silhouette of a long mountain ridge against a deep navy night sky. No moon, no stars.

REALISM
Real materials: rough red brick, pale sand with footprints, grey stone seating. Correct scale: one row of seats is knee-high to a person. Gentle night grain, natural contrast, no glow halos.

NEGATIVE
Text: no letters, signs, billboards, logos, watermarks, frames, borders, captions.
Look: no illustration, no 3D render, no tilt-shift miniature, no HDR, no orange-and-teal grading, no lens flares, no fog.
Content: no people, no cars in the arena, no fireworks, no event stage, no second bullring.
```

Ajustes: Nano Banana Pro · 16:9 · 2K · 2 variantes · referencia: la pieza original.

---

### Opción A: "Del ruedo al horizonte" (una toma, la más sobria)

La cámara sube despacio sobre la plaza encendida hasta que los cerros quedan como una línea de horizonte. Es la más segura y la que mejor empata con el título que sube en el sitio.

Adjuntar en este orden: 1. la plaza limpia que elegiste en el paso 0 (como imagen inicial).

```text
16:9 · 8 seconds · ONE CONTINUOUS SHOT · no speech · no sound.

=== 4 HARD REQUIREMENTS ===
1. ONE SINGLE CONTINUOUS DRONE SHOT. No cuts.
2. The bullring from @Image1 stays EXACTLY the same building: same brick, same arches, same lights. It never bends, melts or changes shape.
3. THE SHOT ENDS ON A LEVEL, ALMOST FLAT HORIZON: the dark mountain ridge as a long low line across the lower third, deep navy sky above, and the camera at rest for the last 1.5 seconds.
4. NO TEXT, NO LOGOS, NO LETTERS anywhere, at any moment.

INPUTS
@Image1 — THE FIRST FRAME AND THE ONLY SOURCE OF THE PLACE AND THE LIGHT. Start exactly on this picture.

THE CAMERA
A real drone, smooth but not perfect: a very slight drift. No zoom ever; closer or wider only because the drone moves.

0.0–2.5s — Start on @Image1. The drone begins to rise slowly, straight up.
2.5–5.5s — Still rising, the drone tilts up gradually. The bullring slides toward the bottom of the frame and gets smaller; more city lights fill the frame; a few car light trails move along the avenues.
5.5–6.5s — The tilt reaches level. The bullring leaves the bottom edge of the frame. The dark mountain ridge now sits as a long, low line in the lower third.
6.5–8.0s — The drone stops and holds, almost still. City lights below the ridge, deep navy sky above.

LIGHT
Only the light already in the city: the bullring's warm lamps, amber street lamps, windows. The sky is darker than every lit surface. One night, one exposure.

THE LOOK
Real drone footage at night: soft, natural contrast, fine grain, warm golden lights against cool dark streets. Calm and unhurried.

NEGATIVE
Motion: no cuts, no fast moves, no spinning, no zoom, no speed ramps, no shake.
Content: no people close up, no fireworks, no searchlights, no drones or birds in frame, no moon, no stars, no clouds racing.
Text: no letters, signs, logos, watermarks, captions.
Look: no illustration, no 3D render, no miniature effect, no lens flares, no glow halos.
```

Ajustes: Seedance 2.5 · 16:9 · 8 s · 720p · sin sonido (generate_audio: false) · la plaza limpia como start_image · 3 variantes.

---

### Opción B: "La ciudad se enciende" (una toma, del atardecer a la noche)

Es la misma plaza vista desde arriba, a la hora azul: el ruedo se enciende y después la ciudad alrededor. Cuenta la frase de la pieza, "cada evento puede ser el inicio de algo grande", sin palabras: una luz que contagia a toda la ciudad.

Adjuntar en este orden: 1. la plaza limpia que elegiste en el paso 0 (como referencia, no como imagen inicial: la toma empieza más clara).

```text
16:9 · 8 seconds · ONE CONTINUOUS SHOT · no speech · no sound.

=== 5 HARD REQUIREMENTS ===
1. ONE SINGLE CONTINUOUS SHOT FROM A DRONE HOLDING ALMOST STILL, slowly descending a little. No cuts, no time-lapse jumps.
2. The light changes ONLY by lamps switching on, in this order: the bullring's ring of lights first, then the streets around it, then the city further away. The sky does not change colour during the shot.
3. The bullring is the SAME building as @Image1: same brick, arches and rows of seats.
4. THE SHOT ENDS on the whole city lit, with the dark mountain ridge as a long low line in the upper third and the camera still for the last 1.5 seconds.
5. NO TEXT, NO LOGOS, NO LETTERS anywhere.

INPUTS
@Image1 — THE PLACE: take the bullring, the streets, trees and buildings around it, and the high drone angle. TAKE NOTHING ELSE FROM @Image1 — not its full night darkness at the start (the shot starts at blue hour), not any text or logos.

THE CAMERA
A real drone about 120 metres up, looking down at about 50 degrees, descending very slowly. A very slight drift. No zoom.

0.0–2.0s — Blue hour: deep blue sky, the city in soft blue shadow, almost no lamps on. The bullring's sand is pale and cool.
2.0–3.5s — The bullring's ring of warm lamps switches on, lamp after lamp around the circle, in about one second. The sand turns warm gold.
3.5–5.5s — The street lamps around the bullring come on, block by block, spreading outward like a ripple.
5.5–6.5s — Windows and avenues further away light up. A few car light trails move.
6.5–8.0s — Everything is lit. The drone stops and holds, almost still.

LIGHT
Only lamps that belong to the city switch on. The sky stays the same blue from start to end and is always darker than the lit surfaces. No sweeping beams, no flashes.

THE LOOK
Real drone footage: soft, natural contrast, fine grain, warm golden lamps against cool blue streets.

NEGATIVE
Motion: no cuts, no time-lapse flicker, no clouds racing, no sun moving, no zoom, no spinning.
Light: no fireworks, no searchlights, no lightning, no lens flares, no glow halos, no flicker of the whole frame.
Content: no people close up, no stage, no crowds, no drones or birds in frame.
Text: no letters, signs, logos, watermarks, captions.
Look: no illustration, no 3D render, no miniature effect.
```

Ajustes: Seedance 2.5 · 16:9 · 8 s · 720p · sin sonido · la plaza limpia como image_reference (no start_image) · 3 variantes.

Consejo: si el encendido sale como un parpadeo de toda la imagen, corre la misma instrucción una vez más antes de cambiar el texto.

---

### Opción C: "El inicio de algo grande" (tres tomas, la más narrativa)

Es la plaza como sede de un evento (turismo de reuniones, el tema de la pieza):
1. Dentro, sillas vacías esperando.
2. Las luces del escenario se encienden.
3. La cámara sale volando hasta el horizonte.

Es la más arriesgada, porque son tres tomas, y por eso necesita una segunda foto.

**Paso C1: la plaza preparada para un evento (foto nueva)**

Adjuntar en este orden: 1. la plaza limpia que elegiste en el paso 0.

```text
ONE ORDINARY, ULTRA-REALISTIC NIGHT PHOTOGRAPH, taken by a person standing inside the arena.

=== 4 HARD REQUIREMENTS ===
1. THE SAME BULLRING as @Image1, seen from INSIDE: round sand arena, rising rows of stone seating all around, a ring of warm lamps along the top edge.
2. ON THE SAND: EXACTLY 8 straight rows of plain white folding chairs, about 12 chairs per row, all facing a low, plain black stage at the far side. The stage is empty: no screen, no banner, no logo, no microphone.
3. NO PEOPLE. NO TEXT, NO LOGOS, NO LETTERS anywhere.
4. ONLY THE LIGHT THAT IS ALREADY THERE: the bullring's own ring of warm lamps. The stage lights are OFF.

INPUTS
@Image1 — THE PLACE, THE ONLY SOURCE OF THE BUILDING AND OF THE COLOUR: take the brick, the stone seating, the pale sand and the warm lamps. THE REFERENCE DEFINES THE WORLD, NOT THE FRAMING: the camera position is our own. TAKE NOTHING ELSE FROM @Image1.

THE CAMERA
A person standing on the sand behind the last row of chairs, camera at chest height (1.4 m), 35 mm lens, square on to the stage. Level horizon.

THE LAYOUT
Foreground: the backs of the last rows of white chairs, in sharp focus.
Middle: the rows of chairs running toward the stage, the pale sand between them.
Far side: the low black stage, and behind it the curved rows of empty stone seating rising up to the ring of warm lamps. Above: a dark navy night sky.

REALISM
Real materials: matte white plastic chairs with small scuffs, pale sand with footprints, grey stone, rough red brick. Correct scale. Gentle night grain.

NEGATIVE
No people, no text, no logos, no banners, no screens, no flags, no confetti, no fog, no coloured stage lights, no illustration, no 3D render.
```

Ajustes: Nano Banana Pro · 16:9 · 2K · 2 variantes · referencia: la plaza limpia.

**Paso C2: el video**

Adjuntar en este orden: 1. la plaza preparada (paso C1); 2. la plaza limpia desde el aire (paso 0). Las dos van como referencias, no como imagen inicial.

```text
16:9 · 10 seconds · 3 SHOTS · cuts at 3.5s and 6.0s · no speech · no sound.

READ THIS FIRST: THIS IS A SEQUENCE OF 3 SHOTS, NOT A SINGLE TAKE.
Shot 1: 0.0–3.5s. Shot 2: 3.5–6.0s. Shot 3: 6.0–10.0s.

=== 5 HARD REQUIREMENTS ===
1. THREE SEPARATE SHOTS with hard cuts at exactly 3.5s and 6.0s.
2. The SAME bullring in all three shots: same brick, arches, stone seating and ring of warm lamps as @Image1 and @Image2.
3. NO PEOPLE IN SHOTS 1 AND 2. In shot 3, only tiny distant figures if any, never a face.
4. NO TEXT, NO LOGOS, NO LETTERS, NO SCREENS WITH IMAGES anywhere.
5. SHOT 3 ENDS ON A LEVEL, ALMOST FLAT HORIZON: the dark mountain ridge as a long low line in the lower third, deep navy sky above, the camera still for the last 1.5 seconds.

INPUTS
@Image1 — THE INSIDE OF THE ARENA FOR SHOTS 1 AND 2: the rows of white chairs, the low black stage, the stone seating, the warm lamps. THE REFERENCE DEFINES THE WORLD, NOT THE FRAMING.
@Image2 — THE BULLRING FROM THE AIR FOR SHOT 3: its shape, the city around it, the mountain ridge. TAKE NOTHING ELSE FROM @Image2.

THE CAMERA
Shots 1 and 2: handheld with a small, constant shake; no zoom ever. Shot 3: a real drone, smooth with a very slight drift; no zoom.

=== SHOT 1 — 0.0 to 3.5s — LOW CLOSE SHOT ALONG A ROW OF CHAIRS ===
The camera is at seat height at the end of a row, looking along the empty white chairs toward the stage. If the whole stage is visible, the shot is too wide and it is wrong.
0.0–2.0s — Stillness. The empty chairs, the pale sand, the warm lamps of the ring soft and out of focus in the background.
2.0–3.5s — The camera slides slowly sideways along the row, about one chair width.

=== CUT AT 3.5s ===

=== SHOT 2 — 3.5 to 6.0s — WIDE SHOT FROM BEHIND THE LAST ROW ===
The framing of @Image1: the rows of chairs, the black stage, the curved seating rising behind it.
3.5–4.5s — The stage is dark.
4.5–5.0s — Four warm white lamps above the stage switch on together. The stage floor and the first rows of chairs light up. Nothing else changes.
5.0–6.0s — Hold. The light settles.

=== CUT AT 6.0s ===

=== SHOT 3 — 6.0 to 10.0s — DRONE RISE OUT OF THE ARENA ===
6.0–7.5s — The drone starts just above the top ring of lamps, looking down at the lit arena: the chairs, the stage glowing, the bullring whole. It rises steadily.
7.5–8.5s — Still rising, it tilts up. The bullring shrinks toward the bottom of the frame; the city lights spread out.
8.5–10.0s — Level. The dark mountain ridge is a long low line in the lower third. The drone holds, almost still.

LIGHT
Only lamps that belong to the place: the bullring's ring of warm lamps, the four stage lamps, the street lamps and windows of the city. The sky is always darker than every lit surface.

THE LOOK
Real footage from a real camera at night: soft, natural contrast, fine grain, warm golden light against cool dark streets. Calm.

NEGATIVE
Structure: no single continuous take, no extra cuts, no dissolves.
Content: no people close up, no faces, no crowds, no performers, no confetti, no fireworks, no smoke, no coloured or moving stage lights, no screens.
Text: no letters, signs, banners, logos, watermarks, captions.
Look: no illustration, no 3D render, no miniature effect, no lens flares, no glow halos.
```

Ajustes: Seedance 2.5 · 16:9 · 10 s · 720p · sin sonido · referencias en este orden: 1. la plaza preparada, 2. la plaza desde el aire · 2 variantes.

Consejo: pruébala primero en modo borrador (draft: true, 480p). Si las tres tomas salen como una sola, pídele al chat que la repita antes de cambiar el texto.

### Después de elegir (esto lo escribes tú, es el contenido del bloque)

Responde en el chat, o mándamelo aquí:

1. **Cuál elegiste y por qué** (una frase).
2. **Qué descartaste y por qué** (una frase por cada una; por ejemplo "deformó el ruedo", "la cámara se movía demasiado").
3. **Qué decidiste tú** que la IA no habría decidido (por ejemplo: quitar el texto, cerrar en el horizonte).

---

## Qué hago yo cuando avises

1. Leo el proyecto de Higgsfield desde aquí y bajo los videos elegidos (y los descartados para el ejemplo 2).
2. Los comprimo a WebM y MP4 de menos de 2 MB, con una imagen fija de respaldo.
3. Los integro con el generador: reproducción en silencio y en bucle; solo imagen fija con "reducir movimiento"; etiqueta de IA visible.
4. Marco los textos nuevos con `PROPUESTA DE TEXTO` y te los paso para aprobar.
5. Pruebas (accesibilidad, anchos, sin JavaScript, movimiento reducido, peso y LCP) y capturas.
