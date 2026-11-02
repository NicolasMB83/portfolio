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
import re, json, hashlib, pathlib

HERE = pathlib.Path(__file__).resolve().parent
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


LOGO = (PARTS / 'frag-logo.svg').read_text().strip()
LOGO_SYMBOL = '<symbol id="logo-shape" viewBox="0 0 119.912 22">' + re.search(r'<svg[^>]*>(.*)</svg>', LOGO, re.S).group(1) + '</symbol>'
LOGO_PROSURGE = (PARTS / 'frag-prosurge.svg').read_text().strip()
LOGO_IIB = (PARTS / 'frag-iib.svg').read_text().strip()
FILM_BURN = (PARTS / 'film-burn.svg').read_text().strip()
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
  intro="I'm Nicolás, a multidisciplinary designer with experience in Product and Digital Design, creating campaigns on social media.",
  work='WORK', view='VIEW PORTFOLIO',
  r_art='Art Director', r_vai='Visual and AI Designer', r_dgd='Digital Graphic Designer', r_vec='Visual Experience Coordinator', r_ad='Art Direction',
  s1='Digital Graphic Design', s1t='Developing design concepts that encompass visual identity, color palettes, typography, and visual guidelines.',
  s2='Web Design', s2t='Navigation structure strategies, visual design, mobile device optimization, and style guides.',
  s3='UI Design', s3t='I enhance the user experience with intuitive interface designs for web and mobile applications.',
  s4='Brand Identity', s4t='Creating brand strategies, including logo design, color schemes, typography, and guidelines.',
  clients='Organizations that trust my work', career='Career path',
  roles=[
   ('Jan 2026 - Current', 'Graphic Designer, Creative', 'ReloQuest', [
      'Redesigned the interface of ReloQuest’s main website.',
      'Produce brand videos and now integrate AI video tools into the production workflow.',
      'Design social media graphics as well as digital and print collateral.',
      'Create print pieces such as backdrops, and mock-ups that present each design in context.'], 'ReloQuest: viñetas aprobadas salvo revisión final'),
   ('Feb 2025 - Jan 2026', 'Visual and AI Designer', 'Invest in Bogotá', [
      'Design of graphic assets for national and international investment promotion events.',
      'Creation of visual assets for social media campaigns, aimed at informing, promoting and attracting investors to Bogotá, the capital of Colombia.',
      'Implemented AI to support design workflow across the Design department.'], None),
   ('Jan 2023 - Sept 2024', 'Art Director', 'Ondas y Ecos S.A.S.', [
      'Redesigned the company’s visual identity across digital platforms.',
      'Implemented design strategies for web and social media.',
      'Directed the narrative of the brand Radio a Domicilio. Closeness and familiarity.'], None),
   ('Nov 2021 - Nov 2022', 'Visual Experience Coordinator', 'Infinited - Area Andina University', [
      'Led cross-functional collaboration between the marketing, design and development teams to deliver campaigns aligned with the university goals.',
      'Created interactive content aligned with brand identity, leading to further improvement and organic evolution of the brand.',
      'UI prototyping and deployment optimized for the sales funnel.'], None),
   ('Jun 2017 - Aug 2022', 'Digital Graphic Designer', 'Colombian Ministry of ICT (MINTIC)', [
      'Created a wide range of graphic assets for government campaigns, including presentations (PPT/keynote), social media content, email campaigns, infographics, print materials, custom signage, branded furnishings and other specialty formats.',
      'Translated complex research and economic data into accessible visual materials, backed by international partnerships.',
      'Contributed to strategic planning sessions of the Digital Transformation and Economy departments.'], None),
  ],
  magic="Let's make magic!", magic_sub='Working together to achieve greatness', cv='Download CV',
  copy='Copy', copied='Copied', copy_aria='Copy email address', close='Close',
  made='Created with passion, love, and design', rights='© 2026 Nicolás Mogollón Barbosa',
  # case study: Invest in Bogotá
  c_title='Invest in Bogotá - Nicolas MB', c_desc='Invest in Bogotá: visual and AI design for the investment promotion agency of Bogotá.',
  c_summary='The investment promotion agency for Bogotá&nbsp;– Region.',
  c_year='YEAR', c_ind='INDUSTRY', c_srv='SERVICES', c_year_v='Feb 2025 - Jan 2026', c_ind_v='Investment',
  c_reel='SIGO presentation opener: Una idea que nace en Bogotá',
  c_obj='Objectives - Challenges',
  c_ch=[('A brand to develop', 'IBB has a new rebranding, making this the perfect environment to develop the brand, through creative implementations in printed, web, and social media assets the challenge is to preserve its brand while developing new ways to communicate'),
        ('Keep sharp graphics', "The biggest challenge is to keep the brand relevant, by researching every day about current trends and styles I'm able to keep the brand cohesion while creating content for web, digital and printed media."),
        ('Keep evolving', 'Integrate AI tools into the mix in order to reduce times in production and/or develop products that demand speed, complexity and quality')],
  c_social='Social Media', c_slides='Slides', c_other='Other work',
  alts=['Four social media pieces about Bogotá procurement rules, in red, blue and violet', 'Semana del Emprendedor poster with a Bogotá skyline photo',
        'Invest in Bogotá website pages for events and business guides', 'Presentation slide: Su mejor aliado estratégico',
        'MICE tourism post: En Bogotá, cada evento es una oportunidad', 'Post: Bogotá se vive con propósito, over the Santamaría bullring at night',
        'Convention Bureau call for unique tourism experiences, yellow isometric map', 'ScaleUpBog presentation slide',
        'Economic data slide comparing Colombia with Latin American markets', 'ABC Works for Taxes guide cover on a red circle',
        'Editorial spread with Bogotá cathedral and red circle device'],
  # case study: Radio a Domicilio (content from the site's CMS; chapter labels are proposals)
  r_title='Radio a Domicilio - Nicolas MB',
  r_desc='Radio a Domicilio: art direction for a radio brand, its website, campaigns and social media.',
  r_summary='Under the slogan “Radio at Home,” we seek to create an authentic and welcoming experience',
  r_ind_v='Communications', r_year_v='2023-2024',
  chapters_label='Chapters',
  ch=['Context', 'Objectives', 'Process', 'The work', 'Results'],
  r_obj=[('Modern essence', 'Achieving a balance between an iconic identity and a modern touch that attracts new audiences.'),
         ('Multichannel consistency', 'Designing a visual identity that is adaptable and coherent across all channels.'),
         ('Visual engagement', 'Create striking graphics that capture attention and retain users on social media.')],
  r_phases=[('Discovery Phase', [('Market and Style Study', 'Thoroughly research audience preferences to create an aesthetic that reinvents the legacy of Radio a Domicilio and attracts new listeners.')]),
            ('Design and Development', [('UI/UX Design', 'I designed a clean, intuitive interface with streamlined navigation and engaging visuals to motivate users'),
                                        ('Audience and Style Analysis', 'Examine audience preferences to define the aesthetic of Radio a Domicilio and attract new listeners.')]),
            ('Testing and Iteration', [('User Testing', 'Initial testing of a controlled group of users to obtain feedback about the web interface, its use, and future implementations before launch'),
                                       ('Web Optimization', 'Implemented optimizations in the user interface to enhance the navigation experience of the website on computers and mobile devices.')])],
  r_results='“Radio a Domicilio” received positive feedback and an exceptional reception in the company. Metrics such as audience retention and participation exceeded expectations in the first three months, driven by an intuitive design and a content offering that connected with listeners of all ages.',
  r_next_label='Next steps',
  r_next=[('Continuous Improvements', 'Planning regular updates based on audience feedback and industry trends, always seeking to enhance functionality and listener satisfaction.'),
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
  intro='Soy Nicolás, diseñador multidisciplinario con experiencia en diseño de producto y diseño digital, creando campañas para redes sociales.',
  work='PROYECTOS', view='VER PORTAFOLIO',
  r_art='Director de arte', r_vai='Diseñador visual y de IA', r_dgd='Diseñador gráfico digital', r_vec='Coordinador de experiencia visual', r_ad='Dirección de arte',
  s1='Diseño gráfico digital', s1t='Desarrollo de conceptos de diseño que abarcan identidad visual, paletas de color, tipografía y lineamientos visuales.',
  s2='Diseño web', s2t='Estrategias de estructura de navegación, diseño visual, optimización para dispositivos móviles y guías de estilo.',
  s3='Diseño UI', s3t='Mejoro la experiencia de usuario con diseños de interfaz intuitivos para aplicaciones web y móviles.',
  s4='Identidad de marca', s4t='Creación de estrategias de marca, que incluyen diseño de logotipo, esquemas de color, tipografía y lineamientos.',
  clients='Organizaciones que confían en mi trabajo', career='Trayectoria',
  roles=[
   ('Ene 2026 - Actual', 'Diseñador gráfico, creativo', 'ReloQuest', [
      'Rediseñé la interfaz del sitio web principal de ReloQuest.',
      'Produzco videos de marca y ahora integro herramientas de video con IA en el flujo de producción.',
      'Diseño piezas gráficas para redes sociales, así como material publicitario digital e impreso.',
      'Creo piezas impresas como backdrops, y mock-ups que presentan cada diseño en contexto.'], 'ReloQuest: viñetas aprobadas salvo revisión final'),
   ('Feb 2025 - Ene 2026', 'Diseñador visual y de IA', 'Invest in Bogotá', [
      'Diseño de piezas gráficas para eventos nacionales e internacionales de promoción de inversión.',
      'Creación de piezas visuales para campañas en redes sociales, orientadas a informar, promover y atraer inversionistas a Bogotá, la capital de Colombia.',
      'Implementé IA para apoyar el flujo de trabajo de diseño en todo el departamento de Diseño.'], None),
   ('Ene 2023 - Sept 2024', 'Director de arte', 'Ondas y Ecos S.A.S.', [
      'Rediseñé la identidad visual de la empresa en sus plataformas digitales.',
      'Implementé estrategias de diseño para web y redes sociales.',
      'Dirigí la narrativa de la marca Radio a Domicilio. Cercanía y familiaridad.'], None),
   ('Nov 2021 - Nov 2022', 'Coordinador de experiencia visual', 'Infinited - Universidad del Área Andina', [
      'Lideré la colaboración interdisciplinaria entre los equipos de mercadeo, diseño y desarrollo para entregar campañas alineadas con los objetivos de la universidad.',
      'Creé contenido interactivo alineado con la identidad de marca, lo que llevó a una mayor mejora y a la evolución orgánica de la marca.',
      'Prototipado y despliegue de UI optimizados para el embudo de ventas.'], None),
   ('Jun 2017 - Ago 2022', 'Diseñador gráfico digital', 'Ministerio TIC de Colombia (MINTIC)', [
      'Creé una amplia gama de piezas gráficas para campañas del gobierno, incluyendo presentaciones (PPT/keynote), contenido para redes sociales, campañas de email, infografías, material impreso, señalética personalizada, mobiliario de marca y otros formatos especiales.',
      'Traduje investigaciones complejas y datos económicos en materiales visuales accesibles, respaldados por alianzas internacionales.',
      'Contribuí a las sesiones de planeación estratégica de los departamentos de Transformación Digital y Economía.'], None),
  ],
  magic='¡Hagamos magia!', magic_sub='Trabajando juntos para lograr grandes cosas', cv='Descargar CV',
  copy='Copiar', copied='Copiado', copy_aria='Copiar correo', close='Cerrar',
  made='Creado con pasión, amor y diseño', rights='© 2026 Nicolás Mogollón Barbosa',
  c_title='Invest in Bogotá - Nicolas MB', c_desc='Invest in Bogotá: diseño visual y con IA para la agencia de promoción de inversión de Bogotá.',
  c_summary='La agencia de promoción de inversión de Bogotá&nbsp;– Región.',
  c_year='AÑO', c_ind='INDUSTRIA', c_srv='SERVICIOS', c_year_v='Feb 2025 - Ene 2026', c_ind_v='Inversión',
  c_reel='Apertura de la presentación de SIGO: Una idea que nace en Bogotá',
  c_obj='Objetivos - Retos',
  c_ch=[('Una marca por desarrollar', 'IBB tiene un nuevo rebranding, lo que hace de este el entorno perfecto para desarrollar la marca; a través de implementaciones creativas en piezas impresas, web y de redes sociales, el reto es preservar su marca mientras se desarrollan nuevas formas de comunicar'),
        ('Mantener gráficas impecables', 'El mayor reto es mantener la marca vigente; investigando cada día sobre tendencias y estilos actuales, logro mantener la cohesión de la marca mientras creo contenido para medios web, digitales e impresos.'),
        ('Seguir evolucionando', 'Integrar herramientas de IA al proceso para reducir los tiempos de producción y/o desarrollar productos que exigen velocidad, complejidad y calidad')],
  c_social='Redes sociales', c_slides='Diapositivas', c_other='Otros proyectos',
  alts=['Cuatro piezas para redes sociales sobre las reglas de contratación de Bogotá, en rojo, azul y violeta', 'Afiche de la Semana del Emprendedor con el skyline de Bogotá',
        'Páginas del sitio web de Invest in Bogotá para eventos y guías de negocios', 'Diapositiva: Su mejor aliado estratégico',
        'Post de turismo MICE: En Bogotá, cada evento es una oportunidad', 'Post: Bogotá se vive con propósito, sobre la plaza de toros La Santamaría de noche',
        'Convocatoria del Convention Bureau para experiencias turísticas únicas, mapa isométrico amarillo', 'Diapositiva de la presentación de ScaleUpBog',
        'Diapositiva con datos económicos que compara a Colombia con mercados latinoamericanos', 'Portada de la guía ABC Obras por Impuestos sobre un círculo rojo',
        'Doble página editorial con la catedral de Bogotá y el círculo rojo'],
  r_title='Radio a Domicilio - Nicolas MB',
  r_desc='Radio a Domicilio: dirección de arte para una marca de radio, su sitio web, campañas y redes sociales.',
  r_summary='Bajo el lema “Radio a Domicilio”, buscamos crear una experiencia auténtica y acogedora',
  r_ind_v='Comunicaciones', r_year_v='2023-2024',
  chapters_label='Capítulos',
  ch=['Contexto', 'Objetivos', 'Proceso', 'Las piezas', 'Resultados'],
  r_obj=[('Esencia moderna', 'Lograr un equilibrio entre una identidad icónica y un toque moderno que atraiga nuevas audiencias.'),
         ('Coherencia multicanal', 'Diseñar una identidad visual adaptable y coherente en todos los canales.'),
         ('Conexión visual', 'Crear gráficas llamativas que capten la atención y retengan a los usuarios en redes sociales.')],
  r_phases=[('Fase de descubrimiento', [('Estudio de mercado y estilo', 'Investigar a fondo las preferencias de la audiencia para crear una estética que reinvente el legado de Radio a Domicilio y atraiga nuevos oyentes.')]),
            ('Diseño y desarrollo', [('Diseño UI/UX', 'Diseñé una interfaz limpia e intuitiva, con una navegación simplificada y visuales atractivos para motivar a los usuarios'),
                                     ('Análisis de audiencia y estilo', 'Examinar las preferencias de la audiencia para definir la estética de Radio a Domicilio y atraer nuevos oyentes.')]),
            ('Pruebas e iteración', [('Pruebas con usuarios', 'Pruebas iniciales con un grupo controlado de usuarios para obtener retroalimentación sobre la interfaz web, su uso y futuras implementaciones antes del lanzamiento'),
                                     ('Optimización web', 'Implementé optimizaciones en la interfaz de usuario para mejorar la experiencia de navegación del sitio web en computadores y dispositivos móviles.')])],
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
    dict(slug='vende-digital', title='Vende Digital', role='r_dgd', lottie='opJXddsePYvkvZBgp7zGeH5vII8', poster=None, client='oklch(0.8 0.035 278)', shape='wide'),
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
  <link rel="preload" as="font" type="font/woff2" crossorigin href="@A/fonts/clash-display-600.woff2">
  <link rel="preload" as="font" type="font/woff2" crossorigin href="@A/fonts/dm-sans-latin.woff2">
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
      <a class="brand" href="{home}" aria-label="Nicolas MB">{LOGO}</a>
      <nav class="nav" aria-label="Primary">
        <ul class="nav-links">
          <li><a href="{home}#work">{t['nav_work']}</a></li>
          <li><a href="{home}#about">{t['nav_about']}</a></li>
          <li><a href="{home}#experience">{t['nav_exp']}</a></li>
        </ul>
        {lang_link(t, other)}
        <a class="btn btn--sun" href="{home}#contact" data-contact>{t['cta']} {ic('i-go', 'icon--go')}</a>
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
    <a class="btn btn--sun btn--lg" href="{home}#contact" data-contact>{t['cta']} {ic('i-go', 'icon--go')}</a>
  </div>'''


def hint(t, other):
    return f'''
  <div class="lang-hint" lang="{t['other_lang']}" data-lang-hint="{t['other_lang']}" role="region" aria-label="{t['other_name']}" hidden>
    {P.format('sugerencia de idioma (texto nuevo)')}
    <span>{t['hint_text']}</span>
    <a class="btn btn--sun" href="{other}" hreflang="{t['other_lang']}" data-lang-switch>{t['hint_btn']}</a>
    <button class="x" type="button" data-dismiss aria-label="{t['hint_close']}">{ic('i-close')}</button>
  </div>'''


def email_row(t):
    return f'''<div class="email-row">
          {P.format('dirección visible + Copy/Copied (aprobado)')}
          <span class="email-address">{EMAIL}</span>
          <button class="btn copy-btn" type="button" data-copy="{EMAIL}" aria-label="{t['copy_aria']}">
            <span class="when-idle">{ic('i-copy')} {t['copy']}</span>
            <span class="when-done">{ic('i-check')} {t['copied']}</span>
          </button>
          <span class="sr-only" role="status" data-copy-status></span>
        </div>'''


def socials():
    return f'''<ul class="socials">
          <li><a href="https://www.linkedin.com/in/nicolasmb" target="_blank" rel="noopener" aria-label="LinkedIn">{ic('i-linkedin')}</a></li>
          <li><a href="https://www.behance.net/NicolasMB" target="_blank" rel="noopener" aria-label="Behance">{ic('i-behance')}</a></li>
          <li><a href="mailto:{EMAIL}" aria-label="Email">{ic('i-mail')}</a></li>
        </ul>'''


def sheet(t):
    return f'''
  <dialog id="contact-sheet" class="sheet" aria-labelledby="sheet-title">
    <div class="sheet-inner">
      <button class="sheet-close" type="button" data-close aria-label="{t['close']}">{ic('i-close')}</button>
      <div class="sky"><span class="sun" aria-hidden="true"></span><h2 id="sheet-title" class="rise sheet-title">{t['magic']}</h2></div>
      <span class="horizon horizon--night" style="margin-inline:0" aria-hidden="true"></span>
      <p class="contact-sub">{t['magic_sub']}</p>
      {email_row(t)}
      <div class="sheet-actions">
        <a class="btn btn--sun btn--lg" href="mailto:{EMAIL}">{t['cta']} {ic('i-go', 'icon--go')}</a>
        <a class="btn btn--line btn--lg" href="{CV}" target="_blank" rel="noopener">{t['cv']} {ic('i-download')}</a>
      </div>
      {socials()}
    </div>
  </dialog>'''


def footer(t, other):
    return f'''
  <footer id="contact" class="contact is-night">
    {FILM_BURN}
    <div class="wrap">
      <div class="sky"><h2 class="rise contact-title">{t['magic']}</h2></div>
      <span class="horizon" aria-hidden="true"></span>
      <p class="contact-sub">{t['magic_sub']}</p>
      {email_row(t)}
      <div class="contact-actions">
        <div class="cta-group">
          <a class="btn btn--sun btn--lg" href="mailto:{EMAIL}">{t['cta']} {ic('i-go', 'icon--go')}</a>
          <a class="btn btn--line btn--lg" href="{CV}" target="_blank" rel="noopener">{t['cv']} {ic('i-download')}</a>
        </div>
        {socials()}
      </div>
      <div class="footer-bar">
        <p>{t['made']} <span class="heart">♥</span></p>
        <div class="footer-end">
          {lang_link(t, other, full=True)}
          <a href="https://www.be.net/nicolasmb">{t['rights']}</a>
        </div>
      </div>
    </div>
    <div class="film-end" aria-hidden="true">
      <div class="film-logo">
        <svg class="fl fl-r" viewBox="0 0 119.912 22" focusable="false"><use href="#logo-shape"/></svg>
        <svg class="fl fl-g" viewBox="0 0 119.912 22" focusable="false"><use href="#logo-shape"/></svg>
        <svg class="fl fl-y" viewBox="0 0 119.912 22" focusable="false"><use href="#logo-shape"/></svg>
        <svg class="fl fl-core" viewBox="0 0 119.912 22" focusable="false"><use href="#logo-shape"/></svg>
      </div>
    </div>
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
              <div class="project-media"{attrs}>{media}<span class="dawn" aria-hidden="true">{ic('i-go')}</span></div>
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
              <div class="project-media tile-media"{attrs}>{media}<span class="dawn" aria-hidden="true">{ic('i-go')}</span></div>
              <span class="tile-line" aria-hidden="true"></span>
              <div class="project-meta tile-meta">
                <h3 class="project-title">{p['title']}</h3>
                <p class="project-role">{t[p['role']]}</p>
              </div>
            </a>
          </li>''')
    return '<ul class="tiles">' + ''.join(out) + '\n        </ul>'


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
        <h1 class="hero-title display-1">
          <span class="sky"><span class="sun" aria-hidden="true"></span><span class="rise">{t['h1a']}</span></span>
          <span class="horizon" aria-hidden="true"></span>
          <span class="below lede"><span>{t['h1b']}</span></span>
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
          {ic('i-go')}
        </a>
      </div>
    </section>

    <section id="about" class="about">
      <div class="wrap">
        <ul class="services">''' + ''.join(f'''
          <li class="service">
            <h3 class="service-title">{t[k]}</h3>
            <p class="service-text">{t[k + 't']}</p>
            <div class="service-plate"><img src="@A/img/{f}.svg" width="{w}" height="{hh}" alt="" loading="lazy" decoding="async"></div>
          </li>''' for k, f, w, hh in [('s1', 'service-graphic', 1024, 1024), ('s2', 'service-web', 797, 813), ('s3', 'service-ui', 1024, 1024), ('s4', 'service-brand', 1024, 1024)]) + f'''
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


# ------------------------------------------------------------------ CASE STUDY: Invest in Bogotá (gallery template)
def case(lang):
    t = T[lang]
    depth = 1 if lang == 'en' else 2
    h = '@H/' if lang == 'en' else '@H/es/'
    other = '@H/es/invest-in-bogota/' if lang == 'en' else '@H/invest-in-bogota/'
    a = t['alts']

    def fig(name, cls, sizes, alt):
        return f'<figure class="{cls}">{pic(name, sizes, alt)}</figure>'
    ch = ''.join(f'\n          <li><strong>{hd}</strong><p>{p}</p></li>' for hd, p in t['c_ch'])
    note = ES_DRAFT if lang == 'es' else ''
    body = hint(t, other) + header(t, h, other) + sheet(t) + f'''

  <main>{note}
    <section class="case-hero" style="--client: #EF491F">
      <div class="wrap">
        <a class="back-link" href="{h}#work">{ic('i-back')} {t['work']}</a>
        <h1 class="title-lg">
          <span class="sky"><span class="sun" aria-hidden="true"></span><span class="rise">Invest in Bogotá</span></span>
        </h1>
        <span class="horizon" aria-hidden="true"></span>
        <p class="case-summary lede">{t['c_summary']}</p>
        <dl class="facts">
          <div><dt>{t['c_year']}</dt><dd>{t['c_year_v']}</dd></div>
          <div><dt>{t['c_ind']}</dt><dd>{t['c_ind_v']}</dd></div>
          <div><dt>{t['c_srv']}</dt><dd>{t['r_vai']}</dd></div>
        </dl>
      </div>
      <div class="reel" style="--reel-bg: rgb(235 62 27)">
        <video src="@R/case-studies/invest-in-bogota/presentations/sigo.webm" poster="@A/sigo-poster.jpg" autoplay muted loop playsinline preload="metadata" width="720" height="576" aria-label="{t['c_reel']}"></video>
      </div>
    </section>
    {P.format('punto 9 en espera: el resumen del CMS no se muestra hasta que decidas')}

    <section class="case-block" aria-labelledby="challenges-title">
      <div class="wrap grid">
        <div class="case-block-head"><h2 id="challenges-title">{t['c_obj']}</h2></div>
        <ul class="case-block-body challenges">{ch}
        </ul>
      </div>
    </section>

    <section class="case-block" aria-label="{t['work']}">
      <div class="wrap">
        <div class="gallery">
          {fig('iib-social-grid', '', '(max-width: 760px) 100vw, 1320px', a[0])}
          {fig('iib-semana-emprendedor', 'g-5', '(max-width: 760px) 100vw, 40vw', a[1])}
          {fig('iib-web', 'g-7', '(max-width: 760px) 100vw, 58vw', a[2])}
          {fig('iib-slide-aliado', '', '(max-width: 760px) 100vw, 1320px', a[3])}

          <div class="gallery-label"><h2>{t['c_social']}</h2></div>
          {fig('iib-mice', 'g-4', '(max-width: 760px) 100vw, 33vw', a[4])}
          {fig('iib-bogota-proposito', 'g-4', '(max-width: 760px) 100vw, 33vw', a[5])}
          {fig('iib-convention-bureau', 'g-4', '(max-width: 760px) 100vw, 33vw', a[6])}

          <div class="gallery-label"><h2>{t['c_slides']}</h2></div>
          {fig('iib-scaleup', 'g-7', '(max-width: 760px) 100vw, 58vw', a[7])}
          {fig('iib-data-slide', 'g-5', '(max-width: 760px) 100vw, 40vw', a[8])}
          {fig('iib-abc-guide', 'g-6', '(max-width: 760px) 100vw, 50vw', a[9])}
          {fig('iib-editorial-spread', 'g-6', '(max-width: 760px) 100vw, 50vw', a[10])}

          <div class="gallery-label">
            <h2 class="sr-only">Behance</h2>
            <a class="behance-link" href="https://www.behance.net/gallery/230400817/Invest-in-Bogota" target="_blank" rel="noopener">{ic('i-behance')} Behance {ic('i-go', 'icon--go')}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="other-work is-night" aria-labelledby="other-title">
      <div class="wrap">
        <div class="titled">
          <div class="sky"><h2 id="other-title" class="rise display-2" style="padding-bottom:.16em">{t['c_other']}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </div>
        <ul class="grid projects">''' + \
        project(t, h, 'vende-digital') + \
        project(t, h, 'infinited', 'project--narrow project--square', '(max-width: 760px) 100vw, 42vw') + '''
        </ul>
      </div>
    </section>
  </main>
''' + footer(t, other)
    alts = [('en', BASE + 'invest-in-bogota/'), ('es', BASE + 'es/invest-in-bogota/'), ('x-default', BASE + 'invest-in-bogota/')]
    return page(lang, depth, body, t['c_title'], t['c_desc'], alts, 'page-night')


# ------------------------------------------------------------------ CASE STUDY: Radio a Domicilio (chapter template)
WAVES = '''<svg class="waves" viewBox="0 0 240 120" aria-hidden="true" focusable="false">
            <path class="w w1" d="M96 120a24 24 0 0 1 48 0"/>
            <path class="w w2" d="M66 120a54 54 0 0 1 108 0"/>
            <path class="w w3" d="M36 120a84 84 0 0 1 168 0"/>
            <path class="w w4" d="M6 120a114 114 0 0 1 228 0"/>
          </svg>'''
BANNERS = [('300x600', 300, 600), ('160x600', 160, 600), ('300x250', 300, 250), ('320x50', 320, 50), ('930x180', 930, 180)]


def chapter_head(n, label, hid):
    return f'''<header class="chapter-head">
          <div class="sky"><span class="rise chapter-no" aria-hidden="true">{n:02d}</span><h2 id="{hid}" class="rise chapter-title"><span class="sr-only">{n:02d}. </span>{label}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </header>'''


def case_chapters(lang):
    t = T[lang]
    depth = 1 if lang == 'en' else 2
    h = '@H/' if lang == 'en' else '@H/es/'
    other = '@H/es/radio-a-domicilio/' if lang == 'en' else '@H/radio-a-domicilio/'
    ch, ra = t['ch'], t['r_alts']
    ids = ['ch-context', 'ch-objectives', 'ch-process', 'ch-work', 'ch-results']
    note = ES_DRAFT if lang == 'es' else ''
    rail = ''.join(f'\n          <li><a href="#{i}"><span class="cn-no">{n:02d}</span> <span class="cn-label">{lab}</span></a></li>' for n, (i, lab) in enumerate(zip(ids, ch), 1))
    objectives = ''.join(f'''
            <li class="objective"><h3>{hd}</h3><p>{p}</p></li>''' for hd, p in t['r_obj'])
    phases = ''.join(f'''
            <li class="phase">
              <span class="phase-dot" aria-hidden="true"></span>
              <h3 class="phase-title">{ph}</h3>''' + ''.join(f'''
              <h4>{ih}</h4>
              <p>{ip}</p>''' for ih, ip in items) + '''
            </li>''' for ph, items in t['r_phases'])
    nxt = ''.join(f'''
              <li><h4>{hd}</h4><p>{p}</p></li>''' for hd, p in t['r_next'])
    banners = ''.join(f'''
              <figure class="banner banner--{k}" style="--bw: {w}; --bh: {hh}">
                <iframe src="@R/ads/rad/{k}/index.html" width="{w}" height="{hh}" title="{t['r_banner']} {w}×{hh}" loading="lazy" sandbox="allow-scripts" scrolling="no"></iframe>
                <figcaption>{w} × {hh}</figcaption>
              </figure>''' for k, w, hh in BANNERS)
    body = hint(t, other) + header(t, h, other) + sheet(t) + f'''

  <main style="--client: #ffc845; --client-ink: #4a3fc8">{note}
    <!-- PLANTILLA DE CAPÍTULOS (ejemplo). Portada tipo deck + capítulos que se abren sobre el horizonte.
         Contenido: CMS del sitio. Textos nuevos marcados como PROPUESTA DE TEXTO. -->
    <section class="case-hero chapter-cover is-night tone-night">
      <div class="wrap">
        <a class="back-link" href="{h}#work">{ic('i-back')} {t['work']}</a>
        <h1 class="title-lg">
          <span class="sky">{WAVES}<span class="rise">Radio a Domicilio</span></span>
        </h1>
        <span class="horizon" aria-hidden="true"></span>
        <dl class="facts">
          <div><dt>{t['c_year']}</dt><dd>{t['r_year_v']}</dd></div>
          <div><dt>{t['c_ind']}</dt><dd>{t['r_ind_v']}</dd></div>
          <div><dt>{t['c_srv']}</dt><dd>{t['r_art']}</dd></div>
        </dl>
      </div>
      <figure class="cover-shot">{pic('rad-campaign', '100vw', ra['campaign'], eager=True)}</figure>
    </section>

    <div class="chapters">
      <nav class="chapter-nav" aria-label="{t['chapters_label']}">
        {P.format('nombres de capítulo: Context y The work son nuevos; Objectives, Process, Results y Next steps vienen del CMS')}
        <ol class="wrap">{rail}
        </ol>
      </nav>

      <section id="{ids[0]}" class="chapter" aria-labelledby="{ids[0]}-t">
        <div class="wrap">
          {chapter_head(1, ch[0], ids[0] + '-t')}
          <div class="chapter-body grid">
            <p class="chapter-lede lede">{t['r_summary']}</p>
            <figure class="chapter-figure">{pic('rad-studio', '(max-width: 760px) 100vw, 50vw', ra['studio'])}</figure>
          </div>
        </div>
      </section>

      <section id="{ids[1]}" class="chapter" aria-labelledby="{ids[1]}-t">
        <div class="wrap">
          {chapter_head(2, ch[1], ids[1] + '-t')}
          <ol class="objectives">{objectives}
          </ol>
        </div>
      </section>

      <section id="{ids[2]}" class="chapter" aria-labelledby="{ids[2]}-t">
        <div class="wrap">
          {chapter_head(3, ch[2], ids[2] + '-t')}
          <ol class="phases">{phases}
          </ol>
        </div>
      </section>

      <section id="{ids[3]}" class="chapter is-night tone-night" aria-labelledby="{ids[3]}-t">
        <div class="wrap">
          {chapter_head(4, ch[3], ids[3] + '-t')}
          <div class="gallery">
            <figure class="g-7">{pic('rad-web', '(max-width: 760px) 100vw, 58vw', ra['web'])}</figure>
            <figure class="g-5">{pic('rad-headphones', '(max-width: 760px) 100vw, 40vw', ra['headphones'])}</figure>
            <figure>{pic('rad-brand', '(max-width: 760px) 100vw, 1320px', ra['brand'])}</figure>
            <div class="gallery-label"><h3>{t['c_social']}</h3></div>
            <figure>{pic('rad-social', '(max-width: 760px) 100vw, 1320px', ra['social'])}</figure>
            <div class="gallery-label">{P.format('“HTML5 banners” es un rótulo nuevo')}<h3>{t['r_banners']}</h3></div>
            <div class="banners">{banners}
            </div>
          </div>
        </div>
      </section>

      <section id="{ids[4]}" class="chapter chapter--results" aria-labelledby="{ids[4]}-t">
        <div class="wrap">
          {chapter_head(5, ch[4], ids[4] + '-t')}
          <div class="chapter-body grid">
            <p class="results lede">{t['r_results']}</p>
            <div class="next">
              <h3>{t['r_next_label']}</h3>
              <ul>{nxt}
              </ul>
              <a class="behance-link" href="https://www.behance.net/gallery/190745145/Radio-a-Domicilio" target="_blank" rel="noopener">{ic('i-behance')} Behance {ic('i-go', 'icon--go')}</a>
            </div>
          </div>
        </div>
      </section>
    </div>

    <section class="other-work is-night" aria-labelledby="other-title">
      <div class="wrap">
        <div class="titled">
          <div class="sky"><h2 id="other-title" class="rise display-2" style="padding-bottom:.16em">{t['c_other']}</h2></div>
          <span class="horizon" aria-hidden="true"></span>
        </div>
        <ul class="grid projects">''' + \
        project(t, h, 'invest-in-bogota', 'project--narrow', '(max-width: 760px) 100vw, 42vw') + \
        project(t, h, 'pro-surge-ja') + '''
        </ul>
      </div>
    </section>
  </main>
''' + footer(t, other)
    alts = [('en', BASE + 'radio-a-domicilio/'), ('es', BASE + 'es/radio-a-domicilio/'), ('x-default', BASE + 'radio-a-domicilio/')]
    return page(lang, depth, body, t['r_title'], t['r_desc'], alts, 'page-chapters')


# ------------------------------------------------------------------ 404 (one file, both languages)
def lost():
    en = T['en']
    body = header(en, '@H/', '@H/es/') + sheet(en) + f'''

  <main class="lost">
    <div class="wrap">
      <h1 class="sr-only">404</h1>
      <!-- GIF aleatorio de gatos dentro del sol: clave GIPHY del dueño del sitio, cambia en cada recarga -->
      <div class="sky" aria-hidden="true" data-giphy-key="DPRlJyFbg3L9PxY5AEqfssUoabElSV2k" data-giphy-tag="cat"><span class="sun"></span><span class="rise lost-code">404</span></div>
      <span class="horizon" aria-hidden="true"></span>
      <div class="lost-body" data-lang-block="en">
        <p>The page you are looking for is not found or has been moved. Please return to the main page.</p>
        <a class="btn btn--sun btn--lg" href="@H/">{ic('i-back')} Back to home</a>
        <a class="giphy-credit" href="https://giphy.com" target="_blank" rel="noopener" data-giphy-credit hidden>Powered by GIPHY</a>
      </div>
      <div class="lost-body" data-lang-block="es" lang="es" hidden>
        {ES_DRAFT}
        <p>La página que buscas no se encuentra o ha sido movida. Por favor, regresa a la página principal.</p>
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
write('invest-in-bogota/index.html', case('en'))
write('es/invest-in-bogota/index.html', case('es'))
write('radio-a-domicilio/index.html', case_chapters('en'))
write('es/radio-a-domicilio/index.html', case_chapters('es'))
write('projects-a/index.html', home('en', 'plates'))
write('projects-b/index.html', home('en', 'sheet'))
write('projects-c/index.html', home('en', 'tiles'))
write('404.html', lost())
print('built', ASSET_V, sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*.html')))
