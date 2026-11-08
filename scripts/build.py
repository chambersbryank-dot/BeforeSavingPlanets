#!/usr/bin/env python3
"""Before Saving Planets scaffold generator. Builds 6 languages x pages from STRINGS below.
Everything marked PLACEHOLDER is review copy, not researched content."""
import json, os, html, re, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from deep import DEEP, HOT, CR, PHOTOS
from story import PLAY, HINT, STORY, GLOBE
from smilodon import page as smilodon_page
import archaeopteryx, dunkleosteus, meganeura, pterodactylus, plesiosaurus, mosasaurus
import otodus, argentavis, haast
import support
import about_pages
from finds import FIND_SLUGS, find_page, hub_page, deep_time_page, has_map, has_video, NAV as DINO_NAV, DEEP_NAV
import life
import seo_copy
import home_library
import bsp_knowledge
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOM = "https://www.beforesavingplanets.com"
LANGS = ["en","fr","es","ar","it","he"]
RTL = {"ar","he"}
NAMES = {"en":("EN","English"),"fr":("FR","Français"),"es":("ES","Español"),"ar":("عربي","العربية"),"it":("IT","Italiano"),"he":("עב","עברית")}
PAGES = ["index","Quest","Continents","Oceans","Seas","DeadSea","About","Contact","World_Map","Smilodon","Dinosaurs","Mammals","Aerial","Marine","Deep_Time","Borealopelta","Nigersaurus","Triceratops","Stegosaurus","Archaeopteryx","Dunkleosteus","Meganeura","Pterodactylus","Plesiosaurus","Mosasaurus","Otodus_megalodon","Argentavis","Haasts_eagle","Kids_Map","Ways_to_Help","Search","Myth_vs_Fact","Learn","Kids","Teachers","Courses","Lesson_Plan","Earth_Materials","Stratigraphic_Record","Field_Geology","World_Archaeology","Site_Context","Field_Methods","Geophysics","Sediments","Field_Camp","Animal_Bones","Site_Soils","Long_Essay"]
DOSSIER_PAGES = [
    ("Archaeopteryx", archaeopteryx.page),
    ("Dunkleosteus", dunkleosteus.page),
    ("Meganeura", meganeura.page),
    ("Pterodactylus", pterodactylus.page),
    ("Plesiosaurus", plesiosaurus.page),
    ("Mosasaurus", mosasaurus.page),
    ("Otodus_megalodon", otodus.page),
    ("Argentavis", argentavis.page),
    ("Haasts_eagle", haast.page),
]
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
  t_contact="Contact us", d_contact="Questions, corrections or ideas? We’d love to hear from you.", t_map="Fossil sites around the world", d_map="An interactive map of fossil sites, first forests, and deep-time archives. Each pin opens a coin: what, when, where, and why it matters.",
  t_kids="Kids Fossil Map", d_kids="Tap a bubble to travel back in time. Fun facts will be added after research.", t_help="Ways to Help", d_help="Donate or volunteer at the museums that hold these fossils. This site is free and asks for nothing.",
  t_search="Search", d_search="One shared index for this site and Saving Planets. It is not published yet, and a question here is not saved.", eras="Eras (placeholder)", credit="Hero art: Created by the Founder and SI (illustrative, not a scientific reconstruction).",
  pin="Placeholder pin — sourced page coming soon", north="Look up here for older stories!", bubbles=["Trilobites","Ancient ferns","Amber","Dinosaurs","Ice Age","Ancient reefs"], email="hello@savingplanets.com", foot="A sister site of", pause="Pause animation"),
"fr": dict(brand="Before Saving Planets", home="Accueil", about="À propos", contact="Contact", map="Carte du monde", kids="Carte des fossiles (enfants)", help="Comment aider", search="Rechercher", sister="Site jumeau : Saving Planets",
  kicker="LÀ OÙ TOUT COMMENCE", h1a="Où commence", h1b="l’histoire de la Terre", sub="Fossiles, climats anciens et écosystèmes disparus — et ce qu’ils peuvent nous apprendre pour soigner notre planète aujourd’hui.",
  cta1="Explorer la carte des fossiles", cta2="Visiter Saving Planets", hook="Saving Planets trouve des solutions sans catastrophisme. Before Saving Planets, c’est là où commence l’histoire de la Terre.",
  ph="Contenu provisoire — bientôt disponible. Cette page est une maquette à relire ; le contenu sourcé sera ajouté ensuite.",
  t_about="À propos de Before Saving Planets", d_about="Site jumeau de Saving Planets sur le temps profond : ce que les fossiles disent des climats passés et des solutions d’aujourd’hui.",
  t_contact="Nous contacter", d_contact="Questions, corrections ou idées ? Écrivez-nous.", t_map="Sites fossilifères du monde", d_map="Carte des sites fossilifères, des premières forêts et du temps profond. Chaque repère ouvre une pièce : quoi, quand, où et pourquoi.",
  t_kids="Carte des fossiles pour enfants", d_kids="Touche une bulle pour remonter le temps. Les anecdotes arriveront après nos recherches.", t_help="Comment aider", d_help="Dons et bénévolat auprès des musées qui gardent ces fossiles. Ce site est gratuit et ne demande rien.",
  t_search="Rechercher", d_search="Un index partagé pour ce site et Saving Planets. Il n’est pas encore publié, et une question ici n’est pas enregistrée.", eras="Ères (provisoire)", credit="Illustration : créée par le fondateur et SI (illustrative, pas une reconstitution scientifique).",
  pin="Repère provisoire — page sourcée à venir", north="Regarde ici pour des histoires plus anciennes !", bubbles=["Trilobites","Fougères anciennes","Ambre","Dinosaures","Ère glaciaire","Récifs anciens"], email="hello@savingplanets.com", foot="Un site jumeau de", pause="Mettre en pause"),
"es": dict(brand="Before Saving Planets", home="Inicio", about="Acerca de", contact="Contacto", map="Mapa mundial", kids="Mapa de fósiles (niños)", help="Cómo ayudar", search="Buscar", sister="Sitio hermano: Saving Planets",
  kicker="DONDE TODO COMIENZA", h1a="La historia", h1b="de la Tierra", sub="Fósiles, climas antiguos y ecosistemas perdidos, y lo que pueden enseñarnos para sanar nuestro planeta hoy.",
  cta1="Explorar el mapa de fósiles", cta2="Visitar Saving Planets", hook="Saving Planets encuentra soluciones sin catastrofismo. Before Saving Planets es donde comienza la historia de la Tierra.",
  ph="Contenido provisional: próximamente. Esta página es una maqueta para revisión; después se añadirá contenido con fuentes.",
  t_about="Acerca de Before Saving Planets", d_about="Sitio hermano de Saving Planets sobre el tiempo profundo: cómo los fósiles registran climas pasados y orientan las soluciones de hoy.",
  t_contact="Contáctanos", d_contact="¿Preguntas, correcciones o ideas? Escríbenos.", t_map="Yacimientos de fósiles del mundo", d_map="Mapa de yacimientos, primeros bosques y archivos del tiempo profundo. Cada ficha dice qué, cuándo, dónde y por qué importa.",
  t_kids="Mapa de fósiles para niños", d_kids="Toca una burbuja para viajar en el tiempo. Los datos curiosos llegarán tras investigar.", t_help="Cómo ayudar", d_help="Dona o haz de voluntario en los museos que custodian estos fósiles. Este sitio es gratis y no pide nada.",
  t_search="Buscar", d_search="Un índice compartido para este sitio y Saving Planets. Aún no está publicado, y una pregunta aquí no se guarda.", eras="Eras (provisional)", credit="Arte: creado por el fundador y SI (ilustrativo, no es una reconstrucción científica).",
  pin="Marcador provisional: página con fuentes próximamente", north="¡Mira aquí para historias más antiguas!", bubbles=["Trilobites","Helechos antiguos","Ámbar","Dinosaurios","Edad de Hielo","Arrecifes antiguos"], email="hello@savingplanets.com", foot="Un sitio hermano de", pause="Pausar animación"),
"ar": dict(brand="Before Saving Planets", home="الرئيسية", about="من نحن", contact="اتصل بنا", map="خريطة العالم", kids="خريطة الأحافير للأطفال", help="طرق المساعدة", search="بحث", sister="الموقع الشقيق: Saving Planets",
  kicker="حيث تبدأ الحكاية", h1a="حيث تبدأ", h1b="قصة الأرض", sub="أحافير ومناخات قديمة ونظم بيئية مفقودة، وما يمكن أن تعلّمنا إياه لنداوي كوكبنا اليوم.",
  cta1="استكشف خريطة الأحافير", cta2="زر Saving Planets", hook="يجد Saving Planets حلولاً بلا تهويل. وBefore Saving Planets هو حيث تبدأ قصة الأرض.",
  ph="محتوى مؤقت — قريباً. هذه الصفحة نموذج للمراجعة، وسيُضاف المحتوى الموثّق لاحقاً.",
  t_about="عن Before Saving Planets", d_about="موقع شقيق لـ Saving Planets يركّز على الزمن العميق: كيف تسجّل الأحافير مناخات ونظماً بيئية سابقة، وكيف يمكن لهذا السجل أن يرشد حلول اليوم.",
  t_contact="اتصل بنا", d_contact="أسئلة أو تصحيحات أو أفكار؟ يسعدنا أن نسمع منك.", t_map="مواقع الأحافير حول العالم", d_map="خريطة لمواقع الأحافير والغابات الأولى وأرشيف الزمن العميق. كل بطاقة تقول ماذا ومتى وأين ولماذا يهم.",
  t_kids="خريطة الأحافير للأطفال", d_kids="اضغط على فقاعة لتعود بالزمن. ستضاف الحقائق الممتعة بعد البحث.", t_help="طرق المساعدة", d_help="تبرّع أو تطوّع في المتاحف التي تحفظ هذه الأحافير. هذا الموقع مجاني ولا يطلب شيئًا.",
  t_search="بحث", d_search="فهرس مشترك لهذا الموقع وSaving Planets. ليس منشورًا بعد، والسؤال هنا لا يُحفظ.", eras="العصور (مؤقت)", credit="الرسم: من إعداد المؤسس وSI (توضيحي، وليس إعادة بناء علمية).",
  pin="علامة مؤقتة — صفحة موثّقة قريباً", north="انظر هنا لقصص أقدم!", bubbles=["ثلاثيات الفصوص","سراخس قديمة","كهرمان","ديناصورات","العصر الجليدي","شعاب قديمة"], email="hello@savingplanets.com", foot="موقع شقيق لـ", pause="إيقاف الحركة"),
"it": dict(brand="Before Saving Planets", home="Home", about="Chi siamo", contact="Contatti", map="Mappa del mondo", kids="Mappa dei fossili (bambini)", help="Come aiutare", search="Cerca", sister="Sito gemello: Saving Planets",
  kicker="DOVE TUTTO HA INIZIO", h1a="Dove inizia", h1b="la storia della Terra", sub="Fossili, climi antichi ed ecosistemi perduti, e ciò che possono insegnarci per curare il nostro pianeta oggi.",
  cta1="Esplora la mappa dei fossili", cta2="Visita Saving Planets", hook="Saving Planets trova soluzioni senza catastrofismo. Before Saving Planets è dove inizia la storia della Terra.",
  ph="Contenuto provvisorio: in arrivo. Questa pagina è una bozza da rivedere; i contenuti con fonti verranno aggiunti dopo.",
  t_about="Chi è Before Saving Planets", d_about="Sito gemello di Saving Planets sul tempo profondo: come i fossili registrano i climi passati e guidano le soluzioni di oggi.",
  t_contact="Contattaci", d_contact="Domande, correzioni o idee? Scrivici.", t_map="Siti fossili nel mondo", d_map="Mappa di siti fossili, prime foreste e archivi del tempo profondo. Ogni scheda dice cosa, quando, dove e perché conta.",
  t_kids="Mappa dei fossili per bambini", d_kids="Tocca una bolla per viaggiare nel tempo. Le curiosità arriveranno dopo la ricerca.", t_help="Come aiutare", d_help="Dona o fai volontariato nei musei che custodiscono questi fossili. Il sito è gratis e non chiede nulla.",
  t_search="Cerca", d_search="Un indice condiviso per questo sito e Saving Planets. Non è ancora pubblicato, e una domanda qui non viene salvata.", eras="Ere (provvisorio)", credit="Illustrazione: creata dal fondatore e da SI (illustrativa, non una ricostruzione scientifica).",
  pin="Segnaposto provvisorio: pagina con fonti in arrivo", north="Guarda qui per storie più antiche!", bubbles=["Trilobiti","Felci antiche","Ambra","Dinosauri","Era glaciale","Barriere antiche"], email="hello@savingplanets.com", foot="Un sito gemello di", pause="Metti in pausa"),
"he": dict(brand="Before Saving Planets", home="בית", about="אודות", contact="צור קשר", map="מפת העולם", kids="מפת מאובנים לילדים", help="איך לעזור", search="חיפוש", sister="אתר אחות: Saving Planets",
  kicker="היכן שהכול מתחיל", h1a="היכן שמתחיל", h1b="סיפורו של כדור הארץ", sub="מאובנים, אקלים קדום ומערכות אקולוגיות שאבדו, ומה הם יכולים ללמד אותנו כדי לרפא את כוכב הלכת שלנו היום.",
  cta1="גלו את מפת המאובנים", cta2="בקרו ב-Saving Planets", hook="Saving Planets מוצא פתרונות בלי אווירת אבדון. Before Saving Planets הוא המקום שבו מתחיל סיפורו של כדור הארץ.",
  ph="תוכן זמני — בקרוב. דף זה הוא שלד לבדיקה; תוכן עם מקורות יתווסף בהמשך.",
  t_about="אודות Before Saving Planets", d_about="אתר אחות של Saving Planets המתמקד בזמן העמוק: כיצד מאובנים מתעדים אקלים ומערכות אקולוגיות של העבר, וכיצד התיעוד הזה יכול להנחות פתרונות כיום.",
  t_contact="צרו קשר", d_contact="שאלות, תיקונים או רעיונות? נשמח לשמוע.", t_map="אתרי מאובנים ברחבי העולם", d_map="מפה של אתרי מאובנים, יערות ראשונים וארכיוני זמן עמוק. כל כרטיס אומר מה, מתי, איפה ולמה זה חשוב.",
  t_kids="מפת מאובנים לילדים", d_kids="הקישו על בועה כדי לחזור בזמן. עובדות מעניינות יתווספו אחרי המחקר.", t_help="איך לעזור", d_help="תרמו או התנדבו במוזיאונים ששומרים על המאובנים האלה. האתר חינמי ואינו מבקש דבר.",
  t_search="חיפוש", d_search="אינדקס משותף לאתר הזה ול-Saving Planets. הוא עדיין לא פורסם, ושאלה כאן אינה נשמרת.", eras="תקופות (זמני)", credit="איור: נוצר על ידי המייסד ו-SI (להמחשה, לא שחזור מדעי).",
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
# Batch 9 Our Family Tree. Denisova ships with the cave mouth and the finger bone only.
# No face. Cradle of Humankind stays the Batch 1 pin. Lake Turkana and Zhoukoudian stay off.
# Dmanisi is the historic site (Wikidata), not the modern town center 12 km west.
# Laetoli keeps the research pin. Wikipedia’s Laetoli coordinate sits on Olduvai Gorge.
BATCH9 = [
("Hadar, Afar Region, Ethiopia (Lucy)",11.1,40.58),
("Laetoli footprints, Tanzania",-3.21,35.19),
("Olduvai Gorge, Tanzania",-2.994,35.351),
("Jebel Irhoud, Morocco",31.855,-8.8725),
("Dmanisi, Georgia",41.3373,44.3447),
("Atapuerca (Sima de los Huesos, Gran Dolina), Spain",42.3525,-3.5183),
("Liang Bua, Flores, Indonesia",-8.5342,120.4603),
("Denisova Cave, Altai Mountains, Russia",51.3975,84.6761),
]
# Batch 10 Ice Age giants. Pilauco stays off until a peer-reviewed English source is in hand.
# La Brea is already a Batch 1b coin and is not edited.
# Waco’s restoration is Knight. Hot Springs uses a different Columbian mammoth drawing.
# The London Megatherium is a cast. The Tellus Smilodon is a cast, not a Lagoa Santa cave fossil.
BATCH10 = [
("Waco Mammoth National Monument, Texas, USA",31.606,-97.175),
("The Mammoth Site, Hot Springs, South Dakota, USA",43.42471,-103.48313),
("Blue Babe, Fairbanks, Alaska, USA",64.8589,-147.8422),
("Lyuba, Yamal Peninsula, Russia",68.0,71.0),
("Cueva del Milodón, Patagonia, Chile",-51.568,-72.617),
("Luján, Buenos Aires, Argentina (Megatherium)",-34.57,-59.11),
("Lagoa Santa caves, Minas Gerais, Brazil",-19.63,-43.89),
]
# Batch 11. The eight sites that stayed off earlier batches.
# Xinhang is the Late Devonian Guangdedendron forest at Jianchuan (Wang and others, 2019). The paper prints no GPS point.
# Pilauco’s footprint is published and still disputed, so the card says so.
BATCH11 = [
("Meishan Section D (Permian–Triassic golden spike), Changxing, China",31.0798,119.7058),
("Kuhjoch (Triassic–Jurassic golden spike), Karwendel, Austria",47.4839,11.5306),
("Crato Formation, Araripe Basin, Ceará, Brazil",-7.0919,-39.6808),
("The Dolomites (Schlern / Sciliar), Italy",46.515,11.5756),
("Pilauco, Osorno, Chile",-40.57,-73.1039),
("Xinhang fossil forest, Guangde, Anhui, China",31.0702,119.5604),
("Glossopteris trunks, Karoo National Park, South Africa",-32.2622,22.3091),
("Ventastega, Pavāri outcrop, Latvia",56.6878,22.1331),
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
    rm=s.get("readMore") or {}
    if isinstance(rm, dict): parts += [rm.get("label")]
    return "\n".join(str(p or "") for p in parts)

def fossil_doc(lang):
    """Mirror assets/data/fossil-map.en.json. Fossil coins stay; later batches are appended."""
    en=json.load(open(os.path.join(ROOT,"assets","data","fossil-map.en.json"),encoding="utf-8"))
    ph=[s for s in en["sites"] if "teach" not in s]
    coins=[s for s in en["sites"] if "teach" in s]
    if ph:
        raise SystemExit("placeholder pin left on the fossil map: "+ph[0].get("n",""))
    order=[n for n,_,_ in BATCH1B]+list(GOLD)+[n for n,_,_ in BATCH2]+[n for n,_,_ in BATCH3]+[n for n,_,_ in BATCH4]+[n for n,_,_ in BATCH5]+[n for n,_,_ in BATCH6]+[n for n,_,_ in BATCH7]+[n for n,_,_ in BATCH8]+[n for n,_,_ in BATCH9]+[n for n,_,_ in BATCH10]+[n for n,_,_ in BATCH11]
    if len(coins)!=len(order):
        raise SystemExit("expected 16 fossil coins, 8 Batch 2 coins, 4 Batch 3 coins, 6 Batch 4 coins, 6 Batch 5 coins, 6 Batch 6 coins, 7 Batch 7 coins, 6 Batch 8 coins, 8 Batch 9 coins, 7 Batch 10 coins, and 8 Batch 11 coins")
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
        raise SystemExit("site order drifted; keep Batches 1b through 11 in order")
    for n,lat,lng in BATCH4:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 4 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 4 must not take the Chicxulub–Gubbio pairWith slot: "+n)
    for bad in ("Onder Karoo","Daonella"):
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
    for n,lat,lng in BATCH9:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 9 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 9 must not take the Chicxulub–Gubbio pairWith slot: "+n)
        if "missing link" in visible_text(s).lower():
            raise SystemExit("Batch 9 must not say missing link: "+n)
        blob=json.dumps(s,ensure_ascii=False)
        for bad in ("Zhoukoudian","Turkana","Rising Star","pekinensis","KNM-ER","Bioanthropologist","Homo_erectus_artistic_reconstruction","Laetoli_Footprints_Site_A","Denisova_cave_01","Cranium_17.png"):
            if bad in blob:
                raise SystemExit("Batch 9 used a blocked image or site: "+bad+" on "+n)
    def b9_face(name, license_bit):
        rest=by[name].get("restoration") or {}
        text=" ".join([rest.get("caption") or "", rest.get("alt") or "", rest.get("credit") or ""])
        if rest.get("label")!="Artist’s concept" or "Artist" not in text or "not a photograph" not in text.lower():
            raise SystemExit("Batch 9 facial approximation must be labeled and captioned: "+name)
        if "Cicero Moraes" not in (rest.get("credit") or "") or license_bit not in (rest.get("credit") or ""):
            raise SystemExit("Batch 9 face must credit Cicero Moraes "+license_bit+": "+name)
    b9_face("Hadar, Afar Region, Ethiopia (Lucy)","CC BY-SA 4.0")
    b9_face("Atapuerca (Sima de los Huesos, Gran Dolina), Spain","CC BY-SA 3.0")
    b9_face("Liang Bua, Flores, Indonesia","CC BY-SA 4.0")
    hadar=by["Hadar, Afar Region, Ethiopia (Lucy)"]
    if "cast" not in ((hadar.get("specimen") or {}).get("caption") or "").lower() or "not the original" not in ((hadar.get("specimen") or {}).get("caption") or "").lower():
        raise SystemExit("Lucy specimen must be captioned as a cast, not the original fossil")
    if "afarensis" not in ((hadar.get("restoration") or {}).get("caption") or "").lower():
        raise SystemExit("Lucy face must name Australopithecus afarensis")
    if "4.6" not in " ".join((hadar.get("teach") or {}).values()):
        raise SystemExit("Hadar must frame Lucy in Earth’s 4.6-billion-year story")
    laet=by["Laetoli footprints, Tanzania"]
    if (laet.get("specimen") or {}).get("label")!="Replica" or "not the original" not in ((laet.get("specimen") or {}).get("caption") or "").lower():
        raise SystemExit("Laetoli first round must be a replica, not the original ash")
    if (laet.get("restoration") or {}).get("label")!="Site":
        raise SystemExit("Laetoli second round must be the site, not a life restoration")
    if "Site A" in visible_text(laet):
        raise SystemExit("Laetoli must not use the Site A trail for the classic footprint story")
    oldu=by["Olduvai Gorge, Tanzania"]
    if (oldu.get("specimen") or {}).get("label")!="Gorge" or "Olduvai_gorge" not in ((oldu.get("specimen") or {}).get("src") or ""):
        raise SystemExit("Olduvai first round must be the gorge")
    if (oldu.get("restoration") or {}).get("label")!="Tool" or "British_Museum_Olduvai_handaxe" not in ((oldu.get("restoration") or {}).get("src") or ""):
        raise SystemExit("Olduvai second round must be the Olduvai handaxe")
    if "1.2 million" not in ((oldu.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Olduvai handaxe must keep the museum age of about 1.2 million years")
    jebel=by["Jebel Irhoud, Morocco"]
    jrest=jebel.get("restoration") or {}
    if "cast" not in ((jebel.get("specimen") or {}).get("caption") or "").lower():
        raise SystemExit("Jebel Irhoud skull must be captioned as a cast")
    jcap=(jrest.get("caption") or "").lower()
    if jrest.get("label")!="Reconstruction" or "not a photograph" not in jcap or "not a fleshed face" not in jcap:
        raise SystemExit("Jebel Irhoud second round must be the scan composite, not a fleshed face")
    if "Homo_sapiens_from_Jebel_Irhoud" not in (jrest.get("src") or ""):
        raise SystemExit("Jebel Irhoud reconstruction must be the Gunz composite")
    dman=by["Dmanisi, Georgia"]
    if "Skull 5" not in ((dman.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Dmanisi second round must name Skull 5")
    if "Mashavera" not in ((dman.get("teach") or {}).get("where") or ""):
        raise SystemExit("Dmanisi pin must name the Mashavera river valley")
    if any("science.org" in (x.get("href") or "") for x in (dman.get("learnMore") or [])):
        raise SystemExit("Dmanisi must not link the Science DOI that returns 403")
    ata=by["Atapuerca (Sima de los Huesos, Gran Dolina), Spain"]
    if "de_la_Sima" not in ((ata.get("specimen") or {}).get("src") or "") and "de_la_Sima" not in ((ata.get("specimen") or {}).get("href") or ""):
        raise SystemExit("Atapuerca specimen must be the single Cranium 17 photo")
    if "Cranium 17" not in ((ata.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Atapuerca face must say it is not a portrait of Cranium 17")
    liang=by["Liang Bua, Flores, Indonesia"]
    liang_when=(liang.get("teach") or {}).get("when") or ""
    if "100,000" not in liang_when or "50,000" not in liang_when or "2016" not in liang_when:
        raise SystemExit("Liang Bua must use the revised 2016 age, 100,000 to 50,000 years ago")
    if "18,000" in visible_text(liang) or "18 ka" in visible_text(liang).lower():
        raise SystemExit("Liang Bua must not print the outdated 18,000-year age")
    if "Senckenberg" not in ((liang.get("specimen") or {}).get("caption") or ""):
        raise SystemExit("Liang Bua skull must name the Senckenberg display")
    if "facial_approximation_-_color_2" not in ((liang.get("restoration") or {}).get("src") or ""):
        raise SystemExit("Liang Bua face must be the Cicero Moraes color approximation")
    den=by["Denisova Cave, Altai Mountains, Russia"]
    if (den.get("restoration") or {}).get("label")!="Cave" or "Denisova_cave_03" not in ((den.get("restoration") or {}).get("src") or ""):
        raise SystemExit("Denisova second round must be the cave entrance photo")
    if "phalanx" not in ((den.get("specimen") or {}).get("src") or "").lower():
        raise SystemExit("Denisova specimen must be the finger bone")
    if "no face reconstruction" not in visible_text(den).lower():
        raise SystemExit("Denisova must say the coin has no face reconstruction")
    if "approximation" in json.dumps(den).lower() or "facial" in json.dumps(den.get("restoration") or {}).lower():
        raise SystemExit("Denisova must not carry a facial approximation")
    for n,need in (
        ("Hadar, Afar Region, Ethiopia (Lucy)","al-288-1"),
        ("Laetoli footprints, Tanzania","laetoli-footprint-trails"),
        ("Olduvai Gorge, Tanzania","whc.unesco.org/en/list/39"),
        ("Jebel Irhoud, Morocco","nature22336"),
        ("Dmanisi, Georgia","homo-erectus"),
        ("Atapuerca (Sima de los Huesos, Gran Dolina), Spain","whc.unesco.org/en/list/989"),
        ("Liang Bua, Flores, Indonesia","nature17179"),
        ("Denisova Cave, Altai Mountains, Russia","nature09710"),
    ):
        hrefs=" ".join((x.get("href") or "") for x in (by[n].get("learnMore") or []))
        if need not in hrefs:
            raise SystemExit("Batch 9 learn-more missing "+need+" on "+n)
    if abs(by["Laetoli footprints, Tanzania"]["lat"]-by["Olduvai Gorge, Tanzania"]["lat"])<0.15:
        raise SystemExit("Laetoli pin must not sit on Olduvai Gorge")
    for n,lat,lng in BATCH10:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 10 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 10 must not take the Chicxulub–Gubbio pairWith slot: "+n)
        blob=json.dumps(s,ensure_ascii=False)
        for blocked in ("Smilodon_Knight","Smilodon_fatalis","fatalis"):
            if blocked in blob:
                raise SystemExit("Batch 10 reused a La Brea image or species name: "+blocked+" on "+n)
        for side in ("specimen","restoration"):
            credit=(s.get(side) or {}).get("credit") or ""
            if "CC BY-SA" in credit and "ShareAlike" not in credit:
                raise SystemExit("Batch 10 CC BY-SA credit needs a ShareAlike notice: "+n+" "+side)
    waco=by["Waco Mammoth National Monument, Texas, USA"]
    hot=by["The Mammoth Site, Hot Springs, South Dakota, USA"]
    if "Waco_mammoth_site_QRT" not in (waco.get("specimen") or {}).get("src",""):
        raise SystemExit("Waco specimen must be the in-ground bones")
    if "not the whole nursery herd" not in ((waco.get("specimen") or {}).get("caption") or ""):
        raise SystemExit("Waco bones must say they are not the whole nursery herd")
    if (waco.get("restoration") or {}).get("label")!="Artist’s concept" or "Columbian_mammoth_TFA" not in (waco.get("restoration") or {}).get("src",""):
        raise SystemExit("Waco restoration must be the Knight Columbian mammoth painting")
    if "not a photograph" not in ((waco.get("restoration") or {}).get("caption") or "").lower():
        raise SystemExit("Waco painting must say it is not a photograph")
    if "nursery herd" not in ((waco.get("teach") or {}).get("why") or "").lower():
        raise SystemExit("Waco why must name the nursery herd")
    if "nps.gov/waco" not in " ".join(x.get("href") or "" for x in waco.get("learnMore") or []):
        raise SystemExit("Waco learn-more must include the National Park Service page")
    waco_when = (waco.get("teach") or {}).get("when") or ""
    if "65,000" not in waco_when or "72,000" not in waco_when or "not a single measured year" not in waco_when:
        raise SystemExit("Waco coin must keep the 65,000 to 72,000 herd range")
    if "Mammoth_Site" not in (hot.get("specimen") or {}).get("src","") or "Hot_Springs" not in (hot.get("specimen") or {}).get("src",""):
        raise SystemExit("Hot Springs specimen must be the in-situ bone bed")
    if "Sergiodlarosa" not in (hot.get("restoration") or {}).get("src",""):
        raise SystemExit("Hot Springs restoration must be the Sergiodlarosa drawing, not the Knight painting")
    if "Columbian_mammoth" in json.dumps(hot):
        raise SystemExit("Hot Springs must not reuse the Knight Columbian mammoth file")
    if (hot.get("restoration") or {}).get("label")!="Artist’s concept" or "not a photograph" not in ((hot.get("restoration") or {}).get("caption") or "").lower():
        raise SystemExit("Hot Springs drawing must be labeled as an artist’s concept")
    hot_when=(hot.get("teach") or {}).get("when") or ""
    if "232,000" not in hot_when or "160,000" not in hot_when or "26,000" not in hot_when:
        raise SystemExit("Hot Springs must give the 2026 age and say the 26,000-year guess is too young")
    if "usgs.gov/publications/age-reassignment" not in " ".join(x.get("href") or "" for x in hot.get("learnMore") or []):
        raise SystemExit("Hot Springs learn-more must include the USGS page for the 2026 age")
    if (waco.get("restoration") or {}).get("src")==(hot.get("restoration") or {}).get("src"):
        raise SystemExit("Waco and Hot Springs must not share a restoration")
    babe=by["Blue Babe, Fairbanks, Alaska, USA"]
    if (babe.get("restoration") or {}).get("label")!="Model" or "not Blue Babe" not in ((babe.get("restoration") or {}).get("caption") or ""):
        raise SystemExit("Blue Babe second round must be a model, not Blue Babe")
    if "Museum of the North" not in ((babe.get("teach") or {}).get("where") or ""):
        raise SystemExit("Blue Babe pin must say it marks the Museum of the North, not the mine")
    if "spotlight/blue-babe" not in " ".join(x.get("href") or "" for x in babe.get("learnMore") or []):
        raise SystemExit("Blue Babe learn-more must be the Museum of the North spotlight page")
    lyuba=by["Lyuba, Yamal Peninsula, Russia"]
    lyuba_hrefs=" ".join(x.get("href") or "" for x in lyuba.get("learnMore") or [])
    if "Lyuba_(mammoth)" not in lyuba_hrefs:
        raise SystemExit("Lyuba learn-more must be the mammoth article, not the name disambiguation")
    if lyuba_hrefs.rstrip("/").endswith("/wiki/Lyuba"):
        raise SystemExit("Lyuba must not link the Wikipedia disambiguation page")
    if "Yuka" not in visible_text(lyuba):
        raise SystemExit("Lyuba must not claim she is still the single best-preserved mammoth")
    if "Spain" not in ((lyuba.get("restoration") or {}).get("caption") or "") or "not a photograph" not in ((lyuba.get("restoration") or {}).get("caption") or "").lower():
        raise SystemExit("Lyuba drawing must be captioned as Ice Age Spain, not a photograph of her")
    if "approximate" not in ((lyuba.get("teach") or {}).get("where") or "").lower():
        raise SystemExit("Lyuba pin must say the river coordinate is approximate")
    mil=by["Cueva del Milodón, Patagonia, Chile"]
    mil_cap=(mil.get("specimen") or {}).get("caption") or ""
    if "London" not in mil_cap or "not a photo" not in mil_cap.lower() or "5,000" not in mil_cap:
        raise SystemExit("Mylodon skin must be the London display, not a cave photo, and must flag the sign’s 5,000-year line")
    if (mil.get("restoration") or {}).get("label")!="Artist’s concept" or "not a photograph" not in ((mil.get("restoration") or {}).get("caption") or "").lower():
        raise SystemExit("Mylodon drawing must be labeled as an artist’s concept")
    lujan=by["Luján, Buenos Aires, Argentina (Megatherium)"]
    lujan_cap=(lujan.get("specimen") or {}).get("caption") or ""
    if (lujan.get("specimen") or {}).get("label")!="Cast" or "cast" not in lujan_cap.lower() or "Madrid" not in lujan_cap or "1787" not in lujan_cap:
        raise SystemExit("Luján skeleton must be captioned as the London cast, not the 1787 Madrid skeleton")
    if "what-was-megatherium" not in " ".join(x.get("href") or "" for x in lujan.get("learnMore") or []):
        raise SystemExit("Luján learn-more must include the Natural History Museum page that calls the London mount a cast")
    if "not a settled" not in ((lujan.get("restoration") or {}).get("caption") or "").lower() and "disagree" not in ((lujan.get("restoration") or {}).get("caption") or "").lower():
        raise SystemExit("Megatherium drawing must say the fur is not settled")
    lagoa=by["Lagoa Santa caves, Minas Gerais, Brazil"]
    lagoa_cap=(lagoa.get("specimen") or {}).get("caption") or ""
    if (lagoa.get("specimen") or {}).get("label")!="Cast" or "Tellus" not in lagoa_cap or "not a fossil from those caves" not in lagoa_cap.lower():
        raise SystemExit("Lagoa Santa skeleton must be captioned as the Tellus cast, not a cave fossil")
    if "Smilodon_pop2_15" not in (lagoa.get("restoration") or {}).get("src",""):
        raise SystemExit("Lagoa Santa second round must be the Bogdanov drawing, not the La Brea Knight painting")
    if "populator" not in (lagoa.get("teach") or {}).get("what",""):
        raise SystemExit("Lagoa Santa must name Smilodon populator, the species Lund named from these caves")
    if "lagoasanta.mg.gov.br" not in " ".join(x.get("href") or "" for x in lagoa.get("learnMore") or []):
        raise SystemExit("Lagoa Santa learn-more must include the live Brazilian city page")
    if "Lagoa_Santa_skulls" in json.dumps(lagoa):
        raise SystemExit("Lagoa Santa must not use the wide row of human skulls")
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
    if "85%" in json.dumps(dobs) or "443.1" not in ((dobs.get("teach") or {}).get("when") or ""):
        raise SystemExit("Dob’s Linn coin must keep the commission age and drop the species percentage")
    cou=by["Coumiac Quarry (Frasnian–Famennian boundary), Montagne Noire, France"]
    dunk=(cou.get("restoration") or {}).get("caption") or ""
    if "Late Devonian" not in dunk or "Not a fossil from Coumiac" not in dunk:
        raise SystemExit("Dunkleosteus must be captioned as Late Devonian ocean life, not a Coumiac fossil")
    if "oxygen" in ((cou.get("teach") or {}).get("why") or "").lower():
        raise SystemExit("Coumiac coin must not assign an oxygen cause")
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
    for n in ("La Brea Tar Pits, Los Angeles, USA","Lagoa Santa caves, Minas Gerais, Brazil"):
        if n not in by:
            raise SystemExit("Smilodon range site missing: "+n)
    for n in (
        "Glossopteris forests, Transantarctic Mountains, Antarctica",
        "Glossopteris trunks, Karoo National Park, South Africa",
        "Gotland, Sweden (Silurian reefs)",
        "Falls of the Ohio, Indiana, USA",
    ):
        life_img=by[n].get("life") or {}
        href=life_img.get("href") or ""
        if not href.startswith("https://") or "wikipedia.org" in href:
            raise SystemExit("organism life picture needs a non-Wikipedia https credit: "+n)
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
    for n,lat,lng in BATCH11:
        s=by.get(n)
        if not s or s.get("lat")!=lat or s.get("lng")!=lng:
            raise SystemExit("Batch 11 pin moved or renamed: "+n)
        if s.get("pairWith"):
            raise SystemExit("Batch 11 must not take the Chicxulub–Gubbio pairWith slot: "+n)
        for side in ("specimen","restoration"):
            credit=(s.get(side) or {}).get("credit") or ""
            if "CC BY-SA" in credit and "ShareAlike" not in credit:
                raise SystemExit("Batch 11 CC BY-SA credit needs a ShareAlike notice: "+n+" "+side)
    def b11(name):
        s=by[name]
        return " ".join([
            json.dumps(s.get("teach") or {}, ensure_ascii=False),
            (s.get("specimen") or {}).get("caption") or "",
            (s.get("restoration") or {}).get("caption") or "",
        ])
    if "Hindeodus parvus" not in b11("Meishan Section D (Permian–Triassic golden spike), Changxing, China") or "Bed 27c" not in b11("Meishan Section D (Permian–Triassic golden spike), Changxing, China"):
        raise SystemExit("Meishan must name Hindeodus parvus and Bed 27c")
    if "not a photograph" not in b11("Meishan Section D (Permian–Triassic golden spike), Changxing, China").lower():
        raise SystemExit("Meishan must say the rounds are not a photograph of the cliff")
    if "Psiloceras spelae" not in b11("Kuhjoch (Triassic–Jurassic golden spike), Karwendel, Austria") or "not the spike" not in b11("Kuhjoch (Triassic–Jurassic golden spike), Karwendel, Austria").lower():
        raise SystemExit("Kuhjoch must name the ammonite and say the village photo is not the spike")
    if "Dastilbe" not in b11("Crato Formation, Araripe Basin, Ceará, Brazil") or "Nova Olinda" not in b11("Crato Formation, Araripe Basin, Ceará, Brazil"):
        raise SystemExit("Crato must name Dastilbe and the Nova Olinda pin")
    if "Claraia" not in b11("The Dolomites (Schlern / Sciliar), Italy") or "not a piece of the cliff" not in b11("The Dolomites (Schlern / Sciliar), Italy").lower():
        raise SystemExit("Dolomites shell must be Claraia and not the Schlern cliff")
    if "not convinced" not in b11("Pilauco, Osorno, Chile").lower() or "sculptures" not in b11("Pilauco, Osorno, Chile").lower():
        raise SystemExit("Pilauco must say the footprint is disputed and the herd is sculptures")
    xh=b11("Xinhang fossil forest, Guangde, Anhui, China")
    if "Guangdedendron" not in xh or "not a Xinhang fossil" not in xh or "7.7" not in xh:
        raise SystemExit("Xinhang must name Guangdedendron, the stand-in root, and the 7.7 m estimate")
    if "not the oldest forest on Earth" not in xh:
        raise SystemExit("Xinhang must not claim to be the oldest forest on Earth")
    if "Fossil Trail" not in b11("Glossopteris trunks, Karoo National Park, South Africa") or "not the Lystrosaurus" not in b11("Glossopteris trunks, Karoo National Park, South Africa"):
        raise SystemExit("Karoo Glossopteris must be the Fossil Trail, not the Lystrosaurus pin")
    if "not a photograph" not in b11("Ventastega, Pavāri outcrop, Latvia").lower() or "walked on dry ground" not in b11("Ventastega, Pavāri outcrop, Latvia").lower():
        raise SystemExit("Ventastega must label the drawing and must not claim it walked on dry ground")
    doc={"lang":lang,"pin":T[lang]["pin"],"ui":en["ui"],"sites":en["sites"]}
    return doc

def fossil_li(s, t):
    if "teach" not in s:
        return f'<li>{html.escape(s["n"])} — <em>{t["pin"]}</em></li>'
    links=s.get("learnMore") or []
    if isinstance(links, dict): links=[links]
    more="".join(f' <a href="{html.escape(x["href"], quote=True)}">{html.escape(x.get("label") or "Learn more")}</a>' for x in links)
    rm=s.get("readMore") or {}
    if isinstance(rm, dict) and rm.get("href","").endswith(".html") and ".." not in rm.get("href",""):
        more=f' <a href="{html.escape(rm["href"], quote=True)}">{html.escape(rm.get("label") or "Read more")}</a>'+more
    pair=f' See also: {html.escape(s["pairWith"])}.' if s.get("pairWith") else ""
    return f'<li>{html.escape(s["n"])} — <em>{html.escape(s.get("era") or "")}</em>. {html.escape(s["teach"]["what"])}{pair}{more}</li>'

def rel(lang): return "" if lang=="en" else "../"
def url(lang,page): return DOM+"/"+("" if lang=="en" else lang+"/")+("" if page=="index" else page)

def nav(lang,page):
    t=T[lang]; X=EXTRA[lang]; r=rel(lang); sw=""
    for L in LANGS:
        c,n=NAMES[L]; href=("" if L=="en" else ("" if lang!="en" else "")+L+"/") 
        href=(r if lang!="en" else "")+("" if L=="en" else L+"/")+page+".html"
        cur=' aria-current="true"' if L==lang else ""
        sw+=f'<a class="spn-ls" role="switch" aria-checked="{str(L==lang).lower()}" href="{href}" hreflang="{L}" lang="{L}"{cur} aria-label="{n}" title="{n}" data-lang="{L}"><span class="spn-ls-t" aria-hidden="true"><span class="spn-ls-k"></span></span><span class="spn-ls-c" aria-hidden="true">{c}</span><span class="spn-ls-n" aria-hidden="true">{n}</span></a>'
    # Home stays on the logo only. Main items use the Saving Planets trigger class so spacing matches that nav.
    # Life over Time is the existing dropdown pattern (button.spn-trig + ul.spn-sub).
    def item(href, label):
        cur = ' aria-current="page"' if page+".html"==href else ""
        return f'<li><a class="spn-trig" href="{href}"{cur}>{label}</a></li>'
    # Smilodon is a child of Mammals, the same indented row the nav already styles with .spn-child.
    shelves = [
        ("Dinosaurs.html", DINO_NAV[lang], {"Dinosaurs", *FIND_SLUGS}, False),
        ("Mammals.html", life.SHELF_NAV["Mammals"][lang], {"Mammals"}, False),
        ("Smilodon.html", "Smilodon", {"Smilodon"}, True),
        ("Aerial.html", life.SHELF_NAV["Aerial"][lang], {"Aerial"}, False),
        ("Marine.html", life.SHELF_NAV["Marine"][lang], {"Marine"}, False),
    ]
    sub = "".join(
        f'<li{" class=\"spn-child\"" if child else ""}><a href="{href}"{" aria-current=\"page\"" if page in pages else ""}>{html.escape(label)}</a></li>'
        for href, label, pages, child in shelves
    )
    life_cls = "spn-dd is-current" if any(page in pages for _, _, pages, _child in shelves) else "spn-dd"
    life_item = (
        f'<li class="{life_cls}"><button type="button" class="spn-trig" aria-expanded="false" aria-haspopup="true" aria-controls="spn-life">'
        f'{html.escape(life.LIFE_NAV[lang])} <span class="spn-chev" aria-hidden="true"></span></button>'
        f'<ul class="spn-sub" id="spn-life">{sub}</ul></li>'
    )
    import edu_tracks
    courses_label = {"en": "Courses", "fr": "Cours", "es": "Cursos", "ar": "الدورات", "it": "Corsi", "he": "קורסים"}[lang]
    edu_label = {"en": "Education", "fr": "Éducation", "es": "Educación", "ar": "التعليم", "it": "Istruzione", "he": "חינוך"}[lang]
    edu_links = [
        ("Learn.html", X[1], {"Learn"}),
        ("Courses.html", courses_label, {"Courses"} | edu_tracks.COURSE_PAGES),
        ("Teachers.html", X[3], {"Teachers", "Lesson_Plan"}),
        ("Kids.html", X[2], {"Kids"}),
    ]
    edu_sub = "".join(
        f'<li><a class="edu-crystal" href="{href}"{" aria-current=\"page\"" if page in pages else ""}>{html.escape(label)}</a></li>'
        for href, label, pages in edu_links
    )
    edu_cls = "spn-dd is-current" if any(page in pages for _, _, pages in edu_links) else "spn-dd"
    edu_item = (
        f'<li class="{edu_cls}"><button type="button" class="spn-trig" aria-expanded="false" aria-haspopup="true" aria-controls="spn-edu">'
        f'{html.escape(edu_label)} <span class="spn-chev" aria-hidden="true"></span></button>'
        f'<ul class="spn-sub" id="spn-edu">{edu_sub}</ul></li>'
    )
    # Dig Quest stays off this bar. Kids Fossil Map stays in the footer.
    menu = (
        item("World_Map.html", t["map"])
        + life_item
        + item("Deep_Time.html", "Deep Time" if lang=="en" else DEEP_NAV[lang])
        + edu_item
        + item("Myth_vs_Fact.html", X[0])
        + item("Ways_to_Help.html", t["help"])
        + item("About.html", t["about"])
    )
    return f'''<nav id="topnav"><div class="spn"><a class="spn-brand" href="index.html"><span class="spn-logo"><img src="{r}assets/brand/sp-logo-72.png" srcset="{r}assets/brand/sp-logo-72.png 1x, {r}assets/brand/sp-logo-144.png 2x" width="72" height="72" alt="{t['brand']} logo, the Saving Planets globe"></span>{t['brand']}</a><button type="button" class="spn-toggle" aria-expanded="false" aria-controls="spn-panel" aria-label="Menu" data-open="Menu" data-close="Close"><span></span><span></span><span></span></button><div class="spn-panel" id="spn-panel"><ul class="spn-util" aria-label="Site links"><li class="lang-switch"><span class="spn-lt" role="group" aria-label="Language">{sw}</span></li><li><a href="Search.html">{t['search']}</a></li><li><a href="Contact.html">{t['contact']}</a></li><li class="nav-help"><a class="edu-crystal" href="Ways_to_Help.html">{t['help']}</a></li><li><a href="https://www.savingplanets.com/">{t['sister']}</a></li></ul><ul class="spn-main" aria-label="Main menu">{menu}</ul></div></div></nav>'''

TAGLINE={
"en":("Built on your ideas — so every lesson, search, and discovery here stays free, clear, sourced, and world-class for every classroom and family.","Why trust it: our 4.5-billion-year Earth voyage is cross-checked against NASA, Yale, Harvard, MIT, and other leading universities and scholars.","Our sources"),
"fr":("Construit à partir de vos idées — pour que chaque leçon, recherche et découverte reste gratuite, claire, sourcée et de classe mondiale pour chaque classe et chaque famille.","Pourquoi nous faire confiance : notre voyage de 4,5 milliards d’années est vérifié en croisant NASA, Yale, Harvard, MIT et d’autres grandes universités et chercheurs.","Nos sources"),
"es":("Creado a partir de sus ideas, para que cada lección, búsqueda y descubrimiento siga siendo gratuito, claro, con fuentes y de nivel mundial para cada aula y cada familia.","Por qué confiar: nuestro viaje de 4.500 millones de años se contrasta con la NASA, Yale, Harvard, el MIT y otras grandes universidades y académicos.","Nuestras fuentes"),
"ar":("مبني على أفكاركم — ليبقى كل درس وبحث واكتشاف هنا مجانيًا وواضحًا وموثّق المصادر وبمستوى عالمي لكل صف دراسي ولكل أسرة.","لماذا تثق بنا: رحلتنا عبر 4.5 مليار سنة من تاريخ الأرض تُراجَع بالمقارنة مع ناسا وييل وهارفارد ومعهد MIT وغيرها من كبرى الجامعات والعلماء.","مصادرنا"),
"it":("Costruito sulle vostre idee, perché ogni lezione, ricerca e scoperta resti gratuita, chiara, documentata e di livello mondiale per ogni classe e ogni famiglia.","Perché fidarsi: il nostro viaggio di 4,5 miliardi di anni è verificato incrociando NASA, Yale, Harvard, MIT e altre grandi università e studiosi.","Le nostre fonti"),
"he":("נבנה על בסיס הרעיונות שלכם — כדי שכל שיעור, חיפוש וגילוי כאן יישארו חינמיים, ברורים, מבוססי מקורות וברמה עולמית לכל כיתה ולכל משפחה.","למה לסמוך עלינו: המסע שלנו בן 4.5 מיליארד השנים נבדק מול נאס\"א, ייל, הרווארד, MIT ואוניברסיטאות וחוקרים מובילים נוספים.","המקורות שלנו"),
}
def tagline(lang):
    a,b,c=TAGLINE[lang]
    return f'<p class="footer-tagline" style="max-width:720px;margin:0 auto .9rem;text-align:center;font-style:italic;opacity:.9">{a}<br><span style="font-style:normal;font-size:.9em">{b} <a href="Policy.html">{c}</a></span></p>'
LOGO_CREDIT={"en":"Logo created by the Founder and SI","fr":"Logo créé par le fondateur et SI","es":"Logotipo creado por el fundador y SI","it":"Logo creato dal fondatore e da SI","ar":"الشعار من إعداد المؤسس وSI","he":"הלוגו נוצר על ידי המייסד ו-SI"}
def footer(lang):
    t=T[lang]; X=EXTRA[lang]
    return f'''<footer>{tagline(lang)}<div class="footer-map" role="navigation" aria-label="Site map"><div class="fm-col"><h2 class="fm-h">{t['brand']}</h2><ul><li><a href="index.html">{t['home']}</a></li><li><a href="World_Map.html">{t['map']}</a></li><li><a href="Dinosaurs.html">{DINO_NAV[lang]}</a></li><li><a href="Mammals.html">{life.SHELF_NAV["Mammals"][lang]}</a></li><li><a href="Aerial.html">{life.SHELF_NAV["Aerial"][lang]}</a></li><li><a href="Marine.html">{life.SHELF_NAV["Marine"][lang]}</a></li><li><a href="Deep_Time.html">{"Deep Time" if lang=="en" else DEEP_NAV[lang]}</a></li><li><a href="Smilodon.html">Smilodon</a></li><li><a href="Kids_Map.html">{t['kids']}</a></li><li><a href="Ways_to_Help.html">{t['help']}</a></li><li><a href="Search.html">{t['search']}</a></li><li><a href="Learn.html">{X[1]}</a></li><li><a href="Courses.html">{"Courses" if lang=="en" else {"fr":"Cours","es":"Cursos","ar":"الدورات","it":"Corsi","he":"קורסים"}[lang]}</a></li><li><a href="Lesson_Plan.html">{"Lesson plan" if lang=="en" else {"fr":"Plan de cours","es":"Plan de clase","ar":"خطة درس","it":"Piano di lezione","he":"מערך שיעור"}[lang]}</a></li><li><a href="Kids.html">{X[2]}</a></li><li><a href="Teachers.html">{X[3]}</a></li><li><a href="Myth_vs_Fact.html">{X[0]}</a></li><li><a href="About.html">{t['about']}</a></li><li><a href="Contact.html">{t['contact']}</a></li><li><a href="Policy.html">{"Policy" if lang=="en" else {"fr":"Politique","es":"Política","ar":"السياسة","it":"Politica","he":"מדיניות"}[lang]}</a></li></ul></div></div><p class="bsp-hook">{t['hook']}</p><p>&copy; 2026 Before Saving Planets • {t['foot']} <a href="https://www.savingplanets.com/">www.savingplanets.com</a></p><p class="dept-foot"><a href="mailto:{t['email']}">{t['email']}</a></p><p class="logo-credit">{LOGO_CREDIT[lang]}</p></footer>'''

# Cloudflare Web Analytics for beforesavingplanets.com.
# site_tag f1aab5fb2fc94a7b8e000d6565a6a9c7 is the dashboard id.
# The snippet uses site_token. The beacon lives in body(), so every generated page gets it.
CF_BEACON = "dd1b254bbc7b40b3a1967fe9e6053987"
BEACON = ("<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' "
          "data-cf-beacon='{\"token\": \""+CF_BEACON+"\"}'></script><!-- End Cloudflare Web Analytics -->")
INDEXABLE = {"index","Quest","Continents","Oceans","Seas","DeadSea","World_Map","Smilodon","Dinosaurs","Deep_Time","Borealopelta","Nigersaurus","Triceratops","Stegosaurus","Archaeopteryx","Dunkleosteus","Meganeura","Pterodactylus","Plesiosaurus","Mosasaurus","Otodus_megalodon","Argentavis","Haasts_eagle","Learn","Kids","Teachers","Courses","Lesson_Plan","Earth_Materials","Stratigraphic_Record","Field_Geology","World_Archaeology","Site_Context","Field_Methods","Geophysics","Sediments","Field_Camp","Animal_Bones","Site_Soils","Long_Essay"}
OG_LOCALE = {"en":"en_US","fr":"fr_FR","es":"es_ES","ar":"ar_AR","it":"it_IT","he":"he_IL"}
# Real photographs already on the site. Paths are root-absolute so every language shares one file.
OG = {
"index":("/assets/deep/photo-earth.webp","The Blue Marble, Earth photographed from Apollo 17 on 7 December 1972"),
"Quest":("/assets/deep/photo-earth.webp","The Blue Marble, Earth photographed from Apollo 17 on 7 December 1972"),
"Continents":("/assets/deep/photo-earth.webp","The Blue Marble, Earth photographed from Apollo 17 on 7 December 1972"),
"Oceans":("/assets/deep/photo-pacific.webp","Clouds over the northwestern Pacific, photographed from the International Space Station"),
"Seas":("/assets/deep/photo-gibraltar.webp","Satellite view of the Strait of Gibraltar on 30 December 2016"),
"DeadSea":("/assets/deep/photo-deadsea.webp","Landsat view of the Dead Sea, with the southern basin turned into evaporation ponds"),
"World_Map":("/assets/deep/photo-earth.webp","The Blue Marble, Earth photographed from Apollo 17 on 7 December 1972"),
"Deep_Time":("/assets/hero/paleo/earth.webp","A PALEOMAP frame of Earth’s coastlines"),
"Dinosaurs":("/assets/finds/stegosaurus-1600.webp","Stegosaurus mount at the American Museum of Natural History"),
"Smilodon":("/assets/smilodon/hero-1600.webp","Smilodon fatalis skeleton at the La Brea Tar Pits Museum"),
"Borealopelta":("/assets/finds/borealopelta-1600.webp","Borealopelta fossil at the Royal Tyrrell Museum"),
"Nigersaurus":("/assets/finds/nigersaurus-1600.webp","Scientific figure of the Nigersaurus taqueti skull"),
"Triceratops":("/assets/finds/triceratops-1600.webp","Triceratops mount at the Ulster Museum"),
"Stegosaurus":("/assets/finds/stegosaurus-1600.webp","Stegosaurus mount at the American Museum of Natural History"),
}
KW = {
"en":{
"index":"fossils, deep time, Earth history, ancient climates, Before Saving Planets",
"Quest":"Dig Quest, geologic time, Earth formation, Ice Age, deep time",
"Continents":"plate tectonics, Pangaea, continents, Himalayas, East African Rift",
"Oceans":"oceans, first oceans, Earth water, Pacific Ocean",
"Seas":"seas, Mediterranean, Strait of Gibraltar, Zanclean flood",
"DeadSea":"Dead Sea, rift valley, shrinking lake, salt lake",
"World_Map":"fossil map, fossil sites, lagerstätten, first forests, deep time",
"Smilodon":"Smilodon, saber-toothed cat, La Brea, felid, not a tiger",
"Dinosaurs":"dinosaur fossils, Borealopelta, Nigersaurus, Triceratops, Stegosaurus",
"Deep_Time":"deep time, PALEOMAP, geologic periods, mass extinctions, Milky Way",
"Borealopelta":"Borealopelta, nodosaur, Royal Tyrrell Museum, Albian, armored dinosaur",
"Nigersaurus":"Nigersaurus, sauropod, Gadoufaoua, Aptian, Albian",
"Triceratops":"Triceratops, Hell Creek, Maastrichtian, Tyrannosaurus, horned dinosaur",
"Stegosaurus":"Stegosaurus, Morrison Formation, Kimmeridgian, plated dinosaur",
"About":"Before Saving Planets, Saving Planets, deep time",
"Ways_to_Help":"citizen science, museum volunteering, fossil collecting",
"Search":"search Before Saving Planets, fossil sites, deep time",
"Myth_vs_Fact":"Earth myths, fossil facts, sourced claims",
"Learn":"Earth lessons, fossil lessons",
"Kids":"kids Earth science, fossils for children",
"Teachers":"classroom Earth science, fossil lessons for teachers",
"Contact":"contact Before Saving Planets, corrections, questions",
"Kids_Map":"kids fossil map, trilobites, dinosaurs, Ice Age",
},
"fr":{
"index":"fossiles, temps profond, histoire de la Terre, climats anciens",
"Quest":"Dig Quest, temps géologique, formation de la Terre, ère glaciaire",
"Continents":"tectonique des plaques, Pangée, continents, Himalaya",
"Oceans":"océans, premiers océans, eau de la Terre",
"Seas":"mers, Méditerranée, détroit de Gibraltar, Zancléen",
"DeadSea":"mer Morte, rift, lac salé",
"World_Map":"carte des fossiles, lagerstätten, premières forêts, temps profond",
"Smilodon":"Smilodon, chat à dents de sabre, La Brea, félidé",
"Dinosaurs":"fossiles de dinosaures, Borealopelta, Nigersaurus, Triceratops, Stegosaurus",
"Deep_Time":"temps profond, PALEOMAP, périodes géologiques, extinctions, Voie lactée",
"Borealopelta":"Borealopelta, nodosaure, Royal Tyrrell Museum, Albien",
"Nigersaurus":"Nigersaurus, sauropode, Gadoufaoua, Aptien",
"Triceratops":"Triceratops, Hell Creek, Maastrichtien, dinosaure à cornes",
"Stegosaurus":"Stegosaurus, formation de Morrison, Kimméridgien",
"About":"Before Saving Planets, Saving Planets, temps profond",
"Ways_to_Help":"science participative, bénévolat en musée, collecte de fossiles",
"Search":"recherche Before Saving Planets, sites fossilifères, temps profond",
"Myth_vs_Fact":"mythes sur la Terre, faits sur les fossiles",
"Learn":"leçons sur la Terre, leçons sur les fossiles",
"Kids":"sciences de la Terre pour enfants, fossiles",
"Teachers":"sciences de la Terre en classe, fossiles pour enseignants",
"Contact":"contacter Before Saving Planets, corrections, questions",
"Kids_Map":"carte des fossiles pour enfants, trilobites, dinosaures",
},
"es":{
"index":"fósiles, tiempo profundo, historia de la Tierra, climas antiguos, Before Saving Planets",
"Quest":"Dig Quest, tiempo geológico, formación de la Tierra, era de hielo, tiempo profundo",
"Continents":"tectónica de placas, Pangea, continentes, Himalaya, rift de África oriental",
"Oceans":"océanos, primeros océanos, agua de la Tierra, océano Pacífico",
"Seas":"mares, Mediterráneo, estrecho de Gibraltar, inundación zancliense",
"DeadSea":"mar Muerto, valle de rift, lago salado",
"World_Map":"mapa de fósiles, yacimientos, lagerstätten, primeros bosques, tiempo profundo",
"Smilodon":"Smilodon, félido de dientes de sable, La Brea, no es un tigre",
"Dinosaurs":"fósiles de dinosaurios, Borealopelta, Nigersaurus, Triceratops, Stegosaurus",
"Deep_Time":"tiempo profundo, PALEOMAP, períodos geológicos, extinciones masivas, Vía Láctea",
"Borealopelta":"Borealopelta, nodosaurio, Royal Tyrrell Museum, Albiense, dinosaurio acorazado",
"Nigersaurus":"Nigersaurus, saurópodo, Gadoufaoua, Aptiense, Albiense",
"Triceratops":"Triceratops, Hell Creek, Maastrichtiense, Tyrannosaurus, dinosaurio con cuernos",
"Stegosaurus":"Stegosaurus, Formación Morrison, Kimmeridgiense, dinosaurio con placas",
"About":"Before Saving Planets, Saving Planets, tiempo profundo",
"Ways_to_Help":"ciencia ciudadana, voluntariado en museos, recolección de fósiles",
"Search":"buscar en Before Saving Planets, yacimientos, tiempo profundo",
"Myth_vs_Fact":"mitos sobre la Tierra, hechos sobre fósiles, afirmaciones con fuentes",
"Learn":"lecciones sobre la Tierra, lecciones sobre fósiles",
"Kids":"ciencias de la Tierra para niños, fósiles",
"Teachers":"ciencias de la Tierra en el aula, fósiles para docentes",
"Contact":"contacto Before Saving Planets, correcciones, preguntas",
"Kids_Map":"mapa de fósiles para niños, trilobites, dinosaurios, era de hielo",
},
"it":{
"index":"fossili, tempo profondo, storia della Terra, climi antichi, Before Saving Planets",
"Quest":"Dig Quest, tempo geologico, formazione della Terra, era glaciale, tempo profondo",
"Continents":"tettonica delle placche, Pangea, continenti, Himalaya, rift dell’Africa orientale",
"Oceans":"oceani, primi oceani, acqua della Terra, oceano Pacifico",
"Seas":"mari, Mediterraneo, stretto di Gibilterra, alluvione zancleana",
"DeadSea":"mar Morto, valle del rift, lago salato",
"World_Map":"mappa dei fossili, siti fossili, lagerstätten, prime foreste, tempo profondo",
"Smilodon":"Smilodon, felide dai denti a sciabola, La Brea, non è una tigre",
"Dinosaurs":"fossili di dinosauri, Borealopelta, Nigersaurus, Triceratops, Stegosaurus",
"Deep_Time":"tempo profondo, PALEOMAP, periodi geologici, estinzioni di massa, Via Lattea",
"Borealopelta":"Borealopelta, nodosauro, Royal Tyrrell Museum, Albiano, dinosauro corazzato",
"Nigersaurus":"Nigersaurus, sauropode, Gadoufaoua, Aptiano, Albiano",
"Triceratops":"Triceratops, Hell Creek, Maastrichtiano, Tyrannosaurus, dinosauro con le corna",
"Stegosaurus":"Stegosaurus, Formazione Morrison, Kimmeridgiano, dinosauro con le placche",
"About":"Before Saving Planets, Saving Planets, tempo profondo",
"Ways_to_Help":"citizen science, volontariato nei musei, raccolta di fossili",
"Search":"cerca su Before Saving Planets, siti fossili, tempo profondo",
"Myth_vs_Fact":"miti sulla Terra, fatti sui fossili, affermazioni con fonti",
"Learn":"lezioni sulla Terra, lezioni sui fossili",
"Kids":"scienze della Terra per bambini, fossili",
"Teachers":"scienze della Terra in classe, fossili per insegnanti",
"Contact":"contatto Before Saving Planets, correzioni, domande",
"Kids_Map":"mappa dei fossili per bambini, trilobiti, dinosauri, era glaciale",
},
"ar":{
"index":"أحافير, زمن عميق, تاريخ الأرض, مناخات قديمة, Before Saving Planets",
"Quest":"Dig Quest, زمن جيولوجي, تكوّن الأرض, عصر جليدي, زمن عميق",
"Continents":"تكتونية الصفائح, بانجيا, قارات, جبال الهيمالايا, الصدع الأفريقي",
"Oceans":"محيطات, المحيطات الأولى, ماء الأرض, المحيط الهادئ",
"Seas":"بحار, البحر المتوسط, مضيق جبل طارق, الفيض الزانكلي",
"DeadSea":"البحر الميت, وادي صدع, بحيرة مالحة",
"World_Map":"خريطة الأحافير, مواقع أحافير, لاغرشتاتن, الغابات الأولى, زمن عميق",
"Smilodon":"Smilodon, قط ذو أسنان سيفية, لا بريا, ليس نمراً",
"Dinosaurs":"أحافير ديناصورات, Borealopelta, Nigersaurus, Triceratops, Stegosaurus",
"Deep_Time":"زمن عميق, PALEOMAP, فترات جيولوجية, انقراضات جماعية, درب التبانة",
"Borealopelta":"Borealopelta, نودوصور, متحف رويال تيريل, الألبي, ديناصور مدرّع",
"Nigersaurus":"Nigersaurus, سوروبود, غادوفاوا, الأبتي, الألبي",
"Triceratops":"Triceratops, هل كريك, الماستريختي, تيرانوصور, ديناصور بقرون",
"Stegosaurus":"Stegosaurus, تكوين موريسون, الكيمريدجي, ديناصور بصفائح",
"About":"Before Saving Planets, Saving Planets, زمن عميق",
"Ways_to_Help":"علم المواطن, تطوع في المتاحف, جمع الأحافير",
"Search":"بحث في Before Saving Planets, مواقع أحافير, زمن عميق",
"Myth_vs_Fact":"خرافات عن الأرض, حقائق عن الأحافير, ادعاءات بمصادر",
"Learn":"دروس عن الأرض, دروس عن الأحافير",
"Kids":"علوم الأرض للأطفال, أحافير",
"Teachers":"علوم الأرض في الصف, أحافير للمعلمين",
"Contact":"الاتصال بـ Before Saving Planets, تصحيحات, أسئلة",
"Kids_Map":"خريطة أحافير للأطفال, ثلاثيات الفصوص, ديناصورات, عصر جليدي",
},
"he":{
"index":"מאובנים, זמן עמוק, היסטוריית כדור הארץ, אקלים קדום, Before Saving Planets",
"Quest":"Dig Quest, זמן גאולוגי, היווצרות כדור הארץ, עידן קרח, זמן עמוק",
"Continents":"טקטוניקת הלוחות, פנגיאה, יבשות, ההימלאיה, הבקע המזרח-אפריקני",
"Oceans":"אוקיינוסים, האוקיינוסים הראשונים, מי כדור הארץ, האוקיינוס השקט",
"Seas":"ימים, הים התיכון, מצר גיברלטר, ההצפה הזנקליאנית",
"DeadSea":"ים המלח, בקע, אגם מלוח",
"World_Map":"מפת מאובנים, אתרי מאובנים, לגרשטטן, יערות ראשונים, זמן עמוק",
"Smilodon":"Smilodon, חתול בעל שיניים חרביות, לה בריאה, לא טיגריס",
"Dinosaurs":"מאובני דינוזאורים, Borealopelta, Nigersaurus, Triceratops, Stegosaurus",
"Deep_Time":"זמן עמוק, PALEOMAP, תקופות גאולוגיות, הכחדות המוניות, שביל החלב",
"Borealopelta":"Borealopelta, נודוזאור, מוזיאון רויאל טיירל, אלביאן, דינוזאור משוריין",
"Nigersaurus":"Nigersaurus, זאורופוד, גדופאווה, אפטיאן, אלביאן",
"Triceratops":"Triceratops, הל קריק, מאסטריכטיאן, טירנוזאורוס, דינוזאור בעל קרניים",
"Stegosaurus":"Stegosaurus, תצורת מוריסון, קימרידג'יאן, דינוזאור בעל לוחות",
"About":"Before Saving Planets, Saving Planets, זמן עמוק",
"Ways_to_Help":"מדע אזרחי, התנדבות במוזיאונים, איסוף מאובנים",
"Search":"חיפוש ב-Before Saving Planets, אתרי מאובנים, זמן עמוק",
"Myth_vs_Fact":"מיתוסים על כדור הארץ, עובדות על מאובנים, טענות עם מקורות",
"Learn":"שיעורים על כדור הארץ, שיעורים על מאובנים",
"Kids":"מדעי כדור הארץ לילדים, מאובנים",
"Teachers":"מדעי כדור הארץ בכיתה, מאובנים למורים",
"Contact":"יצירת קשר עם Before Saving Planets, תיקונים, שאלות",
"Kids_Map":"מפת מאובנים לילדים, טרילוביטים, דינוזאורים, עידן קרח",
},
}

def keywords_for(lang, page):
    if lang not in KW:
        raise SystemExit("missing keyword language: "+lang)
    if page not in KW[lang]:
        raise SystemExit("missing keywords for "+lang+" "+page)
    return KW[lang][page]

def og_for(lang, page):
    path, _alt = OG.get(page, OG["index"])
    return DOM+path, seo_copy.image_alt(lang, page)

def head(lang,page,title,desc,extra=""):
    r=rel(lang); alts="".join(f'<link rel="alternate" hreflang="{L}" href="{url(L,page)}">' for L in LANGS)
    # Home sky uses the Saving Planets Enceladus poster (no colored Earth). Other pages do not preload it.
    if page=="index":
        pre=('<link rel="preload" as="image" href="https://www.savingplanets.com/assets/Threetrees3-1320.webp" fetchpriority="high">')
        theme="#0b3a5b"
    else:
        pre=""
        theme="#2a1a0e"
    canon=url(lang,page)
    full_title=f"{title} | Before Saving Planets"
    image, image_alt=og_for(lang, page)
    robots="index,follow" if page in INDEXABLE else "noindex,follow"
    ld={
      "@context":"https://schema.org",
      "@graph":[
        {"@type":"WebSite","@id":DOM+"/#website","name":"Before Saving Planets","url":DOM+"/","inLanguage":LANGS,
         "publisher":{"@type":"Organization","name":"Before Saving Planets","url":DOM+"/"}},
        {"@type":"WebPage","@id":canon+"#webpage","url":canon,"name":full_title,"description":desc,
         "inLanguage":lang,"isPartOf":{"@id":DOM+"/#website"},
         "primaryImageOfPage":{"@type":"ImageObject","url":image,"caption":image_alt}},
      ],
    }
    ld_json=json.dumps(ld, ensure_ascii=False).replace("<","\\u003c")
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if lang in RTL else 'ltr'}" class="dark">
<head>
<meta charset="UTF-8"><meta name="color-scheme" content="dark"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">{alts}<link rel="alternate" hreflang="x-default" href="{url('en',page)}">
<title>{html.escape(full_title)}</title><meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(full_title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:site_name" content="Before Saving Planets"><meta property="og:locale" content="{OG_LOCALE[lang]}">{"".join(f'<meta property="og:locale:alternate" content="{OG_LOCALE[L]}">' for L in LANGS if L!=lang)}
<meta property="og:image" content="{image}"><meta property="og:image:alt" content="{html.escape(image_alt)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(full_title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{image}"><meta name="twitter:image:alt" content="{html.escape(image_alt)}">
<script type="application/ld+json">{ld_json}</script>
<link rel="icon" href="{r}favicon.ico"><link rel="icon" type="image/png" sizes="32x32" href="{r}assets/brand/favicon-32.png"><link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest"><meta name="theme-color" content="{theme}">
<link rel="preload" href="{r}assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
{pre}<link rel="stylesheet" href="{r}styles.css"><link rel="stylesheet" href="{r}extras.css"><link rel="stylesheet" href="{r}bsp.css">{extra}
</head>
'''

CHILD_PAGES = {"Kids", "Kids_Map"}

def body(lang,page,main,cls="toc-sub",scripts=""):
    r=rel(lang)
    child = page in CHILD_PAGES
    # Children's pages do not load visit analytics and do not grow the newsletter list.
    attr = " data-no-newsletter" if child else ""
    beacon = "" if child else "\n"+BEACON
    help = "" if child else f'<a class="sticky-help" href="Ways_to_Help.html">{html.escape(T[lang]["help"])}</a>'
    return f'''<body class="{cls}" data-glass-tint="site"{attr}><a class="skip-link" href="#main">Skip</a>
{nav(lang,page)}
{main}
{help}
{footer(lang)}
<script src="{r}site.js"></script>{scripts}{beacon}
</body></html>'''

HERO_SVG = open(os.path.join(ROOT,"scripts","hero.html")).read()

def page_hero(title,desc,t):
    return f'<section class="page-hero bsp-page-hero"><div class="bsp-strata" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div><div class="page-hero-content"><h1>{title}</h1><p>{desc}</p></div></section>'

def placeholder(t,n=3):
    return '<div class="edu-wrap bsp-wrap">'+f'<p class="bsp-ph" role="note">⚠ {t["ph"]}</p>'+"".join(f'<section class="bsp-card"><h2>[Placeholder section {i}]</h2><p>{t["ph"]}</p></section>' for i in range(1,n+1))+f'<p class="bsp-hook">{t["hook"]}</p></div>'


# ---- Dig Quest (English copy; other languages TODO machine-draft translation) ----
QCTA="Start the Dig Quest"
HCRED="Lava, early oceans, and the Pangaea rift: artist’s interpretation (SI), not a photograph. From 540 Ma: Scotese PALEOMAP via GPlates (EarthByte). Finish: NASA Blue Marble, public domain."
SP="https://www.savingplanets.com/"
LAYERS=[
 ("Earth forms","4.54 billion years ago","#7a2a12","🪨",
  "Dust and gas around the young Sun clumped into rocks, the rocks collided and merged, and Earth grew. Scientists date Earth to 4.54 billion years (less than 1% uncertainty) using lead isotopes and meteorites.",
  [("USGS — Age of the Earth","https://pubs.usgs.gov/gip/geotime/age.html"),("NASA — Formation of the Solar System","https://mobile.arc.nasa.gov/public/iexplore/missions/pages/yss/november.html")],
  ("layer-earth.webp",1400,1120,
   "Artist’s concept of a dusty disk around a young star, where planets can form.",
   "Artist’s concept of a dusty planet-forming disk around the young star IRS 46. This is not a photograph of the early Earth.",
   "NASA/JPL-Caltech, public domain.",
   "https://commons.wikimedia.org/wiki/File:IRS46_nasa.jpg"),"Earth healed from fire into a living world. See what we’re doing for it today.",("Today’s solutions",SP)),
 ("The Moon is born","about 4.5 billion years ago","#8a3b1c","🌕",
  "A Mars-size body called Theia likely struck young Earth. The debris formed the Moon. Apollo rocks show the Moon formed about 60 million years after the solar system began and was once covered by a magma ocean.",
  [("NASA Science — Moon Formation","https://science.nasa.gov/moon/formation/")],
  ("layer-moon.webp",1024,1024,
   "Apollo 15 lunar sample 15415, the Genesis Rock, on a laboratory stand with a scale.",
   "Apollo 15 lunar sample 15415, called the Genesis Rock. It is a piece of the Moon’s early crust.",
   "NASA, public domain.",
   "https://commons.wikimedia.org/wiki/File:Apollo_15_Genesis_Rock.jpg"),"The Moon drives our tides, which shape coasts and ocean life.",("Ocean solutions",SP+"Oceans.html")),
 ("First crust and water","4.4 billion years ago","#6e4526","💧",
  "A tiny zircon crystal from the Jack Hills of Western Australia is 4.404 billion years old — the oldest known piece of Earth. Its chemistry points to continental crust and liquid water very early on.",
  [("Wilde et al., Nature 409:175 (2001)","https://doi.org/10.1038/35051550")],
  ("layer-jack-hills.webp",1400,1001,
   "Polished quartz-pebble rock from the Jack Hills, Western Australia. Zircon grains older than 4 billion years come from this kind of rock.",
   "Jack Hills host rock. The oldest known zircon grains, about 4.4 billion years old, come from rock like this. This is not a microscope photo of one crystal.",
   "James St. John, CC BY 2.0, via Wikimedia Commons. Resized for this page.",
   "https://commons.wikimedia.org/wiki/File:Quartz-pebble_metaconglomerate_(Jack_Hills_Quartzite,_Archean,_2.65_to_3.05_Ga;_Jack_Hills,_Western_Australia)_2.jpg"),"Earth’s first oceans became today’s oceans. Help protect them.",("Ocean solutions",SP+"Oceans.html")),
 ("Oxygen arrives","about 2.4 billion years ago","#5b3820","🫧",
  "Tiny ocean microbes, likely ancestors of cyanobacteria, made oxygen by photosynthesis. Around 2.4 billion years ago oxygen built up in the air — the Great Oxidation Event — paving the way for complex life.",
  [("NASA Astrobiology — Great Oxidation Event","https://astrobiology.nasa.gov/news/oxygen-production-in-earths-early-oceans-predates-the-great-oxidation-event/"),("NOAA Climate.gov — Coldest Earth","https://www.climate.gov/news-features/climate-qa/whats-coldest-earths-ever-been")],
  ("layer-stromatolite.webp",1400,933,
   "A fossil stromatolite, a layered mound built by ancient microbes, on Pitamakan Pass in Glacier National Park.",
   "Fossil stromatolite on Pitamakan Pass, Glacier National Park.",
   "Glacier National Park, National Park Service, public domain.",
   "https://commons.wikimedia.org/wiki/File:Stromatolite_Fossil_on_Pitamakan_Pass_(29305962428).jpg"),"Forests and ocean plants still make the oxygen we breathe.",("Forest solutions",SP+"Deforestation.html")),
 ("Life explodes in the sea","508 million years ago","#4a5a3a","🐚",
  "The Burgess Shale in the Canadian Rockies preserves soft-bodied sea animals from the Cambrian, 508 million years ago, recording the rapid diversification of life called the “Cambrian Explosion.” Charles Walcott collected some 65,000 specimens there for the Smithsonian.",
  [("Smithsonian Ocean — Ocean Through Time","https://www.ocean.si.edu/through-time/ocean-through-time")],
  ("layer-burgess.webp",1280,960,
   "Fossil of Anomalocaris canadensis, a Burgess Shale predator, on display. This photo may show a museum cast.",
   "Anomalocaris canadensis from the Burgess Shale. The photo was taken at CosmoCaixa in Barcelona and may show a museum cast.",
   "Esv, CC BY-SA 3.0, via Wikimedia Commons. ShareAlike: remixes keep the same license. Resized for this page.",
   "https://commons.wikimedia.org/wiki/File:Anomalocaris_canadensis_fossil.jpg"),"Today’s reefs carry on those first ocean worlds.",("Coral reef restoration",SP+"Coral_Restoration_Foundation.html")),
 ("The Great Dying","about 252 million years ago","#3b2618","🌋",
  "The end-Permian extinction was the largest in Earth’s history: about 96% of species were lost. Massive volcanic eruptions in Siberia released carbon dioxide, linked to warming and ocean acidification. Life took millions of years to recover — but it did.",
  [("National Park Service — Mass Extinctions","https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm"),("Smithsonian NMNH — Extinction Over Time","https://naturalhistory.si.edu/education/teaching-resources/paleontology/extinction-over-time")],
  ("layer-brachiopod.webp",800,525,
   "A fossil brachiopod in the Permian Kaibab Formation, with small round crinoid pieces in the rock around it.",
   "A Permian brachiopod in the Kaibab Formation, Grand Canyon, with scattered crinoid pieces.",
   "National Park Service, public domain.",
   "https://commons.wikimedia.org/wiki/File:Kaibab_Formation_-_fossil_brachiopod_and_crinoid_columnals.jpg"),"CO₂ and acidifying oceans are back. Reef rescuers are fighting it.",("Coral reef restoration",SP+"Coral_Restoration_Foundation.html")),
 ("Asteroid and recovery","66 million years ago","#2e2a3a","☄️",
  "An asteroid 10–20 km wide struck near today’s Yucatán, forming the Chicxulub crater. About 76% of species died out, including all dinosaurs except birds. Mammals then flourished.",
  [("National Park Service — Mass Extinctions","https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm")],
  ("layer-chicxulub.webp",715,799,
   "NASA radar map of the Yucatán Peninsula. A faint arc marks the buried Chicxulub crater.",
   "Radar map of the Yucatán. The faint arc is the rim of the buried Chicxulub crater.",
   "NASA/JPL-Caltech, public domain. Shuttle Radar Topography Mission.",
   "https://commons.wikimedia.org/wiki/File:Chicxulub_radar_topography.jpg"),"After disasters, forests regrow. See who helps them today.",("Forest solutions",SP+"Deforestation.html")),
 ("The last Ice Age","20,000 years ago","#2a4a6a","🧊",
  "At the Last Glacial Maximum, about 20,000 years ago, ice sheets covered Canada and northern Europe and sea level was about 120 meters lower. Ice cores from Greenland and Antarctica record this climate history year by year.",
  [("NOAA Ocean Explorer — Paleoclimate","https://archive.oceanexplorer.noaa.gov/explorations/05stepstones/background/paleoclimate/paleoclimate.html"),("NASA — The Ice Core Record","https://science.nasa.gov/earth/earth-observatory/paleoclimatology-the-ice-core-record/")],
  ("layer-ice-core.webp",741,335,
   "A slice of the GISP2 ice core from Greenland, lit from below so the yearly light and dark layers show.",
   "Greenland ice from the GISP2 drill, 1,855 meters down. The stripes are years of snow.",
   "NOAA, public domain.",
   "https://commons.wikimedia.org/wiki/File:GISP2_1855m_ice_core_layers.png"),"Ice holds Earth’s memory. Meet the people protecting the poles.",("Polar solutions",SP+"Polar.html")),
]
def hot(i):
    k=HOT.get(i,[])
    if not k: return ""
    return '<div class="q-hot" role="group" aria-label="Dig deeper">'+"".join(f'<a class="q-hotspot" href="{d}.html"><span class="q-pulse" aria-hidden="true"></span>🔎 Dig deeper: {DEEP[d][0]}</a>' for d in k)+'</div>'
def deep(lang,key):
    _en_title,_en_sub,img,cap,facts,src,(bt,bl,bu)=DEEP[key]; r=rel(lang)
    title,sub=seo_copy.DEEP[key][lang]
    note="" if lang=="en" else '<p class="bsp-ph" role="note">TODO machine-draft translation: English for review.</p>'
    la="" if lang=="en" else ' lang="en"'
    fs="".join(f'<section class="bsp-card d-fact"><h2>{h}</h2><p>{b}</p></section>' for h,b in facts)
    cites="".join(f'<li><a href="{u}" rel="noopener">{a}</a></li>' for a,u in src)
    others="".join(f'<a class="q-hotspot" href="{k}.html">{v[0]}</a>' for k,v in DEEP.items() if k!=key)
    photo=PHOTOS[key]
    shot=(f'<figure class="d-fig d-photo"><img src="{r}assets/deep/{photo["file"]}" width="{photo["w"]}" height="{photo["h"]}" alt="{html.escape(photo["alt"])}" loading="lazy">'
          f'<figcaption>{html.escape(photo["cap"])}<br><small>{html.escape(photo["credit"])} <a href="{html.escape(photo["href"], quote=True)}" rel="noopener noreferrer">File page</a></small></figcaption></figure>')
    render=(f'<figure class="d-fig"><img src="{r}assets/deep/{img}" width="1024" height="576" alt="{html.escape(cap)}" loading="eager"><figcaption>{cap}<br><small>{CR}</small></figcaption></figure>')
    return (f'<main id="main">'+page_hero(title,sub,None)+f'<div class="edu-wrap bsp-wrap"{la}>{note}<div class="d-figs">{render}{shot}</div>{fs}'
            f'<section class="bsp-card"><h2>Sources</h2><ul class="q-src">{cites}</ul></section><div class="q-bridge"><span>🌍 {bt}</span><a href="{bu}">{bl} on Saving Planets →</a></div>'
            f'<p class="q-hot">Keep digging: {others} · <a href="Deep_Time.html">Deep Time</a></p></div></main>')
# Burgess layer only. The model is Anomalocaris canadensis, already the Emu Bay coin’s
# second picture, and the fossil below it is the Burgess specimen. Other quest layers
# have no life picture of that subject already on the site.
QUEST_LIFE={
 "Life explodes in the sea":(
  "layer-anomalocaris-life.webp",1080,720,
  "Museum model of Anomalocaris canadensis from the Burgess Shale. This is a photo of a model, not the fossil.",
  "Matteo De Stefano / MUSE, Science Museum of Trento, CC BY-SA 3.0, via Wikimedia Commons. Photo of a model.",
  "https://commons.wikimedia.org/wiki/File:Anomalocaris_canadensis_-_reconstruction_-_MUSE.jpg"),
}
def quest(lang):
    en = lang=="en"
    note = "" if en else '<p class="bsp-ph" role="note">TODO machine-draft translation: quest copy below is English for review.</p>'
    la = "" if en else ' lang="en"'
    out=f'<div class="edu-wrap bsp-wrap"{la}>{note}<p class="q-intro">The Dig Quest tour is retired. These sourced layers stay on this page so the facts remain readable. Deep Time and the fossil map are the way through the rest of the record.</p><p><a href="Deep_Time.html">Deep Time</a> · <a href="World_Map.html">Fossil map</a> · <a href="Continents.html">Continents</a> · <a href="Oceans.html">Oceans</a> · <a href="Seas.html">Seas</a> · <a href="DeadSea.html">The Dead Sea</a></p><div class="q-dig">'
    r=rel(lang)
    for i,(name,age,col,ic,fact,src,img,bridge,(bl,bu)) in enumerate(LAYERS):
        fn,w,h,alt,cap,credit,filepage=img
        cites="".join(f'<li><a href="{u}" rel="noopener">{html.escape(a)}</a></li>' for a,u in src)
        fig=""
        life=QUEST_LIFE.get(name)
        if life:
            lfn,lw,lh,lcap,lcredit,lpage=life
            if not os.path.isfile(os.path.join(ROOT,"assets","quest",lfn)):
                raise SystemExit("quest life picture missing: "+lfn)
            fig+=(f'<figure class="q-fig q-life"><img src="{r}assets/quest/{lfn}" width="{lw}" height="{lh}" alt="{html.escape(lcap)}" loading="lazy">'
                  f'<figcaption>Life restoration. {html.escape(lcap)}<br><small>{html.escape(lcredit)} <a href="{html.escape(lpage, quote=True)}" rel="noopener noreferrer">File page</a></small></figcaption></figure>')
        fig+=(f'<figure class="q-fig"><img src="{r}assets/quest/{fn}" width="{w}" height="{h}" alt="{html.escape(alt)}" loading="lazy">'
             f'<figcaption>{"Fossil. " if life else ""}{html.escape(cap)}<br><small>{html.escape(credit)} <a href="{html.escape(filepage, quote=True)}" rel="noopener noreferrer">File page</a></small></figcaption></figure>')
        out+=(f'<section class="q-layer" style="--q:{col}" id="q{i}"><h2>Layer {i+1}: {html.escape(name)} <span class="q-age">({html.escape(age)})</span></h2>'
              f'<div class="q-body">{fig}<p>{fact}</p><p class="q-src">Sources:</p><ul class="q-src">{cites}</ul>'+
              hot(i)+f'<div class="q-bridge"><span>🌍 {bridge}</span><a href="{bu}">{bl} on Saving Planets →</a></div></div></section>')
    out+=f'</div><p class="bsp-hook">You reached today. <a href="{SP}">Continue the story with solutions on Saving Planets →</a></p></div>'
    return out
def quest_teaser(lang):
    q_title,_q_desc,_q_hero,q_tease=seo_copy.QUEST[lang]
    return f'<div class="edu-wrap bsp-wrap"><section class="bsp-card"><h2>{q_title}</h2><p>{q_tease}</p><p><a class="btn hero-cta" href="Quest.html">{QCTA}</a> <a class="btn hero-cta2" href="Quest.html#time-scrubber">{GLOBE[lang]["scrub"]}</a></p></section></div>'

def story_block(lang):
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
    return f'<div class="bsp-eras">{"".join(cards)}</div>'

# Teach-first cards for the four Dig Quest globe pairs. Same order as GLOBE pairs.
# Burgess is pair 0. Its pin used to be a checked radio with no opener, so a click did nothing.
PIN_CARDS=[
 dict(what="A mudslide buried a sea floor so fast that soft bodies, including legs, guts, and eyes, turned to stone. One animal from these rocks is Anomalocaris, a top hunter of that sea.",
      when="The Royal Ontario Museum dates Anomalocaris canadensis to the Wuliuan stage of the Middle Cambrian, about 505 million years ago.",
      where="High in the Rocky Mountains of Yoho National Park, British Columbia, Canada.",
      why="It is one of the best snapshots of the Cambrian explosion, when most animal body plans first appeared.",
      now="The Coral Restoration Foundation in the Florida Keys grows corals in nurseries and plants them back on the reef. Today’s reefs carry on those early ocean worlds."),
 dict(what="Buried under Mexico’s Yucatán is a crater about 180 km wide, made when an asteroid roughly 10 km across hit Earth.",
      when="About 66 million years ago.",
      where="Under the Yucatán Peninsula, Mexico.",
      why="The blast and the years of darkness after it ended the age of dinosaurs and opened the world for mammals.",
      now="The Cristalino forest in Brazil is protected so a living forest can keep standing."),
 dict(what="Inside these hills are crystals smaller than a grain of sand, called zircons. One was dated to about 4.4 billion years, Earth’s oldest known piece.",
      when="About 4.4 billion years ago, when the planet was only about 150 million years old.",
      where="The Jack Hills, Western Australia.",
      why="Its chemistry hints that Earth already had continental crust and liquid water very early.",
      now="Cairns sits on the Great Barrier Reef coast, where people work to protect the ocean."),
 dict(what="On top of Greenland, each year’s snow makes a thin layer, like tree rings made of ice. Drills named GISP2 and NGRIP counted those layers.",
      when="From the last warm period, about 123,000 years ago, through today.",
      where="GISP2, on the Greenland ice sheet.",
      why="The ice shows that climate can flip suddenly, in just decades.",
      now="Syowa Station, on the East Antarctic ice, is a place where people study and protect the poles."),
]
def globe_block(lang):
    g=GLOBE[lang]; r=rel(lang)
    pairs=[]
    cards=[]
    for i,(fossil,sol,href) in enumerate(g["pairs"]):
        chk=' checked' if i==0 else ""
        info=PIN_CARDS[i]
        cards.append({"fossil":fossil,"solution":sol,"href":href,**info})
        pairs.append(
            f'<div class="bsp-pair"><input type="radio" name="bsp-pair" value="{i}"{chk} aria-label="{html.escape(fossil)}">'
            f'<div class="bsp-pair-pins">'
            f'<button type="button" class="bsp-pin-open" data-pair="{i}"><span class="bsp-pin-f">● {html.escape(fossil)}</span></button>'
            f'<button type="button" class="bsp-pin-open" data-pair="{i}"><span class="bsp-pin-s">● {html.escape(sol)}</span></button>'
            f'</div></div>')
    blob=json.dumps(cards, ensure_ascii=False).replace("<","\\u003c")
    return (
        f'<section class="bsp-globe-sec" id="time-scrubber" data-pins="{r}assets/data/paleo-pins.json" data-tex="{r}assets/hero/paleo/" data-today="{html.escape(g["today"])}" data-far-msg="{html.escape(g["far"])}">'
        f'<div class="edu-wrap bsp-wrap"><h2>{g["h"]}</h2><p>{g["p"]}</p>'
        f'<div class="bsp-globe-layout"><div class="bsp-globe-stage"><canvas id="bsp-globe" width="360" height="360" aria-label="{html.escape(g["canvas"])}"></canvas></div>'
        f'<div><p class="bsp-globe-time"><span data-readout>540 Ma</span>'
        f'<input type="range" min="0" max="540" step="1" value="540" aria-label="{html.escape(g["axis"])}" aria-valuemin="0" aria-valuemax="540" aria-valuenow="540"></p>'
        f'<p class="bsp-globe-note">{g["axis"]}</p><div class="bsp-pairs" role="radiogroup" aria-label="{html.escape(g["h"])}">{"".join(pairs)}</div>'
        f'<div class="bsp-pin-card" id="bsp-pin-card" hidden role="region" aria-live="polite"></div>'
        f'<script type="application/json" id="bsp-pin-cards">{blob}</script>'
        f'<p data-far hidden></p><p class="bsp-globe-note">{g["credit"]}</p></div></div></div></section>')

SEARCH_UI = {
"en": ("One search index is meant to cover Before Saving Planets and Saving Planets. That shared index is not published on this site yet.", "From the shared index. Each result names its site.", "Nothing in the shared index matches. The question was not saved. This page does not search a separate note list.", "Leave out names, emails, phone numbers, and schools. Nothing from this search is saved.", "Search is paused for a minute so it cannot run without a limit.", "The shared index did not load. There is no second index to search instead, and the question was not saved."),
"fr": ("Un seul index doit couvrir Before Saving Planets et Saving Planets. Cet index partagé n’est pas encore publié sur ce site.", "Tiré de l’index partagé. Chaque résultat nomme son site.", "Rien dans l’index partagé ne correspond. La question n’a pas été enregistrée. Cette page ne cherche pas une liste de notes à part.", "N’indiquez pas de nom, d’e-mail, de téléphone ou d’école. Rien de cette recherche n’est enregistré.", "La recherche marque une pause d’une minute pour rester limitée.", "L’index partagé ne s’est pas chargé. Il n’y a pas de second index à chercher, et la question n’a pas été enregistrée."),
"es": ("Un solo índice debe cubrir Before Saving Planets y Saving Planets. Ese índice compartido aún no está publicado en este sitio.", "Del índice compartido. Cada resultado nombra su sitio.", "Nada en el índice compartido coincide. La pregunta no se guardó. Esta página no busca una lista de notas aparte.", "No escriba nombres, correos, teléfonos ni escuelas. Esta búsqueda no guarda nada.", "La búsqueda se detiene un minuto para no quedar sin límite.", "El índice compartido no se cargó. No hay un segundo índice que buscar, y la pregunta no se guardó."),
"ar": ("فهرس واحد يُفترض أن يغطّي Before Saving Planets وSaving Planets. هذا الفهرس المشترك غير منشور على هذا الموقع بعد.", "من الفهرس المشترك. كل نتيجة تذكر موقعها.", "لا شيء في الفهرس المشترك يطابق. السؤال لم يُحفظ. هذه الصفحة لا تبحث في قائمة ملاحظات منفصلة.", "لا تكتب أسماء أو بريدًا أو هاتفًا أو مدارس. هذا البحث لا يحفظ شيئًا.", "يتوقف البحث دقيقة حتى لا يعمل بلا حد.", "لم يُحمَّل الفهرس المشترك. لا يوجد فهرس ثانٍ للبحث، والسؤال لم يُحفظ."),
"it": ("Un solo indice deve coprire Before Saving Planets e Saving Planets. Quell’indice condiviso non è ancora pubblicato su questo sito.", "Dall’indice condiviso. Ogni risultato nomina il suo sito.", "Niente nell’indice condiviso corrisponde. La domanda non è stata salvata. Questa pagina non cerca un elenco di note a parte.", "Non scrivere nomi, email, telefoni o scuole. Questa ricerca non salva nulla.", "La ricerca si ferma un minuto così non resta senza limite.", "L’indice condiviso non si è caricato. Non c’è un secondo indice da cercare, e la domanda non è stata salvata."),
"he": ("אינדקס אחד אמור לכסות את Before Saving Planets ואת Saving Planets. האינדקס המשותף הזה עדיין לא פורסם באתר הזה.", "מהאינדקס המשותף. כל תוצאה מציינת את האתר שלה.", "אין התאמה באינדקס המשותף. השאלה לא נשמרה. העמוד הזה אינו מחפש ברשימת הערות נפרדת.", "אל תכתבו שמות, דוא״ל, טלפון או בית ספר. החיפוש הזה אינו שומר דבר.", "החיפוש נעצר לדקה כדי שלא יפעל בלי גבול.", "האינדקס המשותף לא נטען. אין אינדקס שני לחיפוש, והשאלה לא נשמרה."),
}

def search_block(lang, prefix):
    ready, ok, missing, refused, limited, down = SEARCH_UI[lang]
    t = T[lang]
    ids = ("bsp-search-ready", "bsp-search-ok", "bsp-search-missing", "bsp-search-refused", "bsp-search-limited", "bsp-search-down")
    notes = "".join(f'<p id="{i}" hidden>{html.escape(s)}</p>' for i, s in zip(ids, (ready, ok, missing, refused, limited, down)))
    return (
        f'<div class="edu-wrap bsp-wrap"><form class="bsp-search" id="bsp-search" role="search" data-corpus="">'
        f'<label for="bsp-q">{html.escape(t["search"])}</label>'
        f'<input id="bsp-q" name="q" type="search" enterkeyhint="search" placeholder="{html.escape(t["search"])}">'
        f'<button type="submit" class="edu-crystal">{html.escape(t["search"])}</button></form>'
        f'<p id="bsp-search-status" role="status">{html.escape(ready)}</p>'
        f'<ol id="bsp-search-results"></ol>{notes}</div>'
    )

def build(lang):
    t=T[lang]; r=rel(lang); out=os.path.join(ROOT,"" if lang=="en" else lang); os.makedirs(out,exist_ok=True)
    def w(page,s): open(os.path.join(out,page+".html"),"w").write(s)
    q_title,q_desc,q_hero,_q_tease=seo_copy.QUEST[lang]
    w("Quest",head(lang,"Quest",q_title,q_desc)+body(lang,"Quest",'<main id="main">'+page_hero(q_title,q_hero,t)+quest(lang)+'</main>',"toc-sub"))
    for k in DEEP:
        d_title,d_desc=seo_copy.DEEP[k][lang]
        w(k,head(lang,k,d_title,d_desc)+body(lang,k,deep(lang,k)))
    film_js=f'<script src="{r}assets/bsp-film.js" defer></script>'
    w("index",head(lang,"index",t['h1a']+" "+t['h1b'],t['sub'],f'<link rel="stylesheet" href="{r}home.css">')+body(lang,"index",home_library.render_home(lang,t,EXTRA[lang]),"toc-home",film_js))
    w("About",head(lang,"About",t["t_about"],t["d_about"])+body(lang,"About",about_pages.about(lang,r,t),"toc-sub",film_js))
    w("Ways_to_Help",head(lang,"Ways_to_Help",t["t_help"],t["d_help"])+body(lang,"Ways_to_Help",about_pages.ways(lang,r,t),"toc-sub",film_js))
    search_hero = about_pages.title_band(r, about_pages.MAPS, t["t_search"], t["d_search"], about_pages.MAP_CREDIT, t["pause"], about_pages.PLAY[lang])
    w("Search",head(lang,"Search",t["t_search"],t["d_search"])+body(lang,"Search",f'<main id="main">{search_hero}{search_block(lang, r)}</main>',"toc-sub",f'<script type="module" src="{r}assets/bsp-shared-search.js"></script>{film_js}'))
    X=EXTRA[lang]
    topic_desc={
      "en":{
        "Myth_vs_Fact":"Six sourced checks a seventh grader can read: Earth’s age, Smilodon, the asteroid, Mosasaurus, Jack Hills, and the Borealopelta film.",
        "Learn":"Lessons on fossils, climates, and deep time. The lessons are not written yet.",
        "Kids":"Earth and fossil pages for children. The stories are not written yet.",
        "Teachers":"Classroom pages on fossils and deep time. The lessons are not written yet.",
      },
      "fr":{
        "Myth_vs_Fact":"Six vérifications sourcées. Le texte des cartes est encore en anglais, en attente de relecture.",
        "Learn":"Des leçons sur les fossiles, les climats et le temps profond. Les leçons ne sont pas encore écrites.",
        "Kids":"Des pages sur la Terre et les fossiles pour les enfants. Les récits ne sont pas encore écrits.",
        "Teachers":"Des pages de classe sur les fossiles et le temps profond. Les leçons ne sont pas encore écrites.",
      },
      "es":{
        "Myth_vs_Fact":"Seis comprobaciones con fuente. El texto de las tarjetas sigue en inglés, pendiente de revisión.",
        "Learn":"Lecciones sobre fósiles, climas y tiempo profundo. Las lecciones aún no están escritas.",
        "Kids":"Páginas de la Tierra y los fósiles para niños. Los relatos aún no están escritos.",
        "Teachers":"Páginas de aula sobre fósiles y tiempo profundo. Las lecciones aún no están escritas.",
      },
      "it":{
        "Myth_vs_Fact":"Sei controlli con fonte. Il testo delle schede è ancora in inglese, in attesa di revisione.",
        "Learn":"Lezioni su fossili, climi e tempo profondo. Le lezioni non sono ancora scritte.",
        "Kids":"Pagine sulla Terra e sui fossili per bambini. I racconti non sono ancora scritti.",
        "Teachers":"Pagine per la classe su fossili e tempo profondo. Le lezioni non sono ancora scritte.",
      },
      "ar":{
        "Myth_vs_Fact":"ست مراجعات بمصادر. نص البطاقات ما زال بالإنجليزية بانتظار المراجعة.",
        "Learn":"دروس عن الأحافير والمناخات والزمن العميق. الدروس لم تُكتب بعد.",
        "Kids":"صفحات عن الأرض والأحافير للأطفال. القصص لم تُكتب بعد.",
        "Teachers":"صفحات صفية عن الأحافير والزمن العميق. الدروس لم تُكتب بعد.",
      },
      "he":{
        "Myth_vs_Fact":"שש בדיקות עם מקור. טקסט הכרטיסים עדיין באנגלית וממתין לסקירה.",
        "Learn":"שיעורים על מאובנים, אקלים וזמן עמוק. השיעורים עדיין לא נכתבו.",
        "Kids":"דפים על כדור הארץ ועל מאובנים לילדים. הסיפורים עדיין לא נכתבו.",
        "Teachers":"דפי כיתה על מאובנים וזמן עמוק. השיעורים עדיין לא נכתבו.",
      },
    }
    page = "Myth_vs_Fact"
    pdesc = topic_desc[lang][page]
    w(page, head(lang, page, X[0], pdesc)+body(lang, page, about_pages.myth(lang, r, t, X[0]), "toc-sub", film_js))
    import edu_tracks
    edu_tracks.write_lang(lang, ROOT, head, body, rel)
    shelf_css = f'<link rel="stylesheet" href="{r}assets/leaflet/leaflet.css"><link rel="stylesheet" href="{r}smilodon.css">'
    shelf_js = f'<script src="{r}assets/leaflet/leaflet.js" defer></script><script src="{r}bsp-smilodon.js" defer></script>'
    for slug, maker in DOSSIER_PAGES:
        dt, dd, dm = maker(lang, r)
        w(slug, head(lang, slug, dt, dd, shelf_css)+body(lang, slug, dm, "toc-sub", shelf_js))
    contact_hero = about_pages.title_band(r, about_pages.MAPS, t["t_contact"], t["d_contact"], about_pages.MAP_CREDIT, t["pause"], about_pages.PLAY[lang])
    w("Contact",head(lang,"Contact",t['t_contact'],t['d_contact'])+body(lang,"Contact",f'<main id="main">{contact_hero}<div class="edu-wrap bsp-wrap"><section class="bsp-card"><p><a href="mailto:{t["email"]}">{t["email"]}</a> (placeholder: Saving Planets inbox until a Before Saving Planets address exists)</p></section></div></main>',"toc-sub",film_js))
    # map data: English file is the coin source; other languages mirror that text. Native review is still welcome.
    os.makedirs(os.path.join(ROOT,"assets","data"),exist_ok=True)
    doc=fossil_doc(lang)
    with open(os.path.join(ROOT,"assets","data",f"fossil-map.{lang}.json"),"w",encoding="utf-8") as f:
        json.dump(doc,f,ensure_ascii=False,indent=2)
        f.write("\n")
    mascot=f'<button type="button" class="bsp-mascot" data-go="north" aria-label="{t["north"]}"><span class="bsp-dino" aria-hidden="true">🦕</span><span class="bsp-say">{t["north"]}</span></button>'
    lst="".join(fossil_li(s,t) for s in doc["sites"])
    banner='<p class="bsp-ph">Eighty-two sites open as coin cards: sixteen classic fossil sites, six soft-body lagerstätten, twelve deep-time archives, six mass-extinction sites, six first-forest sites, seven From Fins to Feet sites, six ancient-reef sites, eight Our Family Tree sites, seven Ice Age giant sites, and eight more: Meishan, Kuhjoch, the Crato Formation, the Dolomites, Pilauco, the Xinhang forest, Karoo Glossopteris, and Ventastega. When a card has a life picture, that picture is large and the fossil or the site is next. Cards without a life picture still lead with the fossil or the site. Then what, when, where, and why it matters. Learn more is last. Chicxulub and Gubbio link to each other.</p>'
    wm=f'''<main id="main" class="wm-main"><div class="wm-wrap bsp-map" data-src="{r}assets/data/fossil-map.{lang}.json"><div class="wm-screen"><h1 class="wm-title">{t['t_map']}</h1>{banner}<div class="wm-stage"><div id="wm" class="wm-map" dir="ltr" role="region" aria-label="{t['t_map']}"></div>{mascot}</div></div><details class="wm-list"><summary>{t['t_map']}</summary><ul>{lst}</ul></details></div></main>'''
    w("World_Map",head(lang,"World_Map",t['t_map'],t['d_map'],f'<link rel="stylesheet" href="{r}assets/leaflet/leaflet.css"><link rel="stylesheet" href="{r}map.css">')+body(lang,"World_Map",wm,"toc-sub world-map-page",f'<script src="{r}assets/leaflet/leaflet.js" defer></script><script src="{r}bsp-map.js" defer></script>'))
    stitle,sdesc,smain=smilodon_page(lang,r)
    smain=smain[:-len("</div></main>")]+support.block("Smilodon",lang)+"</div></main>" if smain.endswith("</div></main>") else smain
    w("Smilodon",head(lang,"Smilodon",stitle,sdesc,f'<link rel="stylesheet" href="{r}assets/leaflet/leaflet.css"><link rel="stylesheet" href="{r}smilodon.css">')+body(lang,"Smilodon",smain,"toc-sub",f'<script src="{r}assets/leaflet/leaflet.js" defer></script><script src="{r}bsp-smilodon.js" defer></script>'))
    ht,hd,hm=hub_page(lang,r)
    w("Dinosaurs",head(lang,"Dinosaurs",ht,hd,f'<link rel="stylesheet" href="{r}smilodon.css"><link rel="stylesheet" href="{r}finds.css">')+body(lang,"Dinosaurs",hm,"toc-sub"))
    shelf_css = f'<link rel="stylesheet" href="{r}smilodon.css"><link rel="stylesheet" href="{r}finds.css">'
    for slug in life.GROUP:
        lt, ld, lm = life.life_page(slug, lang, r)
        w(slug, head(lang, slug, lt, ld, shelf_css)+body(lang, slug, lm, "toc-sub"))
    dtitle,ddesc,dmain=deep_time_page(lang,r)
    w("Deep_Time",head(lang,"Deep_Time",dtitle,ddesc,f'<link rel="stylesheet" href="{r}smilodon.css"><link rel="stylesheet" href="{r}deeptime.css">')+body(lang,"Deep_Time",dmain,"toc-sub",f'<script src="{r}bsp-deeptime.js" defer></script>'))
    for slug in FIND_SLUGS:
        ft,fd,fm=find_page(slug,lang,r)
        fm=fm.replace('<p class="find-back">',support.block(slug,lang)+'<p class="find-back">',1)
        extra=f'<link rel="stylesheet" href="{r}smilodon.css"><link rel="stylesheet" href="{r}finds.css"><link rel="stylesheet" href="{r}deeptime.css">'
        scripts=""
        if has_map(slug):
            extra=f'<link rel="stylesheet" href="{r}assets/leaflet/leaflet.css">'+extra
            scripts=f'<script src="{r}assets/leaflet/leaflet.js" defer></script><script src="{r}bsp-smilodon.js" defer></script><script src="{r}bsp-deeptime.js" defer></script>'
        if has_video(slug):
            scripts += f'<script src="{r}assets/bsp-film.js" defer></script>'
        w(slug,head(lang,slug,ft,fd,extra)+body(lang,slug,fm,"toc-sub",scripts))
    pos=[(18,20),(62,14),(40,38),(78,44),(22,62),(60,70)]
    bub="".join(f'<button type="button" class="edu-bubble glass bsp-bubble" style="left:{x}%;top:{y}%" aria-pressed="false" data-ph="{html.escape(t["ph"])}"><span class="em" aria-hidden="true">{e}</span>{n}</button>' for (x,y),e,n in zip(pos,"🪲🌿🟠🦖🧊🪸",t["bubbles"]))
    km=f'''<main id="main">{page_hero(t['t_kids'],t['d_kids'],t)}<div class="edu-wrap"><p class="bsp-ph">⚠ {t['ph']}</p><div class="km-stage bsp-km" role="group" aria-label="{t['t_kids']}">{bub}{mascot}</div><p class="bsp-km-out" aria-live="polite"></p></div></main>'''
    w("Kids_Map",head(lang,"Kids_Map",t['t_kids'],t['d_kids'],f'<link rel="stylesheet" href="{r}edu.css">')+body(lang,"Kids_Map",km,"toc-sub kids-map-page",f'<script src="{r}bsp-kids.js" defer></script>'))

def _https_cite(url, what):
    if not isinstance(url, str) or not url.startswith("https://"):
        raise SystemExit("missing https citation: "+what)
    if "wikipedia.org" in url:
        raise SystemExit("Wikipedia is not an allowed citation: "+what)

def check_deep_time():
    path=os.path.join(ROOT,"assets","data","deep-time.json")
    pack=json.load(open(path,encoding="utf-8"))
    hrefs=[]
    def take(obj, what, required):
        for field in required:
            if not str(obj.get(field) or "").strip():
                raise SystemExit("data entry lacks "+field+": "+what)
        for field in ("sourceHref","sourceHref2","paleoHref","colorHref","imageHref","lifeHref"):
            if obj.get(field):
                _https_cite(obj[field], what+" "+field)
                hrefs.append(obj[field])
    for item in pack.get("life") or []:
        take(item, "life "+item.get("name",""), ("source","sourceHref","imageHref","imageCredit","imgAvif"))
        if item.get("lifeImg") or item.get("lifeHref") or item.get("lifeCredit"):
            take(item, "life picture "+item.get("name",""), ("lifeImg","lifeImgAvif","lifeHref","lifeCredit"))
            for rel in (item.get("lifeImg"), item.get("lifeImgAvif")):
                if not rel or not os.path.isfile(os.path.join(ROOT, rel)):
                    raise SystemExit("life picture file missing: "+item.get("name",""))
            if int(item.get("lifeW") or 0) > 1600:
                raise SystemExit("life picture is wider than a card: "+item.get("name",""))
    for item in pack.get("extinctions") or []:
        take(item, "extinction "+item.get("name",""), ("source","sourceHref","cause"))
    for spec in pack.get("species") or []:
        take(spec, "species "+spec.get("id",""), ("source","sourceHref"))
        for site in spec.get("sites") or []:
            take(site, spec.get("id","")+" site "+site.get("id",""), ("source","sourceHref","paleoHref"))
    for row in (pack.get("bands") or [])+(pack.get("eras") or []):
        take(row, "time "+row.get("en",""), ("source","sourceHref","colorHref"))
    unique=[]
    for href in hrefs:
        if href not in unique: unique.append(href)
    return len(pack["life"]), len(pack["extinctions"]), len(pack["species"]), len(unique)

def check_species_pages():
    pages=["Smilodon","Borealopelta","Nigersaurus","Triceratops","Stegosaurus","Archaeopteryx","Dunkleosteus","Meganeura","Pterodactylus","Plesiosaurus","Mosasaurus","Otodus_megalodon","Argentavis","Haasts_eagle"]
    counts={}
    for lang in LANGS:
        base="" if lang=="en" else lang+os.sep
        for page in pages:
            text=open(os.path.join(ROOT,base+page+".html"),encoding="utf-8").read()
            if page=="Smilodon":
                if 'class="sm-hero-video"' not in text or "hero-1080.mp4" not in text or "hero-video-poster.webp" not in text:
                    raise SystemExit("Smilodon hero is not the video behind the title: "+lang)
                if "World_Map.html?range=Smilodon" not in text:
                    raise SystemExit("Smilodon page lost the thrived-range map link: "+lang)
                vcredit=text.split('class="sm-vcredit"',1)
                if len(vcredit)<2 or "https://" not in vcredit[1][:1800]:
                    raise SystemExit("Smilodon video credit has no https citation: "+lang)
            else:
                credit=text.split('class="sm-credit"',1)
                if len(credit)<2 or "https://" not in credit[1][:1200]:
                    raise SystemExit("image credit has no https citation: "+lang+" "+page)
                if 'type="image/avif"' not in text:
                    raise SystemExit("hero is missing an AVIF source: "+lang+" "+page)
            found=re.search(r'<h2>Sources \((\d+)\)</h2>\s*<ul>(.*?)</ul>', text, re.S)
            if not found:
                raise SystemExit("page lacks a counted Sources list: "+lang+" "+page)
            links=re.findall(r'href="(https://[^"]+)"', found.group(2))
            if int(found.group(1))!=len(links):
                raise SystemExit("Sources count does not match links: "+lang+" "+page+" heading "+found.group(1)+" links "+str(len(links)))
            for href in links:
                _https_cite(href, lang+" "+page)
            counts[page]=len(links)
    return counts

def _meta(head, name):
    found=re.search(r'<meta name="'+name+r'" content="(.*?)">', head)
    if not found:
        raise SystemExit("missing meta "+name)
    return html.unescape(found.group(1))

TITLE_LIMIT=60
DESC_LIMIT=155
# IndexNow key for www.beforesavingplanets.com. The public file {key}.txt proves the host.
# https://www.indexnow.org/documentation
INDEXNOW_KEY="7c4e9a2b-6d18-4f03-9b55-1e8a0c3d6f21"

def check_seo():
    """Fail the build if any generated page is missing topic tags or the analytics beacon."""
    titles={}
    descs={}
    for lang in LANGS:
        base="" if lang=="en" else lang+os.sep
        titles[lang]=set()
        for page in PAGES:
            path=os.path.join(ROOT, base+page+".html")
            text=open(path, encoding="utf-8").read()
            head, sep, rest = text.partition("</head>")
            where=lang+" "+page
            if not sep:
                raise SystemExit("no head: "+where)
            if page in CHILD_PAGES:
                if CF_BEACON in text or "cloudflareinsights.com" in text:
                    raise SystemExit("analytics beacon is on a children's page: "+where)
                if "data-no-newsletter" not in text:
                    raise SystemExit("children's page can still show the newsletter form: "+where)
            elif text.count(CF_BEACON)!=1 or BEACON not in rest:
                raise SystemExit("Cloudflare beacon missing from the page body: "+where)
            canon=url(lang, page)
            if f'<link rel="canonical" href="{canon}">' not in head:
                raise SystemExit("canonical mismatch: "+where)
            for L in LANGS:
                if f'<link rel="alternate" hreflang="{L}" href="{url(L,page)}">' not in head:
                    raise SystemExit("hreflang missing: "+where+" "+L)
            if 'hreflang="x-default" href="'+url("en", page)+'"' not in head:
                raise SystemExit("x-default missing: "+where)
            for L in LANGS:
                if L==lang:
                    continue
                if 'property="og:locale:alternate" content="'+OG_LOCALE[L]+'"' not in head:
                    raise SystemExit("og:locale:alternate missing: "+where+" "+L)
            title=html.unescape(re.search(r"<title>(.*?)</title>", head).group(1))
            if not title.endswith(" | Before Saving Planets") or title in titles[lang]:
                raise SystemExit("title is not topic-specific: "+where+" "+title)
            if len(title)>TITLE_LIMIT:
                raise SystemExit("title longer than "+str(TITLE_LIMIT)+": "+where+" "+str(len(title))+" "+title)
            titles[lang].add(title)
            desc=_meta(head, "description")
            if len(desc)<20 or desc==title.split(" | ",1)[0]:
                raise SystemExit("description too thin: "+where)
            if len(desc)>DESC_LIMIT:
                raise SystemExit("description longer than "+str(DESC_LIMIT)+": "+where+" "+str(len(desc)))
            descs.setdefault(lang, set())
            if desc in descs[lang]:
                raise SystemExit("description is not unique: "+where)
            descs[lang].add(desc)
            if lang=="en":
                titles.setdefault("_en", {})[page]=title
                titles.setdefault("_end", {})[page]=desc
                titles.setdefault("_alt", {})[page]=og_for(lang, page)[1]
            else:
                if desc==titles["_end"][page]:
                    raise SystemExit("meta description is an English copy: "+where)
                bare=title.split(" | ",1)[0]
                en_bare=titles["_en"][page].split(" | ",1)[0]
                if bare==en_bare and " " in bare:
                    raise SystemExit("title is an English copy: "+where)
                if og_for(lang, page)[1]==titles["_alt"][page]:
                    raise SystemExit("image description is an English copy: "+where)
            if 'name="keywords"' in head:
                raise SystemExit("keywords meta tag should not be emitted: "+where)
            robots="index,follow" if page in INDEXABLE else "noindex,follow"
            if _meta(head, "robots")!=robots:
                raise SystemExit("robots mismatch: "+where)
            full=title
            for prop, expect in (
                ("og:title", full), ("og:description", desc), ("og:url", canon),
                ("og:type", "website"), ("og:site_name", "Before Saving Planets"),
                ("og:locale", OG_LOCALE[lang]), ("og:image", og_for(lang, page)[0]),
                ("og:image:alt", og_for(lang, page)[1]),
            ):
                found=re.search(r'<meta property="'+prop+r'" content="(.*?)">', head)
                if not found or html.unescape(found.group(1))!=expect:
                    raise SystemExit("Open Graph mismatch "+prop+": "+where)
            image_path=og_for(lang, page)[0][len(DOM):]
            if not os.path.isfile(os.path.join(ROOT, image_path.lstrip("/"))):
                raise SystemExit("Open Graph image missing on disk: "+image_path)
            for name, expect in (
                ("twitter:card", "summary_large_image"), ("twitter:title", full),
                ("twitter:description", desc), ("twitter:image", og_for(lang, page)[0]),
                ("twitter:image:alt", og_for(lang, page)[1]),
            ):
                if _meta(head, name)!=expect:
                    raise SystemExit("Twitter mismatch "+name+": "+where)
            blob=re.search(r'<script type="application/ld\+json">(.*?)</script>', head)
            if not blob:
                raise SystemExit("JSON-LD missing: "+where)
            ld=json.loads(blob.group(1))
            graph=ld.get("@graph") or []
            page_node=next((n for n in graph if n.get("@type")=="WebPage"), None)
            site_node=next((n for n in graph if n.get("@type")=="WebSite"), None)
            if not page_node or page_node.get("url")!=canon or page_node.get("name")!=full or page_node.get("description")!=desc:
                raise SystemExit("JSON-LD WebPage mismatch: "+where)
            if not site_node or site_node.get("url")!=DOM+"/":
                raise SystemExit("JSON-LD WebSite mismatch: "+where)
            if page_node.get("primaryImageOfPage",{}).get("url")!=og_for(lang, page)[0]:
                raise SystemExit("JSON-LD image mismatch: "+where)
            if page_node.get("primaryImageOfPage",{}).get("caption")!=og_for(lang, page)[1]:
                raise SystemExit("JSON-LD image caption mismatch: "+where)
    missing=open(os.path.join(ROOT,"404.html"),encoding="utf-8").read()
    if "Page not found | Before Saving Planets" not in missing or 'content="noindex,follow"' not in missing or BEACON not in missing:
        raise SystemExit("404.html is missing its title, noindex, or beacon")
    if missing.count(CF_BEACON)!=1:
        raise SystemExit("404.html beacon count is not 1")
    if "coming soon" in missing.lower() or "Placeholder section" in missing:
        raise SystemExit("404.html still promises content that is not written")
    if 'id="bsp-h1">Page not found' not in missing:
        raise SystemExit("404.html is missing the page-not-found heading")
    for href in ("index.html", "Search.html", "Dinosaurs.html", "Mammals.html", "Aerial.html", "Marine.html", "Learn.html"):
        if 'href="'+href+'"' not in missing:
            raise SystemExit("404.html is missing a real link: "+href)
    index=open(os.path.join(ROOT,"sitemap.xml"),encoding="utf-8").read()
    if "<sitemapindex" not in index:
        raise SystemExit("sitemap.xml is not a sitemap index")
    index_locs=re.findall(r"<loc>(.*?)</loc>", index)
    expected_maps=[DOM+"/sitemap-"+L+".xml" for L in LANGS]
    if index_locs!=expected_maps:
        raise SystemExit("sitemap index does not list the six language sitemaps")
    if index.count("<lastmod>2026-11-02</lastmod>")!=len(LANGS):
        raise SystemExit("sitemap index lastmod missing")
    page_urls=[]
    for L in LANGS:
        text=open(os.path.join(ROOT,"sitemap-"+L+".xml"),encoding="utf-8").read()
        if "xhtml" in text:
            raise SystemExit("language sitemap carries hreflang; Yandex rejects that. Keep hreflang in the HTML head.")
        locs=re.findall(r"<loc>(.*?)</loc>", text)
        want=[url(L,p) for p in PAGES if p in INDEXABLE]
        if locs!=want:
            raise SystemExit("language sitemap URLs do not match: "+L)
        if text.count("<lastmod>2026-11-02</lastmod>")!=len(want):
            raise SystemExit("language sitemap lastmod missing: "+L)
        for page in PAGES:
            if page not in INDEXABLE and url(L, page) in locs:
                raise SystemExit("scaffold page leaked into the sitemap: "+page)
        page_urls.extend(locs)
    key_path=os.path.join(ROOT, INDEXNOW_KEY+".txt")
    if open(key_path,encoding="utf-8").read().strip()!=INDEXNOW_KEY:
        raise SystemExit("IndexNow key file does not match the key")
    robots=open(os.path.join(ROOT,"robots.txt"),encoding="utf-8").read()
    if robots!="User-agent: *\nAllow: /\n\nSitemap: https://www.beforesavingplanets.com/sitemap.xml\n":
        raise SystemExit("robots.txt is not the Allow-all sitemap file")
    return len(LANGS)*len(PAGES), len(page_urls)

def _main_menu(text):
    start = text.find('<ul class="spn-main"')
    if start < 0:
        return None
    depth = 0
    i = start
    while i < len(text):
        if text.startswith("<ul", i):
            depth += 1
            i += 3
            continue
        if text.startswith("</ul>", i):
            depth -= 1
            i += 5
            if depth == 0:
                return text[start:i]
            continue
        i += 1
    return None

def sync_hand_nav():
    """Policy and the 404 page are not in PAGES. Give them the same main menu."""
    for lang in LANGS:
        base = "" if lang=="en" else lang+os.sep
        contact = open(os.path.join(ROOT, base+"Contact.html"), encoding="utf-8").read()
        menu = _main_menu(contact)
        if not menu:
            raise SystemExit("main menu missing: "+lang+" Contact")
        targets = ["Policy.html"]
        if lang=="en":
            targets.append("404.html")
        for name in targets:
            path = os.path.join(ROOT, base+name)
            text = open(path, encoding="utf-8").read()
            start = text.find('<ul class="spn-main"')
            end = text.find("</div></div></nav>", start)
            if start < 0 or end < 0:
                raise SystemExit("hand nav not updated: "+path)
            open(path, "w", encoding="utf-8").write(text[:start] + menu + text[end:])

def check_search():
    if not os.path.isfile(bsp_knowledge.INDEX_PATH):
        raise SystemExit("search index was not written")
    doc = json.load(open(bsp_knowledge.INDEX_PATH, encoding="utf-8"))
    if doc.get("research") != "unavailable":
        raise SystemExit("search index claims research is available")
    if not any(row.get("title") == "Smilodon" for row in doc.get("records") or []):
        raise SystemExit("search index lost Smilodon")
    mosa = next(row for row in doc["records"] if row.get("title") == "Mosasaurus")
    if "did not live after" not in mosa["answer"] or "61.66" not in mosa["answer"]:
        raise SystemExit("Mosasaurus search note lost the age correction")
    ples = next(row for row in doc["records"] if row.get("title") == "Plesiosaurus")
    if "whole Sinemurian" not in ples["answer"] or "199.5" not in ples["answer"] or "192.9" not in ples["answer"]:
        raise SystemExit("Plesiosaurus search note lost the stage-bin correction")
    ich = next(row for row in doc["records"] if row.get("title") == "Ichthyosaurus")
    if "174.7" not in ich["answer"] or "184.2" not in ich["answer"] or "not the end of the Early Pliensbachian" not in ich["answer"]:
        raise SystemExit("Ichthyosaurus search note lost the bin-edge correction")
    waco = next(row for row in doc["records"] if row.get("title") == "Waco mammoths")
    if "65,000" not in waco["answer"] or "72,000" not in waco["answer"] or "not a single measured year" not in waco["answer"]:
        raise SystemExit("Waco search note lost the herd-age range")
    devon = next(row for row in doc["records"] if row.get("title") == "Late Devonian")
    if "does not give the cause" not in devon["answer"] or "oxygen" in devon["answer"].lower():
        raise SystemExit("Late Devonian search note still assigns a cause to the boundary paper")
    smil = next(row for row in doc["records"] if row.get("title") == "Smilodon")
    if "700,000" not in smil["answer"] or "last 50,000 years" not in smil["answer"] or "10,000 years ago" in smil["answer"]:
        raise SystemExit("Smilodon search note lost the species range and the La Brea collection span")
    laet = next(row for row in doc["records"] if row.get("title") == "Laetoli")
    if "about 3.6 million" not in laet["answer"] or "3.66" not in laet["answer"]:
        raise SystemExit("Laetoli search note lost the Smithsonian age and the finer mark")
    anom = next(row for row in doc["records"] if row.get("title") == "Anomalocaris")
    if "505" not in anom["answer"] or "Wuliuan" not in anom["answer"] or "508" in anom["answer"]:
        raise SystemExit("Anomalocaris search note lost the museum age")
    mega = next(row for row in doc["records"] if row.get("title") == "Meganeura")
    if "MNHN-F-R51142" not in mega["answer"] or "lectotype" in mega["answer"].lower():
        raise SystemExit("Meganeura search note lost the museum inventory number")
    for lang in ("en", "fr"):
        base = "" if lang == "en" else lang + os.sep
        smil_page = open(os.path.join(ROOT, base + "Smilodon.html"), encoding="utf-8").read()
        if "To scale" in smil_page or "À l’échelle" in smil_page:
            raise SystemExit("Smilodon page still calls the drawing a measured scale: " + lang)
        if ("not a measured scale" not in smil_page and "pas une échelle mesurée" not in smil_page) or ("700,000" not in smil_page and "700 000" not in smil_page):
            raise SystemExit("Smilodon page lost the scale qualification or the species range: " + lang)
        mega_page = open(os.path.join(ROOT, base + "Meganeura.html"), encoding="utf-8").read()
        if "MNHN-F-R51142" not in mega_page or "lectotype" in mega_page.lower() or "lectotipo" in mega_page.lower():
            raise SystemExit("Meganeura page lost the inventory number: " + lang)
        bore = open(os.path.join(ROOT, base + "Borealopelta.html"), encoding="utf-8").read()
        if "5.5 m" not in bore and "5,5 m" not in bore:
            raise SystemExit("Borealopelta page lost the 2017 length estimate: " + lang)
        nig = open(os.path.join(ROOT, base + "Nigersaurus.html"), encoding="utf-8").read()
        if "9 m" not in nig:
            raise SystemExit("Nigersaurus page lost the 2007 length estimate: " + lang)
        tri = open(os.path.join(ROOT, base + "Triceratops.html"), encoding="utf-8").read()
        if "58" not in tri or "22" not in tri or ("2.5 cm" not in tri and "2,5 cm" not in tri):
            raise SystemExit("Triceratops page lost the 1996 bite counts: " + lang)
    for lang in ("en", "fr"):
        base = "" if lang == "en" else lang + os.sep
        ples_page = open(os.path.join(ROOT, base + "Plesiosaurus.html"), encoding="utf-8").read()
        if "whole Sinemurian" not in ples_page and "tout l’étage du Sinémurien" not in ples_page:
            raise SystemExit("Plesiosaurus page lost the stage-bin correction: " + lang)
    verified = json.load(open(bsp_knowledge.VERIFIED_PATH, encoding="utf-8"))
    if verified.get("entries"):
        raise SystemExit("verified answer store must ship empty")
    for lang in LANGS:
        base = "" if lang == "en" else lang + os.sep
        text = open(os.path.join(ROOT, base + "Search.html"), encoding="utf-8").read()
        if 'id="bsp-search"' not in text or 'data-corpus=""' not in text or "assets/bsp-shared-search.js" not in text:
            raise SystemExit("search page is not the shared-index client: " + lang)
        if "assets/bsp-search.js" in text or "bsp-verified" in text:
            raise SystemExit("search page still uses the separate note index: " + lang)
        if "shared index is not published" not in text and "index partagé n’est pas encore publié" not in text and "índice compartido aún no está publicado" not in text and "الفهرس المشترك غير منشور" not in text and "indice condiviso non è ancora pubblicato" not in text and "האינדקס המשותף הזה עדיין לא פורסם" not in text:
            raise SystemExit("search page does not say the shared index is unpublished: " + lang)
        for child_name in ("Kids.html", "Kids_Map.html"):
            kids = open(os.path.join(ROOT, base + child_name), encoding="utf-8").read()
            if "assets/bsp-search.js" in kids or "assets/bsp-shared-search.js" in kids or "cloudflareinsights" in kids or "sticky-help" in kids:
                raise SystemExit("kids page picked up search, analytics, or the help button: " + child_name + " " + lang)
        mosa_page = open(os.path.join(ROOT, base + "Mosasaurus.html"), encoding="utf-8").read()
        if "did not live after" not in mosa_page and "n’a pas vécu après" not in mosa_page and "pas après environ 66" not in mosa_page:
            if lang in ("en", "fr"):
                raise SystemExit("Mosasaurus page lost the 66-million-year line: " + lang)

def check_local_links():
    """Fail when a generated page points at a local file that is not in the tree."""
    missing = []
    hrefs = re.compile(r'''(?:href|src)="([^"]+)"''')
    for dirpath, _, names in os.walk(ROOT):
        if "/.git" in dirpath or "__pycache__" in dirpath:
            continue
        for name in names:
            if not name.endswith(".html"):
                continue
            path = os.path.join(dirpath, name)
            text = open(path, encoding="utf-8", errors="replace").read()
            for raw in hrefs.findall(text):
                if raw.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                    continue
                target = raw.split("#", 1)[0].split("?", 1)[0]
                if not target:
                    continue
                if target.startswith("/"):
                    full = os.path.normpath(os.path.join(ROOT, target.lstrip("/")))
                else:
                    full = os.path.normpath(os.path.join(dirpath, target))
                if not full.startswith(ROOT) or not os.path.isfile(full):
                    missing.append(os.path.relpath(path, ROOT) + " -> " + raw)
                    if len(missing) > 25:
                        break
    if missing:
        raise SystemExit("local link missing:\n" + "\n".join(missing[:25]))

def check_retired():
    """Dig Quest stays out of the public chrome. Cartoon continent globes stay deleted."""
    banned = (
        "assets/hero/morph/hero-1080.mp4",
        "assets/hero/morph/era-540.webp",
        "assets/hero/morph/era-drift.webp",
        "assets/hero/morph/era-today.webp",
        "assets/hero/morph/end.webp",
    )
    for rel in banned:
        if os.path.isfile(os.path.join(ROOT, rel)):
            raise SystemExit("cartoon Earth asset is still in the tree: "+rel)
    if not os.path.isfile(os.path.join(ROOT, "assets/hero/paleo/m540.webp")):
        raise SystemExit("PALEOMAP frame missing")
    if not os.path.isfile(os.path.join(ROOT, "assets/hero/morph/start.webp")):
        raise SystemExit("lava still missing")
    if not os.path.isfile(os.path.join(ROOT, "assets/deep/photo-earth.webp")):
        raise SystemExit("NASA Blue Marble still missing")
    for lang in LANGS:
        base = "" if lang=="en" else lang+os.sep
        home = open(os.path.join(ROOT, base+"index.html"), encoding="utf-8").read()
        nav = _main_menu(home) or ""
        if "Quest.html" in nav or "Dig Quest" in nav:
            raise SystemExit("Dig Quest is still in the menu: "+lang)
        if "Quest.html" in home or "Dig Quest" in home:
            raise SystemExit("Dig Quest is still on the homepage: "+lang)
        if "bsp-globe.js" in home or "hero/morph/hero-1080" in home:
            raise SystemExit("cartoon Earth is still on the homepage: "+lang)
        deep = open(os.path.join(ROOT, base+"Deep_Time.html"), encoding="utf-8").read()
        if 'data-map="off"' not in deep or 'data-map="on"' in deep:
            raise SystemExit("Deep Time page still mounts its map: "+lang)
        dino = open(os.path.join(ROOT, base+"Borealopelta.html"), encoding="utf-8").read()
        if 'data-map="on"' not in dino:
            raise SystemExit("species Then map was removed: "+lang)
        world = open(os.path.join(ROOT, base+"World_Map.html"), encoding="utf-8").read()
        if 'id="wm"' not in world:
            raise SystemExit("World Map was removed: "+lang)
        quest = open(os.path.join(ROOT, base+"Quest.html"), encoding="utf-8").read()
        if "bsp-globe.js" in quest or "id=\"bsp-globe\"" in quest or "q-progress" in quest:
            raise SystemExit("Dig Quest globe is still on the layer page: "+lang)
        if "Jack Hills" not in quest and "Jack Hills" not in open(os.path.join(ROOT, base+"Continents.html"), encoding="utf-8").read():
            pass
        if "4.404" not in quest and "4,404" not in quest:
            raise SystemExit("Jack Hills age left the layer archive: "+lang)
        lesson = open(os.path.join(ROOT, base+"Lesson_Plan.html"), encoding="utf-8").read()
        if "bsp-lesson.js" not in lesson:
            raise SystemExit("lesson plan builder missing: "+lang)
        sm = open(os.path.join(ROOT, base+"Smilodon.html"), encoding="utf-8").read()
        if "smilodon-vs-woman-v4" not in sm:
            raise SystemExit("Smilodon passport compare missing: "+lang)

if __name__=="__main__":
    if not os.path.isfile(bsp_knowledge.VERIFIED_PATH):
        json.dump({"entries": []}, open(bsp_knowledge.VERIFIED_PATH, "w", encoding="utf-8"))
    bsp_knowledge.write_index()
    life_n, ext_n, sp_n, cite_n = check_deep_time()
    for L in LANGS: build(L)
    sync_hand_nav()
    page_counts=check_species_pages()
    check_retired()
    check_search()
    check_local_links()
    # Language alternates stay in the HTML head. Yandex no longer reads them from sitemaps,
    # and an xhtml tag there can be reported as an unknown tag. Google treats HTML hreflang as enough.
    maps=[]
    for L in LANGS:
        urls="".join(f"<url><loc>{url(L,p)}</loc><lastmod>2026-11-02</lastmod></url>" for p in PAGES if p in INDEXABLE)
        open(os.path.join(ROOT,"sitemap-"+L+".xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+"</urlset>")
        maps.append(f"<sitemap><loc>{DOM}/sitemap-{L}.xml</loc><lastmod>2026-11-02</lastmod></sitemap>")
    open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(maps)+"</sitemapindex>")
    open(os.path.join(ROOT, INDEXNOW_KEY+".txt"),"w").write(INDEXNOW_KEY+"\n")
    open(os.path.join(ROOT,"robots.txt"),"w").write("User-agent: *\nAllow: /\n\nSitemap: https://www.beforesavingplanets.com/sitemap.xml\n")
    seo_pages, seo_urls=check_seo()
    print("deep-time sources: "+str(cite_n)+" clickable citations; "+str(life_n)+" life entries; "+str(ext_n)+" extinctions; "+str(sp_n)+" mapped species")
    print("species-page sources: "+", ".join(page+" "+str(page_counts[page]) for page in page_counts))
    print("seo: "+str(seo_pages)+" pages with title, description, canonical, Open Graph, Twitter, JSON-LD, and the Cloudflare beacon; sitemap "+str(seo_urls)+" indexable URLs")
    print("built",len(LANGS)*len(PAGES),"pages")
    import export_public
    export_public.main()
