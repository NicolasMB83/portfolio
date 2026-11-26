# Traspaso para la sesión siguiente (26 de noviembre de 2026)

Este documento sirve para empezar una sesión nueva con el conector de Craftwork activo. La memoria completa del proyecto está en `.claude/CLAUDE.md`, que la sesión nueva lee sola. Aquí va solo lo necesario para seguir.

## Cómo empezar

1. Abre una sesión nueva sobre el repositorio `NicolasMB83/portfolio`, en la rama `redesign`, con el conector de Craftwork activado. Los conectores solo se cargan al empezar una sesión.
2. Pega este mensaje:

> Lee `redesign/a-v3/TRASPASO.md` y `.claude/CLAUDE.md`. Usa el conector de Craftwork para proponerme 3 opciones de mockup de celular para las historias de Vende Digital, combinadas con el fondo de líneas topográficas. Investiga antes, muéstrame las opciones con capturas y no publiques en `main`.

## Dónde estamos

- **Versión en trabajo:** a-v3, en `redesign/a-v3/` (inglés) y `redesign/a-v3/es/` (español), rama `redesign`. El último commit de esta sesión es `5a51eb2`.
- **Generador:** `python3 redesign/tools/build.py`. No se edita el HTML a mano.
- **Pruebas:** sirve el repo en el puerto 8765 y corre `NODE_PATH=/opt/node22/lib/node_modules node redesign/tools/qa/qa.js` (accesibilidad, 9 anchos, sin JavaScript y movimiento reducido).
- **Vista previa:** https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v3/index.html (para una versión exacta, cambia `redesign` por el hash del commit).
- **Sitio en vivo:** `main` (nicolasmb.com) no se ha tocado y no se toca sin aprobación explícita.

## Tarea siguiente: mockups con Craftwork

**Qué hay hoy.** En Vende Digital, sección de piezas, tres historias reales van en celulares rectos dibujados en HTML (`phones()` en `build.py`, estilos `.phones` y `.phone` en `site.css`). El fondo es de líneas topográficas vectoriales generadas por `redesign/tools/topo.py`, que escribe `assets/img/vd-topo.svg`. Al dueño le gusta como punto de partida, pero quiere algo mejor.

**Qué pidió.** Opciones que integren un mockup de Craftwork, pueden ser un híbrido con el fondo topográfico y el rosado del sistema 2022. Hay que mostrarle opciones antes de elegir.

**Restricciones:**
- Nada de mockups flotantes en ángulo ni de aspecto falso: el anterior "se veía falso".
- Usar las historias reales:
  - Están en `assets/img/vd-story-1/2/3-*.webp`, en formato 9:16.
  - Salen de su Behance: https://www.behance.net/gallery/210712239/Vende-Digital
- Revisar la licencia de cada mockup de Craftwork antes de usarlo en un sitio público.
- Imágenes locales en WebP. Si cambia una imagen, debe cambiar de nombre, por la caché de un año.
- Las tres opciones deben verse en escritorio y celular, con capturas.

**Ideas para las opciones:**
1. **Mockup fotográfico de Craftwork:** un celular en una mano o sobre una mesa, con la historia insertada y el fondo rosado con líneas topográficas detrás.
2. **Mockup plano de Craftwork:** tres celulares de frente, sobre el panel topográfico actual.
3. **Híbrido:** un solo celular grande de Craftwork con la historia principal, y las otras dos historias pequeñas al lado, sin marco.

## Textos esperando aprobación del dueño

Todo está en `redesign/a-v3/CAMBIOS.md`.

| Texto | Qué es |
|---|---|
| V1–V11 | Textos de la versión a-v3 (algunos ya cambiaron; ver la tabla) |
| V12 | Reflexión de Vende Digital ("Lo que aporté" ya corregido) |
| V13 | Caso Colombia 4.0 (títulos nuevos, "+62.000 asistentes" y tres errores del texto publicado para decidir) |
| V14 | Vende Digital en cuatro actos (el cambio; conservé, quité y redibujé) |
| V15 | Rótulos "2020 · Banner de lanzamiento" y "2022 · El mismo banner en el nuevo sistema" |

## Decisiones de esta sesión (ya guardadas en `CLAUDE.md`)

**Sistema visual**
- Lo más fuerte del sitio es el sistema que sale del logo (arcos, punto, astas). La forma del cliente va solo en la portada de cada caso.
- Los títulos de sección no llevan ícono. Su línea queda dentro de la columna y se desvanece hacia la derecha. Solo cruza la página entera bajo un sol.
- Las tarjetas del inicio solo tienen la flecha como microanimación.
- Escala de letra de cinco pasos (título, sección, frase principal, ítem y cuerpo), aplicada en los casos y en el inicio. El titular del hero no se toca.
- Las galerías no recortan imágenes: usan filas justificadas (`jrow()`).

**Público y contenido**
- El público es internacional. Se quitaron Bogotá y Colombia; queda "GMT−5" en el contacto.
- Regla para todos los casos: mostrar lo que hizo el dueño. Los datos del programa van solo como contexto o si explican una decisión suya.

**Vende Digital**
- Se cuenta en cuatro actos: el cambio, qué conservé y qué cambié, las piezas, y resultados con reflexión.
- El logo anterior es el de lanzamiento de diciembre de 2020.
- El dueño "actualizó" el logo; no lo rediseñó. El sistema "Hechos que conectan" lo definió el ministerio.

**Otros casos**
- Colombia 4.0 ya tiene caso (`col40-2018/`). Su contenido vivía solo en Framer.
- Infinited usa el infinito hecho con dos anillos como forma.

## Pendientes, además de los mockups

- **Narrativa "Un día en Bogotá", aprobada en tres pasos:**
  1. Proponer tres opciones de frase central.
  2. Hacer un prototipo del inicio en una página aparte.
  3. Contar los demás casos en cuatro actos, usando Vende Digital como plantilla.
- **Referente Louis Paquet:** quedan por decidir los puntos 2 a 6 (ver `CLAUDE.md`). El 3, recortar animaciones, se cumplió en parte al quitar las formas de las tarjetas.
- **Una confirmación del dueño:** que el fondo topográfico y el fucsia los definió el ministerio, y que no fueron suyos.
- **Ya se pueden alojar en local las tres animaciones Lottie de portada,** porque `framerusercontent.com` ya está permitido.
- **Publicación en `main`:** pendiente de aprobación.

## Red del entorno

Hosts permitidos en esta sesión:
- Framer: `framerusercontent.com`, `orange-point-971308.framer.app`.
- Behance: `www.behance.net`, `mir-s3-cdn-cf.behance.net`.
- `nicolasmb.com` y `tympanus.net` (Codrops bloquea las lecturas automáticas igual).
- Sitios de MinTIC y medios colombianos.

Si Craftwork necesita un host para bajar archivos, la sesión nueva debe pedirlo con `update_environment`.
