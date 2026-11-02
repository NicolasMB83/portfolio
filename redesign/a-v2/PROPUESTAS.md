# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/` (inglés) y `redesign/a-v2/es/` (español).

## Sistema visual

**Vocabulario de formas tomado del logotipo:**
- **Arco** (la "n"): grosor igual a la mitad de su radio, extremos redondeados. Se usa en las viñetas de la experiencia, la teselación y el hover de los proyectos.
- **Punto** (la "i"): es el sol. También es el círculo que se expande en cada clic y la ventana del GIF en el 404.
- **Línea** (el horizonte): los títulos se apoyan en ella y suben desde ella.

**Secciones oscuras:** Proyectos, Clientes, Contacto y "Otros proyectos" en el caso de estudio. Cada una tiene su propio grano claro.

**Dos texturas para comparar en la misma página:**
- **Teselación** (por defecto): el arco de la "n" unido en una onda, con el punto de la "i" en los valles. Al 6 %, visible solo en los bordes de la sección y desvanecida detrás de los proyectos.
- **Halación** (agregar `?texture=halation` a la URL): el brillo rojo-naranja que deja la luz en la película fotográfica. Solo aparece alrededor de lo más brillante sobre fondo oscuro (el sol, los botones naranja y los títulos blancos), más una fuga de luz cálida en las esquinas y un grano un poco más marcado. Hecho con sombras y degradados, no con filtros de desenfoque, que son pesados en móvil.

## Movimiento

- **Clic:** al presionar, el botón se hunde un poco y el punto de la "i" se expande desde el lugar exacto del clic.
- **"Let’s talk":** el botón se transforma en el panel de contacto (View Transitions API) y, al cerrar, el panel vuelve al botón.
- **Entre páginas:** la portada de Invest in Bogotá crece hasta convertirse en el video del caso de estudio. Funciona en Chrome, Edge y Safari 18.2+; en Firefox la navegación es normal, sin error.
- **Curvas:** resorte críticamente amortiguado (desacelera de forma física, sin rebote; el rebote se ve anticuado).
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
| 1 | ✅ Aplicado | Email visible + Copy / Copied |
| 2 | ✅ Aplicado | La navegación dice "Let’s talk" (igual que el footer) |
| 3 | ✅ Aplicado | "Back to home". GIF aleatorio dentro del sol del 404: **necesita tu propia clave de GIPHY** (ver abajo) |
| 4 | ✅ Aplicado | "Invest in Bogotá" con tilde en todo el sitio |
| 5 | ✅ Aplicado | Un solo título: "Visual and AI Designer" (el de tu CV; quité "Senior" de la tarjeta). Dime si prefieres otro |
| 6 | ✅ Aplicado | Fechas "Feb 2025 - Aug 2025" |
| 7 | ✅ Solo la tilde | "The investment promotion agency for Bogotá – Region." |
| 8 | ✅ Aplicado (verifica) | Tu mensaje llegó cortado en este punto; lo interpreté como aprobado: "its brand", "products that demand", "AI tools", "every day" |
| 9 | ⏸ En espera | El resumen del CMS no se muestra |
| 10 | ✅ Aplicado | "Contributed to" |
| 11-14 | Pendientes | Sin respuesta todavía (ver versión anterior de este documento) |

## Nuevas propuestas de texto (pendientes)

1. **RealQuest** (Jan 2026 - Current). Título: "Graphic Designer, Creative" (alternativa: "Graphic Designer & Creative"). Viñetas:
   - Redesigned the interface of RealQuest’s main website.
   - Produce brand videos and now integrate AI video tools into the production workflow.
   - Design social media graphics and digital media pieces.
   - Create print pieces such as backdrops, and mock-ups that present each design in context.

   Confirma también que el nombre es **RealQuest** (en un mensaje escribiste "Reloquest").
2. **Todo el texto en español** es un borrador mío, fiel al inglés. Revísalo en `/es/`. Algunas decisiones:
   - "PROYECTOS" en lugar de "TRABAJO".
   - "Trayectoria" por "Career path".
   - "¡Hagamos magia!".
   - "Hablemos" por "Let’s talk".
3. **Textos nuevos de interfaz:** la invitación de idioma, "Volver al inicio" y, si activas el GIF, "Powered by GIPHY" (lo exigen los términos de GIPHY).
4. **Email inconsistente:** el sitio usa `nicolasbarbosa.us@gmail.com` y tu CV `nicolasbarbosa2002@gmail.com`. ¿Cuál debe recibir los contactos?
5. **Dominio:** tu CV menciona `www.nicolasmb.com`. Si está activo, conviene publicar ahí y actualizar las URLs `hreflang`/canonical (hoy apuntan a `nicolasmb83.github.io/portfolio/`).

## GIF aleatorio del 404

El GIF anterior usaba una clave de API que pertenece a Framer, dentro de su componente; no se puede reutilizar fuera de Framer.

Para activarlo:
1. Crea una cuenta gratuita en [developers.giphy.com](https://developers.giphy.com/docs/api/) y genera una clave. La clave inicial permite 100 llamadas por hora, suficiente para un 404.
2. Pásame la clave y la palabra de búsqueda que quieras (por ejemplo "lost" o "confused"). Yo la pongo en `data-giphy-key` y `data-giphy-tag`.

Sin clave, el 404 muestra el sol normal; con clave, el sol sube con un GIF adentro.

## Pendiente de tu lado

- **Tu deck de Figma** (`Portfolio-indepth-01-26`): el conector de Figma no pudo conectarse desde esta sesión. Si me envías un PDF o capturas de las diapositivas con la halación y la teselación, ajusto ambas texturas para que coincidan con tu material.
