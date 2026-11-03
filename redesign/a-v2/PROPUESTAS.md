# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/` (inglés) y `redesign/a-v2/es/` (español).

## ⏳ Pendiente de tu decisión (ronda actual)

Lo que falta para dejar el sitio listo para publicar:

1. **R37 (Pro Surge JA):** aprobaste la propuesta, pero no tenía texto definido. Como el objetivo describe un comercio electrónico, cambié su título de "Market Research" a **"E-commerce" / "Comercio electrónico"**. Si el objetivo era otro, dímelo y lo ajusto.
2. **Rótulo "HTML5 banners" / "Banners HTML5"** en Radio a Domicilio: es el único texto nuevo que sigue marcado como propuesta.
3. **Íconos:** ¿quito el logo de Behance que repite la palabra "Behance" y cambio los círculos de redes del footer por texto ("LinkedIn ↗ · Behance ↗ · Email")?
4. **Sección de proyectos del inicio:** ¿se queda la grilla actual o pasa a la fusión ([projects-c](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/projects-c/index.html))?
5. **Colombia 4.0 (2018):** falta su contenido para construir la página.
6. **Las 3 animaciones Lottie** siguen en Framer (ver más abajo).
7. **Publicar** en nicolasmb.com.

## ✅ Aplicado en esta ronda (arte final)
- **Revisión de textos:** las 41 propuestas aprobadas, aplicadas en inglés y español.
  - R10 y R15 con tu redacción: "sales funnels" y el rebranding en el primer trimestre de 2025.
  - El nombre "ProSurge JA" se escribe igual en toda su página.
  - Se quitaron los marcadores de propuesta de todo lo aprobado.
- **Espaciado:** un solo ritmo vertical, más compacto.
  - Entre secciones del inicio: de 158 px a 128 px (en pantallas de 1440 px).
  - Entre secciones de un caso: 100 px.
  - Antes de cada bloque oscuro: de 316 px a 200 px.
- **Errores corregidos:**
  - En la portada de los casos, una franja clara de unos 40 px aparecía entre la ficha (Año / Empresa / Rol) y la imagen. Era un margen que se escapaba de su bloque.
  - "Other work": en Vende Digital, las dos tarjetas no llenaban el ancho. Ahora siempre son dos tarjetas iguales, con el mismo marco.
  - Las marcas de sección (puntos, trazos, franjas) quedaban bajo la línea y se veían cortadas; ahora se apoyan en el horizonte.
  - En celular, la segunda línea del hero ("and I turn that passion into results") pasaba por encima del sol; ahora se corta antes.
- **Verificado:** los banners HTML5 de Radio a Domicilio funcionan; en las capturas de página completa salían vacíos, pero eso es un efecto de la captura.
- **Pruebas:** todas las páginas en escritorio, tablet y celular, en inglés y español, con accesibilidad (axe), anchos de 320 a 2560 px, sin JavaScript y con "reducir movimiento".

## Pendiente de rondas anteriores

### Las 3 portadas animadas (Lottie) siguen en Framer
Radio a Domicilio, Invest in Bogotá y Vende Digital usan animaciones Lottie alojadas en Framer. Probé con tu enlace `orange-point-971308.framer.app`, pero la política de red de este entorno bloquea tanto ese dominio como `framerusercontent.com`.

**Opción 1: habilitarlos.**
1. Abre el menú del entorno en la barra del título de la sesión y elige **Edit**.
2. En **Network access**, agrega `orange-point-971308.framer.app` y `framerusercontent.com` en **Allowed domains**. Deja marcada la casilla de gestores de paquetes.

Guía: https://code.claude.com/docs/en/cloud-environments#network-access. Después, avísame y las descargo.

**Opción 2: enviarme los 3 archivos `.json`.**

Mientras tanto, se ve una imagen local (Vende Digital muestra la teselación).

### Publicación en nicolasmb.com (cuando lo apruebes)
El dominio está activo en Netlify. Para publicar:
1. Mover `redesign/a-v2/` a la raíz.
2. En `redesign/tools/build.py`, poner `REPO_FROM_SITE = ''`, `ABS_ROOT = '/'` y `LINK_INDEX = False`.
3. Generar de nuevo.

Las direcciones canónicas y `hreflang` ya apuntan a `https://nicolasmb.com/`.

---

## ✅ Aplicado en la ronda anterior
- **Tipografía, medida contra la versión publicada** (a 1440 px):

  | Elemento | Ahora |
  |---|---|
  | "I LOVE DESIGN" | 70 px, Clash Display 700 |
  | Segunda línea del hero | 42 px |
  | Títulos de sección | 70 px |
  | Títulos de proyecto | 20 px, Clash 700 |
  | Servicios y cargos | 24 px |
  | "Let’s make magic!" | 120 px |
  | Menú, idioma y botón | Clash Display 700 |
  | Texto corrido | Albert Sans 16 px (como en la publicada) |
  | Rótulos pequeños | DM Sans |

- **Fondo:** el azul claro de la versión publicada (`#eef2ff`).
- **Píldora:** blanca al 82 % sobre ese azul, como la tuya, con un leve desenfoque del fondo.
- **Hero:** "I LOVE DESIGN and I turn that passion into results" ya no queda partida por la línea. La frase completa está sobre el horizonte y el sol se pone a su lado.
- **Footer:**
  - La película negra se quitó: ahora usa el índigo del sitio.
  - El logo grande en blanco sale del borde inferior; al entrar en pantalla, sus letras suben una tras otra, como el logotipo.
  - La halación se queda solo en el logo del encabezado.
- **Arco en las imágenes:** eliminado de todas las secciones; ahora son marcos redondeados.
- **Botón "Let’s talk":** al pasar el cursor, primero se dibuja el contorno del sol (desde abajo, donde está el horizonte), después se rellena y la flecha gira de ↗ a →.
- **Parallax:**
  - **Error corregido:** el marco con `overflow: hidden` congelaba la animación ligada al scroll; con `overflow: clip` ya se mueve. El mismo error impedía el leve zoom de las imágenes de proyectos, que ahora también funciona.
  - **Movimiento más notorio:** la imagen va unos 15–20 % más lenta que la página.
  - **Navegadores sin soporte:** se agregó un respaldo en JavaScript.
- **Invest in Bogotá:** pasó a la plantilla por capítulos (fondo claro, números), igual que Radio a Domicilio.

## Aplicado antes
- **Soles** (todos: hero, panel de contacto, caso de estudio, 404, el sol de los proyectos, "View portfolio" y el proceso):
  - Un desenfoque leve y un brillo suave, para que se lean como sol.
  - Un gradiente muy sutil: de un amarillo más cálido arriba a un tono un poco más quemado hacia el horizonte.
  - Es un gradiente CSS, igual de vectorial que un SVG: no tiene píxeles y escala a cualquier tamaño.
  - El desenfoque es estático (no se anima), como recomiendan las guías de rendimiento.
  - En el 404, el GIF del gato se ve nítido dentro del sol y solo el borde brilla.
- **Fase 4 aprobada:** la halación del logo y el barrido del horizonte quedan.
- **Película vectorial aprobada.**

- Película 100 % vectorial y por defecto: quemadura SVG con filtros estáticos, polvo SVG y grano SVG. Las texturas en mapa de bits se borraron.
- Sin depender de Framer, salvo las 3 animaciones Lottie (punto D).
- Generador dentro del repositorio: `redesign/tools/build.py`.

## Sistema visual

**Vocabulario de formas tomado del logotipo:**
- **Arco** (la "n"): grosor igual a la mitad de su radio, extremos redondeados. Se usa en las viñetas de la experiencia, la teselación y el hover de los proyectos.
- **Punto** (la "i"): es el sol. También es el círculo que se expande en cada clic y la ventana del GIF en el 404.
- **Línea** (el horizonte): los títulos se apoyan en ella y suben desde ella.

**Secciones oscuras:** Proyectos, Clientes y "Otros proyectos" en índigo; Contacto en película negra (portada de tu deck). Cada una tiene su propio grano claro.

**Textura elegida: teselación.** El arco de la "n" unido en una onda, con el punto de la "i" en los valles. Aparece en dos lugares:
- En los bordes de las secciones oscuras, al 6 %.
- Ocupando el lugar de las imágenes mientras cargan, o si una no carga.

La halación se probó y se descartó.

## Movimiento

- **Clic:** al presionar, el botón se hunde un poco y el punto de la "i" se expande desde el lugar exacto del clic.
- **Panel de contacto ("Let’s talk"):**
  - Entra en unos 0,4 s con desaceleración fuerte y sale más rápido (unos 0,2 s), como recomiendan las guías de movimiento actuales.
  - Adentro, el sol sale, el título sube desde la línea y el resto aparece en secuencia, cada elemento unos 40 ms después del anterior.
  - Se descartó la versión anterior, en la que el botón se transformaba en el panel.
- **Soles:** levemente desenfocados, con brillo y un gradiente sutil (amarillo cálido a quemado).
- **Entre páginas:** la línea del horizonte barre la pantalla de abajo hacia arriba y la página nueva sube detrás de ella (0,66 s). El encabezado se queda quieto.
- **Logo:** halación al pasar el cursor (es un cambio de luz, no de movimiento).
- **Curvas:** resorte críticamente amortiguado (sin rebote).
- **Accesibilidad:** con "reducir movimiento" activo, todo es instantáneo.

## Idiomas (inglés y español)

Lo que hacen las grandes empresas y recomienda Google:

- **Nunca redirigir automáticamente según el idioma o la IP.** Google lo desaconseja porque impide que personas y buscadores lleguen a la otra versión.
- **Una URL propia por idioma** (`/` y `/es/`), con etiquetas `hreflang` (incluida `x-default`).
- **Selector siempre visible:** cada idioma escrito en su propio idioma ("Español" / "English"), sin banderas, porque las banderas representan países, no idiomas.
- **La automatización es una sugerencia:** si el navegador prefiere el otro idioma, aparece una pequeña invitación ("¿Prefieres ver el sitio en español?"). Si la cierras o eliges un idioma, se recuerda y no vuelve a aparecer.
- **El 404 es una sola página** que se muestra en español cuando el navegador lo prefiere, sin cambiar de URL.

## Aprobaciones

| # | Estado | Qué se hizo |
|---|---|---|
| 1 | ✅ | Email visible + Copy / Copied |
| 2 | ✅ | La navegación dice "Let’s talk" |
| 3 | ✅ | "Back to home" + GIF aleatorio de gatos dentro del sol del 404 (cambia en cada recarga) |
| 4 | ✅ | "Invest in Bogotá" con tilde en todo el sitio |
| 5 | ✅ | Título único "Visual and AI Designer" |
| 6 | ✅ | Fechas de Invest in Bogotá: "Feb 2025 - Jan 2026" |
| 7 | ✅ | Solo la tilde: "Bogotá – Region." |
| 8 | ✅ | "its brand", "products that demand", "AI tools", "every day" |
| 9 | ⏸ | En espera: ver sección B arriba |
| 10 | ✅ | "Contributed to" |
| 11, 12, 13 | ✅ | Aplicados |
| 14 | ❌ | Rechazado |
| Email | ✅ | Se mantiene `nicolasbarbosa.us@gmail.com` |
| Secciones oscuras | ✅ | Aprobadas |
| Película (deck) | ↩️ | Retirada del footer por decisión tuya: rompía la estética. Queda la halación del logo del encabezado |
| Fase 4 | ✅ | Halación del logo y barrido del horizonte |
| Película en proyectos (B) | ❌ | Descartada: la película se queda solo en el contacto |
| Formas orgánicas / a mano | ❌ | No van con la marca: todo debe ser geometría del logo |
| Arco como ventana de imagen | ❌ | Eliminado de todas las secciones |
| Punto 9 | ✅ | Integrado en el Contexto de Invest in Bogotá |
| No depender de Framer | ✅ | Hecho, salvo las 3 animaciones Lottie (punto D) |

## GIF aleatorio del 404

Activo con tu clave de GIPHY y la palabra "cat". Cada visita o recarga pide un gato nuevo, que sube dentro del sol.

- Con la clave inicial de GIPHY el límite es de 100 llamadas por hora. Si se supera o la API falla, el 404 muestra el sol normal, sin errores.
- Si el sitio recibe mucho tráfico, se puede pedir una clave de producción en el panel de GIPHY.
- La clave queda visible en el código público (así funcionan las claves de GIPHY en el navegador). Cualquiera podría reutilizarla y gastar ese límite. Si pasa, se genera otra y se reemplaza.

## Si ves una versión vieja

Los archivos CSS/JS ahora llevan una versión en la URL (`site.css?v=…`) que cambia con cada cambio, así que el navegador ya no puede usar una copia vieja. raw.githack puede tardar unos minutos en reflejar un cambio nuevo. Si dudas, recarga forzada: Cmd+Shift+R (Mac) o Ctrl+Shift+R (Windows).
