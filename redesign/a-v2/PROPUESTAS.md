# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/` (inglés) y `redesign/a-v2/es/` (español).

## ⏳ Pendiente de tu decisión

### A. Proyectos: fusión (alternativa C)
Tu respuesta: te gusta la actual. De la B te atrajo la grilla de tres (equilibra y evita tanto scroll) y el efecto al pasar el cursor, pero la película y el círculo a mano no van con la marca. La fusión está en `projects-c/index.html`:
- **Superficie:** la sección índigo actual, con la teselación mientras cargan las imágenes.
- **Composición:** la grilla de la B, tres fotogramas iguales por fila (dos en tablet, uno en celular).
- **Efecto al pasar el cursor:**
  - La imagen pasa a color, como en la B.
  - El círculo a mano se vuelve la geometría de la marca: cada fila se apoya en un solo horizonte continuo. Al pasar el cursor, el tramo de ese proyecto se enciende en naranja de izquierda a derecha y, al final de la línea, sale el sol con la flecha. Es decir: letras que salen de una línea.
- **Celulares** (sin cursor): todo a color, con la línea encendida y el sol visible.

¿Reemplazamos la grilla actual por esta?

### B. Plantilla por capítulos, evolucionada (Radio a Domicilio)
Tu respuesta: te gusta, pero le faltaba blanco. Ahora alterna como un día:
- **Índigo:** la portada (tipo deck) y "Las piezas" (las imágenes resaltan sobre oscuro).
- **Blanco:** Contexto, Objetivos, Proceso y Resultados.

Sobre blanco, los números de capítulo usan el violeta de Radio a Domicilio (el amarillo no se lee sobre blanco); sobre índigo, el amarillo. Si la apruebas, Invest in Bogotá pasa también a esta plantilla.

**Textos nuevos que siguen pendientes de tu sí** (marcados en el HTML con `PROPUESTA DE TEXTO`):
1. Nombres de capítulo nuevos: "Context / Contexto" y "The work / Las piezas". "Objectives", "Process", "Results" y "Next steps" ya estaban en tu CMS.
2. Rótulo "HTML5 banners / Banners HTML5".
3. Textos alternativos de las 6 imágenes y los 5 banners (para lectores de pantalla).
4. La traducción al español de todo el contenido del caso. En español, "Radio at Home" queda como "Radio a Domicilio", que es el nombre original de la marca.

**Observaciones sobre los textos del CMS** (no los cambié):
- "Audience and Style Analysis" repite casi lo mismo que "Market and Style Study".
- "UI/UX Design", "User Testing" y el resumen terminan sin punto.
- "Visual engagement" quedó como "Conexión visual".

### C. Punto 9 (en espera, no se muestra)
> IBB aim is to facilitate relevant international investments and attract world-class meetings and events that contribute to the socioeconomic development, competitiveness, and quality of life of Bogotá-Region. I have to develop impactful collateral to create a strong brand presence as well as keep a coherent narrative of the brand.

### D. Las 3 portadas animadas (Lottie) siguen en Framer
Radio a Domicilio, Invest in Bogotá y Vende Digital usan animaciones Lottie alojadas en Framer. Probé con tu enlace `orange-point-971308.framer.app`, pero la política de red de este entorno bloquea tanto ese dominio como `framerusercontent.com`.

**Opción 1: habilitarlos.**
1. Abre el menú del entorno en la barra del título de la sesión y elige **Edit**.
2. En **Network access**, agrega `orange-point-971308.framer.app` y `framerusercontent.com` en **Allowed domains**. Deja marcada la casilla de gestores de paquetes.

Guía: https://code.claude.com/docs/en/cloud-environments#network-access. Después, avísame y las descargo.

**Opción 2: enviarme los 3 archivos `.json`.**

Mientras tanto, se ve una imagen local (Vende Digital muestra la teselación).

### E. Publicación en nicolasmb.com (cuando lo apruebes)
El dominio está activo en Netlify. Para publicar:
1. Mover `redesign/a-v2/` a la raíz.
2. En `redesign/tools/build.py`, poner `REPO_FROM_SITE = ''`, `ABS_ROOT = '/'` y `LINK_INDEX = False`.
3. Generar de nuevo.

Las direcciones canónicas y `hreflang` ya apuntan a `https://nicolasmb.com/`.

---

## ✅ Aplicado en esta ronda
- **Logo:** se corrigió el brillo negro que aparecía antes de la halación.
  - Causa: una sombra que arranca desde "sin filtro" se interpola desde el color del texto, que en el logo es índigo oscuro.
  - Solución: la halación está ya dibujada en una copia debajo del logo, y al pasar el cursor solo cambia su opacidad. Además es más liviano.
- **Encabezado en píldora** (rescatado de la primera versión):
  - La píldora flota con el logo, las secciones y el botón.
  - Se esconde al bajar y reaparece apenas subes un poco. No se esconde cerca del inicio, con el menú abierto, ni si navegas con el teclado dentro de ella.
  - En celular, el menú se abre como un panel redondeado debajo de la píldora.
  - En los casos de estudio, la barra de capítulos también es una píldora y sube cuando el encabezado se esconde.
  - Las secciones del menú usan Clash Display, como en la primera versión.
- **Botón "Let’s talk":** al pasar el cursor, el punto de la "i" sube desde el borde inferior del botón (su horizonte) detrás de la flecha, y la flecha gira de ↗ a →. Es la idea del original (círculo blanco con flecha), pero contada con el lenguaje del logo y con movimiento de resorte.
- **Parallax al inicio de cada proyecto** (rescatado de la primera versión):
  - Radio a Domicilio: el collage de marca, en un marco redondeado, se mueve más lento que la página.
  - Invest in Bogotá: el video flota dentro de su franja roja.
  - Se hace con animación ligada al scroll en CSS (sin JavaScript), se apaga con "reducir movimiento" y en navegadores sin soporte se ve la imagen quieta.

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
| Película (deck) | ✅ | Aprobada; vectorial y por defecto |
| Fase 4 | ✅ | Halación del logo y barrido del horizonte |
| Película en proyectos (B) | ❌ | Descartada: la película se queda solo en el contacto |
| Formas orgánicas / a mano | ❌ | No van con la marca: todo debe ser geometría del logo |
| No depender de Framer | ✅ | Hecho, salvo las 3 animaciones Lottie (punto D) |

## GIF aleatorio del 404

Activo con tu clave de GIPHY y la palabra "cat". Cada visita o recarga pide un gato nuevo, que sube dentro del sol.

- Con la clave inicial de GIPHY el límite es de 100 llamadas por hora. Si se supera o la API falla, el 404 muestra el sol normal, sin errores.
- Si el sitio recibe mucho tráfico, se puede pedir una clave de producción en el panel de GIPHY.
- La clave queda visible en el código público (así funcionan las claves de GIPHY en el navegador). Cualquiera podría reutilizarla y gastar ese límite. Si pasa, se genera otra y se reemplaza.

## Si ves una versión vieja

Los archivos CSS/JS ahora llevan una versión en la URL (`site.css?v=…`) que cambia con cada cambio, así que el navegador ya no puede usar una copia vieja. raw.githack puede tardar unos minutos en reflejar un cambio nuevo. Si dudas, recarga forzada: Cmd+Shift+R (Mac) o Ctrl+Shift+R (Windows).
