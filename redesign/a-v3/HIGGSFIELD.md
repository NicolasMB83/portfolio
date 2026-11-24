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

### Paso A: imagen limpia (sin textos ni logos)

```text
Use Higgsfield. Workspace 5c1a64f1-6561-4d59-bd0a-1943cfe7eb69, project f583b208-3bef-49c8-8b24-e278a2a235e0; save in folder f583b208-3bef-49c8-8b24-e278a2a235e0. Use my unlimited trial generations (use_unlim: true). Do not spend credits.

Generate 2 variants with model nano_banana_pro, 2k, aspect ratio 16:9, with media a21c561a-052c-4f1c-aa4f-35db7c3d0468 as image_references.

Prompt:
"Recreate this photograph as a clean wide 16:9 frame: the night aerial view of the bullring plaza in Bogotá, the city lights around it, warm golden light. Remove all text, the white frame and every logo. Keep the composition, the camera angle and the color of the original. Photorealistic, no text, no letters."
```

### Paso B: video desde la imagen elegida

```text
Same project and folder, unlimited generations only. Take the image I chose from step A as start_image.

Generate 3 variants with model seedance_2_0, mode std, 720p, 16:9, duration 6, generate_audio false.

Prompt:
"Slow aerial drone rise over the illuminated bullring plaza in Bogotá at night. The city lights flicker gently; a few car light trails move on the avenues. The camera rises and tilts up until the dark mountains of the eastern hills form a flat horizon line against a deep navy sky. Calm, steady, cinematic. No text, no logos, no letters."

Show me the three side by side and wait for me to pick one.
```

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
