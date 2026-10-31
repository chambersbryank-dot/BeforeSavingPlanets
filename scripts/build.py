#!/usr/bin/env python3
"""Before Saving Planets scaffold generator. Builds 6 languages x pages from STRINGS below.
Everything marked PLACEHOLDER is review copy, not researched content."""
import json, os, html, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from deep import DEEP, HOT, CR
from story import PLAY, HINT, STORY, GLOBE
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
  t_contact="Contact us", d_contact="Questions, corrections or ideas? We’d love to hear from you.", t_map="Fossil sites around the world", d_map="An interactive map of fossil sites, soft-body lagerstätten, first forests, and deep-time archives. Every pin opens a coin card: two round pictures, then what, when, where, and why it matters.",
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
# Batch 1 gold pins. The mirror refuses a map that drops them or swaps their specimen photo.
GOLD = (
"Mistaken Point, Newfoundland, Canada",
"Chengjiang Fossil Site, Yunnan, China",
"Joggins Fossil Cliffs, Nova Scotia, Canada",
"Petrified Forest National Park, Arizona, USA",
"Dinosaur National Monument, Utah/Colorado, USA",
"Jurassic Coast (Dorset & East Devon), UK",
"Riversleigh & Naracoorte, Australia",
"Cradle of Humankind, South Africa",
)
GOLD_FILE = {
"Mistaken Point, Newfoundland, Canada":"Ediacaran_fossils_Mistaken_Point",
"Chengjiang Fossil Site, Yunnan, China":"Fuxianhuia_protensa",
"Joggins Fossil Cliffs, Nova Scotia, Canada":"Lycopsid_joggins",
"Petrified Forest National Park, Arizona, USA":"Petrified_forest_log",
"Dinosaur National Monument, Utah/Colorado, USA":"Wall_of_Bones",
"Jurassic Coast (Dorset & East Devon), UK":"Ichthyosaurus_communis",
"Riversleigh & Naracoorte, Australia":"Nimbadon_lavarackorum_skeleton",
"Cradle of Humankind, South Africa":"Cast_of_taung_child",
}
# Deep-time Batch 2. Rock and climate archives, same coin shape as the fossil pins.
BATCH2 = [
("EPICA Dome C & Vostok ice cores, Antarctica",-75.1,123.35),
("Greenland ice cores (GISP2 / NGRIP), Greenland",72.58,-38.46),
("Hamersley banded iron, Karijini NP, Western Australia",-22.48,118.55),
("Shark Bay stromatolites (Hamelin Pool), Western Australia",-26.4,114.16),
("Jack Hills zircons, Western Australia",-26.08,117.17),
("Barberton Makhonjwa Mountains, South Africa",-25.9,31.05),
("Gubbio K-Pg boundary (Bottaccione Gorge), Italy",43.3656,12.5827),
("Grand Canyon National Park, Arizona, USA",36.06,-112.14),
]
# Deep-time Batch 3. Same coin shape. Chicxulub pairs with the Batch 2 Gubbio pin.
BATCH3 = [
("Acasta Gneiss, Northwest Territories, Canada",65.17,-115.55),
("Snowball Earth glacial & cap-carbonate rocks, Otavi Mountains, Namibia",-19.6,17.3),
("Elatina Formation tillite, Flinders Ranges, South Australia",-31.33,138.63),
("Chicxulub impact crater, Yucatán, Mexico",21.4,-89.52),
]
GUBBIO = "Gubbio K-Pg boundary (Bottaccione Gorge), Italy"
CHICXULUB = "Chicxulub impact crater, Yucatán, Mexico"
# Batch 4 mass-extinction coins. Meishan and Kuhjoch stay off the map until a site photo and a restoration are both cleared.
# pairWith is one mutual link. Chicxulub and Gubbio already use it, so Deccan names them in the lesson instead.
BATCH4 = [
("Dob’s Linn, Moffat, Scotland, UK",55.42,-3.27),
("Coumiac Quarry (Frasnian–Famennian boundary), Montagne Noire, France",43.46,3.04),
("Siberian Traps, Putorana Plateau, Russia",69.0,94.0),
("Karoo Basin (Lystrosaurus beds), Eastern Cape, South Africa",-31.9,24.9),
("Palisades Sill (CAMP lavas), New Jersey, USA",40.85,-73.95),
("Deccan Traps, Western Ghats, Maharashtra, India",18.5,73.8),
]
# Batch 5 first forests. Kiltorcan ships on the Geological Survey Ireland quarry report.
# Xinhang and a separate Karoo Glossopteris pin stay off until a cleared site photo is in hand.
BATCH5 = [
("Rhynie Chert, Aberdeenshire, Scotland, UK",57.33,-2.84),
("Baragwanathia beds, Yea, Victoria, Australia",-37.21,145.43),
("Gilboa Fossil Forest (and nearby Cairo forest), New York, USA",42.4,-74.45),
("Kiltorcan Old Quarry, County Kilkenny, Ireland",52.46,-7.181),
("Fossil Grove, Victoria Park, Glasgow, Scotland, UK",55.876,-4.338),
("Glossopteris forests, Transantarctic Mountains, Antarctica",-84.0,165.0),
]
# Batch 6 soft-body lagerstätten. Crato stays off until a cleared restoration and careful Brazilian-source wording exist.
# The Emu Bay second round is a museum model of Burgess Anomalocaris canadensis, captioned as a relative.
BATCH6 = [
("Sirius Passet, Peary Land, North Greenland",82.79,-42.23),
("Emu Bay Shale, Kangaroo Island, South Australia",-35.58,137.47),
("Fezouata Formation, Zagora, Morocco",30.4,-5.9),
("Mazon Creek fossil beds, Grundy/Will Counties, Illinois, USA",41.25,-88.25),
("Solnhofen Limestone, Bavaria, Germany",48.89,10.99),
("Jehol Biota (Yixian Formation), Liaoning, China",41.6,120.8),
]
# Batch 7 From Fins to Feet. Ventastega stays off: no cleared specimen photo.
# Tiktaalik is the 2006 NV2K17 reading. East Greenland is Stensiö Bjerg, not Celsius Bjerg.
# Gogo uses the published Stromatoporoid Camp area. The 2008 paper names the camp and prints no GPS point.
BATCH7 = [
("Qujing, Yunnan, China (Kuanti Formation)",25.4501,103.7506),
("Gogo Formation, Kimberley, Western Australia",-18.683,125.708),
("Miguasha National Park, Quebec, Canada (UNESCO)",48.1071,-66.3542),
("Cleveland Shale, Cleveland, Ohio, USA",41.5099,-81.614),
("Bird Fiord (Tiktaalik), Ellesmere Island, Nunavut, Canada",77.16497,-86.26918),
("Stensiö Bjerg, Gauss Halvø, East Greenland",73.4349,-23.1924),
("Red Hill, Pennsylvania, USA (Catskill Formation)",41.3417,-77.675),
]
# Batch 8 Built by Life: ancient reefs. Dolomites stay off until a site-tied specimen and a restoration are both cleared.
# Windjana’s second round is an Ohio stromatoporoid. The Gogo fish photo stays off this card.
# The Great Barrier Reef uses NASA images. The ESA Copernicus file’s license tag was not CC BY-SA 3.0 IGO.
BATCH8 = [
("Windjana Gorge, Kimberley, Western Australia",-17.41,124.95),
("Capitan Reef, Guadalupe Mountains, Texas, USA",31.89,-104.86),
("Wren’s Nest, Dudley, England",52.53,-2.1),
("Gotland, Sweden (Silurian reefs)",57.47,18.49),
("Falls of the Ohio, Indiana, USA",38.28,-85.76),
("Great Barrier Reef, Queensland, Australia",-18.29,147.7),
]
# Batch 1b coins replaced these pins in place. Names and coordinates stay put.
BATCH1B = [
("Burgess Shale, British Columbia, Canada",51.43,-116.47),
("Messel Pit, Germany",49.92,8.75),
("Dinosaur Provincial Park, Alberta, Canada",50.76,-111.49),
("La Brea Tar Pits, Los Angeles, USA",34.063,-118.356),
("Ediacara Hills, South Australia",-30.8,138.15),
("Wadi Al-Hitan, Egypt",29.27,30.04),
("Ischigualasto, Argentina",-30.0,-67.9),
("Monte San Giorgio, Switzerland/Italy",45.9,8.95),
]
# Visible species captions when the fossil and the restoration are not the same animal.
MISMATCH = {
"Burgess Shale, British Columbia, Canada":("Anomalocaris","Opabinia"),
"Messel Pit, Germany":("Darwinius","Propalaeotherium"),
"Dinosaur Provincial Park, Alberta, Canada":("Gorgosaurus","Centrosaurus"),
"Ediacara Hills, South Australia":("Dickinsonia costata","Dickinsonia menneri"),
"Wadi Al-Hitan, Egypt":("Basilosaurus isis","Basilosaurus cetoides"),
}

def visible_text(s):
    parts=[s.get("n"),s.get("era")]
    parts += list((s.get("teach") or {}).values())
    for side in ("specimen","restoration"):
        img=s.get(side) or {}
        parts += [img.get("alt"),img.get("credit"),img.get("caption")]
    links=s.get("learnMore") or []
    if isinstance(links, dict): links=[links]
    parts += [x.get("label") for x in links]
    return "\n".join(str(p or "") for p in parts)

def fossil_doc(lang):
    """Mirror assets/data/fossil-map.en.json. Fossil coins stay; later batches are appended."""
    en=json.load(open(os.path.join(ROOT,"assets","data","fossil-map.en.json"),encoding="utf-8"))
    ph=[s for s in en["sites"] if "teach" not in s]
    coins=[s for s in en["sites"] if "teach" in s]
    if ph:
        raise SystemExit("placeholder pin left on the fossil map: "+ph[0].get("n",""))
    order=[n for n,_,_ in BATCH1B]+list(GOLD)+[n for n,_,_ in BATCH2]+[n for n,_,_ in BATCH3]+[n for n,_,_ in BATCH4]+[n for n,_,_ in BATCH5]+[n for n,_,_ in BATCH6]+[n for n,_,_ in BATCH7]+[n for n,_,_ in BATCH8]
    if len(coins)!=len(order):
        raise SystemExit("expected 16 fossil coins, 8 Batch 2 coins, 4 Batch 3 coins, 6 Batch 4 coins, 6 Batch 5 coins, 6 Batch 6 coins, 7 Batch 7 coins, and 6 Batch 8 coins")
    by={s.get("n"):s for s in coins}
    if len(by)!=len(order):
        raise SystemExit("duplicate coin name")
    for n,lat,lng in BATCH1B:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 1b pin moved or renamed: "+n)
    for n,(a,b) in MISMATCH.items():
        s=by[n]
        if a not in (s.get("specimen") or {}).get("caption","") or b not in (s.get("restoration") or {}).get("caption",""):
            raise SystemExit("species caption missing on "+n)
    lb=by["La Brea Tar Pits, Los Angeles, USA"]
    if "fatalis" in visible_text(lb).lower() or "populator" in visible_text(lb).lower():
        raise SystemExit("La Brea card must caption Smilodon generically, not by species")
    for side in ("specimen","restoration"):
        if (lb.get(side) or {}).get("caption")!="Saber-toothed cat (Smilodon)":
            raise SystemExit("La Brea "+side+" needs the generic saber-toothed cat caption")
    edi=visible_text(by["Ediacara Hills, South Australia"])
    if "Tentative List" not in edi or "not a World Heritage site yet" not in edi:
        raise SystemExit("Ediacara card must say the Flinders Ranges are tentative, not inscribed")
    if "cast" not in ((by["Ischigualasto, Argentina"].get("specimen") or {}).get("caption") or "").lower():
        raise SystemExit("Ischigualasto specimen must be captioned as a cast")
    for n in GOLD:
        s=by.get(n)
        if not s:
            raise SystemExit("Batch 1 gold pin missing: "+n)
        if GOLD_FILE[n] not in ((s.get("specimen") or {}).get("src") or ""):
            raise SystemExit("Batch 1 gold specimen changed: "+n)

    for n,lat,lng in BATCH2:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("deep-time Batch 2 pin moved or renamed: "+n)
    for n,lat,lng in BATCH3:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("deep-time Batch 3 pin moved or renamed: "+n)
    if [s.get("n") for s in en["sites"]]!=order:
        raise SystemExit("site order drifted; keep Batch 1b, then Batch 1, then Batch 2, then Batch 3, then Batch 4, then Batch 5, then Batch 6, then Batch 7, then Batch 8")
    for n,lat,lng in BATCH4:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 4 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 4 must not take the Chicxulub–Gubbio pairWith slot: "+n)
    for bad in ("Meishan","Kuhjoch","Xinhang","Onder Karoo","Crato","Ventastega","Pavāri","Pavari","Dolomites","Sciliar","Schlern","Daonella"):
        if any(bad in (s.get("n") or "") for s in coins):
            raise SystemExit("deferred pin shipped: "+bad)
    for n,lat,lng in BATCH5:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 5 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 5 must not take the Chicxulub–Gubbio pairWith slot: "+n)
    for n,lat,lng in BATCH6:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 6 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 6 must not take the Chicxulub–Gubbio pairWith slot: "+n)
    bara=by["Baragwanathia beds, Yea, Victoria, Australia"]
    bara2=bara.get("restoration") or {}
    if bara2.get("label")!="Another specimen" or "not a drawing" not in (bara2.get("caption") or "").lower():
        raise SystemExit("Baragwanathia second round must be another specimen, not a restoration")
    rhy=by["Rhynie Chert, Aberdeenshire, Scotland, UK"]
    if "Horneophyton" not in (rhy.get("specimen") or {}).get("caption","") or "Aglaophyton" not in (rhy.get("restoration") or {}).get("caption",""):
        raise SystemExit("Rhynie rounds must name Horneophyton and Aglaophyton")
    if not any("the-rhynie-chert" in (x.get("href") or "") for x in rhy.get("learnMore") or []):
        raise SystemExit("Rhynie learn-more must use the live Aberdeen page")
    kil=by["Kiltorcan Old Quarry, County Kilkenny, Ireland"]
    kil_hrefs=" ".join((x.get("href") or "") for x in (kil.get("learnMore") or []))
    if "gsi.geodata.gov.ie" not in kil_hrefs or "10.1038/19516" not in kil_hrefs:
        raise SystemExit("Kiltorcan needs the Geological Survey Ireland report and the modern-tree paper")
    kil_draw=(kil.get("restoration") or {}).get("caption") or ""
    if "macilenta" not in kil_draw or "not the Kiltorcan" not in kil_draw:
        raise SystemExit("Kiltorcan drawing must be captioned as New York Archaeopteris macilenta")
    gloss=by["Glossopteris forests, Transantarctic Mountains, Antarctica"]
    if (gloss.get("restoration") or {}).get("label")!="Map" or "Not a picture of the living plant" not in (gloss.get("restoration") or {}).get("caption",""):
        raise SystemExit("Glossopteris second round must be the distribution map, not a life restoration")
    if not any("historical.html" in (x.get("href") or "") for x in gloss.get("learnMore") or []):
        raise SystemExit("Glossopteris needs the USGS page that names the plant")
    grove=by["Fossil Grove, Victoria Park, Glasgow, Scotland, UK"]
    for x in grove.get("learnMore") or []:
        href=x.get("href") or ""
        if "glasgow.gov.uk" in href or "://fossilgrove.org" in href:
            raise SystemExit("Fossil Grove must not link the blocked council page or the dead fossilgrove.org host")
    if not any("fossilgroveglasgow.org" in (x.get("href") or "") for x in grove.get("learnMore") or []):
        raise SystemExit("Fossil Grove learn-more must be the trust site")
    for n in (
        "Rhynie Chert, Aberdeenshire, Scotland, UK",
        "Gilboa Fossil Forest (and nearby Cairo forest), New York, USA",
        "Kiltorcan Old Quarry, County Kilkenny, Ireland",
        "Fossil Grove, Victoria Park, Glasgow, Scotland, UK",
    ):
        rest=by[n].get("restoration") or {}
        text=" ".join([rest.get("caption") or "", rest.get("alt") or "", rest.get("credit") or ""])
        if rest.get("label")!="Artist’s concept" or "Artist" not in text or "not a photograph" not in text.lower():
            raise SystemExit("Batch 5 artist concept must be labeled and captioned: "+n)
    for n in (
        "Sirius Passet, Peary Land, North Greenland",
        "Fezouata Formation, Zagora, Morocco",
        "Mazon Creek fossil beds, Grundy/Will Counties, Illinois, USA",
        "Solnhofen Limestone, Bavaria, Germany",
        "Jehol Biota (Yixian Formation), Liaoning, China",
    ):
        rest=by[n].get("restoration") or {}
        text=" ".join([rest.get("caption") or "", rest.get("alt") or "", rest.get("credit") or ""])
        if rest.get("label")!="Artist’s concept" or "Artist" not in text or "not a photograph" not in text.lower():
            raise SystemExit("Batch 6 artist concept must be labeled and captioned: "+n)
    emu=by["Emu Bay Shale, Kangaroo Island, South Australia"]
    emu_r=emu.get("restoration") or {}
    emu_cap=emu_r.get("caption") or ""
    if emu_r.get("label")!="Model" or "Anomalocaris relative" not in emu_cap or "canadensis" not in emu_cap or "not the Kangaroo Island" not in emu_cap:
        raise SystemExit("Emu Bay restoration must be the Burgess canadensis model, captioned as an Anomalocaris relative")
    if "model" not in (emu_r.get("credit") or "").lower():
        raise SystemExit("Emu Bay credit must say the round is a photo of a model")
    if "Fossilised_Anomalocaris_eye" not in (emu.get("specimen") or {}).get("src",""):
        raise SystemExit("Emu Bay specimen must stay the fossil eye")
    if "Anomalocaris_canadensis_fossil" in json.dumps(emu):
        raise SystemExit("Emu Bay must not reuse the Burgess Anomalocaris body fossil")
    for n,lat,lng in BATCH7:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 7 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 7 must not take the Chicxulub–Gubbio pairWith slot: "+n)
    for n,lat,lng in BATCH8:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 8 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 8 must not take the Chicxulub–Gubbio pairWith slot: "+n)
    maz=by["Mazon Creek fossil beds, Grundy/Will Counties, Illinois, USA"]
    maz_teach=" ".join((maz.get("teach") or {}).values())
    if "still argue" not in maz_teach:
        raise SystemExit("Tully Monster teach text must say scientists still argue")
    maz_low=maz_teach.lower()
    for bad_line in ("it is a vertebrate", "it was a vertebrate", "was a fish", "is a fish", "was a lamprey"):
        if bad_line in maz_low:
            raise SystemExit("Tully text states a disputed identity as fact")
    tully_cap=((maz.get("restoration") or {}).get("caption") or "").lower()
    if "still disagree" not in tully_cap and "not a settled picture" not in tully_cap:
        raise SystemExit("Tully drawing must say the identity is not settled")
    sirius=by["Sirius Passet, Peary Land, North Greenland"]
    sir_hrefs=" ".join((x.get("href") or "") for x in (sirius.get("learnMore") or []))
    if "adb2c94e-1dec-492a-8d8d-177b1df5ec8b" not in sir_hrefs and "jgs2019-043" not in sir_hrefs:
        raise SystemExit("Sirius Passet needs the Harper 2019 review")
    sol=by["Solnhofen Limestone, Bavaria, Germany"]
    sol_hrefs=" ".join((x.get("href") or "") for x in (sol.get("learnMore") or []))
    if "museum-solnhofen.de" not in sol_hrefs:
        raise SystemExit("Solnhofen needs the Bürgermeister-Müller museum")
    if "museumfuernaturkunde.berlin" not in sol_hrefs:
        raise SystemExit("Solnhofen needs the live Museum für Naturkunde page")
    jehol=by["Jehol Biota (Yixian Formation), Liaoning, China"]
    if "region" not in ((jehol.get("teach") or {}).get("where") or "").lower():
        raise SystemExit("Jehol pin must say it marks a region, not one cliff")
    dobs=by["Dob’s Linn, Moffat, Scotland, UK"]
    if "not Dob’s Linn" not in ((dobs.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Dob’s Linn diorama must be captioned as period life, not the site")
    cou=by["Coumiac Quarry (Frasnian–Famennian boundary), Montagne Noire, France"]
    dunk=(cou.get("restoration") or {}).get("caption") or ""
    if "Late Devonian" not in dunk or "Not a fossil from Coumiac" not in dunk:
        raise SystemExit("Dunkleosteus must be captioned as Late Devonian ocean life, not a Coumiac fossil")
    sib=by["Siberian Traps, Putorana Plateau, Russia"]
    sib_blob=json.dumps(sib,ensure_ascii=False)
    if "german" in sib_blob.lower() or "Extent_of_Siberian" in sib_blob:
        raise SystemExit("Siberian coin must not use the German-label map")
    if "Krasnye Kamni" not in ((sib.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Siberian landscape must name Krasnye Kamni, near Norilsk")
    dec=visible_text(by["Deccan Traps, Western Ghats, Maharashtra, India"])
    if "Gubbio" not in dec or "Chicxulub" not in dec:
        raise SystemExit("Deccan coin should name the Gubbio coin and Chicxulub")
    pal=by["Palisades Sill (CAMP lavas), New Jersey, USA"]
    if "Not a fossil from the Palisades" not in ((pal.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Palisades restoration must be captioned as an artist’s concept, not a local fossil")
    for s in coins:
        teach=s.get("teach") or {}
        for k in ("what","when","where","why"):
            if not teach.get(k): raise SystemExit("coin missing teach."+k+": "+s.get("n",""))
        for k in ("specimen","restoration"):
            img=s.get(k) or {}
            if not str(img.get("src","")).startswith("https://") or not img.get("credit"):
                raise SystemExit("coin image missing https src or credit: "+s.get("n",""))
            if not str(img.get("href","")).startswith("https://") or not img.get("alt"):
                raise SystemExit("coin image missing alt or file page: "+s.get("n",""))
        links=s.get("learnMore") or []
        if isinstance(links, dict): links=[links]
        if not links: raise SystemExit("coin missing learnMore: "+s.get("n",""))
        for x in links:
            if not str((x or {}).get("href","")).startswith("https://"):
                raise SystemExit("learnMore is not https: "+s.get("n",""))
    epica=by["EPICA Dome C & Vostok ice cores, Antarctica"]
    green=by["Greenland ice cores (GISP2 / NGRIP), Greenland"]
    if "GISP2" in epica["specimen"]["src"] or epica["specimen"]["src"]==green["specimen"]["src"]:
        raise SystemExit("Antarctic coin must not reuse the Greenland ice-core photo")
    canyon=by["Grand Canyon National Park, Arizona, USA"]
    diagram=(canyon.get("restoration") or {}).get("src","")+(canyon.get("restoration") or {}).get("href","")
    if "NPS" not in diagram:
        raise SystemExit("Grand Canyon diagram should be the NPS figure")
    def require_concept(name):
        rest=by[name].get("restoration") or {}
        text=" ".join([rest.get("caption") or "", rest.get("alt") or "", rest.get("credit") or ""])
        if rest.get("label")!="Artist’s concept" or "Artist" not in text or "not a photograph" not in text.lower():
            raise SystemExit("Batch 7 artist concept must be labeled and captioned: "+name)
    for n in (
        "Qujing, Yunnan, China (Kuanti Formation)",
        "Gogo Formation, Kimberley, Western Australia",
        "Miguasha National Park, Quebec, Canada (UNESCO)",
        "Cleveland Shale, Cleveland, Ohio, USA",
        "Bird Fiord (Tiktaalik), Ellesmere Island, Nunavut, Canada",
        "Red Hill, Pennsylvania, USA (Catskill Formation)",
    ):
        require_concept(n)
    gui=by["Qujing, Yunnan, China (Kuanti Formation)"]
    gui_cap=(gui.get("specimen") or {}).get("caption") or ""
    if "V25047" not in (gui.get("specimen") or {}).get("src","") and "V25047" not in (gui.get("specimen") or {}).get("href",""):
        raise SystemExit("Guiyu specimen must be the V25047 fossil plate")
    if "map of the bones" not in gui_cap.lower() and "not the colors" not in gui_cap.lower():
        raise SystemExit("Guiyu plate must say the bright colors are a bone map, not the animal’s colors")
    gui_hrefs=" ".join((x.get("href") or "") for x in (gui.get("learnMore") or []))
    if "nature07855" not in gui_hrefs:
        raise SystemExit("Guiyu needs the live Zhu and others 2009 paper")
    gogo=by["Gogo Formation, Kimberley, Western Australia"]
    gogo_m=gogo.get("specimen") or {}
    gogo_r=gogo.get("restoration") or {}
    if gogo_m.get("label")!="Model" or "Materpiscis02" not in (gogo_m.get("src") or ""):
        raise SystemExit("Gogo first round must be the Museums Victoria model photo")
    if "not the fossil" not in (gogo_m.get("caption") or "").lower():
        raise SystemExit("Gogo model must say it is not the fossil")
    gogo_rc=(gogo_r.get("caption") or "").lower()
    if "Materpiscis.jpg" not in (gogo_r.get("href") or "") and "Materpiscis.jpg" not in (gogo_r.get("src") or ""):
        raise SystemExit("Gogo second round must keep the low-resolution birth restoration")
    if "not a photograph of the fossil" not in gogo_rc or ("700" not in gogo_rc and "low-resolution" not in gogo_rc):
        raise SystemExit("Gogo birth scene must be captioned as a low-resolution restoration, not the fossil")
    if "Windjana" in json.dumps(gogo) or "renovatis" in json.dumps(gogo):
        raise SystemExit("Gogo must not use the Windjana photo or the marked-up derivative")
    gogo_hrefs=" ".join((x.get("href") or "") for x in (gogo.get("learnMore") or []))
    if "nature06966" not in gogo_hrefs:
        raise SystemExit("Gogo needs the live Long and others 2008 paper")
    mig=by["Miguasha National Park, Quebec, Canada (UNESCO)"]
    mig_hrefs=" ".join((x.get("href") or "") for x in (mig.get("learnMore") or []))
    if "whc.unesco.org/en/list/686" not in mig_hrefs:
        raise SystemExit("Miguasha needs the live UNESCO 686 page")
    if "370" not in ((mig.get("teach") or {}).get("when") or ""):
        raise SystemExit("Miguasha must mention UNESCO’s 370-million-year round number")
    cleve=by["Cleveland Shale, Cleveland, Ohio, USA"]
    cleve_cap=(cleve.get("specimen") or {}).get("caption") or ""
    if "CMNH_5768" not in (cleve.get("specimen") or {}).get("src","") and "CMNH 5768" not in cleve_cap:
        raise SystemExit("Cleveland specimen must be the CMNH 5768 skull")
    if "rebuilt" not in cleve_cap.lower() and "reconstructed" not in cleve_cap.lower():
        raise SystemExit("Cleveland skull must say some plates are rebuilt")
    if "Morocco" in json.dumps(cleve) or "WDC_-_Dunkleosteus" in json.dumps(cleve):
        raise SystemExit("Cleveland coin must not use the Morocco skull")
    cleve_hrefs=" ".join((x.get("href") or "") for x in (cleve.get("learnMore") or []))
    if "10.26879/1343" not in cleve_hrefs:
        raise SystemExit("Cleveland needs the live Engelman armor paper")
    tik=by["Bird Fiord (Tiktaalik), Ellesmere Island, Nunavut, Canada"]
    if "cast" not in ((tik.get("specimen") or {}).get("caption") or "").lower():
        raise SystemExit("Tiktaalik photo must be captioned as a cast")
    if "NV2K17" not in ((tik.get("teach") or {}).get("where") or ""):
        raise SystemExit("Tiktaalik pin must name the published site NV2K17")
    tik_hrefs=" ".join((x.get("href") or "") for x in (tik.get("learnMore") or []))
    if "nature04639" not in tik_hrefs:
        raise SystemExit("Tiktaalik needs the live 2006 Nature paper")
    greenland=by["Stensiö Bjerg, Gauss Halvø, East Greenland"]
    gwhere=(greenland.get("teach") or {}).get("where") or ""
    if "Stensiö Bjerg" not in gwhere or "Celsius Bjerg" not in gwhere or "not a surveyed stake" not in gwhere:
        raise SystemExit("East Greenland pin must sit on Stensiö Bjerg and say Celsius Bjerg is a different place")
    gmodel=greenland.get("restoration") or {}
    if gmodel.get("label")!="Model" or "not a photograph of the living animal" not in (gmodel.get("caption") or "").lower():
        raise SystemExit("Acanthostega second round must be the Stuttgart model, not a life photograph")
    green_hrefs=" ".join((x.get("href") or "") for x in (greenland.get("learnMore") or []))
    if "S0263593300000304" not in green_hrefs and "10.1017/S0263593300000304" not in green_hrefs:
        raise SystemExit("East Greenland needs the live Clack 2002 paper")
    hyn=by["Red Hill, Pennsylvania, USA (Catskill Formation)"]
    hyn_teach=" ".join((hyn.get("teach") or {}).values()).lower()
    if "shoulder" not in hyn_teach or "not a whole skeleton" not in hyn_teach:
        raise SystemExit("Hynerpeton must stay limited to the shoulder bone")
    if "its legs" in hyn_teach or "walked on land" in hyn_teach:
        raise SystemExit("Hynerpeton text must not invent a walking body")
    hyn_cap=((hyn.get("restoration") or {}).get("caption") or "").lower()
    if "guess" not in hyn_cap or "shoulder" not in hyn_cap:
        raise SystemExit("Hynerpeton drawing must say the body is a guess from the shoulder bone")
    if "10.1126/science" in json.dumps(hyn):
        raise SystemExit("Hynerpeton must not link the Science DOI that returns 403")
    wind=by["Windjana Gorge, Kimberley, Western Australia"]
    wind_blob=json.dumps(wind)
    if "Gogo_fish" in wind_blob or "Materpiscis" in wind_blob:
        raise SystemExit("Windjana must not use the Gogo fish photo")
    wind_spec=wind.get("restoration") or {}
    wind_cap=wind_spec.get("caption") or ""
    if wind_spec.get("label")!="Specimen" or "Kelleys Island" not in wind_cap or "not a fossil from Windjana" not in wind_cap:
        raise SystemExit("Windjana second round must be an Ohio stromatoporoid, not a local or Gogo fossil")
    if "too young" not in " ".join((wind.get("teach") or {}).values()):
        raise SystemExit("Windjana must say the 350-million-year round number is too young")
    cap=by["Capitan Reef, Guadalupe Mountains, Texas, USA"]
    cap_d=cap.get("restoration") or {}
    cap_cap=(cap_d.get("caption") or "")
    if cap_d.get("label")!="Diorama" or "not a photograph" not in cap_cap.lower() or "Carlsbad" not in cap_cap:
        raise SystemExit("Capitan second round must be the Carlsbad diorama, not a photograph")
    if "Helicoprion" in json.dumps(cap) or "National_Fossil_Day" in json.dumps(cap):
        raise SystemExit("Capitan must not use the National Fossil Day poster")
    wren=by["Wren’s Nest, Dudley, England"]
    wren_d=wren.get("restoration") or {}
    wren_c=wren_d.get("caption") or ""
    if wren_d.get("label")!="Diorama" or "not the Dudley reef" not in wren_c or "not Wren" not in wren_c:
        raise SystemExit("Wren’s Nest diorama must be captioned as a generic Silurian seafloor, not Dudley")
    if "Wrens_Nest" not in ((wren.get("specimen") or {}).get("href") or ""):
        raise SystemExit("Wren’s Nest specimen must be the Dudley Bug from Wren’s Nest")
    got=by["Gotland, Sweden (Silurian reefs)"]
    if (got.get("restoration") or {}).get("label")!="Specimen" or "Gotland_halysites" not in ((got.get("restoration") or {}).get("src") or ""):
        raise SystemExit("Gotland second round must be the Halysites specimen, not a restoration")
    if "Lergrav" not in ((got.get("teach") or {}).get("where") or ""):
        raise SystemExit("Gotland pin must say the rauk photo is at Lergrav")
    falls=by["Falls of the Ohio, Indiana, USA"]
    if "Jeffersonville" not in ((falls.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Falls specimen must name the Jeffersonville Limestone")
    if (falls.get("restoration") or {}).get("label")!="Specimen":
        raise SystemExit("Falls second round must be labeled as a specimen")
    gbr=by["Great Barrier Reef, Queensland, Australia"]
    gbr_blob=json.dumps(gbr)
    if "ESA508080" in gbr_blob or "Attribution-Copernicus" in gbr_blob:
        raise SystemExit("Great Barrier Reef must not use the uncleared ESA image")
    if "Great_Barrier_Reef_(MODIS)" not in ((gbr.get("specimen") or {}).get("href") or ""):
        raise SystemExit("Great Barrier Reef site round must be the NASA MODIS image")
    gbr_map=gbr.get("restoration") or {}
    if gbr_map.get("label")!="Map" or "not a photograph of bleached coral" not in (gbr_map.get("caption") or "").lower():
        raise SystemExit("Great Barrier Reef second round must be the temperature map, not a bleaching photo")
    if "152548" in gbr_blob:
        raise SystemExit("Great Barrier Reef must not link the Earth Observatory page that redirects home")
    gbr_when=(gbr.get("teach") or {}).get("when") or ""
    if "600,000" not in gbr_when or "9,000" not in gbr_when:
        raise SystemExit("Great Barrier Reef ages must follow the park authority figures")
    if by[CHICXULUB].get("pairWith")!=GUBBIO or by[GUBBIO].get("pairWith")!=CHICXULUB:
        raise SystemExit("Chicxulub and Gubbio must pair both ways")
    for s in coins:
        other=s.get("pairWith")
        if not other:
            continue
        back=by.get(other)
        if not back or back.get("pairWith")!=s.get("n"):
            raise SystemExit("pairWith must name a coin that pairs back: "+s.get("n",""))
    # Batch 2 coins other than the reciprocal Gubbio link stay free of pairWith.
    for n,lat,lng in BATCH2:
        if n!=GUBBIO and by[n].get("pairWith"):
            raise SystemExit("unexpected pairWith on Batch 2 pin: "+n)
    nam=by["Snowball Earth glacial & cap-carbonate rocks, Otavi Mountains, Namibia"]
    if "20900468815" in json.dumps(nam) or "Testing_the_Limits" in json.dumps(nam):
        raise SystemExit("Namibia coin must not use the Hoffman talk title slide")
    if "not the Otavi rocks" not in (nam.get("specimen") or {}).get("caption",""):
        raise SystemExit("Namibia diagram must say it is not the Otavi rocks")
    if "Vienna" not in (by["Acasta Gneiss, Northwest Territories, Canada"].get("specimen") or {}).get("credit",""):
        raise SystemExit("Acasta specimen must be captioned as the Vienna museum piece")
    if "Elatina_Formation" not in (by["Elatina Formation tillite, Flinders Ranges, South Australia"].get("specimen") or {}).get("src",""):
        raise SystemExit("Elatina specimen must be the Enorama Creek tillite")
    if "Chicxulub_radar" not in (by[CHICXULUB].get("specimen") or {}).get("src",""):
        raise SystemExit("Chicxulub map round must stay the SRTM radar image")
    for n,lat,lng in BATCH3:
        rest=by[n].get("restoration") or {}
        text=" ".join([rest.get("caption") or "", rest.get("alt") or "", rest.get("credit") or ""])
        if rest.get("label")!="Artist’s concept" or "Artist" not in text or "not a photograph" not in text.lower():
            raise SystemExit("Batch 3 artist concept must be labeled and captioned: "+n)
    doc={"lang":lang,"pin":T[lang]["pin"],"ui":en["ui"],"sites":en["sites"]}
    if lang!="en": doc["draft"]="English coin text pending family review."
    return doc

def fossil_li(s, t):
    if "teach" not in s:
        return f'<li>{html.escape(s["n"])} — <em>{t["pin"]}</em></li>'
    links=s.get("learnMore") or []
    if isinstance(links, dict): links=[links]
    more="".join(f' <a href="{html.escape(x["href"], quote=True)}">{html.escape(x.get("label") or "Learn more")}</a>' for x in links)
    pair=f' See also: {html.escape(s["pairWith"])}.' if s.get("pairWith") else ""
    return f'<li>{html.escape(s["n"])} — <em>{html.escape(s.get("era") or "")}</em>. {html.escape(s["teach"]["what"])}{pair}{more}</li>'

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
HCRED="Before 540 million years: artist’s interpretation (SI). From 540 Ma, continents drift using Scotese PALEOMAP via the GPlates Web Service (EarthByte). Finish: NASA Blue Marble. Not footage."
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
    return f'<div class="edu-wrap bsp-wrap"><section class="bsp-card"><h2>Dig Quest: Earth’s Story</h2><p>Eight layers, 4.54 billion years, every fact cited — and each layer opens a door to today’s solutions on Saving Planets. On the quest, a globe scrubs from 540 million years ago to today.</p><p><a class="btn hero-cta" href="Quest.html">{QCTA}</a> <a class="btn hero-cta2" href="Quest.html#time-scrubber">{GLOBE[lang]["scrub"]}</a></p></section></div>'

def story_block(lang):
    note = "" if lang=="en" else '<p class="bsp-ph" role="note">TODO machine-draft translation: English review copy is the source.</p>'
    cards=[]
    for e in STORY[lang]:
        cta=""
        if e["why"]:
            cta=(f'<p class="hero-ctas"><a class="btn hero-cta" href="Quest.html">{QCTA}</a>'
                 f'<a class="btn hero-cta2" href="Quest.html#time-scrubber">{GLOBE[lang]["scrub"]}</a>'
                 f'<a class="btn hero-cta2" href="https://www.savingplanets.com/">{T[lang]["cta2"]}</a></p>')
        wid=' id="why-bsp"' if e["why"] else ""
        cards.append(
            f'<article class="bsp-era" data-t0="{e["t0"]}" data-t1="{e["t1"]}"{wid}><div class="bsp-era-card">'
            f'<img class="bsp-era-still" src="/assets/hero/morph/{e["still"]}" alt="" width="640" height="360">'
            f'<p class="bsp-era-k">{e["k"]}</p><h2>{e["h"]}</h2><p>{e["p"]}</p>{cta}</div></article>')
    return f'<div class="bsp-eras">{note}{"".join(cards)}</div>'

def globe_block(lang):
    g=GLOBE[lang]; r=rel(lang)
    note="" if lang=="en" else '<p class="bsp-ph" role="note">TODO machine-draft translation: English review copy is the source.</p>'
    pairs=[]
    for i,(fossil,sol,href) in enumerate(g["pairs"]):
        chk=' checked' if i==0 else ""
        pairs.append(
            f'<label><input type="radio" name="bsp-pair" value="{i}"{chk}>'
            f'<span><span class="bsp-pin-f">● {fossil}</span><br><span class="bsp-pin-s">● <a href="{href}">{sol}</a></span></span></label>')
    return (
        f'<section class="bsp-globe-sec" id="time-scrubber" data-pins="{r}assets/data/paleo-pins.json" data-tex="{r}assets/hero/paleo/" data-today="{html.escape(g["today"])}" data-far-msg="{html.escape(g["far"])}">'
        f'<div class="edu-wrap bsp-wrap">{note}<h2>{g["h"]}</h2><p>{g["p"]}</p>'
        f'<div class="bsp-globe-layout"><div class="bsp-globe-stage"><canvas id="bsp-globe" width="360" height="360" aria-label="{html.escape(g["canvas"])}"></canvas></div>'
        f'<div><p class="bsp-globe-time"><span data-readout>540 Ma</span>'
        f'<input type="range" min="0" max="540" step="1" value="540" aria-label="{html.escape(g["axis"])}" aria-valuemin="0" aria-valuemax="540" aria-valuenow="540"></p>'
        f'<p class="bsp-globe-note">{g["axis"]}</p><div class="bsp-pairs" role="radiogroup">{"".join(pairs)}</div>'
        f'<p data-far hidden></p><p class="bsp-globe-note">{g["credit"]}</p></div></div></div></section>')

def build(lang):
    t=T[lang]; r=rel(lang); out=os.path.join(ROOT,"" if lang=="en" else lang); os.makedirs(out,exist_ok=True)
    def w(page,s): open(os.path.join(out,page+".html"),"w").write(s)
    hero=f'''<main id="main"><div class="bsp-story" id="earth-story"><section class="bsp-hero" aria-labelledby="bsp-h1">{HERO_SVG}<button type="button" class="bsp-pause" aria-pressed="false" data-play="{PLAY[lang]}">{t['pause']}</button><p class="bsp-scrollhint">{HINT[lang]}</p><div class="hero-content bsp-hero-content"><div class="bsp-kzone"><p class="hero-kicker bsp-kicker">{t['kicker']}</p></div><h1 id="bsp-h1" class="hero-welcome"><span class="bsp-l1">{t['h1a']}</span> <span class="bsp-l2">{t['h1b']}</span></h1><p class="hero-example">{t['sub']}</p><p class="hero-ctas"><a class="btn hero-cta" href="Quest.html">{QCTA}</a><a class="btn hero-cta2" href="World_Map.html">{t['cta1']}</a><a class="btn hero-cta2" href="https://www.savingplanets.com/">{t['cta2']}</a></p><div class="bsp-bzone"></div></div><p class="bsp-credit">{HCRED}</p></section>
{story_block(lang)}</div><section class="diff-strip"><p class="diff-lead">{t['hook']}</p></section>{quest_teaser(lang)}</main>'''
    w("Quest",head(lang,"Quest","Dig Quest: Earth’s Story","Dig through deep time from Earth’s formation to the last Ice Age, then see today’s solutions on Saving Planets.")+body(lang,"Quest",'<main id="main">'+page_hero("Dig Quest: Earth’s Story","Uncover each layer to travel from 4.54 billion years ago to the last Ice Age. Every fact is cited.",t)+globe_block(lang)+quest(lang)+'</main>',"toc-sub",f'<script src="{r}bsp-globe.js" defer></script><script src="{r}bsp-quest.js" defer></script>'))
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
    # map data: English file is the coin source; other languages mirror it (English copy pending family review).
    os.makedirs(os.path.join(ROOT,"assets","data"),exist_ok=True)
    doc=fossil_doc(lang)
    with open(os.path.join(ROOT,"assets","data",f"fossil-map.{lang}.json"),"w",encoding="utf-8") as f:
        json.dump(doc,f,ensure_ascii=False,indent=2)
        f.write("\n")
    mascot=f'<button type="button" class="bsp-mascot" data-go="north" aria-label="{t["north"]}"><span class="bsp-dino" aria-hidden="true">🦕</span><span class="bsp-say">{t["north"]}</span></button>'
    lst="".join(fossil_li(s,t) for s in doc["sites"])
    if lang=="en":
        banner='<p class="bsp-ph">Fifty-nine sites open as coin cards: sixteen classic fossil sites, six soft-body lagerstätten, twelve deep-time archives, six mass-extinction sites, six first-forest sites, seven From Fins to Feet sites, and six ancient-reef sites. Each card has two round pictures, then what, when, where, and why it matters. Learn more is last. Chicxulub and Gubbio link to each other.</p>'
    else:
        banner=f'<p class="bsp-ph">⚠ {t["ph"]}</p><p class="bsp-ph">Fossil, soft-body, deep-time, mass-extinction, first-forest, fish-to-tetrapod, and ancient-reef coin cards are in English pending family review.</p>'
    wm=f'''<main id="main" class="wm-main"><div class="wm-wrap bsp-map" data-src="{r}assets/data/fossil-map.{lang}.json"><div class="wm-screen"><h1 class="wm-title">{t['t_map']}</h1>{banner}<div class="wm-stage"><div id="wm" class="wm-map" dir="ltr" role="region" aria-label="{t['t_map']}"></div>{mascot}</div></div><details class="wm-list"><summary>{t['t_map']}</summary><ul>{lst}</ul></details></div></main>'''
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
