# Plesiosaurus dossier. Age and finder are the deep-time entry already on the site.
# There is no film. The picture behind the title is Dmitry Bogdanov's drawing,
# 1800 pixels wide. The figure below is J. Dinkel's historical skeleton plate,
# not a photograph of the bones. No body length is on these sources.
import html, json

PBDB = "https://paleobiodb.org/data1.2/occs/list.json?taxon_name=Plesiosaurus%20dolichodeirus&show=time"
NHM = "https://www.nhm.ac.uk/discover/mary-anning-fossils.html"
PLATE = "https://commons.wikimedia.org/wiki/File:Plesiosaurus_dolichodeirus.jpg"
DRAW = "https://commons.wikimedia.org/wiki/File:Plesiosaurus_dolich1DB.jpg"

META = {
"en": ("Plesiosaurus", "Mary Anning’s plesiosaur. The type of Plesiosaurus dolichodeirus is Late Sinemurian, and the lower picture is a historical skeleton plate."),
"fr": ("Plesiosaurus de Lyme Regis", "Le plésiosaure de Mary Anning. Le type de Plesiosaurus dolichodeirus est du Sinémurien tardif, et l’image du bas est une planche ancienne."),
"es": ("Plesiosaurus de Lyme Regis", "El plesiosaurio de Mary Anning. El tipo de Plesiosaurus dolichodeirus es del Sinemuriense tardío, y la imagen inferior es una lámina antigua."),
"ar": ("بليسيوصور من لايم ريجيس", "بليسيوصور ماري أنينغ. نمط بليسيوصوروس دوليخوديروس من السينيموري المتأخر، والصورة السفلى لوحة هيكلية قديمة."),
"it": ("Plesiosaurus di Lyme Regis", "Il plesiosauro di Mary Anning. Il tipo di Plesiosaurus dolichodeirus è del Sinemuriano tardo, e l’immagine in basso è una tavola storica."),
"he": ("פלסיוזאורוס מליים רג'יס", "הפלסיוזאור של מרי אנינג. הטיפוס של פלסיוזאורוס דוליכודאירוס הוא מהסינמוריאן המאוחר, והתמונה למטה היא לוח שלד היסטורי."),
}
ALT = {
"en": "Artist’s concept of Plesiosaurus dolichodeirus by Dmitry Bogdanov. This is a drawing, not a photograph of the fossil.",
"fr": "Concept d’artiste de Plesiosaurus dolichodeirus par Dmitry Bogdanov. C’est un dessin, pas une photographie du fossile.",
"es": "Concepto artístico de Plesiosaurus dolichodeirus por Dmitry Bogdanov. Es un dibujo, no una fotografía del fósil.",
"ar": "تصور فني لبليسيوصوروس دوليخوديروس بريشة دميتري بوغدانوف. هذا رسم وليس صورة للأحفورة.",
"it": "Concetto artistico di Plesiosaurus dolichodeirus di Dmitry Bogdanov. È un disegno, non una fotografia del fossile.",
"he": "דימוי אמנותי של פלסיוזאורוס דוליכודאירוס מאת דמיטרי בוגדנוב. זה ציור, לא צילום של המאובן.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is a drawing. The picture lower down is a historical skeleton plate, not a photograph of the bones.</p>
<h2>What we know</h2>
<ul>
<li>Plesiosaurus dolichodeirus. A Paleobiology Database occurrence of the type is labeled Late Sinemurian. The same list stores that label on the Sinemurian bin, 199.5 to 192.9 million years ago. Those numbers are the whole Sinemurian stage on this timescale, not a measured span of only the late part. {_a(PBDB, "Paleobiology Database occurrence list")}</li>
<li>Mary Anning found the first articulated skeleton. The Natural History Museum in London tells that part of the story. {_a(NHM, "Natural History Museum, London")}</li>
<li>The drawing behind the title is Dmitry Bogdanov’s concept of the living animal. It is not a photograph. The original file is 1800 pixels wide. This page serves 1800 pixels wide, not enlarged. {_a(DRAW, "Drawing file page")}</li>
<li>The picture below is J. Dinkel’s historical figure of a Lower Lias skeleton. The original file is 3505 pixels wide. This page serves 1920 pixels wide, not enlarged. {_a(PLATE, "Skeleton plate")}</li>
</ul>
<h2>What this page does not claim</h2>
<ul>
<li>No body length is written on the sources linked here, so this page does not draw a person beside the animal.</li>
<li>The pin is the Jurassic Coast already on the World Map, the Dorset and East Devon coast. It is not the museum in London, and it is not a drawing of the animal. The place marker was made for this site. Created by the Founder and SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/plesiosaurus-1920.avif"><source type="image/webp" srcset="@@/assets/deeptime/plesiosaurus-1920.webp"><img src="@@/assets/deeptime/plesiosaurus-1920.webp" width="1920" height="808" alt="Historical figure of a Lower Lias Plesiosaurus dolichodeirus skeleton, drawn by J. Dinkel. Not a photograph of the bones."></picture>
<figcaption>Historical skeleton plate of a Lower Lias Plesiosaurus. Not a photograph of the specimen. J. Dinkel, public domain, via Wikimedia Commons. {_a(PLATE, "Skeleton plate")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(NHM, "Natural History Museum, London: Mary Anning’s fossils")}</li>
<li>{_a(PBDB, "Paleobiology Database occurrences of Plesiosaurus dolichodeirus")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the life drawing, CC BY-SA 3.0")}</li>
<li>{_a(PLATE, "Wikimedia Commons — the historical skeleton plate, public domain")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal fait pour ce site. L’image derrière le titre est un dessin. L’image plus bas est une planche ancienne de squelette, pas une photographie des os.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Plesiosaurus dolichodeirus. Une occurrence Paleobiology Database du type est étiquetée Sinémurien tardif. La même liste range cette étiquette sur le bac du Sinémurien, de 199,5 à 192,9 millions d’années. Ces nombres sont tout l’étage du Sinémurien sur cette échelle, pas une durée mesurée de la seule partie tardive. {_a(PBDB, "Liste d’occurrences Paleobiology Database")}</li>
<li>Mary Anning a trouvé le premier squelette articulé. Le Natural History Museum de Londres raconte cette part de l’histoire. {_a(NHM, "Natural History Museum, Londres")}</li>
<li>Le dessin derrière le titre est le concept de Dmitry Bogdanov de l’animal vivant. Ce n’est pas une photographie. Le fichier d’origine fait 1800 pixels de large. Cette page en sert 1800, sans agrandir. {_a(DRAW, "Page du dessin")}</li>
<li>L’image plus bas est la figure ancienne de J. Dinkel d’un squelette du Lias inférieur. Le fichier d’origine fait 3505 pixels de large. Cette page en sert 1920, sans agrandir. {_a(PLATE, "Planche du squelette")}</li>
</ul>
<h2>Ce que cette page ne dit pas</h2>
<ul>
<li>Aucune longueur du corps n’est écrite sur les sources citées ici, donc cette page ne dessine pas une personne à côté de l’animal.</li>
<li>L’épingle est la côte jurassique déjà sur la carte du monde, la côte du Dorset et de l’est du Devon. Ce n’est pas le musée de Londres, et ce n’est pas un dessin de l’animal. Le repère a été fait pour ce site. Créé par le fondateur et SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/plesiosaurus-1920.avif"><source type="image/webp" srcset="@@/assets/deeptime/plesiosaurus-1920.webp"><img src="@@/assets/deeptime/plesiosaurus-1920.webp" width="1920" height="808" alt="Figure ancienne d’un squelette de Plesiosaurus dolichodeirus du Lias inférieur, dessinée par J. Dinkel. Pas une photographie des os."></picture>
<figcaption>Planche ancienne d’un squelette de Plesiosaurus du Lias inférieur. Pas une photographie du spécimen. J. Dinkel, domaine public, via Wikimedia Commons. {_a(PLATE, "Planche du squelette")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(NHM, "Natural History Museum, Londres : les fossiles de Mary Anning")}</li>
<li>{_a(PBDB, "Occurrences Paleobiology Database de Plesiosaurus dolichodeirus")}</li>
<li>{_a(DRAW, "Wikimedia Commons — le dessin, CC BY-SA 3.0")}</li>
<li>{_a(PLATE, "Wikimedia Commons — la planche ancienne, domaine public")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Plesiosaurus"
    if fr:
        kicker, lead = "Le plésiosaure de Mary Anning", "Un dessin de l’animal vivant, et une planche ancienne du squelette. Pas une longueur inventée."
        credit = "Dessin : Dmitry Bogdanov, CC BY-SA 3.0, via Wikimedia Commons. Concept d’artiste, pas une photographie."
        where, aside_h = "Où est le fossile", "Pas le musée"
        aside = "<p>L’épingle est la côte jurassique, déjà sur la carte. Le musée qui raconte Mary Anning est à Londres.</p><p><a href=\"World_Map.html?pin=Jurassic%20Coast%20%28Dorset%20%26%20East%20Devon%29%2C%20UK\">Carte du monde</a></p>"
        back = '<p class="find-back"><a href="Marine.html">Vie marine</a> · <a href="Dunkleosteus.html">Dunkleosteus</a> · <a href="Pterodactylus.html">Pterodactylus</a></p>'
        file_label = "Page du dessin"
    else:
        kicker, lead = "Mary Anning’s plesiosaur", "A drawing of the living animal, and a historical plate of the skeleton. No invented length."
        credit = "Drawing: Dmitry Bogdanov, CC BY-SA 3.0, via Wikimedia Commons. Artist’s concept, not a photograph."
        where, aside_h = "Where the fossil is", "Not the museum"
        aside = "<p>The pin is the Jurassic Coast already on the map. The museum that tells Mary Anning’s story is in London.</p><p><a href=\"World_Map.html?pin=Jurassic%20Coast%20%28Dorset%20%26%20East%20Devon%29%2C%20UK\">World Map</a></p>"
        back = '<p class="find-back"><a href="Marine.html">Marine</a> · <a href="Dunkleosteus.html">Dunkleosteus</a> · <a href="Pterodactylus.html">Pterodactylus</a></p>'
        file_label = "Drawing file page"
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": 50.62, "lng": -2.45, "species": "Plesiosaurus dolichodeirus",
        "href": NHM, "source": "Natural History Museum, London",
        "name": "Jurassic Coast (Dorset & East Devon), UK",
        "note": "The coast. The museum that tells the finder is in London.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/plesiosaurus-life-1800.avif">'
        f'<source type="image/webp" srcset="{prefix}assets/deeptime/plesiosaurus-life-1800.webp">'
        f'<img src="{prefix}assets/deeptime/plesiosaurus-life-1800.jpg" width="1800" height="1106" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(DRAW, file_label)}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-plesiosaurus.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
