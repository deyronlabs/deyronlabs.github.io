import type { Lang } from '../site';

const en = {
  'lang.name': 'English',
  'meta.home.title': 'Deyron Labs: AI news with primary sources',
  'meta.home.description':
    'Fast, verified AI news. Every story starts with a short summary and links to its primary source.',
  'nav.news': 'News',
  'nav.about': 'About',
  'nav.lab': 'Lab Sessions',
  'lab.title': 'Lab Sessions',
  'lab.description':
    'Step-by-step video tutorials for AI tools, each with a written guide. Free tools first, no jargon.',
  'lab.intro':
    'Lab Sessions teaches one AI tool at a time, step by step. Each episode is a short video with a written guide, the exact prompts and the mistakes to avoid.',
  'lab.episode': 'Episode',
  'lab.watch': 'Watch on YouTube',
  'lab.chapters': 'Chapters',
  'lab.tools': 'Tools used',
  'lab.level': 'Level',
  'lab.length': 'Length',
  'lab.aiNotice':
    'The narration in this video uses a synthetic (AI-generated) voice and an animated presenter. The screen recordings are real. The guide was written by the Deyron Labs team with AI assistance.',
  'lab.all': 'All episodes',
  'lab.latest': 'Latest Lab Sessions',
  'lab.read': 'Read the guide',
  'lab.empty': 'The first episode is on its way.',
  'lab.share': 'Share this guide',
  'nav.support': 'Support',
  'nav.main': 'Main navigation',
  'nav.language': 'Language',
  'nav.skip': 'Skip to content',
  'nav.home': 'Home',
  'nav.breadcrumb': 'Breadcrumb',
  'search.title': 'Search',
  'search.description': 'Search every Deyron Labs news story and Lab Session.',
  'search.label': 'Search the site',
  'search.placeholder': 'Search news and Lab Sessions',
  'search.button': 'Search',
  'search.hint': 'Type a company, model or topic, for example "Claude" or "image editing".',
  'search.count': '{n} results',
  'search.none': 'No results. Try a shorter or different word.',
  'search.noscript': 'Search needs JavaScript. You can browse every story on the News page.',
  'search.kind.news': 'News',
  'search.kind.lab': 'Lab Session',
  'home.h1': 'Deyron Labs: AI news with primary sources',
  'home.tagline': 'What changed in AI, in three paragraphs, with the source one click away.',
  'home.latest': 'Latest stories',
  'home.all': 'All stories',
  'home.empty': 'The first stories are on their way. Subscribe on YouTube or follow the RSS feed.',
  'news.title': 'AI news',
  'news.description': 'Every Deyron Labs story, newest first. Each one links to its primary source.',
  'news.intro': 'Every story, newest first. Each one links to its primary source.',
  'article.published': 'Published',
  'article.updated': 'Updated',
  'article.sources': 'Sources',
  'article.sourcesCount': 'sources',
  'article.sourceOne': 'source',
  'article.primary': 'Primary source',
  'article.watch': 'Watch the video',
  'article.playVideo': 'Play video',
  'share.title': 'Share this story',
  'share.on': 'Share on',
  'share.email': 'Email',
  'share.copy': 'Copy link',
  'share.copied': 'Link copied',
  'share.native': 'Share…',
  'article.facts': 'About this story',
  'article.by': 'By',
  'article.aiNotice':
    'This article was written with AI assistance and checked by the Deyron Labs editorial team against the primary sources before publication.',
  'article.aiNoticeLink': 'How we work',
  'article.readMore': 'Read the story',
  'article.related': 'Topics',
  'about.title': 'About Deyron Labs',
  'about.description':
    'Deyron Labs is an independent AI news publication. Stories are written with AI assistance and checked by editors against primary sources.',
  'about.lead':
    'Deyron Labs explains what changed in AI: new models, tools, policies and research. We keep each story short and link to the primary source so you can check it yourself.',
  'about.how.title': 'How stories are made',
  'about.how.body': [
    'We monitor primary sources: company announcements, research papers, official documentation and regulator filings.',
    'Stories are drafted with AI assistance. An editor then checks the facts, figures and headline against the primary source. Nothing is published without that check.',
    'Every story separates what is confirmed from what is reported or rumored, and says so.',
  ],
  'about.corrections.title': 'Corrections',
  'about.corrections.body':
    'If you find a mistake, write to us. We fix it, mark the story as updated and show the date of the change.',
  'about.contact.title': 'Contact',
  'about.contact.general': 'General questions and corrections',
  'about.contact.collab': 'Collaborations and sponsors',
  'author.title': 'Deyron Labs Editorial Desk',
  'author.description':
    'The Deyron Labs editorial desk writes and checks every story on this site. Stories are drafted with AI assistance and verified by an editor.',
  'author.body': [
    'The editorial desk is the byline on every Deyron Labs story. It covers AI models, tools, policy and research, and publishes with a link to the primary source.',
    'Drafts are prepared with AI assistance. An editor checks each story before it goes live.',
  ],
  'author.stories': 'Stories by the desk',
  'footer.about': 'Independent AI news. Written with AI assistance, checked by editors.',
  'footer.follow': 'Follow',
  'footer.explore': 'Explore',
  'footer.contact': 'Contact',
  'footer.feeds': 'For readers and machines',
  'footer.rss': 'RSS feed',
  'footer.sitemap': 'Sitemap',
  'footer.llms': 'llms.txt',
  'footer.rights': 'All rights reserved.',
  'footer.project': 'The project',
  'newsletter.box.title': 'Get The Lab Report by email',
  'newsletter.box.body':
    'One short email every Friday: the week in AI, each story linked to its primary source. A three-minute read.',
  'newsletter.cta': 'Subscribe',
  'newsletter.note': 'Free. You confirm by email and can unsubscribe at any time.',
  'newsletter.more': 'How we handle your email',
  'footer.newsletterCta': 'Get The Lab Report by email',
  'footer.supportCta': 'Support Deyron Labs',
  'support.title': 'Support Deyron Labs',
  'support.description':
    'Deyron Labs is independent and reader-supported. Here is how to help, what the money pays for, and what it does not buy.',
  'support.lead':
    'Deyron Labs is an independent project. If our stories and tutorials save you time, you can help keep them coming with a small, one-time contribution.',
  'support.cta': 'Support on Ko-fi',
  'support.ctaNote': 'Opens Ko-fi in a new tab. Payments are handled by Ko-fi and PayPal.',
  'support.goes.title': 'What your support pays for',
  'support.goes.body': [
    'Voice generation for our videos.',
    'The subscriptions and credits we use to test AI tools before we show them to you.',
    'The domain, email and other running costs of the site and the channel.',
  ],
  'support.promise.title': 'What it does not buy',
  'support.promise.body': [
    'Coverage. Contributions never decide which stories we publish, how we rate them or what we say about a product.',
    'Perks or exclusive content. For now, a contribution is a thank-you, not a purchase.',
    'Contributions are voluntary and are not tax-deductible.',
  ],
  'support.other.title': 'Other ways to help',
  'support.other.body': [
    'Subscribe on YouTube and share a story you found useful.',
    'Send us a correction or a tip at the address below. Corrections make every story better.',
    'Brands and organizations: see our sponsorship page.',
  ],
  'support.sponsorsLink': 'Sponsorship and partnerships',
  'support.youtube': 'Deyron Labs on YouTube',
  'support.box.title': 'Found this useful?',
  'support.box.body': 'Deyron Labs is independent and reader-supported. A small contribution helps us keep testing AI tools.',
  'support.box.cta': 'Support on Ko-fi',
  'support.box.more': 'How support works',
  'sponsors.title': 'Sponsorship and partnerships',
  'sponsors.description':
    'How brands can work with Deyron Labs, and the independence rules that apply to every sponsor.',
  'sponsors.lead':
    'Deyron Labs is a small, independent publication about AI tools. We are open to sponsors who fit our audience, on terms that keep our reporting independent.',
  'sponsors.who.title': 'Who we reach',
  'sponsors.who.body':
    'Our readers and viewers are people who use AI tools at work and at home and want to know what changed, what is worth trying and what to skip. We publish news stories on this site and videos on YouTube, in English.',
  'sponsors.rules.title': 'Our independence rules',
  'sponsors.rules.body': [
    'Sponsors never choose, review or influence which stories we cover, how we assess them or what we conclude.',
    'Paid content is always labeled as sponsored, in the video and in its description or article. We do not publish paid content that looks like reporting.',
    'We do not promise positive coverage, and we do not accept payment to remove or soften coverage.',
    'If we receive a product, access or credits for free, we say so. Receiving them does not buy coverage.',
    'We disclose relationships that could affect our work. We use Claude, made by Anthropic, to help produce our stories, and stories about Anthropic carry a notice saying so.',
  ],
  'sponsors.formats.title': 'What we can discuss',
  'sponsors.formats.body': [
    'A clearly labeled sponsored segment in a video.',
    'A sponsored tutorial about a tool you make, with the limits and drawbacks we find stated honestly.',
    'Longer-term partnerships, once the channel has the audience to justify them.',
  ],
  'sponsors.formats.note':
    'We are early. We do not publish a rate card yet, and we are not accepting paid placements inside news stories.',
  'sponsors.contact.title': 'Get in touch',
  'sponsors.contact.body': 'Write to us with who you are, what you make and what you have in mind.',
  'privacy.title': 'Privacy',
  'privacy.description':
    'What Deyron Labs collects when you visit, what we do not collect and which third-party services are involved.',
  'privacy.lead':
    'We collect as little as we can. We do not run ads, we do not use advertising or tracking cookies, and we do not ask you to create an account.',
  'privacy.updated': 'Last updated: 8 October 2026',
  'privacy.sections': [
    {
      title: 'Visit statistics',
      body: [
        'We use Cloudflare Web Analytics to see which pages are read, from which countries and sources, and on what kind of device. It does not use cookies and does not follow you across sites. We see aggregate numbers, not who you are.',
      ],
    },
    {
      title: 'Hosting and fonts',
      body: [
        'The site is hosted on GitHub Pages, which, like any web host, processes technical data such as your IP address to serve pages. Page text uses a typeface loaded from Google Fonts, which means your browser contacts Google to download it.',
      ],
    },
    {
      title: 'Videos',
      body: [
        'Videos load only when you press play, using YouTube’s privacy-enhanced embed (youtube-nocookie.com). Until then, your browser loads nothing from YouTube except, on the few pages without their own image, the video’s preview picture. After you press play, YouTube’s own privacy policy applies.',
      ],
    },
    {
      title: 'Support links and other sites',
      body: [
        'The Support button links to Ko-fi. We do not load Ko-fi code on this site. If you contribute, your payment is handled by Ko-fi and its payment providers under their terms. We do not see or store your payment details. Links to social networks and sources also leave this site and follow those sites’ policies.',
      ],
    },
    {
      title: 'Newsletter',
      body: [
        'If you subscribe to The Lab Report, our weekly newsletter, we collect your email address. We send it with beehiiv, which stores your address and may process it outside the EU under its own terms and privacy policy. When you subscribe, beehiiv sends you an email to confirm. beehiiv also records whether an email was opened and which links were clicked, and makes that information available to us.',
        'We use your address only to send the newsletter and to reply to you. We do not sell or share it. Every edition has an unsubscribe link, and you can ask us to delete your address at any time at the contact address below. The subscribe page is hosted by beehiiv; this site only links to it and loads none of its code.',
      ],
    },
    {
      title: 'Email',
      body: [
        'If you write to us, we use your message and address only to reply and, if needed, to correct a story. We do not sell or share them.',
      ],
    },
    {
      title: 'Your rights',
      body: [
        'Under EU data protection law you can ask what personal data we hold about you, and ask us to correct or delete it. Write to the contact address below. We hold very little, mostly emails you send us.',
      ],
    },
    {
      title: 'Changes',
      body: [
        'If this page changes in a way that matters, we update the date at the top. If we add a service that uses cookies, such as advertising, we will say so here first.',
      ],
    },
  ],
  'privacy.contact': 'Questions about privacy',
  '404.title': 'Page not found',
  '404.body': 'This page does not exist or has moved. Try the latest stories.',
  '404.cta': 'Go to the latest stories',
};

export type Dict = typeof en;
export type UiKey = keyof Dict;

const es: Dict = {
  'lang.name': 'Español',
  'meta.home.title': 'Deyron Labs: noticias de IA con fuentes primarias',
  'meta.home.description':
    'Noticias de IA rápidas y verificadas. Cada historia empieza con un resumen corto y enlaza a su fuente primaria.',
  'nav.news': 'Noticias',
  'nav.about': 'Acerca de',
  'nav.lab': 'Lab Sessions',
  'lab.title': 'Lab Sessions',
  'lab.description':
    'Tutoriales en vídeo paso a paso sobre herramientas de IA, cada uno con una guía escrita. Primero las herramientas gratuitas, sin jerga.',
  'lab.intro':
    'Lab Sessions enseña una herramienta de IA cada vez, paso a paso. Cada episodio es un vídeo corto con una guía escrita, los prompts exactos y los errores que conviene evitar.',
  'lab.episode': 'Episodio',
  'lab.watch': 'Ver en YouTube',
  'lab.chapters': 'Capítulos',
  'lab.tools': 'Herramientas usadas',
  'lab.level': 'Nivel',
  'lab.length': 'Duración',
  'lab.aiNotice':
    'La narración de este vídeo usa una voz sintética (generada por IA) y un presentador animado. Las grabaciones de pantalla son reales. La guía la escribió el equipo de Deyron Labs con ayuda de IA.',
  'lab.all': 'Todos los episodios',
  'lab.latest': 'Últimos Lab Sessions',
  'lab.read': 'Leer la guía',
  'lab.empty': 'El primer episodio está en camino.',
  'lab.share': 'Compartir esta guía',
  'nav.support': 'Apoyar',
  'nav.main': 'Navegación principal',
  'nav.language': 'Idioma',
  'nav.skip': 'Saltar al contenido',
  'nav.home': 'Inicio',
  'nav.breadcrumb': 'Ruta de navegación',
  'search.title': 'Buscar',
  'search.description': 'Busca entre todas las noticias y Lab Sessions de Deyron Labs.',
  'search.label': 'Buscar en el sitio',
  'search.placeholder': 'Buscar noticias y Lab Sessions',
  'search.button': 'Buscar',
  'search.hint': 'Escribe una empresa, un modelo o un tema, por ejemplo "Claude" o "edición de imágenes".',
  'search.count': '{n} resultados',
  'search.none': 'Sin resultados. Prueba con otra palabra o una más corta.',
  'search.noscript': 'La búsqueda necesita JavaScript. Puedes ver todas las noticias en la página de Noticias.',
  'search.kind.news': 'Noticias',
  'search.kind.lab': 'Lab Session',
  'home.h1': 'Deyron Labs: noticias de IA con fuentes primarias',
  'home.tagline': 'Qué cambió en la IA, en tres párrafos, con la fuente a un clic.',
  'home.latest': 'Últimas historias',
  'home.all': 'Todas las historias',
  'home.empty': 'Las primeras historias están en camino. Suscríbete en YouTube o sigue el feed RSS.',
  'news.title': 'Noticias de IA',
  'news.description':
    'Todas las historias de Deyron Labs, de la más reciente a la más antigua. Cada una enlaza a su fuente primaria.',
  'news.intro':
    'Todas las historias, de la más reciente a la más antigua. Cada una enlaza a su fuente primaria.',
  'article.published': 'Publicado',
  'article.updated': 'Actualizado',
  'article.sources': 'Fuentes',
  'article.sourcesCount': 'fuentes',
  'article.sourceOne': 'fuente',
  'article.primary': 'Fuente primaria',
  'article.watch': 'Ver el video',
  'article.playVideo': 'Reproducir video',
  'share.title': 'Compartir esta historia',
  'share.on': 'Compartir en',
  'share.email': 'Correo',
  'share.copy': 'Copiar enlace',
  'share.copied': 'Enlace copiado',
  'share.native': 'Compartir…',
  'article.facts': 'Sobre esta historia',
  'article.by': 'Por',
  'article.aiNotice':
    'Este artículo fue escrito con ayuda de IA y revisado por el equipo editorial de Deyron Labs frente a las fuentes primarias antes de publicarse.',
  'article.aiNoticeLink': 'Cómo trabajamos',
  'article.readMore': 'Leer la historia',
  'article.related': 'Temas',
  'about.title': 'Acerca de Deyron Labs',
  'about.description':
    'Deyron Labs es una publicación independiente de noticias de IA. Las historias se escriben con ayuda de IA y los editores las revisan frente a fuentes primarias.',
  'about.lead':
    'Deyron Labs explica qué cambió en la IA: modelos, herramientas, políticas e investigación. Mantenemos cada historia breve y enlazamos la fuente primaria para que puedas comprobarla.',
  'about.how.title': 'Cómo se hacen las historias',
  'about.how.body': [
    'Seguimos fuentes primarias: anuncios de empresas, artículos de investigación, documentación oficial y documentos de reguladores.',
    'Las historias se redactan con ayuda de IA. Después, un editor comprueba los hechos, las cifras y el titular frente a la fuente primaria. No se publica nada sin esa revisión.',
    'Cada historia separa lo confirmado de lo que se informa o se rumorea, y lo dice.',
  ],
  'about.corrections.title': 'Correcciones',
  'about.corrections.body':
    'Si encuentras un error, escríbenos. Lo corregimos, marcamos la historia como actualizada y mostramos la fecha del cambio.',
  'about.contact.title': 'Contacto',
  'about.contact.general': 'Preguntas generales y correcciones',
  'about.contact.collab': 'Colaboraciones y patrocinadores',
  'author.title': 'Redacción de Deyron Labs',
  'author.description':
    'La redacción de Deyron Labs escribe y revisa cada historia de este sitio. Las historias se redactan con ayuda de IA y las verifica un editor.',
  'author.body': [
    'La redacción firma todas las historias de Deyron Labs. Cubre modelos, herramientas, políticas e investigación en IA, y publica con un enlace a la fuente primaria.',
    'Los borradores se preparan con ayuda de IA. Un editor revisa cada historia antes de que se publique.',
  ],
  'author.stories': 'Historias de la redacción',
  'footer.about': 'Noticias de IA independientes. Escritas con ayuda de IA y revisadas por editores.',
  'footer.follow': 'Síguenos',
  'footer.explore': 'Explorar',
  'footer.contact': 'Contacto',
  'footer.feeds': 'Para lectores y máquinas',
  'footer.rss': 'Feed RSS',
  'footer.sitemap': 'Mapa del sitio',
  'footer.llms': 'llms.txt',
  'footer.rights': 'Todos los derechos reservados.',
  'footer.project': 'El proyecto',
  'newsletter.box.title': 'Recibe The Lab Report por correo',
  'newsletter.box.body':
    'Un correo breve cada viernes: la semana en IA, con cada historia enlazada a su fuente primaria. Tres minutos de lectura.',
  'newsletter.cta': 'Suscribirme',
  'newsletter.note': 'Gratis. Confirmas por correo y puedes darte de baja cuando quieras.',
  'newsletter.more': 'Cómo tratamos tu correo',
  'footer.newsletterCta': 'Recibe The Lab Report por correo',
  'footer.supportCta': 'Apoya a Deyron Labs',
  'support.title': 'Apoya a Deyron Labs',
  'support.description':
    'Deyron Labs es independiente y se sostiene con el apoyo de sus lectores. Cómo ayudar, en qué se usa el dinero y qué no compra.',
  'support.lead':
    'Deyron Labs es un proyecto independiente. Si nuestras historias y tutoriales te ahorran tiempo, puedes ayudarnos a seguir con una pequeña contribución puntual.',
  'support.cta': 'Apoyar en Ko-fi',
  'support.ctaNote': 'Se abre Ko-fi en una pestaña nueva. Los pagos los gestionan Ko-fi y PayPal.',
  'support.goes.title': 'En qué se usa tu apoyo',
  'support.goes.body': [
    'La generación de voz de nuestros videos.',
    'Las suscripciones y créditos que usamos para probar herramientas de IA antes de mostrártelas.',
    'El dominio, el correo y otros gastos de funcionamiento del sitio y del canal.',
  ],
  'support.promise.title': 'Qué no compra',
  'support.promise.body': [
    'Cobertura. Las contribuciones nunca deciden qué historias publicamos, cómo las valoramos ni qué decimos de un producto.',
    'Ventajas o contenido exclusivo. Por ahora, una contribución es un agradecimiento, no una compra.',
    'Las contribuciones son voluntarias y no son deducibles de impuestos.',
  ],
  'support.other.title': 'Otras formas de ayudar',
  'support.other.body': [
    'Suscríbete en YouTube y comparte una historia que te haya servido.',
    'Envíanos una corrección o una pista a la dirección de abajo. Las correcciones mejoran cada historia.',
    'Marcas y organizaciones: consulta nuestra página de patrocinio.',
  ],
  'support.sponsorsLink': 'Patrocinio y colaboraciones',
  'support.youtube': 'Deyron Labs en YouTube',
  'support.box.title': '¿Te ha resultado útil?',
  'support.box.body':
    'Deyron Labs es independiente y se sostiene con el apoyo de sus lectores. Una pequeña contribución nos ayuda a seguir probando herramientas de IA.',
  'support.box.cta': 'Apoyar en Ko-fi',
  'support.box.more': 'Cómo funciona el apoyo',
  'sponsors.title': 'Patrocinio y colaboraciones',
  'sponsors.description':
    'Cómo pueden trabajar las marcas con Deyron Labs y las reglas de independencia que se aplican a todo patrocinador.',
  'sponsors.lead':
    'Deyron Labs es una publicación pequeña e independiente sobre herramientas de IA. Estamos abiertos a patrocinadores afines a nuestra audiencia, en condiciones que mantengan independiente nuestro trabajo.',
  'sponsors.who.title': 'A quién llegamos',
  'sponsors.who.body':
    'Nuestros lectores y espectadores usan herramientas de IA en el trabajo y en casa, y quieren saber qué cambió, qué merece la pena probar y qué descartar. Publicamos noticias en este sitio y videos en YouTube, en inglés.',
  'sponsors.rules.title': 'Nuestras reglas de independencia',
  'sponsors.rules.body': [
    'Los patrocinadores nunca eligen, revisan ni influyen en qué historias cubrimos, cómo las valoramos ni qué concluimos.',
    'El contenido de pago siempre se etiqueta como patrocinado, en el video y en su descripción o artículo. No publicamos contenido de pago que parezca información periodística.',
    'No prometemos una cobertura positiva ni aceptamos pagos para retirar o suavizar una cobertura.',
    'Si recibimos gratis un producto, acceso o créditos, lo decimos. Recibirlos no compra cobertura.',
    'Declaramos las relaciones que podrían afectar nuestro trabajo. Usamos Claude, de Anthropic, para ayudar a producir nuestras historias, y las historias sobre Anthropic llevan un aviso que lo indica.',
  ],
  'sponsors.formats.title': 'De qué podemos hablar',
  'sponsors.formats.body': [
    'Un segmento patrocinado, claramente etiquetado, dentro de un video.',
    'Un tutorial patrocinado sobre una herramienta tuya, en el que decimos con honestidad los límites y los inconvenientes que encontremos.',
    'Colaboraciones a más largo plazo, cuando el canal tenga la audiencia que las justifique.',
  ],
  'sponsors.formats.note':
    'Estamos empezando. Todavía no publicamos tarifas y no aceptamos emplazamientos de pago dentro de las noticias.',
  'sponsors.contact.title': 'Contacto',
  'sponsors.contact.body': 'Escríbenos con quién eres, qué haces y qué tienes en mente.',
  'privacy.title': 'Privacidad',
  'privacy.description':
    'Qué datos recoge Deyron Labs cuando visitas el sitio, cuáles no recoge y qué servicios de terceros intervienen.',
  'privacy.lead':
    'Recogemos lo mínimo posible. No mostramos anuncios, no usamos cookies publicitarias ni de seguimiento y no te pedimos crear una cuenta.',
  'privacy.updated': 'Última actualización: 8 de octubre de 2026',
  'privacy.sections': [
    {
      title: 'Estadísticas de visitas',
      body: [
        'Usamos Cloudflare Web Analytics para saber qué páginas se leen, desde qué países y fuentes y en qué tipo de dispositivo. No usa cookies ni te sigue entre sitios. Vemos cifras agregadas, no quién eres.',
      ],
    },
    {
      title: 'Alojamiento y tipografías',
      body: [
        'El sitio está alojado en GitHub Pages que, como cualquier alojamiento web, trata datos técnicos como tu dirección IP para servir las páginas. El texto usa una tipografía cargada desde Google Fonts, por lo que tu navegador contacta con Google para descargarla.',
      ],
    },
    {
      title: 'Videos',
      body: [
        'Los videos se cargan solo cuando pulsas reproducir, con el reproductor de YouTube con privacidad mejorada (youtube-nocookie.com). Hasta entonces tu navegador no carga nada de YouTube, salvo, en las pocas páginas sin imagen propia, la imagen de vista previa del video. Después, se aplica la política de privacidad de YouTube.',
      ],
    },
    {
      title: 'Enlaces de apoyo y otros sitios',
      body: [
        'El botón de apoyo enlaza a Ko-fi. No cargamos código de Ko-fi en este sitio. Si contribuyes, tu pago lo gestionan Ko-fi y sus proveedores de pago según sus condiciones. No vemos ni guardamos tus datos de pago. Los enlaces a redes sociales y a fuentes también salen de este sitio y siguen las políticas de esos sitios.',
      ],
    },
    {
      title: 'Newsletter',
      body: [
        'Si te suscribes a The Lab Report, nuestro boletín semanal, recogemos tu dirección de correo. Lo enviamos con beehiiv, que guarda tu dirección y puede tratarla fuera de la UE según sus propias condiciones y política de privacidad. Al suscribirte, beehiiv te envía un correo para confirmar. beehiiv también registra si un correo se abrió y en qué enlaces se hizo clic, y nos pone esa información a disposición.',
        'Usamos tu dirección solo para enviar el boletín y para responderte. No la vendemos ni la compartimos. Cada edición lleva un enlace para darte de baja y puedes pedirnos que eliminemos tu dirección en cualquier momento, en la dirección de contacto de abajo. La página de suscripción está alojada en beehiiv; este sitio solo enlaza a ella y no carga nada de su código.',
      ],
    },
    {
      title: 'Correo electrónico',
      body: [
        'Si nos escribes, usamos tu mensaje y tu dirección solo para responder y, si hace falta, corregir una historia. No los vendemos ni los compartimos.',
      ],
    },
    {
      title: 'Tus derechos',
      body: [
        'Según la normativa de protección de datos de la UE, puedes preguntarnos qué datos personales tenemos sobre ti y pedirnos que los corrijamos o eliminemos. Escribe a la dirección de contacto de abajo. Guardamos muy pocos datos, sobre todo los correos que nos envías.',
      ],
    },
    {
      title: 'Cambios',
      body: [
        'Si esta página cambia de forma relevante, actualizamos la fecha de arriba. Si añadimos un servicio que use cookies, como publicidad, lo diremos aquí antes.',
      ],
    },
  ],
  'privacy.contact': 'Preguntas sobre privacidad',
  '404.title': 'Página no encontrada',
  '404.body': 'Esta página no existe o se movió. Prueba con las últimas historias.',
  '404.cta': 'Ir a las últimas historias',
};

export const ui: Record<Lang, Dict> = { en, es };
