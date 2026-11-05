# Archaeopteryx dossier. Facts are the Solnhofen coin already on the World Map.
# There is no Founder-and-SI film of this animal. The hero is Durbed's drawing.
# The Berlin fossil photograph is the second picture. No body length is on the coin,
# so this page does not invent a scale comparison.
import html, json

SOLN = "https://www.museum-solnhofen.de/"
BERLIN = "https://www.museumfuernaturkunde.berlin/en/plan-your-visit/exhibition/the-world-of-dinosaurs/"
FOSSIL = "https://commons.wikimedia.org/wiki/File:Berlin_Archaeopteryx.jpg"
DRAW = "https://commons.wikimedia.org/wiki/File:Archaeopteryx_lithographica_by_durbed.jpg"

META = {
"en": ("Archaeopteryx", "The Berlin fossil, with feathers, teeth, and a long bony tail, from the Solnhofen lagoons about 150 million years ago."),
"fr": ("Archaeopteryx de Solnhofen", "Le fossile de Berlin, plumes, dents et longue queue osseuse, des lagunes de Solnhofen il y a environ 150 millions d’années."),
"es": ("Archaeopteryx de Solnhofen", "El fósil de Berlín, con plumas, dientes y una cola ósea larga, de las lagunas de Solnhofen hace unos 150 millones de años."),
"ar": ("أركيوبتركس من سولنهوفن", "أحفورة برلين، بريش وأسنان وذيل عظمي طويل، من بحيرات سولنهوفن قبل نحو 150 مليون سنة."),
"it": ("Archaeopteryx di Solnhofen", "Il fossile di Berlino, con piume, denti e una lunga coda ossea, dalle lagune di Solnhofen circa 150 milioni di anni fa."),
"he": ("ארכאופטריקס מסולנהופן", "המאובן מברלין, עם נוצות, שיניים וזנב גרמי ארוך, מלגונות זולנהופן לפני כ־150 מיליון שנה."),
}
ALT = {
"en": "Artist’s concept of Archaeopteryx lithographica chasing Compsognathus. This is a drawing, not a photograph.",
"fr": "Concept d’artiste d’Archaeopteryx lithographica poursuivant Compsognathus. C’est un dessin, pas une photographie.",
"es": "Concepto artístico de Archaeopteryx lithographica persiguiendo a Compsognathus. Es un dibujo, no una fotografía.",
"ar": "تصور فني لأركيوبتركس ليثوغرافيكا وهو يطارد كومبسوغناثوس. هذا رسم وليس صورة فوتوغرافية.",
"it": "Concetto artistico di Archaeopteryx lithographica che insegue Compsognathus. È un disegno, non una fotografia.",
"he": "דימוי אמנותי של ארכאופטריקס ליתוגרפיקה רודף אחרי קומפסוגנתוס. זה ציור, לא צילום.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is a drawing. The photograph lower down is the fossil.</p>
<h2>What we know</h2>
<ul>
<li>Southern Germany was a string of salty, warm lagoons. The bottom water had almost no oxygen, so anything that sank was left alone, then covered in fine lime mud. That is how Archaeopteryx was preserved, feathers and all. It had feathers, teeth, and a long bony tail.</li>
<li>The photograph is the Berlin specimen, the original fossil, not a cast. It is at the Museum für Naturkunde in Berlin. The rock it came from is the Solnhofen Limestone, around Solnhofen in Bavaria. {_a(BERLIN, "Museum für Naturkunde Berlin")} {_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>The drawing behind the title is an artist’s concept of Archaeopteryx chasing Compsognathus, a small dinosaur from the same lagoons. The drawing is not a photograph. {_a(DRAW, "Drawing file page")}</li>
<li>Found in 1861, two years after Darwin’s book, it became famous evidence that birds came from reptiles. The age used on this site’s Solnhofen coin is about 150 million years ago, in the Late Jurassic.</li>
</ul>
<h2>What this page does not claim</h2>
<ul>
<li>No body length is written on the Solnhofen coin or on the two museum pages linked here, so this page does not draw a person next to the animal.</li>
<li>The pin is the limestone in Bavaria. It is not the museum in Berlin, and it is not a drawing of the animal. The place marker was made for this site. Created by the Founder and SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/archaeopteryx-1920.avif 1920w, @@/assets/deeptime/archaeopteryx-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/archaeopteryx-1920.webp 1920w, @@/assets/deeptime/archaeopteryx-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/archaeopteryx-1600.webp" width="1920" height="2294" alt="The Berlin specimen of Archaeopteryx lithographica, the original fossil with feather impressions, at the Museum für Naturkunde in Berlin. Not a cast."></picture>
<figcaption>Berlin specimen of Archaeopteryx at the Museum für Naturkunde. Original fossil, not a cast. Emily Willoughby, CC BY-SA 4.0, via Wikimedia Commons. {_a(FOSSIL, "Fossil file page")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>{_a(BERLIN, "Museum für Naturkunde Berlin: the Berlin specimen")}</li>
<li>{_a(FOSSIL, "Wikimedia Commons — the Berlin fossil photograph, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the hero drawing, CC BY-SA 3.0")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal fait pour ce site. L’image derrière le titre est un dessin. La photographie plus bas est le fossile.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Le sud de l’Allemagne était une suite de lagunes salées et chaudes. L’eau du fond n’avait presque pas d’oxygène, donc ce qui coulait restait tranquille, puis se couvrait de boue calcaire fine. C’est ainsi qu’Archaeopteryx a été conservé, plumes comprises. Il avait des plumes, des dents et une longue queue osseuse.</li>
<li>La photographie est le spécimen de Berlin, le fossile original, pas un moulage. Il est au Museum für Naturkunde, à Berlin. La roche vient du calcaire de Solnhofen, autour de Solnhofen, en Bavière. {_a(BERLIN, "Museum für Naturkunde Berlin")} {_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>Le dessin derrière le titre est un concept d’artiste : Archaeopteryx poursuit Compsognathus, un petit dinosaure des mêmes lagunes. Le dessin n’est pas une photographie. {_a(DRAW, "Page du dessin")}</li>
<li>Trouvé en 1861, deux ans après le livre de Darwin, il est devenu une preuve célèbre que les oiseaux viennent des reptiles. L’âge retenu sur la pièce Solnhofen de ce site est d’environ 150 millions d’années, au Jurassique supérieur.</li>
</ul>
<h2>Ce que cette page ne dit pas</h2>
<ul>
<li>Aucune longueur du corps n’est écrite sur la pièce de Solnhofen ni sur les deux pages de musée citées ici, donc cette page ne dessine pas une personne à côté de l’animal.</li>
<li>L’épingle marque le calcaire en Bavière. Ce n’est pas le musée de Berlin, et ce n’est pas un dessin de l’animal. Le repère a été fait pour ce site. Créé par le fondateur et SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/archaeopteryx-1920.avif 1920w, @@/assets/deeptime/archaeopteryx-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/archaeopteryx-1920.webp 1920w, @@/assets/deeptime/archaeopteryx-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/archaeopteryx-1600.webp" width="1920" height="2294" alt="Le spécimen de Berlin d’Archaeopteryx lithographica, le fossile original avec les empreintes de plumes, au Museum für Naturkunde de Berlin. Pas un moulage."></picture>
<figcaption>Spécimen de Berlin d’Archaeopteryx au Museum für Naturkunde. Fossile original, pas un moulage. Emily Willoughby, CC BY-SA 4.0, via Wikimedia Commons. {_a(FOSSIL, "Page du fossile")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>{_a(BERLIN, "Museum für Naturkunde Berlin : le spécimen de Berlin")}</li>
<li>{_a(FOSSIL, "Wikimedia Commons — la photo du fossile de Berlin, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — le dessin du bandeau, CC BY-SA 3.0")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Archaeopteryx"
    if fr:
        kicker, lead = "Un dinosaure à plumes", "Des plumes, des dents, et une longue queue osseuse. Pas un oiseau ordinaire."
        credit = "Dessin : Durbed, CC BY-SA 3.0, via Wikimedia Commons. Concept d’artiste, pas une photographie."
        where, aside_h = "Où est le fossile", "Pas sur cette épingle"
        aside = "<p>L’épingle est le calcaire de Solnhofen, en Bavière. Le spécimen de Berlin est au musée, à Berlin, pas dans la carrière.</p><p><a href=\"World_Map.html?pin=Solnhofen%20Limestone%2C%20Bavaria%2C%20Germany\">Carte du monde</a></p>"
        back = '<p class="find-back"><a href="Dinosaurs.html">Dinosaures</a> · <a href="Aerial.html">Aérien</a> · <a href="Smilodon.html">Smilodon</a></p>'
    else:
        kicker, lead = "A feathered dinosaur", "Feathers, teeth, and a long bony tail. Not an ordinary bird."
        credit = "Drawing: Durbed, CC BY-SA 3.0, via Wikimedia Commons. Artist’s concept, not a photograph."
        where, aside_h = "Where the fossil is", "Not on this pin"
        aside = "<p>The pin is the Solnhofen Limestone in Bavaria. The Berlin specimen is in the museum in Berlin, not in the quarry.</p><p><a href=\"World_Map.html?pin=Solnhofen%20Limestone%2C%20Bavaria%2C%20Germany\">World Map</a></p>"
        back = '<p class="find-back"><a href="Dinosaurs.html">Dinosaurs</a> · <a href="Aerial.html">Aerial</a> · <a href="Smilodon.html">Smilodon</a></p>'
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": 48.89, "lng": 10.99, "species": "Archaeopteryx lithographica",
        "href": SOLN, "source": "Bürgermeister-Müller-Museum, Solnhofen",
        "name": "Solnhofen Limestone, Bavaria, Germany",
        "note": "The lagoons. The Berlin fossil is in the museum in Berlin.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/archaeopteryx-life-1920.avif">'
        f'<source type="image/webp" srcset="{prefix}assets/deeptime/archaeopteryx-life-1920.webp">'
        f'<img src="{prefix}assets/deeptime/archaeopteryx-life-1920.jpg" width="1920" height="1395" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(DRAW, "Page du dessin" if fr else "Drawing file page")}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-archaeopteryx.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
