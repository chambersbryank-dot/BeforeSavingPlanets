#!/usr/bin/env python3
"""Before Saving Planets scaffold generator. Builds 6 languages x pages from STRINGS below.
Everything marked PLACEHOLDER is review copy, not researched content."""
import json, os, html, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from deep import DEEP, HOT, CR
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOM = "https://www.beforesavingplanets.com"
LANGS = ["en","fr","es","ar","it","he"]
RTL = {"ar","he"}
NAMES = {"en":("EN","English"),"fr":("FR","Français"),"es":("ES","Español"),"ar":("عربي","العربية"),"it":("IT","Italiano"),"he":("עב","עברית")}
PAGES = ["index","Quest","Continents","Oceans","Seas","DeadSea","About","Contact","World_Map","Kids_Map","Ways_to_Help","Search","Myth_vs_Fact","Learn","Kids","Teachers"]
EXTRA = {"en":("Myth vs Fact","Learn","Kids","Teachers","Where our facts will come from","We start with these institutions and will add other world museums later. Every claim will cite its source."),
"fr":("Mythe ou réalité","Apprendre","Enfants","Enseignants","D’où viendront nos faits","Nous commençons par ces institutions et ajouterons d’autres musées du monde. Chaque affirmation citera sa source."),
"es":("Mito o realidad","Aprender","Niños","Docentes","De dónde vendrán nuestros datos","Empezamos con estas instituciones y añadiremos otros museos del mundo. Cada afirmación citará su fuente."),
"ar":("خرافة أم حقيقة","تعلّم","الأطفال","المعلمون","من أين ستأتي معلوماتنا","نبدأ بهذه المؤسسات وسنضيف متاحف عالمية أخرى لاحقاً. كل معلومة ستذكر مصدرها."),
"it":("Mito o realtà","Impara","Bambini","Insegnanti","Da dove verranno i nostri fatti","Partiamo da queste istituzioni e aggiungeremo altri musei del mondo. Ogni affermazione citerà la sua fonte."),
"he":("מיתוס מול עובדה","למידה","ילדים","מורים","מאיפה יגיעו העובדות שלנו","נתחיל במוסדות האלה ונוסיף בהמשך מוזיאונים נוספים מהעולם. כל טענה תצוטט עם מקור.")}
SOURCES=[("Smithsonian National Museum of Natural History","https://naturalhistory.si.edu/"),("Natural History Museum, London","https://www.nhm.ac.uk/"),("Yale Peabody Museum","https://peabody.yale.edu/"),("UC Museum of Paleontology, Berkeley","https://ucmp.berkeley.edu/"),("NASA Earth Observatory","https://earthobservatory.nasa.gov/")]
T = {
"en": dict(brand="Before Saving Planets", home="Home", about="About", contact="Contact", map="World Map", kids="Kids Fossil Map", help="Ways to Help", search="Search", sister="Sister site: Saving Planets",
  kicker="WHERE IT ALL BEGINS", h1a="Where Earth’s", h1b="Story Begins", sub="Fossils, ancient climates and lost ecosystems — and what they can teach us about healing our planet today.",
  cta1="Explore the fossil map", cta2="Visit Saving Planets", hook="Saving Planets finds solutions without the doom. Before Saving Planets is where Earth’s story begins.",
  ph="Placeholder — content coming soon. This page is a scaffold for review; research and sourced content will be added next.",
  t_about="About Before Saving Planets", d_about="A sister site to Saving Planets, focused on deep time: how fossils record past climates and ecosystems, and how that record can inform solutions today.",
  t_contact="Contact us", d_contact="Questions, corrections or ideas? We’d love to hear from you.", t_map="Fossil sites around the world", d_map="An interactive map of fossil sites. Placeholder pins for review; each will link to a sourced page.",
  t_kids="Kids Fossil Map", d_kids="Tap a bubble to travel back in time. Fun facts will be added after research.", t_help="Ways to Help", d_help="Ways to help will be listed here: citizen science, museum volunteering and responsible fossil collecting.",
  t_search="Search", d_search="Search across Before Saving Planets (coming soon).", eras="Eras (placeholder)", credit="Hero art: SI and Biological SI Partner created (illustrative, not a scientific reconstruction).",
  pin="Placeholder pin — sourced page coming soon", north="Look up here for older stories!", bubbles=["Trilobites","Ancient ferns","Amber","Dinosaurs","Ice Age","Ancient reefs"], email="hello@savingplanets.com", foot="A sister site of", pause="Pause animation"),
"fr": dict(brand="Before Saving Planets", home="Accueil", about="À propos", contact="Contact", map="Carte du monde", kids="Carte des fossiles (enfants)", help="Comment aider", search="Rechercher", sister="Site jumeau : Saving Planets",
  kicker="LÀ OÙ TOUT COMMENCE", h1a="Là où commence", h1b="l’histoire de la Terre", sub="Fossiles, climats anciens et écosystèmes disparus — et ce qu’ils peuvent nous apprendre pour soigner notre planète aujourd’hui.",
  cta1="Explorer la carte des fossiles", cta2="Visiter Saving Planets", hook="Saving Planets trouve des solutions sans catastrophisme. Before Saving Planets, c’est là où commence l’histoire de la Terre.",
  ph="Contenu provisoire — bientôt disponible. Cette page est une maquette à relire ; le contenu sourcé sera ajouté ensuite.",
  t_about="À propos de Before Saving Planets", d_about="Un site jumeau de Saving Planets consacré au temps profond : ce que les fossiles révèlent des climats et écosystèmes passés, et comment cela peut éclairer les solutions d’aujourd’hui.",
  t_contact="Nous contacter", d_contact="Questions, corrections ou idées ? Écrivez-nous.", t_map="Sites fossilifères du monde", d_map="Carte interactive des sites fossilifères. Repères provisoires à relire.",
  t_kids="Carte des fossiles pour enfants", d_kids="Touche une bulle pour remonter le temps. Les anecdotes arriveront après nos recherches.", t_help="Comment aider", d_help="Les façons d’aider seront listées ici : science participative, bénévolat en musée, collecte responsable.",
  t_search="Rechercher", d_search="Recherche sur Before Saving Planets (bientôt).", eras="Ères (provisoire)", credit="Illustration : créée par SI et Biological SI Partner (illustrative, pas une reconstitution scientifique).",
  pin="Repère provisoire — page sourcée à venir", north="Regarde ici pour des histoires plus anciennes !", bubbles=["Trilobites","Fougères anciennes","Ambre","Dinosaures","Ère glaciaire","Récifs anciens"], email="hello@savingplanets.com", foot="Un site jumeau de", pause="Mettre en pause"),
"es": dict(brand="Before Saving Planets", home="Inicio", about="Acerca de", contact="Contacto", map="Mapa mundial", kids="Mapa de fósiles (niños)", help="Cómo ayudar", search="Buscar", sister="Sitio hermano: Saving Planets",
  kicker="DONDE TODO COMIENZA", h1a="Donde comienza", h1b="la historia de la Tierra", sub="Fósiles, climas antiguos y ecosistemas perdidos, y lo que pueden enseñarnos para sanar nuestro planeta hoy.",
  cta1="Explorar el mapa de fósiles", cta2="Visitar Saving Planets", hook="Saving Planets encuentra soluciones sin catastrofismo. Before Saving Planets es donde comienza la historia de la Tierra.",
  ph="Contenido provisional: próximamente. Esta página es una maqueta para revisión; después se añadirá contenido con fuentes.",
  t_about="Acerca de Before Saving Planets", d_about="Un sitio hermano de Saving Planets centrado en el tiempo profundo: cómo los fósiles registran climas y ecosistemas pasados y cómo ese registro puede orientar las soluciones de hoy.",
  t_contact="Contáctanos", d_contact="¿Preguntas, correcciones o ideas? Escríbenos.", t_map="Yacimientos de fósiles del mundo", d_map="Mapa interactivo de yacimientos. Marcadores provisionales para revisión.",
  t_kids="Mapa de fósiles para niños", d_kids="Toca una burbuja para viajar en el tiempo. Los datos curiosos llegarán tras investigar.", t_help="Cómo ayudar", d_help="Aquí aparecerán formas de ayudar: ciencia ciudadana, voluntariado en museos y recolección responsable.",
  t_search="Buscar", d_search="Búsqueda en Before Saving Planets (próximamente).", eras="Eras (provisional)", credit="Arte: creado por SI y Biological SI Partner (ilustrativo, no es una reconstrucción científica).",
  pin="Marcador provisional: página con fuentes próximamente", north="¡Mira aquí para historias más antiguas!", bubbles=["Trilobites","Helechos antiguos","Ámbar","Dinosaurios","Edad de Hielo","Arrecifes antiguos"], email="hello@savingplanets.com", foot="Un sitio hermano de", pause="Pausar animación"),
"ar": dict(brand="Before Saving Planets", home="الرئيسية", about="من نحن", contact="اتصل بنا", map="خريطة العالم", kids="خريطة الأحافير للأطفال", help="طرق المساعدة", search="بحث", sister="الموقع الشقيق: Saving Planets",
  kicker="حيث تبدأ الحكاية", h1a="حيث تبدأ", h1b="قصة الأرض", sub="أحافير ومناخات قديمة ونظم بيئية مفقودة، وما يمكن أن تعلّمنا إياه لنداوي كوكبنا اليوم.",
  cta1="استكشف خريطة الأحافير", cta2="زر Saving Planets", hook="يجد Saving Planets حلولاً بلا تهويل. وBefore Saving Planets هو حيث تبدأ قصة الأرض.",
  ph="محتوى مؤقت — قريباً. هذه الصفحة نموذج للمراجعة، وسيُضاف المحتوى الموثّق لاحقاً.",
  t_about="عن Before Saving Planets", d_about="موقع شقيق لـ Saving Planets يركّز على الزمن العميق: كيف تسجّل الأحافير مناخات ونظماً بيئية سابقة، وكيف يمكن لهذا السجل أن يرشد حلول اليوم.",
  t_contact="اتصل بنا", d_contact="أسئلة أو تصحيحات أو أفكار؟ يسعدنا أن نسمع منك.", t_map="مواقع الأحافير حول العالم", d_map="خريطة تفاعلية لمواقع الأحافير. علامات مؤقتة للمراجعة.",
  t_kids="خريطة الأحافير للأطفال", d_kids="اضغط على فقاعة لتعود بالزمن. ستضاف الحقائق الممتعة بعد البحث.", t_help="طرق المساعدة", d_help="ستُدرج هنا طرق المساعدة: علم المواطن، والتطوع في المتاحف، والجمع المسؤول للأحافير.",
  t_search="بحث", d_search="البحث في Before Saving Planets (قريباً).", eras="العصور (مؤقت)", credit="الرسم: من إنشاء SI وBiological SI Partner (توضيحي، وليس إعادة بناء علمية).",
  pin="علامة مؤقتة — صفحة موثّقة قريباً", north="انظر هنا لقصص أقدم!", bubbles=["ثلاثيات الفصوص","سراخس قديمة","كهرمان","ديناصورات","العصر الجليدي","شعاب قديمة"], email="hello@savingplanets.com", foot="موقع شقيق لـ", pause="إيقاف الحركة"),
"it": dict(brand="Before Saving Planets", home="Home", about="Chi siamo", contact="Contatti", map="Mappa del mondo", kids="Mappa dei fossili (bambini)", help="Come aiutare", search="Cerca", sister="Sito gemello: Saving Planets",
  kicker="DOVE TUTTO HA INIZIO", h1a="Dove inizia", h1b="la storia della Terra", sub="Fossili, climi antichi ed ecosistemi perduti, e ciò che possono insegnarci per curare il nostro pianeta oggi.",
  cta1="Esplora la mappa dei fossili", cta2="Visita Saving Planets", hook="Saving Planets trova soluzioni senza catastrofismo. Before Saving Planets è dove inizia la storia della Terra.",
  ph="Contenuto provvisorio: in arrivo. Questa pagina è una bozza da rivedere; i contenuti con fonti verranno aggiunti dopo.",
  t_about="Chi è Before Saving Planets", d_about="Un sito gemello di Saving Planets dedicato al tempo profondo: come i fossili registrano climi ed ecosistemi del passato e come questa memoria può guidare le soluzioni di oggi.",
  t_contact="Contattaci", d_contact="Domande, correzioni o idee? Scrivici.", t_map="Siti fossili nel mondo", d_map="Mappa interattiva dei siti fossili. Segnaposto provvisori da rivedere.",
  t_kids="Mappa dei fossili per bambini", d_kids="Tocca una bolla per viaggiare nel tempo. Le curiosità arriveranno dopo la ricerca.", t_help="Come aiutare", d_help="Qui elencheremo i modi per aiutare: citizen science, volontariato nei musei e raccolta responsabile.",
  t_search="Cerca", d_search="Ricerca su Before Saving Planets (in arrivo).", eras="Ere (provvisorio)", credit="Illustrazione: creata da SI e Biological SI Partner (illustrativa, non una ricostruzione scientifica).",
  pin="Segnaposto provvisorio: pagina con fonti in arrivo", north="Guarda qui per storie più antiche!", bubbles=["Trilobiti","Felci antiche","Ambra","Dinosauri","Era glaciale","Barriere antiche"], email="hello@savingplanets.com", foot="Un sito gemello di", pause="Metti in pausa"),
"he": dict(brand="Before Saving Planets", home="בית", about="אודות", contact="צור קשר", map="מפת העולם", kids="מפת מאובנים לילדים", help="איך לעזור", search="חיפוש", sister="אתר אחות: Saving Planets",
  kicker="היכן שהכול מתחיל", h1a="היכן שמתחיל", h1b="סיפורו של כדור הארץ", sub="מאובנים, אקלים קדום ומערכות אקולוגיות שאבדו, ומה הם יכולים ללמד אותנו כדי לרפא את כוכב הלכת שלנו היום.",
  cta1="גלו את מפת המאובנים", cta2="בקרו ב-Saving Planets", hook="Saving Planets מוצא פתרונות בלי אווירת אבדון. Before Saving Planets הוא המקום שבו מתחיל סיפורו של כדור הארץ.",
  ph="תוכן זמני — בקרוב. דף זה הוא שלד לבדיקה; תוכן עם מקורות יתווסף בהמשך.",
  t_about="אודות Before Saving Planets", d_about="אתר אחות של Saving Planets המתמקד בזמן העמוק: כיצד מאובנים מתעדים אקלים ומערכות אקולוגיות של העבר, וכיצד התיעוד הזה יכול להנחות פתרונות כיום.",
  t_contact="צרו קשר", d_contact="שאלות, תיקונים או רעיונות? נשמח לשמוע.", t_map="אתרי מאובנים ברחבי העולם", d_map="מפה אינטראקטיבית של אתרי מאובנים. סמנים זמניים לבדיקה.",
  t_kids="מפת מאובנים לילדים", d_kids="הקישו על בועה כדי לחזור בזמן. עובדות מעניינות יתווספו אחרי המחקר.", t_help="איך לעזור", d_help="כאן יופיעו דרכים לעזור: מדע אזרחי, התנדבות במוזיאונים ואיסוף אחראי.",
  t_search="חיפוש", d_search="חיפוש ב-Before Saving Planets (בקרוב).", eras="תקופות (זמני)", credit="איור: נוצר על ידי SI ו-Biological SI Partner (להמחשה, לא שחזור מדעי).",
  pin="סמן זמני — דף עם מקורות בקרוב", north="הביטו כאן לסיפורים עתיקים יותר!", bubbles=["טרילוביטים","שרכים קדומים","ענבר","דינוזאורים","עידן הקרח","שוניות קדומות"], email="hello@savingplanets.com", foot="אתר אחות של", pause="השהיית אנימציה"),
}
# Well-known fossil localities (location names only; no claims). Placeholder pins for review.
SITES = [("Burgess Shale, British Columbia, Canada",51.43,-116.47),("Messel Pit, Germany",49.92,8.75),("Dinosaur Provincial Park, Alberta, Canada",50.76,-111.49),
 ("La Brea Tar Pits, Los Angeles, USA",34.063,-118.356),("Chengjiang-adjacent: Ediacara Hills, South Australia",-30.8,138.15),("Wadi Al-Hitan, Egypt",29.27,30.04),("Ischigualasto, Argentina",-30.0,-67.9),("Monte San Giorgio, Switzerland/Italy",45.9,8.95)]
SITES[4]=("Ediacara Hills, South Australia",-30.8,138.15)

def rel(lang): return "" if lang=="en" else "../"
def url(lang,page): return DOM+"/"+("" if lang=="en" else lang+"/")+("" if page=="index" else page+".html")

def nav(lang,page):
    t=T[lang]; X=EXTRA[lang]; r=rel(lang); sw=""
    for L in LANGS:
        c,n=NAMES[L]; href=("" if L=="en" else ("" if lang!="en" else "")+L+"/") 
        href=(r if lang!="en" else "")+("" if L=="en" else L+"/")+page+".html"
        cur=' aria-current="true"' if L==lang else ""
        sw+=f'<a class="spn-ls" role="switch" aria-checked="{str(L==lang).lower()}" href="{href}" hreflang="{L}" lang="{L}"{cur} aria-label="{n}" title="{n}" data-lang="{L}"><span class="spn-ls-t" aria-hidden="true"><span class="spn-ls-k"></span></span><span class="spn-ls-c" aria-hidden="true">{c}</span><span class="spn-ls-n" aria-hidden="true">{n}</span></a>'
    return f'''<nav id="topnav"><div class="spn"><a class="spn-brand" href="index.html"><span class="spn-logo"><img src="{r}assets/brand/sp-logo-72.png" srcset="{r}assets/brand/sp-logo-72.png 1x, {r}assets/brand/sp-logo-144.png 2x" width="72" height="72" alt="{t['brand']} logo (placeholder: Saving Planets logo)"></span>{t['brand']}</a><button type="button" class="spn-toggle" aria-expanded="false" aria-controls="spn-panel" aria-label="Menu" data-open="Menu" data-close="Close"><span></span><span></span><span></span></button><div class="spn-panel" id="spn-panel"><ul class="spn-util" aria-label="Site links"><li class="lang-switch"><span class="spn-lt" role="group" aria-label="Language">{sw}</span></li><li><a href="Search.html">{t['search']}</a></li><li><a href="Contact.html">{t['contact']}</a></li><li><a href="https://www.savingplanets.com/">{t['sister']}</a></li></ul><ul class="spn-main" aria-label="Main menu"><li><a href="index.html">{t['home']}</a></li><li><a href="Quest.html">Dig Quest</a></li><li><a href="World_Map.html">{t['map']}</a></li><li><a href="Kids_Map.html">{t['kids']}</a></li><li><a href="Learn.html">{X[1]}</a></li><li><a href="Kids.html">{X[2]}</a></li><li><a href="Teachers.html">{X[3]}</a></li><li><a href="Myth_vs_Fact.html">{X[0]}</a></li><li><a href="Ways_to_Help.html">{t['help']}</a></li><li><a href="About.html">{t['about']}</a></li></ul></div></div></nav>'''

TAGLINE={
"en":("Built on your ideas — so every lesson, search, and discovery here stays free, clear, sourced, and world-class for every classroom and family.","Why trust it: our 4.5-billion-year Earth voyage is cross-checked against NASA, Yale, Harvard, MIT, and other leading universities and scholars.","Our sources"),
"fr":("Construit à partir de vos idées — pour que chaque leçon, recherche et découverte reste gratuite, claire, sourcée et de classe mondiale pour chaque classe et chaque famille.","Pourquoi nous faire confiance : notre voyage de 4,5 milliards d’années est vérifié en croisant NASA, Yale, Harvard, MIT et d’autres grandes universités et chercheurs.","Nos sources"),
"es":("Creado a partir de sus ideas, para que cada lección, búsqueda y descubrimiento siga siendo gratuito, claro, con fuentes y de nivel mundial para cada aula y cada familia.","Por qué confiar: nuestro viaje de 4.500 millones de años se contrasta con la NASA, Yale, Harvard, el MIT y otras grandes universidades y académicos.","Nuestras fuentes"),
"ar":("مبني على أفكاركم — ليبقى كل درس وبحث واكتشاف هنا مجانيًا وواضحًا وموثّق المصادر وبمستوى عالمي لكل صف دراسي ولكل أسرة.","لماذا تثق بنا: رحلتنا عبر 4.5 مليار سنة من تاريخ الأرض تُراجَع بالمقارنة مع ناسا وييل وهارفارد ومعهد MIT وغيرها من كبرى الجامعات والعلماء.","مصادرنا"),
"it":("Costruito sulle vostre idee, perché ogni lezione, ricerca e scoperta resti gratuita, chiara, documentata e di livello mondiale per ogni classe e ogni famiglia.","Perché fidarsi: il nostro viaggio di 4,5 miliardi di anni è verificato incrociando NASA, Yale, Harvard, MIT e altre grandi università e studiosi.","Le nostre fonti"),
"he":("נבנה על בסיס הרעיונות שלכם — כדי שכל שיעור, חיפוש וגילוי כאן יישארו חינמיים, ברורים, מבוססי מקורות וברמה עולמית לכל כיתה ולכל משפחה.","למה לסמוך עלינו: המסע שלנו בן 4.5 מיליארד השנים נבדק מול נאס\"א, ייל, הרווארד, MIT ואוניברסיטאות וחוקרים מובילים נוספים.","המקורות שלנו"),
}
def tagline(lang):
    a,b,c=TAGLINE[lang]; sp="https://www.savingplanets.com/"+("" if lang=="en" else lang+"/")+"Editorial_Policy.html"
    return f'<p class="footer-tagline" style="max-width:720px;margin:0 auto .9rem;text-align:center;font-style:italic;opacity:.9">{a}<br><span style="font-style:normal;font-size:.9em">{b} <a href="{sp}">{c}</a></span></p>'
def footer(lang):
    t=T[lang]; X=EXTRA[lang]
    return f'''<footer>{tagline(lang)}<div class="footer-map" role="navigation" aria-label="Site map"><div class="fm-col"><h2 class="fm-h">{t['brand']}</h2><ul><li><a href="index.html">{t['home']}</a></li><li><a href="World_Map.html">{t['map']}</a></li><li><a href="Kids_Map.html">{t['kids']}</a></li><li><a href="Ways_to_Help.html">{t['help']}</a></li><li><a href="Search.html">{t['search']}</a></li><li><a href="Learn.html">{X[1]}</a></li><li><a href="Kids.html">{X[2]}</a></li><li><a href="Teachers.html">{X[3]}</a></li><li><a href="Myth_vs_Fact.html">{X[0]}</a></li><li><a href="About.html">{t['about']}</a></li><li><a href="Contact.html">{t['contact']}</a></li></ul></div></div><p class="bsp-hook">{t['hook']}</p><p>&copy; 2026 Before Saving Planets • {t['foot']} <a href="https://www.savingplanets.com/">www.savingplanets.com</a></p><p class="dept-foot"><a href="mailto:{t['email']}">{t['email']}</a></p><p class="logo-credit">Logo created by SI and Biological SI Partner</p></footer>'''

def head(lang,page,title,desc,extra=""):
    r=rel(lang); alts="".join(f'<link rel="alternate" hreflang="{L}" href="{url(L,page)}">' for L in LANGS)
    # Home only: the lava first frame. The mp4 is chosen in bsp-hero.js after first paint.
    # end.webp is the reduced-motion still (Earth today), so only that preference preloads it.
    pre=('<link rel="preload" href="/assets/hero/morph/start.webp" as="image" fetchpriority="high" media="(prefers-reduced-motion: no-preference)">'
         '<link rel="preload" href="/assets/hero/morph/end.webp" as="image" fetchpriority="high" media="(prefers-reduced-motion: reduce)">') if page=="index" else ""
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if lang in RTL else 'ltr'}" class="dark">
<head>
<meta charset="UTF-8"><meta name="color-scheme" content="dark"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,follow"><!-- SCAFFOLD: flip to index,follow at launch -->
<link rel="canonical" href="{url(lang,page)}">{alts}<link rel="alternate" hreflang="x-default" href="{url('en',page)}">
<title>{html.escape(title)} | Before Saving Planets</title><meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)} | Before Saving Planets"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url(lang,page)}"><meta property="og:type" content="website"><meta property="og:site_name" content="Before Saving Planets"><meta name="twitter:card" content="summary">
<link rel="icon" href="{r}favicon.ico"><link rel="icon" type="image/png" sizes="32x32" href="{r}assets/brand/favicon-32.png"><link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest"><meta name="theme-color" content="#2a1a0e">
<link rel="preload" href="{r}assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
{pre}<link rel="stylesheet" href="{r}styles.css"><link rel="stylesheet" href="{r}extras.css"><link rel="stylesheet" href="{r}bsp.css">{extra}
</head>
'''

def body(lang,page,main,cls="toc-sub",scripts=""):
    r=rel(lang)
    # BEACON: set CF Web Analytics token for beforesavingplanets.com here when created
    return f'''<body class="{cls}" data-glass-tint="site"><a class="skip-link" href="#main">Skip</a>
{nav(lang,page)}
{main}
{footer(lang)}
<script src="{r}site.js"></script>{scripts}
</body></html>'''

HERO_SVG = open(os.path.join(ROOT,"scripts","hero.html")).read()

def page_hero(title,desc,t):
    return f'<section class="page-hero bsp-page-hero"><div class="bsp-strata" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div><div class="page-hero-content"><h1>{title}</h1><p>{desc}</p></div></section>'

def placeholder(t,n=3):
    return '<div class="edu-wrap bsp-wrap">'+f'<p class="bsp-ph" role="note">⚠ {t["ph"]}</p>'+"".join(f'<section class="bsp-card"><h2>[Placeholder section {i}]</h2><p>{t["ph"]}</p></section>' for i in range(1,n+1))+f'<p class="bsp-hook">{t["hook"]}</p></div>'


# ---- Dig Quest (English copy; other languages TODO machine-draft translation) ----
QCTA="Start the Dig Quest"
HCRED="Artist’s interpretation — 10-second morph made with SI (AI rendering) and Biological SI Partner; science based on NASA &amp; USGS (not real footage)."
SP="https://www.savingplanets.com/"
LAYERS=[
 ("Earth forms","4.54 billion years ago","#7a2a12","🪨",
  "Dust and gas around the young Sun clumped into rocks, the rocks collided and merged, and Earth grew. Scientists date Earth to 4.54 billion years (less than 1% uncertainty) using lead isotopes and meteorites.",
  [("USGS — Age of the Earth","https://pubs.usgs.gov/gip/geotime/age.html"),("NASA — Formation of the Solar System","https://mobile.arc.nasa.gov/public/iexplore/missions/pages/yss/november.html")],
  "NASA/JPL-Caltech artist’s concept of a dusty planet-forming disk (public domain) — Bryan to pick","Earth healed from fire into a living world. See what we’re doing for it today.",("Today’s solutions",SP)),
 ("The Moon is born","about 4.5 billion years ago","#8a3b1c","🌕",
  "A Mars-size body called Theia likely struck young Earth. The debris formed the Moon. Apollo rocks show the Moon formed about 60 million years after the solar system began and was once covered by a magma ocean.",
  [("NASA Science — Moon Formation","https://science.nasa.gov/moon/formation/")],
  "NASA Apollo lunar sample photo (public domain)","The Moon drives our tides, which shape coasts and ocean life.",("Ocean solutions",SP+"Oceans.html")),
 ("First crust and water","4.4 billion years ago","#6e4526","💧",
  "A tiny zircon crystal from the Jack Hills of Western Australia is 4.404 billion years old — the oldest known piece of Earth. Its chemistry points to continental crust and liquid water very early on.",
  [("Wilde et al., Nature 409:175 (2001)","https://doi.org/10.1038/35051550")],
  "Jack Hills zircon image (license to verify) — Bryan to approve","Earth’s first oceans became today’s oceans. Help protect them.",("Ocean solutions",SP+"Oceans.html")),
 ("Oxygen arrives","about 2.4 billion years ago","#5b3820","🫧",
  "Tiny ocean microbes, likely ancestors of cyanobacteria, made oxygen by photosynthesis. Around 2.4 billion years ago oxygen built up in the air — the Great Oxidation Event — paving the way for complex life.",
  [("NASA Astrobiology — Great Oxidation Event","https://astrobiology.nasa.gov/news/oxygen-production-in-earths-early-oceans-predates-the-great-oxidation-event/"),("NOAA Climate.gov — Coldest Earth","https://www.climate.gov/news-features/climate-qa/whats-coldest-earths-ever-been")],
  "NPS photo of stromatolites (public domain) — Bryan to pick","Forests and ocean plants still make the oxygen we breathe.",("Forest solutions",SP+"Deforestation.html")),
 ("Life explodes in the sea","508 million years ago","#4a5a3a","🐚",
  "The Burgess Shale in the Canadian Rockies preserves soft-bodied sea animals from the Cambrian, 508 million years ago, recording the rapid diversification of life called the “Cambrian Explosion.” Charles Walcott collected some 65,000 specimens there for the Smithsonian.",
  [("Smithsonian Ocean — Ocean Through Time","https://www.ocean.si.edu/through-time/ocean-through-time")],
  "Smithsonian Open Access CC0 Burgess Shale specimen photo — Bryan to pick","Today’s reefs carry on those first ocean worlds.",("Coral reef restoration",SP+"Coral_Restoration_Foundation.html")),
 ("The Great Dying","about 252 million years ago","#3b2618","🌋",
  "The end-Permian extinction was the largest in Earth’s history: about 96% of species were lost. Massive volcanic eruptions in Siberia released carbon dioxide, linked to warming and ocean acidification. Life took millions of years to recover — but it did.",
  [("National Park Service — Mass Extinctions","https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm"),("Smithsonian NMNH — Extinction Over Time","https://naturalhistory.si.edu/education/teaching-resources/paleontology/extinction-over-time")],
  "NPS photo of Permian brachiopod fossils (public domain)","CO₂ and acidifying oceans are back. Reef rescuers are fighting it.",("Coral reef restoration",SP+"Coral_Restoration_Foundation.html")),
 ("Asteroid and recovery","66 million years ago","#2e2a3a","☄️",
  "An asteroid 10–20 km wide struck near today’s Yucatán, forming the Chicxulub crater. About 76% of species died out, including all dinosaurs except birds. Mammals then flourished.",
  [("National Park Service — Mass Extinctions","https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm")],
  "NASA radar image of the Chicxulub area (public domain)","After disasters, forests regrow. See who helps them today.",("Forest solutions",SP+"Deforestation.html")),
 ("The last Ice Age","20,000 years ago","#2a4a6a","🧊",
  "At the Last Glacial Maximum, about 20,000 years ago, ice sheets covered Canada and northern Europe and sea level was about 120 meters lower. Ice cores from Greenland and Antarctica record this climate history year by year.",
  [("NOAA Ocean Explorer — Paleoclimate","https://archive.oceanexplorer.noaa.gov/explorations/05stepstones/background/paleoclimate/paleoclimate.html"),("NASA — The Ice Core Record","https://science.nasa.gov/earth/earth-observatory/paleoclimatology-the-ice-core-record/")],
  "NASA ice core photo (public domain) — Bryan to pick","Ice holds Earth’s memory. Meet the people protecting the poles.",("Polar solutions",SP+"Polar.html")),
]
def hot(i):
    k=HOT.get(i,[])
    if not k: return ""
    return '<div class="q-hot" role="group" aria-label="Dig deeper">'+"".join(f'<a class="q-hotspot" href="{d}.html"><span class="q-pulse" aria-hidden="true"></span>🔎 Dig deeper: {DEEP[d][0]}</a>' for d in k)+'</div>'
def deep(lang,key):
    title,sub,img,cap,facts,src,(bt,bl,bu)=DEEP[key]; r=rel(lang)
    note="" if lang=="en" else '<p class="bsp-ph" role="note">TODO machine-draft translation: English for review.</p>'
    la="" if lang=="en" else ' lang="en"'
    fs="".join(f'<section class="bsp-card d-fact"><h2>{h}</h2><p>{b}</p></section>' for h,b in facts)
    cites="".join(f'<li><a href="{u}" rel="noopener">{a}</a></li>' for a,u in src)
    others="".join(f'<a class="q-hotspot" href="{k}.html">{v[0]}</a>' for k,v in DEEP.items() if k!=key)
    return (f'<main id="main">'+page_hero(title,sub,None)+f'<div class="edu-wrap bsp-wrap"{la}>{note}<figure class="d-fig"><img src="{r}assets/deep/{img}" width="1024" height="576" alt="{html.escape(cap)}" loading="eager"><figcaption>{cap}<br><small>{CR}</small></figcaption></figure>{fs}'
            f'<section class="bsp-card"><h2>Sources</h2><ul class="q-src">{cites}</ul></section><div class="q-bridge"><span>🌍 {bt}</span><a href="{bu}">{bl} on Saving Planets →</a></div>'
            f'<p class="q-hot">Keep digging: {others} · <a href="Quest.html">Back to the Dig Quest</a></p></div></main>')
def quest(lang):
    en = lang=="en"
    note = "" if en else '<p class="bsp-ph" role="note">TODO machine-draft translation: quest copy below is English for review.</p>'
    la = "" if en else ' lang="en"'
    n=len(LAYERS)
    out=f'<div class="edu-wrap bsp-wrap"{la}>{note}<p class="q-intro">Tap a layer to dig in. Start at the very beginning and dig toward today.</p><p class="q-progress" aria-live="polite" data-total="{n}">0 of {n} layers uncovered</p><div class="q-dig">'
    for i,(name,age,col,ic,fact,src,img,bridge,(bl,bu)) in enumerate(LAYERS):
        cites="".join(f'<li><a href="{u}" rel="noopener">{html.escape(a)}</a></li>' for a,u in src)
        out+=(f'<section class="q-layer" style="--q:{col}"><button type="button" aria-expanded="false" aria-controls="q{i}"><span>Layer {i+1}: {name} <span class="q-age">({age})</span></span><span class="q-tool" aria-hidden="true">{ic}</span></button>'
              f'<div class="q-body" id="q{i}" hidden><figure><div class="q-ph-img">Image placeholder: {html.escape(img)}</div></figure><p>{fact}</p><p class="q-src">Sources:</p><ul class="q-src">{cites}</ul>'+
              hot(i)+f'<div class="q-bridge"><span>🌍 {bridge}</span><a href="{bu}">{bl} on Saving Planets →</a></div></div></section>')
    out+=f'</div><p class="bsp-hook">You reached today. <a href="{SP}">Continue the story with solutions on Saving Planets →</a></p></div>'
    return out
def quest_teaser(lang):
    return f'<div class="edu-wrap bsp-wrap"><section class="bsp-card"><h2>Dig Quest: Earth’s Story</h2><p>Eight layers, 4.54 billion years, every fact cited — and each layer opens a door to today’s solutions on Saving Planets.</p><p><a class="btn hero-cta" href="Quest.html">{QCTA}</a></p></section></div>'

def build(lang):
    t=T[lang]; r=rel(lang); out=os.path.join(ROOT,"" if lang=="en" else lang); os.makedirs(out,exist_ok=True)
    def w(page,s): open(os.path.join(out,page+".html"),"w").write(s)
    hero=f'''<main id="main"><section class="bsp-hero" aria-labelledby="bsp-h1">{HERO_SVG}<button type="button" class="bsp-pause" aria-pressed="false">{t['pause']}</button><div class="hero-content bsp-hero-content"><div class="bsp-kzone"><p class="hero-kicker bsp-kicker">{t['kicker']}</p></div><h1 id="bsp-h1" class="hero-welcome"><span class="bsp-l1">{t['h1a']}</span> <span class="bsp-l2">{t['h1b']}</span></h1><p class="hero-example">{t['sub']}</p><p class="hero-ctas"><a class="btn hero-cta" href="Quest.html">{QCTA}</a><a class="btn hero-cta2" href="World_Map.html">{t['cta1']}</a><a class="btn hero-cta2" href="https://www.savingplanets.com/">{t['cta2']}</a></p><div class="bsp-bzone"></div></div><p class="bsp-credit">{HCRED}</p></section>
<section class="diff-strip"><p class="diff-lead">{t['hook']}</p></section>{quest_teaser(lang)}</main>'''
    w("Quest",head(lang,"Quest","Dig Quest: Earth’s Story","Dig through deep time from Earth’s formation to the last Ice Age, then see today’s solutions on Saving Planets.")+body(lang,"Quest",'<main id="main">'+page_hero("Dig Quest: Earth’s Story","Uncover each layer to travel from 4.54 billion years ago to the last Ice Age. Every fact is cited.",t)+quest(lang)+'</main>',"toc-sub",f'<script src="{r}bsp-quest.js" defer></script>'))
    for k in DEEP: w(k,head(lang,k,DEEP[k][0],DEEP[k][1])+body(lang,k,deep(lang,k)))
    w("index",head(lang,"index",t['h1a']+" "+t['h1b'],t['sub'])+body(lang,"index",hero,"toc-home",f'<script src="{r}bsp-hero.js" defer></script>'))
    for page,tk,dk in [("About","t_about","d_about"),("Ways_to_Help","t_help","d_help"),("Search","t_search","d_search")]:
        extra=""
        if page=="Search": extra=f'<form class="bsp-search" role="search" onsubmit="return false"><input type="search" placeholder="{t["search"]}…" aria-label="{t["search"]}" disabled> <span>(placeholder)</span></form>'
        if page=="About": extra=f'<div class="edu-wrap bsp-wrap"><section class="bsp-card"><h2>{t["sister"]}</h2><p>{t["hook"]}</p><p><a href="https://www.savingplanets.com/">www.savingplanets.com</a></p></section></div>'
        w(page,head(lang,page,t[tk],t[dk])+body(lang,page,f'<main id="main">{page_hero(t[tk],t[dk],t)}{extra}{placeholder(t)}</main>'))
    X=EXTRA[lang]; src='<div class="edu-wrap bsp-wrap"><section class="bsp-card"><h2>'+X[4]+'</h2><p>'+X[5]+'</p><ul>'+"".join(f'<li><a href="{u}" lang="en">{n}</a></li>' for n,u in SOURCES)+'</ul></section></div>'
    for i,page in enumerate(["Myth_vs_Fact","Learn","Kids","Teachers"]):
        w(page,head(lang,page,X[i],t['ph'])+body(lang,page,f'<main id="main">{page_hero(X[i],t["hook"],t)}{src}{placeholder(t)}</main>'))
    w("Contact",head(lang,"Contact",t['t_contact'],t['d_contact'])+body(lang,"Contact",f'<main id="main">{page_hero(t["t_contact"],t["d_contact"],t)}<div class="edu-wrap bsp-wrap"><section class="bsp-card"><p><a href="mailto:{t["email"]}">{t["email"]}</a> (placeholder: Saving Planets inbox until a Before Saving Planets address exists)</p></section></div></main>'))
    # map data
    os.makedirs(os.path.join(ROOT,"assets","data"),exist_ok=True)
    json.dump({"lang":lang,"pin":t["pin"],"sites":[{"n":n,"lat":a,"lng":b} for n,a,b in SITES]},open(os.path.join(ROOT,"assets","data",f"fossil-map.{lang}.json"),"w"),ensure_ascii=False)
    mascot=f'<button type="button" class="bsp-mascot" data-go="north" aria-label="{t["north"]}"><span class="bsp-dino" aria-hidden="true">🦕</span><span class="bsp-say">{t["north"]}</span></button>'
    lst="".join(f'<li>{html.escape(n)} — <em>{t["pin"]}</em></li>' for n,a,b in SITES)
    wm=f'''<main id="main" class="wm-main"><div class="wm-wrap bsp-map" data-src="{r}assets/data/fossil-map.{lang}.json"><div class="wm-screen"><h1 class="wm-title">{t['t_map']}</h1><p class="bsp-ph">⚠ {t['ph']}</p><div class="wm-stage"><div id="wm" class="wm-map" dir="ltr" role="region" aria-label="{t['t_map']}"></div>{mascot}</div></div><details class="wm-list"><summary>{t['t_map']}</summary><ul>{lst}</ul></details></div></main>'''
    w("World_Map",head(lang,"World_Map",t['t_map'],t['d_map'],f'<link rel="stylesheet" href="{r}assets/leaflet/leaflet.css"><link rel="stylesheet" href="{r}map.css">')+body(lang,"World_Map",wm,"toc-sub world-map-page",f'<script src="{r}assets/leaflet/leaflet.js" defer></script><script src="{r}bsp-map.js" defer></script>'))
    pos=[(18,20),(62,14),(40,38),(78,44),(22,62),(60,70)]
    bub="".join(f'<button type="button" class="edu-bubble glass bsp-bubble" style="left:{x}%;top:{y}%" aria-pressed="false" data-ph="{html.escape(t["ph"])}"><span class="em" aria-hidden="true">{e}</span>{n}</button>' for (x,y),e,n in zip(pos,"🪲🌿🟠🦖🧊🪸",t["bubbles"]))
    km=f'''<main id="main">{page_hero(t['t_kids'],t['d_kids'],t)}<div class="edu-wrap"><p class="bsp-ph">⚠ {t['ph']}</p><div class="km-stage bsp-km" role="group" aria-label="{t['t_kids']}">{bub}{mascot}</div><p class="bsp-km-out" aria-live="polite"></p></div></main>'''
    w("Kids_Map",head(lang,"Kids_Map",t['t_kids'],t['d_kids'],f'<link rel="stylesheet" href="{r}edu.css">')+body(lang,"Kids_Map",km,"toc-sub kids-map-page",f'<script src="{r}bsp-kids.js" defer></script>'))

if __name__=="__main__":
    for L in LANGS: build(L)
    sm="".join(f"<url><loc>{url(L,p)}</loc></url>" for L in LANGS for p in PAGES)
    open(os.path.join(ROOT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
    print("built",len(LANGS)*len(PAGES),"pages")
