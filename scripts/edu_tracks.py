#!/usr/bin/env python3
"""Education tracks for Before Saving Planets.

Geologist and archaeologist self-study, modeled on published university scopes.
Not those universities' courses, and not a copy of Saving Planets aerospace.
"""
import html, json, os, re

LANGS = ["en", "fr", "es", "ar", "it", "he"]
IX = {k: i for i, k in enumerate(LANGS)}

def T(lang, *six):
    if len(six) != 6:
        raise SystemExit("translation needs 6 languages, got %s" % len(six))
    return six[IX[lang]]

COURSE_PAGES = {
    "Earth_Materials", "Stratigraphic_Record", "Field_Geology",
    "World_Archaeology", "Site_Context", "Field_Methods",
    "Geophysics", "Sediments", "Field_Camp",
    "Animal_Bones", "Site_Soils", "Long_Essay",
}
EDU_PAGES = {"Learn", "Courses", "Teachers", "Kids", "Lesson_Plan"} | COURSE_PAGES

MIT12 = "https://catalog.mit.edu/subjects/12/"
MIT_DEPT = "https://catalog.mit.edu/schools/science/earth-atmospheric-planetary-sciences/"
UCL_MOD = "https://www.ucl.ac.uk/social-historical-sciences/archaeology/study/undergraduate-programmes/undergraduate-modules"
UCL_FIELD = "https://www.ucl.ac.uk/module-catalogue/modules/field-methods-ARCL0011"
USGS_AGE = "https://pubs.usgs.gov/gip/geotime/age.html"
ICS = "https://stratigraphy.org/chart"
NGSS_4 = "https://www.nextgenscience.org/pe/4-ess1-1-earths-place-universe"
NGSS_MS = "https://www.nextgenscience.org/pe/ms-ess1-4-earths-place-universe"
NGSS_HS = "https://www.nextgenscience.org/pe/hs-ess1-5-earths-place-universe"
NGSS_LS = "https://www.nextgenscience.org/pe/3-ls4-1-biological-evolution-unity-and-diversity"
C3 = "https://www.socialstudies.org/standards/c3"
SI_HS = "https://humanorigins.si.edu/evidence/human-fossils/species/homo-sapiens"
SI_DATE = "https://humanorigins.si.edu/evidence/dating"
SI_TOOLS = "https://humanorigins.si.edu/evidence/behavior/stone-tools"
NPS_TIME = "https://www.nps.gov/subjects/geology/time-scale.htm"
USGS_MAP = "https://ngmdb.usgs.gov/ngmdb/ngmdb_home.html"
UCMP_TRI = "https://ucmp.berkeley.edu/arthropoda/trilobita/trilobita.html"

STD_4 = "Identify evidence from patterns in rock formations and fossils in rock layers to support an explanation for changes in a landscape over time."
STD_MS = "Construct a scientific explanation based on evidence from rock strata for how the geologic time scale is used to organize Earth's 4.6-billion-year-old history."
STD_HS = "Evaluate evidence of the past and current movements of continental and oceanic crust and the theory of plate tectonics to explain the ages of crustal rocks."
STD_LS = "Analyze and interpret data from fossils to provide evidence of the organisms and the environments in which they lived long ago."
STD_C3 = "Evaluate how historical events and developments were shaped by unique circumstances of time and place as well as broader historical contexts."

def earth_stds():
    return [
        {"band": "3-5", "subject": "earth", "code": "4-ESS1-1", "text": STD_4, "url": NGSS_4},
        {"band": "6-8", "subject": "earth", "code": "MS-ESS1-4", "text": STD_MS, "url": NGSS_MS},
        {"band": "9-12", "subject": "earth", "code": "HS-ESS1-5", "text": STD_HS, "url": NGSS_HS},
    ]

def arch_stds():
    return [
        {"band": "3-5", "subject": "arch", "code": "3-LS4-1", "text": STD_LS, "url": NGSS_LS},
        {"band": "6-8", "subject": "arch", "code": "MS-ESS1-4", "text": STD_MS, "url": NGSS_MS},
        {"band": "9-12", "subject": "arch", "code": "D2.His.1.9-12", "text": STD_C3, "url": C3},
    ]

# Suggested self-study calendar. Not a university term.
DATES = [
    "8–11 Sep 2026", "14–18 Sep 2026", "21–25 Sep 2026", "28 Sep–2 Oct 2026",
    "5–9 Oct 2026", "12–16 Oct 2026", "19–23 Oct 2026", "26–30 Oct 2026",
    "2–6 Nov 2026", "9–13 Nov 2026", "16–20 Nov 2026", "23–25 Nov 2026",
    "30 Nov–4 Dec 2026", "7–11 Dec 2026", "14–18 Dec 2026",
]

def weeks(*titles):
    if len(titles) != 15:
        raise SystemExit("need 15 week titles")
    return [{"date": DATES[i], "title": titles[i]} for i in range(15)]

def unit(anchor, title, body, questions, eli):
    return {"id": anchor, "title": title, "body": body, "questions": questions, "eli": eli}

# Each course: slug, code, track earth|arch, live, titles, blurbs, model, about, weeks, units, sources
def C(slug, code, track, title, blurb, about, model_name, model_url, weeks, units, sources, sheet_q):
    return dict(slug=slug, code=code, track=track, title=title, blurb=blurb, about=about,
                model_name=model_name, model_url=model_url, weeks=weeks, units=units,
                sources=sources, sheet_q=sheet_q)

EARTH = C(
    "Earth_Materials", "GEOL 110", "earth",
    ("Earth materials", "Matières de la Terre", "Materiales terrestres", "مواد الأرض", "Materiali terrestri", "חומרי כדור הארץ"),
    ("Minerals, rocks, and the processes that make them.",
     "Minéraux, roches, et les processus qui les forment.",
     "Minerales, rocas y los procesos que las forman.",
     "معادن وصخور والعمليات التي تكوّنها.",
     "Minerali, rocce e i processi che le formano.",
     "מינרלים, סלעים והתהליכים שיוצרים אותם."),
    ("A rock is a record of heat, water, or pressure. This outline follows the scope of MIT 12.001 Introduction to Geology: minerals, rocks, time, field structures, sediment, and plates, with lab habits. It is not MIT’s class and carries no credit.",
     "Une roche enregistre chaleur, eau ou pression. Ce plan suit le périmètre du cours MIT 12.001 : minéraux, roches, temps, structures, sédiments et plaques, avec des habitudes de labo. Ce n’est pas le cours du MIT et il ne donne aucun crédit.",
     "Una roca registra calor, agua o presión. Este plan sigue el alcance de MIT 12.001: minerales, rocas, tiempo, estructuras, sedimento y placas, con hábitos de laboratorio. No es la clase del MIT y no da crédito.",
     "الصخر سجل للحرارة أو الماء أو الضغط. يتبع هذا المخطط نطاق مقرر MIT 12.001: معادن وصخور وزمن وتراكيب ورواسب وألواح، مع عادات المختبر. ليس صف معهد MIT ولا يمنح ساعات معتمدة.",
     "Una roccia registra calore, acqua o pressione. Questo schema segue l’ambito di MIT 12.001: minerali, rocce, tempo, strutture, sedimenti e placche, con abitudini di laboratorio. Non è il corso del MIT e non dà crediti.",
     "סלע הוא תיעוד של חום, מים או לחץ. המתווה עוקב אחרי היקף MIT 12.001: מינרלים, סלעים, זמן, מבנים, משקע ולוחות, עם הרגלי מעבדה. זה אינו הקורס של MIT ואין בו נקודות זכות."),
    "MIT 12.001 Introduction to Geology", MIT12,
    weeks(
        ("Hand sample", "Échantillon", "Muestra de mano", "عينة يد", "Campione", "דוגמת יד"),
        ("Minerals", "Minéraux", "Minerales", "معادن", "Minerali", "מינרלים"),
        ("Silicates", "Silicates", "Silicatos", "سيليكات", "Silicati", "סיליקטים"),
        ("Igneous", "Ignées", "Ígneas", "نارية", "Ignee", "סלעי תצרה"),
        ("Sedimentary", "Sédimentaires", "Sedimentarias", "رسوبية", "Sedimentarie", "משקע"),
        ("Metamorphic", "Métamorphiques", "Metamórficas", "متحولة", "Metamorfiche", "מותמרים"),
        ("Relative time", "Temps relatif", "Tiempo relativo", "زمن نسبي", "Tempo relativo", "זמן יחסי"),
        ("The time chart", "L’échelle", "La escala", "سلم الزمن", "La scala", "סרגל הזמן"),
        ("A geologic map", "Carte géologique", "Mapa geológico", "خريطة جيولوجية", "Carta geologica", "מפה גאולוגית"),
        ("Sediment moves", "Le sédiment bouge", "El sedimento se mueve", "الرواسب تتحرك", "Il sedimento si muove", "המשקע זז"),
        ("Plates", "Plaques", "Placas", "ألواح", "Placche", "לוחות"),
        ("Brittle or ductile", "Cassant ou ductile", "Frágil o dúctil", "هش أو لدن", "Fragile o duttile", "שביר או רקיע"),
        ("Mineral lab", "Labo minéraux", "Lab de minerales", "مختبر المعادن", "Lab minerali", "מעבדת מינרלים"),
        ("Rock lab", "Labo roches", "Lab de rocas", "مختبر الصخور", "Lab rocce", "מעבדת סלעים"),
        ("One outcrop", "Un affleurement", "Un afloramiento", "مكشف واحد", "Un affioramento", "מחשוף אחד"),
    ),
    [
        unit("minerals",
             ("Minerals are ingredients", "Les minéraux sont les ingrédients", "Los minerales son los ingredientes", "المعادن هي المكونات", "I minerali sono gli ingredienti", "מינרלים הם הרכיבים"),
             ("Name a mineral by properties you can test: color is weak, scratch and shape are stronger. Quartz, feldspar, mica, and calcite cover most beginner samples. The Mohs list is a scratch order, not a price.",
              "On nomme un minéral par des tests : la couleur est faible, la rayure et la forme sont plus fortes. Quartz, feldspath, mica et calcite couvrent la plupart des échantillons de début. L’échelle de Mohs est un ordre de rayure, pas un prix.",
              "Se nombra un mineral por pruebas: el color es débil, la raya y la forma pesan más. Cuarzo, feldespato, mica y calcita cubren casi todas las muestras de inicio. La escala de Mohs es un orden de rayado, no un precio.",
              "نسمّي المعدن بخصائص نختبرها: اللون ضعيف، والخدش والشكل أقوى. الكوارتز والفلسبار والميكا والكالسيت تغطي معظم عينات المبتدئ. مقياس موهس ترتيب خدش لا ثمن.",
              "Si nomina un minerale con prove: il colore è debole, la striatura e la forma contano di più. Quarzo, feldspato, mica e calcite coprono quasi tutti i campioni iniziali. La scala di Mohs è un ordine di scalfittura, non un prezzo.",
              "נותנים למינרל שם לפי תכונות שאפשר לבדוק: הצבע חלש, השריטה והצורה חזקות יותר. קוורץ, פלדספר, נציץ וקלציט מכסים את רוב דוגמאות המתחיל. סולם מוס הוא סדר שריטה, לא מחיר."),
             (("Which property would you trust more than color?", "Quelle propriété vaut mieux que la couleur ?", "¿Qué propiedad vale más que el color?", "أي خاصية تثق بها أكثر من اللون؟", "Quale proprietà conta più del colore?", "איזו תכונה עדיפה על הצבע?"),
              ("Why is Mohs not a measure of value?", "Pourquoi Mohs n’est-il pas une valeur ?", "¿Por qué Mohs no mide el valor?", "لماذا ليس موهس مقياس قيمة؟", "Perché Mohs non è un valore?", "למה מוס אינו מידת ערך?")),
             ("Color alone misnames many minerals. Scratch, shape, and a simple acid test, only with a teacher, sort the common ones.",)),
        unit("rocks",
             ("Three rock families", "Trois familles de roches", "Tres familias de rocas", "ثلاث عائلات من الصخور", "Tre famiglie di rocce", "שלוש משפחות סלע"),
             ("Igneous rocks cool from melt, and small grains usually mean faster cooling. Sedimentary rocks are laid down; most fossils are in them. Metamorphic rocks change while solid, by heat and pressure, without fully melting.",
              "Les roches ignées refroidissent d’un magma : de petits grains veulent souvent dire un refroidissement rapide. Les sédimentaires se déposent ; la plupart des fossiles y sont. Les métamorphiques changent à l’état solide, par chaleur et pression, sans fondre entièrement.",
              "Las ígneas se enfrían desde un fundido: el grano fino suele indicar un enfriamiento rápido. Las sedimentarias se depositan; ahí están casi todos los fósiles. Las metamórficas cambian en sólido, por calor y presión, sin fundirse del todo.",
              "الصخور النارية تبرد من مصهور، والحبيبات الصغيرة تعني غالباً تبرداً أسرع. الرسوبية تتراكم، وفيها معظم الأحافير. المتحولة تتغير وهي صلبة بالحرارة والضغط دون انصهار كامل.",
              "Le ignee si raffreddano da un fuso: grani piccoli di solito indicano un raffreddamento rapido. Le sedimentarie si depositano; quasi tutti i fossili stanno lì. Le metamorfiche cambiano da solide, con calore e pressione, senza fondere del tutto.",
              "סלעי תצרה מתקררים מנתך, וגרגרים קטנים בדרך כלל פירושם קירור מהיר. סלעי משקע שוקעים, ורוב המאובנים בהם. סלעים מותמרים משתנים במצב מוצק, בחום ולחץ, בלי להינתך לגמרי."),
             (("Where do most fossils sit, and why?", "Où sont la plupart des fossiles, et pourquoi ?", "¿Dónde están casi todos los fósiles, y por qué?", "أين معظم الأحافير، ولماذا؟", "Dove stanno quasi tutti i fossili, e perché?", "איפה רוב המאובנים, ולמה?"),
              ("What is the difference between melting and metamorphism?", "Quelle est la différence entre fondre et le métamorphisme ?", "¿Qué diferencia hay entre fundirse y el metamorfismo?", "ما الفرق بين الانصهار والتحول؟", "Che differenza c’è tra fondere e il metamorfismo?", "מה ההבדל בין התכה להתמרה?")),
             ("Igneous, sedimentary, and metamorphic are processes, not a ranking of importance.",)),
        unit("time",
             ("Time without a bare abbreviation", "Le temps sans abréviation sèche", "El tiempo sin una sigla sola", "الزمن دون اختصار جاف", "Il tempo senza una sigla nuda", "זמן בלי קיצור יבש"),
             ("Younger layers usually lie on older ones, unless the stack was turned over. The USGS dates Earth at 4.54 billion years. The International Commission on Stratigraphy publishes the chart of named time. Say the years in words.",
              "Les couches plus jeunes reposent en général sur les plus vieilles, sauf si la pile a été retournée. L’USGS date la Terre à 4,54 milliards d’années. La Commission internationale de stratigraphie publie le tableau des temps nommés. Dites les années en mots.",
              "Las capas más jóvenes suelen estar sobre las más viejas, salvo si la pila se volcó. El USGS fecha la Tierra en 4.540 millones de años. La Comisión Internacional de Estratigrafía publica la escala con nombres. Di los años con palabras.",
              "الطبقات الأحدث تعلو الأقدم عادة، إلا إذا انقلبت الرزمة. تحدّد هيئة المسح الجيولوجي الأمريكية عمر الأرض بـ 4.54 مليار سنة. تنشر اللجنة الدولية للطبقات جدول الزمن المسمّى. اكتبوا السنوات بالكلمات.",
              "Gli strati più giovani stanno di solito sopra i più vecchi, salvo se la pila è stata capovolta. L’USGS data la Terra a 4,54 miliardi di anni. La Commissione internazionale di stratigrafia pubblica la scala con i nomi. Dite gli anni a parole.",
              "שכבות צעירות בדרך כלל מונחות על עתיקות, אלא אם הערימה התהפכה. USGS מתארך את כדור הארץ ל-4.54 מיליארד שנה. הוועדה הבינלאומית לסטרטיגרפיה מפרסמת את סרגל הזמן בעל השמות. אמרו את השנים במילים."),
             (("What does 4.54 billion years come from on this site?", "D’où vient 4,54 milliards d’années ici ?", "¿De dónde sale 4.540 millones de años aquí?", "من أين يأتي رقم 4.54 مليار سنة هنا؟", "Da dove arriva 4,54 miliardi di anni qui?", "מאיפה מגיע 4.54 מיליארד שנה באתר הזה?"),
              ("Why say the words instead of a two-letter age?", "Pourquoi des mots plutôt qu’un âge en deux lettres ?", "¿Por qué palabras y no una edad de dos letras?", "لماذا الكلمات لا عمر من حرفين؟", "Perché parole e non un’età di due lettere?", "למה מילים ולא גיל בן שתי אותיות?")),
             ("The USGS figure is 4.54 billion years. Some school standards still print 4.6 billion. Keep those two numbers apart.",)),
        unit("field",
             ("Look, sketch, leave the rock", "Regarder, dessiner, laisser la roche", "Mirar, dibujar, dejar la roca", "انظر وارسم واترك الصخر", "Guarda, disegna, lascia la roccia", "הסתכלו, שרטטו, השאירו את הסלע"),
             ("A geologic map paints rock units and draws the lines where they meet. MIT 12.001 includes mapping and two optional day trips. This free page stops at a notebook: one permitted view, a sketch, and no collecting.",
              "Une carte géologique colore les unités et trace leurs contacts. Le 12.001 du MIT inclut la cartographie et deux sorties d’un jour, facultatives. Cette page gratuite s’arrête au carnet : une vue autorisée, un croquis, et pas de collecte.",
              "Un mapa geológico pinta unidades y dibuja sus contactos. MIT 12.001 incluye mapas y dos salidas de un día, opcionales. Esta página gratis se queda en el cuaderno: una vista permitida, un dibujo, y nada de recoger.",
              "الخريطة الجيولوجية تلوّن الوحدات وترسم خطوط التقائها. يشمل 12.001 في MIT رسم الخرائط ورحلتين اختياريتين ليوم واحد. تتوقف هذه الصفحة المجانية عند الدفتر: مشهد مسموح، ورسمة، وبلا جمع.",
              "Una carta geologica colora le unità e disegna i contatti. MIT 12.001 include la cartografia e due uscite di un giorno, facoltative. Questa pagina gratuita si ferma al taccuino: una vista permessa, uno schizzo, e nessuna raccolta.",
              "מפה גאולוגית צובעת יחידות סלע ומשרטטת את קווי המגע. MIT 12.001 כולל מיפוי ושני ימי שדה רשות. העמוד החינמי הזה נעצר במחברת: מבט מותר, שרטוט, ובלי איסוף."),
             (("What do you bring home instead of a rock?", "Que ramenez-vous à la place d’une roche ?", "¿Qué te llevas en lugar de una roca?", "ماذا تعيد بدل الصخر؟", "Che cosa porti a casa al posto di una roccia?", "מה מביאים הביתה במקום סלע?"),
              ("What is a contact on a geologic map?", "Qu’est-ce qu’un contact sur une carte ?", "¿Qué es un contacto en un mapa geológico?", "ما هو التماس على الخريطة؟", "Che cos’è un contatto su una carta?", "מהו מגע במפה גאולוגית?")),
             ("The sample is the notebook. Leave protected rock where it is.",)),
    ],
    [("MIT Course 12 catalog, 12.001", MIT12),
     ("USGS — Age of the Earth", USGS_AGE),
     ("International Chronostratigraphic Chart", ICS),
     ("NGSS MS-ESS1-4", NGSS_MS)],
    (("What are the three rock families, and which one usually holds fossils?",
      "Quelles sont les trois familles, et laquelle porte en général les fossiles ?",
      "¿Cuáles son las tres familias, y cuál suele guardar fósiles?",
      "ما عائلات الصخور الثلاث، وأيها تحمل الأحافير عادة؟",
      "Quali sono le tre famiglie, e quale di solito custodisce i fossili?",
      "מהן שלוש משפחות הסלע, ואיזו מהן בדרך כלל מחזיקה מאובנים?"),
     ("Whose number is 4.54 billion years, and which standard still says 4.6?",
      "À qui appartient 4,54 milliards d’années, et quelle norme dit encore 4,6 ?",
      "¿De quién es 4.540 millones de años, y qué norma dice todavía 4.6?",
      "لمن رقم 4.54 مليار سنة، وأي معيار ما زال يقول 4.6؟",
      "Di chi è 4,54 miliardi di anni, e quale standard dice ancora 4,6?",
      "של מי המספר 4.54 מיליארד, ואיזה תקן עדיין אומר 4.6?"),
     ("Why does this course forbid collecting?",
      "Pourquoi ce cours interdit-il la collecte ?",
      "¿Por qué este curso prohíbe recoger?",
      "لماذا يمنع هذا المسار الجمع؟",
      "Perché questo percorso vieta la raccolta?",
      "למה המסלול הזה אוסר איסוף?")),
)

STRAT = C(
    "Stratigraphic_Record", "GEOL 120", "earth",
    ("Rock layers", "Couches de roche", "Capas de roca", "طبقات الصخر", "Strati di roccia", "שכבות סלע"),
    ("How layers and fossils put the world in order.",
     "Comment couches et fossiles mettent le monde en ordre.",
     "Cómo las capas y los fósiles ordenan el mundo.",
     "كيف ترتّب الطبقات والأحافير العالم.",
     "Come strati e fossili mettono in ordine il mondo.",
     "איך שכבות ומאובנים מסדרים את העולם."),
    ("A formation is a body of rock. A period is a span of time. They are not the same kind of name. This course uses the USGS age of Earth, the International Commission on Stratigraphy chart, and the fossil coins already on this site.",
     "Une formation est un corps de roche. Une période est une durée. Ce ne sont pas le même genre de nom. Ce cours utilise l’âge USGS de la Terre, le tableau de la Commission internationale de stratigraphie, et les pièces fossiles déjà sur ce site.",
     "Una formación es un cuerpo de roca. Un período es un tramo de tiempo. No son el mismo tipo de nombre. Este curso usa la edad USGS de la Tierra, la tabla de la Comisión Internacional de Estratigrafía y las monedas de fósiles de este sitio.",
     "التكوين جسم من الصخر. والفترة مدى من الزمن. ليسا نوع الاسم نفسه. يستخدم هذا المسار عمر الأرض لدى USGS وجدول اللجنة الدولية للطبقات وقطع الأحافير الموجودة على هذا الموقع.",
     "Una formazione è un corpo di roccia. Un periodo è un intervallo di tempo. Non sono lo stesso tipo di nome. Questo percorso usa l’età USGS della Terra, la carta della Commissione internazionale di stratigrafia e le monete fossili già su questo sito.",
     "תצורה היא גוף סלע. תור הוא פרק זמן. אלה לא אותו סוג של שם. המסלול משתמש בגיל USGS של כדור הארץ, בטבלת הוועדה הבינלאומית לסטרטיגרפיה, ובמטבעות המאובנים שכבר באתר."),
    "International Chronostratigraphic Chart", ICS,
    weeks(
        ("A layer is a page", "Une couche est une page", "Una capa es una página", "الطبقة صفحة", "Uno strato è una pagina", "שכבה היא עמוד"),
        ("Fossils as evidence", "Les fossiles, preuves", "Fósiles como prueba", "أحافير كدليل", "Fossili come prova", "מאובנים כראיה"),
        ("Index fossils", "Fossiles marqueurs", "Fósiles guía", "أحافير دالة", "Fossili guida", "מאובני מדד"),
        ("Rock name or time name", "Nom de roche ou de temps", "Nombre de roca o de tiempo", "اسم صخر أو اسم زمن", "Nome di roccia o di tempo", "שם סלע או שם זמן"),
        ("About 539 million years", "Environ 539 millions d’années", "Unos 539 millones de años", "نحو 539 مليون سنة", "Circa 539 milioni di anni", "כ-539 מיליון שנה"),
        ("A golden spike", "Un clou d’or", "Un clavo de oro", "مسمار ذهبي", "Un chiodo d’oro", "מסמר זהב"),
        ("66 million years", "66 millions d’années", "66 millones de años", "66 مليون سنة", "66 milioni di anni", "66 מיליון שנה"),
        ("Parent and daughter", "Parent et fille", "Padre e hija", "أصل وابنة", "Genitore e figlia", "הורה ובת"),
        ("Half-life", "Demi-vie", "Vida media", "عمر النصف", "Tempo di dimezzamento", "זמן מחצית"),
        ("Open a coin", "Ouvrir une pièce", "Abrir una moneda", "افتح قطعة", "Apri una moneta", "לפתוח מטבע"),
        ("Correlation", "Corrélation", "Correlación", "مضاهاة", "Correlazione", "מתאם"),
        ("Missing pages", "Pages manquantes", "Páginas que faltan", "صفحات مفقودة", "Pagine mancanti", "עמודים חסרים"),
        ("Order five layers", "Ordonner cinq couches", "Ordenar cinco capas", "رتّب خمس طبقات", "Ordina cinque strati", "סדר חמש שכבות"),
        ("Write the years", "Écrire les années", "Escribir los años", "اكتب السنوات", "Scrivi gli anni", "כתבו את השנים"),
        ("One paragraph", "Un paragraphe", "Un párrafo", "فقرة واحدة", "Un paragrafo", "פסקה אחת"),
    ),
    [
        unit("layers",
             ("Younger on older", "Plus jeune sur plus vieux", "Más joven sobre más viejo", "الأحدث فوق الأقدم", "Più giovane sul più vecchio", "צעיר על עתיק"),
             ("Superposition is the usual order, not a promise. Faults, folds, and overturned beds break it. Say so before you date a stack from position alone.",
              "La superposition est l’ordre habituel, pas une promesse. Failles, plis et couches renversées la cassent. Dites-le avant de dater une pile par la seule position.",
              "La superposición es el orden habitual, no una promesa. Fallas, pliegues y capas volcadas la rompen. Dilo antes de fechar una pila solo por la posición.",
              "التراكب هو الترتيب المعتاد لا وعد. الصدوع والطيات والطبقات المقلوبة تكسره. قولوا ذلك قبل تأريخ رزمة من موضعها وحده.",
              "La sovrapposizione è l’ordine solito, non una promessa. Faglie, pieghe e strati rovesciati la rompono. Ditelo prima di datare una pila solo dalla posizione.",
              "סופרפוזיציה היא הסדר הרגיל, לא הבטחה. העתקים, קמטים ושכבות הפוכות שוברים אותה. אמרו זאת לפני שמתארכים ערימה לפי המיקום לבדו."),
             (("When would the top layer not be the youngest?", "Quand la couche du haut n’est-elle pas la plus jeune ?", "¿Cuándo la capa de arriba no es la más joven?", "متى لا تكون الطبقة العليا هي الأحدث؟", "Quando lo strato in cima non è il più giovane?", "מתי השכבה העליונה אינה הצעירה?"),
              ("What is a formation, as opposed to a period?", "Qu’est-ce qu’une formation, face à une période ?", "¿Qué es una formación, frente a un período?", "ما التكوين مقابل الفترة؟", "Che cos’è una formazione, rispetto a un periodo?", "מהי תצורה לעומת תור?")),
             ("Position is a clue. It is not, by itself, a date.",)),
        unit("fossils",
             ("Fossils correlate", "Les fossiles corrèlent", "Los fósiles correlacionan", "الأحافير تضاهي", "I fossili correlano", "מאובנים מתאמים"),
             ("An index fossil is widespread and lasts a short time on the chart, so two distant layers that share it can be the same part of time. They are not the same quarry. The coins on the world map are the lab: read what, when, and where.",
              "Un fossile marqueur est répandu et bref sur le tableau : deux couches lointaines qui le partagent peuvent être la même part du temps. Ce n’est pas la même carrière. Les pièces de la carte du monde sont le labo : lire quoi, quand, où.",
              "Un fósil guía es amplio y breve en la escala: dos capas lejanas que lo comparten pueden ser la misma parte del tiempo. No son la misma cantera. Las monedas del mapa mundial son el laboratorio: lee qué, cuándo y dónde.",
              "الأحفورة الدالة واسعة وقصيرة على الجدول: طبقتان بعيدتان تشتركان فيها قد تكونان الجزء نفسه من الزمن. ليستا المحجر نفسه. قطع خريطة العالم هي المختبر: اقرأوا ماذا ومتى وأين.",
              "Un fossile guida è diffuso e breve sulla scala: due strati lontani che lo condividono possono essere la stessa parte del tempo. Non sono la stessa cava. Le monete della mappa mondiale sono il laboratorio: leggi cosa, quando e dove.",
              "מאובן מדד נפוץ וקצר על הסרגל: שתי שכבות רחוקות שחולקות אותו יכולות להיות אותו חלק של הזמן. הן לא אותה מחצבה. מטבעות מפת העולם הם המעבדה: קראו מה, מתי ואיפה."),
             (("What makes a fossil useful for correlation?", "Qu’est-ce qui rend un fossile utile pour corréler ?", "¿Qué hace útil a un fósil para correlacionar?", "ما الذي يجعل الأحفورة مفيدة للمضاهاة؟", "Che cosa rende un fossile utile per la correlazione?", "מה הופך מאובן לשימושי למתאם?"),
              ("Why is the same fossil not the same place?", "Pourquoi le même fossile n’est-il pas le même lieu ?", "¿Por qué el mismo fósil no es el mismo lugar?", "لماذا الأحفورة نفسها ليست المكان نفسه؟", "Perché lo stesso fossile non è lo stesso luogo?", "למה אותו מאובן אינו אותו מקום?")),
             ("Correlation matches time. It does not move the quarries onto each other.",)),
        unit("spikes",
             ("Named boundaries", "Des limites nommées", "Límites con nombre", "حدود مسمّاة", "Limiti con un nome", "גבולות עם שם"),
             ("The Cambrian begins about 539 million years ago on the charts this site uses. A golden spike is a chosen point in real rock, not a prize. The end of the Permian is about 252 million years ago. The end of the Cretaceous is 66 million years ago. Chicxulub and the Gubbio clay are two records of that later boundary.",
              "Le Cambrien commence il y a environ 539 millions d’années sur les tableaux de ce site. Un clou d’or est un point choisi dans une vraie roche, pas un trophée. La fin du Permien est il y a environ 252 millions d’années. La fin du Crétacé est il y a 66 millions d’années. Chicxulub et l’argile de Gubbio sont deux archives de cette limite plus récente.",
              "El Cámbrico empieza hace unos 539 millones de años en las escalas de este sitio. Un clavo de oro es un punto elegido en roca real, no un trofeo. El final del Pérmico es hace unos 252 millones de años. El final del Cretácico es hace 66 millones de años. Chicxulub y la arcilla de Gubbio son dos registros de ese límite más reciente.",
              "يبدأ الكمبري قبل نحو 539 مليون سنة على الجداول التي يستخدمها هذا الموقع. المسمار الذهبي نقطة مختارة في صخر حقيقي لا جائزة. نهاية البرمي قبل نحو 252 مليون سنة. نهاية الطباشيري قبل 66 مليون سنة. تشيكشولوب وطين غوبيو سجلان لذلك الحد الأحدث.",
              "Il Cambriano inizia circa 539 milioni di anni fa sulle scale di questo sito. Un chiodo d’oro è un punto scelto in roccia vera, non un trofeo. La fine del Permiano è circa 252 milioni di anni fa. La fine del Cretaceo è 66 milioni di anni fa. Chicxulub e l’argilla di Gubbio sono due archivi di quel limite più recente.",
              "הקמבריון מתחיל לפני כ-539 מיליון שנה בסרגלים של האתר הזה. מסמר זהב הוא נקודה שנבחרה בסלע אמיתי, לא גביע. סוף הפרם לפני כ-252 מיליון שנה. סוף הקרטיקון לפני 66 מיליון שנה. צ'יקשולוב וחרסית גוביו הם שני תיעודים של הגבול המאוחר יותר."),
             (("What is a golden spike, in one sentence?", "Qu’est-ce qu’un clou d’or, en une phrase ?", "¿Qué es un clavo de oro, en una frase?", "ما المسمار الذهبي في جملة؟", "Che cos’è un chiodo d’oro, in una frase?", "מהו מסמר זהב, במשפט אחד?"),
              ("Name two places tied to 66 million years ago.", "Nommez deux lieux liés à il y a 66 millions d’années.", "Nombra dos lugares ligados a hace 66 millones de años.", "سمّ مكانين مرتبطين بقبل 66 مليون سنة.", "Nomina due luoghi legati a 66 milioni di anni fa.", "ציינו שני מקומות הקשורים ללפני 66 מיליון שנה.")),
             ("Say million years ago in words. The chart, not a nickname, holds the boundary.",)),
        unit("clocks",
             ("A mineral clock", "Une horloge minérale", "Un reloj mineral", "ساعة معدنية", "Un orologio minerale", "שעון מינרל"),
             ("A radiometric date counts parent and daughter atoms in a mineral. It dates that mineral. The age of the layer is an argument from the mineral, the fossils, and the contacts. A half-life is a statistical clock, not a timer on one atom.",
              "Une date radiométrique compte les atomes parents et fils dans un minéral. Elle date ce minéral. L’âge de la couche est un argument à partir du minéral, des fossiles et des contacts. Une demi-vie est une horloge statistique, pas un minuteur sur un atome.",
              "Una fecha radiométrica cuenta átomos padre e hijo en un mineral. Data ese mineral. La edad de la capa es un argumento desde el mineral, los fósiles y los contactos. La vida media es un reloj estadístico, no un temporizador en un átomo.",
              "التاريخ الإشعاعي يعدّ ذرات الأصل والابنة في معدن. يؤرّخ ذلك المعدن. عمر الطبقة حجة من المعدن والأحافير والتماسات. عمر النصف ساعة إحصائية لا مؤقت على ذرة واحدة.",
              "Una data radiometrica conta atomi genitori e figli in un minerale. Data quel minerale. L’età dello strato è un argomento dal minerale, dai fossili e dai contatti. Il tempo di dimezzamento è un orologio statistico, non un timer su un atomo.",
              "תאריך רדיומטרי סופר אטומי הורה ובת במינרל. הוא מתארך את המינרל. גיל השכבה הוא טיעון מהמינרל, מהמאובנים ומהמגעים. זמן מחצית הוא שעון סטטיסטי, לא טיימר על אטום אחד."),
             (("What object does a radiometric date actually date?", "Quel objet une date radiométrique date-t-elle vraiment ?", "¿Qué objeto fecha de verdad una data radiométrica?", "أي شيء يؤرخه التاريخ الإشعاعي فعلاً؟", "Quale oggetto data davvero una data radiometrica?", "איזה עצם תאריך רדיומטרי מתארך באמת?"),
              ("Why is half-life not a countdown for one atom?", "Pourquoi la demi-vie n’est-elle pas un compte à rebours pour un atome ?", "¿Por qué la vida media no es una cuenta atrás de un átomo?", "لماذا عمر النصف ليس عدّاً تنازلياً لذرة؟", "Perché il tempo di dimezzamento non è un conto alla rovescia per un atomo?", "למה זמן מחצית אינו ספירה לאחור של אטום אחד?")),
             ("The clock is in the mineral. The layer’s story uses more than one line of evidence.",)),
    ],
    [("International Chronostratigraphic Chart", ICS),
     ("USGS — Age of the Earth", USGS_AGE),
     ("NPS — Geologic time scale", NPS_TIME),
     ("NGSS 4-ESS1-1", NGSS_4)],
    (("How is a rock formation different from a time period?",
      "En quoi une formation diffère-t-elle d’une période ?",
      "¿En qué se diferencia una formación de un período?",
      "كيف يختلف التكوين الصخري عن فترة زمنية؟",
      "In che cosa una formazione è diversa da un periodo?",
      "במה תצורה שונה מתור?"),
     ("What two records does this site keep paired at 66 million years ago?",
      "Quelles deux archives ce site garde-t-il ensemble il y a 66 millions d’années ?",
      "¿Qué dos registros empareja este sitio hace 66 millones de años?",
      "أي سجلين يبقيهما هذا الموقع معاً قبل 66 مليون سنة؟",
      "Quali due archivi questo sito tiene accoppiati a 66 milioni di anni fa?",
      "אילו שני תיעודים האתר מצמיד ללפני 66 מיליון שנה?"),
     ("What does an index fossil correlate, and what does it not prove?",
      "Que corrèle un fossile marqueur, et que ne prouve-t-il pas ?",
      "¿Qué correlaciona un fósil guía, y qué no prueba?",
      "ماذا تضاهي الأحفورة الدالة، وماذا لا تثبت؟",
      "Che cosa correla un fossile guida, e che cosa non prova?",
      "מה מאובן מדד מתאם, ומה הוא לא מוכיח?")),
)

FIELD = C(
    "Field_Geology", "GEOL 210", "earth",
    ("Field geology", "Géologie de terrain", "Geología de campo", "جيولوجيا الحقل", "Geologia di campo", "גאולוגיה בשדה"),
    ("Notebook, map, and permission. No collecting.",
     "Carnet, carte, et permission. Pas de collecte.",
     "Cuaderno, mapa y permiso. Nada de recoger.",
     "دفتر وخريطة وإذن. بلا جمع.",
     "Taccuino, carta e permesso. Nessuna raccolta.",
     "מחברת, מפה ורשות. בלי איסוף."),
    ("MIT’s bachelor’s path in Earth science asks for a field or lab subject. 12.115 and 12.116 are Field Geology and Analysis of Geologic Data. This free module teaches the notebook those courses assume. It is not a supervised traverse and it does not license anyone to break rock.",
     "Le parcours de licence du MIT en sciences de la Terre demande un sujet de terrain ou de labo. 12.115 et 12.116 sont Field Geology et Analysis of Geologic Data. Ce module gratuit enseigne le carnet que ces cours supposent. Ce n’est pas une traversée encadrée et il n’autorise personne à casser la roche.",
     "La licenciatura del MIT en ciencias de la Tierra pide una materia de campo o de laboratorio. 12.115 y 12.116 son Field Geology y Analysis of Geologic Data. Este módulo gratis enseña el cuaderno que esos cursos dan por sentado. No es un recorrido supervisado y no autoriza a romper roca.",
     "مسار البكالوريوس في علوم الأرض في MIT يطلب مادة حقل أو مختبر. 12.115 و12.116 هما الجيولوجيا الحقلية وتحليل البيانات الجيولوجية. تعلّم هذه الوحدة المجانية الدفتر الذي تفترضه تلك المقررات. ليست اجتيازاً بإشراف ولا ترخّص لأحد كسر الصخر.",
     "Il percorso di laurea del MIT in scienze della Terra chiede una materia di campo o di laboratorio. 12.115 e 12.116 sono Field Geology e Analysis of Geologic Data. Questo modulo gratuito insegna il taccuino che quei corsi presuppongono. Non è un percorso sorvegliato e non autorizza nessuno a spaccare roccia.",
     "מסלול התואר של MIT במדעי כדור הארץ דורש מקצוע שדה או מעבדה. 12.115 ו-12.116 הם גאולוגיית שדה וניתוח נתונים גאולוגיים. המודול החינמי מלמד את המחברת שהקורסים האלה מניחים. זה אינו חתך מודרך והוא לא מרשה לאיש לשבור סלע."),
    "MIT 12.115 and 12.116", MIT_DEPT,
    weeks(
        ("Permission", "Permission", "Permiso", "الإذن", "Permesso", "רשות"),
        ("The notebook", "Le carnet", "El cuaderno", "الدفتر", "Il taccuino", "המחברת"),
        ("Strike and dip", "Direction et pendage", "Rumbo y buzamiento", "المضرب والميل", "Direzione e immersione", "כיוון ונטייה"),
        ("A contact", "Un contact", "Un contacto", "تماس", "Un contatto", "מגע"),
        ("Pace and compass", "Pas et boussole", "Paso y brújula", "خطوة وبوصلة", "Passo e bussola", "צעד ומצפן"),
        ("Four lines", "Quatre lignes", "Cuatro líneas", "أربعة أسطر", "Quattro righe", "ארבע שורות"),
        ("Do not collect", "Ne pas collecter", "No recoger", "لا تجمع", "Non raccogliere", "אל תאספו"),
        ("Safety", "Sécurité", "Seguridad", "السلامة", "Sicurezza", "בטיחות"),
        ("A column", "Une colonne", "Una columna", "عمود", "Una colonna", "טור"),
        ("Stop before the stereonet", "Avant le canevas", "Antes de la falsilla", "قبل شبكة الإسقاط", "Prima dello stereonet", "לפני הסטריאונט"),
        ("Practice on a curb", "S’exercer sur un trottoir", "Practicar en un bordillo", "تدرّب على رصيف", "Esercitati su un marciapiede", "תרגול על שפת מדרכה"),
        ("Read a legend", "Lire une légende", "Leer una leyenda", "اقرأ مفتاح خريطة", "Leggi una legenda", "קראו מקרא"),
        ("What camp adds", "Ce qu’ajoute le camp", "Lo que añade el campamento", "ما يضيفه المعسكر", "Che cosa aggiunge il campo", "מה המחנה מוסיף"),
        ("One-page report", "Rapport d’une page", "Informe de una página", "تقرير من صفحة", "Rapporto di una pagina", "דוח של עמוד"),
        ("Not the capstone yet", "Pas encore le projet final", "Aún no es el trabajo final", "ليس المشروع الختامي بعد", "Non è ancora la tesi", "עדיין לא פרויקט הסיום"),
    ),
    [
        unit("permission",
             ("Ask before you walk the outcrop", "Demandez avant l’affleurement", "Pide permiso antes del afloramiento", "اطلب الإذن قبل المكشف", "Chiedi prima dell’affioramento", "בקשו רשות לפני המחשוף"),
             ("Parks, private land, and fossil sites have rules. A school yard or a curb is enough for the four-line practice. A real fossil site on this map is for reading, not for a hammer.",
              "Parcs, terrains privés et sites fossilifères ont des règles. Une cour d’école ou un trottoir suffit pour l’exercice en quatre lignes. Un vrai site fossile de cette carte se lit, il ne se martèle pas.",
              "Parques, terreno privado y sitios de fósiles tienen reglas. Un patio o un bordillo bastan para el ejercicio de cuatro líneas. Un sitio fósil de este mapa se lee, no se golpea.",
              "للحدائق والأرض الخاصة ومواقع الأحافير قواعد. ساحة مدرسة أو رصيف يكفيان لتمرين الأسطر الأربعة. موقع أحافير حقيقي على هذه الخريطة للقراءة لا للمطرقة.",
              "Parchi, terreni privati e siti fossiliferi hanno regole. Un cortile o un marciapiede bastano per l’esercizio in quattro righe. Un sito fossile vero di questa mappa si legge, non si martella.",
              "לגנים, לקרקע פרטית ולאתרי מאובנים יש כללים. חצר בית ספר או שפת מדרכה מספיקות לתרגיל ארבע השורות. אתר מאובנים אמיתי במפה הזו לקריאה, לא לפטיש."),
             (("Where is it acceptable to practice the four lines?", "Où peut-on s’exercer aux quatre lignes ?", "¿Dónde se puede practicar las cuatro líneas?", "أين يجوز تمرين الأسطر الأربعة؟", "Dove si possono provare le quattro righe?", "איפה מותר לתרגל את ארבע השורות?"),
              ("What do you not do at a mapped fossil site?", "Que ne faites-vous pas sur un site fossile de la carte ?", "¿Qué no haces en un sitio fósil del mapa?", "ماذا لا تفعل في موقع أحافير على الخريطة؟", "Che cosa non fai in un sito fossile della mappa?", "מה לא עושים באתר מאובנים שעל המפה?")),
             ("Permission comes before the compass.",)),
        unit("notebook",
             ("Four lines and a sketch", "Quatre lignes et un croquis", "Cuatro líneas y un dibujo", "أربعة أسطر ورسمة", "Quattro righe e uno schizzo", "ארבע שורות ושרטוט"),
             ("Write the rock, the grain size, the structure, and any fossils. Add a sketch with a scale, such as a coin you do not leave behind as litter. Strike and dip describe a tilted plane. A contact is where two units meet.",
              "Écrivez la roche, la taille des grains, la structure, et les fossiles. Ajoutez un croquis à l’échelle, par exemple une pièce que vous ne laissez pas comme déchet. Direction et pendage décrivent un plan incliné. Un contact est la rencontre de deux unités.",
              "Escribe la roca, el tamaño de grano, la estructura y los fósiles. Añade un dibujo con escala, por ejemplo una moneda que no dejas como basura. Rumbo y buzamiento describen un plano inclinado. Un contacto es donde se encuentran dos unidades.",
              "اكتب الصخر وحجم الحبيبات والتركيب وأي أحافير. أضف رسمة بمقياس، كقطعة نقد لا تتركها نفايات. المضرب والميل يصفان مستوياً مائلاً. التماس هو التقاء وحدتين.",
              "Scrivi la roccia, la dimensione dei grani, la struttura e i fossili. Aggiungi uno schizzo in scala, per esempio una moneta che non lasci come rifiuto. Direzione e immersione descrivono un piano inclinato. Un contatto è dove si incontrano due unità.",
              "כתבו את הסלע, גודל הגרגר, המבנה, ומאובנים אם יש. הוסיפו שרטוט עם קנה מידה, למשל מטבע שלא משאירים כפסולת. כיוון ונטייה מתארים מישור נטוי. מגע הוא מפגש של שתי יחידות."),
             (("What are the four lines?", "Quelles sont les quatre lignes ?", "¿Cuáles son las cuatro líneas?", "ما الأسطر الأربعة؟", "Quali sono le quattro righe?", "מהן ארבע השורות?"),
              ("What does a contact mark?", "Que marque un contact ?", "¿Qué marca un contacto?", "ماذا يعلّم التماس؟", "Che cosa segna un contatto?", "מה מסמן מגע?")),
             ("The notebook is the specimen.",)),
        unit("maps",
             ("Read a published map", "Lire une carte publiée", "Leer un mapa publicado", "اقرأ خريطة منشورة", "Leggi una carta pubblicata", "קראו מפה שפורסמה"),
             ("The USGS National Geologic Map Database is the place to see a real legend. Match colors to units. Do not invent a formation name for a curb. A stereonet comes later; this course stops at the sketch and the legend.",
              "La base nationale de cartes géologiques de l’USGS sert à voir une vraie légende. Reliez les couleurs aux unités. N’inventez pas un nom de formation pour un trottoir. Le canevas vient plus tard ; ce cours s’arrête au croquis et à la légende.",
              "La base nacional de mapas geológicos del USGS sirve para ver una leyenda real. Une colores y unidades. No inventes un nombre de formación para un bordillo. La falsilla viene después; este curso se queda en el dibujo y la leyenda.",
              "قاعدة الخرائط الجيولوجية الوطنية لهيئة المسح الأمريكية مكان لرؤية مفتاح حقيقي. طابقوا الألوان بالوحدات. لا تخترعوا اسم تكوين لرصيف. شبكة الإسقاط لاحقاً. يتوقف هذا المسار عند الرسمة والمفتاح.",
              "Il database nazionale delle carte geologiche dell’USGS serve a vedere una legenda vera. Abbina i colori alle unità. Non inventare un nome di formazione per un marciapiede. Lo stereonet viene dopo; questo percorso si ferma allo schizzo e alla legenda.",
              "מסד המפות הגאולוגיות של USGS הוא המקום לראות מקרא אמיתי. התאימו צבעים ליחידות. אל תמציאו שם תצורה לשפת מדרכה. סטריאונט בא אחר כך. המסלול נעצר בשרטוט ובמקרא."),
             (("What database do you open for a real legend?", "Quelle base ouvrez-vous pour une vraie légende ?", "¿Qué base abres para una leyenda real?", "أي قاعدة تفتح لمفتاح حقيقي؟", "Quale database apri per una legenda vera?", "איזה מסד פותחים למקרא אמיתי?"),
              ("Why not name a formation after a curb?", "Pourquoi ne pas nommer une formation d’après un trottoir ?", "¿Por qué no nombrar una formación por un bordillo?", "لماذا لا تسمّي تكويناً باسم رصيف؟", "Perché non dare a una formazione il nome di un marciapiede?", "למה לא לקרוא לתצורה על שם שפת מדרכה?")),
             ("A legend is a published claim. A curb is practice.",)),
        unit("report",
             ("One page, then stop", "Une page, puis stop", "Una página, y basta", "صفحة ثم توقف", "Una pagina, poi basta", "עמוד אחד, ואז די"),
             ("The report names the place, the four lines, what you did not collect, and the map or page you compared. A field camp like MIT 12.115 adds a supervised traverse. That camp is not written here yet.",
              "Le rapport nomme le lieu, les quatre lignes, ce que vous n’avez pas collecté, et la carte ou la page comparée. Un camp comme le 12.115 du MIT ajoute une traversée encadrée. Ce camp n’est pas encore écrit ici.",
              "El informe nombra el lugar, las cuatro líneas, lo que no recogiste y el mapa o la página que comparaste. Un campamento como MIT 12.115 añade un recorrido supervisado. Ese campamento aún no está escrito aquí.",
              "يسمّي التقرير المكان والأسطر الأربعة وما لم تجمعه والخريطة أو الصفحة التي قارنتها. يضيف معسكر مثل 12.115 في MIT اجتيازاً بإشراف. ذلك المعسكر لم يُكتب هنا بعد.",
              "Il rapporto nomina il luogo, le quattro righe, che cosa non hai raccolto e la carta o la pagina confrontata. Un campo come MIT 12.115 aggiunge un percorso sorvegliato. Quel campo non è ancora scritto qui.",
              "הדוח מציין את המקום, את ארבע השורות, מה לא אספתם, ואת המפה או העמוד שהשוויתם. מחנה כמו MIT 12.115 מוסיף חתך מודרך. המחנה הזה עדיין לא נכתב כאן."),
             (("What must the one-page report include about collecting?", "Que doit dire le rapport d’une page sur la collecte ?", "¿Qué debe decir el informe de una página sobre recoger?", "ماذا يجب أن يقول تقرير الصفحة عن الجمع؟", "Che cosa deve dire il rapporto di una pagina sulla raccolta?", "מה הדוח בן העמוד חייב לומר על איסוף?"),
              ("What does a real field camp add that this page does not?", "Qu’ajoute un vrai camp que cette page n’a pas ?", "¿Qué añade un campamento real que esta página no tiene?", "ماذا يضيف معسكر حقيقي لا تملكه هذه الصفحة؟", "Che cosa aggiunge un campo vero che questa pagina non ha?", "מה מחנה אמיתי מוסיף ושאין בעמוד הזה?")),
             ("Stop at the report. The supervised camp is still to be written.",)),
    ],
    [("MIT EAPS degree, field subjects 12.115 and 12.116", MIT_DEPT),
     ("USGS National Geologic Map Database", USGS_MAP),
     ("NPS — Geologic time scale", NPS_TIME)],
    (("What are the four lines of an outcrop note?",
      "Quelles sont les quatre lignes d’une note d’affleurement ?",
      "¿Cuáles son las cuatro líneas de una nota de afloramiento?",
      "ما أسطر ملاحظة المكشف الأربعة؟",
      "Quali sono le quattro righe di una nota di affioramento?",
      "מהן ארבע שורות הערת מחשוף?"),
     ("Why is the notebook the sample?",
      "Pourquoi le carnet est-il l’échantillon ?",
      "¿Por qué el cuaderno es la muestra?",
      "لماذا الدفتر هو العينة؟",
      "Perché il taccuino è il campione?",
      "למה המחברת היא הדוגמה?"),
     ("Which MIT subjects is this module modeled on, and what is it not?",
      "Sur quels sujets du MIT ce module est-il calqué, et que n’est-il pas ?",
      "¿En qué materias del MIT se modela este módulo, y qué no es?",
      "على أي مواد في MIT بُنيت هذه الوحدة، وما ليست؟",
      "Su quali materie del MIT è modellato questo modulo, e che cosa non è?",
      "על אילו מקצועות ב-MIT המודול מעוצב, ומה הוא לא?")),
)

ARCH = C(
    "World_Archaeology", "ARCH 110", "arch",
    ("Deep human past", "Passé humain profond", "Pasado humano", "الماضي البشري", "Passato umano", "העבר האנושי"),
    ("Material evidence of people, set in deep time.",
     "Preuves matérielles des gens, dans le temps profond.",
     "Pruebas materiales de las personas, en el tiempo profundo.",
     "أدلة مادية على الناس، في الزمن العميق.",
     "Prove materiali delle persone, nel tempo profondo.",
     "ראיות חומריות של אנשים, בזמן עמוק."),
    ("UCL’s ARCL0002 is World Archaeology: The Deep History of Human Societies, a 30-credit undergraduate module. This outline follows that idea: people, things, and time longer than writing. It is not UCL’s module.",
     "ARCL0002 à UCL est World Archaeology : The Deep History of Human Societies, un module de licence de 30 crédits. Ce plan suit cette idée : des gens, des choses, et un temps plus long que l’écriture. Ce n’est pas le module de UCL.",
     "ARCL0002 en UCL es World Archaeology: The Deep History of Human Societies, un módulo de grado de 30 créditos. Este plan sigue esa idea: personas, cosas y un tiempo más largo que la escritura. No es el módulo de UCL.",
     "ARCL0002 في UCL هو آثار العالم: التاريخ العميق للمجتمعات البشرية، وحدة بكالوريوس من 30 ساعة معتمدة. يتبع هذا المخطط تلك الفكرة: ناس وأشياء وزمن أطول من الكتابة. ليست وحدة UCL.",
     "ARCL0002 allo UCL è World Archaeology: The Deep History of Human Societies, un modulo di laurea da 30 crediti. Questo schema segue quell’idea: persone, cose e un tempo più lungo della scrittura. Non è il modulo dello UCL.",
     "ARCL0002 ב-UCL הוא ארכאולוגיה עולמית: ההיסטוריה העמוקה של חברות אנושיות, מודול תואר של 30 נקודות. המתווה עוקב אחרי הרעיון: אנשים, חפצים, וזמן ארוך מהכתב. זה אינו המודול של UCL."),
    "UCL ARCL0002", UCL_MOD,
    weeks(
        ("Things people left", "Ce que les gens ont laissé", "Lo que la gente dejó", "ما تركه الناس", "Ciò che la gente ha lasciato", "מה שאנשים השאירו"),
        ("Not treasure", "Pas un trésor", "No es un tesoro", "ليس كنزاً", "Non è un tesoro", "לא אוצר"),
        ("Older than writing", "Plus vieux que l’écriture", "Más viejo que la escritura", "أقدم من الكتابة", "Più antico della scrittura", "עתיק מהכתב"),
        ("About 300,000 years", "Environ 300 000 ans", "Unos 300 000 años", "نحو 300 ألف سنة", "Circa 300 000 anni", "כ-300 אלף שנה"),
        ("Stone tools", "Outils de pierre", "Herramientas de piedra", "أدوات حجرية", "Strumenti di pietra", "כלי אבן"),
        ("Farms are late", "Les fermes sont tardives", "Las granjas son tardías", "المزارع متأخرة", "Le fattorie sono tarde", "חוות הן מאוחרות"),
        ("A site", "Un site", "Un sitio", "موقع", "Un sito", "אתר"),
        ("Survey first", "D’abord le survey", "Primero el reconocimiento", "المسح أولاً", "Prima la ricognizione", "סקר קודם"),
        ("Dating that fits", "Une date qui convient", "Una fecha que encaja", "تأريخ يناسب", "Una data che calza", "תיארוך שמתאים"),
        ("About 50,000 years", "Environ 50 000 ans", "Unos 50 000 años", "نحو 50 ألف سنة", "Circa 50 000 anni", "כ-50 אלף שנה"),
        ("Permission and remains", "Permission et restes", "Permiso y restos", "إذن وبقايا", "Permesso e resti", "רשות ושרידים"),
        ("Fossil or artifact", "Fossile ou artefact", "Fósil o artefacto", "أحفورة أو أثر", "Fossile o manufatto", "מאובן או ממצא"),
        ("Read a species page", "Lire une page d’espèce", "Leer una página de especie", "اقرأ صفحة نوع", "Leggi una pagina di specie", "קראו עמוד מין"),
        ("A cast is not the fossil", "Un moulage n’est pas le fossile", "Un molde no es el fósil", "القالب ليس الأحفورة", "Un calco non è il fossile", "היציקה אינה המאובן"),
        ("Outline, not the module", "Un plan, pas le module", "Un plan, no el módulo", "مخطط لا الوحدة", "Uno schema, non il modulo", "מתווה, לא המודול"),
    ),
    [
        unit("things",
             ("The layer holds the story", "La couche tient l’histoire", "La capa guarda la historia", "الطبقة تمسك الحكاية", "Lo strato tiene la storia", "השכבה מחזיקה את הסיפור"),
             ("Archaeology studies what people made, used, and left, and the ground it sits in. An object without its layer has lost most of its story. It is not a hunt for treasure.",
              "L’archéologie étudie ce que les gens ont fait, utilisé et laissé, et le sol où cela repose. Un objet sans sa couche a perdu presque toute son histoire. Ce n’est pas une chasse au trésor.",
              "La arqueología estudia lo que la gente hizo, usó y dejó, y el suelo donde está. Un objeto sin su capa ha perdido casi toda su historia. No es una búsqueda de tesoros.",
              "تدرس الآثار ما صنعه الناس واستخدموه وتركوه، والأرض التي يقبع فيها. شيء بلا طبقته فقد معظم حكايته. ليست مطاردة كنز.",
              "L’archeologia studia ciò che le persone hanno fatto, usato e lasciato, e il terreno in cui sta. Un oggetto senza il suo strato ha perso quasi tutta la sua storia. Non è una caccia al tesoro.",
              "ארכאולוגיה חוקרת מה אנשים עשו, השתמשו והשאירו, ואת הקרקע שזה יושב בה. חפץ בלי השכבה שלו איבד את רוב הסיפור. זו לא ציד אוצרות."),
             (("What is lost when an object has no layer?", "Que perd un objet sans couche ?", "¿Qué se pierde si un objeto no tiene capa?", "ماذا يُفقد حين لا طبقة للشيء؟", "Che cosa si perde se un oggetto non ha strato?", "מה אובד כשלחפץ אין שכבה?"),
              ("Why is this not treasure hunting?", "Pourquoi ce n’est pas une chasse au trésor ?", "¿Por qué esto no es buscar tesoros?", "لماذا هذه ليست مطاردة كنز؟", "Perché questa non è una caccia al tesoro?", "למה זו לא ציד אוצרות?")),
             ("Context is the find. The object alone is the leftover.",)),
        unit("time",
             ("People in deep time", "Des gens dans le temps profond", "Personas en el tiempo profundo", "ناس في الزمن العميق", "Persone nel tempo profondo", "אנשים בזמן עמוק"),
             ("Writing is late. Smithsonian Human Origins summarizes fossils from Jebel Irhoud, Morocco, at about 300,000 years ago for Homo sapiens, and Oldowan stone tools at about 2.6 million years ago. Farms and cities are much later chapters. Those are research summaries, not a license to dig.",
              "L’écriture est tardive. Smithsonian Human Origins résume les fossiles de Jebel Irhoud, au Maroc, vers 300 000 ans pour Homo sapiens, et les outils oldowayens vers 2,6 millions d’années. Fermes et villes sont des chapitres bien plus tardifs. Ce sont des résumés de recherche, pas un permis de creuser.",
              "La escritura es tardía. Smithsonian Human Origins resume fósiles de Jebel Irhoud, Marruecos, hace unos 300 000 años para Homo sapiens, y herramientas olduvayenses hace unos 2,6 millones de años. Granjas y ciudades son capítulos muy posteriores. Son resúmenes de investigación, no un permiso para cavar.",
              "الكتابة متأخرة. يلخّص Smithsonian Human Origins أحافير جبل إيغود في المغرب قبل نحو 300 ألف سنة للإنسان العاقل، وأدوات أولدوان الحجرية قبل نحو 2.6 مليون سنة. المزارع والمدن فصول أحدث بكثير. هذه ملخصات بحث لا إذن حفر.",
              "La scrittura è tarda. Smithsonian Human Origins riassume fossili di Jebel Irhoud, in Marocco, a circa 300 000 anni fa per Homo sapiens, e strumenti olduvaiani a circa 2,6 milioni di anni fa. Fattorie e città sono capitoli molto più tardi. Sono riassunti di ricerca, non un permesso di scavare.",
              "הכתב מאוחר. Smithsonian Human Origins מסכם מאובנים מג'בל אירהוד במרוקו מלפני כ-300 אלף שנה להומו ספיינס, וכלי אולדובן מלפני כ-2.6 מיליון שנה. חוות וערים הם פרקים מאוחרים בהרבה. אלה סיכומי מחקר, לא רישיון לחפור."),
             (("About how old are the Jebel Irhoud fossils in that summary?", "Quel âge environ pour les fossiles de Jebel Irhoud dans ce résumé ?", "¿Qué edad aproximada tienen los fósiles de Jebel Irhoud en ese resumen?", "ما عمر أحافير جبل إيغود التقريبي في ذلك الملخص؟", "Che età hanno circa i fossili di Jebel Irhoud in quel riassunto?", "בן כמה בערך מאובני ג'בל אירהוד בסיכום הזה?"),
              ("Why are farms not the start of the human story?", "Pourquoi les fermes ne sont-elles pas le début de l’histoire humaine ?", "¿Por qué las granjas no son el inicio de la historia humana?", "لماذا المزارع ليست بداية الحكاية البشرية؟", "Perché le fattorie non sono l’inizio della storia umana?", "למה חוות אינן תחילת הסיפור האנושי?")),
             ("Use the Smithsonian pages for the ages. Do not add a zero.",)),
        unit("clocks",
             ("Pick a clock that fits", "Choisir une horloge qui va", "Elige un reloj que encaje", "اختر ساعة تناسب", "Scegli un orologio che calza", "בחרו שעון שמתאים"),
             ("Layers come first. Radiocarbon dates once-living material and fades out by about 50,000 years, so older questions need other clocks. Smithsonian Human Origins keeps a plain dating guide. A fossil of ancient life and an artifact of people answer different questions.",
              "Les couches d’abord. Le radiocarbone date une matière qui a vécu et s’efface vers 50 000 ans : les questions plus vieilles demandent d’autres horloges. Smithsonian Human Origins tient un guide simple. Un fossile de vie ancienne et un artefact de gens répondent à des questions différentes.",
              "Primero las capas. El radiocarbono fecha materia que estuvo viva y se apaga hacia los 50 000 años: las preguntas más viejas piden otros relojes. Smithsonian Human Origins tiene una guía clara. Un fósil de vida antigua y un artefacto de personas responden preguntas distintas.",
              "الطبقات أولاً. الكربون المشع يؤرّخ مادة كانت حية ويتلاشى نحو 50 ألف سنة، فالأسئلة الأقدم تحتاج ساعات أخرى. لدى Smithsonian Human Origins دليل تأريخ واضح. أحفورة حياة قديمة وأثر بشري يجيبان عن سؤالين مختلفين.",
              "Prima gli strati. Il radiocarbonio data materia che è stata viva e svanisce verso i 50 000 anni: le domande più antiche chiedono altri orologi. Smithsonian Human Origins ha una guida chiara. Un fossile di vita antica e un manufatto di persone rispondono a domande diverse.",
              "קודם השכבות. פחמן רדיואקטיבי מתארך חומר שהיה חי ודועך סביב 50 אלף שנה, אז שאלות עתיקות יותר צריכות שעונים אחרים. ל-Smithsonian Human Origins יש מדריך תיארוך פשוט. מאובן של חיים קדומים וממצא של אנשים עונים על שאלות שונות."),
             (("About when does radiocarbon stop being useful?", "Vers quand le radiocarbone cesse-t-il d’être utile ?", "¿Hacia cuándo el radiocarbono deja de servir?", "متى يتوقف الكربون المشع عن الفائدة تقريباً؟", "Verso quando il radiocarbonio smette di servire?", "בערך מתי פחמן רדיואקטיבי מפסיק להועיל?"),
              ("How is an artifact different from a trilobite?", "En quoi un artefact diffère-t-il d’un trilobite ?", "¿En qué un artefacto difiere de un trilobites?", "كيف يختلف الأثر عن ثلاثي الفصوص؟", "In che cosa un manufatto è diverso da un trilobite?", "במה ממצא שונה מטרילוביט?")),
             ("Match the clock to the material. Do not force one method onto every layer.",)),
        unit("ethics",
             ("A cast is labeled", "Un moulage est étiqueté", "Un molde se etiqueta", "يُوسَم القالب", "Un calco si etichetta", "יציקה מסומנת"),
             ("Human remains and community places need permission that this website cannot give. A museum cast is not the fossil. Say so in the caption. This page is an outline of ARCL0002’s idea, not the module and not a field school.",
              "Restes humains et lieux communautaires exigent une permission que ce site ne peut pas donner. Un moulage de musée n’est pas le fossile. Dites-le dans la légende. Cette page est un plan de l’idée d’ARCL0002, pas le module et pas une école de fouille.",
              "Los restos humanos y los lugares de una comunidad exigen un permiso que este sitio no puede dar. Un molde de museo no es el fósil. Dilo en el pie. Esta página es un plan de la idea de ARCL0002, no el módulo y no una escuela de campo.",
              "بقايا البشر وأماكن المجتمعات تحتاج إذناً لا يستطيع هذا الموقع منحه. قالب المتحف ليس الأحفورة. قولوا ذلك في التعليق. هذه الصفحة مخطط لفكرة ARCL0002 لا الوحدة ولا مدرسة حقل.",
              "Resti umani e luoghi di una comunità chiedono un permesso che questo sito non può dare. Un calco di museo non è il fossile. Dillo nella didascalia. Questa pagina è uno schema dell’idea di ARCL0002, non il modulo e non una scuola di scavo.",
              "שרידי אדם ומקומות של קהילה דורשים רשות שהאתר הזה לא יכול לתת. יציקה במוזיאון אינה המאובן. אמרו זאת בכיתוב. העמוד הזה הוא מתווה של רעיון ARCL0002, לא המודול ולא בית ספר שדה."),
             (("What must a caption say about a cast?", "Que doit dire une légende sur un moulage ?", "¿Qué debe decir un pie sobre un molde?", "ماذا يجب أن يقول التعليق عن قالب؟", "Che cosa deve dire una didascalia su un calco?", "מה כיתוב חייב לומר על יציקה?"),
              ("Can this page permit a dig?", "Cette page peut-elle permettre une fouille ?", "¿Esta página puede permitir una excavación?", "هل تستطيع هذه الصفحة الإذن بحفر؟", "Questa pagina può permettere uno scavo?", "האם העמוד הזה יכול להתיר חפירה?")),
             ("Label the cast. Do not treat this page as permission.",)),
    ],
    [("UCL Institute of Archaeology, undergraduate modules, ARCL0002", UCL_MOD),
     ("Smithsonian Human Origins — Homo sapiens", SI_HS),
     ("Smithsonian Human Origins — stone tools", SI_TOOLS),
     ("Smithsonian Human Origins — dating", SI_DATE)],
    (("What does an object lose without its layer?",
      "Que perd un objet sans sa couche ?",
      "¿Qué pierde un objeto sin su capa?",
      "ماذا يفقد الشيء بلا طبقته؟",
      "Che cosa perde un oggetto senza il suo strato?",
      "מה חפץ מאבד בלי השכבה שלו?"),
     ("Give the Smithsonian ages for Jebel Irhoud and for Oldowan tools, in words.",
      "Donnez les âges du Smithsonian pour Jebel Irhoud et pour l’Oldowayen, en mots.",
      "Da las edades del Smithsonian para Jebel Irhoud y para el Olduvayense, con palabras.",
      "اذكر أعمار Smithsonian لجبل إيغود ولأدوات أولدوان، بالكلمات.",
      "Dai le età dello Smithsonian per Jebel Irhoud e per l’Olduvaiano, a parole.",
      "תנו את גילי Smithsonian לג'בל אירהוד ולכלי אולדובן, במילים."),
     ("Why is a museum cast not the fossil?",
      "Pourquoi un moulage de musée n’est-il pas le fossile ?",
      "¿Por qué un molde de museo no es el fósil?",
      "لماذا قالب المتحف ليس الأحفورة؟",
      "Perché un calco di museo non è il fossile?",
      "למה יציקת מוזיאון אינה המאובן?")),
)

CONTEXT = C(
    "Site_Context", "ARCH 120", "arch",
    ("Find the layer", "Trouver la couche", "Hallar la capa", "إيجاد الطبقة", "Trovare lo strato", "למצוא את השכבה"),
    ("Provenience, assemblages, and why a photo is not enough.",
     "Provenance de fouille, assemblages, et pourquoi une photo ne suffit pas.",
     "Procedencia de excavación, conjuntos, y por qué una foto no basta.",
     "موضع اللقية والمجموعات ولماذا الصورة لا تكفي.",
     "Provenienza di scavo, insiemi, e perché una foto non basta.",
     "מיקום הממצא, מכלולים, ולמה תמונה לא מספיקה."),
    ("UCL’s ARCL0012 is Sites and Artefacts, 15 credits. This course is the classroom half: where a find sat, what sat with it, and how a later object can lie. It does not identify objects for sale.",
     "ARCL0012 à UCL est Sites and Artefacts, 15 crédits. Ce cours est la moitié de classe : où se trouvait une trouvaille, avec quoi, et comment un objet plus tardif peut mentir. Il n’identifie pas d’objets à vendre.",
     "ARCL0012 en UCL es Sites and Artefacts, 15 créditos. Este curso es la mitad de aula: dónde estaba un hallazgo, con qué, y cómo un objeto posterior puede mentir. No identifica objetos para la venta.",
     "ARCL0012 في UCL هو المواقع واللقى، 15 ساعة. هذا المسار نصف الصف: أين كانت اللقية ومع ماذا، وكيف يكذب شيء لاحق. لا يعرّف أشياء للبيع.",
     "ARCL0012 allo UCL è Sites and Artefacts, 15 crediti. Questo percorso è la metà d’aula: dov’era un ritrovamento, con che cosa, e come un oggetto più tardo può mentire. Non identifica oggetti in vendita.",
     "ARCL0012 ב-UCL הוא אתרים וממצאים, 15 נקודות. המסלול הזה הוא חצי הכיתה: איפה ישב ממצא, עם מה, ואיך חפץ מאוחר יכול לשקר. הוא לא מזהה חפצים למכירה."),
    "UCL ARCL0012", UCL_MOD,
    weeks(
        ("Place in the ground", "Place dans le sol", "Lugar en el suelo", "الموضع في الأرض", "Posto nel terreno", "מקום בקרקע"),
        ("An assemblage", "Un assemblage", "Un conjunto", "مجموعة لقى", "Un insieme", "מכלול"),
        ("A photo is not context", "Une photo n’est pas le contexte", "Una foto no es contexto", "الصورة ليست السياق", "Una foto non è contesto", "תמונה אינה הקשר"),
        ("Plans and sections", "Plans et coupes", "Plantas y secciones", "مساقط ومقاطع", "Piante e sezioni", "תוכניות וחתכים"),
        ("Soil is data", "Le sol est une donnée", "El suelo es un dato", "التربة بيان", "Il suolo è un dato", "הקרקע היא נתון"),
        ("A later intruder", "Un intrus plus tardif", "Un intruso posterior", "دخيل لاحق", "Un intruso più tardo", "פולש מאוחר"),
        ("Catalog numbers", "Numéros de catalogue", "Números de catálogo", "أرقام الفهرس", "Numeri di catalogo", "מספרי קטלוג"),
        ("Storage", "Le stockage", "El almacén", "التخزين", "Il deposito", "אחסון"),
        ("A shoebox lab", "Labo boîte à chaussures", "Lab de caja de zapatos", "مختبر علبة حذاء", "Lab scatola di scarpe", "מעבדת קופסת נעליים"),
        ("What fell in later", "Ce qui est tombé plus tard", "Lo que cayó después", "ما سقط لاحقاً", "Ciò che è caduto dopo", "מה נפל אחר כך"),
        ("Not for sale", "Pas à vendre", "No está en venta", "ليس للبيع", "Non è in vendita", "לא למכירה"),
        ("Write the label", "Écrire l’étiquette", "Escribir la etiqueta", "اكتب البطاقة", "Scrivi l’etichetta", "כתבו את התווית"),
        ("Compare two photos", "Comparer deux photos", "Comparar dos fotos", "قارن صورتين", "Confronta due foto", "השוו שתי תמונות"),
        ("One false friend", "Un faux ami", "Un falso amigo", "صديق كاذب", "Un falso amico", "חבר כוזב"),
        ("Stop at the classroom", "S’arrêter à la classe", "Parar en el aula", "قف عند الصف", "Fermati in classe", "לעצור בכיתה"),
    ),
    [
        unit("place",
             ("Provenience is the place", "La place de fouille", "El lugar del hallazgo", "موضع اللقية", "Il luogo del ritrovamento", "מיקום הממצא"),
             ("Provenience here means the find’s place in the ground: layer, square, and depth. A pretty photograph without that place is a story with the page number torn off. An assemblage is the group found together.",
              "Ici, la place de fouille veut dire la position dans le sol : couche, carré et profondeur. Une belle photo sans cette place est une histoire dont on a arraché le numéro de page. Un assemblage est le groupe trouvé ensemble.",
              "Aquí el lugar del hallazgo es su sitio en el suelo: capa, cuadro y profundidad. Una foto bonita sin ese sitio es una historia con el número de página arrancado. Un conjunto es el grupo hallado junto.",
              "الموضع هنا مكان اللقية في الأرض: الطبقة والمربع والعمق. صورة جميلة بلا ذلك الموضع حكاية مُزق رقم صفحتها. المجموعة ما وُجد معاً.",
              "Qui il luogo del ritrovamento è la posizione nel terreno: strato, quadrato e profondità. Una bella foto senza quel luogo è una storia con il numero di pagina strappato. Un insieme è il gruppo trovato insieme.",
              "מיקום הממצא כאן הוא מקומו בקרקע: שכבה, ריבוע ועומק. תמונה יפה בלי המקום הזה היא סיפור שנתלש ממנו מספר העמוד. מכלול הוא הקבוצה שנמצאה יחד."),
             (("What three notes locate a find in the ground?", "Quelles trois notes situent une trouvaille dans le sol ?", "¿Qué tres notas ubican un hallazgo en el suelo?", "ما الملاحظات الثلاث التي تحدد اللقية في الأرض؟", "Quali tre note collocano un ritrovamento nel terreno?", "אילו שלוש הערות ממקמות ממצא בקרקע?"),
              ("What is an assemblage?", "Qu’est-ce qu’un assemblage ?", "¿Qué es un conjunto?", "ما المجموعة؟", "Che cos’è un insieme?", "מהו מכלול?")),
             ("The place is part of the evidence.",)),
        unit("intruder",
             ("Later objects lie", "Les objets tardifs mentent", "Los objetos tardíos mienten", "الأشياء اللاحقة تكذب", "Gli oggetti tardi mentono", "חפצים מאוחרים משקרים"),
             ("A coin that fell into an older pit is not the age of the pit. Plans and section drawings show the cut. Soil color is data, not decoration. Catalog numbers tie the object to the notebook.",
              "Une pièce tombée dans une fosse plus vieille n’a pas l’âge de la fosse. Plans et coupes montrent la coupe. La couleur du sol est une donnée, pas un décor. Les numéros de catalogue lient l’objet au carnet.",
              "Una moneda caída en un pozo más viejo no tiene la edad del pozo. Plantas y secciones muestran el corte. El color del suelo es un dato, no un adorno. Los números de catálogo unen el objeto al cuaderno.",
              "قطعة نقد سقطت في حفرة أقدم ليست عمر الحفرة. المساقط والمقاطع تُظهر القطع. لون التربة بيان لا زينة. أرقام الفهرس تربط الشيء بالدفتر.",
              "Una moneta caduta in una fossa più vecchia non ha l’età della fossa. Piante e sezioni mostrano il taglio. Il colore del suolo è un dato, non un ornamento. I numeri di catalogo legano l’oggetto al taccuino.",
              "מטבע שנפל לבור עתיק יותר אינו גיל הבור. תוכניות וחתכים מראים את החתך. צבע הקרקע הוא נתון, לא קישוט. מספרי קטלוג קושרים את החפץ למחברת."),
             (("Why can a coin misdate a pit?", "Pourquoi une pièce peut-elle mal dater une fosse ?", "¿Por qué una moneda puede fechar mal un pozo?", "لماذا قد تخطئ قطعة نقد في تأريخ حفرة؟", "Perché una moneta può datare male una fossa?", "למה מטבע יכול לתארך בור לא נכון?"),
              ("What do catalog numbers connect?", "Que relient les numéros de catalogue ?", "¿Qué conectan los números de catálogo?", "ماذا تربط أرقام الفهرس؟", "Che cosa collegano i numeri di catalogo?", "מה מספרי קטלוג מחברים?")),
             ("A later object in an older cut is a known trap.",)),
        unit("lab",
             ("A shoebox, not a site", "Une boîte, pas un site", "Una caja, no un sitio", "علبة لا موقع", "Una scatola, non un sito", "קופסה, לא אתר"),
             ("Fill a shoebox with classroom objects. Draw them as an assemblage. Then add one object that “fell in later” and say how it would mislead you. This is practice. It is not an archaeological site, and nothing here is for sale or for authentication.",
              "Remplissez une boîte d’objets de classe. Dessinez-les comme un assemblage. Ajoutez ensuite un objet « tombé plus tard » et dites comment il tromperait. C’est un exercice. Ce n’est pas un site, et rien ici n’est à vendre ni à authentifier.",
              "Llena una caja con objetos de clase. Dibújalos como un conjunto. Luego añade un objeto que «cayó después» y di cómo engañaría. Es práctica. No es un sitio, y nada aquí está en venta ni para autenticar.",
              "املأ علبة بأغراض الصف. ارسمها كمجموعة. ثم أضف شيئاً «سقط لاحقاً» وقل كيف يضلّل. هذا تمرين. ليس موقعاً، ولا شيء هنا للبيع أو للتوثيق التجاري.",
              "Riempi una scatola con oggetti di classe. Disegnali come un insieme. Poi aggiungi un oggetto «caduto dopo» e di’ come ingannerebbe. È un esercizio. Non è un sito, e niente qui è in vendita o da autenticare.",
              "מלאו קופסה בחפצי כיתה. שרטטו אותם כמכלול. אחר כך הוסיפו חפץ «שנפל אחר כך» ואמרו איך הוא היה מטעה. זה תרגול. זה לא אתר, ושום דבר כאן לא למכירה ולא לאימות מסחרי."),
             (("What is the shoebox standing in for?", "Que remplace la boîte à chaussures ?", "¿Qué sustituye la caja de zapatos?", "عمّ تنوب علبة الحذاء؟", "Che cosa sostituisce la scatola di scarpe?", "מה קופסת הנעליים מחליפה?"),
              ("What will this course refuse to do with an object?", "Que refusera ce cours de faire avec un objet ?", "¿Qué se negará este curso a hacer con un objeto?", "ماذا يرفض هذا المسار أن يفعل بشيء؟", "Che cosa questo percorso rifiuta di fare con un oggetto?", "מה המסלול הזה מסרב לעשות עם חפץ?")),
             ("Practice on a shoebox. Do not turn a real place into a classroom dig.",)),
        unit("stop",
             ("Stop at the label", "S’arrêter à l’étiquette", "Parar en la etiqueta", "قف عند البطاقة", "Fermati all’etichetta", "לעצור בתווית"),
             ("Write a label a museum could trust: what it is, where it sat, what was with it, and what you do not know. If the place is missing, the label says the place is missing. ARCL0012’s full module is larger than this page.",
              "Écrivez une étiquette qu’un musée pourrait croire : ce que c’est, où c’était, avec quoi, et ce que vous ignorez. Si la place manque, l’étiquette dit que la place manque. Le module ARCL0012 entier est plus grand que cette page.",
              "Escribe una etiqueta que un museo pudiera creer: qué es, dónde estaba, con qué, y qué no sabes. Si falta el lugar, la etiqueta dice que falta el lugar. El módulo ARCL0012 completo es más grande que esta página.",
              "اكتب بطاقة يثق بها متحف: ما هو وأين كان ومع ماذا وما لا تعرفه. إن غاب الموضع قالت البطاقة إن الموضع غائب. وحدة ARCL0012 الكاملة أكبر من هذه الصفحة.",
              "Scrivi un’etichetta cui un museo potrebbe credere: che cos’è, dov’era, con che cosa, e che cosa non sai. Se il luogo manca, l’etichetta dice che il luogo manca. Il modulo ARCL0012 intero è più grande di questa pagina.",
              "כתבו תווית שמוזיאון יכול לסמוך עליה: מה זה, איפה ישב, עם מה, ומה אינכם יודעים. אם המקום חסר, התווית אומרת שהמקום חסר. המודול המלא ARCL0012 גדול מהעמוד הזה."),
             (("What does the label say when the place is unknown?", "Que dit l’étiquette si la place est inconnue ?", "¿Qué dice la etiqueta si el lugar es desconocido?", "ماذا تقول البطاقة إذا جهل الموضع؟", "Che cosa dice l’etichetta se il luogo è ignoto?", "מה אומרת התווית כשהמקום לא ידוע?"),
              ("Name the UCL module this page is modeled on.", "Nommez le module UCL dont cette page s’inspire.", "Nombra el módulo de UCL en que se inspira esta página.", "سمّ وحدة UCL التي بُنيت عليها الصفحة.", "Nomina il modulo UCL su cui è modellata questa pagina.", "ציינו את מודול UCL שהעמוד מעוצב לפיו.")),
             ("An honest gap on the label is better than a guessed place.",)),
    ],
    [("UCL undergraduate modules, ARCL0012 Sites and Artefacts", UCL_MOD),
     ("Smithsonian Human Origins — dating", SI_DATE)],
    (("What is provenience in this course?",
      "Qu’est-ce que la place de fouille dans ce cours ?",
      "¿Qué es el lugar del hallazgo en este curso?",
      "ما موضع اللقية في هذا المسار؟",
      "Che cos’è il luogo del ritrovamento in questo percorso?",
      "מהו מיקום הממצא במסלול הזה?"),
     ("How can a later coin misdate an older pit?",
      "Comment une pièce plus tardive peut-elle mal dater une fosse plus vieille ?",
      "¿Cómo una moneda posterior puede fechar mal un pozo más viejo?",
      "كيف تخطئ قطعة نقد لاحقة في تأريخ حفرة أقدم؟",
      "Come una moneta più tarda può datare male una fossa più vecchia?",
      "איך מטבע מאוחר יכול לתארך לא נכון בור עתיק יותר?"),
     ("What will the page not do for an object someone wants to sell?",
      "Que ne fera pas la page pour un objet à vendre ?",
      "¿Qué no hará la página con un objeto que alguien quiere vender?",
      "ماذا لن تفعله الصفحة لشيء يريد أحد بيعه؟",
      "Che cosa la pagina non farà per un oggetto che qualcuno vuole vendere?",
      "מה העמוד לא יעשה לחפץ שמישהו רוצה למכור?")),
)

METHODS = C(
    "Field_Methods", "ARCH 210", "arch",
    ("Record a site", "Noter un site", "Registrar un sitio", "تسجيل موقع", "Registrare un sito", "לתעד אתר"),
    ("Survey, records, and why this page will not open ground.",
     "Repérage, archives, et pourquoi cette page n’ouvrira pas le sol.",
     "Reconocimiento, registros, y por qué esta página no abrirá el suelo.",
     "مسح وسجلات ولماذا لن تفتح هذه الصفحة الأرض.",
     "Ricognizione, registri, e perché questa pagina non aprirà il terreno.",
     "סקר, רשומות, ולמה העמוד הזה לא יפתח קרקע."),
    ("UCL’s ARCL0011 Field Methods is a 15-credit module. UCL lists it as not running in 2026–27. Its published scope includes survey, recording, dating, sampling, and a supervised field course. This page teaches the reasons for those records. It does not tell anyone how to excavate a real site.",
     "ARCL0011 Field Methods à UCL est un module de 15 crédits. UCL indique qu’il ne tourne pas en 2026–2027. Son périmètre publié inclut le repérage, l’enregistrement, la datation, l’échantillonnage et un stage encadré. Cette page enseigne pourquoi ces archives existent. Elle ne dit à personne comment fouiller un vrai site.",
     "ARCL0011 Field Methods en UCL es un módulo de 15 créditos. UCL lo lista como no impartido en 2026–27. Su alcance publicado incluye reconocimiento, registro, datación, muestreo y un curso de campo supervisado. Esta página enseña por qué existen esos registros. No dice a nadie cómo excavar un sitio real.",
     "ARCL0011 طرق الحقل في UCL وحدة من 15 ساعة. تذكر UCL أنها لا تُدرَّس في 2026–2027. يشمل نطاقها المنشور المسح والتسجيل والتأريخ وأخذ العينات ودورة حقل بإشراف. تعلّم هذه الصفحة لماذا توجد تلك السجلات. لا تخبر أحداً كيف يحفر موقعاً حقيقياً.",
     "ARCL0011 Field Methods allo UCL è un modulo da 15 crediti. Lo UCL lo indica come non attivo nel 2026–27. L’ambito pubblicato include ricognizione, registrazione, datazione, campionamento e un corso di campo sorvegliato. Questa pagina insegna perché esistono quei registri. Non dice a nessuno come scavare un sito vero.",
     "ARCL0011 שיטות שדה ב-UCL הוא מודול של 15 נקודות. UCL מציינת שהוא לא רץ ב-2026–2027. ההיקף שפורסם כולל סקר, תיעוד, תיארוך, דגימה וקורס שדה מודרך. העמוד מלמד למה הרשומות האלה קיימות. הוא לא אומר לאיש איך לחפור אתר אמיתי."),
    "UCL ARCL0011", UCL_FIELD,
    weeks(
        ("Survey before a dig", "Repérer avant de creuser", "Reconocer antes de cavar", "امسح قبل الحفر", "Ricognizione prima dello scavo", "סקר לפני חפירה"),
        ("A context sheet", "Une fiche de contexte", "Una ficha de contexto", "بطاقة سياق", "Una scheda di contesto", "טופס הקשר"),
        ("Photos with a scale", "Photos à l’échelle", "Fotos con escala", "صور بمقياس", "Foto in scala", "תמונות עם קנה מידה"),
        ("Samples have a reason", "Les échantillons ont une raison", "Las muestras tienen una razón", "للعينات سبب", "I campioni hanno una ragione", "לדגימות יש סיבה"),
        ("Dating after the record", "Dater après l’archive", "Fechar después del registro", "التأريخ بعد السجل", "Datare dopo il registro", "תיארוך אחרי הרשומה"),
        ("What excavation costs", "Ce que coûte une fouille", "Lo que cuesta una excavación", "كلفة الحفر", "Quanto costa uno scavo", "מה חפירה עולה"),
        ("Do not open ground", "Ne pas ouvrir le sol", "No abrir el suelo", "لا تفتح الأرض", "Non aprire il terreno", "אל תפתחו קרקע"),
        ("A sandbox is practice", "Un bac à sable est un exercice", "Un arenero es práctica", "صندوق رمل تمرين", "Una sabbiera è un esercizio", "ארגז חול הוא תרגול"),
        ("Labels that last", "Des étiquettes qui durent", "Etiquetas que duran", "بطاقات تدوم", "Etichette che durano", "תוויות שמחזיקות"),
        ("Archive and care", "Archive et soin", "Archivo y cuidado", "الأرشيف والعناية", "Archivio e cura", "ארכיון וטיפול"),
        ("Publication", "La publication", "La publicación", "النشر", "La pubblicazione", "פרסום"),
        ("What a field school adds", "Ce qu’ajoute une école de fouille", "Lo que añade una escuela de campo", "ما تضيفه مدرسة الحقل", "Che cosa aggiunge una scuola di scavo", "מה בית ספר שדה מוסיף"),
        ("Write the refusal", "Écrire le refus", "Escribir la negativa", "اكتب الرفض", "Scrivi il rifiuto", "כתבו את הסירוב"),
        ("Read ARCL0011", "Lire ARCL0011", "Leer ARCL0011", "اقرأ ARCL0011", "Leggi ARCL0011", "קראו ARCL0011"),
        ("Not this year’s UCL class", "Pas le cours UCL de cette année", "No es la clase UCL de este año", "ليس صف UCL لهذه السنة", "Non è la classe UCL di quest’anno", "לא השיעור של UCL השנה"),
    ),
    [
        unit("survey",
             ("Find before you dig, and then do not dig", "Repérer avant de creuser, puis ne pas creuser", "Hallar antes de cavar, y luego no cavar", "جد قبل الحفر ثم لا تحفر", "Trova prima di scavare, e poi non scavare", "מצאו לפני שחופרים, ואז אל תחפרו"),
             ("Survey is how archaeologists look for sites before anyone opens the ground. This page stops there. Opening a real site needs a permit and a supervisor. Practicing a context sheet in a school sandbox is allowed only because the sandbox is not a site.",
              "Le repérage est la façon de chercher des sites avant d’ouvrir le sol. Cette page s’arrête là. Ouvrir un vrai site exige un permis et un encadrant. Remplir une fiche dans un bac à sable d’école n’est permis que parce que le bac n’est pas un site.",
              "El reconocimiento es cómo se buscan sitios antes de abrir el suelo. Esta página se detiene ahí. Abrir un sitio real exige permiso y un supervisor. Practicar una ficha en un arenero escolar solo vale porque el arenero no es un sitio.",
              "المسح هو كيف يُبحث عن المواقع قبل فتح الأرض. تتوقف هذه الصفحة هناك. فتح موقع حقيقي يحتاج إذناً ومشرفاً. تدريب بطاقة السياق في صندوق رمل مدرسي جائز فقط لأن الصندوق ليس موقعاً.",
              "La ricognizione è come si cercano i siti prima di aprire il terreno. Questa pagina si ferma lì. Aprire un sito vero richiede un permesso e un supervisore. Provare una scheda in una sabbiera di scuola è lecito solo perché la sabbiera non è un sito.",
              "סקר הוא איך מחפשים אתרים לפני שפותחים קרקע. העמוד נעצר שם. פתיחת אתר אמיתי דורשת היתר ומדריך. תרגול טופס הקשר בארגז חול של בית ספר מותר רק כי ארגז החול אינו אתר."),
             (("Why does survey come before excavation?", "Pourquoi le repérage vient-il avant la fouille ?", "¿Por qué el reconocimiento va antes de la excavación?", "لماذا يسبق المسح الحفر؟", "Perché la ricognizione viene prima dello scavo?", "למה הסקר בא לפני החפירה?"),
              ("Why is a sandbox acceptable and a mapped site not?", "Pourquoi un bac à sable est-il acceptable et un site de la carte non ?", "¿Por qué un arenero vale y un sitio del mapa no?", "لماذا يجوز صندوق الرمل ولا يجوز موقع على الخريطة؟", "Perché una sabbiera va bene e un sito della mappa no?", "למה ארגז חול מתקבל ואתר על המפה לא?")),
             ("Look and record. Do not open the ground.",)),
        unit("sheet",
             ("What a context sheet is for", "À quoi sert une fiche de contexte", "Para qué es una ficha de contexto", "فيم بطاقة السياق", "A che cosa serve una scheda di contesto", "למה טופס הקשר"),
             ("A context sheet names the unit, the relationships (above, below, cut by), the finds, the samples, and the photos. The point of the sheet is that a later worker can rebuild the layer without being there. Photos need a scale.",
              "Une fiche nomme l’unité, les relations (au-dessus, au-dessous, coupée par), les trouvailles, les échantillons et les photos. Le but : qu’un travailleur plus tard reconstruise la couche sans y être. Les photos ont une échelle.",
              "Una ficha nombra la unidad, las relaciones (encima, debajo, cortada por), los hallazgos, las muestras y las fotos. El fin: que alguien después reconstruya la capa sin estar allí. Las fotos llevan escala.",
              "تسمّي البطاقة الوحدة والعلاقات (فوق وتحت ومقطوعة بـ) واللقى والعينات والصور. الغاية أن يعيد لاحق بناء الطبقة دون أن يكون هناك. الصور تحتاج مقياساً.",
              "Una scheda nomina l’unità, le relazioni (sopra, sotto, tagliata da), i ritrovamenti, i campioni e le foto. Lo scopo: che qualcuno dopo ricostruisca lo strato senza esserci. Le foto hanno una scala.",
              "הטופס מציין את היחידה, את היחסים (מעל, מתחת, נחתך על ידי), את הממצאים, את הדגימות ואת התמונות. המטרה: שעובד מאוחר יותר ישחזר את השכבה בלי להיות שם. לתמונות צריך קנה מידה."),
             (("Name three relationships a sheet should record.", "Nommez trois relations qu’une fiche doit noter.", "Nombra tres relaciones que una ficha debe anotar.", "سمّ ثلاث علاقات يجب أن تسجلها البطاقة.", "Nomina tre relazioni che una scheda deve annotare.", "ציינו שלושה יחסים שטופס צריך לרשום."),
              ("Why does a photo need a scale?", "Pourquoi une photo a-t-elle besoin d’une échelle ?", "¿Por qué una foto necesita una escala?", "لماذا تحتاج الصورة إلى مقياس؟", "Perché una foto ha bisogno di una scala?", "למה לתמונה צריך קנה מידה?")),
             ("The sheet is how the layer survives the season.",)),
        unit("after",
             ("After the season", "Après la saison", "Después de la temporada", "بعد الموسم", "Dopo la stagione", "אחרי העונה"),
             ("UCL’s field-methods description includes what happens after the dig: analysis, archiving, conservation, and publication. A find without a stored record is a find half lost. This page will not coach sampling of a real site.",
              "La description UCL inclut l’après-fouille : analyse, archivage, conservation et publication. Une trouvaille sans archive stockée est à moitié perdue. Cette page n’entraîne pas au prélèvement sur un vrai site.",
              "La descripción de UCL incluye lo posterior a la excavación: análisis, archivo, conservación y publicación. Un hallazgo sin registro guardado está medio perdido. Esta página no entrena el muestreo de un sitio real.",
              "يشمل وصف UCL ما بعد الحفر: التحليل والأرشفة والحفظ والنشر. لقية بلا سجل محفوظ نصف ضائعة. لن تدرّب هذه الصفحة على أخذ عينات من موقع حقيقي.",
              "La descrizione dello UCL include il dopo scavo: analisi, archivio, conservazione e pubblicazione. Un ritrovamento senza un registro conservato è mezzo perduto. Questa pagina non allena il campionamento di un sito vero.",
              "התיאור של UCL כולל את מה שאחרי החפירה: ניתוח, ארכיון, שימור ופרסום. ממצא בלי רשומה שמורה הוא ממצא חצי אבוד. העמוד לא מאמן דגימה של אתר אמיתי."),
             (("What four after-season jobs does the UCL description name?", "Quels quatre travaux d’après-saison la description UCL nomme-t-elle ?", "¿Qué cuatro trabajos posteriores nombra la descripción de UCL?", "ما أعمال ما بعد الموسم الأربعة التي يذكرها وصف UCL؟", "Quali quattro lavori dopo la stagione nomina la descrizione dello UCL?", "אילו ארבע עבודות אחרי העונה התיאור של UCL מציין?"),
              ("Why is an unstored find only half a find?", "Pourquoi une trouvaille non archivée n’est-elle qu’à moitié une trouvaille ?", "¿Por qué un hallazgo sin archivo es solo medio hallazgo?", "لماذا اللقية غير المؤرشفة نصف لقية؟", "Perché un ritrovamento non archiviato è solo mezzo ritrovamento?", "למה ממצא שלא נשמר הוא רק חצי ממצא?")),
             ("The record outlives the season. The hole should not.",)),
        unit("refusal",
             ("Write what you will not do", "Écrire ce que vous ne ferez pas", "Escribe lo que no harás", "اكتب ما لن تفعله", "Scrivi che cosa non farai", "כתבו מה לא תעשו"),
             ("The closing note says: I will not open ground, I will not buy artifacts, and I will not treat this page as UCL’s 2026–27 class, because UCL says that module is not running. A field school is the missing piece, and it is not written here.",
              "La note finale dit : je n’ouvrirai pas le sol, je n’achèterai pas d’artefacts, et je ne prendrai pas cette page pour le cours UCL 2026–2027, car UCL dit que le module ne tourne pas. L’école de fouille est la pièce manquante, et elle n’est pas écrite ici.",
              "La nota final dice: no abriré el suelo, no compraré artefactos y no tomaré esta página por la clase UCL de 2026–27, porque UCL dice que el módulo no se imparte. La escuela de campo es la pieza que falta, y no está escrita aquí.",
              "تقول الملاحظة الختامية: لن أفتح الأرض ولن أشتري آثاراً ولن أعدّ هذه الصفحة صف UCL لعام 2026–2027، لأن UCL تقول إن الوحدة لا تُدرَّس. مدرسة الحقل هي القطعة الناقصة ولم تُكتب هنا.",
              "La nota finale dice: non aprirò il terreno, non comprerò manufatti e non prenderò questa pagina per la classe UCL 2026–27, perché lo UCL dice che il modulo non è attivo. La scuola di scavo è il pezzo mancante, e non è scritta qui.",
              "ההערה הסוגרת אומרת: לא אפתח קרקע, לא אקנה ממצאים, ולא אתייחס לעמוד הזה כאל שיעור UCL של 2026–2027, כי UCL אומרת שהמודול לא רץ. בית ספר שדה הוא החלק החסר, והוא לא נכתב כאן."),
             (("What three refusals close the course?", "Quels trois refus ferment le cours ?", "¿Qué tres negativas cierran el curso?", "ما الرفضات الثلاث التي تختم المسار؟", "Quali tre rifiuti chiudono il percorso?", "אילו שלושה סירובים סוגרים את המסלול?"),
              ("Is ARCL0011 running at UCL in 2026–27?", "ARCL0011 tourne-t-il à UCL en 2026–2027 ?", "¿Se imparte ARCL0011 en UCL en 2026–27?", "هل يُدرَّس ARCL0011 في UCL في 2026–2027؟", "ARCL0011 è attivo allo UCL nel 2026–27?", "האם ARCL0011 רץ ב-UCL ב-2026–2027?")),
             ("The refusal is part of the record.",)),
    ],
    [("UCL module catalogue, Field Methods ARCL0011", UCL_FIELD),
     ("UCL undergraduate module list", UCL_MOD),
     ("Smithsonian Human Origins — dating", SI_DATE)],
    (("Why will this page not teach you to open a real site?",
      "Pourquoi cette page ne vous apprendra-t-elle pas à ouvrir un vrai site ?",
      "¿Por qué esta página no te enseñará a abrir un sitio real?",
      "لماذا لن تعلّمك هذه الصفحة فتح موقع حقيقي؟",
      "Perché questa pagina non ti insegnerà ad aprire un sito vero?",
      "למה העמוד הזה לא ילמד אותך לפתוח אתר אמיתי?"),
     ("What does a context sheet have to let a later worker do?",
      "Que doit permettre une fiche de contexte à un travailleur plus tard ?",
      "¿Qué debe permitir una ficha de contexto a quien venga después?",
      "ماذا يجب أن تمكّن بطاقة السياق اللاحق من فعله؟",
      "Che cosa deve permettere una scheda di contesto a chi viene dopo?",
      "מה טופס הקשר חייב לאפשר לעובד מאוחר יותר?"),
     ("What does UCL say about ARCL0011 in 2026–27?",
      "Que dit UCL d’ARCL0011 en 2026–2027 ?",
      "¿Qué dice UCL de ARCL0011 en 2026–27?",
      "ماذا تقول UCL عن ARCL0011 في 2026–2027؟",
      "Che cosa dice lo UCL di ARCL0011 nel 2026–27?",
      "מה UCL אומרת על ARCL0011 ב-2026–2027?")),
)

LIVE = [EARTH, STRAT, FIELD, ARCH, CONTEXT, METHODS]
import edu_later
LATER = edu_later.LATER
ALL = LIVE + LATER

SOON = [
    ("earth", "GEOL 220",
     ("Geophysics", "Géophysique", "Geofísica", "جيوفيزياء", "Geofisica", "גיאופיזיקה"),
     ("Interior of the Earth. Modeled on MIT 12.002. Not written yet.",
      "L’intérieur de la Terre. Calqué sur MIT 12.002. Pas encore écrit.",
      "El interior de la Tierra. Modelado en MIT 12.002. Aún no escrito.",
      "باطن الأرض. على غرار MIT 12.002. لم يُكتب بعد.",
      "L’interno della Terra. Modellato su MIT 12.002. Non ancora scritto.",
      "פנים כדור הארץ. לפי MIT 12.002. עדיין לא נכתב.")),
    ("earth", "GEOL 310",
     ("Sediments in the field", "Sédiments sur le terrain", "Sedimentos en el campo", "رواسب في الحقل", "Sedimenti sul campo", "משקעים בשדה"),
     ("A field sediment course. Modeled on MIT 12.110. Not written yet.",
      "Un cours de sédiments sur le terrain. Calqué sur MIT 12.110. Pas encore écrit.",
      "Un curso de sedimentos en el campo. Modelado en MIT 12.110. Aún no escrito.",
      "مقرر رواسب حقلي. على غرار MIT 12.110. لم يُكتب بعد.",
      "Un corso di sedimenti sul campo. Modellato su MIT 12.110. Non ancora scritto.",
      "קורס משקעים בשדה. לפי MIT 12.110. עדיין לא נכתב.")),
    ("earth", "GEOL 410",
     ("Field camp", "Camp de terrain", "Campamento de campo", "معسكر الحقل", "Campo estivo", "מחנה שדה"),
     ("A supervised traverse. Modeled on MIT 12.115. Not written yet.",
      "Une traversée encadrée. Calquée sur MIT 12.115. Pas encore écrite.",
      "Un recorrido supervisado. Modelado en MIT 12.115. Aún no escrito.",
      "اجتياز بإشراف. على غرار MIT 12.115. لم يُكتب بعد.",
      "Un percorso sorvegliato. Modellato su MIT 12.115. Non ancora scritto.",
      "חתך מודרך. לפי MIT 12.115. עדיין לא נכתב.")),
    ("arch", "ARCH 220",
     ("Animal bones", "Os d’animaux", "Huesos de animales", "عظام الحيوانات", "Ossa animali", "עצמות בעלי חיים"),
     ("Zooarchaeology. Modeled on UCL ARCL0022. Not written yet.",
      "Zooarchéologie. Calquée sur UCL ARCL0022. Pas encore écrite.",
      "Zooarqueología. Modelada en UCL ARCL0022. Aún no escrita.",
      "آثار عظام الحيوانات. على غرار UCL ARCL0022. لم تُكتب بعد.",
      "Zooarcheologia. Modellata su UCL ARCL0022. Non ancora scritta.",
      "Zooארכאולוגיה. לפי UCL ARCL0022. עדיין לא נכתב.")),
    ("arch", "ARCH 310",
     ("Soils and sites", "Sols et sites", "Suelos y sitios", "ترب ومواقع", "Suoli e siti", "קרקעות ואתרים"),
     ("Geoarchaeology. Modeled on UCL ARCL0023. Not written yet.",
      "Géoarchéologie. Calquée sur UCL ARCL0023. Pas encore écrite.",
      "Geoarqueología. Modelada en UCL ARCL0023. Aún no escrita.",
      "الجيوأركيولوجيا. على غرار UCL ARCL0023. لم تُكتب بعد.",
      "Geoarcheologia. Modellata su UCL ARCL0023. Non ancora scritta.",
      "גיאוארכאולוגיה. לפי UCL ARCL0023. עדיין לא נכתב.")),
    ("arch", "ARCH 410",
     ("A long essay", "Un long essai", "Un ensayo largo", "مقال طويل", "Un saggio lungo", "חיבור ארוך"),
     ("A dissertation-style close. Modeled on UCL ARCL0047. Not written yet.",
      "Une clôture façon mémoire. Calquée sur UCL ARCL0047. Pas encore écrite.",
      "Un cierre al estilo de una tesina. Modelado en UCL ARCL0047. Aún no escrito.",
      "خاتمة بأسلوب رسالة. على غرار UCL ARCL0047. لم تُكتب بعد.",
      "Una chiusura in stile tesi. Modellata su UCL ARCL0047. Non ancora scritta.",
      "סיום בסגנון עבודת גמר. לפי UCL ARCL0047. עדיין לא נכתב.")),
]

def e(s):
    return html.escape(s, quote=True)

def hero(lang, r, kicker, h1, lead):
    # The continent-cartoon film is retired. This still is the NASA Blue Marble.
    alt = T(lang,
            "The Blue Marble, Earth photographed from Apollo 17 on 7 December 1972.",
            "La Bille bleue, la Terre photographiée depuis Apollo 17 le 7 décembre 1972.",
            "La canica azul, la Tierra fotografiada desde el Apolo 17 el 7 de diciembre de 1972.",
            "الرخامة الزرقاء، الأرض مصوّرة من أبولو 17 في 7 ديسمبر 1972.",
            "La biglia blu, la Terra fotografata dall’Apollo 17 il 7 dicembre 1972.",
            "הגולה הכחולה, כדור הארץ מצולם מאפולו 17 ב-7 בדצמבר 1972.")
    credit = T(lang,
               "Photograph behind the title: NASA, Apollo 17, the Blue Marble, 7 December 1972. Public domain. Not a cartoon globe.",
               "Photo derrière le titre : NASA, Apollo 17, la Bille bleue, 7 décembre 1972. Domaine public. Pas un globe dessiné.",
               "Foto detrás del título: NASA, Apolo 17, la canica azul, 7 de diciembre de 1972. Dominio público. No es un globo dibujado.",
               "الصورة خلف العنوان: ناسا، أبولو 17، الرخامة الزرقاء، 7 ديسمبر 1972. ملكية عامة. ليست كرة مرسومة.",
               "Foto dietro il titolo: NASA, Apollo 17, la biglia blu, 7 dicembre 1972. Dominio pubblico. Non è un globo disegnato.",
               "התצלום מאחורי הכותרת: נאס״א, אפולו 17, הגולה הכחולה, 7 בדצמבר 1972. נחלת הכלל. לא גלובוס מצויר.")
    return (
        f'<section class="sm-hero"><picture>'
        f'<img src="{r}assets/deep/photo-earth.webp" width="1400" height="1400" alt="{e(alt)}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{e(kicker)}</p><h1>{e(h1)}</h1><p class="sm-lead">{e(lead)}</p></div></section>'
        f'<p class="sm-vcredit edu-wrap">{credit}</p>'
    )

def disc(lang):
    return T(lang,
             "Free self-study outline by Before Saving Planets. It is not the university course it is modeled on, it carries no credit, and that university does not endorse this page. Created by the Founder and SI.",
             "Plan d’étude libre de Before Saving Planets. Ce n’est pas le cours universitaire dont il s’inspire, il ne donne aucun crédit, et cette université ne cautionne pas cette page. Created by the Founder and SI.",
             "Plan de estudio gratuito de Before Saving Planets. No es el curso universitario en que se inspira, no da crédito, y esa universidad no respalda esta página. Created by the Founder and SI.",
             "مخطط دراسة مجاني من Before Saving Planets. ليس المقرر الجامعي الذي بُني على غراره، ولا يمنح ساعات، وتلك الجامعة لا تعتمد هذه الصفحة. Created by the Founder and SI.",
             "Schema di studio gratuito di Before Saving Planets. Non è il corso universitario su cui è modellato, non dà crediti, e quell’università non avalla questa pagina. Created by the Founder and SI.",
             "מתווה לימוד חינמי של Before Saving Planets. זה אינו קורס האוניברסיטה שהוא מעוצב לפיו, אין בו נקודות זכות, והאוניברסיטה הזו לא מאשרת את העמוד. Created by the Founder and SI.")

def sheet(lang, course):
    qs = "".join(f"<li>{e(q)}</li>" for q in (T(lang, *q) for q in course["sheet_q"]))
    h = T(lang, "Teacher sheet", "Fiche enseignant", "Ficha docente", "ورقة المعلم", "Scheda docente", "דף מורה")
    btn = T(lang, "Print this sheet", "Imprimer cette fiche", "Imprimir esta ficha", "اطبع هذه الورقة", "Stampa questa scheda", "הדפיסו דף זה")
    std_h = T(lang, "Standards", "Normes", "Estándares", "المعايير", "Standard", "תקנים")
    note = T(lang,
             "NGSS text is the official English performance expectation. MS-ESS1-4 says 4.6 billion years. This site uses the USGS age, 4.54 billion years. Keep both numbers visible. C3 text is the College, Career, and Civic Life indicator, in English.",
             "Le texte NGSS est l’attente officielle en anglais. MS-ESS1-4 dit 4,6 milliards d’années. Ce site utilise l’âge USGS, 4,54 milliards d’années. Gardez les deux nombres visibles. Le texte C3 est l’indicateur du cadre College, Career, and Civic Life, en anglais.",
             "El texto NGSS es la expectativa oficial en inglés. MS-ESS1-4 dice 4.6 mil millones de años. Este sitio usa la edad USGS, 4.540 millones de años. Deja visibles los dos números. El texto C3 es el indicador del marco College, Career, and Civic Life, en inglés.",
             "نص NGSS هو التوقع الرسمي بالإنجليزية. يقول MS-ESS1-4 إن العمر 4.6 مليار سنة. يستخدم هذا الموقع عمر USGS، 4.54 مليار سنة. أبقوا الرقمين ظاهرين. نص C3 هو مؤشر إطار College, Career, and Civic Life بالإنجليزية.",
             "Il testo NGSS è l’aspettativa ufficiale in inglese. MS-ESS1-4 dice 4,6 miliardi di anni. Questo sito usa l’età USGS, 4,54 miliardi di anni. Tieni visibili entrambi i numeri. Il testo C3 è l’indicatore del quadro College, Career, and Civic Life, in inglese.",
             "טקסט NGSS הוא ציפיית הביצוע הרשמית באנגלית. MS-ESS1-4 אומר 4.6 מיליארד שנה. האתר משתמש בגיל USGS, 4.54 מיליארד. השאירו את שני המספרים גלויים. טקסט C3 הוא המדד של מסגרת College, Career, and Civic Life, באנגלית.")
    stds = earth_stds() if course["track"] == "earth" else arch_stds()
    items = "".join(
        f'<li><a href="{s["url"]}">{e(s["code"])}</a> <span lang="en">{e(s["text"])}</span></li>'
        for s in stds
    )
    src_h = T(lang, "Sources on this sheet", "Sources de cette fiche", "Fuentes de esta ficha", "مصادر هذه الورقة", "Fonti di questa scheda", "מקורות בדף זה")
    srcs = "".join(f'<li><a href="{url}">{e(name)}</a></li>' for name, url in course["sources"])
    return (
        f'<section class="teacher-sheet" id="sheet"><h2>{e(h)}</h2><ol>{qs}</ol>'
        f'<h3>{e(std_h)}</h3><p class="std-note">{e(note)}</p><ul>{items}</ul>'
        f'<h3>{e(src_h)}</h3><ul>{srcs}</ul>'
        f'<p><button type="button" class="print-sheet">{e(btn)}</button> '
        f'<a href="Teachers.html">{e(T(lang, "All teacher sheets", "Toutes les fiches", "Todas las fichas", "كل الأوراق", "Tutte le schede", "כל דפי המורים"))}</a></p>'
        f'<p>{e(T(lang, "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI."))}</p>'
        f'</section>'
    )

def course_main(lang, r, course):
    kicker = T(lang, "Education · Courses", "Éducation · Cours", "Educación · Cursos", "التعليم · الدورات", "Istruzione · Corsi", "חינוך · קורסים")
    title = T(lang, *course["title"])
    body = hero(lang, r, kicker, title, T(lang, *course["blurb"]))
    wh = T(lang, "Week", "Semaine", "Semana", "أسبوع", "Settimana", "שבוע")
    dh = T(lang, "Dates", "Dates", "Fechas", "التواريخ", "Date", "תאריכים")
    th = T(lang, "Focus", "Foyer", "Foco", "المحور", "Fuoco", "מוקד")
    rows = "".join(
        f'<tr><td>{i+1}</td><td>{e(w["date"])}</td><td>{e(T(lang, *w["title"]))}</td></tr>'
        for i, w in enumerate(course["weeks"])
    )
    units = []
    for u in course["units"]:
        qs = "".join(f"<li>{e(T(lang, *q))}</li>" for q in u["questions"])
        units.append(
            f'<section class="edu-unit" id="{u["id"]}"><h3>{e(T(lang, *u["title"]))}</h3>'
            f'<p>{e(T(lang, *u["body"]))}</p><ol>{qs}</ol></section>'
        )
    srcs = "".join(f'<li><a href="{url}">{e(name)}</a></li>' for name, url in course["sources"])
    sched = T(lang, "Suggested 15-week calendar", "Calendrier suggéré de 15 semaines", "Calendario sugerido de 15 semanas", "تقويم مقترح لخمسة عشر أسبوعاً", "Calendario suggerito di 15 settimane", "לוח מוצע של 15 שבועות")
    about_h = T(lang, "About this course", "À propos de ce cours", "Sobre este curso", "عن هذا المسار", "Su questo percorso", "על המסלול הזה")
    model = T(lang, "Modeled on", "Calqué sur", "Modelado en", "على غرار", "Modellato su", "מעוצב לפי")
    src_h = T(lang, "Sources", "Sources", "Fuentes", "المصادر", "Fonti", "מקורות")
    term = T(lang,
              "Dates are a suggested self-study term starting 8 September 2026. They are not a university calendar.",
              "Les dates sont un trimestre d’étude libre suggéré, à partir du 8 septembre 2026. Ce n’est pas un calendrier universitaire.",
              "Las fechas son un trimestre de estudio libre sugerido, desde el 8 de septiembre de 2026. No son un calendario universitario.",
              "التواريخ فصل دراسة حرة مقترح يبدأ في 8 سبتمبر 2026. ليست تقويم جامعة.",
              "Le date sono un trimestre di studio libero suggerito, dal 8 settembre 2026. Non sono un calendario universitario.",
              "התאריכים הם סמסטר לימוד עצמי מוצע שמתחיל ב-8 בספטמבר 2026. זה לא לוח אוניברסיטה.")
    jump = [
        ("about", about_h),
        ("calendar", sched),
        ("units", T(lang, "Units", "Unités", "Unidades", "الوحدات", "Unità", "יחידות")),
        ("sheet", T(lang, "Teacher sheet", "Fiche enseignant", "Ficha docente", "ورقة المعلم", "Scheda docente", "דף מורה")),
        ("sources", src_h),
    ]
    bar = "".join(f'<a href="#{i}">{e(lab)}</a>' for i, lab in jump)
    return body + (
        f'<div class="sm-wrap crs"><nav class="edu-jump" aria-label="{e(T(lang, "On this course", "Dans ce cours", "En este curso", "في هذا المسار", "In questo percorso", "במסלול הזה"))}">{bar}</nav>'
        f'<p class="edu-note">{e(disc(lang))}</p>'
        f'<h2 id="about">{e(about_h)}</h2><p>{e(T(lang, *course["about"]))}</p>'
        f'<p>{e(model)} <a href="{course["model_url"]}">{e(course["model_name"])}</a>. <span class="edu-code">{e(course["code"])}</span></p>'
        f'<h2 id="calendar">{e(sched)}</h2><p>{e(term)}</p>'
        f'<table class="edu-weeks"><thead><tr><th>{e(wh)}</th><th>{e(dh)}</th><th>{e(th)}</th></tr></thead><tbody>{rows}</tbody></table>'
        f'<div id="units">' + "".join(units) + "</div>" + sheet(lang, course) +
        f'<h2 id="sources">{e(src_h)} ({len(course["sources"])})</h2><ul>{srcs}</ul></div>'
        '<script>document.querySelectorAll(".print-sheet").forEach(function(b){b.addEventListener("click",function(){document.body.classList.add("printing-sheet");window.print();document.body.classList.remove("printing-sheet");});});</script>'
    )

def card(lang, course, soon=False):
    track = course_track(course)
    cls = "edu-card" + (" arch" if track == "arch" else "") + (" soon" if soon else "")
    badge = T(lang, "Coming soon", "Bientôt", "Pronto", "قريباً", "Presto", "בקרוב") if soon else T(lang, "Live", "En ligne", "En vivo", "متاح", "Attivo", "חי")
    title = T(lang, *course["title"]) if not soon else T(lang, *course[2])
    blurb = T(lang, *course["blurb"]) if not soon else T(lang, *course[3])
    code = course["code"] if not soon else course[1]
    inner = f'<span class="edu-badge">{e(badge)}</span><h3>{e(title)}</h3><p>{e(blurb)}</p><p class="edu-code">{e(code)}</p>'
    if soon:
        return f'<li class="{cls}" data-track="{e(track)}">{inner}</li>'
    return f'<li class="{cls}" data-track="{e(track)}"><a href="{course["slug"]}.html">{inner}</a></li>'

def course_track(course):
    return course["track"] if isinstance(course, dict) else course[0]

def courses_main(lang, r):
    h1 = T(lang, "Courses", "Cours", "Cursos", "الدورات", "Corsi", "קורסים")
    lead = T(lang,
              "Geologist and archaeologist tracks. Year 1 and the later outlines are free self-study. No university credit.",
              "Parcours géologue et archéologue. L’année 1 et les plans suivants sont une étude libre. Aucun crédit universitaire.",
              "Itinerarios de geólogo y arqueólogo. El año 1 y los planes posteriores son estudio libre. Sin crédito universitario.",
              "مسارا الجيولوجي والآثاري. السنة الأولى والمخططات اللاحقة دراسة حرة. بلا ساعات جامعية.",
              "Percorsi di geologo e archeologo. L’anno 1 e gli schemi successivi sono studio libero. Nessun credito universitario.",
              "מסלולי גאולוג וארכאולוג. שנה 1 והמתווים הבאים הם לימוד עצמי חינמי. בלי נקודות זכות.")
    y1 = T(lang, "Year 1", "Année 1", "Año 1", "السنة 1", "Anno 1", "שנה 1")
    later = T(lang, "Later outlines", "Plans suivants", "Planes posteriores", "مخططات لاحقة", "Schemi successivi", "מתווים בהמשך")
    geo = T(lang, "Geologist", "Géologue", "Geólogo", "جيولوجي", "Geologo", "גאולוג")
    arc = T(lang, "Archaeologist", "Archéologue", "Arqueólogo", "آثاري", "Archeologo", "ארכאולוג")
    def grid(items, soon=False):
        return '<ul class="edu-grid">' + "".join(card(lang, c, soon) for c in items) + "</ul>"
    earth_live = [c for c in LIVE if c["track"] == "earth"]
    arch_live = [c for c in LIVE if c["track"] == "arch"]
    earth_later = [c for c in LATER if c["track"] == "earth"]
    arch_later = [c for c in LATER if c["track"] == "arch"]
    filt = T(lang, "Filter", "Filtrer", "Filtrar", "تصفية", "Filtra", "סינון")
    all_l = T(lang, "All", "Tout", "Todo", "الكل", "Tutti", "הכל")
    return hero(lang, r, T(lang, "Education", "Éducation", "Educación", "التعليم", "Istruzione", "חינוך"), h1, lead) + (
        f'<div class="sm-wrap crs"><p class="edu-note">{e(disc(lang))}</p>'
        f'<div class="crs-frow" role="group" aria-label="{e(filt)}">'
        f'<button type="button" aria-pressed="true" data-track="all">{e(all_l)}</button>'
        f'<button type="button" aria-pressed="false" data-track="earth">{e(geo)}</button>'
        f'<button type="button" aria-pressed="false" data-track="arch">{e(arc)}</button></div>'
        f'<h2 id="y1">{e(geo)}</h2><h3>{e(y1)}</h3>{grid(earth_live)}<h3>{e(later)}</h3>{grid(earth_later)}'
        f'<h2 id="y2">{e(arc)}</h2><h3>{e(y1)}</h3>{grid(arch_live)}<h3>{e(later)}</h3>{grid(arch_later)}'
        f'<script>document.querySelectorAll(".crs-frow button").forEach(function(b){{b.addEventListener("click",function(){{'
        f'document.querySelectorAll(".crs-frow button").forEach(function(x){{x.setAttribute("aria-pressed", x===b ? "true" : "false");}});'
        f'var t=b.getAttribute("data-track");document.querySelectorAll(".edu-grid>li").forEach(function(li){{'
        f'li.hidden = t!=="all" && li.getAttribute("data-track")!==t;}});}});}});</script>'
        f'<p><a href="Lesson_Plan.html">{e(T(lang, "Build a lesson plan", "Construire un plan de cours", "Armar un plan de clase", "ابنِ خطة درس", "Costruisci un piano di lezione", "בנו מערך שיעור"))}</a> · '
        f'<a href="Teachers.html">{e(T(lang, "Teacher sheets", "Fiches enseignants", "Fichas docentes", "أوراق المعلمين", "Schede docenti", "דפי מורים"))}</a></p></div>'
    )

def learn_main(lang, r):
    h1 = T(lang, "Learn", "Apprendre", "Aprender", "تعلّم", "Impara", "למידה")
    lead = T(lang,
              "Start with two careers: geologist and archaeologist. Rocks and time on one path. People and their things on the other.",
              "Commencez par deux métiers : géologue et archéologue. Roches et temps d’un côté. Les gens et leurs choses de l’autre.",
              "Empieza por dos oficios: geólogo y arqueólogo. Rocas y tiempo en un camino. Las personas y sus cosas en el otro.",
              "ابدأ بمهنتين: الجيولوجي والآثاري. الصخور والزمن في مسار. الناس وأشياؤهم في الآخر.",
              "Inizia da due mestieri: geologo e archeologo. Rocce e tempo su un sentiero. Le persone e le loro cose sull’altro.",
              "התחילו בשני מקצועות: גאולוג וארכאולוג. סלעים וזמן בנתיב אחד. אנשים והחפצים שלהם בנתיב השני.")
    doors = (
        f'<ul class="edu-grid"><li class="edu-card"><h3><a href="Earth_Materials.html">{e(T(lang, *EARTH["title"]))}</a></h3><p>{e(T(lang, *EARTH["blurb"]))}</p></li>'
        f'<li class="edu-card arch"><h3><a href="World_Archaeology.html">{e(T(lang, *ARCH["title"]))}</a></h3><p>{e(T(lang, *ARCH["blurb"]))}</p></li></ul>'
    )
    lessons = [
        ("Earth_Materials.html#rocks",
         ("Read a rock", "Lire une roche", "Leer una roca", "اقرأ صخراً", "Leggere una roccia", "לקרוא סלע"),
         ("Say whether it cooled, settled, or changed while solid. Most fossils sit in the settled ones.",
          "Dites si elle a refroidi, s’est déposée, ou a changé à l’état solide. La plupart des fossiles sont dans celles qui se sont déposées.",
          "Di si se enfrió, se depositó o cambió en sólido. Casi todos los fósiles están en las depositadas.",
          "قل إن كانت بردت أو ترسّبت أو تغيّرت وهي صلبة. معظم الأحافير في المترسّبة.",
          "Di se si è raffreddata, depositata o cambiata da solida. Quasi tutti i fossili stanno in quelle depositate.",
          "אמרו אם התקרר, שקע, או השתנה כמוצק. רוב המאובנים בשוקעים.")),
        ("Stratigraphic_Record.html#layers",
         ("A layer is a page", "Une couche est une page", "Una capa es una página", "الطبقة صفحة", "Uno strato è una pagina", "שכבה היא עמוד"),
         ("Younger usually lies on older, unless the stack was turned. A formation is rock. A period is time.",
          "Le plus jeune repose en général sur le plus vieux, sauf pile retournée. Une formation est de la roche. Une période est du temps.",
          "Lo más joven suele estar sobre lo más viejo, salvo pila volcada. Una formación es roca. Un período es tiempo.",
          "الأحدث يعلو الأقدم عادة، إلا إذا انقلبت الرزمة. التكوين صخر. والفترة زمن.",
          "Il più giovane sta di solito sul più vecchio, salvo pila rovesciata. Una formazione è roccia. Un periodo è tempo.",
          "הצעיר בדרך כלל על העתיק, אלא אם הערימה התהפכה. תצורה היא סלע. תור הוא זמן.")),
        ("World_Archaeology.html#things",
         ("A thing needs its layer", "Une chose a besoin de sa couche", "Una cosa necesita su capa", "الشيء يحتاج طبقته", "Una cosa ha bisogno del suo strato", "חפץ צריך את השכבה שלו"),
         ("Archaeology is not treasure. Without the layer, most of the story is gone.",
          "L’archéologie n’est pas un trésor. Sans la couche, presque toute l’histoire a disparu.",
          "La arqueología no es un tesoro. Sin la capa, casi toda la historia se fue.",
          "الآثار ليست كنزاً. بلا الطبقة يذهب معظم الحكاية.",
          "L’archeologia non è un tesoro. Senza lo strato, quasi tutta la storia se n’è andata.",
          "ארכאולוגיה אינה אוצר. בלי השכבה, רוב הסיפור נעלם.")),
    ]
    lis = "".join(
        f'<li><a href="{href}">{e(T(lang, *title))}</a> — {e(T(lang, *line))}</li>'
        for href, title, line in lessons
    )
    h2 = T(lang, "Three starts", "Trois départs", "Tres inicios", "ثلاث بدايات", "Tre inizi", "שלוש התחלות")
    more = T(lang, "All courses", "Tous les cours", "Todos los cursos", "كل الدورات", "Tutti i corsi", "כל הקורסים")
    return hero(lang, r, T(lang, "Education", "Éducation", "Educación", "التعليم", "Istruzione", "חינוך"), h1, lead) + (
        f'<div class="sm-wrap">{doors}<h2>{e(h2)}</h2><ol>{lis}</ol>'
        f'<p><a href="Courses.html">{e(more)}</a></p>'
        f'<p class="edu-note">{e(disc(lang))}</p></div>'
    )

def kids_main(lang, r):
    h1 = T(lang, "Kids", "Enfants", "Niños", "الأطفال", "Bambini", "ילדים")
    lead = T(lang,
              "Short fossil facts, with the map one click away. The map stays off the top bar.",
              "De courts faits sur les fossiles, et la carte à un clic. La carte n’est pas dans la barre du haut.",
              "Hechos cortos de fósiles, y el mapa a un clic. El mapa no está en la barra de arriba.",
              "حقائق أحافير قصيرة، والخريطة على بعد نقرة. الخريطة ليست في الشريط العلوي.",
              "Fatti brevi sui fossili, e la mappa a un clic. La mappa non sta nella barra in alto.",
              "עובדות מאובנים קצרות, והמפה בלחיצה אחת. המפה לא בסרגל העליון.")
    facts = [
        (UCMP_TRI,
         ("Trilobites", "Trilobites", "Trilobites", "ثلاثيات الفصوص", "Trilobiti", "טרילוביטים"),
         ("Trilobites lived in the seas and are gone. They are much older than dinosaurs.",
          "Les trilobites vivaient dans les mers et ont disparu. Ils sont bien plus vieux que les dinosaures.",
          "Los trilobites vivían en los mares y ya no están. Son mucho más viejos que los dinosaurios.",
          "عاشت ثلاثيات الفصوص في البحار وانقرضت. هي أقدم بكثير من الديناصورات.",
          "I trilobiti vivevano nei mari e non ci sono più. Sono molto più antichi dei dinosauri.",
          "טרילוביטים חיו בים ואינם. הם עתיקים בהרבה מדינוזאורים.")),
        ("Earth_Materials.html#rocks",
         ("Ferns in rock", "Fougères dans la roche", "Helechos en la roca", "سراخس في الصخر", "Felci nella roccia", "שרכים בסלע"),
         ("A fossil plant means plants grew there. Most fossils sit in sedimentary rock, the kind that settled.",
          "Une plante fossile veut dire que des plantes poussaient là. La plupart des fossiles sont dans la roche sédimentaire, celle qui s’est déposée.",
          "Una planta fósil significa que allí crecían plantas. Casi todos los fósiles están en roca sedimentaria, la que se depositó.",
          "نبات أحفوري يعني أن نباتات نمت هناك. معظم الأحافير في الصخر الرسوبي، الذي ترسّب.",
          "Una pianta fossile significa che lì crescevano piante. Quasi tutti i fossili stanno nella roccia sedimentaria, quella depositata.",
          "צמח מאובן אומר שצמחים צמחו שם. רוב המאובנים בסלע משקע, זה ששקע.")),
        ("Dinosaurs.html",
         ("Dinosaurs", "Dinosaures", "Dinosaurios", "ديناصورات", "Dinosauri", "דינוזאורים"),
         ("Dinosaurs lived on land. A giant swimmer from the same ages is not automatically a dinosaur.",
          "Les dinosaures vivaient sur terre. Un géant nageur des mêmes âges n’est pas automatiquement un dinosaure.",
          "Los dinosaurios vivían en tierra. Un nadador gigante de las mismas edades no es automáticamente un dinosaurio.",
          "عاشت الديناصورات على اليابسة. السبّاح العملاق من الأعمار نفسها ليس تلقائياً ديناصوراً.",
          "I dinosauri vivevano sulla terraferma. Un nuotatore gigante delle stesse età non è automaticamente un dinosauro.",
          "דינוזאורים חיו ביבשה. שחיין ענק מאותם גילים אינו אוטומטית דינוזאור.")),
        (NPS_TIME,
         ("Ice Age", "Âge de glace", "Era de hielo", "العصر الجليدي", "Era glaciale", "עידן הקרח"),
         ("Mammoths are far closer to us in time than a Tyrannosaurus is to a mammoth. Tyrannosaurus lived near 66 million years ago.",
          "Les mammouths sont bien plus proches de nous dans le temps qu’un Tyrannosaurus ne l’est d’un mammouth. Tyrannosaurus vivait vers il y a 66 millions d’années.",
          "Los mamuts están mucho más cerca de nosotros en el tiempo que un Tyrannosaurus de un mamut. Tyrannosaurus vivía hace unos 66 millones de años.",
          "الماموث أقرب إلينا في الزمن بكثير من التيرانوصور إلى الماموث. عاش التيرانوصور قرب قبل 66 مليون سنة.",
          "I mammut sono molto più vicini a noi nel tempo di quanto un Tyrannosaurus lo sia a un mammut. Il Tyrannosaurus viveva circa 66 milioni di anni fa.",
          "ממותות קרובות אלינו בזמן הרבה יותר מטירנוזאורוס אל ממותה. טירנוזאורוס חי סביב לפני 66 מיליון שנה.")),
    ]
    lis = []
    for href, title, line in facts:
        name = e(T(lang, *title))
        text = e(T(lang, *line))
        if href.startswith("http"):
            lis.append(f'<li><a href="{href}">{name}</a> — {text}</li>')
        else:
            lis.append(f'<li><a href="{href}">{name}</a> — {text}</li>')
    map_a = T(lang, "Open the kids fossil map", "Ouvrir la carte des fossiles pour enfants", "Abrir el mapa de fósiles para niños", "افتح خريطة الأحافير للأطفال", "Apri la mappa dei fossili per bambini", "פתחו את מפת המאובנים לילדים")
    return hero(lang, r, T(lang, "Education · Kids", "Éducation · Enfants", "Educación · Niños", "التعليم · الأطفال", "Istruzione · Bambini", "חינוך · ילדים"), h1, lead) + (
        f'<div class="sm-wrap"><ul>{"".join(lis)}</ul>'
        f'<p><a class="btn" href="Kids_Map.html">{e(map_a)}</a></p>'
        f'<p class="edu-note">{e(T(lang, "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI."))}</p></div>'
    )

def teachers_main(lang, r):
    h1 = T(lang, "Teachers", "Enseignants", "Docentes", "المعلمون", "Insegnanti", "מורים")
    lead = T(lang,
              "One-page sheets for the live courses, and a lesson plan you build in the browser.",
              "Des fiches d’une page pour les cours en ligne, et un plan que vous construisez dans le navigateur.",
              "Fichas de una página para los cursos en vivo, y un plan que armas en el navegador.",
              "أوراق من صفحة للمسارات المتاحة، وخطة تبنونها في المتصفح.",
              "Schede di una pagina per i percorsi attivi, e un piano che costruisci nel browser.",
              "דפים של עמוד אחד למסלולים החיים, ומערך שאתם בונים בדפדפן.")
    lis = "".join(
        f'<li><a href="{c["slug"]}.html#sheet">{e(c["code"])} · {e(T(lang, *c["title"]))}</a></li>'
        for c in ALL
    )
    plan = T(lang, "Open the lesson plan builder", "Ouvrir le constructeur de plan", "Abrir el constructor del plan", "افتح بانِي خطة الدرس", "Apri il costruttore del piano", "פתחו את בונה מערך השיעור")
    return hero(lang, r, T(lang, "Education · Teachers", "Éducation · Enseignants", "Educación · Docentes", "التعليم · المعلمون", "Istruzione · Insegnanti", "חינוך · מורים"), h1, lead) + (
        f'<div class="sm-wrap"><p><a class="btn" href="Lesson_Plan.html">{e(plan)}</a></p>'
        f'<h2>{e(T(lang, "Sheets", "Fiches", "Fichas", "الأوراق", "Schede", "דפים"))}</h2><ul>{lis}</ul>'
        f'<p class="edu-note">{e(disc(lang))}</p></div>'
    )

def lesson_main(lang, r=""):
    h1 = T(lang, "Lesson plan", "Plan de cours", "Plan de clase", "خطة درس", "Piano di lezione", "מערך שיעור")
    lead = T(lang,
              "Pick a grade, a subject, and a length. Tick lessons. The plan is built in this browser and is not sent anywhere.",
              "Choisissez un niveau, une matière et une durée. Cochez des leçons. Le plan se construit dans ce navigateur et n’est envoyé nulle part.",
              "Elige un grado, una materia y una duración. Marca lecciones. El plan se arma en este navegador y no se envía a ningún sitio.",
              "اختاروا صفاً ومادة ومدة. علّموا الدروس. تُبنى الخطة في هذا المتصفح ولا تُرسل إلى أي مكان.",
              "Scegli un grado, una materia e una durata. Spunta le lezioni. Il piano si costruisce in questo browser e non viene inviato da nessuna parte.",
              "בחרו כיתה, מקצוע ומשך. סמנו שיעורים. המערך נבנה בדפדפן הזה ולא נשלח לשום מקום.")
    grade = T(lang, "Grade", "Niveau", "Grado", "الصف", "Grado", "כיתה")
    g1 = T(lang, "Grades 3–5", "CM1–CM2", "Grados 3–5", "الصفوف 3–5", "Classi 3–5", "כיתות ג–ה")
    g2 = T(lang, "Grades 6–8", "6e–4e", "Grados 6–8", "الصفوف 6–8", "Classi 6–8", "כיתות ו–ח")
    g3 = T(lang, "Grades 9–12", "3e–Terminale", "Grados 9–12", "الصفوف 9–12", "Classi 9–12", "כיתות ט–יב")
    sub = T(lang, "Subject", "Matière", "Materia", "المادة", "Materia", "מקצוע")
    s1 = T(lang, "Earth science", "Sciences de la Terre", "Ciencias de la Tierra", "علوم الأرض", "Scienze della Terra", "מדעי כדור הארץ")
    s2 = T(lang, "Archaeology", "Archéologie", "Arqueología", "آثار", "Archeologia", "ארכאולוגיה")
    mins = T(lang, "Lesson length", "Durée", "Duración", "المدة", "Durata", "משך")
    choose = T(lang, "Lessons for this plan", "Leçons de ce plan", "Lecciones de este plan", "دروس هذه الخطة", "Lezioni di questo piano", "שיעורים למערך")
    none = T(lang, "No lesson is tagged for this grade and subject yet.", "Aucune leçon n’est étiquetée pour ce niveau et cette matière.", "Ninguna lección está etiquetada para este grado y materia.", "لا درس موسوم لهذا الصف وهذه المادة بعد.", "Nessuna lezione è etichettata per questo grado e questa materia.", "אין עדיין שיעור מתויג לכיתה ולמקצוע האלה.")
    go = T(lang, "Build my lesson plan", "Construire mon plan", "Armar mi plan", "ابنِ خطتي", "Costruisci il mio piano", "בנו את המערך")
    pr = T(lang, "Print plan", "Imprimer", "Imprimir", "اطبع", "Stampa", "הדפסה")
    err = T(lang, "The lesson builder could not load. Refresh the page.", "Le constructeur n’a pas pu se charger. Rafraîchissez la page.", "El constructor no pudo cargarse. Recarga la página.", "تعذّر تحميل الباني. أعيدوا تحميل الصفحة.", "Il costruttore non si è caricato. Ricarica la pagina.", "בונה המערך לא נטען. רעננו את העמוד.")
    nos = T(lang, "This builder needs JavaScript. The teacher sheets still open without it.", "Ce constructeur a besoin de JavaScript. Les fiches s’ouvrent encore sans lui.", "Este constructor necesita JavaScript. Las fichas se abren igual sin él.", "يحتاج الباني إلى جافاسكربت. أوراق المعلمين تُفتح من دونه.", "Questo costruttore ha bisogno di JavaScript. Le schede si aprono anche senza.", "הבונה צריך JavaScript. דפי המורים נפתחים גם בלעדיו.")
    top = hero(lang, r, T(lang, "Education · Teachers", "Éducation · Enseignants", "Educación · Docentes", "التعليم · المعلمون", "Istruzione · Insegnanti", "חינוך · מורים"), h1, lead)
    return (
        f'<main id="main">{top}'
        f'<div class="sm-wrap" id="lp"><form id="lp-form" class="lp-form">'
        f'<div class="lp-field"><label for="lp-grade">{e(grade)}</label><select id="lp-grade" name="grade">'
        f'<option value="3-5">{e(g1)}</option><option value="6-8">{e(g2)}</option><option value="9-12">{e(g3)}</option></select></div>'
        f'<div class="lp-field"><label for="lp-subject">{e(sub)}</label><select id="lp-subject" name="subject">'
        f'<option value="earth">{e(s1)}</option><option value="arch">{e(s2)}</option></select></div>'
        f'<div class="lp-field"><label for="lp-min">{e(mins)}</label><select id="lp-min" name="minutes">'
        f'<option value="30">30</option><option value="45" selected>45</option><option value="60">60</option><option value="90">90</option></select></div>'
        f'<fieldset class="lp-field"><legend>{e(choose)}</legend><div class="lp-sols" id="lp-sols"></div>'
        f'<p id="lp-none" hidden>{e(none)}</p></fieldset>'
        f'<div class="lp-actions"><button type="submit">{e(go)}</button> '
        f'<button type="button" id="lp-print" hidden>{e(pr)}</button></div></form>'
        f'<article class="lp-plan" id="lp-plan" hidden></article>'
        f'<template class="lp-error-tpl"><p role="alert">{e(err)}</p></template>'
        f'<noscript><p>{e(nos)} <a href="Teachers.html">Teachers</a></p></noscript>'
        f'<p class="edu-note">{e(T(lang, "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI.", "Created by the Founder and SI."))}</p></div></main>'
    )

ELI = {
"Color alone misnames many minerals. Scratch, shape, and a simple acid test, only with a teacher, sort the common ones.":
("La couleur seule trompe. Rayure, forme, et un acide seulement avec un enseignant, trient les minéraux courants.",
 "El color solo confunde. Raya, forma, y un ácido solo con un docente, separan los minerales comunes.",
 "اللون وحده يخطئ التسمية. الخدش والشكل وحمض بإشراف معلم فقط تفرز المعادن الشائعة.",
 "Il colore da solo sbaglia. Striatura, forma, e un acido solo con un docente, separano i minerali comuni.",
 "הצבע לבדו מטעה. שריטה, צורה, וחומצה רק עם מורה, ממיינים את המינרלים הנפוצים."),
"Igneous, sedimentary, and metamorphic are processes, not a ranking of importance.":
("Igné, sédimentaire et métamorphique sont des processus, pas un classement.",
 "Ígneo, sedimentario y metamórfico son procesos, no un ranking.",
 "الناري والرسوبي والمتحول عمليات لا ترتيب أهمية.",
 "Igneo, sedimentario e metamorfico sono processi, non una classifica.",
 "תצרה, משקע ומותמר הם תהליכים, לא דירוג חשיבות."),
"The USGS figure is 4.54 billion years. Some school standards still print 4.6 billion. Keep those two numbers apart.":
("Le chiffre USGS est 4,54 milliards d’années. Certaines normes scolaires impriment encore 4,6 milliards. Gardez les deux nombres séparés.",
 "La cifra del USGS es 4.540 millones de años. Algunas normas escolares aún imprimen 4.6 mil millones. Separa los dos números.",
 "رقم USGS هو 4.54 مليار سنة. بعض معايير المدرسة تطبع 4.6 مليار. أبقوا الرقمين منفصلين.",
 "La cifra USGS è 4,54 miliardi di anni. Alcuni standard scolastici stampano ancora 4,6 miliardi. Tieni separati i due numeri.",
 "המספר של USGS הוא 4.54 מיליארד שנה. חלק מתקני בית הספר עדיין מדפיסים 4.6 מיליארד. הפרידו את שני המספרים."),
"The sample is the notebook. Leave protected rock where it is.":
("L’échantillon est le carnet. Laissez la roche protégée sur place.",
 "La muestra es el cuaderno. Deja la roca protegida donde está.",
 "العينة هي الدفتر. اتركوا الصخر المحمي مكانه.",
 "Il campione è il taccuino. Lascia la roccia protetta dov’è.",
 "הדוגמה היא המחברת. השאירו סלע מוגן במקומו."),
"Position is a clue. It is not, by itself, a date.":
("La position est un indice. Ce n’est pas, à elle seule, une date.",
 "La posición es una pista. No es, por sí sola, una fecha.",
 "الموضع قرينة. ليس بمفرده تاريخاً.",
 "La posizione è un indizio. Non è, da sola, una data.",
 "המיקום הוא רמז. הוא לבדו אינו תאריך."),
"Correlation matches time. It does not move the quarries onto each other.":
("La corrélation aligne le temps. Elle ne superpose pas les carrières.",
 "La correlación iguala el tiempo. No pone las canteras una sobre otra.",
 "المضاهاة تطابق الزمن. لا تضع المحاجر فوق بعضها.",
 "La correlazione allinea il tempo. Non sovrappone le cave.",
 "מתאם משווה זמן. הוא לא מניח מחצבות זו על זו."),
"Say million years ago in words. The chart, not a nickname, holds the boundary.":
("Dites « il y a des millions d’années » en mots. Le tableau, pas un surnom, tient la limite.",
 "Di «hace millones de años» con palabras. La escala, no un apodo, guarda el límite.",
 "قولوا «قبل ملايين السنين» بالكلمات. الجدول لا اللقب يمسك الحد.",
 "Dite «milioni di anni fa» a parole. La scala, non un soprannome, tiene il limite.",
 "אמרו «לפני מיליוני שנים» במילים. הסרגל, לא כינוי, מחזיק את הגבול."),
"The clock is in the mineral. The layer’s story uses more than one line of evidence.":
("L’horloge est dans le minéral. L’histoire de la couche utilise plus d’une preuve.",
 "El reloj está en el mineral. La historia de la capa usa más de una prueba.",
 "الساعة في المعدن. حكاية الطبقة تستخدم أكثر من دليل.",
 "L’orologio è nel minerale. La storia dello strato usa più di una prova.",
 "השעון במינרל. סיפור השכבה משתמש ביותר מראיה אחת."),
"Permission comes before the compass.":
("La permission vient avant la boussole.",
 "El permiso va antes que la brújula.",
 "الإذن قبل البوصلة.",
 "Il permesso viene prima della bussola.",
 "הרשות באה לפני המצפן."),
"The notebook is the specimen.":
("Le carnet est l’échantillon.",
 "El cuaderno es la muestra.",
 "الدفتر هو العينة.",
 "Il taccuino è il campione.",
 "המחברת היא הדוגמה."),
"A legend is a published claim. A curb is practice.":
("Une légende est une affirmation publiée. Un trottoir est un exercice.",
 "Una leyenda es una afirmación publicada. Un bordillo es práctica.",
 "مفتاح الخريطة ادعاء منشور. الرصيف تمرين.",
 "Una legenda è un’affermazione pubblicata. Un marciapiede è un esercizio.",
 "מקרא הוא טענה שפורסמה. שפת מדרכה היא תרגול."),
"Stop at the report. The supervised camp is still to be written.":
("Arrêtez-vous au rapport. Le camp encadré n’est pas encore écrit.",
 "Detente en el informe. El campamento supervisado aún no está escrito.",
 "قفوا عند التقرير. المعسكر بإشراف لم يُكتب بعد.",
 "Fermati al rapporto. Il campo sorvegliato non è ancora scritto.",
 "עצרו בדוח. המחנה המודרך עדיין לא נכתב."),
"Context is the find. The object alone is the leftover.":
("Le contexte est la trouvaille. L’objet seul est le reste.",
 "El contexto es el hallazgo. El objeto solo es el resto.",
 "السياق هو اللقية. الشيء وحده بقية.",
 "Il contesto è il ritrovamento. L’oggetto da solo è il resto.",
 "ההקשר הוא הממצא. החפץ לבדו הוא השארית."),
"Use the Smithsonian pages for the ages. Do not add a zero.":
("Utilisez les pages du Smithsonian pour les âges. N’ajoutez pas un zéro.",
 "Usa las páginas del Smithsonian para las edades. No añadas un cero.",
 "استخدموا صفحات Smithsonian للأعمار. لا تضيفوا صفراً.",
 "Usa le pagine dello Smithsonian per le età. Non aggiungere uno zero.",
 "השתמשו בעמודי Smithsonian לגילים. אל תוסיפו אפס."),
"Match the clock to the material. Do not force one method onto every layer.":
("Accordez l’horloge à la matière. Ne forcez pas une méthode sur chaque couche.",
 "Ajusta el reloj al material. No fuerces un método en cada capa.",
 "طابقوا الساعة بالمادة. لا تفرضوا طريقة واحدة على كل طبقة.",
 "Accoppia l’orologio al materiale. Non forzare un metodo su ogni strato.",
 "התאימו את השעון לחומר. אל תכפו שיטה אחת על כל שכבה."),
"Label the cast. Do not treat this page as permission.":
("Étiquetez le moulage. Ne prenez pas cette page pour une permission.",
 "Etiqueta el molde. No tomes esta página como un permiso.",
 "وسِموا القالب. لا تعدّوا هذه الصفحة إذناً.",
 "Etichetta il calco. Non prendere questa pagina come un permesso.",
 "סמנו את היציקה. אל תתייחסו לעמוד הזה כאל רשות."),
"The place is part of the evidence.":
("La place fait partie de la preuve.",
 "El lugar es parte de la prueba.",
 "الموضع جزء من الدليل.",
 "Il luogo fa parte della prova.",
 "המקום הוא חלק מהראיה."),
"A later object in an older cut is a known trap.":
("Un objet plus tardif dans une coupe plus vieille est un piège connu.",
 "Un objeto posterior en un corte más viejo es una trampa conocida.",
 "شيء لاحق في قطع أقدم فخ معروف.",
 "Un oggetto più tardo in un taglio più vecchio è una trappola nota.",
 "חפץ מאוחר בחתך עתיק יותר הוא מלכודת ידועה."),
"Practice on a shoebox. Do not turn a real place into a classroom dig.":
("Entraînez-vous sur une boîte. Ne transformez pas un vrai lieu en fouille de classe.",
 "Practica en una caja. No conviertas un lugar real en una excavación de clase.",
 "تدرّبوا على علبة. لا تحوّلوا مكاناً حقيقياً إلى حفر صفّي.",
 "Esercitati su una scatola. Non trasformare un luogo vero in uno scavo di classe.",
 "תרגלו על קופסה. אל תהפכו מקום אמיתי לחפירת כיתה."),
"An honest gap on the label is better than a guessed place.":
("Un vide honnête sur l’étiquette vaut mieux qu’une place devinée.",
 "Un hueco honesto en la etiqueta vale más que un lugar adivinado.",
 "فراغ صادق على البطاقة خير من موضع مخمّن.",
 "Un vuoto onesto sull’etichetta è meglio di un luogo indovinato.",
 "פער כן על התווית עדיף על מקום מנוחש."),
"Look and record. Do not open the ground.":
("Regardez et notez. N’ouvrez pas le sol.",
 "Mira y anota. No abras el suelo.",
 "انظر وسجّل. لا تفتح الأرض.",
 "Guarda e annota. Non aprire il terreno.",
 "הסתכלו ורשמו. אל תפתחו את הקרקע."),
"The sheet is how the layer survives the season.":
("La fiche est la façon dont la couche survit à la saison.",
 "La ficha es cómo la capa sobrevive a la temporada.",
 "البطاقة هي كيف تبقى الطبقة بعد الموسم.",
 "La scheda è il modo in cui lo strato sopravvive alla stagione.",
 "הטופס הוא איך השכבה שורדת את העונה."),
"The record outlives the season. The hole should not.":
("L’archive survit à la saison. Le trou ne devrait pas.",
 "El registro sobrevive a la temporada. El hoyo no debería.",
 "السجل يبقى بعد الموسم. الحفرة لا ينبغي أن تبقى.",
 "Il registro sopravvive alla stagione. Il buco non dovrebbe.",
 "הרשומה מאריכה ימים אחרי העונה. הבור לא צריך."),
"The refusal is part of the record.":
("Le refus fait partie de l’archive.",
 "La negativa es parte del registro.",
 "الرفض جزء من السجل.",
 "Il rifiuto fa parte del registro.",
 "הסירוב הוא חלק מהרשומה."),
}

def eli_text(lang, raw):
    if len(raw) == 6:
        return T(lang, *raw)
    en = raw[0]
    if lang == "en":
        return en
    return ELI[en][IX[lang] - 1]

def lesson_json(lang):
    ui = {
        "title": T(lang, "Lesson plan", "Plan de cours", "Plan de clase", "خطة الدرس", "Piano di lezione", "מערך שיעור"),
        "minutes": T(lang, "{n} minutes", "{n} minutes", "{n} minutos", "{n} دقيقة", "{n} minuti", "{n} דקות"),
        "lessons": T(lang, "Lessons", "Leçons", "Lecciones", "الدروس", "Lezioni", "שיעורים"),
        "objectives": T(lang, "Objectives", "Objectifs", "Objetivos", "الأهداف", "Obiettivi", "מטרות"),
        "standards": T(lang, "Standards", "Normes", "Estándares", "المعايير", "Standard", "תקנים"),
        "stdNote": T(lang,
                     "Official English text. MS-ESS1-4 says 4.6 billion years. This site uses the USGS age of 4.54 billion years.",
                     "Texte officiel en anglais. MS-ESS1-4 dit 4,6 milliards d’années. Ce site utilise l’âge USGS de 4,54 milliards d’années.",
                     "Texto oficial en inglés. MS-ESS1-4 dice 4.6 mil millones de años. Este sitio usa la edad USGS de 4.540 millones de años.",
                     "النص الرسمي بالإنجليزية. يقول MS-ESS1-4 إن العمر 4.6 مليار سنة. يستخدم هذا الموقع عمر USGS البالغ 4.54 مليار سنة.",
                     "Testo ufficiale in inglese. MS-ESS1-4 dice 4,6 miliardi di anni. Questo sito usa l’età USGS di 4,54 miliardi di anni.",
                     "טקסט רשמי באנגלית. MS-ESS1-4 אומר 4.6 מיליארד שנה. האתר משתמש בגיל USGS של 4.54 מיליארד."),
        "noObj": T(lang, "No standard is tagged for this grade and subject on the lessons you picked.",
                   "Aucune norme n’est étiquetée pour ce niveau et cette matière sur les leçons choisies.",
                   "Ningún estándar está etiquetado para este grado y materia en las lecciones elegidas.",
                   "لا معيار موسوم لهذا الصف وهذه المادة في الدروس المختارة.",
                   "Nessuno standard è etichettato per questo grado e questa materia nelle lezioni scelte.",
                   "אין תקן מתויג לכיתה ולמקצוע האלה בשיעורים שנבחרו."),
        "activity": T(lang, "Activity", "Activité", "Actividad", "النشاط", "Attività", "פעילות"),
        "timing": T(lang, "Times are a split of the length you chose: read, talk, write.",
                    "Les temps partagent la durée choisie : lire, parler, écrire.",
                    "Los tiempos parten la duración elegida: leer, hablar, escribir.",
                    "الأوقات تقسم المدة المختارة: قراءة وحوار وكتابة.",
                    "I tempi dividono la durata scelta: leggere, parlare, scrivere.",
                    "הזמנים מחלקים את המשך שבחרתם: קריאה, שיחה, כתיבה."),
        "read": T(lang, "Read ({n} min)", "Lire ({n} min)", "Leer ({n} min)", "اقرأ ({n} د)", "Leggi ({n} min)", "קריאה ({n} דק')"),
        "talk": T(lang, "Talk ({n} min)", "Parler ({n} min)", "Hablar ({n} min)", "تحدث ({n} د)", "Parla ({n} min)", "שיחה ({n} דק')"),
        "write": T(lang, "Write ({n} min)", "Écrire ({n} min)", "Escribir ({n} min)", "اكتب ({n} د)", "Scrivi ({n} min)", "כתיבה ({n} דק')"),
        "questions": T(lang, "Questions", "Questions", "Preguntas", "أسئلة", "Domande", "שאלות"),
        "assessment": T(lang, "Assessment", "Évaluation", "Evaluación", "التقويم", "Valutazione", "הערכה"),
        "assessText": T(lang, "Students answer in their own words, with one cited age or one cited place. A two-letter age abbreviation does not count.",
                        "Les élèves répondent avec leurs mots, avec un âge cité ou un lieu cité. Une abréviation d’âge en deux lettres ne compte pas.",
                        "El alumnado responde con sus palabras, con una edad citada o un lugar citado. Una sigla de edad de dos letras no cuenta.",
                        "يجيب الطلاب بكلماتهم، مع عمر موثّق أو مكان موثّق. اختصار العمر بحرفين لا يُحتسب.",
                        "Gli studenti rispondono con parole proprie, con un’età citata o un luogo citato. Una sigla di età di due lettere non conta.",
                        "התלמידים עונים במילים שלהם, עם גיל מצוטט או מקום מצוטט. קיצור גיל בן שתי אותיות לא נספר."),
        "sources": T(lang, "Sources", "Sources", "Fuentes", "المصادر", "Fonti", "מקורות"),
        "pick": T(lang, "Tick at least one lesson.", "Cochez au moins une leçon.", "Marca al menos una lección.", "علّموا درساً واحداً على الأقل.", "Spunta almeno una lezione.", "סמנו שיעור אחד לפחות."),
        "credit": "Created by the Founder and SI.",
    }
    lessons = []
    for course in ALL:
        stds = earth_stds() if course["track"] == "earth" else arch_stds()
        grades = ["3-5", "6-8", "9-12"]
        subject = "earth" if course["track"] == "earth" else "arch"
        src_name, src_url = course["sources"][0]
        for u in course["units"][:2]:
            lessons.append({
                "u": course["slug"] + ".html#" + u["id"],
                "n": course["code"] + " · " + T(lang, *u["title"]),
                "grades": grades,
                "subjects": [subject],
                "eli": [eli_text(lang, u["eli"])],
                "questions": [T(lang, *q) for q in u["questions"]],
                "standards": stds,
                "src": {"name": src_name, "href": src_url},
            })
    return {"ui": ui, "lessons": lessons}

META = {
    "Learn": (
        ("Learn", "Apprendre", "Aprender", "تعلّم", "Impara", "למידה"),
        ("Two started careers: geologist and archaeologist, with three short ways in.",
         "Deux métiers commencés : géologue et archéologue, avec trois portes courtes.",
         "Dos oficios empezados: geólogo y arqueólogo, con tres entradas cortas.",
         "مهنتان بدأتا: الجيولوجي والآثاري، مع ثلاثة مداخل قصيرة.",
         "Due mestieri iniziati: geologo e archeologo, con tre ingressi brevi.",
         "שני מקצועות שהתחילו: גאולוג וארכאולוג, עם שלוש כניסות קצרות."),
    ),
    "Courses": (
        ("Courses", "Cours", "Cursos", "الدورات", "Corsi", "קורסים"),
        ("Geologist and archaeologist outlines, year 1 and the later courses, free and sourced.",
         "Plans de géologue et d’archéologue, année 1 et cours suivants, gratuits et sourcés.",
         "Planes de geólogo y arqueólogo, año 1 y cursos posteriores, gratis y con fuentes.",
         "مخططات الجيولوجي والآثاري، السنة الأولى واللاحقة، مجانية وموثّقة.",
         "Schemi di geologo e archeologo, anno 1 e corsi successivi, gratis e con fonti.",
         "מתווי גאולוג וארכאולוג, שנה 1 והקורסים הבאים, חינם ועם מקורות."),
    ),
    "Teachers": (
        ("Teachers", "Enseignants", "Docentes", "المعلمون", "Insegnanti", "מורים"),
        ("Printable sheets for the live Earth courses, plus a browser lesson plan.",
         "Fiches imprimables pour les cours de Terre en ligne, plus un plan dans le navigateur.",
         "Fichas imprimibles de los cursos de la Tierra en vivo, y un plan en el navegador.",
         "أوراق قابلة للطباعة لمسارات الأرض المتاحة، وخطة في المتصفح.",
         "Schede stampabili per i percorsi della Terra attivi, più un piano nel browser.",
         "דפים להדפסה למסלולי כדור הארץ החיים, ומערך בדפדפן."),
    ),
    "Kids": (
        ("Kids", "Enfants", "Niños", "الأطفال", "Bambini", "ילדים"),
        ("Short fossil facts for children, and a link to the kids fossil map.",
         "De courts faits fossiles pour les enfants, et un lien vers la carte.",
         "Hechos fósiles cortos para niños, y un enlace al mapa infantil.",
         "حقائق أحافير قصيرة للأطفال، ورابط إلى خريطة الأطفال.",
         "Fatti fossili brevi per bambini, e un link alla mappa per bambini.",
         "עובדות מאובנים קצרות לילדים, וקישור למפת הילדים."),
    ),
    "Lesson_Plan": (
        ("Lesson plan", "Plan de cours", "Plan de clase", "خطة درس", "Piano di lezione", "מערך שיעור"),
        ("Teachers choose grade, subject, and length. The plan stays in the browser.",
         "Les enseignants choisissent niveau, matière et durée. Le plan reste dans le navigateur.",
         "Los docentes eligen grado, materia y duración. El plan se queda en el navegador.",
         "يختار المعلمون الصف والمادة والمدة. تبقى الخطة في المتصفح.",
         "I docenti scelgono grado, materia e durata. Il piano resta nel browser.",
         "המורים בוחרים כיתה, מקצוע ומשך. המערך נשאר בדפדפן."),
    ),
}

def meta_for(lang, page, course=None):
    if course:
        title = T(lang, *course["title"])
        desc = T(lang, *course["blurb"]) + " " + course["code"] + "."
        # keep description unique and within 155, and not equal to the bare title
        desc = desc.strip()
        if len(desc) > 155:
            desc = desc[:152].rstrip() + "..."
        return title, desc
    title = T(lang, *META[page][0])
    desc = T(lang, *META[page][1])
    return title, desc

def pages_for(lang, r):
    out = {}
    specs = {
        "Learn": learn_main(lang, r),
        "Courses": courses_main(lang, r),
        "Teachers": teachers_main(lang, r),
        "Kids": kids_main(lang, r),
        "Lesson_Plan": lesson_main(lang, r),
    }
    for name, main in specs.items():
        title, desc = meta_for(lang, name)
        scripts = ""
        if name == "Lesson_Plan":
            scripts = f'<script src="{r}bsp-lesson.js" defer></script>'
        out[name] = (title, desc, main if name == "Lesson_Plan" else f'<main id="main">{main}</main>', scripts)
    for course in ALL:
        title, desc = meta_for(lang, course["slug"], course)
        main = f'<main id="main">{course_main(lang, r, course)}</main>'
        out[course["slug"]] = (title, desc, main, "")
    return out

def check_copy():
    bad = re.compile(r"\bMa\b|\bMA\b|\bMYA\b|\bmya\b|\bGa\b")
    for lang in LANGS:
        blob = json.dumps(pages_for(lang, ""), ensure_ascii=False)
        if bad.search(blob):
            raise SystemExit("bare age abbreviation in " + lang)
        for page, (title, desc, _main, _s) in pages_for(lang, "").items():
            full = title + " | Before Saving Planets"
            if len(full) > 60:
                raise SystemExit("title too long %s %s %s" % (lang, page, len(full)))
            if not (20 <= len(desc) <= 155):
                raise SystemExit("desc length %s %s %s" % (lang, page, len(desc)))

def write_lang(lang, root, head, body, rel):
    os.makedirs(os.path.join(root, "assets", "data"), exist_ok=True)
    r = rel(lang)
    folder = root if lang == "en" else os.path.join(root, lang)
    os.makedirs(folder, exist_ok=True)
    css = f'<link rel="stylesheet" href="{r}smilodon.css"><link rel="stylesheet" href="{r}edu-tracks.css">'
    for name, (title, desc, main, scripts) in pages_for(lang, r).items():
        html_page = head(lang, name, title, desc, css) + body(lang, name, main, "toc-sub edu-track", scripts)
        with open(os.path.join(folder, name + ".html"), "w", encoding="utf-8") as f:
            f.write(html_page)
    with open(os.path.join(root, "assets", "data", "lesson-plan.%s.json" % lang), "w", encoding="utf-8") as f:
        json.dump(lesson_json(lang), f, ensure_ascii=False)
        f.write("\n")

def write_all(root, head, body, rel):
    for lang in LANGS:
        write_lang(lang, root, head, body, rel)

def refresh_chrome(root, nav, footer, pages):
    for lang in LANGS:
        folder = root if lang == "en" else os.path.join(root, lang)
        for name in pages:
            path = os.path.join(folder, name + ".html")
            if not os.path.isfile(path):
                continue
            text = open(path, encoding="utf-8").read()
            text2, n1 = re.subn(r'<nav id="topnav">.*?</nav>', nav(lang, name), text, count=1, flags=re.S)
            text3, n2 = re.subn(r'<footer>.*?</footer>', footer(lang), text2, count=1, flags=re.S)
            if n1 != 1 or n2 != 1:
                raise SystemExit("chrome not replaced: " + path)
            open(path, "w", encoding="utf-8").write(text3)

if __name__ == "__main__":
    import build
    check_copy()
    write_all(build.ROOT, build.head, build.body, build.rel)
    refresh_chrome(build.ROOT, build.nav, build.footer, build.PAGES)
    build.sync_hand_nav()
    # Sitemap must list indexable pages in PAGES order, with the existing lastmod.
    maps = []
    for L in build.LANGS:
        urls = "".join(
            f"<url><loc>{build.url(L, p)}</loc><lastmod>2026-11-02</lastmod></url>"
            for p in build.PAGES if p in build.INDEXABLE
        )
        open(os.path.join(build.ROOT, "sitemap-%s.xml" % L), "w", encoding="utf-8").write(
            '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>"
        )
        maps.append(f"<sitemap><loc>{build.DOM}/sitemap-{L}.xml</loc><lastmod>2026-11-02</lastmod></sitemap>")
    open(os.path.join(build.ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(maps) + "</sitemapindex>"
    )
    print("edu pages written")
