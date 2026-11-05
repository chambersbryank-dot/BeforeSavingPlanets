# Meganeura dossier. Facts already on the site come from the Paris museum page.
# There is no Founder-and-SI film. The picture behind the title is a photograph
# of a museum model, reduced from 4608 pixels to 1920. The lectotype is below.
# The only length used here is the museum's 70 cm wingspan, so no person is drawn.
import html, json

MUSEUM = "https://www.mnhn.fr/fr/meganeura-monyi-libellule-geante"
FOSSIL = "https://commons.wikimedia.org/wiki/File:Meganeura_monyi_MNHN_R51142_1.jpg"
MODEL = "https://commons.wikimedia.org/wiki/File:Meganeura_monyi,_reconstitution.jpg"
TOWN = "https://www.openstreetmap.org/relation/115128"

META = {
"en": ("Meganeura", "The Paris lectotype of Meganeura monyi, from Commentry. The museum gives a 70 cm wingspan about 300 million years ago."),
"fr": ("Meganeura de Commentry", "Le lectotype de Paris de Meganeura monyi, de Commentry. Le muséum donne 70 cm d’envergure il y a environ 300 millions d’années."),
"es": ("Meganeura de Commentry", "El lectotipo de París de Meganeura monyi, de Commentry. El museo da 70 cm de envergadura hace unos 300 millones de años."),
"ar": ("ميغانيورا من كومونتري", "النمط المختار في باريس لميغانيورا موني، من كومونتري. المتحف يعطي باع جناح 70 سم قبل نحو 300 مليون سنة."),
"it": ("Meganeura di Commentry", "Il lectotipo di Parigi di Meganeura monyi, da Commentry. Il museo indica 70 cm di apertura alare circa 300 milioni di anni fa."),
"he": ("מגנאוריה מקומנטרי", "הלקטוטיפ מפריז של מגנאוריה מוניי, מקומנטרי. המוזיאון נותן מוטת כנפיים של 70 ס״מ לפני כ־300 מיליון שנה."),
}
ALT = {
"en": "Photograph of a Meganeura monyi model at the Muséum Henri-Lecoq in Clermont-Ferrand. The wall behind it is a painting. This is not the fossil.",
"fr": "Photographie d’une maquette de Meganeura monyi au Muséum Henri-Lecoq, à Clermont-Ferrand. Le mur derrière est une peinture. Ce n’est pas le fossile.",
"es": "Fotografía de una maqueta de Meganeura monyi en el Muséum Henri-Lecoq de Clermont-Ferrand. La pared de atrás es una pintura. No es el fósil.",
"ar": "صورة لنموذج ميغانيورا موني في متحف هنري-لوكوك في كليرمون-فيران. الجدار خلفه لوحة مرسومة. هذه ليست الأحفورة.",
"it": "Fotografia di un modello di Meganeura monyi al Muséum Henri-Lecoq di Clermont-Ferrand. Il muro dietro è un dipinto. Non è il fossile.",
"he": "צילום של דגם מגנאוריה מוניי במוזיאון אנרי-לקוק בקלרמון-פראן. הקיר מאחור הוא ציור. זה אינו המאובן.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is a photograph of a museum model. The photograph lower down is the fossil.</p>
<h2>What we know</h2>
<ul>
<li>Meganeura monyi is a giant insect from Commentry, in the Allier, France. The Paris museum dates it to about 300 million years ago, in the Late Carboniferous, and gives the wingspan as 70 cm. {_a(MUSEUM, "National Museum of Natural History, Paris")}</li>
<li>The photograph below is the lectotype, MNHN R51142, at that museum in Paris. {_a(FOSSIL, "Fossil file page")}</li>
<li>The picture behind the title was taken at the Muséum Henri-Lecoq in Clermont-Ferrand. It is a model. The wall behind the model is a painting in that exhibit. The painting is not a fossil this page identifies. The original file is 4608 pixels wide. This page serves 1920 pixels wide, not enlarged. {_a(MODEL, "Model photograph")}</li>
<li>The photographer’s caption also says the wingspan could reach 70 cm, the same figure this site takes from the Paris museum.</li>
</ul>
<h2>What this page does not claim</h2>
<ul>
<li>70 cm is a wingspan. This page does not draw a person beside the insect, and it does not turn that wingspan into a body length.</li>
<li>The pin is the town of Commentry. It is not the museum in Paris, and it is not the model in Clermont-Ferrand. The place marker was made for this site. Created by the Founder and SI. {_a(TOWN, "Commentry on OpenStreetMap")}</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/meganeura-1772.avif"><source type="image/webp" srcset="@@/assets/deeptime/meganeura-1772.webp"><img src="@@/assets/deeptime/meganeura-1772.webp" width="1772" height="1181" alt="Lectotype of Meganeura monyi, specimen MNHN R51142, at the National Museum of Natural History in Paris."></picture>
<figcaption>Lectotype MNHN R51142 in Paris. Gaëlle Doitteau and Sandra DAILLIE, CC BY 4.0, via Wikimedia Commons. The original file is 1772 pixels wide. {_a(FOSSIL, "Fossil file page")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(MUSEUM, "National Museum of Natural History, Paris: Meganeura monyi")}</li>
<li>{_a(FOSSIL, "Wikimedia Commons — lectotype MNHN R51142, CC BY 4.0")}</li>
<li>{_a(MODEL, "Wikimedia Commons — model photograph, CC BY-SA 4.0")}</li>
<li>{_a(TOWN, "OpenStreetMap — the town of Commentry")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal fait pour ce site. L’image derrière le titre est une photographie d’une maquette de musée. La photographie plus bas est le fossile.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Meganeura monyi est un insecte géant de Commentry, dans l’Allier, en France. Le muséum de Paris le date d’environ 300 millions d’années, au Carbonifère tardif, et donne 70 cm d’envergure. {_a(MUSEUM, "Muséum national d’histoire naturelle, Paris")}</li>
<li>La photographie plus bas est le lectotype, MNHN R51142, dans ce musée à Paris. {_a(FOSSIL, "Page du fossile")}</li>
<li>L’image derrière le titre a été prise au Muséum Henri-Lecoq, à Clermont-Ferrand. C’est une maquette. Le mur derrière la maquette est une peinture de cette exposition. Cette peinture n’est pas un fossile que cette page identifie. Le fichier d’origine fait 4608 pixels de large. Cette page en sert 1920, sans agrandir. {_a(MODEL, "Photo de la maquette")}</li>
<li>La légende du photographe dit aussi que l’envergure pouvait atteindre 70 cm, le même chiffre que ce site retient du muséum de Paris.</li>
</ul>
<h2>Ce que cette page ne dit pas</h2>
<ul>
<li>70 cm est une envergure. Cette page ne dessine pas une personne à côté de l’insecte, et elle ne transforme pas cette envergure en longueur du corps.</li>
<li>L’épingle est la ville de Commentry. Ce n’est pas le musée de Paris, et ce n’est pas la maquette de Clermont-Ferrand. Le repère a été fait pour ce site. Créé par le fondateur et SI. {_a(TOWN, "Commentry sur OpenStreetMap")}</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/meganeura-1772.avif"><source type="image/webp" srcset="@@/assets/deeptime/meganeura-1772.webp"><img src="@@/assets/deeptime/meganeura-1772.webp" width="1772" height="1181" alt="Lectotype de Meganeura monyi, spécimen MNHN R51142, au Muséum national d’histoire naturelle à Paris."></picture>
<figcaption>Lectotype MNHN R51142 à Paris. Gaëlle Doitteau et Sandra DAILLIE, CC BY 4.0, via Wikimedia Commons. Le fichier d’origine fait 1772 pixels de large. {_a(FOSSIL, "Page du fossile")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(MUSEUM, "Muséum national d’histoire naturelle, Paris : Meganeura monyi")}</li>
<li>{_a(FOSSIL, "Wikimedia Commons — lectotype MNHN R51142, CC BY 4.0")}</li>
<li>{_a(MODEL, "Wikimedia Commons — photo de la maquette, CC BY-SA 4.0")}</li>
<li>{_a(TOWN, "OpenStreetMap — la ville de Commentry")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Meganeura"
    if fr:
        kicker, lead = "Un insecte géant", "70 cm d’envergure, un lectotype à Paris, et une maquette qui n’est pas le fossile."
        credit = "Maquette : Eunostos, CC BY-SA 4.0, via Wikimedia Commons. Photographie d’une reconstitution au Muséum Henri-Lecoq, à Clermont-Ferrand. Le mur est une peinture. Ce n’est pas le fossile."
        where, aside_h = "Où est le fossile", "Pas sur cette épingle"
        aside = "<p>L’épingle est la ville de Commentry, dans l’Allier. Le lectotype est à Paris. La maquette est à Clermont-Ferrand.</p><p><a href=\"Aerial.html\">Aérien</a></p>"
        back = '<p class="find-back"><a href="Aerial.html">Aérien</a> · <a href="Archaeopteryx.html">Archaeopteryx</a> · <a href="Dunkleosteus.html">Dunkleosteus</a></p>'
        file_label = "Photo de la maquette"
    else:
        kicker, lead = "A giant insect", "A 70 cm wingspan, a lectotype in Paris, and a model that is not the fossil."
        credit = "Model: Eunostos, CC BY-SA 4.0, via Wikimedia Commons. Photograph of a reconstitution at the Muséum Henri-Lecoq, Clermont-Ferrand. The wall is a painting. This is not the fossil."
        where, aside_h = "Where the fossil is", "Not on this pin"
        aside = "<p>The pin is the town of Commentry, in the Allier. The lectotype is in Paris. The model is in Clermont-Ferrand.</p><p><a href=\"Aerial.html\">Aerial</a></p>"
        back = '<p class="find-back"><a href="Aerial.html">Aerial</a> · <a href="Archaeopteryx.html">Archaeopteryx</a> · <a href="Dunkleosteus.html">Dunkleosteus</a></p>'
        file_label = "Model photograph"
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": 46.2901, "lng": 2.744, "species": "Meganeura monyi",
        "href": MUSEUM, "source": "National Museum of Natural History, Paris",
        "name": "Commentry, Allier, France",
        "note": "The town. The lectotype is in Paris. The model is in Clermont-Ferrand.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/meganeura-life-1920.avif">'
        f'<source type="image/webp" srcset="{prefix}assets/deeptime/meganeura-life-1920.webp">'
        f'<img src="{prefix}assets/deeptime/meganeura-life-1920.jpg" width="1920" height="1434" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(MODEL, file_label)}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-meganeura.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
