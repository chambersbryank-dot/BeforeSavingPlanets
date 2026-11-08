"""About and Contact words for this site.

The banner, menu, and buttons stay the approved Saving Planets layout.
These sentences replace the solutions copy. Facts are the ones this site
already states. The only address is the inbox the pages already use.
"""
import html
import about_pages

MAIL = "hello@savingplanets.com"
MAIL_NOTE = {
    "en": "That is the Saving Planets inbox until a Before Saving Planets address exists.",
    "fr": "C’est la boîte de Saving Planets jusqu’à ce qu’une adresse Before Saving Planets existe.",
    "es": "Es el buzón de Saving Planets hasta que exista una dirección de Before Saving Planets.",
    "ar": "هذا صندوق Saving Planets إلى أن يوجد عنوان لـ Before Saving Planets.",
    "it": "È la casella di Saving Planets finché non esiste un indirizzo di Before Saving Planets.",
    "he": "זו תיבת Saving Planets עד שתהיה כתובת של Before Saving Planets.",
}
SUB = {
    "About": {
        "en": "The fossil record in plain language, with the source next to the claim.",
        "fr": "Le registre fossile en langage clair, avec la source à côté de l’affirmation.",
        "es": "El registro fósil en lenguaje claro, con la fuente junto a la afirmación.",
        "ar": "سجل الأحافير بلغة واضحة، والمصدر بجانب الادعاء.",
        "it": "Il registro fossile in linguaggio chiaro, con la fonte accanto all’affermazione.",
        "he": "תיעוד המאובנים בשפה פשוטה, והמקור ליד הטענה.",
    },
    "Contact": {
        "en": "Questions and corrections.",
        "fr": "Questions et corrections.",
        "es": "Preguntas y correcciones.",
        "ar": "أسئلة وتصحيحات.",
        "it": "Domande e correzioni.",
        "he": "שאלות ותיקונים.",
    },
}


def _e(text):
    return html.escape(text)


def _cards(rows):
    body = []
    for title, text in rows:
        body.append(f'<div class="w-card"><h3>{_e(title)}</h3><p>{text}</p></div>')
    return f'<div class="ws-grid">{"".join(body)}</div>'


def _mail():
    return f'<a href="mailto:{MAIL}">{MAIL}</a>'


def _about(lang):
    mail = _mail()
    note = _e(MAIL_NOTE[lang])
    routes = {
        "en": (
            f'<a href="Dinosaurs.html">Dinosaurs</a>, <a href="Mammals.html">mammals</a>, '
            f'<a href="Aerial.html">animals of the air</a>, <a href="Marine.html">animals of the sea</a>, '
            f'a <a href="World_Map.html">world map of finds</a>, and <a href="Deep_Time.html">Deep Time</a>. '
            f'<a href="Learn.html">Education</a> pages outline geology and archaeology.'
        ),
        "fr": (
            f'<a href="Dinosaurs.html">Dinosaures</a>, <a href="Mammals.html">mammifères</a>, '
            f'<a href="Aerial.html">animaux de l’air</a>, <a href="Marine.html">animaux de la mer</a>, '
            f'une <a href="World_Map.html">carte des trouvailles</a> et le <a href="Deep_Time.html">temps profond</a>. '
            f'Les pages <a href="Learn.html">d’éducation</a> présentent la géologie et l’archéologie.'
        ),
        "es": (
            f'<a href="Dinosaurs.html">Dinosaurios</a>, <a href="Mammals.html">mamíferos</a>, '
            f'<a href="Aerial.html">animales del aire</a>, <a href="Marine.html">animales del mar</a>, '
            f'un <a href="World_Map.html">mapa de hallazgos</a> y el <a href="Deep_Time.html">tiempo profundo</a>. '
            f'Las páginas de <a href="Learn.html">educación</a> presentan la geología y la arqueología.'
        ),
        "ar": (
            f'<a href="Dinosaurs.html">الديناصورات</a>، <a href="Mammals.html">الثدييات</a>، '
            f'<a href="Aerial.html">حيوانات الجو</a>، <a href="Marine.html">حيوانات البحر</a>، '
            f'<a href="World_Map.html">خريطة المكتشفات</a>، و<a href="Deep_Time.html">الزمن العميق</a>. '
            f'صفحات <a href="Learn.html">التعليم</a> تعرض الجيولوجيا والآثار.'
        ),
        "it": (
            f'<a href="Dinosaurs.html">Dinosauri</a>, <a href="Mammals.html">mammiferi</a>, '
            f'<a href="Aerial.html">animali dell’aria</a>, <a href="Marine.html">animali del mare</a>, '
            f'una <a href="World_Map.html">mappa dei ritrovamenti</a> e il <a href="Deep_Time.html">tempo profondo</a>. '
            f'Le pagine di <a href="Learn.html">istruzione</a> presentano geologia e archeologia.'
        ),
        "he": (
            f'<a href="Dinosaurs.html">דינוזאורים</a>, <a href="Mammals.html">יונקים</a>, '
            f'<a href="Aerial.html">בעלי חיים של האוויר</a>, <a href="Marine.html">בעלי חיים של הים</a>, '
            f'<a href="World_Map.html">מפת ממצאים</a> ו<a href="Deep_Time.html">זמן עמוק</a>. '
            f'עמודי <a href="Learn.html">הלימוד</a> מציגים גאולוגיה וארכאולוגיה.'
        ),
    }
    T = {
        "en": {
            "lead": "Ancient Earth, geology, archaeology, and the history of life.",
            "blurb": "A finished page links a claim to a paper, a museum, a survey, or a park service page. This site does not invent a body length and does not draw a cartoon Earth.",
            "h_site": "Before Saving Planets",
            "aim": "The aim", "aim_p": "Show the fossil record in plain language, with the source next to the claim. No invented body length. No cartoon Earth.",
            "cover": "What we cover",
            "mission": "The mission", "mission_p": "Saving Planets shows solutions for the living world. This site shows the record those solutions sit on: climates, ecosystems, and life through deep time.",
            "write": "Write to us",
            "h_rules": "How a page earns its place",
            "src": "A source you can open", "src_p": "A date or a claim on a finished page links to a paper, a museum, a survey, or a park service page.",
            "pic": "A picture is labeled", "pic_p": "A photograph says who made it. An artist’s reconstruction says Created by the Founder and SI. A map says which model drew the coastlines.",
            "len": "No invented measure", "len_p": "A body length appears only when a cited source gives that length. A file note from an artist is not a measurement.",
            "help": "Help goes to the museum", "help_p": "Donate and volunteer buttons open the museum that holds the fossil. This site is free and asks for nothing for itself.",
            "h_who": "Who builds this",
            "founder": "The Founder", "founder_p": "Sets the direction and approves the pages.",
            "si": "SI", "si_p": "Researches, drafts, and checks the sources. The credit line is Created by the Founder and SI.",
            "vol": "Volunteers", "vol_p": "Language corrections are welcome at",
            "h_src": "Sources named on this site",
            "src_intro": "These are sources the pages already link. A link is not an endorsement and not a partnership. This list does not count pages.",
            "h_rest": "This site and its sister",
            "sister": "Sister site", "sister_p": "Before Saving Planets does not run a sponsor program and does not list partners. A museum link is a citation or a way to help that museum, not a partnership.",
            "analytics": "Analytics", "analytics_p": "Home, About, Learn, and the other adult pages load Cloudflare Web Analytics. Kids and Kids Map do not load that script.",
            "news": "Newsletter", "news_p": "Adult pages can show the Weekly Before Saving Planets Brief signup. Kids and Kids Map do not show the form, and they do not send the event beacon.",
            "use": "Use", "use_p": "Read the pages in class. Third-party images keep the credit printed beside them. Pictures and films made for this site stay credited Created by the Founder and SI.",
        },
        "fr": {
            "lead": "La Terre ancienne, la géologie, l’archéologie et l’histoire de la vie.",
            "blurb": "Une page terminée relie une affirmation à un article, un musée, un service géologique ou une page de parc. Ce site n’invente pas une longueur de corps et ne dessine pas une Terre en dessin animé.",
            "h_site": "Before Saving Planets",
            "aim": "Le but", "aim_p": "Montrer le registre fossile en langage clair, avec la source à côté de l’affirmation. Pas de longueur de corps inventée. Pas de Terre en dessin animé.",
            "cover": "Ce que nous couvrons",
            "mission": "La mission", "mission_p": "Saving Planets montre des solutions pour le monde vivant. Ce site montre le registre sur lequel ces solutions reposent : climats, écosystèmes et vie à travers le temps profond.",
            "write": "Nous écrire",
            "h_rules": "Comment une page gagne sa place",
            "src": "Une source que l’on peut ouvrir", "src_p": "Une date ou une affirmation sur une page terminée renvoie à un article, un musée, un service géologique ou une page de parc.",
            "pic": "Une image est légendée", "pic_p": "Une photographie dit qui l’a faite. Une reconstitution d’artiste dit Created by the Founder and SI. Une carte dit quel modèle a tracé les côtes.",
            "len": "Pas de mesure inventée", "len_p": "Une longueur de corps n’apparaît que si une source citée la donne. Une note d’artiste n’est pas une mesure.",
            "help": "L’aide va au musée", "help_p": "Les boutons de don et de bénévolat ouvrent le musée qui garde le fossile. Ce site est gratuit et ne demande rien pour lui-même.",
            "h_who": "Qui construit ceci",
            "founder": "Le fondateur", "founder_p": "Fixe la direction et approuve les pages.",
            "si": "SI", "si_p": "Recherche, rédige et vérifie les sources. La ligne de crédit est Created by the Founder and SI.",
            "vol": "Bénévoles", "vol_p": "Les corrections de langue sont les bienvenues à",
            "h_src": "Sources nommées sur ce site",
            "src_intro": "Ce sont des sources que les pages lient déjà. Un lien n’est pas une approbation ni un partenariat. Cette liste ne compte pas les pages.",
            "sister": "Site jumeau", "sister_p": "Before Saving Planets n’a pas de programme de parrainage et ne liste pas de partenaires. Un lien vers un musée est une citation ou une façon d’aider ce musée, pas un partenariat.",
            "analytics": "Mesure d’audience", "analytics_p": "L’accueil, À propos, Apprendre et les autres pages adultes chargent Cloudflare Web Analytics. Enfants et la carte des enfants ne chargent pas ce script.",
            "news": "Bulletin", "news_p": "Les pages adultes peuvent montrer l’inscription au bulletin. Enfants et la carte des enfants ne montrent pas le formulaire et n’envoient pas le signal de visite.",
            "use": "Usage", "use_p": "Lire les pages en classe. Les images de tiers gardent le crédit imprimé à côté. Les images et films faits pour ce site portent Created by the Founder and SI.",
            "h_rest": "Ce site et son jumeau",
        },
    }
    # Spanish, Arabic, Italian, and Hebrew use the same facts.
    T["es"] = {
        "lead": "La Tierra antigua, la geología, la arqueología y la historia de la vida.",
        "blurb": "Una página terminada enlaza una afirmación con un artículo, un museo, un servicio geológico o una página de un parque. Este sitio no inventa una longitud del cuerpo y no dibuja una Tierra de dibujos.",
        "h_site": "Before Saving Planets",
        "aim": "El propósito", "aim_p": "Mostrar el registro fósil en lenguaje claro, con la fuente junto a la afirmación. Sin longitud del cuerpo inventada. Sin Tierra de dibujos.",
        "cover": "Qué cubrimos",
        "mission": "La misión", "mission_p": "Saving Planets muestra soluciones para el mundo vivo. Este sitio muestra el registro sobre el que se apoyan: climas, ecosistemas y vida a través del tiempo profundo.",
        "write": "Escríbanos",
        "h_rules": "Cómo una página gana su lugar",
        "src": "Una fuente que se puede abrir", "src_p": "Una fecha o una afirmación en una página terminada enlaza un artículo, un museo, un servicio geológico o una página de un parque.",
        "pic": "Una imagen lleva leyenda", "pic_p": "Una fotografía dice quién la hizo. Una reconstrucción de artista dice Created by the Founder and SI. Un mapa dice qué modelo trazó las costas.",
        "len": "Sin medida inventada", "len_p": "Una longitud del cuerpo aparece solo cuando una fuente citada la da. Una nota de un artista no es una medida.",
        "help": "La ayuda va al museo", "help_p": "Los botones de donar y voluntariado abren el museo que guarda el fósil. Este sitio es gratis y no pide nada para sí.",
        "h_who": "Quién construye esto",
        "founder": "El fundador", "founder_p": "Marca la dirección y aprueba las páginas.",
        "si": "SI", "si_p": "Investiga, redacta y comprueba las fuentes. La línea de crédito es Created by the Founder and SI.",
        "vol": "Voluntarios", "vol_p": "Las correcciones de idioma son bienvenidas en",
        "h_src": "Fuentes nombradas en este sitio",
        "src_intro": "Son fuentes que las páginas ya enlazan. Un enlace no es un respaldo ni una asociación. Esta lista no cuenta páginas.",
        "h_rest": "Este sitio y su hermano",
        "sister": "Sitio hermano", "sister_p": "Before Saving Planets no tiene un programa de patrocinio y no lista socios. Un enlace a un museo es una cita o una forma de ayudar a ese museo, no una asociación.",
        "analytics": "Analítica", "analytics_p": "Inicio, Acerca de, Aprender y las demás páginas de adultos cargan Cloudflare Web Analytics. Niños y el mapa infantil no cargan ese script.",
        "news": "Boletín", "news_p": "Las páginas de adultos pueden mostrar la inscripción al boletín. Niños y el mapa infantil no muestran el formulario y no envían la señal de visita.",
        "use": "Uso", "use_p": "Lean las páginas en clase. Las imágenes de terceros conservan el crédito impreso junto a ellas. Las imágenes y películas hechas para este sitio llevan Created by the Founder and SI.",
    }
    T["ar"] = {
        "lead": "الأرض القديمة، والجيولوجيا، والآثار، وتاريخ الحياة.",
        "blurb": "الصفحة المكتملة تربط الادعاء بورقة أو متحف أو هيئة مسح أو صفحة متنزه. هذا الموقع لا يخترع طول جسم ولا يرسم أرضًا كرتونية.",
        "h_site": "Before Saving Planets",
        "aim": "الهدف", "aim_p": "عرض سجل الأحافير بلغة واضحة، والمصدر بجانب الادعاء. لا طول جسم مخترع. لا أرض كرتونية.",
        "cover": "ما نغطيه",
        "mission": "المهمة", "mission_p": "يعرض Saving Planets حلولًا للعالم الحي. يعرض هذا الموقع السجل الذي تقوم عليه تلك الحلول: المناخات والنظم والحياة عبر الزمن العميق.",
        "write": "اكتبوا إلينا",
        "h_rules": "كيف تكسب الصفحة مكانها",
        "src": "مصدر يمكن فتحه", "src_p": "التاريخ أو الادعاء في صفحة مكتملة يربط بورقة أو متحف أو هيئة مسح أو صفحة متنزه.",
        "pic": "الصورة معلَّمة", "pic_p": "الصورة تقول من صنعها. إعادة بناء الفنان تقول Created by the Founder and SI. الخريطة تقول أي نموذج رسم السواحل.",
        "len": "لا قياس مخترع", "len_p": "طول الجسم يظهر فقط إذا أعطته مصدر مذكور. ملاحظة الفنان ليست قياسًا.",
        "help": "المساعدة تذهب إلى المتحف", "help_p": "أزرار التبرع والتطوع تفتح المتحف الذي يحفظ الأحفورة. هذا الموقع مجاني ولا يطلب شيئًا لنفسه.",
        "h_who": "من يبني هذا",
        "founder": "المؤسس", "founder_p": "يحدد الاتجاه ويوافق على الصفحات.",
        "si": "SI", "si_p": "يبحث ويصوغ ويراجع المصادر. سطر الاعتماد هو Created by the Founder and SI.",
        "vol": "المتطوعون", "vol_p": "تصحيحات اللغة مرحب بها على",
        "h_src": "مصادر مذكورة في هذا الموقع",
        "src_intro": "هذه مصادر تربطها الصفحات بالفعل. الرابط ليس تأييدًا ولا شراكة. هذه القائمة لا تحصي الصفحات.",
        "h_rest": "هذا الموقع وموقعه الشقيق",
        "sister": "الموقع الشقيق", "sister_p": "Before Saving Planets ليس لديه برنامج رعاة ولا يسرد شركاء. رابط المتحف استشهاد أو طريقة لمساعدة ذلك المتحف، وليس شراكة.",
        "analytics": "القياس", "analytics_p": "الصفحة الرئيسية ومن نحن وتعلّم وصفحات البالغين الأخرى تحمّل Cloudflare Web Analytics. الأطفال وخريطة الأطفال لا يحمّلان هذا السكربت.",
        "news": "النشرة", "news_p": "صفحات البالغين قد تعرض التسجيل في النشرة. الأطفال وخريطة الأطفال لا يعرضان النموذج ولا يرسلان إشارة الزيارة.",
        "use": "الاستخدام", "use_p": "اقرأوا الصفحات في الصف. صور الغير تبقي الاعتماد مطبوعًا بجانبها. الصور والأفلام المصنوعة لهذا الموقع تحمل Created by the Founder and SI.",
    }
    T["it"] = {
        "lead": "La Terra antica, la geologia, l’archeologia e la storia della vita.",
        "blurb": "Una pagina finita collega un’affermazione a un articolo, un museo, un servizio geologico o una pagina di un parco. Questo sito non inventa una lunghezza del corpo e non disegna una Terra a cartoni.",
        "h_site": "Before Saving Planets",
        "aim": "Lo scopo", "aim_p": "Mostrare il registro fossile in linguaggio chiaro, con la fonte accanto all’affermazione. Nessuna lunghezza del corpo inventata. Nessuna Terra a cartoni.",
        "cover": "Che cosa copriamo",
        "mission": "La missione", "mission_p": "Saving Planets mostra soluzioni per il mondo vivente. Questo sito mostra il registro su cui poggiano: climi, ecosistemi e vita nel tempo profondo.",
        "write": "Scriveteci",
        "h_rules": "Come una pagina guadagna il suo posto",
        "src": "Una fonte che si può aprire", "src_p": "Una data o un’affermazione su una pagina finita rimanda a un articolo, un museo, un servizio geologico o una pagina di un parco.",
        "pic": "Un’immagine è didascalizzata", "pic_p": "Una fotografia dice chi l’ha fatta. Una ricostruzione d’artista dice Created by the Founder and SI. Una mappa dice quale modello ha tracciato le coste.",
        "len": "Nessuna misura inventata", "len_p": "Una lunghezza del corpo compare solo se una fonte citata la dà. Una nota di un artista non è una misura.",
        "help": "L’aiuto va al museo", "help_p": "I pulsanti di donazione e volontariato aprono il museo che conserva il fossile. Questo sito è gratuito e non chiede nulla per sé.",
        "h_who": "Chi costruisce questo",
        "founder": "Il fondatore", "founder_p": "Stabilisce la direzione e approva le pagine.",
        "si": "SI", "si_p": "Ricerca, scrive e controlla le fonti. La riga di credito è Created by the Founder and SI.",
        "vol": "Volontari", "vol_p": "Le correzioni linguistiche sono benvenute a",
        "h_src": "Fonti nominate su questo sito",
        "src_intro": "Sono fonti che le pagine già collegano. Un collegamento non è un avallo né una partnership. Questo elenco non conta le pagine.",
        "h_rest": "Questo sito e il suo gemello",
        "sister": "Sito gemello", "sister_p": "Before Saving Planets non ha un programma di sponsor e non elenca partner. Un collegamento a un museo è una citazione o un modo per aiutare quel museo, non una partnership.",
        "analytics": "Analisi", "analytics_p": "Home, Chi siamo, Impara e le altre pagine per adulti caricano Cloudflare Web Analytics. Bambini e la mappa dei bambini non caricano quello script.",
        "news": "Bollettino", "news_p": "Le pagine per adulti possono mostrare l’iscrizione al bollettino. Bambini e la mappa dei bambini non mostrano il modulo e non inviano il segnale di visita.",
        "use": "Uso", "use_p": "Leggete le pagine in classe. Le immagini di terzi tengono il credito stampato accanto. Immagini e filmati fatti per questo sito portano Created by the Founder and SI.",
    }
    T["he"] = {
        "lead": "כדור הארץ הקדום, גאולוגיה, ארכאולוגיה ותולדות החיים.",
        "blurb": "עמוד גמור מקשר טענה למאמר, למוזיאון, לסקר או לעמוד של שירות פארק. האתר הזה אינו ממציא אורך גוף ואינו מצייר כדור ארץ מצויר.",
        "h_site": "Before Saving Planets",
        "aim": "המטרה", "aim_p": "להציג את תיעוד המאובנים בשפה פשוטה, עם המקור ליד הטענה. בלי אורך גוף מומצא. בלי כדור ארץ מצויר.",
        "cover": "מה אנחנו מכסים",
        "mission": "המשימה", "mission_p": "Saving Planets מציג פתרונות לעולם החי. האתר הזה מציג את התיעוד שעליו הם יושבים: אקלים, מערכות אקולוגיות וחיים לאורך הזמן העמוק.",
        "write": "כתבו אלינו",
        "h_rules": "איך עמוד זוכה למקומו",
        "src": "מקור שאפשר לפתוח", "src_p": "תאריך או טענה בעמוד גמור מקשרים למאמר, למוזיאון, לסקר או לעמוד של שירות פארק.",
        "pic": "לתמונה יש קרדיט", "pic_p": "צילום אומר מי עשה אותו. שחזור אמן אומר Created by the Founder and SI. מפה אומרת איזה מודל שרטט את החופים.",
        "len": "בלי מידה מומצאת", "len_p": "אורך גוף מופיע רק כשמקור מצוטט נותן אותו. הערה של אמן אינה מדידה.",
        "help": "העזרה הולכת למוזיאון", "help_p": "כפתורי תרומה והתנדבות פותחים את המוזיאון ששומר את המאובן. האתר חינם ואינו מבקש דבר לעצמו.",
        "h_who": "מי בונה את זה",
        "founder": "המייסד", "founder_p": "קובע את הכיוון ומאשר את העמודים.",
        "si": "SI", "si_p": "חוקר, מנסח ובודק את המקורות. שורת הקרדיט היא Created by the Founder and SI.",
        "vol": "מתנדבים", "vol_p": "תיקוני שפה יתקבלו בברכה ב",
        "h_src": "מקורות שנזכרים באתר",
        "src_intro": "אלה מקורות שהעמודים כבר מקשרים אליהם. קישור אינו המלצה ואינו שותפות. הרשימה הזאת אינה סופרת עמודים.",
        "h_rest": "האתר הזה ואתר האחות",
        "sister": "אתר אחות", "sister_p": "ל-Before Saving Planets אין תוכנית חסויות והוא אינו מפרט שותפים. קישור למוזיאון הוא ציטוט או דרך לעזור לאותו מוזיאון, לא שותפות.",
        "analytics": "מדידה", "analytics_p": "הבית, אודות, לימוד ושאר עמודי המבוגרים טוענים את Cloudflare Web Analytics. ילדים ומפת הילדים אינם טוענים את הסקריפט.",
        "news": "ידיעון", "news_p": "עמודי מבוגרים יכולים להציג הרשמה לידיעון. ילדים ומפת הילדים אינם מציגים את הטופס ואינם שולחים את אות הביקור.",
        "use": "שימוש", "use_p": "קראו את העמודים בכיתה. תמונות של צד שלישי שומרות את הקרדיט לידן. תמונות וסרטים שנעשו לאתר הזה נושאים Created by the Founder and SI.",
    }
    x = T[lang]
    aim = _cards([
        (x["aim"], _e(x["aim_p"])),
        (x["cover"], routes[lang]),
        (x["mission"], _e(x["mission_p"])),
        (x["write"], mail + ". " + note),
    ])
    rules = _cards([
        (x["src"], _e(x["src_p"])),
        (x["pic"], _e(x["pic_p"])),
        (x["len"], _e(x["len_p"])),
        (x["help"], _e(x["help_p"])),
    ])
    team = (
        '<div class="ws-grid">'
        f'<div class="w-card"><h3>{_e(x["founder"])}</h3><p>{_e(x["founder_p"])}</p></div>'
        f'<div class="w-card"><h3>{_e(x["si"])}</h3><p>{_e(x["si_p"])}</p></div>'
        f'<div class="w-card"><h3>{_e(x["vol"])}</h3><p>{_e(x["vol_p"])} {mail}.</p></div>'
        '</div><p class="team-credit">Created by the Founder and SI</p>'
    )
    sources = _cards([
        (name, f'{_e(line)} <a href="{html.escape(url, quote=True)}">{_e(name)}</a>')
        for name, url, line in about_pages.SOURCES
    ])
    rest = _cards([
        (x["sister"], f'<a href="https://www.savingplanets.com/">www.savingplanets.com</a>. {_e(x["sister_p"])}'),
        (x["analytics"], _e(x["analytics_p"])),
        (x["news"], _e(x["news_p"])),
        (x["use"], _e(x["use_p"])),
    ])
    return (
        f'<section class="diff-strip" aria-label="{_e(x["lead"])}"><p class="diff-lead">{_e(x["lead"])}</p>'
        f'<p class="diff-body">{_e(x["blurb"])}</p></section>'
        f'<section class="five-ws" id="record"><h2>{_e(x["h_site"])}</h2>{aim}</section>'
        f'<section class="five-ws" id="rules"><h2>{_e(x["h_rules"])}</h2>{rules}</section>'
        f'<section class="five-ws" id="team"><h2>{_e(x["h_who"])}</h2>{team}</section>'
        f'<section class="five-ws" id="sources"><h2>{_e(x["h_src"])}</h2><p>{_e(x["src_intro"])}</p>{sources}</section>'
        f'<section class="five-ws" id="sister"><h2>{_e(x["h_rest"])}</h2>{rest}</section>'
    )


def _contact(lang):
    x = {
        "en": ("Write to the address this site already uses.", "Questions, corrections, and reuse.", "About this site", "Ways to help a museum", "Search the notes on this site"),
        "fr": ("Écrivez à l’adresse que ce site utilise déjà.", "Questions, corrections et réutilisation.", "À propos de ce site", "Aider un musée", "Chercher les notes de ce site"),
        "es": ("Escriban a la dirección que este sitio ya usa.", "Preguntas, correcciones y reutilización.", "Acerca de este sitio", "Ayudar a un museo", "Buscar las notas de este sitio"),
        "ar": ("اكتبوا إلى العنوان الذي يستخدمه هذا الموقع بالفعل.", "أسئلة وتصحيحات وإعادة استخدام.", "عن هذا الموقع", "مساعدة متحف", "البحث في ملاحظات هذا الموقع"),
        "it": ("Scrivete all’indirizzo che questo sito usa già.", "Domande, correzioni e riutilizzo.", "Informazioni su questo sito", "Aiutare un museo", "Cercare le note di questo sito"),
        "he": ("כתבו לכתובת שהאתר הזה כבר משתמש בה.", "שאלות, תיקונים ושימוש חוזר.", "על האתר הזה", "עזרה למוזיאון", "חיפוש בהערות של האתר הזה"),
    }[lang]
    lead, title, about, help, search = x
    return (
        f'<section class="diff-strip" aria-label="{_e(lead)}"><p class="diff-lead">{_e(lead)}</p>'
        f'<p class="diff-body">{_mail()}. {_e(MAIL_NOTE[lang])}</p></section>'
        f'<section class="five-ws" id="write"><h2>{_e(title)}</h2><div class="ws-grid">'
        f'<div class="w-card"><h3>{_e(about)}</h3><p><a href="About.html">About</a></p></div>'
        f'<div class="w-card"><h3>{_e(help)}</h3><p><a href="Ways_to_Help.html">Ways to Help</a></p></div>'
        f'<div class="w-card"><h3>{_e(search)}</h3><p><a href="Search.html">Search</a></p></div>'
        f'</div></section>'
    )


def story(page, lang):
    return SUB[page][lang], _about(lang) if page == "About" else _contact(lang)
