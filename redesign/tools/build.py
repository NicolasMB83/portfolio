"""Builds Option A v2 "Horizonte" (EN + ES) into redesign/a-v2/.

    python3 redesign/tools/build.py

Pages: home, Invest in Bogotá case, Radio a Domicilio case (chapter template), bilingual 404,
and two prototype variants of the work section (projects-a, projects-b).
Everything is self-hosted (images, fonts, Lottie player); nothing depends on Framer
except the three animated Lottie covers, which still load from framerusercontent.com.

Paths inside the markup use tokens that page() resolves for each page's depth:
    @A/  -> the shared assets folder      (e.g. "../assets/")
    @H/  -> the root of the site (a-v2)   (e.g. "../")
    @R/  -> the root of the repository    (files that live outside a-v2: CV, video, banners)
When the site is promoted to the repository root, set REPO_FROM_SITE = ''.
"""
import re, json, hashlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
PARTS = HERE / 'parts'
OUT = HERE.parent / 'a-v2'
REPO_FROM_SITE = '../../'
ABS_ROOT = None   # set to '/' once promoted: the 404 is served at any URL, so it needs root-absolute paths
LINK_INDEX = True  # prototype previews (raw.githack, file://) cannot open folders: link to .../index.html. False on Netlify.
BASE = 'https://nicolasmb.com/'
ASSET_V = hashlib.sha1((OUT / 'assets' / 'site.css').read_bytes() + (OUT / 'assets' / 'site.js').read_bytes()).hexdigest()[:10]
MANIFEST = {v['name']: v for v in json.loads((PARTS / 'img-manifest.json').read_text()).values()}


def symbol(name, sid):
    inner = re.search(r'<svg[^>]*>(.*)</svg>', (PARTS / 'icons' / f'{name}.svg').read_text(), re.S).group(1)
    return f'<symbol id="{sid}" viewBox="0 0 256 256">{inner}</symbol>'


def ic(sid, cls=''):
    return f'<svg class="icon {cls}" aria-hidden="true" focusable="false"><use href="#{sid}"/></svg>'


def go(kind=''):
    """The arrow inside the sun: on hover its outline is drawn from the horizon, then it fills (go--outline: no fill)."""
    return (f'<span class="go{(" " + kind) if kind else ""}" aria-hidden="true"><svg class="go-ring" viewBox="0 0 40 40" focusable="false">'
            '<circle cx="20" cy="20" r="18.6" pathLength="1"/></svg>' + ic('i-go') + '</span>')


GO = go()   # the dot of the "i" rises behind the arrow on hover


LOGO = (PARTS / 'frag-logo.svg').read_text().strip()
LOGO_SYMBOL = '<symbol id="logo-shape" viewBox="0 0 119.912 22">' + re.search(r'<svg[^>]*>(.*)</svg>', LOGO, re.S).group(1) + '</symbol>'
LOGO_PROSURGE = (PARTS / 'frag-prosurge.svg').read_text().strip()
LOGO_IIB = (PARTS / 'frag-iib.svg').read_text().strip()


def logo_letters():
    """The logotype split into its letters (sub-paths), left to right, each with its order in --i."""
    d = re.search(r' d="([^"]+)"', LOGO).group(1)
    subs = ['M' + x for x in re.split(r'\s*M\s*', d) if x.strip()]
    left = lambda sp: min(map(float, re.findall(r'-?\d+\.?\d*', sp)[0::2]))
    return ''.join(f'<path style="--i: {i}" d="{sp}"/>' for i, sp in enumerate(sorted(subs, key=left)))


END_LOGO = '<svg class="end-logo" viewBox="0 0 119.912 22" focusable="false">' + logo_letters() + '</svg>'
SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">' + ''.join([
    symbol('arrow-up-right', 'i-go'), symbol('arrow-left', 'i-back'), symbol('copy', 'i-copy'), symbol('check', 'i-check'),
    symbol('x', 'i-close'), symbol('envelope-simple', 'i-mail'), symbol('linkedin-logo', 'i-linkedin'),
    symbol('behance-logo', 'i-behance'), symbol('download-simple', 'i-download'), symbol('list', 'i-menu'),
]) + LOGO_SYMBOL + '</svg>'
EMAIL = 'nicolasbarbosa.us@gmail.com'
CV = '@R/assets/cv/NMB%202025%20CV%20EN%20v3.pdf'
FIGMA = 'https://www.figma.com/deck/A2FLZyFCZUkYItYyTG2Tgn/Portfolio-indepth-aug-25--Copy-?node-id=1-2107&amp;t=LsYBkuOOnqmHxrCe-1'
LOTTIE = 'https://framerusercontent.com/assets/{}.json'   # the only remaining Framer dependency (see PROPUESTAS.md)
P = '<!-- PROPUESTA DE TEXTO: {} -->'
ES_DRAFT = '<!-- Español: traducción fiel del inglés (aprobada la terminología del punto D) -->'

# ------------------------------------------------------------------ copy
T = {
 'en': dict(
  title='Nicolas MB - Designer',
  desc='Nicolás Mogollón Barbosa, visual and brand designer. Campaigns, identities and digital products for MinTIC, Invest in Bogotá, Radio a Domicilio and more.',
  nav_work='WORK', nav_about='ABOUT', nav_exp='EXPERIENCE', cta='Let’s talk', menu='Menu',
  other_lang='es', other_short='ES', other_name='Español',
  hint_text='¿Prefieres ver el sitio en español?', hint_btn='Ver en español', hint_close='Cerrar',
  h1a='I LOVE DESIGN', h1b='and I turn that passion into results',
  intro="I’m Nicolás, a multidisciplinary designer with experience in product design, digital design and social media campaigns.",
  work='WORK', view='VIEW PORTFOLIO',
  r_art='Art Director', r_vai='Visual and AI Designer', r_dgd='Digital Graphic Designer', r_vec='Visual Experience Coordinator', r_ad='Art Direction',
  s1='Digital Graphic Design', s1t='Developing design concepts that encompass visual identity, color palettes, typography, and visual guidelines.',
  s2='Web Design', s2t='Navigation structure strategies, visual design, mobile device optimization, and style guides.',
  s3='UI Design', s3t='Enhancing the user experience with intuitive interfaces for web and mobile apps.',
  s4='Brand Identity', s4t='Creating brand strategies, including logo design, color schemes, typography, and guidelines.',
  clients='Organizations that trust my work', career='Career path',
  roles=[
   ('Jan 2026 - Current', 'Graphic Designer, Creative', 'ReloQuest', [
      'Redesigned the interface of ReloQuest’s main website.',
      'Produce brand videos and now integrate AI video tools into the production workflow.',
      'Design social media graphics as well as digital and print collateral.',
      'Create print pieces such as backdrops, plus mockups that show each design in context.'], None),
   ('Feb 2025 - Jan 2026', 'Visual and AI Designer', 'Invest in Bogotá', [
      'Designed graphic assets for national and international investment promotion events.',
      'Created visual assets for social media campaigns that inform, promote and attract investment to Bogotá, the capital of Colombia.',
      'Implemented AI tools to support the design workflow across the Design department.'], None),
   ('Jan 2023 - Sept 2024', 'Art Director', 'Ondas y Ecos S.A.S.', [
      'Redesigned the company’s visual identity across digital platforms.',
      'Implemented design strategies for web and social media.',
      'Directed the Radio a Domicilio brand narrative, built on closeness and familiarity.'], None),
   ('Nov 2021 - Nov 2022', 'Visual Experience Coordinator', 'Infinited - Area Andina University', [
      'Led cross-functional collaboration between the marketing, design and development teams to deliver campaigns aligned with the university’s goals.',
      'Created interactive content aligned with the brand identity, helping the brand improve and evolve organically.',
      'Prototyped and deployed interfaces optimized for sales funnels.'], None),
   ('Jun 2017 - Aug 2022', 'Digital Graphic Designer', 'Colombian Ministry of ICT (MINTIC)', [
      'Created a wide range of graphic assets for government campaigns, including presentations (PowerPoint/Keynote), social media content, email campaigns, infographics, print materials, custom signage, branded furnishings and other specialty formats.',
      'Translated complex research and economic data into accessible visual materials, backed by international partnerships.',
      'Contributed to strategic planning sessions of the Digital Transformation and Economy departments.'], None),
  ],
  magic="Let’s make magic!", magic_sub='Working together to achieve greatness', cv='Download CV',
  copy='Copy', copied='Copied', copy_aria='Copy email address', close='Close',
  made='Created with passion, love, and design', rights='© 2026 Nicolás Mogollón Barbosa',
  # case study: Invest in Bogotá
  c_title='Invest in Bogotá - Nicolas MB', c_desc='Invest in Bogotá: visual and AI design for the investment promotion agency of Bogotá.',
  c_summary='The investment promotion agency for Bogotá&nbsp;– Region.',
  c_year='YEAR', c_company='COMPANY', c_role='ROLE', c_ind='INDUSTRY', c_srv='SERVICES', c_year_v='Feb 2025 - Jan 2026', c_ind_v='Investment',
  c_reel='SIGO presentation opener: Una idea que nace en Bogotá',
  c_aim='IBB’s aim is to facilitate relevant international investment and attract world-class meetings and events that contribute to the socioeconomic development, competitiveness and quality of life of Bogotá–Region. My role is to develop impactful collateral that builds a strong brand presence and keeps the brand’s narrative coherent.',
  c_obj='Objectives and challenges',
  c_ch=[('A brand to develop', 'IBB was rebranded in the first quarter of 2025, which made it the perfect moment to develop the brand. Through creative work for print, web and social media, the challenge is to preserve the brand while finding new ways to communicate.'),
        ('Keep the graphics sharp', "The biggest challenge is keeping the brand relevant. By researching current trends and styles every day, I keep the brand cohesive while creating content for web, digital and print media."),
        ('Keep evolving', 'Integrate AI tools into the process to reduce production times and to develop products that demand speed, complexity and quality.')],
  c_social='Social media', c_slides='Slides', c_other='Other work',
  alts=['Four social media pieces about Bogotá procurement rules, in red, blue and violet', 'Semana del Emprendedor poster with a Bogotá skyline photo',
        'Invest in Bogotá website pages for events and business guides', 'Presentation slide: Su mejor aliado estratégico',
        'MICE tourism post: En Bogotá, cada evento es una oportunidad', 'Post: Bogotá se vive con propósito, over the Santamaría bullring at night',
        'Convention Bureau call for unique tourism experiences, yellow isometric map', 'ScaleUpBog presentation slide',
        'Economic data slide comparing Colombia with Latin American markets', 'ABC Works for Taxes guide cover on a red circle',
        'Editorial spread with Bogotá cathedral and red circle device'],
  # case study: Radio a Domicilio (content from the site's CMS; chapter labels are proposals)
  r_title='Radio a Domicilio - Nicolas MB',
  r_desc='Radio a Domicilio: art direction for a radio brand, its website, campaigns and social media.',
  r_summary='Under the slogan “Radio at Home,” we set out to create an authentic, welcoming experience.',
  r_ind_v='Communications', r_year_v='2023-2024',
  chapters_label='Chapters',
  ch_obj='Objectives', ch_proc='Process', ch_res='Results',
  work_rad='Brand, web and campaigns', work_iib='Campaigns, presentations and web', c_aim_label='About the agency',
  r_company='Ondas y Ecos S.A.S.', new_tab='(opens in a new tab)',
  r_obj=[('Modern essence', 'Achieving a balance between an iconic identity and a modern touch that attracts new audiences.'),
         ('Multichannel consistency', 'Designing a visual identity that is adaptable and coherent across all channels.'),
         ('Visual engagement', 'Creating striking graphics that capture attention and keep users engaged on social media.')],
  r_phases=[('Discovery Phase', [('Market and Style Study', 'Researched audience preferences in depth to create an aesthetic that reinvents the legacy of Radio a Domicilio and attracts new listeners.')]),
            ('Design and Development', [('UI/UX Design', 'Designed a clean, intuitive interface with streamlined navigation and engaging visuals.'),
                                        ('Audience and Style Analysis', 'Analyzed how the audience responded to each visual direction to settle the final aesthetic.')]),
            ('Testing and Iteration', [('User Testing', 'Tested the web interface with a controlled group of users before launch to gather feedback on its use and on future features.'),
                                       ('Web Optimization', 'Optimized the interface to improve navigation on desktop and mobile.')])],
  r_results='“Radio a Domicilio” received positive feedback and an exceptional reception within the company. Metrics such as audience retention and participation exceeded expectations in the first three months, driven by an intuitive design and a content offering that connected with listeners of all ages.',
  r_next_label='Next steps',
  r_next=[('Continuous improvements', 'Planning regular updates based on audience feedback and industry trends, always seeking to enhance functionality and listener satisfaction.'),
          ('Expansion', 'Exploring collaborations with podcasting platforms and other media to expand the presence of “Radio a Domicilio” and enrich the listener experience with exclusive content.')],
  r_web='Web', r_banners='HTML5 banners', r_banner='Animated HTML5 banner',
  r_alts=dict(
    campaign='Campaign banner: La radio en casa, a smiling listener with yellow headphones next to the Radio a Domicilio logo',
    studio='A host in a yellow jacket reads a Radio a Domicilio script in the studio, in front of the branded backdrop',
    web='Radio a Domicilio website on a desktop monitor: La casa de todos',
    social='Two social media posts: ¡Súbele el volumen! and El café y la radio van de la mano',
    brand='Brand applications: website, hoodie, business cards and social media posts in yellow and violet',
    headphones='Headphones on a yellow background crossed by a violet stripe'),
 ),
 'es': dict(
  title='Nicolas MB - Diseñador',
  desc='Nicolás Mogollón Barbosa, diseñador visual y de marca. Campañas, identidades y productos digitales para MinTIC, Invest in Bogotá, Radio a Domicilio y más.',
  nav_work='PROYECTOS', nav_about='SOBRE MÍ', nav_exp='EXPERIENCIA', cta='Hablemos', menu='Menú',
  other_lang='en', other_short='EN', other_name='English',
  hint_text='Prefer to read this site in English?', hint_btn='View in English', hint_close='Close',
  h1a='AMO EL DISEÑO', h1b='y convierto esa pasión en resultados',
  intro='Soy Nicolás, diseñador multidisciplinario con experiencia en diseño de producto, diseño digital y campañas para redes sociales.',
  work='PROYECTOS', view='VER PORTAFOLIO',
  r_art='Director de arte', r_vai='Diseñador visual y de IA', r_dgd='Diseñador gráfico digital', r_vec='Coordinador de experiencia visual', r_ad='Dirección de arte',
  s1='Diseño gráfico digital', s1t='Desarrollo de conceptos de diseño que abarcan identidad visual, paletas de color, tipografía y lineamientos visuales.',
  s2='Diseño web', s2t='Estrategias de estructura de navegación, diseño visual, optimización para dispositivos móviles y guías de estilo.',
  s3='Diseño UI', s3t='Mejora de la experiencia de usuario con interfaces intuitivas para aplicaciones web y móviles.',
  s4='Identidad de marca', s4t='Creación de estrategias de marca, que incluyen diseño de logotipo, esquemas de color, tipografía y lineamientos.',
  clients='Organizaciones que confían en mi trabajo', career='Trayectoria',
  roles=[
   ('Ene 2026 - Actual', 'Diseñador gráfico, creativo', 'ReloQuest', [
      'Rediseñé la interfaz del sitio web principal de ReloQuest.',
      'Produzco videos de marca y ahora integro herramientas de video con IA en el flujo de producción.',
      'Diseño piezas gráficas para redes sociales, así como material publicitario digital e impreso.',
      'Creo piezas impresas como <i>backdrops</i>, además de <i>mockups</i> que muestran cada diseño en contexto.'], None),
   ('Feb 2025 - Ene 2026', 'Diseñador visual y de IA', 'Invest in Bogotá', [
      'Diseñé piezas gráficas para eventos nacionales e internacionales de promoción de inversión.',
      'Creé piezas visuales para campañas en redes sociales que informan, promueven y atraen inversión a Bogotá, la capital de Colombia.',
      'Implementé herramientas de IA para apoyar el flujo de trabajo en todo el departamento de Diseño.'], None),
   ('Ene 2023 - Sept 2024', 'Director de arte', 'Ondas y Ecos S.A.S.', [
      'Rediseñé la identidad visual de la empresa en sus plataformas digitales.',
      'Implementé estrategias de diseño para web y redes sociales.',
      'Dirigí la narrativa de la marca Radio a Domicilio, basada en la cercanía y la familiaridad.'], None),
   ('Nov 2021 - Nov 2022', 'Coordinador de experiencia visual', 'Infinited - Universidad del Área Andina', [
      'Lideré la colaboración interdisciplinaria entre los equipos de mercadeo, diseño y desarrollo para entregar campañas alineadas con los objetivos de la universidad.',
      'Creé contenido interactivo alineado con la identidad de marca, que ayudó a la marca a mejorar y evolucionar de forma orgánica.',
      'Prototipé y desplegué interfaces optimizadas para embudos de ventas.'], None),
   ('Jun 2017 - Ago 2022', 'Diseñador gráfico digital', 'Ministerio TIC de Colombia (MINTIC)', [
      'Creé una amplia gama de piezas gráficas para campañas del gobierno, incluyendo presentaciones (PowerPoint/Keynote), contenido para redes sociales, campañas de email, infografías, material impreso, señalética personalizada, mobiliario de marca y otros formatos especiales.',
      'Traduje investigaciones complejas y datos económicos en materiales visuales accesibles, respaldados por alianzas internacionales.',
      'Contribuí a las sesiones de planeación estratégica de los departamentos de Transformación Digital y Economía.'], None),
  ],
  magic='¡Hagamos magia!', magic_sub='Trabajando juntos para lograr grandes cosas', cv='Descargar CV',
  copy='Copiar', copied='Copiado', copy_aria='Copiar correo', close='Cerrar',
  made='Creado con pasión, amor y diseño', rights='© 2026 Nicolás Mogollón Barbosa',
  c_title='Invest in Bogotá - Nicolas MB', c_desc='Invest in Bogotá: diseño visual y con IA para la agencia de promoción de inversión de Bogotá.',
  c_summary='La agencia de promoción de inversión de Bogotá&nbsp;– Región.',
  c_year='AÑO', c_company='EMPRESA', c_role='ROL', c_ind='INDUSTRIA', c_srv='SERVICIOS', c_year_v='Feb 2025 - Ene 2026', c_ind_v='Inversión',
  c_reel='Apertura de la presentación de SIGO: Una idea que nace en Bogotá',
  c_aim='El objetivo de IBB es facilitar inversiones internacionales relevantes y atraer reuniones y eventos de talla mundial que contribuyan al desarrollo socioeconómico, la competitividad y la calidad de vida de Bogotá–Región. Mi labor es desarrollar piezas de impacto que construyan una presencia de marca sólida y mantengan coherente su narrativa.',
  c_obj='Objetivos y retos',
  c_ch=[('Una marca por desarrollar', 'IBB renovó su marca en el primer trimestre de 2025, lo que hizo de este el momento perfecto para desarrollarla. A través de piezas creativas impresas, web y para redes sociales, el reto es preservar la marca mientras se encuentran nuevas formas de comunicar.'),
        ('Mantener gráficas impecables', 'El mayor reto es mantener la marca vigente. Investigando cada día tendencias y estilos actuales, mantengo la cohesión de la marca mientras creo contenido para medios web, digitales e impresos.'),
        ('Seguir evolucionando', 'Integrar herramientas de IA al proceso para reducir los tiempos de producción y desarrollar productos que exigen velocidad, complejidad y calidad.')],
  c_social='Redes sociales', c_slides='Diapositivas', c_other='Otros proyectos',
  alts=['Cuatro piezas para redes sociales sobre las reglas de contratación de Bogotá, en rojo, azul y violeta', 'Afiche de la Semana del Emprendedor con el skyline de Bogotá',
        'Páginas del sitio web de Invest in Bogotá para eventos y guías de negocios', 'Diapositiva: Su mejor aliado estratégico',
        'Post de turismo MICE: En Bogotá, cada evento es una oportunidad', 'Post: Bogotá se vive con propósito, sobre la plaza de toros La Santamaría de noche',
        'Convocatoria del Convention Bureau para experiencias turísticas únicas, mapa isométrico amarillo', 'Diapositiva de la presentación de ScaleUpBog',
        'Diapositiva con datos económicos que compara a Colombia con mercados latinoamericanos', 'Portada de la guía ABC Obras por Impuestos sobre un círculo rojo',
        'Doble página editorial con la catedral de Bogotá y el círculo rojo'],
  r_title='Radio a Domicilio - Nicolas MB',
  r_desc='Radio a Domicilio: dirección de arte para una marca de radio, su sitio web, campañas y redes sociales.',
  r_summary='Bajo el lema “Radio a Domicilio”, buscamos crear una experiencia auténtica y acogedora.',
  r_ind_v='Comunicaciones', r_year_v='2023-2024',
  chapters_label='Capítulos',
  ch_obj='Objetivos', ch_proc='Proceso', ch_res='Resultados',
  work_rad='Marca, web y campañas', work_iib='Campañas, presentaciones y web', c_aim_label='Sobre la agencia',
  r_company='Ondas y Ecos S.A.S.', new_tab='(se abre en una pestaña nueva)',
  r_obj=[('Esencia moderna', 'Lograr un equilibrio entre una identidad icónica y un toque moderno que atraiga nuevas audiencias.'),
         ('Coherencia multicanal', 'Diseñar una identidad visual adaptable y coherente en todos los canales.'),
         ('Conexión visual', 'Crear gráficas llamativas que capten la atención y retengan a los usuarios en redes sociales.')],
  r_phases=[('Fase de descubrimiento', [('Estudio de mercado y estilo', 'Investigué a fondo las preferencias de la audiencia para crear una estética que reinventara el legado de Radio a Domicilio y atrajera nuevos oyentes.')]),
            ('Diseño y desarrollo', [('Diseño UI/UX', 'Diseñé una interfaz limpia e intuitiva, con navegación simplificada y visuales atractivos.'),
                                     ('Análisis de audiencia y estilo', 'Analicé cómo respondía la audiencia a cada dirección visual para definir la estética final.')]),
            ('Pruebas e iteración', [('Pruebas con usuarios', 'Probé la interfaz web con un grupo controlado de usuarios antes del lanzamiento para recoger comentarios sobre su uso y sobre funciones futuras.'),
                                     ('Optimización web', 'Optimicé la interfaz para mejorar la navegación en computador y celular.')])],
  r_results='“Radio a Domicilio” recibió comentarios positivos y una acogida excepcional en la empresa. Métricas como la retención y la participación de la audiencia superaron las expectativas en los primeros tres meses, impulsadas por un diseño intuitivo y una oferta de contenido que conectó con oyentes de todas las edades.',
  r_next_label='Próximos pasos',
  r_next=[('Mejoras continuas', 'Planear actualizaciones periódicas basadas en los comentarios de la audiencia y las tendencias del sector, buscando siempre mejorar la funcionalidad y la satisfacción de los oyentes.'),
          ('Expansión', 'Explorar colaboraciones con plataformas de pódcast y otros medios para ampliar la presencia de “Radio a Domicilio” y enriquecer la experiencia de los oyentes con contenido exclusivo.')],
  r_web='Web', r_banners='Banners HTML5', r_banner='Banner HTML5 animado',
  r_alts=dict(
    campaign='Banner de campaña: La radio en casa, una oyente sonriente con audífonos amarillos junto al logo de Radio a Domicilio',
    studio='Un locutor con chaqueta amarilla lee un guion de Radio a Domicilio en el estudio, frente al backdrop de la marca',
    web='Sitio web de Radio a Domicilio en un monitor de escritorio: La casa de todos',
    social='Dos piezas para redes sociales: ¡Súbele el volumen! y El café y la radio van de la mano',
    brand='Aplicaciones de marca: sitio web, buzo, tarjetas de presentación y piezas para redes sociales en amarillo y violeta',
    headphones='Audífonos sobre un fondo amarillo atravesado por una franja violeta'),
 ),
}

# The six projects. Colours are sampled from each project's own material; Vende Digital stays neutral
# until its cover can be checked (its only cover is the Lottie animation on Framer).
PROJECTS = [
    dict(slug='radio-a-domicilio', title='Radio a Domicilio', role='r_art', lottie='LzoOJsiAnZTMUyRsHiyCzTp4XY', poster='rad-brand', client='#ffc845', shape='arch'),
    dict(slug='invest-in-bogota', title='Invest in Bogotá', role='r_vai', lottie='xMkFo0SEeC5T5e9mvolD6PBvXW8', poster='iib-social-grid', client='#ef491f', shape='circle'),
    dict(slug='vende-digital', title='Vende Digital', role='r_dgd', lottie='opJXddsePYvkvZBgp7zGeH5vII8', poster='vd-key-visual', client='oklch(0.8 0.035 278)', shape='wide'),
    dict(slug='infinited', title='Infinited', role='r_vec', img='infinited-cover', client='#1fc8c8', shape='square'),
    dict(slug='col40-2018', title='Colombia 4.0 (2018)', role='r_dgd', img='col40-cover', client='#ff6a00', shape='bowl'),
    dict(slug='pro-surge-ja', title='Pro Surge JA', role='r_ad', img='prosurge-cover', client='#4a63ff', shape='band'),
]
PJ = {p['slug']: p for p in PROJECTS}


# ------------------------------------------------------------------ images (self-hosted WebP, responsive)
def pic(name, sizes, alt='', cls='', eager=False):
    m = MANIFEST[name]
    if 'file' in m:   # vector
        return f'<img{f" class={chr(34)}{cls}{chr(34)}" if cls else ""} src="@A/img/{m["file"]}" alt="{alt}" loading="lazy" decoding="async">'
    ws = m['sizes']
    w = ws[-1]
    h = round(m['h'] * w / m['w'])
    srcset = ', '.join(f'@A/img/{name}-{s}.webp {s}w' for s in ws)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="@A/img/{name}-{ws[min(1, len(ws) - 1)]}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {load} decoding="async">'


# ------------------------------------------------------------------ partials
def head(lang, title, desc, alternates):
    alt = ''.join(f'\n  <link rel="alternate" hreflang="{hl}" href="{href}">' for hl, href in alternates)
    canonical = dict(alternates)[lang]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#f6f7fd">
  <link rel="canonical" href="{canonical}">{alt}
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{'en_US' if lang == 'en' else 'es_CO'}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <link rel="icon" href="@A/img/favicon-light.png" media="(prefers-color-scheme: light)">
  <link rel="icon" href="@A/img/favicon-dark.png" media="(prefers-color-scheme: dark)">
  <link rel="preload" as="font" type="font/woff2" crossorigin href="@A/fonts/clash-display-700.woff2">
  <link rel="preload" as="font" type="font/woff2" crossorigin href="@A/fonts/albert-sans-400.woff2">
  <link rel="stylesheet" href="@A/site.css?v={ASSET_V}">
  <script src="@A/site.js?v={ASSET_V}" defer></script>
</head>'''


def lang_link(t, href, cls='lang-switch', full=False):
    label = t['other_name'] if full else t['other_short']
    aria = '' if full else f' aria-label="{t["other_name"]}"'
    return f'<a class="{cls}" href="{href}" hreflang="{t["other_lang"]}" lang="{t["other_lang"]}"{aria} data-lang-switch>{label}</a>'


def header(t, home, other):
    return f'''
  <header class="site-header" data-header>
    <div class="wrap header-inner">
      <a class="brand" href="{home}" aria-label="Nicolas MB"><svg class="brand-halo" viewBox="0 0 119.912 22" aria-hidden="true" focusable="false"><use href="#logo-shape"/></svg>{LOGO}</a>
      <nav class="nav" aria-label="Primary">
        <ul class="nav-links">
          <li><a href="{home}#work">{t['nav_work']}</a></li>
          <li><a href="{home}#about">{t['nav_about']}</a></li>
          <li><a href="{home}#experience">{t['nav_exp']}</a></li>
        </ul>
        {lang_link(t, other)}
        <a class="btn btn--sun" href="{home}#contact" data-contact>{t['cta']} {GO}</a>
      </nav>
      <div class="header-tools">
        {lang_link(t, other)}
        <button class="menu-toggle" type="button" popovertarget="menu" aria-controls="menu" aria-expanded="false" aria-label="{t['menu']}">{ic('i-menu')}</button>
      </div>
    </div>
  </header>

  <div id="menu" class="menu" popover>
    <ul>
      <li><a href="{home}#work">{t['nav_work']}</a></li>
      <li><a href="{home}#about">{t['nav_about']}</a></li>
      <li><a href="{home}#experience">{t['nav_exp']}</a></li>
    </ul>
    <a class="btn btn--sun btn--lg" href="{home}#contact" data-contact>{t['cta']} {GO}</a>
  </div>'''


def hint(t, other):
    return f'''
  <div class="lang-hint" lang="{t['other_lang']}" data-lang-hint="{t['other_lang']}" role="region" aria-label="{t['other_name']}" hidden>
    <span>{t['hint_text']}</span>
    <a class="btn btn--sun" href="{other}" hreflang="{t['other_lang']}" data-lang-switch>{t['hint_btn']}</a>
    <button class="x" type="button" data-dismiss aria-label="{t['hint_close']}">{ic('i-close')}</button>
  </div>'''


def email_row(t):
    return f'''<div class="email-row">
          <span class="email-address">{EMAIL}</span>
          <button class="btn copy-btn" type="button" data-copy="{EMAIL}" aria-label="{t['copy_aria']}">
            <span class="when-idle">{ic('i-copy')} {t['copy']}</span>
            <span class="when-done">{ic('i-check')} {t['copied']}</span>
          </button>
          <span class="sr-only" role="status" data-copy-status></span>
        </div>'''


def socials(t):
    nt = t['new_tab']   # links that open a new tab say so to screen readers (W3C technique G201)
    return f'''<ul class="socials">
          <li><a href="https://www.linkedin.com/in/nicolasmb" target="_blank" rel="noopener" aria-label="LinkedIn {nt}">{ic('i-linkedin')}</a></li>
          <li><a href="https://www.behance.net/NicolasMB" target="_blank" rel="noopener" aria-label="Behance {nt}">{ic('i-behance')}</a></li>
          <li><a href="mailto:{EMAIL}" aria-label="Email">{ic('i-mail')}</a></li>
        </ul>'''


def sheet(t):
    return f'''
  <dialog id="contact-sheet" class="sheet" aria-labelledby="sheet-title">
    <div class="sheet-inner">
      <button class="sheet-close" type="button" data-close aria-label="{t['close']}">{ic('i-close')}</button>
      <div class="sky"><span class="sun" aria-hidden="true"></span><h2 id="sheet-title" class="rise sheet-title">{t['magic']}</h2></div>
      <span class="horizon horizon--night horizon--sun" style="margin-inline:0" aria-hidden="true"></span>
      <p class="contact-sub">{t['magic_sub']}</p>
      {email_row(t)}
      <div class="sheet-actions">
        <a class="btn btn--sun btn--lg" href="mailto:{EMAIL}">{t['cta']} {GO}</a>
        <a class="btn btn--line btn--lg" href="{CV}" target="_blank" rel="noopener">{t['cv']}<span class="sr-only"> {t['new_tab']}</span> {ic('i-download')}</a>
      </div>
      {socials(t)}
    </div>
  </dialog>'''


def footer(t, other):
    return f'''
  <footer id="contact" class="contact is-night">
    <div class="wrap">
      <div class="sky"><h2 class="rise contact-title">{t['magic']}</h2></div>
      <span class="horizon" aria-hidden="true"></span>
      <p class="contact-sub">{t['magic_sub']}</p>
      {email_row(t)}
      <div class="contact-actions">
        <div class="cta-group">
          <a class="btn btn--sun btn--lg" href="mailto:{EMAIL}">{t['cta']} {GO}</a>
          <a class="btn btn--line btn--lg" href="{CV}" target="_blank" rel="noopener">{t['cv']}<span class="sr-only"> {t['new_tab']}</span> {ic('i-download')}</a>
        </div>
        {socials(t)}
      </div>
      <div class="footer-bar">
        <p>{t['made']} <span class="heart">♥</span></p>
        <div class="footer-end">
          {lang_link(t, other, full=True)}
          <a href="https://www.be.net/nicolasmb">{t['rights']}</a>
        </div>
      </div>
    </div>
    <div class="end-mark" aria-hidden="true" data-reveal>{END_LOGO}</div>
  </footer>'''


def cover(p, sizes):
    """The media of a project: its Lottie cover (with a local poster underneath) or a local image."""
    if p.get('lottie'):
        poster = pic(p['poster'], sizes, cls='poster') if p.get('poster') else ''
        return f' data-lottie="{LOTTIE.format(p["lottie"])}"', poster
    return '', pic(p['img'], sizes)


def project(t, home, slug, cls='', sizes='(max-width: 760px) 100vw, 58vw'):
    p = PJ[slug]
    attrs, media = cover(p, sizes)
    return f'''
          <li class="project {cls}">
            <a class="project-link" href="{home}{slug}/">
              <div class="project-media"{attrs}>{media}<span class="card-go">{go('go--sun')}</span></div>
              <div class="project-meta">
                <h3 class="project-title">{p['title']}</h3>
                <p class="project-role">{t[p['role']]}</p>
              </div>
            </a>
          </li>'''


def work_grid(t, home):
    return f'''<ul class="grid projects">''' + \
        project(t, home, 'radio-a-domicilio') + \
        project(t, home, 'invest-in-bogota', 'project--narrow', '(max-width: 760px) 100vw, 42vw') + \
        project(t, home, 'vende-digital') + \
        project(t, home, 'infinited', 'project--narrow project--square', '(max-width: 760px) 100vw, 42vw') + \
        project(t, home, 'col40-2018', 'project--narrow project--square', '(max-width: 760px) 100vw, 42vw') + \
        project(t, home, 'pro-surge-ja') + '''
        </ul>'''


def work_plates(t, home):
    """Alternative A: art direction per project. Each project gets its client's colour, a shape from
    the logotype's vocabulary (arch, dot, line) and its own place in an asymmetric composition."""
    sizes = {'arch': '(max-width: 760px) 100vw, 40vw', 'circle': '(max-width: 760px) 100vw, 40vw', 'wide': '(max-width: 760px) 100vw, 90vw',
             'square': '(max-width: 760px) 100vw, 33vw', 'bowl': '(max-width: 760px) 100vw, 40vw', 'band': '100vw'}
    out = []
    for i, p in enumerate(PROJECTS, 1):
        attrs, media = cover(p, sizes[p['shape']])
        out.append(f'''
          <li class="plate plate--{p['shape']}" style="--client: {p['client']}">
            <a class="plate-link" href="{home}{p['slug']}/">
              <div class="plate-media"><div class="project-media"{attrs}>{media}</div></div>
              <div class="plate-text">
                <span class="plate-no" aria-hidden="true">{i:02d}</span>
                <h3 class="plate-title">{p['title']}</h3>
                <p class="project-role">{t[p['role']]}</p>
              </div>
            </a>
          </li>''')
    return '<ol class="plates">' + ''.join(out) + '\n        </ol>'


GREASE = '<svg class="grease" viewBox="0 0 200 140" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path pathLength="1" d="M30 26C62 6 142 4 178 24S204 104 160 124 40 138 14 104 6 44 44 22 92 8 112 10"/></svg>'


def work_sheet(t, home):
    """Alternative B: a contact sheet. The projects are frames on strips of film (continuity with the
    deck and the contact section). Hovering a frame brings it to full colour and circles it in grease pencil."""
    out = []
    for i, p in enumerate(PROJECTS, 1):
        attrs, media = cover(p, '(max-width: 600px) 100vw, (max-width: 1080px) 50vw, 33vw')
        out.append(f'''
          <li class="frame">
            <a class="frame-link" href="{home}{p['slug']}/">
              <div class="frame-strip">
                <div class="project-media frame-media"{attrs}>{media}</div>
                <span class="frame-edge" aria-hidden="true"><span>NMB&ensp;{i:02d}</span><span>&#9656;&ensp;{i}A</span></span>
                {GREASE}
              </div>
              <div class="project-meta">
                <h3 class="project-title">{p['title']}</h3>
                <p class="project-role">{t[p['role']]}</p>
              </div>
            </a>
          </li>''')
    return '<ol class="contact-sheet">' + ''.join(out) + '\n        </ol>'


def work_tiles(t, home):
    """Alternative C, fusion: the current indigo section with B's balanced grid (three equal frames per row,
    less scroll) and B's colour reveal. The hand-drawn circle becomes the brand's geometry: each row sits on
    one continuous horizon; on hover the frame's stretch of it lights up and the sun rises at its end."""
    out = []
    for p in PROJECTS:
        attrs, media = cover(p, '(max-width: 600px) 100vw, (max-width: 1080px) 50vw, 33vw')
        out.append(f'''
          <li class="tile">
            <a class="project-link tile-link" href="{home}{p['slug']}/">
              <div class="project-media tile-media"{attrs}>{media}<span class="card-go">{go('go--sun')}</span></div>
              <span class="tile-line" aria-hidden="true"></span>
              <div class="project-meta tile-meta">
                <h3 class="project-title">{p['title']}</h3>
                <p class="project-role">{t[p['role']]}</p>
              </div>
            </a>
          </li>''')
    return '<ul class="tiles">' + ''.join(out) + '\n        </ul>'


from review import REVIEW, APPLIED
from projects import VD, INF, PS


def mark_review(html):
    """Style review: put <!-- PROPUESTA DE TEXTO R<n>: ... --> right before each reviewed text (never inside a tag)."""
    for n, where, en_old, en_new, es_old, es_new, why in REVIEW:
        if n in APPLIED:
            continue
        for old, new in ((en_old, en_new), (es_old, es_new)):
            if not old:
                continue
            start = 1 if old.startswith('>') else 0
            i = html.find(old)
            while i != -1 and html.rfind('<', 0, i + start) > html.rfind('>', 0, i + start):
                i = html.find(old, i + 1)   # inside a tag (e.g. an attribute): look further
            if i != -1:
                i += start
                html = html[:i] + f'<!-- PROPUESTA DE TEXTO R{n}: {new} -->' + html[i:]
    return html


def page(lang, depth, body, title, desc, alternates, body_cls='', robots=None, absolute=False):
    up = ABS_ROOT if (absolute and ABS_ROOT) else '../' * depth
    cls = f' class="{body_cls}"' if body_cls else ''
    html = head(lang, title, desc, alternates) + f'\n<body{cls}>\n  ' + SPRITE + body + \
        '\n  <div class="vt-horizon" aria-hidden="true"></div>\n</body>\n</html>\n'
    if body_cls == 'page-night':
        html = html.replace('<meta name="theme-color" content="#f6f7fd">', '<meta name="theme-color" content="#101025">')
    if robots:
        html = html.replace('  <link rel="canonical"', f'  <meta name="robots" content="{robots}">\n  <link rel="canonical"', 1)
    html = html.replace('@A/', up + 'assets/').replace('@R/', up + REPO_FROM_SITE).replace('@H/', up or './')
    html = mark_review(html)
    if LINK_INDEX:
        html = re.sub(r'href="(\.\.?/(?:[^"#:]*/)?)(#[^"]*)?"', lambda m: f'href="{m.group(1)}index.html{m.group(2) or ""}"', html)
    return html


def roles_html(t):
    out = []
    for dates, title, place, points, note in t['roles']:
        pts = ''.join(f'\n                <li>{p}</li>' for p in points)
        out.append(f'''
          <li class="role">{(chr(10) + '            ' + P.format(note)) if note else ''}
            <p class="role-dates">{dates}</p>
            <div>
              <h3 class="role-title">{title}</h3>
              <p class="role-place">{place}</p>
              <ul class="points">{pts}
              </ul>
            </div>
          </li>''')
    return ''.join(out)


# ------------------------------------------------------------------ HOME
def home(lang, variant='grid'):
    t = T[lang]
    h = '@H/' if lang == 'en' else '@H/es/'
    other = '@H/es/' if lang == 'en' else '@H/'
    note = ES_DRAFT if lang == 'es' else ''
    work_cls, work_list = {
        'grid': ('work is-night', work_grid(t, h)),
        'plates': ('work work--plates is-night', work_plates(t, h)),
        'sheet': ('work work--sheet is-night', work_sheet(t, h)),
        'tiles': ('work work--tiles is-night', work_tiles(t, h)),
    }[variant]
    proto = '' if variant == 'grid' else '\n  <!-- PROTOTIPO: alternativa ' + {'plates': 'A, dirección de arte por proyecto', 'sheet': 'B, hoja de contactos', 'tiles': 'C, fusión (grilla de B + marca)'}[variant] + '. Solo cambia la sección de proyectos. -->'
    body = proto + hint(t, other) + header(t, h, other) + sheet(t) + f'''

  <main>{note}
    <section class="hero">
      <div class="wrap">
        <h1 class="hero-title">
          <span class="sky"><span class="sun" aria-hidden="true"></span><span class="rise"><span class="hero-a display-1">{t['h1a']}</span> <span class="hero-b lede">{t['h1b']}</span></span></span>
          <span class="horizon horizon--sun" aria-hidden="true"></span>
        </h1>
        <div class="hero-below">
          <p class="hero-intro body-lg">{t['intro']}</p>
        </div>
      </div>
    </section>

    <section id="work" class="{work_cls}" aria-labelledby="work-title">
      <div class="wrap">
        <div class="titled">
          <div class="sky"><h2 id="work-title" class="rise display-2">{t['work']}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </div>
        {work_list}

        <a class="view-all" href="{FIGMA}">
          <span>{t['view']}</span>
          {go('go--sun')}
        </a>
      </div>
    </section>

    <section id="about" class="about">
      <div class="wrap">
        <h2 class="sr-only">{t['nav_about']}</h2>
        <ul class="svc">''' + ''.join(f'''
          <li class="svc-item" style="--i: {i}">
            <div class="svc-sky"><span class="svc-plate"><img src="@A/img/{f}.svg" width="{w}" height="{hh}" alt="" loading="lazy" decoding="async"></span></div>
            <h3 class="svc-title">{t[k]}</h3>
            <p class="svc-text">{t[k + 't']}</p>
            <p class="svc-work">{' · '.join(f'<a href="{h}{slug}/">{PJ[slug]["title"]}</a>' for slug in work)}</p>
          </li>''' for i, (k, f, w, hh, work) in enumerate([('s1', 'service-graphic', 1024, 1024, ('invest-in-bogota', 'vende-digital')), ('s2', 'service-web', 797, 813, ('radio-a-domicilio', 'infinited')), ('s3', 'service-ui', 1024, 1024, ('infinited', 'radio-a-domicilio')), ('s4', 'service-brand', 1024, 1024, ('pro-surge-ja', 'radio-a-domicilio'))])) + f'''
        </ul>
      </div>
      <div class="clients is-night">
        <div class="wrap">
          <h2 class="clients-title">{t['clients']}</h2>
          <ul class="client-list">
            <li><img class="client-logo client-logo--tall" src="@A/img/logo-mintic.svg" width="512" height="110" alt="MinTIC" loading="lazy" decoding="async"></li>
            <li><img class="client-logo" src="@A/img/logo-areandina.svg" width="137" height="32" alt="Areandina" loading="lazy" decoding="async"></li>
            <li><img class="client-logo client-logo--tall" src="@A/img/logo-ean.svg" width="138" height="32" alt="EAN" loading="lazy" decoding="async"></li>
            <li>{LOGO_PROSURGE}</li>
            <li>{LOGO_IIB}</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="experience" class="experience" aria-labelledby="exp-title">
      <div class="wrap grid">
        <div class="exp-head titled">
          <div class="sky"><h2 id="exp-title" class="rise display-2" style="padding-bottom:.16em">{t['career']}</h2></div>
          <span class="horizon" style="margin-inline:0" aria-hidden="true"></span>
        </div>
        <ol class="roles">{roles_html(t)}
        </ol>
      </div>
    </section>
  </main>
''' + footer(t, other)
    alts = [('en', BASE), ('es', BASE + 'es/'), ('x-default', BASE)]
    if variant != 'grid':
        return page(lang, 1, body, t['title'], t['desc'], alts, robots='noindex')
    return page(lang, 0 if lang == 'en' else 1, body, t['title'], t['desc'], alts)


# ------------------------------------------------------------------ CASE STUDIES
# Each project has its own structure (each project is different), but they share a family:
# the same cover (title on the horizon + short description + Year / Company / Role), type, horizon and frames.
WAVES = '''<svg class="waves cover-shape" viewBox="0 0 240 120" aria-hidden="true" focusable="false">
            <path class="w w1" d="M96 120a24 24 0 0 1 48 0"/>
            <path class="w w2" d="M66 120a54 54 0 0 1 108 0"/>
            <path class="w w3" d="M36 120a84 84 0 0 1 168 0"/>
            <path class="w w4" d="M6 120a114 114 0 0 1 228 0"/>
          </svg>'''
BANNERS = [('300x600', 300, 600), ('160x600', 160, 600), ('300x250', 300, 250), ('320x50', 320, 50), ('930x180', 930, 180)]
BEHANCE = {'radio-a-domicilio': 'https://www.behance.net/gallery/190745145/Radio-a-Domicilio',
           'invest-in-bogota': 'https://www.behance.net/gallery/230400817/Invest-in-Bogota'}


def fig(name, cls, sizes, alt):
    c = f' class="{cls}"' if cls else ''
    return f'<figure{c}>{pic(name, sizes, alt)}</figure>'


def behance_link(t, slug):
    return f'<a class="behance-link" href="{BEHANCE[slug]}" target="_blank" rel="noopener">{ic("i-behance")} Behance<span class="sr-only"> {t["new_tab"]}</span> {go("go--outline")}</a>'


def objectives_html(items):
    return '<ol class="objectives">' + ''.join(f'''
            <li class="objective"><h3>{hd}</h3><p>{p}</p></li>''' for hd, p in items) + '\n          </ol>'


def case_cover(t, h, title, shape, desc, facts, media, sun=False, stage=''):
    """The cover every project shares: back link, title rising from the horizon beside the client's shape,
    a short description, Year / Company / Role, and the opening image."""
    note = ''
    return f'''
    <section class="case-hero chapter-cover{' chapter-cover--sun' if sun else ''} is-night tone-night">
      <div class="wrap">
        <a class="back-link" href="{h}#work">{ic('i-back')} {t['work']}</a>
        <h1 class="title-lg">
          <span class="sky">{shape}<span class="rise">{title}</span></span>
        </h1>
        <span class="horizon horizon--sun" aria-hidden="true"></span>
        <p class="case-desc">{desc}</p>
        {note}
        <dl class="facts">
          <div><dt>{t['c_year']}</dt><dd>{facts[0]}</dd></div>
          <div><dt>{t['c_company']}</dt><dd>{facts[1]}</dd></div>
          <div><dt>{t['c_role']}</dt><dd>{facts[2]}</dd></div>
        </dl>
      </div>
    </section>
    <div class="cover-stage{(" cover-stage--" + stage) if stage else ""} is-night tone-night"><div class="wrap cover-wrap">{media}</div></div>'''


def other_work(t, h, items):
    others = ''.join(project(t, h, s, c, z) for s, c, z in items)
    return f'''
    <section class="other-work is-night" aria-labelledby="other-title">
      <div class="wrap">
        <div class="titled">
          <div class="sky"><h2 id="other-title" class="rise display-2" style="padding-bottom:.16em">{t['c_other']}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </div>
        <ul class="grid projects">{others}
        </ul>
      </div>
    </section>'''


def case_shell(lang, slug, meta, client, client_ink, main_html):
    t = dict(T[lang], _lang=lang)
    depth = 1 if lang == 'en' else 2
    h = '@H/' if lang == 'en' else '@H/es/'
    other = f'@H/es/{slug}/' if lang == 'en' else f'@H/{slug}/'
    note = ES_DRAFT if lang == 'es' else ''
    body = hint(t, other) + header(t, h, other) + sheet(t) + f'''

  <main style="--client: {client}; --client-ink: {client_ink}">{note}{main_html(t, h)}
  </main>
''' + footer(t, other)
    alts = [('en', BASE + f'{slug}/'), ('es', BASE + f'es/{slug}/'), ('x-default', BASE + f'{slug}/')]
    return page(lang, depth, body, meta(t)[0], meta(t)[1], alts, 'page-chapters')


# ---------- Radio a Domicilio: a story told in numbered chapters (objectives, process, pieces, results)
def chapter_head(n, label, hid):
    return f'''<header class="chapter-head">
          <div class="sky"><span class="rise chapter-no" aria-hidden="true">{n:02d}</span><h2 id="{hid}" class="rise chapter-title"><span class="sr-only">{n:02d}. </span>{label}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </header>'''


def rad_main(t, h):
    ra = t['r_alts']
    phases = '<ol class="phases">' + ''.join(f'''
            <li class="phase">
              <span class="phase-dot" aria-hidden="true"></span>
              <h3 class="phase-title">{ph}</h3>''' + ''.join(f'''
              <h4>{ih}</h4>
              <p>{ip}</p>''' for ih, ip in items) + '''
            </li>''' for ph, items in t['r_phases']) + '\n          </ol>'
    banners = ''.join(f'''
              <figure class="banner banner--{k}" style="--bw: {w}; --bh: {hh}">
                <iframe src="@R/ads/rad/{k}/index.html" width="{w}" height="{hh}" title="{t['r_banner']} {w}×{hh}" loading="lazy" sandbox="allow-scripts" scrolling="no"></iframe>
                <figcaption>{w} × {hh}</figcaption>
              </figure>''' for k, w, hh in BANNERS)
    work = f'''<div class="gallery">
            {fig('rad-web', 'g-7', '(max-width: 760px) 100vw, 58vw', ra['web'])}
            {fig('rad-studio', 'g-5', '(max-width: 760px) 100vw, 40vw', ra['studio'])}
            {fig('rad-campaign', '', '(max-width: 760px) 100vw, 1320px', ra['campaign'])}
            <div class="gallery-label"><h3>{t['c_social']}</h3></div>
            {fig('rad-social', 'g-7', '(max-width: 760px) 100vw, 58vw', ra['social'])}
            {fig('rad-headphones', 'g-5', '(max-width: 760px) 100vw, 40vw', ra['headphones'])}
            <div class="gallery-label">{P.format('“HTML5 banners” es un rótulo nuevo')}<h3>{t['r_banners']}</h3></div>
            <div class="banners">{banners}
            </div>
          </div>'''
    nxt = ''.join(f'''
                <li><h4>{hd}</h4><p>{p}</p></li>''' for hd, p in t['r_next'])
    results = f'''<div class="chapter-body grid">
            <p class="results lede">{t['r_results']}</p>
            <div class="next">
              <h3>{t['r_next_label']}</h3>
              <ul>{nxt}
              </ul>
              {behance_link(t, 'radio-a-domicilio')}
            </div>
          </div>'''
    chs = [('objectives', t['ch_obj'], objectives_html(t['r_obj']), False),
           ('process', t['ch_proc'], phases, False),
           ('work', t['work_rad'], work, True),
           ('results', t['ch_res'], results, False)]
    rail = ''.join(f'\n          <li><a href="#ch-{k}"><span class="cn-no">{n:02d}</span> <span class="cn-label">{lab}</span></a></li>' for n, (k, lab, _, _) in enumerate(chs, 1))
    sections = ''.join(f'''

      <section id="ch-{k}" class="chapter{' is-night tone-night' if night else ''}{' chapter--last' if n == len(chs) else ''}" aria-labelledby="ch-{k}-t">
        <div class="wrap">
          {chapter_head(n, lab, f'ch-{k}-t')}
          {html}
        </div>
      </section>''' for n, (k, lab, html, night) in enumerate(chs, 1))
    cover_img = f'<figure class="cover-shot">{pic("rad-brand", "(max-width: 760px) 100vw, 1320px", ra["brand"], eager=True)}</figure>'
    return case_cover(t, h, 'Radio a Domicilio', WAVES, t['r_summary'], (t['r_year_v'], t['r_company'], t['r_art']), cover_img, stage='curtain') + f'''

    <div class="chapters">
      <nav class="chapter-nav" aria-label="{t['chapters_label']}">
        <ol class="wrap">{rail}
        </ol>
      </nav>{sections}
    </div>''' + other_work(t, h, [('invest-in-bogota', 'project--narrow', '(max-width: 760px) 100vw, 42vw'), ('pro-surge-ja', '', '(max-width: 760px) 100vw, 58vw')])


# ---------- Invest in Bogotá: a brand-system showcase, marked by the agency's own red dot (no numbers)
def dot_head(label, hid):
    return f'''<header class="dot-head">
          <div class="sky"><span class="dot-mark" aria-hidden="true"></span><h2 id="{hid}" class="rise chapter-title">{label}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </header>'''


def iib_main(t, h):
    a = t['alts']
    reel = f'''<figure class="cover-shot cover-shot--reel" style="--reel-bg: rgb(235 62 27)">
          <video src="@R/case-studies/invest-in-bogota/presentations/sigo.webm" poster="@A/sigo-poster.jpg" autoplay muted loop playsinline preload="metadata" width="720" height="576" aria-label="{t['c_reel']}"></video>
        </figure>'''
    work = f'''<div class="gallery">
            {fig('iib-web', 'settle', '(max-width: 760px) 100vw, 1320px', a[2])}
            {fig('iib-social-grid', '', '(max-width: 760px) 100vw, 1320px', a[0])}
            <div class="gallery-label"><h3>{t['c_social']}</h3></div>
            {fig('iib-mice', 'g-4', '(max-width: 760px) 100vw, 33vw', a[4])}
            {fig('iib-semana-emprendedor', 'g-4', '(max-width: 760px) 100vw, 33vw', a[1])}
            {fig('iib-convention-bureau', 'g-4', '(max-width: 760px) 100vw, 33vw', a[6])}
            <div class="gallery-label"><h3>{t['c_slides']}</h3></div>
            {fig('iib-slide-aliado', '', '(max-width: 760px) 100vw, 1320px', a[3])}
            {fig('iib-scaleup', 'g-7', '(max-width: 760px) 100vw, 58vw', a[7])}
            {fig('iib-data-slide', 'g-5', '(max-width: 760px) 100vw, 40vw', a[8])}
            {fig('iib-abc-guide', 'g-6', '(max-width: 760px) 100vw, 50vw', a[9])}
            {fig('iib-editorial-spread', 'g-6', '(max-width: 760px) 100vw, 50vw', a[10])}
            {fig('iib-bogota-proposito', 'g-4', '(max-width: 760px) 100vw, 33vw', a[5])}
            <div class="gallery-label"><h3 class="sr-only">Behance</h3>{behance_link(t, 'invest-in-bogota')}</div>
          </div>'''
    return case_cover(t, h, 'Invest in Bogotá', '<span class="sun" aria-hidden="true"></span>', t['c_summary'], (t['c_year_v'], 'Invest in Bogotá', t['r_vai']), reel, sun=True) + f'''

    <section class="statement" aria-label="{t['c_aim_label']}">
      <div class="wrap">
        <p class="statement-text"><span class="dot-mark dot-mark--inline" aria-hidden="true"></span>{t['c_aim']}</p>
      </div>
    </section>

    <section class="case-section" aria-labelledby="iib-challenges">
      <div class="wrap">
        {dot_head(t['c_obj'], 'iib-challenges')}
        {objectives_html(t['c_ch'])}
      </div>
    </section>

    <section class="case-section is-night tone-night" aria-labelledby="iib-work">
      <div class="wrap">
        {dot_head(t['work_iib'], 'iib-work')}
        {work}
      </div>
    </section>''' + other_work(t, h, [('vende-digital', '', '(max-width: 760px) 100vw, 58vw'), ('infinited', 'project--narrow project--square', '(max-width: 760px) 100vw, 42vw')])


def case_rad(lang):
    return case_shell(lang, 'radio-a-domicilio', lambda t: (t['r_title'], t['r_desc']), '#ffc845', '#4a3fc8', rad_main)


def case_iib(lang):
    return case_shell(lang, 'invest-in-bogota', lambda t: (t['c_title'], t['c_desc']), '#ef491f', '#c8361a', iib_main)


# ---------- Shapes for the other covers (geometric, from the logo's vocabulary: dot, line, stem)
SHAPE_VD = '''<svg class="cover-shape links" viewBox="0 0 240 120" aria-hidden="true" focusable="false">
            <path class="link-line" d="M30 106L120 32L210 106"/><circle class="w w1" cx="30" cy="106" r="13"/><circle class="w w2" cx="120" cy="32" r="18"/><circle class="w w3" cx="210" cy="106" r="13"/>
          </svg>'''
SHAPE_INF = '''<svg class="cover-shape stems" viewBox="0 0 240 120" aria-hidden="true" focusable="false">
            <rect class="w w1" x="38" y="72" width="30" height="64" rx="15"/><rect class="w w2" x="105" y="38" width="30" height="98" rx="15"/><rect class="w w3" x="172" y="4" width="30" height="132" rx="15"/>
          </svg>'''
SHAPE_PS = '''<svg class="cover-shape bars" viewBox="0 0 240 120" aria-hidden="true" focusable="false">
            <path class="w w1" d="M54 120L118 0H158L94 120Z"/><path class="w w2" d="M124 120L188 0H228L164 120Z"/>
          </svg>'''
MARK_VD = '<svg class="mark mark--links" viewBox="0 0 40 24" aria-hidden="true" focusable="false"><path d="M6 20L20 6L34 20"/><circle cx="6" cy="20" r="4"/><circle cx="20" cy="6" r="5"/><circle cx="34" cy="20" r="4"/></svg>'
MARK_INF = '<svg class="mark mark--stems" viewBox="0 0 40 24" aria-hidden="true" focusable="false"><rect x="4" y="14" width="7" height="14" rx="3.5"/><rect x="16.5" y="8" width="7" height="20" rx="3.5"/><rect x="29" y="2" width="7" height="26" rx="3.5"/></svg>'
MARK_PS = '<svg class="mark mark--bars" viewBox="0 0 40 24" aria-hidden="true" focusable="false"><path d="M6 24L17 0H24L13 24Z"/><path d="M19 24L30 0H37L26 24Z"/></svg>'


def mark_head(label, hid, mark):
    return f'''<header class="dot-head">
          <div class="sky">{mark}<h2 id="{hid}" class="rise chapter-title">{label}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </header>'''


def section(cls, hid, head, inner):
    return f'''

    <section class="case-section{(" " + cls) if cls else ""}" aria-labelledby="{hid}">
      <div class="wrap">
        {head}
        {inner}
      </div>
    </section>'''


def results_block(t, text, nxt=None, slug=None):
    items = ''.join(f'''
                <li><h4>{hd}</h4><p>{p}</p></li>''' for hd, p in (nxt or []))
    side = f'''
            <div class="next">
              <h3>{t['r_next_label']}</h3>
              <ul>{items}
              </ul>
            </div>''' if nxt else ''
    return f'''<div class="chapter-body grid">
            <p class="results lede{' results--wide' if not nxt else ''}">{text}</p>{side}
          </div>'''


# ---------- Vende Digital: a campaign, "Facts that connect": its points are joined by a line
def vd_main(t, h):
    c = VD[t['_lang']]; a = c['alts']
    connect = '<ol class="connect">' + ''.join(f'''
            <li><span class="connect-dot" aria-hidden="true"></span><p>{x}</p></li>''' for x in c['obj']) + '\n          </ol>'
    work = f'''<div class="gallery">
            {fig('vd-key-visual', 'g-6', '(max-width: 760px) 100vw, 50vw', a['key'])}
            {fig('vd-phone-mockup', 'g-6', '(max-width: 760px) 100vw, 50vw', a['mockup'])}
            {fig('vd-phones', '', '(max-width: 760px) 100vw, 1320px', a['phones'])}
            <div class="gallery-label"><h3>{t['c_social']}</h3></div>
            {fig('vd-post-catalogo', 'g-4', '(max-width: 760px) 100vw, 33vw', a['catalogo'])}
            {fig('vd-post-tiendas', 'g-4', '(max-width: 760px) 100vw, 33vw', a['tiendas'])}
            {fig('vd-post-ventas', 'g-4', '(max-width: 760px) 100vw, 33vw', a['ventas'])}
            {fig('vd-post-vitrina', 'g-6', '(max-width: 760px) 100vw, 50vw', a['vitrina'])}
            {fig('vd-post-empresas', 'g-6', '(max-width: 760px) 100vw, 50vw', a['empresas'])}
            {fig('vd-event', '', '(max-width: 760px) 100vw, 1320px', a['event'])}
          </div>'''
    cover = f'<figure class="cover-shot">{pic("vd-billboard", "(max-width: 760px) 100vw, 1320px", a["billboard"], eager=True)}</figure>'
    return case_cover(t, h, 'Vende Digital', SHAPE_VD, c['desc'], (c['year'], c['company'], t['r_dgd']), cover) + \
        section('', 'vd-obj', mark_head(t['c_obj'], 'vd-obj', MARK_VD), connect) + \
        section('is-night tone-night', 'vd-work', mark_head(c['work'], 'vd-work', MARK_VD), work) + \
        section('case-section--last', 'vd-res', mark_head(t['ch_res'], 'vd-res', MARK_VD), results_block(t, c['results'])) + \
        other_work(t, h, [('infinited', 'project--narrow project--square', '(max-width: 760px) 100vw, 42vw'), ('col40-2018', 'project--narrow project--square', '(max-width: 760px) 100vw, 42vw')])


# ---------- Infinited: learning as a climb; the three phases are steps that rise
def inf_main(t, h):
    c = INF[t['_lang']]; a = c['alts']
    steps = '<ol class="steps">' + ''.join(f'''
            <li class="step">
              <span class="step-stem" aria-hidden="true"></span>
              <h3 class="phase-title">{ph}</h3>''' + ''.join(f'''
              <h4>{ih}</h4>
              <p>{ip}</p>''' for ih, ip in items) + '''
            </li>''' for ph, items in c['phases']) + '\n          </ol>'
    posts = ''.join(fig(f'inf-post-{i}', 'g-3', '(max-width: 760px) 50vw, 25vw', alt) for i, alt in enumerate(a['posts'], 1))
    work = f'''<div class="gallery">
            {fig('inf-overview', '', '(max-width: 760px) 100vw, 1320px', a['overview'])}
            {fig('inf-key-visual', 'g-7', '(max-width: 760px) 100vw, 58vw', a['key'])}
            {fig('inf-logo', 'g-5', '(max-width: 760px) 100vw, 40vw', a['logo'])}
            {fig('inf-escalo', '', '(max-width: 760px) 100vw, 1320px', a['escalo'])}
            <div class="gallery-label"><h3>{t['c_social']}</h3></div>
            {posts}
            {fig('inf-post-crecer', 'g-6', '(max-width: 760px) 100vw, 50vw', a['crecer'])}
            {fig('inf-post-growth', 'g-6', '(max-width: 760px) 100vw, 50vw', a['growth'])}
            {fig('inf-post-legal', 'g-6', '(max-width: 760px) 100vw, 50vw', a['legal'])}
            {fig('inf-computer', 'g-6', '(max-width: 760px) 100vw, 50vw', a['computer'])}
          </div>'''
    cover = f'<figure class="cover-shot">{pic("inf-key-visual", "(max-width: 760px) 100vw, 1320px", a["key"], eager=True)}</figure>'
    return case_cover(t, h, 'Infinited', SHAPE_INF, c['desc'], (c['year'], c['company'], t['r_vec']), cover) + \
        section('', 'inf-proc', mark_head(t['ch_proc'], 'inf-proc', MARK_INF), steps) + \
        section('is-night tone-night', 'inf-work', mark_head(c['work'], 'inf-work', MARK_INF), work) + \
        section('case-section--last', 'inf-res', mark_head(t['ch_res'], 'inf-res', MARK_INF), results_block(t, c['results'])) + \
        other_work(t, h, [('vende-digital', '', '(max-width: 760px) 100vw, 58vw'), ('pro-surge-ja', 'project--narrow', '(max-width: 760px) 100vw, 42vw')])


# ---------- Pro Surge JA: an identity built like its packaging: spec labels, the approach, the reveal, the verdict
def ps_main(t, h):
    c = PS[t['_lang']]; a = c['alts']
    specs = '<ol class="specs">' + ''.join(f'''
            <li class="spec"><h3>{hd}</h3><p>{p}</p></li>''' for hd, p in c['obj']) + '\n          </ol>'
    approach = '<div class="approach">' + ''.join(f'''
            <div class="approach-row">
              <h3 class="phase-title">{ph}</h3>
              <ul>''' + ''.join(f'''
                <li><h4>{ih}</h4><p>{ip}</p></li>''' for ih, ip in items) + '''
              </ul>
            </div>''' for ph, items in c['phases']) + '\n          </div>'
    work = f'''<div class="gallery">
            {fig('ps-logo-red', 'g-6', '(max-width: 760px) 100vw, 50vw', a['logo_red'])}
            {fig('ps-logo-navy', 'g-6', '(max-width: 760px) 100vw, 50vw', a['logo_navy'])}
            {fig('ps-box-surge', 'g-6', '(max-width: 760px) 100vw, 50vw', a['box_surge'])}
            {fig('ps-box-fridge', 'g-6', '(max-width: 760px) 100vw, 50vw', a['box_fridge'])}
            {fig('ps-billboard', '', '(max-width: 760px) 100vw, 1320px', a['billboard'])}
            <div class="gallery-label"><h3>{t['c_social']}</h3></div>
            {fig('ps-post-surge', 'g-4', '(max-width: 760px) 100vw, 33vw', a['post_surge'])}
            {fig('ps-post-fridge', 'g-4', '(max-width: 760px) 100vw, 33vw', a['post_fridge'])}
            {fig('ps-post-monitor', 'g-4', '(max-width: 760px) 100vw, 33vw', a['post_monitor'])}
          </div>'''
    concl = f'''<p class="statement-text">{c['conclusions']}</p>'''
    cover = f'<figure class="cover-shot">{pic("ps-overview", "(max-width: 760px) 100vw, 1320px", a["overview"], eager=True)}</figure>'
    return case_cover(t, h, 'Pro Surge JA', SHAPE_PS, c['desc'], (c['year'], c['company'], t['r_ad']), cover) + \
        section('', 'ps-obj', mark_head(t['c_obj'], 'ps-obj', MARK_PS), specs) + \
        section('', 'ps-app', mark_head(c['approach'], 'ps-app', MARK_PS), approach) + \
        section('is-night tone-night', 'ps-work', mark_head(c['work'], 'ps-work', MARK_PS), work) + \
        section('', 'ps-res', mark_head(t['ch_res'], 'ps-res', MARK_PS), results_block(t, c['results'], c['next'])) + \
        section('case-section--last', 'ps-concl', mark_head(c['conclusions_label'], 'ps-concl', MARK_PS), concl) + \
        other_work(t, h, [('vende-digital', '', '(max-width: 760px) 100vw, 58vw'), ('infinited', 'project--narrow project--square', '(max-width: 760px) 100vw, 42vw')])


def case_vd(lang):
    return case_shell(lang, 'vende-digital', lambda t: (VD[lang]['title'], VD[lang]['meta']), '#ff00bc', '#2836d9', vd_main)


def case_inf(lang):
    return case_shell(lang, 'infinited', lambda t: (INF[lang]['title'], INF[lang]['meta']), '#2ccfc7', '#0b6f7a', inf_main)


def case_ps(lang):
    return case_shell(lang, 'pro-surge-ja', lambda t: (PS[lang]['title'], PS[lang]['meta']), '#ff4848', '#b3121b', ps_main)


# ------------------------------------------------------------------ 404 (one file, both languages)
def lost():
    en = T['en']
    body = header(en, '@H/', '@H/es/') + sheet(en) + f'''

  <main class="lost">
    <div class="wrap">
      <h1 class="sr-only">404</h1>
      <!-- GIF aleatorio de gatos dentro del sol: clave GIPHY del dueño del sitio, cambia en cada recarga -->
      <div class="sky" aria-hidden="true" data-giphy-key="DPRlJyFbg3L9PxY5AEqfssUoabElSV2k" data-giphy-tag="cat"><span class="sun"></span><span class="rise lost-code">404</span></div>
      <span class="horizon horizon--sun" aria-hidden="true"></span>
      <div class="lost-body" data-lang-block="en">
        <p>The page you’re looking for doesn’t exist or has moved. Head back to the home page.</p>
        <a class="btn btn--sun btn--lg" href="@H/">{ic('i-back')} Back to home</a>
        <a class="giphy-credit" href="https://giphy.com" target="_blank" rel="noopener" data-giphy-credit hidden>Powered by GIPHY</a>
      </div>
      <div class="lost-body" data-lang-block="es" lang="es" hidden>
        {ES_DRAFT}
        <p>La página que buscas no existe o cambió de lugar. Vuelve al inicio.</p>
        <a class="btn btn--sun btn--lg" href="@H/es/">{ic('i-back')} Volver al inicio</a>
      </div>
    </div>
  </main>
  <script>
    /* One 404 for both languages: show Spanish when the browser prefers it. Same URL, no redirect. */
    (function () {{
      var prefs = (navigator.languages || [navigator.language || ""]).map(function (l) {{ return String(l).slice(0, 2).toLowerCase(); }});
      var saved = null; try {{ saved = localStorage.getItem("nmb-lang"); }} catch (e) {{}}
      if ((saved || prefs[0]) === "es") {{
        document.documentElement.lang = "es";
        document.querySelector('[data-lang-block="en"]').hidden = true;
        document.querySelector('[data-lang-block="es"]').hidden = false;
      }}
    }})();
  </script>
'''
    alts = [('en', BASE + '404.html'), ('x-default', BASE + '404.html')]
    return page('en', 0, body, 'Nicolas MB - Designer', en['desc'], alts, robots='noindex', absolute=True)


# ------------------------------------------------------------------ write
def write(rel, html):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)


write('index.html', home('en'))
write('es/index.html', home('es'))
write('invest-in-bogota/index.html', case_iib('en'))
write('es/invest-in-bogota/index.html', case_iib('es'))
write('radio-a-domicilio/index.html', case_rad('en'))
write('es/radio-a-domicilio/index.html', case_rad('es'))
for slug, fn in (('vende-digital', case_vd), ('infinited', case_inf), ('pro-surge-ja', case_ps)):
    write(f'{slug}/index.html', fn('en'))
    write(f'es/{slug}/index.html', fn('es'))
write('projects-a/index.html', home('en', 'plates'))
write('projects-b/index.html', home('en', 'sheet'))
write('projects-c/index.html', home('en', 'tiles'))
write('404.html', lost())
print('built', ASSET_V, sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*.html')))
