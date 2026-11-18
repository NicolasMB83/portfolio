# Versión a futuro (a-v3)

Construida el 17 de noviembre de 2026 a partir de la auditoría (`redesign/a-v2/AUDITORIA.md`). No está publicada.

## Dónde está cada versión

| Versión | Dónde | Estado |
|---|---|---|
| Actual (a-v2) | Carpeta `redesign/a-v2/` y rama `backup/a-v2-2026-11-17` | Guardada, no se toca |
| A futuro (a-v3) | Carpeta `redesign/a-v3/`, rama `redesign` | En trabajo; el generador (`redesign/tools/build.py`) ahora escribe aquí |
| Sitio en vivo | Rama `main` | Sin cambios |

Vista previa:
- Actual: https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/index.html
- A futuro: https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v3/index.html

## Qué cambió frente a la versión actual

### Vender el perfil
- **Hero:** el titular no cambia. Debajo, el texto de apoyo ahora dice cargo, ciudad, años y clientes. A la derecha hay tres cifras: 9 años de experiencia, 5 organizaciones y 2 idiomas.
- **Hora de Bogotá:** una línea con la hora local en vivo y la zona horaria (GMT−5).
- **Tarjetas de proyecto:** dicen el tipo de trabajo y el año ("Campaigns, presentations and web · 2025") en lugar del cargo.
- **Bloque "AI in my workflow":** tres frases sobre tu uso de la IA, tomadas de textos que ya tenías aprobados (ReloQuest e Invest in Bogotá).
- **Contacto:** una línea con ciudad, idiomas y disponibilidad.
- **"View portfolio"** pasa a "See the full deck", porque el enlace lleva al deck de Figma.

### Ser único
- **El día en Bogotá:** después del amanecer del hero, un sol pequeño recorre el borde derecho con el scroll. Sube rápido, se queda arriba sobre los proyectos y se pone al llegar al contacto. Se apaga con "reducir movimiento" y en navegadores sin soporte.
- **La forma de cada cliente en su tarjeta:** al pasar el cursor, suben desde el borde las ondas de Radio a Domicilio, el punto de Invest in Bogotá, los puntos de Vende Digital, los trazos de Infinited o las franjas de Pro Surge.

### Pulido
- **Jerarquía:** los títulos de sección bajan de 70 a 52 px, para que mande el titular.
- **Trayectoria plegable:** cargo, empresa y fechas siempre visibles; las viñetas se abren con "What I did". El primer cargo viene abierto. La sección pasa de unos 1875 a unos 1450 px (medido a 1440 px de ancho).
- **Celular:** se quitó la doble línea bajo "Career path".
- **Colombia 4.0:** su tarjeta ya no es un enlace roto; dice "Case study coming soon".

### Fuera del sitio
- **Imagen para compartir** (1200 × 630 px, 65 KB) en LinkedIn y WhatsApp: `assets/og.png`.
- **Título de la página:** "Nicolás Mogollón Barbosa · Visual and AI Designer".
- **Datos de persona para Google:** nombre, cargo, ciudad, idiomas y redes.

## Textos nuevos que necesitan tu sí

Están marcados en el HTML con `PROPUESTA DE TEXTO`.

| # | Dónde | Inglés | Español |
|---|---|---|---|
| V1 | Texto de apoyo del hero | I’m Nicolás, a visual and AI designer based in Bogotá. For nine years I’ve turned public programs, universities and brands into identities, campaigns and websites, for MinTIC, Invest in Bogotá and ReloQuest. | Soy Nicolás, diseñador visual y de IA en Bogotá. Desde hace nueve años convierto programas públicos, universidades y marcas en identidades, campañas y sitios web, para MinTIC, Invest in Bogotá y ReloQuest. |
| V2 | Cifras del hero | 9 years of experience · 5 organizations · 2 languages | 9 años de experiencia · 5 organizaciones · 2 idiomas |
| V3 | Línea de ubicación | Bogotá, Colombia · (hora) (GMT−5) | Igual |
| V4 | Título de proyectos | Work | Proyectos |
| V5 | Línea de cada tarjeta | Tipo de trabajo · año (por ejemplo "Brand, web and campaigns · 2023–2024") | Igual, traducido |
| V6 | Tarjeta de Colombia 4.0 | Case study coming soon | Caso de estudio en preparación |
| V7 | Enlace al deck | SEE THE FULL DECK | VER LA PRESENTACIÓN COMPLETA |
| V8 | Título del bloque de IA | AI in my workflow | La IA en mi flujo de trabajo |
| V9 | Rótulo de la trayectoria | What I did | Qué hice |
| V10 | Línea del contacto | Based in Bogotá (GMT−5) · English and Spanish · Open to full-time roles and freelance projects | En Bogotá (GMT−5) · Español e inglés · Disponible para empleo de tiempo completo y proyectos independientes |
| V11 | Título de la página | Nicolás Mogollón Barbosa · Visual and AI Designer | Nicolás Mogollón Barbosa · Diseñador visual y de IA |
| V12 | Vende Digital, sección nueva "Reflection" al final del caso | I’m grateful to have helped launch a program that gives small and mid-sized businesses the tools to thrive in a growing, competitive economy. · **What I contributed:** I gave the 2022 edition its visual voice: the narrative theme “Facts that Connect,” a logo that builds on the 2021 version, and a campaign system that carried the program across the country, from billboards to social media and events. · **What I take away:** Putting my creativity at the service of the community made me feel part of a bigger purpose. It also showed me that design can make communication clearer, and clear communication is what ultimately helps people build new capabilities. | Agradezco haber ayudado a lanzar un programa que les da a las pequeñas y medianas empresas herramientas para prosperar en una economía creciente y competitiva. · **Lo que aporté:** Le di a la edición 2022 su voz visual: el eje narrativo “Hechos que conectan”, un logo que parte de la versión 2021 y un sistema de campaña que llevó el programa a todo el país, de las vallas a las redes sociales y los eventos. · **Lo que me llevo:** Poner mi creatividad al servicio de la comunidad me hizo sentir parte de un propósito más grande. También me mostró que el diseño puede hacer más clara la comunicación, y una comunicación clara es lo que, al final, ayuda a las personas a desarrollar nuevas capacidades. |

Tres datos que debes confirmar:
- **V1 y V2, "nueve años":** los conté desde junio de 2017, tu primer cargo en la trayectoria.
- **V2, "5 organizaciones":** son las cinco de tu trayectoria (ReloQuest, Invest in Bogotá, Ondas y Ecos, Areandina y MinTIC).
- **V10, disponibilidad:** puse empleo y proyectos independientes porque al inicio dijiste que el sitio era para reclutadores y clientes por igual.

## Lo que recomendé y no está, y por qué

| Recomendación | Por qué no está |
|---|---|
| Cifras de resultados (alcance, campañas, tiempo ahorrado) | No las tengo y no las invento. Las tres del hero son hechos que salen de tu trayectoria. |
| Ejemplo real de IA (encargo → resultado de la IA → pieza final) | Necesito el material. |
| "Sobre mí" y testimonios | Necesito tus frases y las citas. |
| El sol como ventana al trabajo | Compite con el sol suave que pediste; lo dejé como alternativa. |
| Redibujar las ilustraciones de servicios y atenuar animaciones | Son decisiones tuyas. |
| Analítica | Requiere abrir una cuenta (Plausible o Umami). |

## Base técnica (17 de noviembre de 2026)

Nada de esto cambia cómo se ve el sitio: las capturas de las 8 páginas, en escritorio y celular, son idénticas píxel a píxel antes y después.

| Qué | Antes | Ahora |
|---|---|---|
| Pintado del texto principal del inicio (LCP, en local) | 1880 ms | 344 ms |
| Saltos de diseño al cargar (CLS) | 0 | 0 |
| CSS | 84 KB, con estilos de prototipos descartados | 76 KB, sin reglas que ninguna página use |

- **Pintado más rápido:** el texto de apoyo del hero esperaba detrás de una animación de aparición; ya no. Cada página precarga el peso de fuente que pinta primero (700 en el inicio, 600 en los casos).
- **Navegación instantánea:** al posar el cursor o tocar un enlace interno, Chrome y Edge preparan la página siguiente. Los demás navegadores lo ignoran sin efecto.
- **Buscadores:** `sitemap.xml` con las 12 páginas y sus dos idiomas, `robots.txt`, y datos estructurados en cada caso (la obra, su autor y su lugar en el sitio).
- **Servidor (Netlify):** archivo `_headers` con caché de un año para `assets/` y cabeceras de seguridad. La política de contenido (CSP) va en modo "solo informar" hasta verificarla en el sitio publicado, porque no se puede probar antes.
- **Robustez:** estilos para modo de alto contraste y para imprimir; ícono para la pantalla de inicio del celular.
- **Pruebas dentro del repositorio** (`redesign/tools/qa/`): antes vivían en una carpeta temporal que se puede borrar.
  - `qa.js`: accesibilidad, anchos de 320 a 2560 px, sin JavaScript y movimiento reducido.
  - `measure.js`: peso, peticiones, LCP y CLS por página.
  - `snap.js` y `diff.py`: capturas de referencia y comparación píxel a píxel, para refactorizar sin miedo.
  - `prune_css.py` (en `redesign/tools/`): quita el CSS que ninguna página usa.

Regla nueva: una imagen o fuente que cambie debe cambiar de nombre, porque el navegador la guarda un año.

Fuentes: [umbrales de Core Web Vitals 2026](https://corewebvitals.io/core-web-vitals) (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1), [Chrome: prerender con reglas de especulación](https://developer.chrome.com/docs/web-platform/prerender-pages), [caché en Netlify](https://netli.fyi/blog/netlify-headers-and-caching). Una fuente no oficial dice que Netlify puede duplicar `Cache-Control`; hay que comprobarlo al publicar.

## Fuentes de esta ronda

- Imagen para compartir: [guía 2026 de tamaños](https://dev.to/grabbit/open-graph-image-sizes-and-dimensions-the-complete-2026-guide-1k16) y [env.dev](https://env.dev/guides/opengraph-image-sizes). 1200 × 630 px sirve en todas las plataformas. Las fuentes no coinciden en el límite de WhatsApp (300 o 600 KB); la imagen pesa 65 KB.
- Trayectoria plegable: [MDN](https://developer.mozilla.org/docs/Web/HTML/Element/summary), [Scott O’Hara](https://www.scottohara.me/blog/2022/09/12/details-summary.html) y la [guía de accesibilidad del gobierno de Nueva Zelanda](https://govtnz.github.io/web-a11y-guidance/wct/disclosures-and-accordions). Un título dentro del botón que pliega pierde su papel de título en algunos lectores de pantalla; por eso el cargo queda fuera y solo se pliegan las viñetas.
- Sol ligado al scroll: [web.dev, octubre de 2026](https://web.dev/blog/web-platform-10-2026) y [Chrome for Developers](https://developer.chrome.com/docs/css-ui/scroll-driven-animations). Firefox 159 lo activó en octubre de 2026; en versiones anteriores el sol simplemente no aparece.
