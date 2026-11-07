# Mosasaurus dossier. Age bins and the Haarlem skull are the deep-time entry.
# There is no film. The picture behind the title is a 2800-pixel-wide drawing.
# The photograph below was taken at the Teylers Museum. No measured body length
# is on this site's sources, so no person is drawn beside the animal.
import html, json

PBDB = "https://paleobiodb.org/data1.2/occs/list.json?taxon_name=Mosasaurus%20hoffmannii&show=time"
SKULL = "https://commons.wikimedia.org/wiki/File:Mosasaurus_hoffmanni_first_specimen.jpg"
DRAW = "https://commons.wikimedia.org/wiki/File:Mosasaurus.png"
TOWN = "https://www.openstreetmap.org/relation/2078292"

META = {
"en": ("Mosasaurus", "A skull photographed at the Teylers Museum in Haarlem. The youngest time bin is not a claim that it outlived the Cretaceous."),
"fr": ("Mosasaurus de Maastricht", "Un crâne photographié au musée Teylers, à Haarlem. Le bac de temps le plus jeune n’est pas une preuve qu’il a vécu après le Crétacé."),
"es": ("Mosasaurus de Maastricht", "Un cráneo fotografiado en el museo Teylers, en Haarlem. El intervalo más joven no afirma que viviera después del Cretácico."),
"ar": ("موساصور من ماستريخت", "جمجمة صُوّرت في متحف تايلرز في هارلم. حد الزمن الأحدث ليس ادعاءً بأنه عاش بعد العصر الطباشيري."),
"it": ("Mosasaurus di Maastricht", "Un cranio fotografato al museo Teylers di Haarlem. Il limite più giovane non dice che visse dopo il Cretaceo."),
"he": ("מוזאזאורוס ממאסטריכט", "גולגולת שצולמה במוזיאון טיילרס בהארלם. קצה הזמן הצעיר אינו טענה שחי אחרי הקרטיקון."),
}
ALT = {
"en": "Artist’s concept of Mosasaurus hoffmannii. This is a drawing, not a photograph of the skull.",
"fr": "Concept d’artiste de Mosasaurus hoffmannii. C’est un dessin, pas une photographie du crâne.",
"es": "Concepto artístico de Mosasaurus hoffmannii. Es un dibujo, no una fotografía del cráneo.",
"ar": "تصور فني لموساصوروس هوفماني. هذا رسم وليس صورة للجمجمة.",
"it": "Concetto artistico di Mosasaurus hoffmannii. È un disegno, non una fotografia del cranio.",
"he": "דימוי אמנותי של מוזאזאורוס הופמני. זה ציור, לא צילום של הגולגולת.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is a drawing. The photograph lower down is a skull at the Teylers Museum in Haarlem.</p>
<h2>What we know</h2>
<ul>
<li>Mosasaurus hoffmannii. Paleobiology Database occurrences are binned from the Campanian through the Maastrichtian. On this timescale the oldest bin starts at 83.6 million years ago. Most are Late Maastrichtian. The youngest stored bin edge is 61.66, a bin boundary, not a claim that it lived past the end of the Cretaceous. {_a(PBDB, "Paleobiology Database occurrence list")}</li>
<li>The photograph is a fossil mosasaur taken at the Teylers Museum in Haarlem. The file is titled as the first specimen. The original file is 4000 pixels wide. This page serves 1920 pixels wide, not enlarged. {_a(SKULL, "Skull file page")}</li>
<li>The drawing behind the title is an artist’s concept of the whole animal. It is not a photograph. The original file is 2800 pixels wide. This page serves 2800 pixels wide, not enlarged. {_a(DRAW, "Drawing file page")}</li>
</ul>
<h2>What this page does not claim</h2>
<ul>
<li>The artist’s file note says a full body is hard to estimate from the skull. This page does not copy a length from that note, and it does not draw a person beside the animal.</li>
<li>The pin is the city of Maastricht. The skull photograph was taken in Haarlem, not at this pin. The place marker was made for this site. Created by the Founder and SI. {_a(TOWN, "Maastricht on OpenStreetMap")}</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/mosasaurus-1920.avif"><source type="image/webp" srcset="@@/assets/deeptime/mosasaurus-1920.webp"><img src="@@/assets/deeptime/mosasaurus-1920.webp" width="1920" height="1440" alt="Fossil mosasaur skull photographed at the Teylers Museum in Haarlem. The file is titled as the first specimen."></picture>
<figcaption>Skull photographed at the Teylers Museum, Haarlem. Ghedoghedo, CC BY-SA 4.0, via Wikimedia Commons. {_a(SKULL, "Skull file page")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(PBDB, "Paleobiology Database occurrences of Mosasaurus hoffmannii")}</li>
<li>{_a(SKULL, "Wikimedia Commons — the Haarlem skull photograph, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the life drawing, CC BY 4.0")}</li>
<li>{_a(TOWN, "OpenStreetMap — the city of Maastricht")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal fait pour ce site. L’image derrière le titre est un dessin. La photographie plus bas est un crâne au musée Teylers, à Haarlem.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Mosasaurus hoffmannii. Les occurrences de la Paleobiology Database vont du Campanien au Maastrichtien. Sur cette échelle, le bac le plus ancien commence à 83,6 millions d’années. La plupart sont du Maastrichtien tardif. Le bord du bac le plus jeune est 61,66, une limite de bac, pas une affirmation qu’il a vécu après la fin du Crétacé. {_a(PBDB, "Liste d’occurrences Paleobiology Database")}</li>
<li>La photographie est un mosasaure fossile prise au musée Teylers, à Haarlem. Le fichier est titré comme le premier spécimen. Le fichier d’origine fait 4000 pixels de large. Cette page en sert 1920, sans agrandir. {_a(SKULL, "Page du crâne")}</li>
<li>Le dessin derrière le titre est un concept d’artiste de l’animal entier. Ce n’est pas une photographie. Le fichier d’origine fait 2800 pixels de large. Cette page en sert 2800, sans agrandir. {_a(DRAW, "Page du dessin")}</li>
</ul>
<h2>Ce que cette page ne dit pas</h2>
<ul>
<li>La note du fichier de l’artiste dit qu’un corps entier est difficile à estimer à partir du crâne. Cette page ne copie pas une longueur depuis cette note, et elle ne dessine pas une personne à côté de l’animal.</li>
<li>L’épingle est la ville de Maastricht. La photographie du crâne a été prise à Haarlem, pas sur cette épingle. Le repère a été fait pour ce site. Créé par le fondateur et SI. {_a(TOWN, "Maastricht sur OpenStreetMap")}</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/mosasaurus-1920.avif"><source type="image/webp" srcset="@@/assets/deeptime/mosasaurus-1920.webp"><img src="@@/assets/deeptime/mosasaurus-1920.webp" width="1920" height="1440" alt="Crâne de mosasaure fossile photographié au musée Teylers, à Haarlem. Le fichier est titré comme le premier spécimen."></picture>
<figcaption>Crâne photographié au musée Teylers, à Haarlem. Ghedoghedo, CC BY-SA 4.0, via Wikimedia Commons. {_a(SKULL, "Page du crâne")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(PBDB, "Occurrences Paleobiology Database de Mosasaurus hoffmannii")}</li>
<li>{_a(SKULL, "Wikimedia Commons — la photo du crâne de Haarlem, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — le dessin, CC BY 4.0")}</li>
<li>{_a(TOWN, "OpenStreetMap — la ville de Maastricht")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Mosasaurus"
    if fr:
        kicker, lead = "Un crâne à Haarlem", "Un dessin de l’animal entier, et le crâne du musée Teylers. Pas une longueur copiée d’une note d’artiste."
        credit = "Dessin : UnexpectedDinoLesson, CC BY 4.0, via Wikimedia Commons. Concept d’artiste, pas une photographie."
        where, aside_h = "Où est le fossile", "Pas sur cette épingle"
        aside = "<p>L’épingle est la ville de Maastricht. La photographie du crâne a été prise au musée Teylers, à Haarlem.</p>"
        back = '<p class="find-back"><a href="Marine.html">Vie marine</a> · <a href="Plesiosaurus.html">Plesiosaurus</a> · <a href="Dunkleosteus.html">Dunkleosteus</a></p>'
        file_label = "Page du dessin"
    else:
        kicker, lead = "A skull in Haarlem", "A drawing of the whole animal, and the skull at the Teylers Museum. No length copied from an artist’s note."
        credit = "Drawing: UnexpectedDinoLesson, CC BY 4.0, via Wikimedia Commons. Artist’s concept, not a photograph."
        where, aside_h = "Where the fossil is", "Not on this pin"
        aside = "<p>The pin is the city of Maastricht. The skull photograph was taken at the Teylers Museum in Haarlem.</p>"
        back = '<p class="find-back"><a href="Marine.html">Marine</a> · <a href="Plesiosaurus.html">Plesiosaurus</a> · <a href="Dunkleosteus.html">Dunkleosteus</a></p>'
        file_label = "Drawing file page"
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": 50.8512, "lng": 5.691, "species": "Mosasaurus hoffmannii",
        "href": TOWN, "source": "OpenStreetMap, the city of Maastricht",
        "name": "Maastricht, Limburg, Netherlands",
        "note": "The city. The skull photograph was taken in Haarlem.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/mosasaurus-life-2800.avif">'
        f'<source type="image/webp" srcset="{prefix}assets/deeptime/mosasaurus-life-2800.webp">'
        f'<img src="{prefix}assets/deeptime/mosasaurus-life-2800.png" width="2800" height="600" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(DRAW, file_label)}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-mosasaurus.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
