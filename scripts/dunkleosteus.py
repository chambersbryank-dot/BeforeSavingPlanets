# Dunkleosteus dossier. Facts are the Cleveland Shale coin and Engelman, 2024.
# There is no Founder-and-SI film. The life drawing on file is 634 pixels wide,
# so it is not stretched behind the title. The hero is the CMNH 5768 armor photo.
# The length in the 2024 paper is an estimate, so this page does not draw a person.
import html, json

PAPER = "https://doi.org/10.26879/1343"
SKULL = "https://commons.wikimedia.org/wiki/File:Dunkleosteus_CMNH_5768_skull.png"
DRAW = "https://commons.wikimedia.org/wiki/File:Dunkleosteus_terrelli_(2024).png"

META = {
"en": ("Dunkleosteus", "Cleveland Shale skull CMNH 5768, about 360 million years ago. The skull and belly armor are real. Some side plates are rebuilt."),
"fr": ("Dunkleosteus de Cleveland", "Le crâne CMNH 5768 du schiste de Cleveland, il y a environ 360 millions d’années. Le crâne et le ventre sont vrais. Certaines plaques sont refaites."),
"es": ("Dunkleosteus de Cleveland", "El cráneo CMNH 5768 del esquisto de Cleveland, hace unos 360 millones de años. El cráneo y el vientre son reales. Algunas placas están reconstruidas."),
"ar": ("دنكليوستيوس من كليفلاند", "جمجمة CMNH 5768 من طَفل كليفلاند، قبل نحو 360 مليون سنة. الجمجمة ودرع البطن حقيقيان. بعض الصفائح الجانبية معاد بناؤها."),
"it": ("Dunkleosteus di Cleveland", "Il cranio CMNH 5768 dello scisto di Cleveland, circa 360 milioni di anni fa. Cranio e ventre sono veri. Alcune piastre laterali sono ricostruite."),
"he": ("דנקליאוסטיוס מקליבלנד", "גולגולת CMNH 5768 מפצלי קליבלנד, לפני כ־360 מיליון שנה. הגולגולת ושריון הבטן אמיתיים. חלק מלוחות הצד משוחזרים."),
}
ALT = {
"en": "Skull of Dunkleosteus terrelli, Cleveland Museum specimen CMNH 5768. The skull and belly armor are real. Some side plates are rebuilt.",
"fr": "Crâne de Dunkleosteus terrelli, spécimen CMNH 5768 du musée de Cleveland. Le crâne et l’armure du ventre sont vrais. Certaines plaques latérales sont reconstruites.",
"es": "Cráneo de Dunkleosteus terrelli, ejemplar CMNH 5768 del museo de Cleveland. El cráneo y la armadura del vientre son reales. Algunas placas laterales están reconstruidas.",
"ar": "جمجمة دنكليوستيوس تيريلي، العيّنة CMNH 5768 في متحف كليفلاند. الجمجمة ودرع البطن حقيقيان. بعض الصفائح الجانبية معاد بناؤها.",
"it": "Cranio di Dunkleosteus terrelli, esemplare CMNH 5768 del museo di Cleveland. Il cranio e l’armatura del ventre sono veri. Alcune piastre laterali sono ricostruite.",
"he": "גולגולת של דנקליאוסטיוס טרלי, פריט CMNH 5768 במוזיאון קליבלנד. הגולגולת ושריון הבטן אמיתיים. חלק מלוחות הצד משוחזרים.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is the fossil armor. The life drawing is only 634 pixels wide, so this page does not stretch it across the title.</p>
<h2>What we know</h2>
<ul>
<li>Before animals with legs were common, the seas had armored hunters. Dunkleosteus, from the shale under Cleveland, wore a bony helmet and had self-sharpening jaw blades instead of teeth. The age used on this site’s Cleveland Shale coin is about 360 million years ago, near the end of the Devonian.</li>
<li>The photograph is skull CMNH 5768 at the Cleveland Museum of Natural History. The skull and the belly armor are real. Some of the side plates are rebuilt. {_a(SKULL, "Fossil file page")} {_a(PAPER, "Engelman, 2024")}</li>
<li>Engelman, 2024, gives about 3.0 to 3.4 metres for subadults to typical adults, and about 4.1 metres for the largest individuals, from the method in his 2023 study. The same paper says lengths a little higher, about 3.8 and 4.5 metres, remain possible, and that the old pictures of an 8 to 10 metre fish are not supported. The body behind the armor is poorly known, so these are estimates, not a tape measure.</li>
<li>The small drawing is an artist’s concept of that shorter fish. It is not a photograph. The file is 634 pixels wide, and this page does not enlarge it. {_a(DRAW, "Drawing file page")}</li>
</ul>
<h2>What this page does not claim</h2>
<ul>
<li>A typical adult estimate of about 3 to 3.4 metres is longer than a person. This page does not draw a person beside the fish, because the length is an estimate and the tail is poorly known.</li>
<li>The pin is Doan Brook in Cleveland, the brook the Cleveland Shale was named for. Armor has been found in that shale under the city and in nearby counties, not in one single hole. The marker was made for this site. Created by the Founder and SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/dunkleosteus-life-634.avif"><source type="image/webp" srcset="@@/assets/deeptime/dunkleosteus-life-634.webp"><img src="@@/assets/deeptime/dunkleosteus-life-634.png" width="634" height="393" alt="Artist’s concept of Dunkleosteus terrelli with a shorter body than the old museum monsters. The file is 634 pixels wide. This is a drawing, not a photograph."></picture>
<figcaption>Artist’s concept of the shorter body. The file is 634 pixels wide, and this page does not enlarge it. PlacodermReconstructions, CC BY 4.0, via Wikimedia Commons. {_a(DRAW, "Drawing file page")}</figcaption></figure>
<h2>Sources (3)</h2>
<ul>
<li>{_a(PAPER, "Engelman, 2024, Palaeontologia Electronica")}</li>
<li>{_a(SKULL, "Wikimedia Commons — skull CMNH 5768, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the 2024 life drawing, CC BY 4.0")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal fait pour ce site. L’image derrière le titre est l’armure fossile. Le dessin de l’animal vivant ne fait que 634 pixels de large, donc cette page ne l’étire pas derrière le titre.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Avant que les animaux à pattes soient courants, les mers avaient des chasseurs cuirassés. Dunkleosteus, du schiste sous Cleveland, portait un casque osseux et des lames de mâchoire qui s’aiguisaient, à la place des dents. L’âge retenu sur la pièce du schiste de Cleveland de ce site est d’environ 360 millions d’années, vers la fin du Dévonien.</li>
<li>La photographie est le crâne CMNH 5768, au Cleveland Museum of Natural History. Le crâne et l’armure du ventre sont vrais. Certaines plaques latérales sont reconstruites. {_a(SKULL, "Page du fossile")} {_a(PAPER, "Engelman, 2024")}</li>
<li>Engelman, 2024, donne environ 3,0 à 3,4 mètres pour les subadultes et les adultes typiques, et environ 4,1 mètres pour les plus grands, d’après la méthode de son étude de 2023. Le même article dit que des longueurs un peu plus hautes, environ 3,8 et 4,5 mètres, restent possibles, et que les anciennes images d’un poisson de 8 à 10 mètres ne tiennent pas. Le corps derrière l’armure est mal connu, donc ce sont des estimations, pas un mètre ruban.</li>
<li>Le petit dessin est un concept d’artiste de ce poisson plus court. Ce n’est pas une photographie. Le fichier fait 634 pixels de large, et cette page ne l’agrandit pas. {_a(DRAW, "Page du dessin")}</li>
</ul>
<h2>Ce que cette page ne dit pas</h2>
<ul>
<li>Une estimation d’environ 3 à 3,4 mètres pour un adulte typique est plus longue qu’une personne. Cette page ne dessine pas une personne à côté du poisson, parce que la longueur est une estimation et que la queue est mal connue.</li>
<li>L’épingle est le ruisseau Doan, à Cleveland, le ruisseau qui a donné son nom au schiste. L’armure a été trouvée dans ce schiste sous la ville et dans les comtés voisins, pas dans un seul trou. Le repère a été fait pour ce site. Créé par le fondateur et SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/dunkleosteus-life-634.avif"><source type="image/webp" srcset="@@/assets/deeptime/dunkleosteus-life-634.webp"><img src="@@/assets/deeptime/dunkleosteus-life-634.png" width="634" height="393" alt="Concept d’artiste de Dunkleosteus terrelli, au corps plus court que les anciens monstres de musée. Le fichier fait 634 pixels de large. C’est un dessin, pas une photographie."></picture>
<figcaption>Concept d’artiste du corps plus court. Le fichier fait 634 pixels de large, et cette page ne l’agrandit pas. PlacodermReconstructions, CC BY 4.0, via Wikimedia Commons. {_a(DRAW, "Page du dessin")}</figcaption></figure>
<h2>Sources (3)</h2>
<ul>
<li>{_a(PAPER, "Engelman, 2024, Palaeontologia Electronica")}</li>
<li>{_a(SKULL, "Wikimedia Commons — le crâne CMNH 5768, CC BY-SA 4.0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — le dessin de 2024, CC BY 4.0")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Dunkleosteus"
    if fr:
        kicker, lead = "Un poisson cuirassé", "Un casque osseux, des lames à la place des dents, et un corps plus court que les anciens monstres de musée."
        credit = "Fossile : Russell K. Engelman, CC BY-SA 4.0, via Wikimedia Commons. Le crâne et l’armure du ventre sont vrais. Certaines plaques latérales sont reconstruites."
        where, aside_h = "Où est le fossile", "Pas un seul trou"
        aside = "<p>L’épingle est le ruisseau Doan, à Cleveland. L’armure vient du schiste sous la ville et des comtés voisins.</p><p><a href=\"World_Map.html?pin=Cleveland%20Shale%2C%20Cleveland%2C%20Ohio%2C%20USA\">Carte du monde</a></p>"
        back = '<p class="find-back"><a href="Marine.html">Vie marine</a> · <a href="Archaeopteryx.html">Archaeopteryx</a> · <a href="Smilodon.html">Smilodon</a></p>'
        file_label = "Page du fossile"
    else:
        kicker, lead = "An armored fish", "A bony helmet, blades instead of teeth, and a shorter body than the old museum monsters."
        credit = "Fossil: Russell K. Engelman, CC BY-SA 4.0, via Wikimedia Commons. The skull and the belly armor are real. Some side plates are rebuilt."
        where, aside_h = "Where the fossil is", "Not one hole"
        aside = "<p>The pin is Doan Brook in Cleveland. The armor comes from the shale under the city and from nearby counties.</p><p><a href=\"World_Map.html?pin=Cleveland%20Shale%2C%20Cleveland%2C%20Ohio%2C%20USA\">World Map</a></p>"
        back = '<p class="find-back"><a href="Marine.html">Marine</a> · <a href="Archaeopteryx.html">Archaeopteryx</a> · <a href="Smilodon.html">Smilodon</a></p>'
        file_label = "Fossil file page"
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": 41.5099, "lng": -81.614, "species": "Dunkleosteus terrelli",
        "href": PAPER, "source": "Engelman, 2024",
        "name": "Cleveland Shale, Cleveland, Ohio, USA",
        "note": "Doan Brook. The armor is from the shale under the city and nearby counties.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/dunkleosteus-1730.avif">'
        f'<source type="image/webp" srcset="{prefix}assets/deeptime/dunkleosteus-1730.webp">'
        f'<img src="{prefix}assets/deeptime/dunkleosteus-1730.webp" width="1730" height="1672" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(SKULL, file_label)}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-dunkleosteus.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
