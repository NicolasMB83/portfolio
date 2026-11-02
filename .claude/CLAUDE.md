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
- Páginas: home, `invest-in-bogota/` (galería), `radio-a-domicilio/` (plantilla por capítulos, ejemplo), `404.html` (bilingüe), `projects-a/`, `projects-b/` y `projects-c/` (alternativas de la sección de proyectos, solo EN, noindex; C es la fusión vigente).
- Decisiones tomadas por el dueño:
  - Textura = teselación (también como placeholder de imágenes).
  - Secciones oscuras aprobadas.
  - Panel de contacto con entrada desacelerada (sin morph).
  - 404 con GIF aleatorio de gatos (GIPHY) dentro del sol.
  - Email `nicolasbarbosa.us@gmail.com`; título "Visual and AI Designer"; empresa "ReloQuest".
  - Película del deck aprobada: contacto en negro película con quemadura, polvo y logo con halación, todo en vectores (SVG), sin mapas de bits.
  - No depender de Framer: aprobado.
  - Fase 4 aprobada: halación del logo al pasar el cursor + barrido del horizonte entre páginas.
  - Soles: todos levemente desenfocados, con brillo suave y gradiente muy sutil (amarillo cálido arriba, más quemado hacia el horizonte).
  - Le gusta la grilla actual de proyectos. De la alternativa B le gustó la grilla de tres y el revelado a color; la película en proyectos está descartada.
  - Regla de marca: el logo es geométrico y perfecto. Nada orgánico ni dibujado a mano (fue lindo, pero rompe la marca); todo efecto sale del arco, el punto y la línea.
  - La plantilla por capítulos le gusta, pero necesitaba blanco: ahora alterna secciones índigo y blancas.
- Pendiente de aprobación (ver "Pendiente de tu decisión" en `redesign/a-v2/PROPUESTAS.md`):
  - Fusión de proyectos (`projects-c/`).
  - Plantilla por capítulos evolucionada y sus textos nuevos.
  - Punto 9.
  - Archivos Lottie.
  - Publicación.
- El español debe ser una traducción fiel del inglés (mismo contenido, palabras nativas de cada idioma).
- Casos de estudio:
  - Invest in Bogotá sigue completo en índigo (`body.page-night`).
  - La plantilla por capítulos es una página clara con secciones `is-night tone-night`.
  - Color del cliente: `--client` (sobre oscuro) y `--client-ink` (sobre blanco).
- Red del entorno: `framerusercontent.com` y `*.framer.app` están bloqueados. Para descargar las Lottie, el dueño debe permitirlos en Network access.
- Nada se publica en `main` sin aprobación explícita. El sitio en vivo es `https://nicolasmb.com/` (Netlify, se actualiza desde `main` en minutos).
- Deck de Figma del dueño (Figma Slides, fileKey `A2FLZyFCZUkYItYyTG2Tgn`, portada nodo `1:2107`): fondo negro tipo película, grano, polvo/rayas, quemadura de película naranja en una esquina y el logotipo con halación (núcleo amarillo, naranja, borde magenta). El conector de Figma solo puede capturar diapositivas cuyo enlace (node-id) comparta el dueño; no puede listar las diapositivas de un deck.
- Vista previa: `https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/index.html`. Puede tardar unos minutos en reflejar un cambio; si dudas, recarga forzada.
