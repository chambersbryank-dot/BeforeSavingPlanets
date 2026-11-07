# Otodus megalodon. Facts are the life card already on this site.
# Boessenecker and others, 2019. No body length is copied from the drawing.
# The pin is the town the Capistrano Formation is named for, not one hole.
import html, json

DOI = "https://doi.org/10.7717/peerj.6088"
PAPER = "https://peerj.com/articles/6088/"
TOOTH = "https://commons.wikimedia.org/wiki/File:Otodus_megalodon_from_Capistrano_Fm.png"
DRAW = "https://commons.wikimedia.org/wiki/File:Otodus_megalodon_restoration.png"

META = {
"en": ("Otodus megalodon", "Teeth from the Capistrano Formation. Boessenecker and others, 2019, record this shark from the middle Miocene to about 3.6 million years ago."),
"fr": ("Le requin Otodus", "Dents de la formation de Capistrano. Boessenecker et autres, 2019, le signalent du Miocène moyen jusqu’à environ 3,6 millions d’années."),
"es": ("El tiburón Otodus", "Dientes de la Formación Capistrano. Boessenecker y otros, 2019, lo registran desde el Mioceno medio hasta hace unos 3,6 millones de años."),
"ar": ("قرش أوتودوس", "أسنان من تكوين كابيسترانو. يسجله بوسنكر وآخرون، 2019، من الميوسين الأوسط حتى نحو 3.6 مليون سنة."),
"it": ("Lo squalo Otodus", "Denti della Formazione Capistrano. Boessenecker e altri, 2019, lo registrano dal Miocene medio fino a circa 3,6 milioni di anni fa."),
"he": ("הכריש אוטודוס", "שיניים מתצורת קפיסטרנו. בוסנקר ואחרים, 2019, מתעדים אותו מהמיוקן התיכון עד לפני כ־3.6 מיליון שנה."),
}
ALT = {
"en": "Artist’s life restoration of Otodus megalodon. This is a drawing, not a photograph, and not a measured length.",
"fr": "Reconstitution artistique d’Otodus megalodon. C’est un dessin, pas une photographie, et pas une longueur mesurée.",
"es": "Restauración artística de Otodus megalodon. Es un dibujo, no una fotografía, y no una longitud medida.",
"ar": "ترميم فني لأوتودوس ميغالودون. هذا رسم وليس صورة، وليس طولاً مقاساً.",
"it": "Restauro artistico di Otodus megalodon. È un disegno, non una fotografia, e non una lunghezza misurata.",
"he": "שחזור אמנותי של אוטודוס מגלודון. זה ציור, לא צילום, ולא אורך שנמדד.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is a drawing. The photograph lower down is fossil teeth.</p>
<h2>What we know</h2>
<ul>
<li>Boessenecker and others, 2019, record Otodus megalodon from middle Miocene rocks through the early Pliocene, and put the extinction at about 3.6 million years ago. {_a(DOI, "PeerJ paper")}</li>
<li>The teeth in the photograph are from the Capistrano Formation. That paper’s corrected age for this set is 5.6 to 3.7 million years. {_a(PAPER, "PeerJ article page")}</li>
<li>The drawing behind the title is the artist’s restoration. This page does not copy a body length from the drawing, and it does not draw a person beside the shark.</li>
<li>The pin is San Juan Capistrano, the town the formation is named for. It is not one hole in the rock. Created by the Founder and SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/otodus-megalodon-1920.avif 1920w, @@/assets/deeptime/otodus-megalodon-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/otodus-megalodon-1920.webp 1920w, @@/assets/deeptime/otodus-megalodon-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/otodus-megalodon-1600.webp" width="1920" height="1272" alt="Fossil teeth of Otodus megalodon from the Capistrano Formation."></picture>
<figcaption>Teeth from the Capistrano Formation. Robert W. Boessenecker and coauthors, CC BY 4.0, via Wikimedia Commons. {_a(TOOTH, "Tooth figure")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(DOI, "Boessenecker and others, 2019, PeerJ, DOI")}</li>
<li>{_a(PAPER, "Same paper on the PeerJ site")}</li>
<li>{_a(TOOTH, "Wikimedia Commons — the tooth figure, CC BY 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the life restoration, CC BY 4.0")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal pour ce site. L’image derrière le titre est un dessin. La photo plus bas montre des dents fossiles.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Boessenecker et autres, 2019, signalent Otodus megalodon du Miocène moyen au Pliocène précoce, et placent l’extinction vers 3,6 millions d’années. {_a(DOI, "Article PeerJ")}</li>
<li>Les dents de la photo viennent de la formation de Capistrano. L’âge corrigé de cet ensemble, dans cet article, est de 5,6 à 3,7 millions d’années. {_a(PAPER, "Page de l’article")}</li>
<li>Le dessin derrière le titre est la reconstitution de l’artiste. Cette page ne reprend pas une longueur du dessin, et elle ne dessine pas une personne à côté du requin.</li>
<li>L’épingle est San Juan Capistrano, la ville qui donne son nom à la formation. Ce n’est pas un seul trou dans la roche. Créé par le fondateur et SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/otodus-megalodon-1920.avif 1920w, @@/assets/deeptime/otodus-megalodon-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/otodus-megalodon-1920.webp 1920w, @@/assets/deeptime/otodus-megalodon-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/otodus-megalodon-1600.webp" width="1920" height="1272" alt="Dents fossiles d’Otodus megalodon de la formation de Capistrano."></picture>
<figcaption>Dents de la formation de Capistrano. Robert W. Boessenecker et coauteurs, CC BY 4.0, via Wikimedia Commons. {_a(TOOTH, "Figure des dents")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(DOI, "Boessenecker et autres, 2019, PeerJ, DOI")}</li>
<li>{_a(PAPER, "Le même article sur le site PeerJ")}</li>
<li>{_a(TOOTH, "Wikimedia Commons — la figure des dents, CC BY 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — la reconstitution, CC BY 4.0")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Otodus megalodon"
    if fr:
        kicker, lead = "Un requin géant", "Des dents, pas une longueur inventée."
        credit = "Dessin : Oliver E. Demuth, CC BY 4.0, via Wikimedia Commons. Concept d’artiste, pas une photographie."
        where, aside_h = "Où sont les dents", "Pas un seul trou"
        aside = "<p>L’épingle est la ville de San Juan Capistrano, en Californie. La formation porte ce nom. Ce n’est pas un seul gisement pointé au mètre près.</p>"
        back = '<p class="find-back"><a href="Marine.html">Marin</a> · <a href="Deep_Time.html">Temps profond</a></p>'
    else:
        kicker, lead = "A giant shark", "Teeth, not an invented length."
        credit = "Drawing: Oliver E. Demuth, CC BY 4.0, via Wikimedia Commons. Artist’s concept, not a photograph."
        where, aside_h = "Where the teeth are", "Not one hole"
        aside = "<p>The pin is the town of San Juan Capistrano, California. The formation is named for that town. It is not one hole marked to the meter.</p>"
        back = '<p class="find-back"><a href="Marine.html">Marine</a> · <a href="Deep_Time.html">Deep Time</a></p>'
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": 33.5016932, "lng": -117.6625509, "species": "Otodus megalodon",
        "href": PAPER, "source": "OpenStreetMap relation 2310550, the town",
        "name": "San Juan Capistrano, California, USA",
        "note": "The town the Capistrano Formation is named for. Not one hole.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/life-otodus-megalodon.avif">'
        f'<img src="{prefix}assets/deeptime/life-otodus-megalodon.webp" width="1600" height="834" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(DRAW, "Page du dessin" if fr else "Drawing file page")}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-otodus.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
