# Opción A v2 · "Horizonte"

Prototipo, no publicado. Rama `redesign`, carpeta `redesign/a-v2/` (inglés) y `redesign/a-v2/es/` (español).

## ⏳ Pendiente de tu decisión (ronda actual)

### 1. Encabezado: elige una propuesta
Abre cualquier página con el parámetro y baja un poco. Luego sube un poco para que aparezca la píldora.

| Propuesta | Qué es | Ver |
|---|---|---|
| Actual | Píldora flotante sin marco: el contenido pasa por detrás y alrededor | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/index.html) |
| A, banda | Como tu versión anterior: la píldora va sobre una banda del color del fondo; el contenido desaparece bajo la banda | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/index.html?header=a) |
| B, banda difuminada | La banda se desvanece hacia abajo y desenfoca lo que pasa por debajo | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/index.html?header=b) |
| C, píldora enmarcada | Sin banda; la píldora tiene un contorno fino y una sombra más marcada | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/index.html?header=c) |

### 2. Parallax de Radio a Domicilio: elige una propuesta
Investigué los patrones más usados en portafolios y sitios premiados. Hay cuatro familias:
- **Imagen que se mueve más lento:** el parallax clásico.
- **Imagen fija con el contenido pasando por encima:** el "telón", con `sticky`.
- **Imagen que se expande al hacer scroll:** con `clip-path`, muy presente en Awwwards.
- **Portada a pantalla completa** que se asienta.

Todas respetan "reducir movimiento".

| Propuesta | Qué es | Ver |
|---|---|---|
| A, marco (actual) | La imagen, dentro de un marco redondeado, se mueve más lento que la página | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/radio-a-domicilio/index.html) |
| B, pantalla completa | La imagen ocupa el 100 % de la pantalla, de borde a borde, y se mueve más lento | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/radio-a-domicilio/index.html?parallax=b) |
| C, telón | La imagen queda fija a pantalla completa y los capítulos suben por encima, como un telón | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/radio-a-domicilio/index.html?parallax=c) |
| D, expansión | La imagen empieza enmarcada y se abre hasta el ancho completo cuando empiezas a bajar | [ver](https://raw.githack.com/NicolasMB83/portfolio/redesign/redesign/a-v2/radio-a-domicilio/index.html?parallax=d) |

Mi recomendación es **D** o **A**:
- **D** cuenta la idea de "abrirse al horizonte".
- **A** es la más sobria.
- **B** y **C** dan mucho protagonismo a una sola imagen; funcionan si esa imagen es muy fuerte.

### 3. Nombre de la sección de piezas ("The work")
Las fuentes consultadas no fijan un nombre estándar, pero coinciden en que los títulos descriptivos funcionan mejor que los genéricos para quien escanea un caso en 10–30 segundos.

| Opción | Inglés | Español |
|---|---|---|
| A (recomendada, descriptiva) | Brand, web and campaigns · Campaigns, presentations and web | Marca, web y campañas · Campañas, presentaciones y web |
| B (genérica) | Selected work | Piezas seleccionadas |
| C (la anterior) | The work | Las piezas |

Hoy se ve la opción A: en Radio a Domicilio "Brand, web and campaigns / Marca, web y campañas"; en Invest in Bogotá "Campaigns, presentations and web / Campañas, presentaciones y web".

### 4. Revisión ortográfica y de estilo (ronda 1)
No cambié ningún texto visible. Cada propuesta está marcada en el HTML como `PROPUESTA DE TEXTO R<número>`. Respóndeme por número, por ejemplo: "sí R1–R12, no R24".

| # | Dónde | Inglés actual | Inglés propuesto | Español actual | Español propuesto | Por qué |
|---|---|---|---|---|---|---|
| R1 | Inicio · intro | I'm Nicolás, a multidisciplinary designer with experience in Product and Digital Design, creating campaigns on social media. | **I’m Nicolás, a multidisciplinary designer with experience in product design, digital design and social media campaigns.** | Soy Nicolás, diseñador multidisciplinario con experiencia en diseño de producto y diseño digital, creando campañas para redes sociales. | **Soy Nicolás, diseñador multidisciplinario con experiencia en diseño de producto, diseño digital y campañas para redes sociales.** | EN: "creating campaigns on social media" queda colgando; las disciplinas van en minúscula; apóstrofo tipográfico. ES: mismo ajuste (el gerundio "creando" queda suelto). |
| R2 | Contacto · título | Let's make magic! | **Let’s make magic!** | — | **—** | Apóstrofo tipográfico (’), igual que en "Let’s talk". |
| R3 | Servicios · UI Design | I enhance the user experience with intuitive interface designs for web and mobile applications. | **Enhancing the user experience with intuitive interfaces for web and mobile apps.** | Mejoro la experiencia de usuario con diseños de interfaz intuitivos para aplicaciones web y móviles. | **Mejora de la experiencia de usuario con interfaces intuitivas para aplicaciones web y móviles.** | Los otros tres servicios están escritos sin sujeto ("Developing…", "Creating…"); este es el único en primera persona. |
| R4 | Trayectoria · Invest in Bogotá, viñeta 1 | Design of graphic assets for national and international investment promotion events. | **Designed graphic assets for national and international investment promotion events.** | Diseño de piezas gráficas para eventos nacionales e internacionales de promoción de inversión. | **Diseñé piezas gráficas para eventos nacionales e internacionales de promoción de inversión.** | Las viñetas de un mismo cargo deben ser paralelas: verbo en pasado, como "Implemented…". |
| R5 | Trayectoria · Invest in Bogotá, viñeta 2 | Creation of visual assets for social media campaigns, aimed at informing, promoting and attracting investors to Bogotá, the capital of Colombia. | **Created visual assets for social media campaigns that inform, promote and attract investment to Bogotá, the capital of Colombia.** | Creación de piezas visuales para campañas en redes sociales, orientadas a informar, promover y atraer inversionistas a Bogotá, la capital de Colombia. | **Creé piezas visuales para campañas en redes sociales que informan, promueven y atraen inversión a Bogotá, la capital de Colombia.** | Verbo en pasado (paralelismo) y frase más directa. |
| R6 | Trayectoria · Invest in Bogotá, viñeta 3 | Implemented AI to support design workflow across the Design department. | **Implemented AI tools to support the design workflow across the Design department.** | Implementé IA para apoyar el flujo de trabajo de diseño en todo el departamento de Diseño. | **Implementé herramientas de IA para apoyar el flujo de trabajo en todo el departamento de Diseño.** | EN: falta el artículo ("the design workflow"). ES: se evita repetir "diseño". |
| R7 | Trayectoria · Ondas y Ecos, viñeta 3 | Directed the narrative of the brand Radio a Domicilio. Closeness and familiarity. | **Directed the Radio a Domicilio brand narrative, built on closeness and familiarity.** | Dirigí la narrativa de la marca Radio a Domicilio. Cercanía y familiaridad. | **Dirigí la narrativa de la marca Radio a Domicilio, basada en la cercanía y la familiaridad.** | "Closeness and familiarity." es una frase sin verbo; se integra a la oración. |
| R8 | Trayectoria · Infinited, viñeta 1 | Led cross-functional collaboration between the marketing, design and development teams to deliver campaigns aligned with the university goals. | **Led cross-functional collaboration between the marketing, design and development teams to deliver campaigns aligned with the university’s goals.** | — | **—** | Falta el posesivo: "the university’s goals". |
| R9 | Trayectoria · Infinited, viñeta 2 | Created interactive content aligned with brand identity, leading to further improvement and organic evolution of the brand. | **Created interactive content aligned with the brand identity, helping the brand improve and evolve organically.** | Creé contenido interactivo alineado con la identidad de marca, lo que llevó a una mayor mejora y a la evolución orgánica de la marca. | **Creé contenido interactivo alineado con la identidad de marca, que ayudó a la marca a mejorar y evolucionar de forma orgánica.** | Más corta y directa; "further improvement and organic evolution" es redundante. |
| R10 | Trayectoria · Infinited, viñeta 3 | UI prototyping and deployment optimized for the sales funnel. | **Prototyped and deployed interfaces optimized for the sales funnel.** | Prototipado y despliegue de UI optimizados para el embudo de ventas. | **Prototipé y desplegué interfaces optimizadas para el embudo de ventas.** | Paralelismo con las otras viñetas (verbo en pasado). |
| R11 | Trayectoria · MinTIC, viñeta 1 | presentations (PPT/keynote) | **presentations (PowerPoint/Keynote)** | presentaciones (PPT/keynote) | **presentaciones (PowerPoint/Keynote)** | Nombres de producto con su grafía oficial. |
| R12 | Trayectoria · ReloQuest, viñeta 4 | Create print pieces such as backdrops, and mock-ups that present each design in context. | **Create print pieces such as backdrops, plus mockups that show each design in context.** | Creo piezas impresas como backdrops, y mock-ups que presentan cada diseño en contexto. | **Creo piezas impresas como *backdrops*, además de *mockups* que muestran cada diseño en contexto.** | La coma antes de "and" hace pensar que los mock-ups son piezas impresas. ES: los extranjerismos van en cursiva (RAE). |
| R13 | Invest in Bogotá · párrafo de la agencia (punto 9) | IBB aim is to facilitate relevant international investments and attract world-class meetings and events that contribute to the socioeconomic development, competitiveness, and quality of life of Bogotá-Region. I have to develop impactful collateral to create a strong brand presence as well as keep a coherent narrative of the brand. | **IBB’s aim is to facilitate relevant international investment and attract world-class meetings and events that contribute to the socioeconomic development, competitiveness and quality of life of Bogotá–Region. My role is to develop impactful collateral that builds a strong brand presence and keeps the brand’s narrative coherent.** | El objetivo de IBB es facilitar inversiones internacionales relevantes y atraer reuniones y eventos de talla mundial que contribuyan al desarrollo socioeconómico, la competitividad y la calidad de vida de Bogotá-Región. Debo desarrollar piezas de impacto para crear una presencia de marca sólida, así como mantener una narrativa coherente de la marca. | **El objetivo de IBB es facilitar inversiones internacionales relevantes y atraer reuniones y eventos de talla mundial que contribuyan al desarrollo socioeconómico, la competitividad y la calidad de vida de Bogotá–Región. Mi labor es desarrollar piezas de impacto que construyan una presencia de marca sólida y mantengan coherente su narrativa.** | Falta el posesivo ("IBB’s aim"); "I have to" suena a obligación, no a rol; "Bogotá-Region" se escribe distinto en la portada ("Bogotá – Region"): se unifica con raya corta. |
| R14 | Invest in Bogotá · título de sección | Objectives - Challenges | **Objectives and challenges** | Objetivos - Retos | **Objetivos y retos** | Un guion no separa títulos; se usa "y". |
| R15 | Invest in Bogotá · reto 1 | IBB has a new rebranding, making this the perfect environment to develop the brand, through creative implementations in printed, web, and social media assets the challenge is to preserve its brand while developing new ways to communicate | **IBB had just been rebranded, which made it the perfect moment to develop the brand. Through creative work for print, web and social media, the challenge is to preserve the brand while finding new ways to communicate.** | IBB tiene un nuevo rebranding, lo que hace de este el entorno perfecto para desarrollar la marca; a través de implementaciones creativas en piezas impresas, web y de redes sociales, el reto es preservar su marca mientras se desarrollan nuevas formas de comunicar | **IBB acababa de renovar su marca, lo que hizo de este el momento perfecto para desarrollarla. A través de piezas creativas impresas, web y para redes sociales, el reto es preservar la marca mientras se encuentran nuevas formas de comunicar.** | Oración demasiado larga (dos ideas unidas por comas) y sin punto final. "A new rebranding" es redundante. |
| R16 | Invest in Bogotá · reto 2 | The biggest challenge is to keep the brand relevant, by researching every day about current trends and styles I'm able to keep the brand cohesion while creating content for web, digital and printed media. | **The biggest challenge is keeping the brand relevant. By researching current trends and styles every day, I keep the brand cohesive while creating content for web, digital and print media.** | El mayor reto es mantener la marca vigente; investigando cada día sobre tendencias y estilos actuales, logro mantener la cohesión de la marca mientras creo contenido para medios web, digitales e impresos. | **El mayor reto es mantener la marca vigente. Investigando cada día tendencias y estilos actuales, mantengo la cohesión de la marca mientras creo contenido para medios web, digitales e impresos.** | Dos oraciones en una; "researching about" sobra la preposición. |
| R17 | Invest in Bogotá · reto 2, título | Keep sharp graphics | **Keep the graphics sharp** | — | **—** | Orden natural en inglés. |
| R18 | Invest in Bogotá · reto 3 | Integrate AI tools into the mix in order to reduce times in production and/or develop products that demand speed, complexity and quality | **Integrate AI tools into the process to reduce production times and to develop products that demand speed, complexity and quality.** | Integrar herramientas de IA al proceso para reducir los tiempos de producción y/o desarrollar productos que exigen velocidad, complejidad y calidad | **Integrar herramientas de IA al proceso para reducir los tiempos de producción y desarrollar productos que exigen velocidad, complejidad y calidad.** | "and/or" no es recomendable en textos de presentación; falta el punto final. |
| R19 | Casos · "Social Media" | Social Media | **Social media** | — | **—** | Mayúscula solo inicial, como el resto de rótulos ("Slides"). |
| R20 | Radio a Domicilio · descripción | Under the slogan “Radio at Home,” we seek to create an authentic and welcoming experience | **Under the slogan “Radio at Home,” we set out to create an authentic, welcoming experience.** | Bajo el lema “Radio a Domicilio”, buscamos crear una experiencia auténtica y acogedora | **Bajo el lema “Radio a Domicilio”, buscamos crear una experiencia auténtica y acogedora.** | Falta el punto final. |
| R21 | Radio a Domicilio · objetivo 3 | Create striking graphics that capture attention and retain users on social media. | **Creating striking graphics that capture attention and keep users engaged on social media.** | — | **—** | Paralelismo con los otros dos objetivos ("Achieving…", "Designing…"). |
| R22 | Radio a Domicilio · proceso (tiempos verbales) | Thoroughly research audience preferences to create an aesthetic that reinvents the legacy of Radio a Domicilio and attracts new listeners. | **Researched audience preferences in depth to create an aesthetic that reinvents the legacy of Radio a Domicilio and attracts new listeners.** | Investigar a fondo las preferencias de la audiencia para crear una estética que reinvente el legado de Radio a Domicilio y atraiga nuevos oyentes. | **Investigué a fondo las preferencias de la audiencia para crear una estética que reinventara el legado de Radio a Domicilio y atrajera nuevos oyentes.** | El proceso mezcla imperativo, pasado y sustantivos; todo en pasado. |
| R23 | Radio a Domicilio · proceso, Diseño UI/UX | I designed a clean, intuitive interface with streamlined navigation and engaging visuals to motivate users | **Designed a clean, intuitive interface with streamlined navigation and engaging visuals.** | Diseñé una interfaz limpia e intuitiva, con una navegación simplificada y visuales atractivos para motivar a los usuarios | **Diseñé una interfaz limpia e intuitiva, con navegación simplificada y visuales atractivos.** | Falta el punto final; "to motivate users" no agrega información. |
| R24 | Radio a Domicilio · proceso, Análisis de audiencia | Examine audience preferences to define the aesthetic of Radio a Domicilio and attract new listeners. | **Analyzed how the audience responded to each visual direction to settle the final aesthetic.** | Examinar las preferencias de la audiencia para definir la estética de Radio a Domicilio y atraer nuevos oyentes. | **Analicé cómo respondía la audiencia a cada dirección visual para definir la estética final.** | Repite casi palabra por palabra el "Market and Style Study". Propongo diferenciarlo; si no corresponde a lo que hiciste, se puede quitar. |
| R25 | Radio a Domicilio · proceso, Pruebas con usuarios | Initial testing of a controlled group of users to obtain feedback about the web interface, its use, and future implementations before launch | **Tested the web interface with a controlled group of users before launch to gather feedback on its use and on future features.** | Pruebas iniciales con un grupo controlado de usuarios para obtener retroalimentación sobre la interfaz web, su uso y futuras implementaciones antes del lanzamiento | **Probé la interfaz web con un grupo controlado de usuarios antes del lanzamiento para recoger comentarios sobre su uso y sobre funciones futuras.** | Tiempo verbal y punto final. |
| R26 | Radio a Domicilio · proceso, Optimización web | Implemented optimizations in the user interface to enhance the navigation experience of the website on computers and mobile devices. | **Optimized the interface to improve navigation on desktop and mobile.** | Implementé optimizaciones en la interfaz de usuario para mejorar la experiencia de navegación del sitio web en computadores y dispositivos móviles. | **Optimicé la interfaz para mejorar la navegación en computador y celular.** | Más directa. |
| R27 | Radio a Domicilio · resultados | received positive feedback and an exceptional reception in the company. | **received positive feedback and an exceptional reception within the company.** | — | **—** | "within the company" es la preposición natural. |
| R28 | Radio a Domicilio · próximos pasos | Continuous Improvements | **Continuous improvements** | — | **—** | Mayúscula solo inicial, como los demás títulos. |
| R29 | 404 | The page you are looking for is not found or has been moved. Please return to the main page. | **The page you’re looking for doesn’t exist or has moved. Head back to the home page.** | La página que buscas no se encuentra o ha sido movida. Por favor, regresa a la página principal. | **La página que buscas no existe o cambió de lugar. Vuelve al inicio.** | "is not found" no es natural en inglés; más corto y en el tono del sitio. |

### 5. Íconos: qué dicen las normas y qué recomiendo
Lo que dicen las normas:
- **Un ícono solo no basta.** Las guías de usabilidad, el sistema de diseño de la Oficina de Estadísticas del Reino Unido (ONS) y los estudios que citan a NN/g coinciden en que la mayoría de los íconos solo se entienden bien con una etiqueta de texto.
- **Excepciones:** los íconos universales (cerrar, menú, reproducir, descargar) y los logos de redes conocidas.
- **Pestaña nueva:** un enlace que abre una pestaña nueva debe anunciarlo a lectores de pantalla (W3C, técnica G201). Ya lo apliqué en LinkedIn, Behance y el CV: "(opens in a new tab)" / "(se abre en una pestaña nueva)", no visible.

Lo que hacen los portafolios destacados: usan pocos íconos. Las redes suelen ir como texto ("LinkedIn ↗") y la flecha ↗ aparece solo para indicar que el enlace sale del sitio.

Mi recomendación (no aplicada, dime si sí):

| Ícono | Recomendación | Por qué |
|---|---|---|
| ↗ del "Let’s talk" | Mantener | Es parte de la animación aprobada |
| Copiar / ✓ copiado | Mantener | Comunica un cambio de estado |
| Cerrar (×) y menú (≡) | Mantener | Universales |
| Descarga del CV | Mantener | Indica que baja un archivo |
| Logo de Behance junto a la palabra "Behance" | Quitar | Repite lo mismo dos veces |
| Footer: círculos solo con ícono (LinkedIn, Behance, correo) | Cambiar por texto: "LinkedIn ↗ · Behance ↗ · Email" | Íconos sin etiqueta, la forma menos clara según las normas |

---

## ✅ Aplicado en esta ronda
- **Línea del horizonte bajo el sol:** es invisible lejos del sol y gana opacidad a medida que se acerca. Pasado el sol se desvanece de nuevo. Aplica en el hero, el 404, el panel de contacto y la portada de Invest in Bogotá.
- **Cada proyecto con su propia estructura, misma familia:**
  - Portada común: título sobre el horizonte, **descripción breve** y **Año / Empresa / Rol**.
  - **Radio a Domicilio:** capítulos numerados (Objetivos, Proceso, piezas, Resultados). Los números son más pequeños, en proporción a secciones cortas. La descripción pasó a la portada.
  - **Invest in Bogotá:** sin números. Párrafo de la agencia como declaración, retos y piezas, marcados con el punto rojo de su marca, que sube desde la línea.
- **Píldora:** al pasar el cursor, las secciones y el idioma se ponen naranja. Usé un naranja un poco más profundo (`#bd4600`) para que el texto mantenga contraste 5:1; el naranja del sol daría 2,6:1.
- **Teselación:**
  - Se corrigió la falla: en cada unión entre baldosas el trazo se cortaba y dejaba un escalón. Ahora cada baldosa dibuja también los arcos vecinos como una sola onda continua.
  - Solo aparece mientras una imagen carga o si falla. Se quitó de los bordes de las secciones, y cuando la imagen carga desaparece (las imágenes con fondo transparente ya no quedan enmarcadas).
- **Animación al hacer scroll** (la imagen que se aleja): ya no está en todas. Por ahora solo en la captura del sitio de Invest in Bogotá ("5 claves legales para situar tus negocios en Bogotá").
- **Accesibilidad:** los enlaces que abren pestaña nueva lo anuncian a lectores de pantalla.

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
