# Auditoría de UI y de perfil (10 de noviembre de 2026)

Revisión del inicio y de los cinco casos en escritorio (1440 px) y celular (390 px). No se cambió nada: son hallazgos y propuestas, ordenados por impacto.

## Veredicto

El sitio ya tiene oficio: es rápido, accesible, bilingüe y tiene un lenguaje propio (el horizonte, el sol, las letras que suben). Lo que todavía no hace es **vender el perfil**. Quien llega no sabe en diez segundos qué haces, para quién ni qué resultado lograste, y tu diferencial (diseñador visual **y de IA**) aparece en el cargo pero no se demuestra en ninguna parte.

El concepto "Horizonte" está bien ejecutado en los detalles, pero la idea grande que lo haría inolvidable (el sitio como un día) quedó planeada y sin construir.

## Lo que ya funciona (no tocar)

- Píldora que se esconde, halación del logo, barrido del horizonte, telón de Radio a Domicilio y logo que sube en el footer.
- Cada caso con su estructura y su forma, en la misma familia.
- Tipografía y fondo iguales a la versión publicada.
- Correo visible con botón de copiar, CV a un clic, inglés y español.
- Pruebas automáticas limpias en todas las páginas.

## Hallazgos

### A. Vender el perfil (lo más importante)

| # | Qué pasa hoy | Evidencia | Qué haría |
|---|---|---|---|
| A1 | El titular promete resultados y la página no muestra ninguno. | En el inicio y en cuatro de los cinco casos no hay una sola cifra. La única del sitio es "30 años", de Pro Surge. | Una franja de 3 o 4 cifras reales bajo el hero o junto a los clientes (años de experiencia, campañas, alcance, tiempo ahorrado con IA). Una cifra por caso en la portada, junto a Año / Empresa / Rol. |
| A2 | El primer pantallazo no dice quién eres. | El titular ("I LOVE DESIGN…") lo podría firmar cualquier diseñador. Tu cargo, tu ciudad y tus clientes no están ahí; el texto de apoyo es genérico. | El titular se queda (decisión tuya). El texto de apoyo carga lo específico: cargo, años, tipo de clientes, ciudad y disponibilidad. Propuesta de texto más abajo. |
| A3 | "Visual and AI Designer" sin prueba de IA. | "AI" aparece 4 veces en el inicio, siempre como cargo o viñeta. Ningún caso muestra cómo la usas. | Un bloque "Cómo uso la IA" con un ejemplo real: encargo → resultado crudo de la IA → pieza final, y qué decidiste tú. Es lo que hoy piden ver quienes contratan. |
| A4 | "ABOUT" lleva a servicios; no hay un "sobre mí". | No hay historia, foto ni forma de trabajar. | Un bloque corto: tres frases con tu recorrido (gobierno, universidad, marca privada), cómo trabajas y qué buscas. La foto es opcional. |
| A5 | No hay voz de terceros. | Hay cinco logos, ninguna cita. | Dos o tres testimonios cortos (jefe, cliente, colega) con nombre y cargo. |
| A6 | Las tarjetas de proyecto dicen el cargo, no el proyecto. | "Invest in Bogotá · Visual and AI Designer" no dice qué hiciste. | Una línea por tarjeta: tipo de trabajo y año ("Campañas y presentaciones · 2025"), y el cargo pasa al caso. |
| A7 | El contacto no dice qué buscas. | "Let’s make magic!" y "Working together to achieve greatness" no informan. | Añadir disponibilidad (empleo, freelance o ambos), ciudad y zona horaria, idiomas y tiempo de respuesta. |
| A8 | "VIEW PORTFOLIO" confunde. | El sitio ya es el portafolio; el enlace lleva al deck de Figma. | Renombrarlo, por ejemplo "See the full deck (Figma)". |

### B. Ser único (el concepto)

| # | Idea | Por qué destaca | Cómo |
|---|---|---|---|
| B1 | **El sitio como un día en Bogotá.** | Es la idea que estaba en el plan (Fase 1) y no se construyó. Convierte un adorno en narrativa: nadie más tiene un portafolio que amanece y anochece. | El sol recorre el borde de la pantalla con el scroll: sale en el hero, está alto en los proyectos, baja en la trayectoria y se oculta en el contacto. Sin secuestrar el scroll y apagado con "reducir movimiento". |
| B2 | **La hora real de Bogotá.** | Une concepto y utilidad: a un reclutador de otro país le dice tu zona horaria y si estás en línea. | Una línea pequeña en el hero o el contacto: "Bogotá · 3:42 p. m." y el sol del hero a la altura que corresponde a esa hora. |
| B3 | **El sol como ventana al trabajo.** | Hoy la mitad derecha del hero es solo un círculo naranja. El primer segundo no muestra trabajo. | Dentro del sol del hero, una secuencia lenta de tus piezas (como el gato del 404). Con "reducir movimiento", una imagen fija. |
| B4 | **Cada proyecto con su forma también en el inicio.** | Las formas de las portadas (ondas, punto, trazos, franjas) solo viven dentro de cada caso. | Al pasar el cursor por una tarjeta, la forma del cliente sube desde el borde, en su color. El inicio anticipa el caso. |
| B5 | **Las ilustraciones de servicios rompen tu propia regla.** | Son lo único orgánico y dibujado a mano que queda. Tú mismo descartaste lo orgánico porque rompe la marca. | Redibujarlas con la geometría del logo (arco, punto, línea), o asumirlas como la excepción cálida y decirlo. |

### C. UI moderna (pulido)

| # | Qué pasa hoy | Qué haría |
|---|---|---|
| C1 | **Jerarquía plana:** "I LOVE DESIGN", "WORK" y "Career path" miden lo mismo (70 px). El titular no manda. | Dejar el hero en 70 px (decisión tuya) y bajar los títulos de sección a unos 48–56 px. |
| C2 | **Demasiados movimientos pequeños:** el sitio tiene 22 animaciones distintas. Tu regla es que cada una tenga una razón. | Un momento protagonista por página (amanecer del hero, telón, logo del footer) y atenuar el resto. |
| C3 | **Trayectoria larga:** 5 cargos con viñetas ocupan unos 1900 px. | Mostrar cargo, empresa y fechas; las viñetas se abren al tocar. O dejar los tres últimos y enlazar el CV. |
| C4 | **Títulos de sección inconsistentes:** "WORK" en mayúsculas, "Career path" en minúsculas. | Un solo criterio. |
| C5 | **Celular, trayectoria:** dos líneas seguidas con un vacío de unos 65 px entre el título y el primer cargo. | Quitar la segunda línea. |
| C6 | **Servicios con texto de catálogo** ("Developing design concepts that encompass…"). | Una frase concreta por servicio: qué entregas y un ejemplo. |

### D. Técnico (para que el enlace se vea bien fuera del sitio)

| # | Qué falta | Por qué importa |
|---|---|---|
| D1 | **Imagen para compartir.** | Hoy, al pegar el enlace en LinkedIn o WhatsApp no sale ninguna imagen. Es la primera impresión antes de entrar. |
| D2 | **Título de la página:** "Nicolas MB - Designer". | En Google y en la pestaña conviene tu nombre completo y tu cargo: "Nicolás Mogollón Barbosa · Visual and AI Designer". |
| D3 | **Datos estructurados de persona.** | Ayuda a que Google asocie tu nombre, cargo y redes. |
| D4 | **Analítica respetuosa** (Plausible o Umami). | Saber qué proyectos abren y dónde se van. |
| D5 | **Las 3 portadas animadas** siguen en Framer. | Si Framer se cae, se ve una imagen fija. |

## Propuestas de texto (no aplicadas)

- **Texto de apoyo del hero (A2):**
  - EN: "I’m Nicolás, a visual and AI designer based in Bogotá. For nine years I’ve turned public programs, universities and brands into identities, campaigns and websites, for MinTIC, Invest in Bogotá and ReloQuest."
  - ES: "Soy Nicolás, diseñador visual y de IA en Bogotá. Desde hace nueve años convierto programas públicos, universidades y marcas en identidades, campañas y sitios web, para MinTIC, Invest in Bogotá y ReloQuest."
  - Los nueve años salen de tu trayectoria (junio de 2017 a hoy). Confírmalo.
- **Título de la página (D2):** "Nicolás Mogollón Barbosa · Visual and AI Designer".

## Qué necesito de ti para A1, A3, A4 y A5

1. Tres o cuatro cifras reales (aunque sean aproximadas y lo digamos).
2. Un ejemplo de trabajo con IA: el encargo, lo que generó la herramienta y la pieza final.
3. Tres frases sobre ti, o una nota de voz que yo transcribo.
4. Dos o tres testimonios, o los nombres de quienes podrían darlos.

## Orden sugerido

1. **Sin esperar contenido:** D1, D2, D3, A6, A8, C1, C3, C4, C5 y B4.
2. **La idea grande:** B1 con B2 (el día en Bogotá). B3 es alternativa o complemento.
3. **Con tu contenido:** A1, A2, A3, A4, A5, A7 y C6.
4. **Decisión tuya:** B5 y C2.

## Fuentes

- Qué miran quienes contratan: [ADPList](https://adplist.org/blog/what-is-a-hiring-manager-looking-for-in-a-design-portfolio), [Dribbble](https://content-hub.dribbble.com/?p=176), [The Fountain Institute, 2026](https://www.thefountaininstitute.com/blog/senior-product-designers-hired), [UX Collective](https://uxdesign.cc/what-hiring-managers-look-for-in-a-product-design-portfolio-7b1837360bf9) y [ResumeGeni](https://resumegeni.com/blog/product-designer-portfolio). Coinciden en que el primer pantallazo decide (entre 6 y 20 segundos según la fuente) y en que pesan más los resultados que el proceso.
- Cómo mostrar el trabajo con IA: [Lovart, guía 2026](https://www.lovart.ai/fr/blog/ai-design-portfolio-interview-2026), [Be Your Own Design Team](https://beyourowndesignteam.beehiiv.com/p/2025-portfolio-vs-2026-portfolio-what-changed), [Belmont University](https://belmont.edu/stories/articles/2025/ai-in-design.html) y [AI Indigo](https://aiindigo.com/blog/augmented-creative-graphic-designer-ai-guide-2026).
- Portafolios destacados: [David Martín Suárez (Awwwards)](https://www.awwwards.com/sites/david-martin-suarez), [Sam Stoof (Awwwards)](https://www.awwwards.com/sites/sam-stoof) y [Acodez, enero de 2026](https://acodez.in/?p=28205) sobre testimonios.
- Límite de estas fuentes: casi todas son blogs y guías, no estudios. El informe con más base (UXfolio, más de 100 líderes de diseño) no lo pude abrir. Las cifras de segundos son orientativas.
