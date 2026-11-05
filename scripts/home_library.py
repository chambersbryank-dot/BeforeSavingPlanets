"""Homepage library. Fixed sky, then shelves. No scroll-driven Earth journey."""
import html

from finds import DEEP_NAV, NAV as DINO_NAV
from story import GLOBE, PLAY, STORY

# Same full-bleed film as the Saving Planets homepage. The jpg next to that file
# is a colored Earth still, so this page never uses it as a poster or background.
FILM = "https://media.savingplanets.com/videos/hero-loop.97191e628115.mp4"
POSTER = "https://www.savingplanets.com/assets/Threetrees3-1320.webp"

# Journey stills. The colored Earth globes (era-540, era-drift, era-today) stay off this page.
# Measured maps use the flat PALEOMAP frames, not a colored globe.
STILLS = {
    "start.webp": ("assets/hero/morph/start.webp", 1920, 1080),
    "era-oceans.webp": ("assets/hero/morph/era-oceans.webp", 1280, 720),
    "era-540.webp": ("assets/hero/paleo/m540.webp", 640, 320),
    "era-drift.webp": ("assets/hero/paleo/m200.webp", 640, 320),
    "era-today.webp": ("assets/quest/layer-stromatolite.webp", 1400, 933),
}

LIB = {
"en": dict(
    find_h="Find a chapter",
    shelf_a="Earth’s story", shelf_b="on the shelf",
    shelf_lead="Dig Quest, the fossil map, the dinosaurs, and deep time. Each shelf opens a part of the record.",
    journey_a="The", journey_b="journey",
    journey_lead="The long story sits on this shelf: a molten world, the first oceans, the measured maps, and why this library exists.",
    journey_credit="Lava and the first oceans: Created by the Founder and SI, an artist’s interpretation, not a photograph. From 540 million years: Scotese PALEOMAP via GPlates (EarthByte). The last photograph is a fossil stromatolite in Glacier National Park (National Park Service, public domain).",
    start_h="Start here",
    numbers_h="From the record",
    numbers_note="Counts on this site. The age of Earth is the U.S. Geological Survey figure used on the Dig Quest.",
    cap0="Enceladus: jets of water ice above a hidden ocean. Earth’s ice ages are a stop in the Dig Quest.",
    cap1="The cratered Moon, seen from orbit. The impact that made it opens the Dig Quest.",
    q_cta="Start the Dig Quest",
    dig_links=("Eight layers", "Continents", "Oceans", "Seas", "The Dead Sea"),
    dino_more="More dinosaurs",
    aud=(
        ("🦕", "Dig Quest", "Eight layers, from Earth’s formation to the last ice age.", "Quest.html"),
        ("🗺️", "Fossil map", "Coin cards for sites, forests, reefs, and deep-time archives.", "World_Map.html"),
        ("🧒", "Kids", "Earth and fossil pages for children.", "Kids.html"),
        ("🎓", "Teachers", "Classroom pages on fossils and deep time.", "Teachers.html"),
        ("📚", "Learn", "Lessons on fossils, climates, and deep time.", "Learn.html"),
        ("🌙", "About", "Why this library sits beside Saving Planets.", "About.html"),
    ),
    nums=(
        ("4.54 billion", "years: the age of Earth on the Dig Quest", "Quest.html", 'Source: <a href="https://pubs.usgs.gov/gip/geotime/age.html">U.S. Geological Survey</a>'),
        ("82", "fossil sites open as coin cards", "World_Map.html", "Source: the World Map on this site"),
        ("8", "Dig Quest layers, formation to the last ice age", "Quest.html", "Source: the Dig Quest on this site"),
        ("6", "languages", "index.html", "Source: this site"),
    ),
),
"fr": dict(
    find_h="Trouver un chapitre",
    shelf_a="L’histoire de la Terre", shelf_b="sur les rayons",
    shelf_lead="Dig Quest, la carte des fossiles, les dinosaures et le temps profond. Chaque rayon ouvre une part des archives.",
    journey_a="Le", journey_b="voyage",
    journey_lead="La longue histoire est sur ce rayon : un monde en fusion, les premiers océans, les cartes mesurées, et pourquoi cette bibliothèque existe.",
    journey_credit="Lave et premiers océans : créé par le fondateur et SI, une interprétation d’artiste, pas une photographie. Depuis 540 millions d’années : Scotese PALEOMAP via GPlates (EarthByte). La dernière photo est un stromatolite fossile dans le parc national des Glaciers (National Park Service, domaine public).",
    start_h="Commencer ici",
    numbers_h="Dans les archives",
    numbers_note="Les comptes de ce site. L’âge de la Terre est le chiffre du U.S. Geological Survey utilisé dans le Dig Quest.",
    cap0="Encelade : des jets de glace d’eau au-dessus d’un océan caché. Les âges de glace de la Terre sont une étape du Dig Quest.",
    cap1="La Lune cratérisée, vue depuis l’orbite. L’impact qui l’a faite ouvre le Dig Quest.",
    q_cta="Commencer le Dig Quest",
    dig_links=("Huit couches", "Continents", "Océans", "Mers", "La mer Morte"),
    dino_more="D’autres dinosaures",
    aud=(
        ("🦕", "Dig Quest", "Huit couches, de la formation de la Terre à la dernière glaciation.", "Quest.html"),
        ("🗺️", "Carte des fossiles", "Des pièces pour les sites, les forêts, les récifs et le temps profond.", "World_Map.html"),
        ("🧒", "Enfants", "Des pages sur la Terre et les fossiles pour les enfants.", "Kids.html"),
        ("🎓", "Enseignants", "Des pages de classe sur les fossiles et le temps profond.", "Teachers.html"),
        ("📚", "Apprendre", "Des leçons sur les fossiles, les climats et le temps profond.", "Learn.html"),
        ("🌙", "À propos", "Pourquoi cette bibliothèque est à côté de Saving Planets.", "About.html"),
    ),
    nums=(
        ("4,54 milliards", "d’années : l’âge de la Terre dans le Dig Quest", "Quest.html", 'Source : <a href="https://pubs.usgs.gov/gip/geotime/age.html">U.S. Geological Survey</a>'),
        ("82", "sites fossilifères ouvrent une pièce", "World_Map.html", "Source : la carte du monde de ce site"),
        ("8", "couches du Dig Quest, de la formation à la dernière glaciation", "Quest.html", "Source : le Dig Quest de ce site"),
        ("6", "langues", "index.html", "Source : ce site"),
    ),
),
"es": dict(
    find_h="Encontrar un capítulo",
    shelf_a="La historia de la Tierra", shelf_b="en los estantes",
    shelf_lead="Dig Quest, el mapa de fósiles, los dinosaurios y el tiempo profundo. Cada estante abre una parte del archivo.",
    journey_a="El", journey_b="viaje",
    journey_lead="La historia larga está en este estante: un mundo fundido, los primeros océanos, los mapas medidos y por qué existe esta biblioteca.",
    journey_credit="Lava y primeros océanos: creado por el fundador y SI, una interpretación artística, no una fotografía. Desde hace 540 millones de años: Scotese PALEOMAP vía GPlates (EarthByte). La última foto es un estromatolito fósil en el Parque Nacional de los Glaciares (National Park Service, dominio público).",
    start_h="Empieza aquí",
    numbers_h="Del archivo",
    numbers_note="Cuentas de este sitio. La edad de la Tierra es la cifra del Servicio Geológico de EE. UU. que usa el Dig Quest.",
    cap0="Encélado: chorros de hielo de agua sobre un océano escondido. Las edades de hielo de la Tierra son una parada del Dig Quest.",
    cap1="La Luna con cráteres, vista desde la órbita. El impacto que la formó abre el Dig Quest.",
    q_cta="Empieza el Dig Quest",
    dig_links=("Ocho capas", "Continentes", "Océanos", "Mares", "El mar Muerto"),
    dino_more="Más dinosaurios",
    aud=(
        ("🦕", "Dig Quest", "Ocho capas, de la formación de la Tierra a la última glaciación.", "Quest.html"),
        ("🗺️", "Mapa de fósiles", "Fichas de yacimientos, bosques, arrecifes y archivos del tiempo profundo.", "World_Map.html"),
        ("🧒", "Niños", "Páginas de la Tierra y los fósiles para niños.", "Kids.html"),
        ("🎓", "Docentes", "Páginas de aula sobre fósiles y tiempo profundo.", "Teachers.html"),
        ("📚", "Aprender", "Lecciones sobre fósiles, climas y tiempo profundo.", "Learn.html"),
        ("🌙", "Acerca de", "Por qué esta biblioteca está junto a Saving Planets.", "About.html"),
    ),
    nums=(
        ("4540 millones", "de años: la edad de la Tierra en el Dig Quest", "Quest.html", 'Fuente: <a href="https://pubs.usgs.gov/gip/geotime/age.html">U.S. Geological Survey</a>'),
        ("82", "yacimientos se abren como fichas", "World_Map.html", "Fuente: el mapa mundial de este sitio"),
        ("8", "capas del Dig Quest, de la formación a la última glaciación", "Quest.html", "Fuente: el Dig Quest de este sitio"),
        ("6", "idiomas", "index.html", "Fuente: este sitio"),
    ),
),
"ar": dict(
    find_h="ابحث عن فصل",
    shelf_a="قصة الأرض", shelf_b="على الرفوف",
    shelf_lead="Dig Quest، وخريطة الأحافير، والديناصورات، والزمن العميق. كل رف يفتح جزءًا من السجل.",
    journey_a="الرحلة", journey_b="",
    journey_lead="القصة الطويلة على هذا الرف: عالم منصهر، والمحيطات الأولى، والخرائط المقاسة، وسبب وجود هذه المكتبة.",
    journey_credit="الحمم والمحيطات الأولى: من إعداد المؤسس وSI، تفسير فنّي وليس صورة فوتوغرافية. من 540 مليون سنة: Scotese PALEOMAP عبر GPlates (EarthByte). الصورة الأخيرة ستروماتوليت أحفوري في منتزه غلاسير الوطني (National Park Service، ملكية عامة).",
    start_h="ابدأ هنا",
    numbers_h="من السجل",
    numbers_note="أرقام هذا الموقع. عمر الأرض هو رقم هيئة المسح الجيولوجي الأمريكية المستخدم في Dig Quest.",
    cap0="إنسيلادوس: نافورات من جليد الماء فوق محيط مخفي. العصور الجليدية للأرض محطة في Dig Quest.",
    cap1="القمر ذو الفوهات، من المدار. الاصطدام الذي كوّنه يفتتح Dig Quest.",
    q_cta="ابدأ Dig Quest",
    dig_links=("ثماني طبقات", "القارات", "المحيطات", "البحار", "البحر الميت"),
    dino_more="مزيد من الديناصورات",
    aud=(
        ("🦕", "Dig Quest", "ثماني طبقات، من تكوّن الأرض إلى آخر عصر جليدي.", "Quest.html"),
        ("🗺️", "خريطة الأحافير", "بطاقات للمواقع والغابات والشعاب وأرشيف الزمن العميق.", "World_Map.html"),
        ("🧒", "الأطفال", "صفحات عن الأرض والأحافير للأطفال.", "Kids.html"),
        ("🎓", "المعلمون", "صفحات صفية عن الأحافير والزمن العميق.", "Teachers.html"),
        ("📚", "تعلّم", "دروس عن الأحافير والمناخات والزمن العميق.", "Learn.html"),
        ("🌙", "من نحن", "لماذا تقف هذه المكتبة إلى جانب Saving Planets.", "About.html"),
    ),
    nums=(
        ("4.54 مليار", "سنة: عمر الأرض في Dig Quest", "Quest.html", 'المصدر: <a href="https://pubs.usgs.gov/gip/geotime/age.html">U.S. Geological Survey</a>'),
        ("82", "موقع أحافير يُفتح كبطاقة", "World_Map.html", "المصدر: خريطة العالم في هذا الموقع"),
        ("8", "طبقات في Dig Quest، من التكوّن إلى آخر عصر جليدي", "Quest.html", "المصدر: Dig Quest في هذا الموقع"),
        ("6", "لغات", "index.html", "المصدر: هذا الموقع"),
    ),
),
"it": dict(
    find_h="Trova un capitolo",
    shelf_a="La storia della Terra", shelf_b="sugli scaffali",
    shelf_lead="Dig Quest, la mappa dei fossili, i dinosauri e il tempo profondo. Ogni scaffale apre una parte dell’archivio.",
    journey_a="Il", journey_b="viaggio",
    journey_lead="La storia lunga sta su questo scaffale: un mondo fuso, i primi oceani, le mappe misurate e perché esiste questa biblioteca.",
    journey_credit="Lava e primi oceani: creato dal fondatore e da SI, un’interpretazione artistica, non una fotografia. Da 540 milioni di anni: Scotese PALEOMAP tramite GPlates (EarthByte). L’ultima foto è una stromatolite fossile nel Glacier National Park (National Park Service, pubblico dominio).",
    start_h="Inizia qui",
    numbers_h="Dall’archivio",
    numbers_note="Conteggi di questo sito. L’età della Terra è la cifra dello U.S. Geological Survey usata nel Dig Quest.",
    cap0="Encelado: getti di ghiaccio d’acqua sopra un oceano nascosto. Le ere glaciali della Terra sono una tappa del Dig Quest.",
    cap1="La Luna craterizzata, vista dall’orbita. L’impatto che l’ha formata apre il Dig Quest.",
    q_cta="Inizia il Dig Quest",
    dig_links=("Otto strati", "Continenti", "Oceani", "Mari", "Il mar Morto"),
    dino_more="Altri dinosauri",
    aud=(
        ("🦕", "Dig Quest", "Otto strati, dalla formazione della Terra all’ultima glaciazione.", "Quest.html"),
        ("🗺️", "Mappa dei fossili", "Schede di siti, foreste, barriere e archivi del tempo profondo.", "World_Map.html"),
        ("🧒", "Bambini", "Pagine sulla Terra e sui fossili per bambini.", "Kids.html"),
        ("🎓", "Insegnanti", "Pagine per la classe su fossili e tempo profondo.", "Teachers.html"),
        ("📚", "Impara", "Lezioni su fossili, climi e tempo profondo.", "Learn.html"),
        ("🌙", "Chi siamo", "Perché questa biblioteca sta accanto a Saving Planets.", "About.html"),
    ),
    nums=(
        ("4,54 miliardi", "di anni: l’età della Terra nel Dig Quest", "Quest.html", 'Fonte: <a href="https://pubs.usgs.gov/gip/geotime/age.html">U.S. Geological Survey</a>'),
        ("82", "siti fossili si aprono come schede", "World_Map.html", "Fonte: la mappa del mondo di questo sito"),
        ("8", "strati del Dig Quest, dalla formazione all’ultima glaciazione", "Quest.html", "Fonte: il Dig Quest di questo sito"),
        ("6", "lingue", "index.html", "Fonte: questo sito"),
    ),
),
"he": dict(
    find_h="מצאו פרק",
    shelf_a="סיפור כדור הארץ", shelf_b="על המדפים",
    shelf_lead="Dig Quest, מפת המאובנים, הדינוזאורים והזמן העמוק. כל מדף פותח חלק מהארכיון.",
    journey_a="המסע", journey_b="",
    journey_lead="הסיפור הארוך יושב על המדף הזה: עולם מותך, האוקיינוסים הראשונים, המפות המדודות, ולמה הספרייה הזו קיימת.",
    journey_credit="לבה והאוקיינוסים הראשונים: נוצר על ידי המייסד ו-SI, פרשנות אמנותית, לא צילום. מ-540 מיליון שנה: Scotese PALEOMAP דרך GPlates (EarthByte). התצלום האחרון הוא סטרומטוליט מאובן בפארק הלאומי גליישר (National Park Service, נחלת הכלל).",
    start_h="התחילו כאן",
    numbers_h="מן התיעוד",
    numbers_note="המספרים באתר הזה. גיל כדור הארץ הוא הנתון של הסקר הגאולוגי של ארצות הברית שב-Dig Quest.",
    cap0="אנסלדוס: סילוני קרח מים מעל אוקיינוס נסתר. עידני הקרח של כדור הארץ הם תחנה ב-Dig Quest.",
    cap1="הירח המכתשי, ממסלול. ההתנגשות שיצרה אותו פותחת את ה-Dig Quest.",
    q_cta="התחילו את Dig Quest",
    dig_links=("שמונה שכבות", "יבשות", "אוקיינוסים", "ימים", "ים המלח"),
    dino_more="עוד דינוזאורים",
    aud=(
        ("🦕", "Dig Quest", "שמונה שכבות, מהיווצרות כדור הארץ עד עידן הקרח האחרון.", "Quest.html"),
        ("🗺️", "מפת מאובנים", "כרטיסים לאתרים, ליערות, לשוניות ולארכיוני זמן עמוק.", "World_Map.html"),
        ("🧒", "ילדים", "דפים על כדור הארץ ועל מאובנים לילדים.", "Kids.html"),
        ("🎓", "מורים", "דפי כיתה על מאובנים וזמן עמוק.", "Teachers.html"),
        ("📚", "למידה", "שיעורים על מאובנים, אקלים וזמן עמוק.", "Learn.html"),
        ("🌙", "אודות", "למה הספרייה הזו יושבת לצד Saving Planets.", "About.html"),
    ),
    nums=(
        ("4.54 מיליארד", "שנים: גיל כדור הארץ ב-Dig Quest", "Quest.html", 'מקור: <a href="https://pubs.usgs.gov/gip/geotime/age.html">U.S. Geological Survey</a>'),
        ("82", "אתרי מאובנים נפתחים ככרטיסים", "World_Map.html", "מקור: מפת העולם באתר הזה"),
        ("8", "שכבות ב-Dig Quest, מההיווצרות עד עידן הקרח האחרון", "Quest.html", "מקור: Dig Quest באתר הזה"),
        ("6", "שפות", "index.html", "מקור: האתר הזה"),
    ),
),
}


def e(text):
    return html.escape(text, quote=True)


def _links(items):
    return "".join(f'<li><a href="{e(href)}">{e(label)}</a></li>' for label, href in items)


def _card(r, href, src, w, h, alt, credit, title, links):
    return (
        f'<article class="card"><div class="image-container"><a class="photo-link" href="{e(href)}">'
        f'<img src="{r}{src}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></a></div>'
        f'<p class="photo-credit">{e(credit)}</p><h3><a href="{e(href)}">{e(title)}</a></h3>'
        f'<ul class="solution-list">{_links(links)}</ul></article>'
    )


def _chips(label, items):
    bits = "".join(f'<a class="dom-chip" href="{e(href)}">{e(name)}</a>' for name, href in items)
    return f'<p class="hf-row"><span class="hf-lab">{e(label)}</span>{bits}</p>'


def home_main(lang, t):
    L = LIB[lang]
    r = "" if lang == "en" else "../"
    X_learn, X_kids, X_teachers, X_myth = None, None, None, None
    # EXTRA order is myth, learn, kids, teachers — passed by the caller via t only.
    # Labels that already live on the nav are read from t and the imported nav maps.
    g = GLOBE[lang]
    deep = DEEP_NAV[lang]
    dinos = DINO_NAV[lang]
    dig_names = L["dig_links"]
    dig_hrefs = ("Quest.html", "Continents.html", "Oceans.html", "Seas.html", "DeadSea.html")
    q_cta = L["q_cta"]

    vision_h = {"en": "Vision", "fr": "Vision", "es": "Visión", "ar": "الرؤية", "it": "Visione", "he": "חזון"}[lang]
    dig_lab = {"en": "Dig", "fr": "Fouille", "es": "Excavar", "ar": "تنقيب", "it": "Scavo", "he": "חפירה"}[lang]
    hero = f'''<section class="hero space-hero has-video bsp-film" aria-labelledby="bsp-h1"><div class="hero-media" aria-hidden="true"><video class="hero-video" muted loop playsinline autoplay preload="auto" poster="{POSTER}" width="1280" height="546"><source src="{FILM}" type="video/mp4"></video><div class="hero-overlay"></div></div><p class="hero-video-credit">Created by the Founder and SI.</p><div class="hero-content"><p class="hero-kicker">{e(t["kicker"])}</p><h1 id="bsp-h1" class="hero-welcome"><span class="bsp-line">{e(t["h1a"])}</span> <span class="bsp-line welcome-brand">{e(t["h1b"])}</span></h1><p class="hero-example">{e(t["sub"])}</p><p class="hero-ctas"><a class="btn hero-cta" href="Quest.html">{e(q_cta)}</a><a class="btn hero-cta2" href="World_Map.html">{e(t["cta1"])}</a></p></div><button type="button" class="bsp-pause" aria-pressed="false" data-play="{e(PLAY[lang])}">{e(t["pause"])}</button></section>'''

    vision = f'''<section class="home-vision" id="vision" aria-labelledby="vision-h"><h2 id="vision-h">{e(vision_h)}</h2><p class="hv-p">{e(t["hook"])}</p><p class="hv-p">{e(L["shelf_lead"])}</p><p class="hv-chips"><a class="hv-chip hv-chip-ext" href="Quest.html">{e(q_cta)}</a><a class="hv-chip" href="World_Map.html">{e(t["cta1"])}</a><a class="hv-chip" href="https://www.savingplanets.com/">{e(t["cta2"])}</a></p></section>'''

    find = f'''<section class="home-find" id="find" aria-labelledby="find-h"><h2 id="find-h">{e(L["find_h"])}</h2><form role="search" action="Search.html" method="get"><label for="hf-q" class="visually-hidden">{e(t["search"])}</label><input id="hf-q" name="q" type="search" enterkeyhint="search" placeholder="{e(t["search"])}"><button type="submit">{e(t["search"])}</button></form>{_chips(dig_lab, ((q_cta, "Quest.html"), (g["scrub"], "Quest.html#time-scrubber"), (deep, "Deep_Time.html")))}{_chips(t["map"], ((t["map"], "World_Map.html"), (t["kids"], "Kids_Map.html"), ("Smilodon", "Smilodon.html"), (dinos, "Dinosaurs.html")))}</section>'''

    # Learn row is filled by the caller labels. Rebuilt below so EXTRA names stay in one place.
    return hero, vision, find, L, r, q_cta, dig_names, dig_hrefs, deep, dinos


def render_home(lang, t, extra):
    """extra is EXTRA[lang]: myth, learn, kids, teachers, ..."""
    hero, vision, find, L, r, q_cta, dig_names, dig_hrefs, deep, dinos = home_main(lang, t)
    myth, learn, kids, teachers = extra[0], extra[1], extra[2], extra[3]
    g = GLOBE[lang]
    learn_row = _chips(learn, (
        (learn, "Learn.html"), (kids, "Kids.html"), (teachers, "Teachers.html"),
        (myth, "Myth_vs_Fact.html"), (t["kids"], "Kids_Map.html"),
    ))
    # home_main closed the find section before the learn row. Reopen by replacing the end.
    find = find.replace("</section>", learn_row + f'<p class="wm-cta"><a class="btn hero-cta" href="World_Map.html">{e(t["cta1"])}</a></p></section>')

    dig_items = (
        (q_cta, "Quest.html"),
        (g["scrub"], "Quest.html#time-scrubber"),
        (dig_names[1], "Continents.html"),
        (dig_names[2], "Oceans.html"),
        (dig_names[3], "Seas.html"),
        (dig_names[4], "DeadSea.html"),
    )
    cards = [
        _card(r, "Quest.html", "assets/quest/layer-burgess.webp", 1280, 960,
              "Anomalocaris canadensis from the Burgess Shale",
              "Esv, CC BY-SA 3.0, via Wikimedia Commons",
              "Dig Quest", dig_items),
        _card(r, "World_Map.html", "assets/deeptime/waco-mammoths-1600.webp", 1600, 1067,
              "Columbian mammoth bones at Waco Mammoth National Monument",
              "Larry D. Moore, CC BY 4.0, via Wikimedia Commons",
              t["map"], ((t["map"], "World_Map.html"), (t["kids"], "Kids_Map.html"), ("Smilodon", "Smilodon.html"))),
        _card(r, "Dinosaurs.html", "assets/finds/borealopelta-1600.webp", 1600, 1208,
              "Borealopelta fossil at the Royal Tyrrell Museum",
              "Chris Woodrich, CC BY-SA 4.0, via Wikimedia Commons",
              dinos, ((dinos, "Dinosaurs.html"), ("Borealopelta", "Borealopelta.html"),
                      ("Triceratops", "Triceratops.html"), ("Stegosaurus", "Stegosaurus.html"),
                      ("Nigersaurus", "Nigersaurus.html"))),
        _card(r, "Smilodon.html", "assets/smilodon/hero-1600.webp", 1600, 1200,
              "Smilodon fatalis skeleton at the La Brea Tar Pits Museum",
              "TheUltimateGrass, CC0, via Wikimedia Commons",
              "Smilodon", (("Smilodon", "Smilodon.html"),)),
        _card(r, "Deep_Time.html", "assets/quest/layer-jack-hills.webp", 1400, 1001,
              "Jack Hills host rock, Western Australia",
              "James St. John, CC BY 2.0, via Wikimedia Commons",
              deep, ((deep, "Deep_Time.html"), (g["scrub"], "Quest.html#time-scrubber"))),
    ]
    shelf = (
        f'<section class="card-band" id="shelves" aria-labelledby="shelf-h">'
        f'<h2 id="shelf-h"><span class="brand-blue">{e(L["shelf_a"])}</span> {e(L["shelf_b"])}</h2>'
        f'<p class="home-lead">{e(L["shelf_lead"])}</p><div class="grid">{"".join(cards)}</div></section>'
    )

    journey_cards = []
    for era in STORY[lang]:
        src, w, h = STILLS[era["still"]]
        if era["still"] in ("start.webp", "era-oceans.webp"):
            credit = "Created by the Founder and SI"
        elif era["still"] == "era-today.webp":
            credit = "National Park Service, public domain"
        else:
            credit = "Scotese PALEOMAP via GPlates (EarthByte)"
        links = ""
        if era["why"]:
            links = _links(((q_cta, "Quest.html"), (g["scrub"], "Quest.html#time-scrubber"), (t["cta2"], "https://www.savingplanets.com/")))
            links = f'<ul class="solution-list">{links}</ul>'
        journey_cards.append(
            f'<article class="card"{" id=\"why-bsp\"" if era["why"] else ""}>'
            f'<div class="image-container"><img src="{r}{src}" alt="{e(era["h"])}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>'
            f'<p class="photo-credit">{e(credit)}</p><p class="bsp-era-k">{e(era["k"])}</p>'
            f'<h3>{e(era["h"])}</h3><p class="card-blurb">{e(era["p"])}</p>{links}</article>'
        )
    journey = (
        f'<section class="card-band" id="journey" aria-labelledby="journey-h">'
        f'<h2 id="journey-h"><span class="brand-blue">{e(L["journey_a"])}</span> {e(L["journey_b"])}</h2>'
        f'<p class="home-lead">{e(L["journey_lead"])}</p><div class="grid">{"".join(journey_cards)}</div>'
        f'<p class="journey-credit">{e(L["journey_credit"])}</p></section>'
    )

    aud = "".join(
        f'<a class="aud-card" href="{e(href)}"><span class="aud-icon" aria-hidden="true">{icon}</span>'
        f'<span class="aud-title">{e(title)}</span><span class="aud-text">{e(text)}</span></a>'
        for icon, title, text, href in L["aud"]
    )
    # Audience titles for kids/teachers/learn/about should follow the nav language.
    # The tuples above are already translated per language.
    start = f'<section class="audience" id="start" aria-labelledby="start-h"><h2 id="start-h">{e(L["start_h"])}</h2><div class="aud-grid">{aud}</div></section>'

    nums = "".join(
        f'<li class="hn-item"><span class="hn-num">{e(num)}</span><a class="hn-label" href="{e(href)}">{e(label)}</a><span class="hn-src">{src}</span></li>'
        for num, label, href, src in L["nums"]
    )
    numbers = (
        f'<section class="home-numbers" aria-labelledby="hn-h"><h2 id="hn-h">{e(L["numbers_h"])}</h2>'
        f'<ul class="hn-list">{nums}</ul><p class="hn-note">{e(L["numbers_note"])}</p></section>'
    )
    # hn src contains trusted anchors written in this file. Escape would break them.
    # Guard: only the four source strings above are interpolated raw.
    return f'<main id="main">{hero}{vision}{find}{shelf}{journey}{start}{numbers}</main>'
