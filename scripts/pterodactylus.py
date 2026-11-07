# Pterodactylus dossier. Age and place are the deep-time entry already on the site.
# There is no film. The life drawing is 931 pixels wide, so it is not stretched
# behind the title. The hero is the Solnhofen fossil photograph. The crest on
# the drawing is the artist's speculation, and no wingspan is measured here.
import html, json

PBDB = "https://paleobiodb.org/classic/basicTaxonInfo?taxon_no=156644"
FOSSIL = "https://commons.wikimedia.org/wiki/File:Fossil_of_Pterodactylus_antiquus_from_Solnhofen.jpg"
DRAW = "https://commons.wikimedia.org/wiki/File:Pterodactylus_BMMS7_life.png"
SOLN = "https://www.museum-solnhofen.de/"

META = {
"en": ("Pterodactylus", "A Solnhofen pterosaur. The type of Pterodactylus antiquus is Tithonian, and the fossil photograph is not Archaeopteryx."),
"fr": ("Pterodactylus de Solnhofen", "Un ptérosaure de Solnhofen. Le type de Pterodactylus antiquus est du Tithonien, et la photo du fossile n’est pas Archaeopteryx."),
"es": ("Pterodactylus de Solnhofen", "Un pterosaurio de Solnhofen. El tipo de Pterodactylus antiquus es del Titoniense, y la foto del fósil no es Archaeopteryx."),
"ar": ("بتروداكتيلوس من سولنهوفن", "زاحف طائر من سولنهوفن. نمط بتروداكتيلوس أنتيكوس من التيثوني، وصورة الأحفورة ليست أركيوبتركس."),
"it": ("Pterodactylus di Solnhofen", "Uno pterosauro di Solnhofen. Il tipo di Pterodactylus antiquus è del Titoniano, e la foto del fossile non è Archaeopteryx."),
"he": ("פטרודקטיליוס מסולנהופן", "פטרוזאור מסולנהופן. הטיפוס של פטרודקטיליוס אנטיקווס הוא מהטיתוניאן, וצילום המאובן אינו ארכאופטריקס."),
}
ALT = {
"en": "Fossil of Pterodactylus antiquus from the Solnhofen Limestone. This is not Archaeopteryx.",
"fr": "Fossile de Pterodactylus antiquus du calcaire de Solnhofen. Ce n’est pas Archaeopteryx.",
"es": "Fósil de Pterodactylus antiquus de la caliza de Solnhofen. No es Archaeopteryx.",
"ar": "أحفورة بتروداكتيلوس أنتيكوس من حجر سولنهوفن الجيري. هذه ليست أركيوبتركس.",
"it": "Fossile di Pterodactylus antiquus dal calcare di Solnhofen. Non è Archaeopteryx.",
"he": "מאובן של פטרודקטיליוס אנטיקווס מאבן הגיר של זולנהופן. זה אינו ארכאופטריקס.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is the fossil. The life drawing is 931 pixels wide, so this page does not stretch it across the title.</p>
<h2>What we know</h2>
<ul>
<li>Pterodactylus antiquus is a pterosaur from the Solnhofen lagoons in Bavaria. The Paleobiology Database places the type in the Tithonian, 149.2 to 143.1 million years ago on this map’s scale. This site’s Solnhofen coin rounds those same lagoons to about 150 million years ago. {_a(PBDB, "Paleobiology Database, taxon 156644")} {_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>The photograph behind the title is a fossil from Solnhofen. It is not Archaeopteryx. The original file is 4128 pixels wide. This page serves 1920 pixels wide, not enlarged. {_a(FOSSIL, "Fossil file page")}</li>
<li>The drawing below is Matthew Martyniuk’s life restoration of specimen BMMS 7, which he describes as the largest known Pterodactylus antiquus. He writes that the crest shape is based on specimen BSP 1929 and was made speculatively larger for a more mature stage. It is a drawing, not a photograph, and the crest is not a measurement. The file is 931 pixels wide, and this page does not enlarge it. {_a(DRAW, "Drawing file page")}</li>
</ul>
<h2>What this page does not claim</h2>
<ul>
<li>No wingspan is written on this site’s Solnhofen entry or on the Paleobiology Database page linked here, so this page does not draw a person beside the animal.</li>
<li>The pin is the Solnhofen Limestone, the same lagoons as Archaeopteryx. It is a place marker made for this site, not a drawing of the pterosaur. Created by the Founder and SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/pterodactylus-life-931.avif"><source type="image/webp" srcset="@@/assets/deeptime/pterodactylus-life-931.webp"><img src="@@/assets/deeptime/pterodactylus-life-931.png" width="931" height="438" alt="Life restoration of Pterodactylus antiquus specimen BMMS 7. The crest is the artist’s speculation. The file is 931 pixels wide. This is a drawing, not a photograph."></picture>
<figcaption>Life restoration of BMMS 7. The crest is speculative. The file is 931 pixels wide, and this page does not enlarge it. Matthew Martyniuk, CC BY-SA 4.0, via Wikimedia Commons. {_a(DRAW, "Drawing file page")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(PBDB, "Paleobiology Database, taxon 156644")}</li>
<li>{_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>{_a(FOSSIL, "Wikimedia Commons — the Solnhofen fossil photograph, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the life drawing, CC BY-SA 4.0")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal fait pour ce site. L’image derrière le titre est le fossile. Le dessin de l’animal vivant fait 931 pixels de large, donc cette page ne l’étire pas derrière le titre.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Pterodactylus antiquus est un ptérosaure des lagunes de Solnhofen, en Bavière. La Paleobiology Database place le type dans le Tithonien, de 149,2 à 143,1 millions d’années sur cette échelle. La pièce de Solnhofen de ce site arrondit ces mêmes lagunes à environ 150 millions d’années. {_a(PBDB, "Paleobiology Database, taxon 156644")} {_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>La photographie derrière le titre est un fossile de Solnhofen. Ce n’est pas Archaeopteryx. Le fichier d’origine fait 4128 pixels de large. Cette page en sert 1920, sans agrandir. {_a(FOSSIL, "Page du fossile")}</li>
<li>Le dessin plus bas est la reconstitution de Matthew Martyniuk du spécimen BMMS 7, qu’il décrit comme le plus grand Pterodactylus antiquus connu. Il écrit que la forme de la crête s’appuie sur le spécimen BSP 1929 et a été agrandie de façon spéculative pour un stade plus mûr. C’est un dessin, pas une photographie, et la crête n’est pas une mesure. Le fichier fait 931 pixels de large, et cette page ne l’agrandit pas. {_a(DRAW, "Page du dessin")}</li>
</ul>
<h2>Ce que cette page ne dit pas</h2>
<ul>
<li>Aucune envergure n’est écrite sur l’entrée de Solnhofen de ce site ni sur la page Paleobiology Database citée ici, donc cette page ne dessine pas une personne à côté de l’animal.</li>
<li>L’épingle est le calcaire de Solnhofen, les mêmes lagunes qu’Archaeopteryx. C’est un repère fait pour ce site, pas un dessin du ptérosaure. Créé par le fondateur et SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/pterodactylus-life-931.avif"><source type="image/webp" srcset="@@/assets/deeptime/pterodactylus-life-931.webp"><img src="@@/assets/deeptime/pterodactylus-life-931.png" width="931" height="438" alt="Reconstitution de Pterodactylus antiquus, spécimen BMMS 7. La crête est une supposition de l’artiste. Le fichier fait 931 pixels de large. C’est un dessin, pas une photographie."></picture>
<figcaption>Reconstitution de BMMS 7. La crête est spéculative. Le fichier fait 931 pixels de large, et cette page ne l’agrandit pas. Matthew Martyniuk, CC BY-SA 4.0, via Wikimedia Commons. {_a(DRAW, "Page du dessin")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(PBDB, "Paleobiology Database, taxon 156644")}</li>
<li>{_a(SOLN, "Bürgermeister-Müller-Museum, Solnhofen")}</li>
<li>{_a(FOSSIL, "Wikimedia Commons — la photo du fossile de Solnhofen, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — le dessin, CC BY-SA 4.0")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Pterodactylus"
    if fr:
        kicker, lead = "Un ptérosaure de Solnhofen", "Pas Archaeopteryx. Un fossile des mêmes lagunes, et un dessin dont la crête est une supposition."
        credit = "Fossile : Dean Falk Schnabel, CC BY-SA 4.0, via Wikimedia Commons. Pterodactylus antiquus de Solnhofen. Ce n’est pas Archaeopteryx."
        where, aside_h = "Où est le fossile", "Les mêmes lagunes"
        aside = "<p>L’épingle est le calcaire de Solnhofen, en Bavière, le même lieu que la page Archaeopteryx.</p><p><a href=\"World_Map.html?pin=Solnhofen%20Limestone%2C%20Bavaria%2C%20Germany\">Carte du monde</a></p>"
        back = '<p class="find-back"><a href="Aerial.html">Aérien</a> · <a href="Archaeopteryx.html">Archaeopteryx</a> · <a href="Meganeura.html">Meganeura</a></p>'
        file_label = "Page du fossile"
    else:
        kicker, lead = "A Solnhofen pterosaur", "Not Archaeopteryx. A fossil from the same lagoons, and a drawing whose crest is a guess."
        credit = "Fossil: Dean Falk Schnabel, CC BY-SA 4.0, via Wikimedia Commons. Pterodactylus antiquus from Solnhofen. This is not Archaeopteryx."
        where, aside_h = "Where the fossil is", "The same lagoons"
        aside = "<p>The pin is the Solnhofen Limestone in Bavaria, the same place as the Archaeopteryx page.</p><p><a href=\"World_Map.html?pin=Solnhofen%20Limestone%2C%20Bavaria%2C%20Germany\">World Map</a></p>"
        back = '<p class="find-back"><a href="Aerial.html">Aerial</a> · <a href="Archaeopteryx.html">Archaeopteryx</a> · <a href="Meganeura.html">Meganeura</a></p>'
        file_label = "Fossil file page"
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": 48.89, "lng": 10.99, "species": "Pterodactylus antiquus",
        "href": PBDB, "source": "Paleobiology Database, taxon 156644",
        "name": "Solnhofen Limestone, Bavaria, Germany",
        "note": "The lagoons. The same pin as Archaeopteryx.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/pterodactylus-1920.avif">'
        f'<source type="image/webp" srcset="{prefix}assets/deeptime/pterodactylus-1920.webp">'
        f'<img src="{prefix}assets/deeptime/pterodactylus-1920.webp" width="1920" height="1440" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(FOSSIL, file_label)}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-pterodactylus.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
