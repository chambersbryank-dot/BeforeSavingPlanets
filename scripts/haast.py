# Haast's eagle. Facts are the life card already on this site.
# New Zealand Birds Online: died out 500 to 600 years ago, around the same
# time as the moa. No wingspan is invented. The pin is the Southland region
# named with the Castle Rocks skull plate, not one hole.
import html, json

NZ = "https://www.nzbirdsonline.org.nz/species/haasts-eagle"
SKULL = "https://commons.wikimedia.org/wiki/File:Harpagornis_moorei_skull.jpg"
DRAW = "https://commons.wikimedia.org/wiki/File:Giant_Haasts_eagle_attacking_New_Zealand_moa.jpg"

META = {
"en": ("Haast’s eagle", "A bird of prey in New Zealand. New Zealand Birds Online says it died out 500 to 600 years ago, around the same time as the moa."),
"fr": ("Aigle de Haast", "Un rapace de Nouvelle-Zélande. New Zealand Birds Online écrit qu’il a disparu il y a 500 à 600 ans, à peu près en même temps que les moas."),
"es": ("Águila de Haast", "Un ave de presa de Nueva Zelanda. New Zealand Birds Online dice que desapareció hace 500 a 600 años, más o menos cuando los moas."),
"ar": ("عقاب هاست", "جارح من نيوزيلندا. يقول New Zealand Birds Online إنه انقرض قبل 500 إلى 600 سنة، قريباً من زمن الموا."),
"it": ("Aquila di Haast", "Un rapace della Nuova Zelanda. New Zealand Birds Online scrive che si estinse 500–600 anni fa, circa insieme ai moa."),
"he": ("עיט האסט", "עוף דורס בניו זילנד. New Zealand Birds Online כותב שנכחד לפני 500 עד 600 שנה, בערך בזמן המואה."),
}
ALT = {
"en": "Artist’s illustration of Haast’s eagle and a moa. This is a drawing, not a photograph.",
"fr": "Illustration d’artiste de l’aigle de Haast et d’un moa. C’est un dessin, pas une photographie.",
"es": "Ilustración artística del águila de Haast y un moa. Es un dibujo, no una fotografía.",
"ar": "رسم فنّي لعقاب هاست وموَا. هذا رسم وليس صورة.",
"it": "Illustrazione artistica dell’aquila di Haast e di un moa. È un disegno, non una fotografia.",
"he": "איור אמנותי של עיט האסט ומואה. זה ציור, לא צילום.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is a drawing. The figure lower down is a skull plate, not a life portrait.</p>
<h2>What we know</h2>
<ul>
<li>New Zealand Birds Online says Haast’s eagle died out 500 to 600 years ago, around the same time as the moa. {_a(NZ, "New Zealand Birds Online")}</li>
<li>The figure below is a skull plate from Castle Rocks, Southland. It is not a life portrait. This page does not give a wingspan, because it does not invent one.</li>
<li>The drawing behind the title shows the eagle and a moa. It is an artist’s illustration, not a photograph of either animal.</li>
<li>The pin is the Southland region, the region named with that skull plate. It is not one hole. Created by the Founder and SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/haast-s-eagle-1920.avif 1920w, @@/assets/deeptime/haast-s-eagle-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/haast-s-eagle-1920.webp 1920w, @@/assets/deeptime/haast-s-eagle-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/haast-s-eagle-1600.webp" width="1920" height="826" alt="Skull plate of Haast’s eagle from Castle Rocks, Southland. Not a life portrait."></picture>
<figcaption>Skull plate from Castle Rocks, Southland. Public domain, via Wikimedia Commons. {_a(SKULL, "Skull plate file page")}</figcaption></figure>
<h2>Sources (3)</h2>
<ul>
<li>{_a(NZ, "New Zealand Birds Online: Haast’s eagle")}</li>
<li>{_a(SKULL, "Wikimedia Commons — the Castle Rocks skull plate, public domain")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the illustration, CC BY 2.5")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal pour ce site. L’image derrière le titre est un dessin. La figure plus bas est une planche de crâne, pas un portrait vivant.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>New Zealand Birds Online écrit que l’aigle de Haast a disparu il y a 500 à 600 ans, à peu près en même temps que les moas. {_a(NZ, "New Zealand Birds Online")}</li>
<li>La figure ci-dessous est une planche de crâne de Castle Rocks, dans le Southland. Ce n’est pas un portrait vivant. Cette page ne donne pas d’envergure, parce qu’elle n’en invente pas.</li>
<li>Le dessin derrière le titre montre l’aigle et un moa. C’est une illustration d’artiste, pas une photo de l’un ou de l’autre.</li>
<li>L’épingle est la région du Southland, la région nommée avec cette planche. Ce n’est pas un seul trou. Créé par le fondateur et SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/haast-s-eagle-1920.avif 1920w, @@/assets/deeptime/haast-s-eagle-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/haast-s-eagle-1920.webp 1920w, @@/assets/deeptime/haast-s-eagle-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/haast-s-eagle-1600.webp" width="1920" height="826" alt="Planche de crâne de l’aigle de Haast, Castle Rocks, Southland. Pas un portrait vivant."></picture>
<figcaption>Planche de crâne de Castle Rocks, Southland. Domaine public, via Wikimedia Commons. {_a(SKULL, "Page de la planche")}</figcaption></figure>
<h2>Sources (3)</h2>
<ul>
<li>{_a(NZ, "New Zealand Birds Online : aigle de Haast")}</li>
<li>{_a(SKULL, "Wikimedia Commons — la planche de Castle Rocks, domaine public")}</li>
<li>{_a(DRAW, "Wikimedia Commons — l’illustration, CC BY 2.5")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Haast’s eagle" if not fr else "Aigle de Haast"
    if fr:
        kicker, lead = "Un rapace disparu", "Une planche de crâne, pas une envergure inventée."
        credit = "Dessin : John Megahan, CC BY 2.5, via Wikimedia Commons. Illustration, pas une photographie."
        where, aside_h = "D’où vient la planche", "La région, pas un trou"
        aside = "<p>La planche vient de Castle Rocks, dans le Southland. L’épingle marque la région du Southland, pas un seul site au mètre près.</p>"
        back = '<p class="find-back"><a href="Aerial.html">Aérien</a> · <a href="Deep_Time.html">Temps profond</a></p>'
    else:
        kicker, lead = "A lost bird of prey", "A skull plate, not an invented wingspan."
        credit = "Drawing: John Megahan, CC BY 2.5, via Wikimedia Commons. An illustration, not a photograph."
        where, aside_h = "Where the plate is from", "The region, not one hole"
        aside = "<p>The plate is from Castle Rocks, Southland. The pin marks the Southland region, not one site to the meter.</p>"
        back = '<p class="find-back"><a href="Aerial.html">Aerial</a> · <a href="Deep_Time.html">Deep Time</a></p>'
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": -45.9254266, "lng": 167.6068483, "species": "Haast’s eagle",
        "href": NZ, "source": "OpenStreetMap relation 1640159, the region",
        "name": "Southland, New Zealand",
        "note": "The region named with the Castle Rocks skull plate. Not one hole.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/life-haasts-eagle.avif">'
        f'<img src="{prefix}assets/deeptime/life-haasts-eagle.webp" width="1374" height="1100" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{html.escape(h1)}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(DRAW, "Page du dessin" if fr else "Drawing file page")}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-haast.svg" role="region" aria-label="{html.escape(h1)}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
