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
- Trabajo vigente: versión a futuro **a-v3** en `redesign/a-v3/` (EN) y `redesign/a-v3/es/` (ES), rama `redesign`. Detalle y textos por aprobar (V1–V11): `redesign/a-v3/CAMBIOS.md`.
- Versión anterior **a-v2** ("Horizonte"): congelada en `redesign/a-v2/` y en la rama `backup/a-v2-2026-11-17`. No se regenera; allí siguen PROPUESTAS.md, PLAN.md y AUDITORIA.md.
- a-v3 añade sobre a-v2:
  - Hero con texto de apoyo específico, tres cifras y la hora de Bogotá (`[data-bogota-time]`).
  - Sol del día ligado al scroll (`.day-sun`, solo en el inicio).
  - Forma del cliente en las tarjetas (`CARD_SHAPES`) y línea de tipo de trabajo + año (`card_kind`).
  - Bloque de IA con frases ya aprobadas.
  - Trayectoria plegable con `<details>` (el título del cargo queda fuera del `summary`).
  - Línea de datos en el contacto.
  - Títulos de sección a 52 px.
  - `assets/og.png`, título de página con nombre y cargo, y JSON-LD de persona.
  - La tarjeta de Colombia 4.0 no es enlace.
  - Sin las páginas `projects-a/b/c`.
- Pruebas (dentro del repo, `redesign/tools/qa/`): servir el repo en el puerto 8765 y correr con `NODE_PATH=/opt/node22/lib/node_modules` (Playwright del sistema; `npm install` ahí solo trae axe-core).
  - `node qa.js`: axe, anchos, sin JS, movimiento reducido.
  - `node measure.js`: peso, LCP, CLS.
  - `node snap.js <carpeta>` + `python3 diff.py antes después`: comparación píxel a píxel antes de refactorizar.
  - `python3 redesign/tools/prune_css.py`: quita CSS sin uso (luego regenerar).
- El generador también escribe `sitemap.xml`, `robots.txt` y `_headers` (Netlify). La CSP está en modo solo-informe: verificarla tras publicar. Una imagen o fuente que cambie debe cambiar de nombre (caché de un año).
- Generador: `python3 redesign/tools/build.py` escribe todas las páginas de **a-v3** (`OUT`); sus piezas (logo, íconos Phosphor, quemadura SVG, manifiesto de imágenes) están en `redesign/tools/parts/`. No edites el HTML generado a mano: edita el generador.
  - CSS/JS compartidos: `redesign/a-v3/assets/` (`site.css`, `site.js`). El generador calcula el `?v=<hash>` solo.
  - Todo es local: imágenes WebP en `assets/img/`, fuentes WOFF2 en `assets/fonts/`, Lottie en `assets/vendor/`. Lo único en Framer son las 3 animaciones Lottie de portada.
  - Para publicar en la raíz: `REPO_FROM_SITE = ''`, `ABS_ROOT = '/'`, `LINK_INDEX = False`.
- Páginas (EN y ES): home, `invest-in-bogota/`, `radio-a-domicilio/`, `vende-digital/`, `infinited/`, `pro-surge-ja/`, `404.html` (bilingüe), `projects-a/`, `projects-b/` y `projects-c/` (alternativas de la sección de proyectos, solo EN, noindex; C es la fusión vigente).
- Falta Colombia 4.0 (2018): no hay contenido publicado; se pidió al dueño.
- Contenido de los casos nuevos: `redesign/tools/projects.py`, tomado del sitio publicado (capturado en el scratchpad `prev/assets/orange-point-971308.framer.app/`).
- Revisión de textos: `redesign/tools/review.py` (R1…R41). El generador marca cada una en el HTML. El dueño decide en la página https://claude.ai/artifact/EaVz97Axgp22ehvcy5VmEH (colección `decisions` del artifact; leer con ArtifactData `list`).
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
  - Cada proyecto tiene su propia estructura (cada uno es diferente), pero de la misma familia (generador: `case_cover` + `case_shell` + `rad_main` / `iib_main` / `vd_main` / `inf_main` / `ps_main`).
    - La forma de cada portada es geométrica, del vocabulario del logo: ondas, sol, puntos conectados, trazos que suben y franjas diagonales.
    - La marca de cada sección usa esa misma forma.
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
  - Flecha (`go()` en el generador): al pasar el cursor se dibuja el contorno del sol y luego se rellena.
    - Se usa en botones, "View portfolio" y tarjetas de proyecto.
    - En los enlaces de Behance, solo el contorno (`go--outline`).
  - Encabezado: se queda la píldora actual.
  - Parallax: telón en Radio a Domicilio (`cover-stage--curtain`).
  - Sección de piezas: nombre descriptivo por proyecto.
  - Servicios: cuatro soles sobre un mismo horizonte que suben al entrar en pantalla, con enlaces a proyectos (propuesta R41).
  - Punto 9 aprobado e integrado en Invest in Bogotá.
  - Créditos: el dueño decide cuándo parar; no limitar el trabajo por eso.
  - Rescatado de la primera versión (Framer, en la raíz del repo):
    - Encabezado en píldora flotante que se esconde al bajar y aparece al subir.
    - Hover del CTA con círculo y flecha (reinterpretado como el punto que sube desde el horizonte).
    - Parallax en la imagen inicial de cada proyecto.
  - Halación del logo: capa ya dibujada que solo cambia de opacidad (animar `filter` desde `none` daba un brillo negro).
- Rumbo (decidido 2026-11-17, ver `redesign/a-v3/RUMBO.md`):
  - Ahora: nicho editorial, de datos y de marca para instituciones de inversión y gobierno, con sistemas e IA.
  - A futuro: design engineer.
  - No publicar la velocidad personal del dueño (tiempos y horas): mostrar alcance, calidad y sistema. Las métricas técnicas del sitio sí.
  - Gráficos interactivos candidatos G1–G6, solo con datos publicados.
  - G3 hecho en Vende Digital: `vd_chart` en `build.py`; datos y fuente en `VD_DATA` y `VD_CHART` (`projects.py`); estilos `.chart`/`.bars`/`.dots`; pestañas en `site.js` (`[data-chart]`). Es el patrón para los siguientes: tabla real con barras CSS.
  - Red del entorno: se permitieron mintic.gov.co y medios colombianos (dplnews, larepublica, elnuevosiglo, semana, elheraldo) para leer datos públicos.
- Revisión de textos R1–R41: aprobada y aplicada el 2026-11-02 (`APPLIED` en `review.py`).
  - R10 y R15 llevan la redacción del dueño.
  - R37 se interpretó como retitular "E-commerce"; está pendiente de que el dueño lo confirme.
- Ritmo vertical: `--section` (inicio, máx. 128 px) y `--section-sm` (casos, máx. 104 px). El espacio de la imagen de portada vive dentro de `.cover-stage` (un margen en la imagen se escapaba y dejaba una franja clara).
- Auditoría de UI y de perfil: `redesign/a-v2/AUDITORIA.md` (2026-11-10). Son propuestas, nada aplicado. Lo principal: el sitio no vende el perfil (sin cifras, sin prueba de IA, sin "sobre mí" ni testimonios) y la idea del "día en Bogotá" (Fase 1 del plan) sigue sin construir. El titular del hero no se toca (decisión del dueño).
- Pendiente de aprobación (ver "Pendiente de tu decisión" en `redesign/a-v2/PROPUESTAS.md`):
  - R37 (título "E-commerce").
  - Rótulo "HTML5 banners".
  - Íconos (Behance repetido, redes del footer como texto).
  - Fusión de proyectos (`projects-c/`).
  - Contenido de Colombia 4.0.
  - Archivos Lottie.
  - Publicación.
- El español debe ser una traducción fiel del inglés (mismo contenido, palabras nativas de cada idioma).
- Casos de estudio:
  - Todos son páginas claras con secciones `is-night tone-night`.
  - Color del cliente: `--client` (sobre oscuro) y `--client-ink` (sobre blanco).
- Red del entorno: `framerusercontent.com` y `*.framer.app` están bloqueados. Para descargar las Lottie, el dueño debe permitirlos en Network access.
- Nada se publica en `main` sin aprobación explícita. El sitio en vivo es `https://nicolasmb.com/` (Netlify, se actualiza desde `main` en minutos).
- Deck de Figma del dueño (Figma Slides, fileKey `A2FLZyFCZUkYItYyTG2Tgn`, portada nodo `1:2107`): fondo negro tipo película, grano, polvo/rayas, quemadura de película naranja en una esquina y el logotipo con halación (núcleo amarillo, naranja, borde magenta). El conector de Figma solo puede capturar diapositivas cuyo enlace (node-id) comparta el dueño; no puede listar las diapositivas de un deck.
- Vista previa: `https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v3/index.html` (a-v2: misma ruta con `a-v2`). Puede tardar unos minutos en reflejar un cambio; si dudas, recarga forzada.
- Lección técnica: un contenedor con `overflow: hidden` se vuelve contenedor de scroll y congela las animaciones `view()` de sus hijos. Usa `overflow: clip`.
- Higgsfield (storytelling con IA, prueba hasta el 2026-11-27): la prueba ilimitada no funciona en Claude Code, solo en chat de Claude, Cowork o ChatGPT. El dueño genera allí; el puente es el proyecto de Higgsfield `f583b208-3bef-49c8-8b24-e278a2a235e0` (workspace `5c1a64f1-6561-4d59-bd0a-1943cfe7eb69`), que se lee y se baja desde aquí (hosts `upload.higgsfield.ai` y `d2ol7oe51mr4n9.cloudfront.net` permitidos). Prompts y reglas: `redesign/a-v3/HIGGSFIELD.md`. Sin texto, logos ni la cara de la modelo de Vende Digital en lo generado.
- Encabezado en los casos: la píldora flota sobre la portada oscura (como en el inicio) y se queda blanca al 82 % (el dueño dijo "déjalos").
