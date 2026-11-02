# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/` (inglés) y `redesign/a-v2/es/` (español).

## ⏳ Pendiente de tu decisión

### A. Proyectos: ¿grilla actual, alternativa A o alternativa B?
Solo cambia la sección de proyectos; el resto de la página es igual.
- **Actual:** `index.html` (grilla de tarjetas sobre índigo).
- **A, dirección de arte por proyecto:** `projects-a/index.html`. Cada proyecto tiene su color (tomado de sus propias piezas), una forma del logotipo y su propio lugar en una composición asimétrica:
  - Radio a Domicilio: arco.
  - Invest in Bogotá: punto (círculo).
  - Colombia 4.0: arco invertido.
  - Pro Surge JA: franja.

  Detrás de cada imagen, el color del cliente se imprime levemente desfasado y, al pasar el cursor, se desplaza más.
- **B, hoja de contactos:** `projects-b/index.html`. Fondo de película negra con tiras perforadas y numeración de borde ("NMB 01 ▸ 1A").
  - Los fotogramas están casi en blanco y negro y se revelan a color al pasar el cursor.
  - Al mismo tiempo, un lápiz graso naranja los encierra en un círculo.
  - En celulares el círculo se dibuja al hacer scroll.

  Todo es vectorial.

### B. Plantilla de caso por capítulos (ejemplo: Radio a Domicilio)
Ver `radio-a-domicilio/index.html` (y `es/radio-a-domicilio/index.html`).

**Estructura:**
- **Portada tipo deck:** el título sobre el horizonte. En lugar del sol aparece la forma del cliente: ondas de radio dibujadas con el arco de la "n" en el amarillo de la marca.
- **Barra de capítulos fija** (01 Contexto · 02 Objetivos · 03 Proceso · 04 Las piezas · 05 Resultados). Marca en qué capítulo estás y en el celular se desliza sola.
- **Apertura de cada capítulo:** un número grande que sube desde la línea.
- **Proceso:** una línea del tiempo en la que el sol sale un poco más en cada fase.
- **Piezas:** incluyen los banners HTML5 reales del repositorio, animados.

**Textos nuevos que necesitan tu sí** (marcados en el HTML con `PROPUESTA DE TEXTO`):
1. Nombres de capítulo nuevos: "Context / Contexto" y "The work / Las piezas". "Objectives", "Process", "Results" y "Next steps" ya estaban en tu CMS.
2. Rótulo "HTML5 banners / Banners HTML5".
3. Textos alternativos de las 6 imágenes y los 5 banners (para lectores de pantalla).
4. La traducción al español de todo el contenido del caso. En español, "Radio at Home" queda como "Radio a Domicilio", que es el nombre original de la marca.

**Observaciones sobre los textos del CMS** (no los cambié; dime si quieres ajustarlos):
- "Audience and Style Analysis" (en Diseño y desarrollo) repite casi lo mismo que "Market and Style Study" (en Descubrimiento).
- "UI/UX Design", "User Testing" y el resumen de la portada terminan sin punto.
- "Visual engagement": lo traduje como "Conexión visual", porque "engagement" no es palabra nativa del español.

### C. Punto 9 (en espera, no se muestra)
> IBB aim is to facilitate relevant international investments and attract world-class meetings and events that contribute to the socioeconomic development, competitiveness, and quality of life of Bogotá-Region. I have to develop impactful collateral to create a strong brand presence as well as keep a coherent narrative of the brand.

### D. Las 3 portadas animadas (Lottie) siguen en Framer
Radio a Domicilio, Invest in Bogotá y Vende Digital usan animaciones Lottie alojadas en `framerusercontent.com`. Desde este entorno no pude descargarlas porque el dominio está bloqueado.

Mientras cargan, o si Framer desaparece, ahora se ve una imagen local:
- Radio a Domicilio e Invest in Bogotá muestran una de sus piezas.
- Vende Digital muestra la teselación, porque no tengo ninguna imagen suya.

Para cortar del todo con Framer:
- **Opción 1:** envíame los 3 archivos `.json`, exportados desde Framer o After Effects con Bodymovin.
- **Opción 2:** agrega `framerusercontent.com` a los dominios permitidos del entorno.

### E. Publicación en nicolasmb.com (cuando lo apruebes)
El dominio está activo en Netlify. Para publicar:
1. Mover `redesign/a-v2/` a la raíz.
2. En `redesign/tools/build.py`, poner `REPO_FROM_SITE = ''`, `ABS_ROOT = '/'` y `LINK_INDEX = False`.
3. Generar de nuevo.

Las direcciones canónicas y `hreflang` ya apuntan a `https://nicolasmb.com/`.

---

## ✅ Aplicado en esta ronda
- **Película aprobada, ahora 100 % vectorial y por defecto** (ya no hace falta `?look=film`):
  - La quemadura es un SVG en la página, con filtros estáticos (ruido, desplazamiento y desenfoque) que escalan con el dibujo.
  - El polvo y las rayas son un SVG de 1 KB.
  - El grano es ruido SVG.
  - Se borraron 4 texturas en mapa de bits (unos 93 KB), reemplazadas por unos 3 KB de vectores.
- **Sin depender de Framer:** imágenes en WebP con varios tamaños (`assets/img/`), fuentes propias en WOFF2 (Clash Display y DM Sans; ya no se usa Google Fonts) y el reproductor Lottie local. Solo quedan los 3 `.json` del punto D.
- **Fase 4:**
  - Al pasar el cursor por el logo, se enciende con halación como en tu deck: núcleo cálido con bordes coral y verde.
  - Al cambiar de página, la nueva sube desde abajo detrás de una línea de horizonte naranja que barre la pantalla. Funciona en Chrome, Edge y Safari 18.2 o superior. En otros navegadores la página carga normal, y con "reducir movimiento" no hay barrido.
- **Generador dentro del repositorio:** `redesign/tools/build.py` (antes vivía en una carpeta temporal).

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
| Película (deck) | ✅ | Aprobada; ahora vectorial y por defecto |
| No depender de Framer | ✅ | Hecho, salvo las 3 animaciones Lottie (punto D) |

## GIF aleatorio del 404

Activo con tu clave de GIPHY y la palabra "cat". Cada visita o recarga pide un gato nuevo, que sube dentro del sol.

- Con la clave inicial de GIPHY el límite es de 100 llamadas por hora. Si se supera o la API falla, el 404 muestra el sol normal, sin errores.
- Si el sitio recibe mucho tráfico, se puede pedir una clave de producción en el panel de GIPHY.
- La clave queda visible en el código público (así funcionan las claves de GIPHY en el navegador). Cualquiera podría reutilizarla y gastar ese límite. Si pasa, se genera otra y se reemplaza.

## Si ves una versión vieja

Los archivos CSS/JS ahora llevan una versión en la URL (`site.css?v=…`) que cambia con cada cambio, así que el navegador ya no puede usar una copia vieja. raw.githack puede tardar unos minutos en reflejar un cambio nuevo. Si dudas, recarga forzada: Cmd+Shift+R (Mac) o Ctrl+Shift+R (Windows).
