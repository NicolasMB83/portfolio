# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/`.

## El concepto

Tu logotipo son letras que asoman sobre una línea, como un sol saliendo en el horizonte. Ese gesto se volvió el sistema de toda la página:

- **La línea (horizonte):** los títulos se apoyan en una línea de tinta índigo y suben desde ella al aparecer.
- **El sol:** un medio círculo naranja, construido con los mismos arcos de tu logo. Sale en el hero, se oculta cuando haces scroll y vuelve a salir detrás de "Let's make magic!", así que la página abre y cierra con el mismo gesto.
- **Hover en proyectos:** un pequeño sol sube desde el borde inferior de la portada. Reemplaza los círculos con flecha, que eran una plantilla de Framer.
- **404:** el número queda cortado por el horizonte, exactamente como tu logotipo, y el sol casi se ha puesto.
- **Caso de estudio:** el círculo se vuelve el "punto rojo" de Invest in Bogotá (#EF491F, de su manual de marca). Así la página habla el idioma visual del cliente sin perder el tuyo.
- **Textura:** un grano de papel muy sutil, porque eres diseñador gráfico y la pantalla puede sentirse impresa.

## Contacto (UX 2026)

Lo que recomiendan las fuentes actuales:

- **El problema del `mailto:`:** falla para quien usa correo web (Gmail en el navegador) y hace difícil copiar la dirección.
- **El patrón más sólido:** mostrar la dirección visible, con un botón de copiar y el enlace de correo como alternativa.

Implementado así:

- **CONTACT** (navegación) abre un panel lateral (en móvil, una hoja inferior) con: email visible, botón Copy, Let’s talk (abre el correo), Download CV, LinkedIn y Behance. No pierdes tu lugar en la página.
- **Funciona sin JavaScript:** si el JS no carga, CONTACT sigue bajando a la sección final.
- **Accesibilidad:** el panel es un `<dialog>` nativo. El foco entra al panel, Esc lo cierra y el lector de pantalla anuncia "Copied".
- **Formulario (opcional):** si más adelante quieres un formulario, GitHub Pages necesita un servicio externo (p. ej. Formspree). Lo dejo como opción, no implementado.

## Propuestas de texto (pendientes de tu aprobación)

Marcadas en el HTML con `<!-- PROPUESTA DE TEXTO -->`. Nada de esto se ha cambiado en el contenido existente, salvo lo indicado como "implementado".

| # | Dónde | Hoy | Propuesta | Por qué |
|---|---|---|---|---|
| 1 | Contacto | (no existe) | Email visible + botones "Copy" / "Copied" | **Implementado en el prototipo.** Necesario para que el contacto funcione con correo web. |
| 2 | Navegación vs. footer | "CONTACT" y "Let’s talk" | Usar un solo nombre para la misma acción (p. ej. "Let’s talk" en ambos) | Dos etiquetas para la misma intención confunden. |
| 3 | 404 | "Volver" | "Back to home" | El sitio está en inglés. |
| 4 | Nombre del cliente | "Invest in Bogota" (tarjeta) / "Invest in Bogotá" (experiencia) | "Invest in Bogotá" en todo el sitio | Es el nombre oficial de la marca, con tilde. |
| 5 | Rol en IiB | "Senior Visual and A.I. Designer" (tarjeta) / "Visual and AI Designer" (experiencia) | Un solo título en todo el sitio | Un reclutador nota la inconsistencia. |
| 6 | Fechas IiB | CMS: "Feb 2025 - Current" / Career path: "Feb 2025 - Aug 2025" | Usar el dato real | En el caso de estudio usé "Feb 2025 - Aug 2025". |
| 7 | Resumen IiB | "The investment promotion agency for Bogota – Region." | "The investment promotion agency for Bogotá and its region." | Quita la raya y la tilde faltante. |
| 8 | Retos IiB | "preserve it's brand", "products that demands", "A.I tools", "researching everyday" | "preserve its brand", "products that demand", "AI tools", "researching every day" | Gramática. |
| 9 | Overview IiB | (estaba en tu CMS, no se mostraba) | Mostrarlo como introducción del caso | Da contexto en 10 segundos. Revisa si lo quieres. |
| 10 | Experiencia | "Contributed in strategic planning sessions" | "Contributed to strategic planning sessions" | Gramática. |
| 11 | Clientes | "Organizations that have trust in me" | "Organizations that trust my work" | Más natural en inglés. |
| 12 | Footer | "2025 Nicolas Mogollón Barbosa" | "© 2026 Nicolás Mogollón Barbosa" | Año actual y tilde en tu nombre. |
| 13 | Meta descripción (Google) | "Welcome to my online portfolio - a showcase of innovative designs…" | Algo específico: quién eres, qué haces, para quién | Es lo que aparece en Google y LinkedIn. |
| 14 | Hero (opcional) | "I'm Nicolás, a multidisciplinary designer with experience in Product and Digital Design, creating campaigns on social media." | Nombrar dónde y para quién has trabajado (ya está en la página: MinTIC, Invest in Bogotá, Radio a Domicilio) | Un reclutador decide en ~30 segundos; los nombres reales generan confianza más rápido que los adjetivos. |

## Sugerencias para que el sitio sea lo más profesional posible

En orden de impacto:

1. **Un caso de estudio por proyecto**, con la misma estructura que el de Invest in Bogotá: contexto, reto, decisiones, piezas y **resultado medible** cuando exista. Es lo que más piden quienes contratan: ver cómo piensas, no solo piezas sueltas.
2. **Dejar de depender de Framer para imágenes y fuentes.** Hoy todo carga desde `framerusercontent.com`; si un día borras ese proyecto en Framer, el sitio se queda sin imágenes. Conviene copiarlas al repositorio.
3. **Imagen para compartir (Open Graph).** Hoy, al pegar el link en LinkedIn o WhatsApp, no aparece ninguna imagen. Una imagen 1200×630 con tu logo y el sol lo resuelve.
4. **Dominio propio** en lugar de `github.io`.
5. **Un retrato tuyo** cuando lo tengas. Ya hay un lugar natural para él en el panel de contacto o junto a "Career path".
6. **Analítica respetuosa** (Plausible o Umami) para saber qué proyectos abren los reclutadores.
7. **Versión en español** si también buscas clientes locales.
8. **Modo oscuro** automático (la paleta noche ya existe; es una extensión natural).

## Referentes

Portfolios y galerías que encontré en la investigación:

- **Bethany Heck e Ivo Mynttinen:** portfolios centrados en la tipografía, en [Case Study Club](https://www.casestudy.club/journal/ux-designer-portfolio).
- **Angello Torres** (identidad gráfica fuerte) y **Tommy Arnold** (sitio tipográfico con parallax sutil), en [Sitebuilder Report](https://www.sitebuilderreport.com/inspiration/portfolio-websites).
- **Studio Size, LoveFrom y Alessandro Scarpellini:** estudios más que portfolios personales, en [Refs Gallery](https://refs.gallery/margins/best-typography-websites-2026).
- **Galerías curadas:** [Typewolf](https://www.typewolf.com/portfolio-sites), [A1 Gallery](https://www.a1.gallery/websites/typographic-portfolio) y [Muzli, top 100](https://muz.li/blog/top-100-most-creative-and-unique-portfolio-websites-of-2025/).

Lo que tienen en común y que aplicamos aquí:

- Una sola idea visual propia, repetida con disciplina.
- El trabajo aparece pronto y grande.
- Navegación y contacto simples.
- Casos de estudio que muestran el razonamiento.
