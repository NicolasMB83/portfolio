# Working agreements for this portfolio (Nicolás Mogollón Barbosa)

These rules come from the site owner and apply to every task in this repo.

## Research before doing (mandatory)
- Before designing or building anything, research first. Use the newest sources available (current year), not memory.
- Cite what you found (links) when you report back, and say when a source could not be reached.
- Style can be our own and does not need to follow trends. Rules (UX, accessibility, SEO, i18n, performance, browser support) must follow the latest published guidance.

## Content and copy
- Do not change visible copy without approval. Propose text changes in a list, mark them in the HTML with `<!-- PROPUESTA DE TEXTO: ... -->`, and wait for a yes.
- The brand name is "Invest in Bogotá" (with tilde) everywhere.
- Talk to the owner in Spanish.

## Project context
- Brand/strategy context: `.agents/context/PRODUCT.md`.
- Current redesign work lives on the `redesign` branch under `redesign/`. The live site (`main`) is not touched without explicit approval.
- Backup of the original Framer export: branch `backup/original-framer-2026-11-01`.
- Visual concept "Horizonte": the logotype is letters rising from a line; its arcs, dot and stems are the shape vocabulary of the whole site.

## Delivery
- Verify every page visually (desktop + mobile) and with automated checks (axe, overflow, no-JS, reduced motion) before reporting.
- Do not crowd the site: every texture, animation or element needs a reason.

## Estado actual (para retomar en cualquier sesión)
- Trabajo vigente: Opción A v2 "Horizonte" en `redesign/a-v2/` (EN) y `redesign/a-v2/es/` (ES), rama `redesign`.
- Generador: `python3 redesign/tools/build.py` escribe todas las páginas; sus piezas (logo, íconos Phosphor, quemadura SVG, manifiesto de imágenes) están en `redesign/tools/parts/`. No edites el HTML generado a mano: edita el generador.
  - CSS/JS compartidos: `redesign/a-v2/assets/` (`site.css`, `site.js`). El generador calcula el `?v=<hash>` solo.
  - Todo es local: imágenes WebP en `assets/img/`, fuentes WOFF2 en `assets/fonts/`, Lottie en `assets/vendor/`. Lo único en Framer son las 3 animaciones Lottie de portada.
  - Para publicar en la raíz: `REPO_FROM_SITE = ''`, `ABS_ROOT = '/'`, `LINK_INDEX = False`.
- Páginas: home, `invest-in-bogota/`, `radio-a-domicilio/`, `404.html` (bilingüe), `projects-a/`, `projects-b/` y `projects-c/` (alternativas de la sección de proyectos, solo EN, noindex; C es la fusión vigente).
- Propuestas en comparación (prototipo, se quitan al publicar): `?header=a|b|c` y, en Radio a Domicilio, `?parallax=b|c|d` (script en el `<head>` que pone `data-header` / `data-parallax`).
- Revisión de textos: `redesign/tools/review.py` (R1…R29). El generador marca cada una en el HTML; la tabla está en PROPUESTAS.md.
- Decisiones tomadas por el dueño:
  - Textura = teselación (también como placeholder de imágenes).
  - Secciones oscuras aprobadas.
  - Panel de contacto con entrada desacelerada (sin morph).
  - 404 con GIF aleatorio de gatos (GIPHY) dentro del sol.
  - Email `nicolasbarbosa.us@gmail.com`; título "Visual and AI Designer"; empresa "ReloQuest".
  - Footer: índigo del sitio (la película negra se retiró porque rompía la estética). Logo grande en blanco cuyas letras suben al entrar en pantalla. La halación queda solo en el logo del encabezado.
  - No depender de Framer: aprobado.
  - Fase 4 aprobada: halación del logo al pasar el cursor + barrido del horizonte entre páginas.
  - Soles: todos levemente desenfocados, con brillo suave y gradiente muy sutil (amarillo cálido arriba, más quemado hacia el horizonte).
  - Le gusta la grilla actual de proyectos. De la alternativa B le gustó la grilla de tres y el revelado a color; la película en proyectos está descartada.
  - Regla de marca: el logo es geométrico y perfecto. Nada orgánico ni dibujado a mano (fue lindo, pero rompe la marca); todo efecto sale del arco, el punto y la línea.
  - Cada proyecto tiene su propia estructura (cada uno es diferente), pero de la misma familia (generador: `case_cover` + `case_shell` + `rad_main` / `iib_main`).
    - Portada común: título sobre el horizonte, descripción breve y Año / Empresa / Rol.
    - Radio a Domicilio: capítulos numerados, con números pequeños.
    - Invest in Bogotá: sin números, marcado con el punto rojo de la marca.
  - Nada de arcos como ventana de imagen (no le gustan); se usan marcos redondeados.
  - Tipografía igual a la versión publicada: Clash Display (700 en hero, menú, botones y títulos de proyecto), Albert Sans para el texto, DM Sans para rótulos. Fondo `#eef2ff`; píldora blanca al 82 %.
  - El hero no se parte: "I LOVE DESIGN" y la segunda línea van juntas sobre el horizonte.
  - La línea del horizonte bajo un sol tiene opacidad 0 lejos del sol y aumenta al acercarse (`.horizon--sun`).
  - Píldora: hover naranja en secciones e idioma (`--sun-ink`, para que el texto tenga 5:1 de contraste).
  - Teselación solo como placeholder de imágenes que cargan o fallan; nunca para enmarcar imágenes ni en bordes de sección. La baldosa dibuja la onda continua (sin cortes en las uniones).
  - La animación de scroll de imágenes (`.settle`) solo donde aporta. Hoy: la captura del sitio de Invest in Bogotá.
  - CTA: al pasar el cursor se dibuja el contorno del sol y luego se rellena.
  - Punto 9 aprobado e integrado en Invest in Bogotá.
  - Créditos: el dueño decide cuándo parar; no limitar el trabajo por eso.
  - Rescatado de la primera versión (Framer, en la raíz del repo):
    - Encabezado en píldora flotante que se esconde al bajar y aparece al subir.
    - Hover del CTA con círculo y flecha (reinterpretado como el punto que sube desde el horizonte).
    - Parallax en la imagen inicial de cada proyecto.
  - Halación del logo: capa ya dibujada que solo cambia de opacidad (animar `filter` desde `none` daba un brillo negro).
- Pendiente de aprobación (ver "Pendiente de tu decisión" en `redesign/a-v2/PROPUESTAS.md`):
  - Encabezado (A / B / C).
  - Parallax (A / B / C / D).
  - Nombre de la sección de piezas.
  - Revisión de textos R1–R29.
  - Íconos.
  - Fusión de proyectos (`projects-c/`).
  - Archivos Lottie.
  - Publicación.
- El español debe ser una traducción fiel del inglés (mismo contenido, palabras nativas de cada idioma).
- Casos de estudio:
  - Todos son páginas claras con secciones `is-night tone-night`.
  - Color del cliente: `--client` (sobre oscuro) y `--client-ink` (sobre blanco).
- Red del entorno: `framerusercontent.com` y `*.framer.app` están bloqueados. Para descargar las Lottie, el dueño debe permitirlos en Network access.
- Nada se publica en `main` sin aprobación explícita. El sitio en vivo es `https://nicolasmb.com/` (Netlify, se actualiza desde `main` en minutos).
- Deck de Figma del dueño (Figma Slides, fileKey `A2FLZyFCZUkYItYyTG2Tgn`, portada nodo `1:2107`): fondo negro tipo película, grano, polvo/rayas, quemadura de película naranja en una esquina y el logotipo con halación (núcleo amarillo, naranja, borde magenta). El conector de Figma solo puede capturar diapositivas cuyo enlace (node-id) comparta el dueño; no puede listar las diapositivas de un deck.
- Vista previa: `https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/index.html`. Puede tardar unos minutos en reflejar un cambio; si dudas, recarga forzada.
- Lección técnica: un contenedor con `overflow: hidden` se vuelve contenedor de scroll y congela las animaciones `view()` de sus hijos. Usa `overflow: clip`.
