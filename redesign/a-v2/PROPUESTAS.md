# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/` (inglés) y `redesign/a-v2/es/` (español).

## ⏳ Pendiente de tu decisión (todo en un solo lugar)

Responde con el número y "sí", "no" o tu versión.

### A. ReloQuest (ya visible en Career path, primera posición)
- **Fechas:** Jan 2026 - Current
- **Título:** "Graphic Designer, Creative" (alternativa: "Graphic Designer & Creative")
- **Viñetas:**
  1. Redesigned the interface of ReloQuest’s main website.
  2. Produce brand videos and now integrate AI video tools into the production workflow.
  3. Design social media graphics and digital media pieces.
  4. Create print pieces such as backdrops, and mock-ups that present each design in context.

### B. Punto 9 (en espera, no se muestra en la página)
Este resumen estaba en tu CMS de Framer pero la página antigua no lo mostraba. La propuesta es ponerlo como introducción del caso de estudio de Invest in Bogotá, debajo del video:
> IBB aim is to facilitate relevant international investments and attract world-class meetings and events that contribute to the socioeconomic development, competitiveness, and quality of life of Bogotá-Region. I have to develop impactful collateral to create a strong brand presence as well as keep a coherent narrative of the brand.

### C. Puntos 11 a 14
| # | Dónde | Hoy | Propuesta | Por qué |
|---|---|---|---|---|
| 11 | Clientes | "Organizations that have trust in me" | "Organizations that trust my work" | Más natural en inglés. |
| 12 | Footer | "2025 Nicolas Mogollón Barbosa" | "© 2026 Nicolás Mogollón Barbosa" | Año actual y tilde en tu nombre. |
| 13 | Descripción para Google y LinkedIn | "Welcome to my online portfolio - a showcase of innovative designs and creative web solutions." | "Nicolás Mogollón Barbosa, visual and brand designer. Campaigns, identities and digital products for MinTIC, Invest in Bogotá, Radio a Domicilio and more." | Es lo que aparece en Google y al compartir el link. |
| 14 | Hero (opcional) | "I'm Nicolás, a multidisciplinary designer with experience in Product and Digital Design, creating campaigns on social media." | "I'm Nicolás, a multidisciplinary designer. I've designed campaigns, identities and digital products for MinTIC, Invest in Bogotá and Radio a Domicilio." | Nombres reales generan confianza más rápido que adjetivos. |

### D. Versión en español (borrador completo para revisar)
Está en `redesign/a-v2/es/`. Todo es traducción mía y fiel al inglés. Decisiones a confirmar:
- "PROYECTOS" en lugar de "TRABAJO".
- "Trayectoria" por "Career path".
- "¡Hagamos magia!".
- "Hablemos" por "Let’s talk".
- "Diseñador visual y de IA".

### E. Textos nuevos de interfaz
- La invitación de idioma: "¿Prefieres ver el sitio en español?" / "Prefer to read this site in English?"
- "Volver al inicio".
- "Powered by GIPHY".

### F. Dominio
Tu CV menciona `www.nicolasmb.com`. Si está activo, conviene publicar ahí.

---

## Sistema visual

**Vocabulario de formas tomado del logotipo:**
- **Arco** (la "n"): grosor igual a la mitad de su radio, extremos redondeados. Se usa en las viñetas de la experiencia, la teselación y el hover de los proyectos.
- **Punto** (la "i"): es el sol. También es el círculo que se expande en cada clic y la ventana del GIF en el 404.
- **Línea** (el horizonte): los títulos se apoyan en ella y suben desde ella.

**Secciones oscuras:** Proyectos, Clientes, Contacto y "Otros proyectos" en el caso de estudio. Cada una tiene su propio grano claro.

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
- **Entre páginas:** un fundido corto; el encabezado se queda quieto.
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
| 6 | ✅ | Fechas "Feb 2025 - Aug 2025" |
| 7 | ✅ | Solo la tilde: "Bogotá – Region." |
| 8 | ✅ | "its brand", "products that demand", "AI tools", "every day" |
| 9 | ⏸ | En espera: ver sección B arriba |
| 10 | ✅ | "Contributed to" |
| 11-14 | ⏳ | Ver sección C arriba |
| Email | ✅ | Se mantiene `nicolasbarbosa.us@gmail.com` |
| Secciones oscuras | ✅ | Aprobadas |

## GIF aleatorio del 404

Activo con tu clave de GIPHY y la palabra "cat". Cada visita o recarga pide un gato nuevo, que sube dentro del sol.

- Con la clave inicial de GIPHY el límite es de 100 llamadas por hora. Si se supera o la API falla, el 404 muestra el sol normal, sin errores.
- Si el sitio recibe mucho tráfico, se puede pedir una clave de producción en el panel de GIPHY.
- La clave queda visible en el código público (así funcionan las claves de GIPHY en el navegador). Cualquiera podría reutilizarla y gastar ese límite. Si pasa, se genera otra y se reemplaza.

## Si ves una versión vieja

Los archivos CSS/JS ahora llevan una versión en la URL (`site.css?v=…`) que cambia con cada cambio, así que el navegador ya no puede usar una copia vieja. raw.githack puede tardar unos minutos en reflejar un cambio nuevo. Si dudas, recarga forzada: Cmd+Shift+R (Mac) o Ctrl+Shift+R (Windows).
