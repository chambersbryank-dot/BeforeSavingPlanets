#!/usr/bin/env python3
"""Dig Quest rebuild. Bright discovery page, Smilodon hero pattern, six languages.

Years are written out. The bare acronym Ma is refused.
Page experience: Created by the Founder and SI.
"""
import html, re
from quest_diet import DIET

EARTH = 4.54e9
CAMBRIAN = 539e6
PERM_END = 251.902e6
CRET_END = 66e6

PERIODS = [
    ("precambrian", [
        ("hadean", 4.54e9, 4e9),
        ("archean", 4e9, 2.5e9),
        ("proterozoic", 2.5e9, 539e6),
    ], 0),
    ("paleozoic", [
        ("cambrian", 539e6, 486.85e6),
        ("ordovician", 486.85e6, 443.1e6),
        ("silurian", 443.1e6, 419.62e6),
        ("devonian", 419.62e6, 358.86e6),
        ("carboniferous", 358.86e6, 298.9e6),
        ("permian", 298.9e6, 251.902e6),
    ], 1),
    ("mesozoic", [
        ("triassic", 251.902e6, 201.4e6),
        ("jurassic", 201.4e6, 143.1e6),
        ("cretaceous", 143.1e6, 66e6),
    ], 2),
    ("cenozoic", [
        ("paleogene", 66e6, 23.04e6),
        ("neogene", 23.04e6, 2.58e6),
        ("quaternary", 2.58e6, 0),
    ], 3),
]

# Durations used for the proportional bar. Sum is Earth's age on this page.
DURS = [EARTH - CAMBRIAN, CAMBRIAN - PERM_END, PERM_END - CRET_END, CRET_END]

NAMES = {
"en": dict(precambrian="Precambrian", paleozoic="Paleozoic", mesozoic="Mesozoic", cenozoic="Cenozoic",
    hadean="Hadean", archean="Archean", proterozoic="Proterozoic",
    cambrian="Cambrian", ordovician="Ordovician", silurian="Silurian", devonian="Devonian",
    carboniferous="Carboniferous", permian="Permian", triassic="Triassic", jurassic="Jurassic",
    cretaceous="Cretaceous", paleogene="Paleogene", neogene="Neogene", quaternary="Quaternary"),
"fr": dict(precambrian="Précambrien", paleozoic="Paléozoïque", mesozoic="Mésozoïque", cenozoic="Cénozoïque",
    hadean="Hadéen", archean="Archéen", proterozoic="Protérozoïque",
    cambrian="Cambrien", ordovician="Ordovicien", silurian="Silurien", devonian="Dévonien",
    carboniferous="Carbonifère", permian="Permien", triassic="Trias", jurassic="Jurassique",
    cretaceous="Crétacé", paleogene="Paléogène", neogene="Néogène", quaternary="Quaternaire"),
"es": dict(precambrian="Precámbrico", paleozoic="Paleozoico", mesozoic="Mesozoico", cenozoic="Cenozoico",
    hadean="Hádico", archean="Arcaico", proterozoic="Proterozoico",
    cambrian="Cámbrico", ordovician="Ordovícico", silurian="Silúrico", devonian="Devónico",
    carboniferous="Carbonífero", permian="Pérmico", triassic="Triásico", jurassic="Jurásico",
    cretaceous="Cretácico", paleogene="Paleógeno", neogene="Neógeno", quaternary="Cuaternario"),
"it": dict(precambrian="Precambriano", paleozoic="Paleozoico", mesozoic="Mesozoico", cenozoic="Cenozoico",
    hadean="Adeano", archean="Archeano", proterozoic="Proterozoico",
    cambrian="Cambriano", ordovician="Ordoviciano", silurian="Siluriano", devonian="Devoniano",
    carboniferous="Carbonifero", permian="Permiano", triassic="Triassico", jurassic="Giurassico",
    cretaceous="Cretaceo", paleogene="Paleogene", neogene="Neogene", quaternary="Quaternario"),
"ar": dict(precambrian="ما قبل الكمبري", paleozoic="الباليوزوي", mesozoic="الميزوزوي", cenozoic="السينوزوي",
    hadean="الهادي", archean="الأركي", proterozoic="البروتيروزوي",
    cambrian="الكمبري", ordovician="الأوردوفيشي", silurian="السيلوري", devonian="الديفوني",
    carboniferous="الكربوني", permian="البرمي", triassic="الترياسي", jurassic="الجوراسي",
    cretaceous="الطباشيري", paleogene="الباليوجين", neogene="النيوجين", quaternary="الرباعي"),
"he": dict(precambrian="פרקמבריון", paleozoic="פלאוזואיקון", mesozoic="מזוזואיקון", cenozoic="קנוזואיקון",
    hadean="האדן", archean="ארכאיקון", proterozoic="פרוטרוזואיקון",
    cambrian="קמבריון", ordovician="אורדוביק", silurian="סילור", devonian="דבון",
    carboniferous="קרבון", permian="פרם", triassic="טריאס", jurassic="יורה",
    cretaceous="קרטיקון", paleogene="פלאוגן", neogene="נאוגן", quaternary="רביעון"),
}

def _round_m(years):
    n = years / 1e6
    x = int(n * 10 + 0.5) / 10.0
    if abs(x - round(x)) < 0.051:
        return float(int(round(x)))
    return x

def _billions(years):
    n = years / 1e9
    return f"{n:.3f}".rstrip("0").rstrip(".")

def phrase(lang, years):
    years = float(years)
    if years >= 1e9 - 1:
        b = _billions(years)
        if lang == "en":
            return b + " billion years ago"
        if lang == "fr":
            word = "milliard" if abs(float(b) - 1) < 0.01 else "milliards"
            return "il y a " + b.replace(".", ",") + " " + word + " d’années"
        if lang == "es":
            millions = int(round(float(b) * 1000))
            s = f"{millions // 1000}.{millions % 1000:03d}"
            return "hace " + s + " millones de años"
        if lang == "it":
            word = "miliardo" if abs(float(b) - 1) < 0.01 else "miliardi"
            return b.replace(".", ",") + " " + word + " di anni fa"
        if lang == "ar":
            return "قبل " + b + " مليار سنة"
        if lang == "he":
            return "לפני " + b + " מיליארד שנים"
    if years >= 1e6 - 1:
        n = _round_m(years)
        if abs(n - round(n)) < 0.051:
            s = str(int(round(n)))
        else:
            s = f"{n:.1f}"
        if lang == "en":
            return s + " million years ago"
        if lang == "fr":
            return "il y a " + s.replace(".", ",") + " millions d’années"
        if lang == "es":
            return "hace " + s.replace(".", ",") + " millones de años"
        if lang == "it":
            word = "milione" if abs(n - 1) < 0.05 else "milioni"
            return s.replace(".", ",") + " " + word + " di anni fa"
        if lang == "ar":
            return "قبل " + s + " مليون سنة"
        if lang == "he":
            return "לפני " + s + " מיליון שנים"
    n = int(round(years))
    if lang == "en":
        return f"{n:,} years ago"
    if lang == "fr":
        return "il y a " + f"{n:,}".replace(",", "\u202f") + " ans"
    if lang == "es":
        return "hace " + f"{n:,}".replace(",", ".") + " años"
    if lang == "it":
        return f"{n:,}".replace(",", ".") + " anni fa"
    if lang == "ar":
        return "قبل " + f"{n:,}" + " سنة"
    if lang == "he":
        return "לפני " + f"{n:,}" + " שנים"
    raise SystemExit("bad lang " + lang)

def span(lang, a, b=None):
    A = phrase(lang, a)
    if b is None or b <= 0:
        end = {"en":"today","fr":"aujourd’hui","es":"hoy","it":"oggi","ar":"اليوم","he":"היום"}[lang]
        if lang == "en":
            return A + " to today"
        if lang == "fr":
            return "de " + A.removeprefix("il y a ") + " à aujourd’hui"
        if lang == "es":
            return "desde " + A + " hasta hoy"
        if lang == "it":
            return "da " + A + " a oggi"
        if lang == "ar":
            return "من " + A + " حتى اليوم"
        return "מ-" + A + " עד היום"
    B = phrase(lang, b)
    if lang == "en":
        return A + " to " + B
    if lang == "fr":
        return "de " + A.removeprefix("il y a ") + " à " + B.removeprefix("il y a ")
    if lang == "es":
        return "desde " + A + " hasta " + B
    if lang == "it":
        return "da " + A + " a " + B
    if lang == "ar":
        return "من " + A + " حتى " + B
    return "מ-" + A + " עד " + B

# Shared media. Credits that are names and licenses stay in Latin on every language.
MEDIA = {
"earth": ("assets/deep/photo-earth.webp", 1400, 1400, "https://commons.wikimedia.org/wiki/File:The_Earth_seen_from_Apollo_17.jpg",
          "NASA / Apollo 17 crew, public domain."),
"disk": ("assets/quest/layer-earth.webp", 1400, 1120, "https://commons.wikimedia.org/wiki/File:IRS46_nasa.jpg",
         "NASA/JPL-Caltech, public domain."),
"moon": ("assets/quest/layer-moon.webp", 1024, 1024, "https://commons.wikimedia.org/wiki/File:Apollo_15_Genesis_Rock.jpg",
         "NASA, public domain."),
"jack": ("assets/quest/layer-jack-hills.webp", 1400, 1001,
         "https://commons.wikimedia.org/wiki/File:Quartz-pebble_metaconglomerate_(Jack_Hills_Quartzite,_Archean,_2.65_to_3.05_Ga;_Jack_Hills,_Western_Australia)_2.jpg",
         "James St. John, CC BY 2.0, via Wikimedia Commons."),
"strom": ("assets/quest/layer-stromatolite.webp", 1400, 933,
          "https://commons.wikimedia.org/wiki/File:Stromatolite_Fossil_on_Pitamakan_Pass_(29305962428).jpg",
          "Glacier National Park, National Park Service, public domain."),
"burgess": ("assets/quest/layer-burgess.webp", 1280, 960,
            "https://commons.wikimedia.org/wiki/File:Anomalocaris_canadensis_fossil.jpg",
            "Esv, CC BY-SA 3.0, via Wikimedia Commons. ShareAlike: remixes keep the same license."),
"brach": ("assets/quest/layer-brachiopod.webp", 800, 525,
          "https://commons.wikimedia.org/wiki/File:Kaibab_Formation_-_fossil_brachiopod_and_crinoid_columnals.jpg",
          "National Park Service, public domain."),
"chicx": ("assets/quest/layer-chicxulub.webp", 715, 799,
          "https://commons.wikimedia.org/wiki/File:Chicxulub_radar_topography.jpg",
          "NASA/JPL-Caltech, public domain. Shuttle Radar Topography Mission."),
"ice": ("assets/quest/layer-ice-core.webp", 741, 335,
        "https://commons.wikimedia.org/wiki/File:GISP2_1855m_ice_core_layers.png",
        "NOAA, public domain."),
"dick": ("assets/quest/dickinsonia.webp", 1600, 1200,
         "https://commons.wikimedia.org/wiki/File:DickinsoniaCostata.jpg",
         "Verisimilus, CC BY 2.5, via Wikimedia Commons."),
"frond": ("assets/quest/mistaken-point.webp", 1600, 1200,
          "https://commons.wikimedia.org/wiki/File:Ediacaran_fossils_Mistaken_Point_Newfoundland.jpg",
          "Alicejmichel, CC BY-SA 4.0, via Wikimedia Commons."),
"steg": ("assets/finds/stegosaurus-1600.webp", 1600, 1200,
         "https://commons.wikimedia.org/wiki/File:Stegosaurus_skeleton_at_American_Museum_of_Natural_History.jpg",
         "Vicpeters, CC BY 4.0, via Wikimedia Commons."),
"boreal": ("assets/finds/borealopelta-1600.webp", 1600, 1208,
           "https://commons.wikimedia.org/wiki/File:Borealopelta_markmitchelli_(TMP_2011.033.0001),_Royal_Tyrrell_Museum,_Drumheller,_Alberta,_2025-07-13.jpg",
           "Chris Woodrich, CC BY-SA 4.0, via Wikimedia Commons. ShareAlike: remixes keep the same license."),
"niger": ("assets/finds/nigersaurus-1600.webp", 1600, 2154,
          "https://commons.wikimedia.org/wiki/File:Nigersaurus_taqueti_skull.jpg",
          "Sereno and others, 2007, CC BY 2.5, via Wikimedia Commons."),
"trike": ("assets/finds/triceratops-1600.webp", 1600, 1200,
          "https://commons.wikimedia.org/wiki/File:Triceratops_skeleton_-_Ulster_Museum_2.JPG",
          "Bazonka, CC BY-SA 3.0, via Wikimedia Commons. ShareAlike: remixes keep the same license."),
"whale": ("assets/quest/basilosaurus.webp", 1600, 2133,
          "https://commons.wikimedia.org/wiki/File:Basilosaurus_isis,_lower_jaw_in_Wadi_Al-Hitan.jpg",
          "Tom Horton, CC BY-SA 2.0, via Wikimedia Commons."),
"smilo": ("assets/smilodon/hero-1600.webp", 1600, 1200,
          "https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_skeleton.jpg",
          "TheUltimateGrass, CC0, via Wikimedia Commons."),
"mammoth": ("assets/quest/waco-mammoth.webp", 1600, 1066,
            "https://upload.wikimedia.org/wikipedia/commons/7/77/Waco_mammoth_site_QRT.jpg",
            "Larry D. Moore, CC BY 4.0, via Wikimedia Commons."),
"human": ("assets/quest/jebel-irhoud.webp", 1453, 1546,
          "https://commons.wikimedia.org/wiki/File:Jebel_Irhoud-1_NMNH.jpg",
          "Jonathan Chen, CC BY-SA 4.0, via Wikimedia Commons."),
"pacific": ("assets/deep/photo-pacific.webp", 1400, 932,
            "https://commons.wikimedia.org/wiki/File:ISS034E016601_-_Stratocumulus_Clouds_-_Pacific_Ocean.jpg",
            "NASA, public domain. ISS photograph ISS034-E-016601."),
}
# Waco file page is the commons page, not the upload URL. Fix below.
MEDIA["mammoth"] = ("assets/quest/waco-mammoth.webp", 1600, 1066,
    "https://commons.wikimedia.org/wiki/File:Waco_mammoth_site_QRT.jpg",
    "Larry D. Moore, CC BY 4.0, via Wikimedia Commons.")

# era, media key, link or "", tag key
ANIMALS = [
    ("precambrian", "dick", "World_Map.html", "tag_animal"),
    ("precambrian", "frond", "World_Map.html", "tag_like"),
    ("paleozoic", "burgess", "World_Map.html", "tag_animal"),
    ("paleozoic", "brach", "", "tag_animal"),
    ("mesozoic", "steg", "Stegosaurus.html", "tag_animal"),
    ("mesozoic", "boreal", "Borealopelta.html", "tag_animal"),
    ("mesozoic", "niger", "Nigersaurus.html", "tag_animal"),
    ("mesozoic", "trike", "Triceratops.html", "tag_animal"),
    ("cenozoic", "whale", "World_Map.html", "tag_animal"),
    ("cenozoic", "smilo", "Smilodon.html", "tag_animal"),
    ("cenozoic", "mammoth", "World_Map.html", "tag_animal"),
    ("cenozoic", "human", "World_Map.html", "tag_animal"),
]
BAND = {"precambrian":"strom", "paleozoic":"pacific", "mesozoic":"steg", "cenozoic":"earth"}

SOURCES = [
("src_usgs","https://pubs.usgs.gov/gip/geotime/age.html"),
("src_nasa_ss","https://science.nasa.gov/solar-system/solar-system-facts/"),
("src_moon","https://science.nasa.gov/moon/formation/"),
("src_wilde","https://doi.org/10.1038/35051550"),
("src_goe","https://astrobiology.nasa.gov/news/oxygen-production-in-earths-early-oceans-predates-the-great-oxidation-event/"),
("src_nps_time","https://www.nps.gov/subjects/geology/geotime.htm"),
("src_nps_scale","https://www.nps.gov/subjects/geology/time-scale.htm"),
("src_nps_fossils","https://www.nps.gov/subjects/fossils/fossils-through-geologic-time.htm"),
("src_nps_ext","https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm"),
("src_pbdb","https://paleobiodb.org/data1.2/intervals/list.json?scale=1"),
("src_cgmw","https://doi.org/10.14682/2022ICCCOLCODE"),
("src_ocean","https://www.ocean.si.edu/through-time/ocean-through-time"),
("src_rom","https://burgess-shale.rom.on.ca/"),
("src_mp","https://whc.unesco.org/en/list/1497"),
("src_flinders","https://whc.unesco.org/en/tentativelists/6524/"),
("src_wadi","https://whc.unesco.org/en/list/1186"),
("src_noaa","https://archive.oceanexplorer.noaa.gov/explorations/05stepstones/background/paleoclimate/paleoclimate.html"),
("src_ice","https://science.nasa.gov/earth/earth-observatory/paleoclimatology-the-ice-core-record/"),
("src_hublin","https://www.nature.com/articles/nature22336"),
("src_sapiens","https://humanorigins.si.edu/evidence/human-fossils/species/homo-sapiens"),
("src_waco","https://www.nps.gov/waco/index.htm"),
]

def _e(s):
    return html.escape(s, quote=True)

def ui(lang):
    """Interface and teaching copy. {y} fields are filled by the caller."""
    # Built in quest_copy to keep this file's logic readable.
    from quest_copy import COPY
    if lang not in COPY:
        raise SystemExit("missing quest copy: " + lang)
    base = COPY["en"]
    got = COPY[lang]
    missing = [k for k in base if k not in got]
    if missing:
        raise SystemExit(lang + " missing " + ", ".join(missing[:12]))
    return got

def _fill(lang, text):
    # Teaching copy uses these tokens so every language shares one clock.
    tokens = {
        "earth": phrase(lang, EARTH),
        "cam": phrase(lang, CAMBRIAN),
        "perm": phrase(lang, PERM_END),
        "cret": phrase(lang, CRET_END),
        "span_pre": span(lang, EARTH, CAMBRIAN),
        "span_pal": span(lang, CAMBRIAN, PERM_END),
        "span_mes": span(lang, PERM_END, CRET_END),
        "span_cen": span(lang, CRET_END, None),
        "y4404": phrase(lang, 4.404e9),
        "y45": phrase(lang, 4.5e9),
        "y24": phrase(lang, 2.4e9),
        "y508": phrase(lang, 508e6),
        "y560": phrase(lang, 560e6),
        "y542": phrase(lang, 542e6),
        "y580": phrase(lang, 580e6),
        "y160": phrase(lang, 160e6),
        "y120": phrase(lang, 120e6),
        "y40": phrase(lang, 40e6),
        "y37": phrase(lang, 37e6),
        "y16": phrase(lang, 1.6e6),
        "y20": phrase(lang, 20000),
        "y300": phrase(lang, 300000),
        "y68": phrase(lang, 68000),
        "y10": phrase(lang, 10000),
        "y252": phrase(lang, 252e6),
        "r560": span(lang, 560e6, 542e6),
        "r580": span(lang, 580e6, 560e6),
        "r40": span(lang, 40e6, 37e6),
        "r16": span(lang, 1.6e6, 10000),
        "r298": span(lang, 298.9e6, PERM_END),
        "earth_b": bare(lang, EARTH),
        "cam_b": bare(lang, CAMBRIAN),
        "y24_b": bare(lang, 2.4e9),
        "y4404_b": bare(lang, 4.404e9),
    }
    return text.format(**tokens)

def bare(lang, years):
    p = phrase(lang, years)
    if lang == "en":
        return p.removesuffix(" ago")
    if lang == "fr":
        return p.removeprefix("il y a ")
    if lang == "es":
        return p.removeprefix("hace ")
    if lang == "it":
        return p.removesuffix(" fa")
    if lang == "ar":
        return p.removeprefix("قبل ")
    return p.removeprefix("לפני ")

def fig(r, key, alt, cap, file_label, resized, lang):
    file, w, h, href, credit = MEDIA[key]
    # Jack Hills commons filename contains "Ga" as part of a file title, not page copy.
    cap_html = _e(cap)
    small = _e(credit + " " + resized)
    return (f'<figure class="dq-fig"><img src="{r}{file}" width="{w}" height="{h}" alt="{_e(alt)}" loading="lazy" decoding="async">'
            f'<figcaption>{cap_html}<br><small>{small} <a href="{_e(href)}" rel="noopener noreferrer">{_e(file_label)}</a></small></figcaption></figure>')

def diet_block(lang):
    d = DIET.get(lang) or DIET["en"]
    cards = []
    for key, klass in (("carn","is-carn"),("herb","is-herb"),("omni","is-omni")):
        c = d[key]
        realms = "".join(
            f'<p class="dq-realm"><b>{html.escape(c[realm+"_h"])}</b>{html.escape(c[realm])}</p>'
            for realm in ("land","sea","air")
        )
        cards.append(f'<article class="dq-diet {klass}"><h3>{html.escape(c["h"])}</h3><p>{html.escape(c["p"])}</p>{realms}</article>')
    homes = "".join(
        f'<article class="dq-diet"><h3>{html.escape(h)}</h3><p>{html.escape(p)}</p></article>'
        for h,p in d["homes"]
    )
    return (
        f'<section id="diets"><h2 class="dq-h">{html.escape(d["h"])}</h2><p class="dq-sub">{html.escape(d["lead"])}</p>'
        f'<div class="dq-diets">{"".join(cards)}</div></section>'
        f'<section id="homes"><h2 class="dq-h">{html.escape(d["homes_h"])}</h2><p class="dq-sub">{html.escape(d["homes_lead"])}</p>'
        f'<div class="dq-diets">{homes}</div></section>'
    )

def main(lang):
    t = ui(lang)
    en = ui("en")
    def T(k):
        text = t[k]
        use = lang
        if lang not in ("en","fr") and text == en.get(k) and not text.startswith("{"):
            use = "en"
        return _fill(use, text)
    r = "" if lang == "en" else "../"
    names = NAMES[lang]
    file_label = T("file_page")
    resized = T("resized")

    hero_file, hw, hh, hhref, hcredit = MEDIA["earth"]
    hero = (
        f'<section class="sm-hero">'
        f'<img src="{r}{hero_file}" width="{hw}" height="{hh}" alt="{_e(T("hero_alt"))}" fetchpriority="high" decoding="async">'
        f'<div class="sm-hero-shade" aria-hidden="true"></div>'
        f'<div class="sm-hero-copy"><p class="sm-kicker">{_e(T("kicker"))}</p>'
        f'<h1>{_e(T("h1"))}</h1><p class="sm-lead">{_e(T("lead"))}</p></div></section>'
    )

    # Proportional bar. Oldest on the left in every language, same as the deep-time map.
    acc = 0.0
    total = sum(DURS)
    starts = []
    for d in DURS:
        a = acc / total
        acc += d
        starts.append((a, acc / total))
    segs = "".join(
        f'<i class="{c}"></i>' for c in ("s-pre","s-pal","s-mes","s-cen")
    )
    legend = []
    era_ids = [p[0] for p in PERIODS]
    for (eid, _rows, idx), (a, b) in zip(PERIODS, starts):
        span_key = ["span_pre","span_pal","span_mes","span_cen"][idx]
        legend.append(
            f'<li><a href="#{eid}"><strong>{_e(names[eid])}</strong><span>{_e(T(span_key))}</span></a></li>'
        )
    stick = (
        f'<div class="dq-stick"><div class="dq-stick-in">'
        f'<p class="dq-oldest">{_e(T("oldest"))}</p>'
        f'<div class="dq-bar" dir="ltr" aria-hidden="true">{segs}<span class="dq-needle" id="dq-needle"></span></div>'
        f'<ul class="dq-legend">{"".join(legend)}</ul>'
        f'<p class="dq-now" id="dq-now" aria-live="polite"></p>'
        f'</div></div>'
    )

    intro = (
        f'<p class="sm-vcredit dq-credit">{_e(T("hero_cap"))} {_e(hcredit)} '
        f'<a href="{_e(hhref)}" rel="noopener noreferrer">{_e(file_label)}</a></p>'
        f'<p class="dq-lead">{_e(T("intro"))}</p>'
        f'<p class="dq-sign">{_e(T("sign"))}</p>'
    )

    # Calendar: radios, then panels, as siblings so CSS can switch them with no script.
    cals = ["earth","life","shells","land","dying","dinos","humans"]
    inputs = []
    labels = []
    panels = []
    for i, cid in enumerate(cals):
        chk = " checked" if i == 0 else ""
        inputs.append(f'<input type="radio" name="dqcal" id="dqcal-{cid}"{chk}>')
        labels.append(f'<label for="dqcal-{cid}">{_e(T("btn_"+cid))}</label>')
        panels.append(
            f'<article class="dq-panel is-{cid}"><h4>{_e(T("cal_"+cid+"_h"))}</h4><p>{_e(T("cal_"+cid+"_p"))}</p></article>'
        )
    calendar = (
        f'<div class="dq-cal">{"".join(inputs)}'
        f'<div class="dq-cal-tabs" role="group" aria-label="{_e(T("cal_h"))}">{"".join(labels)}</div>'
        f'{"".join(panels)}</div>'
    )
    arm = (
        f'<svg class="dq-arm" viewBox="0 0 760 180" aria-hidden="true">'
        f'<path d="M70 150 C 180 40, 580 40, 690 150" fill="none" stroke="#0b6ea8" stroke-width="16" stroke-linecap="round"/>'
        f'<circle cx="70" cy="150" r="14" fill="#f0a202"/>'
        f'<circle cx="610" cy="92" r="11" fill="#14915f"/>'
        f'<circle cx="690" cy="150" r="14" fill="#083453"/>'
        f'<circle cx="668" cy="132" r="6" fill="#fff" stroke="#083453" stroke-width="3"/>'
        f'</svg>'
        f'<ol class="dq-points">'
        f'<li>{_e(T("arm1"))}</li><li>{_e(T("arm2"))}</li><li>{_e(T("arm3"))}</li><li>{_e(T("arm4"))}</li>'
        f'</ol><p class="dq-note">{_e(T("arm_credit"))}</p>'
    )
    # arm lines may include <strong> we author. They are not user input.
    stats = (
        f'<div class="dq-stats">'
        f'<p class="dq-stat"><b>{_e(T("stat1n"))}</b>{_e(T("stat1l"))}</p>'
        f'<p class="dq-stat"><b>{_e(T("stat2n"))}</b>{_e(T("stat2l"))}</p>'
        f'<p class="dq-stat"><b>{_e(T("stat3n"))}</b>{_e(T("stat3l"))}</p>'
        f'</div><p class="dq-note">{_e(T("string_note"))}</p>'
    )
    tools = (
        f'<section id="time-scrubber"><h2 class="dq-h">{_e(T("feel_h"))}</h2><p class="dq-sub">{_e(T("feel_p"))}</p>'
        f'<div class="dq-tools">'
        f'<section class="dq-tool"><h3>{_e(T("cal_h"))}</h3><p>{_e(T("cal_p"))}</p>{calendar}</section>'
        f'<section class="dq-tool"><h3>{_e(T("arm_h"))}</h3><p>{_e(T("arm_p"))}</p>{arm}</section>'
        f'<section class="dq-tool"><h3>{_e(T("string_h"))}</h3><p>{_e(T("string_p"))}</p>{stats}</section>'
        f'</div></section>'
    )

    beats = []
    for key in ("disk","moon","jack","strom","chicx","ice"):
        beats.append(
            f'<article class="dq-beat">{fig(r, key, T(key+"_alt"), T(key+"_cap"), file_label, resized, lang)}'
            f'<div><p class="dq-k">{_e(T(key+"_k"))}</p><h3>{_e(T(key+"_h"))}</h3><p>{_e(T(key+"_p"))}</p></div></article>'
        )
    # fig already includes the image; the beat wraps figure + div. But fig returns a figure, and I also wanted the image on top.
    # The CSS expects img as a direct child for the 210px crop, and figure.dq-fig inside a card is ok if we don't double-wrap.
    # Rebuild beats so the image is the figure (object-fit cover via .dq-beat img). The figure's img matches .dq-beat img. Good.
    story = (
        f'<section id="story"><h2 class="dq-h">{_e(T("story_h"))}</h2><p class="dq-sub">{_e(T("story_p"))}</p>'
        f'<div class="dq-scroller">{"".join(beats)}</div></section>'
    )

    eras_html = []
    for eid, rows, idx in PERIODS:
        a, b = starts[idx]
        label = names[eid] + ", " + T(["span_pre","span_pal","span_mes","span_cen"][idx])
        band_key = BAND[eid]
        bfile, bw, bh, bhref, bcred = MEDIA[band_key]
        band_cap = {"precambrian":"strom_cap","paleozoic":"pacific_cap","mesozoic":"steg_cap","cenozoic":"hero_cap"}[eid]
        periods = []
        for pid, pa, pb in rows:
            periods.append(
                f'<li><strong>{_e(names[pid])}</strong><span>{_e(span(lang, pa, pb))}</span></li>'
            )
        cards = []
        for era, mid, link, tag in ANIMALS:
            if era != eid:
                continue
            more = ""
            if link:
                label_more = T("more_page") if link.endswith(".html") and link != "World_Map.html" else T("more_map")
                more = f'<p><a class="dq-more" href="{link}">{_e(label_more)}</a></p>'
            cards.append(
                f'<article class="dq-animal">{fig(r, mid, T(mid+"_alt"), T(mid+"_cap"), file_label, resized, lang)}'
                f'<div class="dq-card"><p class="dq-tag">{_e(T(tag))}</p>'
                f'<h3>{_e(T(mid+"_name"))}</h3>'
                f'<p class="dq-when">{_e(T(mid+"_when"))}</p>'
                f'<p>{_e(T(mid+"_body"))}</p>{more}</div></article>'
            )
        animals_h = T("animals_h") if eid != "precambrian" else T("animals_pre_h")
        eras_html.append(
            f'<section class="dq-era" id="{eid}" data-era data-start="{a:.6f}" data-end="{b:.6f}" data-label="{_e(label)}">'
            f'<div class="dq-era-band"><img src="{r}{bfile}" width="{bw}" height="{bh}" alt="" loading="lazy">'
            f'<div class="shade" aria-hidden="true"></div>'
            f'<div class="dq-era-copy"><p class="dq-era-kicker">{_e(T("era_kicker"))}</p>'
            f'<h2>{_e(names[eid])}</h2>'
            f'<p class="dq-years">{_e(T(["span_pre","span_pal","span_mes","span_cen"][idx]))}</p>'
            f'<p class="dq-nick">{_e(T(eid+"_nick"))}</p></div></div>'
            f'<div class="dq-era-body"><p>{_e(T(eid+"_intro"))}</p>'
            f'<p class="dq-credit">{_e(T(band_cap))} {_e(bcred)} '
            f'<a href="{_e(bhref)}" rel="noopener noreferrer">{_e(file_label)}</a></p>'
            f'<h3>{_e(T("years_h"))}</h3><ul class="dq-periods">{"".join(periods)}</ul>'
            f'<h3>{_e(animals_h)}</h3><div class="dq-animals">{"".join(cards)}</div>'
            f'<details class="dq-look"><summary>{_e(T("look"))}</summary><div class="dq-in">'
            f'<h4>{_e(T("concepts"))}</h4><p>{_e(T(eid+"_c"))}</p>'
            f'<h4>{_e(T("evidence"))}</h4><p>{_e(T(eid+"_e"))}</p>'
            f'<h4>{_e(T("openq"))}</h4><p>{_e(T(eid+"_q"))}</p>'
            f'</div></details></div></section>'
        )

    sources = "".join(
        f'<li><a href="{_e(url)}" rel="noopener noreferrer">{_e(T(key))}</a></li>' for key, url in SOURCES
    )
    close = (
        f'<section class="dq-close"><h2 class="dq-h">{_e(T("close_h"))}</h2><p>{_e(T("close_p"))}</p>'
        f'<p><a href="https://www.savingplanets.com/">{_e(T("close_a"))}</a></p></section>'
        f'<details class="dq-sources"><summary>{_e(T("sources"))} ({len(SOURCES)})</summary>'
        f'<div class="dq-in"><ul>{sources}</ul></div></details>'
    )

    page = (
        f'<main id="main">{hero}{stick}'
        f'<div class="sm-wrap">{intro}{diet_block(lang)}{tools}{story}</div>'
        f'<div class="dq-eras">{"".join(eras_html)}</div>'
        f'<div class="sm-wrap">{close}</div></main>'
    )
    banned = re.findall(r"\bMa\b|\bMA\b|\bMYA\b|\bmya\b|\bGa\b|\bGyr\b", page)
    if banned:
        raise SystemExit("bare time acronym in Dig Quest " + lang + ": " + " ".join(banned[:8]))
    return page
