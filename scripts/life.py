# Life over Time shelves. The four menu labels are Dinosaurs (existing hub),
# Mammals, Aerial, and Marine. These three shelves do not invent animals.
# Each card is a life entry already tagged on the deep-time map, with that
# entry's sentence, picture, and source. Dinosaurs.html and Deep_Time.html
# stay the homes they already are.
import html, json, os
from urllib.parse import quote

from finds import DEEP_NAV, FIND_SLUGS, NAV as DINO_NAV

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIFE_NAV = {
    "en": "Life over Time",
    "fr": "La vie dans le temps",
    "es": "Vida en el tiempo",
    "ar": "الحياة عبر الزمن",
    "it": "La vita nel tempo",
    "he": "החיים לאורך הזמן",
}
SHELF_NAV = {
    "Mammals": {"en": "Mammals", "fr": "Mammifères", "es": "Mamíferos", "ar": "ثدييات", "it": "Mammiferi", "he": "יונקים"},
    "Aerial": {"en": "Aerial", "fr": "Aérien", "es": "Aéreo", "ar": "جوّي", "it": "Aereo", "he": "אווירי"},
    "Marine": {"en": "Marine", "fr": "Vie marine", "es": "Vida marina", "ar": "حياة بحرية", "it": "Vita marina", "he": "חיים בים"},
}
GROUP = {"Mammals": "mammals", "Aerial": "flying", "Marine": "marine"}
# Deep-time chip name, so the shelf and the map use the same word.
# The deep-time chips are French only when the page is French. Every other
# language shows the English chip, so the sentence has to name that word.
CHIP = {
    "Mammals": {"en": "Mammals", "fr": "Mammifères"},
    "Aerial": {"en": "Flying", "fr": "En vol"},
    "Marine": {"en": "Marine life", "fr": "Vie marine"},
}
# Page title (before the brand suffix) and meta description. Descriptions stay
# under 155 characters and are not an English copy on the other languages.
META = {
    "Mammals": {
        "en": ("Mammals", "Mammal finds already on this site, including the written Smilodon page and the deep-time map."),
        "fr": ("Mammifères", "Les mammifères déjà sur ce site, dont la page écrite de Smilodon et la carte du temps profond."),
        "es": ("Mamíferos", "Mamíferos que ya están en este sitio, incluida la página escrita de Smilodon y el mapa del tiempo profundo."),
        "ar": ("ثدييات", "ثدييات موجودة أصلًا في هذا الموقع، ومنها صفحة Smilodon المكتوبة وخريطة الزمن العميق."),
        "it": ("Mammiferi", "Mammiferi già presenti su questo sito, inclusa la pagina scritta di Smilodon e la mappa del tempo profondo."),
        "he": ("יונקים", "ממצאי יונקים שכבר נמצאים באתר, כולל העמוד הכתוב של סמילודון ומפת הזמן העמוק."),
    },
    "Aerial": {
        "en": ("Aerial", "Animals already tagged Flying on the deep-time map, each card keeping that entry’s existing source."),
        "fr": ("Aérien", "Les animaux déjà marqués En vol sur la carte du temps profond, chaque fiche gardant sa source."),
        "es": ("Aéreo", "Animales ya marcados como voladores en el mapa del tiempo profundo, cada ficha con su fuente."),
        "ar": ("جوّي", "حيوانات موسومة أصلًا بالطيران على خريطة الزمن العميق، وكل بطاقة تحتفظ بمصدرها."),
        "it": ("Aereo", "Animali già segnati In volo sulla mappa del tempo profondo, ogni scheda con la sua fonte."),
        "he": ("אווירי", "בעלי חיים שכבר מסומנים כמעופפים במפת הזמן העמוק, וכל כרטיס שומר את המקור שלו."),
    },
    "Marine": {
        "en": ("Marine", "Marine entries already on the deep-time map, each card keeping that entry’s existing source."),
        "fr": ("Vie marine", "Les entrées marines déjà sur la carte du temps profond, chaque fiche gardant sa source."),
        "es": ("Vida marina", "Entradas marinas que ya están en el mapa del tiempo profundo, cada ficha con su fuente."),
        "ar": ("حياة بحرية", "مدخلات بحرية موجودة أصلًا على خريطة الزمن العميق، وكل بطاقة تحتفظ بمصدرها."),
        "it": ("Vita marina", "Voci marine già sulla mappa del tempo profondo, ogni scheda con la sua fonte."),
        "he": ("חיים בים", "רשומות ימיות שכבר נמצאות במפת הזמן העמוק, וכל כרטיס שומר את המקור שלו."),
    },
}
LEAD = {
    "Mammals": {
        "en": "The mammal finds already on this site. Smilodon has a full page. The other cards open the fossil coin or the source already used on the deep-time map.",
        "fr": "Les mammifères déjà sur ce site. Smilodon a une page complète. Les autres cartes ouvrent la pièce fossile ou la source déjà utilisée sur la carte du temps profond.",
        "es": "Los mamíferos que ya están en este sitio. Smilodon tiene una página completa. Las otras fichas abren la moneda fósil o la fuente que ya usa el mapa del tiempo profundo.",
        "ar": "الثدييات الموجودة أصلًا في هذا الموقع. لـ Smilodon صفحة كاملة. البطاقات الأخرى تفتح قطعة الأحفورة أو المصدر المستخدم أصلًا في خريطة الزمن العميق.",
        "it": "I mammiferi già presenti su questo sito. Smilodon ha una pagina intera. Le altre schede aprono la moneta fossile o la fonte già usata sulla mappa del tempo profondo.",
        "he": "ממצאי היונקים שכבר נמצאים באתר. לסמילודון יש עמוד מלא. שאר הכרטיסים נפתחים אל מטבע המאובן או אל המקור שכבר משמש במפת הזמן העמוק.",
    },
    "Aerial": {
        "en": "Animals already tagged Flying on the deep-time map. Argentavis, Haast’s eagle, Archaeopteryx, Pterodactylus, and Meganeura have full pages. Each card keeps that entry’s source.",
        "fr": "Animaux déjà marqués En vol sur la carte du temps profond. Argentavis, l’aigle de Haast, Archaeopteryx, Pterodactylus et Meganeura ont une page. Chaque fiche garde sa source.",
        "es": "Animales ya marcados como voladores en el mapa del tiempo profundo. Argentavis, el águila de Haast, Archaeopteryx, Pterodactylus y Meganeura tienen página. Cada ficha guarda su fuente.",
        "ar": "حيوانات موسومة أصلًا بالطيران على خريطة الزمن العميق. لأرجنتافيس ونسر هاست وأركيوبتركس وبتروداكتيلوس وميغانيورا صفحات. كل بطاقة تحتفظ بمصدرها.",
        "it": "Animali già segnati In volo sulla mappa del tempo profondo. Argentavis, l’aquila di Haast, Archaeopteryx, Pterodactylus e Meganeura hanno una pagina. Ogni scheda tiene la sua fonte.",
        "he": "בעלי חיים שכבר מסומנים כמעופפים במפת הזמן העמוק. לארגנטאביס, לעיט האסט, לארכאופטריקס, לפטרודקטילוס ולמגנאוריה יש עמוד. כל כרטיס שומר את המקור.",
    },
    "Marine": {
        "en": "Marine entries already on the deep-time map. Mosasaurus, Dunkleosteus, Otodus megalodon, and Plesiosaurus have full pages. The other cards open the coin or the source already used.",
        "fr": "Entrées marines déjà sur la carte du temps profond. Mosasaurus, Dunkleosteus, Otodus megalodon et Plesiosaurus ont une page. Les autres fiches ouvrent la pièce ou la source déjà utilisée.",
        "es": "Entradas marinas que ya están en el mapa del tiempo profundo. Mosasaurus, Dunkleosteus, Otodus megalodon y Plesiosaurus tienen página. Las otras fichas abren la moneda o la fuente ya usada.",
        "ar": "مدخلات بحرية موجودة أصلًا على خريطة الزمن العميق. لموساصور ودانكليوستيوس وأتودوس ميغالودون وبليسيوصور صفحات. البطاقات الأخرى تفتح القطعة أو المصدر المستخدم أصلًا.",
        "it": "Voci marine già sulla mappa del tempo profondo. Mosasaurus, Dunkleosteus, Otodus megalodon e Plesiosaurus hanno una pagina. Le altre schede aprono la moneta o la fonte già usata.",
        "he": "רשומות ימיות שכבר נמצאות במפת הזמן העמוק. למוזאזאורוס, לדונקליאוסטיוס, לאוטודוס מגלודון ולפלסיוזאורוס יש עמוד. שאר הכרטיסים נפתחים אל המטבע או אל המקור שכבר בשימוש.",
    },
}
CHIP_LINE = {
    "en": "Turn on the {chip} chip there to see this group move.",
    "fr": "Activez-y la puce {chip} pour voir ce groupe se déplacer.",
    "es": "Active allí la ficha {chip} para ver moverse a este grupo.",
    "ar": "فعّلوا هناك شريحة {chip} لتروا هذه المجموعة تتحرك.",
    "it": "Attivate lì il filtro {chip} per vedere questo gruppo muoversi.",
    "he": "הפעילו שם את המסנן {chip} כדי לראות את הקבוצה הזו נעה.",
}
FILE_LABEL = {"en": "File page", "fr": "Page du fichier", "es": "Página del archivo", "ar": "صفحة الملف", "it": "Pagina del file", "he": "עמוד הקובץ"}
LIFE_WORD = {"en": "Life restoration", "fr": "Reconstitution", "es": "Reconstrucción", "ar": "إعادة بناء", "it": "Ricostruzione", "he": "שחזור"}
FOSSIL_WORD = {"en": "Fossil", "fr": "Fossile", "es": "Fósil", "ar": "أحفورة", "it": "Fossile", "he": "מאובן"}
SOURCE_LABEL = {"en": "Source", "fr": "Source", "es": "Fuente", "ar": "المصدر", "it": "Fonte", "he": "מקור"}
NOTE = {
    "es": "Las frases de cada animal siguen en inglés, a la espera de una revisión.",
    "ar": "جمل كل حيوان ما زالت بالإنجليزية، بانتظار المراجعة.",
    "it": "Le frasi di ogni animale restano in inglese, in attesa di una revisione.",
    "he": "המשפטים על כל בעל חיים נשארו באנגלית, וממתינים לבדיקה.",
}

# Ichthyosaurus’s deep-time link is a Paleobiology Database JSON file, not a page.
# The same skull is already the Jurassic Coast coin on the world map.
PIN_OVERRIDE = {
    "Ichthyosaurus": "Jurassic Coast (Dorset & East Devon), UK",
}


def _readable(url):
    if not url:
        return False
    if "data1.2" in url or ".json" in url:
        return False
    return True


def _primary(item):
    pin = PIN_OVERRIDE.get(item.get("name"))
    if pin:
        return "World_Map.html?pin=" + quote(pin, safe="")
    href = item.get("href") or ""
    if _readable(href):
        return href
    # A second source can be a museum page. A JSON file is not a place to land.
    # Otherwise the animal already lives on the deep-time map.
    if _readable(item.get("sourceHref2")):
        return item["sourceHref2"]
    return "Deep_Time.html"


# Living animals with a sourced picture lead. Within that, the striking
# well-known ones come first. The rest stay in age order. No invented animals.
WOW = {
    "mammals": ["Smilodon", "Waco mammoths", "Nimbadon", "Lucy", "La Brea Tar Pits"],
    "flying": ["Argentavis", "Haast\u2019s eagle", "Archaeopteryx", "Pterodactylus", "Meganeura"],
    "marine": ["Mosasaurus", "Dunkleosteus", "Otodus megalodon", "Plesiosaurus", "Ichthyosaurus", "Anomalocaris"],
}

def _entries(group):
    path = os.path.join(ROOT, "assets", "data", "deep-time.json")
    pack = json.load(open(path, encoding="utf-8"))
    rows = [item for item in pack.get("life") or [] if group in (item.get("groups") or [])]
    wow = WOW.get(group, [])
    def rank(item):
        name = item.get("name") or ""
        life = 0 if item.get("lifeImg") else 1
        try:
            place = wow.index(name)
        except ValueError:
            place = 100
        return (life, place, -float(item.get("ma") or 0), name)
    rows.sort(key=rank)
    if not rows:
        raise SystemExit("life shelf has no deep-time entries: " + group)
    return rows


def _card(prefix, lang, item):
    fr = lang == "fr"
    name = item.get("nameFr") if fr and item.get("nameFr") else item.get("name") or ""
    blurb = item.get("blurbFr") if fr and item.get("blurbFr") else item.get("blurb") or ""
    credit = item.get("imageCreditFr") if fr and item.get("imageCreditFr") else item.get("imageCredit") or ""
    foreign = ' lang="en"' if lang not in ("en", "fr") else ""
    if not blurb or not item.get("img") or not item.get("sourceHref"):
        raise SystemExit("life shelf entry is missing a blurb, image, or source: " + name)
    webp = item.get("imgSm") or item["img"]
    avif = item.get("imgAvifSm") or item.get("imgAvif")
    life_webp = item.get("lifeImg") or ""
    life_avif = item.get("lifeImgAvif") or ""
    life_sm = item.get("lifeImgSm") or ""
    for rel in (webp, avif, life_webp, life_avif, life_sm):
        if rel and not os.path.isfile(os.path.join(ROOT, rel)):
            raise SystemExit("life shelf image missing: " + rel)
    w = int(item.get("picSmW") or item.get("picW") or 800)
    h = int(item.get("picH") or 600)

    def one(rel_webp, rel_avif, iw, ih, alt, srcset=""):
        src = html.escape(prefix + rel_webp, quote=True)
        tag = ""
        if rel_avif:
            tag += f'<source type="image/avif" srcset="{html.escape(prefix + rel_avif, quote=True)}">'
        extra = f" {srcset}" if srcset else ""
        tag += f'<img src="{src}" width="{iw}" height="{ih}" alt="{html.escape(alt)}"{extra} loading="lazy" decoding="async">'
        return f"<picture>{tag}</picture>"

    fossil_alt = item.get("imgAlt") or name
    if life_webp:
        lw, lh = int(item.get("lifeW") or 1080), int(item.get("lifeH") or 720)
        srcset = ""
        if life_sm and item.get("lifeSmW"):
            srcset = (
                f'srcset="{html.escape(prefix + life_sm, quote=True)} {int(item["lifeSmW"])}w, '
                f'{html.escape(prefix + life_webp, quote=True)} {lw}w" sizes="(max-width: 700px) 70vw, 280px"'
            )
        picture = (
            f'<span class="find-pair">{one(life_webp, life_avif, lw, lh, item.get("lifeAlt") or name, srcset)}'
            f'{one(webp, avif, w, h, item.get("imgAlt") or (FOSSIL_WORD[lang] + ": " + name))}</span>'
        )
    else:
        picture = one(webp, avif, w, h, fossil_alt)
    dest = _primary(item)
    if not dest:
        raise SystemExit("life shelf entry has nowhere to go: " + name)
    rel = ' rel="noopener noreferrer"' if dest.startswith("http") else ""
    links = []
    if life_webp and item.get("lifeHref"):
        life_credit = item.get("lifeCreditFr") if fr and item.get("lifeCreditFr") else item.get("lifeCredit") or ""
        links.append(
            f'{html.escape(LIFE_WORD[lang])}. {html.escape(life_credit)} '
            f'<a href="{html.escape(item["lifeHref"], quote=True)}" rel="noopener noreferrer">{html.escape(FILE_LABEL[lang])}</a>'
        )
    file_href = item.get("imageHref")
    if file_href:
        fossil_bit = (html.escape(FOSSIL_WORD[lang]) + ". ") if life_webp else ""
        links.append(
            f'{fossil_bit}{html.escape(credit)} '
            f'<a href="{html.escape(file_href, quote=True)}" rel="noopener noreferrer">{html.escape(FILE_LABEL[lang])}</a>'
        )
    seen = set()
    for key, label_key in (("sourceHref", "source"), ("sourceHref2", "source2")):
        href = item.get(key)
        if not href or href in seen:
            continue
        seen.add(href)
        label = item.get(label_key + "Fr") if fr and item.get(label_key + "Fr") else item.get(label_key) or SOURCE_LABEL[lang]
        links.append(
            f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(SOURCE_LABEL[lang])}: {html.escape(label)}</a>'
        )
    lead_credit = "" if (life_webp or file_href) else html.escape(credit)
    sep = " · " if lead_credit and links else ""
    return (
        f'<article class="find-card"><a class="find-go" href="{html.escape(dest, quote=True)}"{rel}>'
        f'{picture}<h3>{html.escape(name)}</h3><p{foreign}>{html.escape(blurb)}</p></a>'
        f'<p class="find-credit"{foreign}>{lead_credit}{sep}{" · ".join(links)}</p></article>'
    )


def life_page(slug, lang, prefix=""):
    if slug not in GROUP:
        raise SystemExit("unknown life shelf: " + slug)
    title, desc = META[slug][lang]
    h1 = SHELF_NAV[slug][lang]
    lead = LEAD[slug][lang]
    kicker = LIFE_NAV[lang]
    note = ""
    if lang not in ("en", "fr"):
        note = f'<p class="sm-note" role="note">{html.escape(NOTE[lang])}</p>'
    cards = "".join(_card(prefix, lang, item) for item in _entries(GROUP[slug]))
    chip_name = CHIP[slug]["fr"] if lang == "fr" else CHIP[slug]["en"]
    chip = CHIP_LINE[lang].format(chip=html.escape(chip_name))
    others = []
    for other, labels in (("Dinosaurs.html", DINO_NAV), ("Mammals.html", SHELF_NAV["Mammals"]), ("Aerial.html", SHELF_NAV["Aerial"]), ("Marine.html", SHELF_NAV["Marine"]), ("Deep_Time.html", DEEP_NAV)):
        if other == slug + ".html":
            continue
        others.append(f'<a href="{other}">{html.escape(labels[lang])}</a>')
    main = (
        f'<main id="main"><section class="sm-hero life-hero"><div class="sm-hero-shade" aria-hidden="true"></div>'
        f'<div class="sm-hero-copy"><p class="sm-kicker">{html.escape(kicker)}</p><h1>{html.escape(h1)}</h1>'
        f'<p class="sm-lead">{html.escape(lead)}</p></div></section>'
        f'<div class="sm-wrap">{note}'
        f'<p><a href="Deep_Time.html">{html.escape(DEEP_NAV[lang])}</a>. {chip}</p>'
        f'<div class="find-grid">{cards}</div>'
        f'<p class="find-back">{" · ".join(others)}</p></div></main>'
    )
    return title, desc, main
