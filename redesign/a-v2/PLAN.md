# Plan de acción: un portafolio con lenguaje propio

## Qué encontré (noviembre 2026)

1. **La reacción contra la uniformidad es explícita.** Las plantillas y los constructores no-code hicieron fácil un sitio "decente", y por eso muchos se ven casi idénticos. En 2026 los diseñadores responden con:
   - grillas rotas y asimetría;
   - dirección de arte por sección;
   - narrativa guiada por el scroll;
   - marcas hechas a mano y tipografía con movimiento.

   Fuentes: Envato, DesignRush, Figma, Line25.
2. **Los bento grids ya son la nueva plantilla.** Varias fuentes los consideran mainstream, así que no son una salida.
3. **Expresión sí, pero no en la mecánica.** Jakob Nielsen insiste en que innovar en lo básico suele costar más de lo que aporta.
   - El ejemplo clásico es el scrolljacking (secuestrar el scroll).
   - Un estudio citado de NN/g encontró que volver al inicio es seis veces más difícil con el logo centrado.
   - La forma de innovar sin riesgo: mezclar lo nuevo con lo familiar y probarlo con personas.
4. **Los referentes premiados parten de una sola metáfora propia y la llevan a todo:**
   - Bruno Simon: su portafolio se recorre manejando un carro.
   - Victor Furuya: el sitio es un instrumento.
   - Lando Norris (OFF+BRAND) y Messenger: Site of the Year 2025 en Awwwards.

   Ninguno parte de una plantilla, y todos tienen navegación entendible.

## La regla para este sitio

**Reglas para la mecánica. Lenguaje propio para todo lo demás.**

| No se toca (convención) | Lo nuestro (lenguaje propio) |
|---|---|
| Navegación arriba, logo arriba a la izquierda que lleva al inicio | La narrativa y el orden del recorrido |
| Scroll nativo (nunca secuestrarlo) | Composición y ritmo de cada sección |
| Botones y enlaces reconocibles | Tipografía, color, texturas (teselación, película) |
| Contraste AA, foco visible, "reducir movimiento" | Transiciones y microinteracciones derivadas del logo |
| Carga rápida, inglés/español bien hechos | Plantillas propias de caso de estudio |

Nuestra metáfora ya existe y es tuya: **el logotipo son letras que salen de una línea**. Horizonte, sol, día y noche, película.

## Fases

### Fase 1: Narrativa "Un día"
El recorrido del sitio se cuenta como un día de luz:

| Sección | Momento del día |
|---|---|
| Hero | Amanecer |
| Proyectos | Día |
| Trayectoria | Atardecer |
| Contacto | Noche, como la portada de tu deck: película negra, quemadura y tu logo con halación |

- El sol acompaña el scroll sin secuestrarlo: sale en el hero, baja por el borde de la pantalla y se oculta antes del contacto, donde aparece tu logo encendido.
- **Estado:** la película está aprobada y aplicada en el contacto (vectorial). Falta el recorrido del sol a lo largo de toda la página.

### Fase 2: Proyectos sin grilla de tarjetas
Dos alternativas para comparar, ambas derivadas de tu material:
- **A. Dirección de arte por proyecto:** cada proyecto en la home con su propio color, su forma (el círculo de IiB, por ejemplo) y su encuadre, en una composición asimétrica que respira distinto en cada uno.
- **B. Hoja de contactos de película:** los proyectos como fotogramas de una tira de película (continuidad con el deck). Al pasar el cursor, el fotograma se revela a color.
- **Estado:** ambas construidas para comparar: `projects-a/index.html` y `projects-b/index.html`. Falta que elijas.

### Fase 3: Plantilla propia de caso de estudio ("capítulos")
- **Portada tipo deck:** fondo índigo o película, título sobre el horizonte y la forma del cliente.
- **Capítulos separados por el horizonte:** Contexto, Reto, Decisiones, Piezas, Resultado.
- **Aplicarla a los 6 proyectos.**
- **Necesito de ti:** textos, imágenes y resultados (aunque sean cualitativos) de Vende Digital, Infinited, Colombia 4.0 y Pro Surge JA.
- **Estado:** ejemplo construido con Radio a Domicilio, usando el contenido de tu CMS: `radio-a-domicilio/index.html` (EN) y `es/radio-a-domicilio/index.html` (ES). Si lo apruebas, se aplica a Invest in Bogotá y a los demás.

### Fase 4: Firma interactiva
Hecho:
- El punto que se expande con cada clic.
- El sol que sale.
- Los gatos del 404.

Hecho en esta ronda:
- Hover del logo con halación.
- Transición entre páginas en la que la línea del horizonte barre la pantalla. Usa las transiciones de vista entre documentos, que funcionan en Chrome, Edge y Safari 18.2 o superior; en los demás navegadores la página carga normal.

Se mantiene el cursor normal, porque los cursores personalizados perjudican la accesibilidad.

### Fase 5: Robustez y lanzamiento
- **Imágenes y fuentes dentro del repositorio:** hecho. Solo quedan en Framer las 3 animaciones Lottie (ver PROPUESTAS, punto D).
- **Imagen para compartir en LinkedIn y WhatsApp** (Open Graph).
- **Dominio:** `nicolasmb.com` está activo en Netlify. Las direcciones canónicas ya apuntan ahí.
- **Analítica respetuosa:** Plausible o Umami.
- **Prueba de 5 segundos con 5 personas** (reclutadores y diseñadores): ¿qué recuerdan, qué entienden, dónde hacen clic?
- **Publicar en `main`** solo con tu aprobación, con el respaldo ya creado.

## Orden sugerido
1. Decides la propuesta película y la alternativa de la Fase 2.
2. Construyo la Fase 1 y la alternativa elegida.
3. Me envías el contenido de los casos y construyo la Fase 3.
4. Fases 4 y 5, y lanzamiento.

## Fuentes de esta ronda
- [Chrome for Developers: transiciones de vista entre documentos](https://developer.chrome.com/docs/web-platform/view-transitions/cross-document). Soporte según los resultados de búsqueda: Chrome/Edge 126+ y Safari 18.2+; Firefox aún en desarrollo. Las páginas de Chrome y MDN no se pudieron abrir desde este entorno (dominio bloqueado).
- [Guía 2026 de CSS View Transitions](https://devtoolbox.dedyn.io/blog/css-view-transitions-complete-guide)
- [Rendimiento de feTurbulence (Mozilla)](https://bugzilla.mozilla.org/show_bug.cgi?id=422371): el costo crece con `numOctaves`. Por eso se usan pocas octavas, una región de filtro acotada y ningún filtro animado.
- [GreenSock: feTurbulence en móviles](https://greensock.com/forums/topic/33075-gsap-and-feturbulence-mobile-performance/): animarlo en áreas grandes es lento en iOS. Por eso la quemadura es estática.
- [Grano SVG y rendimiento](https://loke-dev-lokedevs-projects.vercel.app/blog/svg-grain-textures-performance)
- Casos de estudio que leen los reclutadores: problema, rol y resultado primero; fáciles de escanear; mostrar el proceso. Fuentes: [UX Planet](https://uxplanet.org/4-tips-for-structuring-case-studies-in-your-design-portfolio-f7436fd460ec), [Hiration](https://www.hiration.com/blog/build-portfolio-for-job-search/) y [Coderhouse, que resume a NN/g](https://www.coderhouse.com/coderlibrary/documentar-caso-de-estudio-ux-para-recruiters). No pude abrir el artículo original de NN/g.

## Fuentes
- [Envato: tendencias 2026, grillas rotas y personalidad visual](https://elements.envato.com/learn/web-design-trends)
- [DesignRush: "Polished is no longer enough"](https://www.designrush.com/agency/website-design-development/trends/web-design-trends)
- [Figma: tendencias web 2026](https://www.figma.com/resource-library/web-design-trends/)
- [Line25: tendencias 2026](https://line25.com/articles/web-design-trends-2026/)
- [Bubble: qué entra y qué sale en 2026](https://bubble.io/blog/web-design-trends/)
- [Jakob Nielsen: Jakob's Law](https://jakobnielsenphd.substack.com/p/jakobs-law)
- [UX Collective: no reinventes la rueda, pero a veces sí](https://uxdesign.cc/jakobs-law-revisited-don-t-reinvent-the-wheel-but-sometimes-do-a59b2fb06a42)
- [Awwwards: Sites of the Year](https://www.awwwards.com/websites/sites_of_the_year/)
- [Awwwards: mejores portafolios](https://www.awwwards.com/websites/winner_category_portfolio/)
- [Juror: 10 sitios premiados 2026](https://www.hontran.dev/blog/best-award-winning-websites-2026)
