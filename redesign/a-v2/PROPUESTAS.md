# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/` (inglés) y `redesign/a-v2/es/` (español).

## ⏳ Pendiente de tu decisión

### A. Propuesta "película" (inspirada en tu deck)
Ver con `?look=film`. El contacto se vuelve la portada de tu deck: película negra, quemadura en la esquina superior y tu logo con halación saliendo del borde inferior. ¿Sí o no?

### B. Punto 9 (en espera, no se muestra)
> IBB aim is to facilitate relevant international investments and attract world-class meetings and events that contribute to the socioeconomic development, competitiveness, and quality of life of Bogotá-Region. I have to develop impactful collateral to create a strong brand presence as well as keep a coherent narrative of the brand.

### C. Plan de acción
Ver `PLAN.md`: hay que elegir la alternativa de la Fase 2 y reunir el contenido de los casos.

### Dominio
Tu CV menciona `www.nicolasmb.com`. Si está activo, conviene publicar ahí.

---

## ✅ Aplicado en esta ronda
- **ReloQuest, viñeta 3:** "Design social media graphics as well as digital and print collateral." Tu redacción ("digital and printed collateral") era correcta; ajusté "print" (término habitual en marketing) y "as well as" (evita "and… and").
- **Invest in Bogotá:** termina en enero de 2026 ("Feb 2025 - Jan 2026"), en Career path y en el caso de estudio.
- **Caso de estudio:** fondo índigo como las secciones oscuras del home.
- **Puntos 11, 12 y 13:**
  - "Organizations that trust my work".
  - "© 2026 Nicolás Mogollón Barbosa".
  - Nueva descripción para Google y LinkedIn.
- **Punto 14:** rechazado; el hero no cambia.
- **Español:** traducción fiel del inglés, frase por frase, con palabras nativas; aprobada la terminología del punto D.
- **404:** gatos reales vía GIPHY. Ahora con búsqueda por relevancia, para que siempre sean gatos.

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
| 11, 12, 13 | ✅ | Aplicados |
| 14 | ❌ | Rechazado |
| Email | ✅ | Se mantiene `nicolasbarbosa.us@gmail.com` |
| Secciones oscuras | ✅ | Aprobadas |

## GIF aleatorio del 404

Activo con tu clave de GIPHY y la palabra "cat". Cada visita o recarga pide un gato nuevo, que sube dentro del sol.

- Con la clave inicial de GIPHY el límite es de 100 llamadas por hora. Si se supera o la API falla, el 404 muestra el sol normal, sin errores.
- Si el sitio recibe mucho tráfico, se puede pedir una clave de producción en el panel de GIPHY.
- La clave queda visible en el código público (así funcionan las claves de GIPHY en el navegador). Cualquiera podría reutilizarla y gastar ese límite. Si pasa, se genera otra y se reemplaza.

## Si ves una versión vieja

Los archivos CSS/JS ahora llevan una versión en la URL (`site.css?v=…`) que cambia con cada cambio, así que el navegador ya no puede usar una copia vieja. raw.githack puede tardar unos minutos en reflejar un cambio nuevo. Si dudas, recarga forzada: Cmd+Shift+R (Mac) o Ctrl+Shift+R (Windows).
