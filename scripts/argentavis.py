# Argentavis magnificens. Facts are the life card already on this site.
# Campbell and Tonni, 1980. No wingspan is invented. The Trelew skeleton
# is not identified here as the type specimen.
import html, json

DOI = "https://doi.org/10.5962/p.208145"
PBDB = "https://paleobiodb.org/data1.2/occs/list.json?taxon_name=Argentavis%20magnificens&show=time"
BONE = "https://commons.wikimedia.org/wiki/File:MEF_Argentavis.jpg"
DRAW = "https://commons.wikimedia.org/wiki/File:Argentavis_magnificens.png"

META = {
"en": ("Argentavis", "Named by Campbell and Tonni in 1980 from the Huayquerian of Argentina. The Trelew skeleton is on display and is not called the type here."),
"fr": ("Argentavis d’Argentine", "Nommé par Campbell et Tonni en 1980 dans l’Huayquérien d’Argentine. Le squelette de Trelew est exposé et n’est pas appelé le type ici."),
"es": ("Argentavis de Argentina", "Nombrado por Campbell y Tonni en 1980 en el Huayqueriense de Argentina. El esqueleto de Trelew está expuesto y aquí no se llama el tipo."),
"ar": ("أرجنتافيس الأرجنتين", "أرجنتافيس ماجنيفيسنس، سمّاه كامبل وتوني سنة 1980 من الهوايكيري في الأرجنتين. هيكل تريليو معروض. لا نحدده هنا كعينة نمطية."),
"it": ("Argentavis d’Argentina", "Nominato da Campbell e Tonni nel 1980 nell’Huayqueriano dell’Argentina. Lo scheletro di Trelew è in mostra e qui non è chiamato il tipo."),
"he": ("ארגנטאביס מארגנטינה", "ארגנטאביס מגניפיסנס, שם שנתנו קמפבל וטוני ב־1980 מהוואיקריאן של ארגנטינה. השלד בטרלאו מוצג. הוא לא מזוהה כאן כטיפוס."),
}
ALT = {
"en": "Artist’s life restoration of Argentavis magnificens. This is a drawing, not a photograph.",
"fr": "Reconstitution artistique d’Argentavis magnificens. C’est un dessin, pas une photographie.",
"es": "Restauración artística de Argentavis magnificens. Es un dibujo, no una fotografía.",
"ar": "ترميم فني لأرجنتافيس ماجنيفيسنس. هذا رسم وليس صورة.",
"it": "Restauro artistico di Argentavis magnificens. È un disegno, non una fotografia.",
"he": "שחזור אמנותי של ארגנטאביס מגניפיסנס. זה ציור, לא צילום.",
}

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

def _english():
    return f'''
<p>There is no film of this animal made for this site. The picture behind the title is a drawing. The photograph lower down is a skeleton on display.</p>
<h2>What we know</h2>
<ul>
<li>Campbell and Tonni, 1980, named Argentavis magnificens from the Huayquerian of Argentina. {_a(DOI, "Campbell and Tonni, 1980")}</li>
<li>Paleobiology Database occurrences of this species are binned 8 to 5 million years ago. That file is a data table, not a museum label. {_a(PBDB, "Paleobiology Database occurrences")}</li>
<li>The photograph is a skeleton on display in Trelew. This page does not identify it as the type specimen. No wingspan is given, because this page does not invent one.</li>
<li>The pin is the museum in Trelew where that skeleton is on display. It is not the quarry. Created by the Founder and SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/argentavis-1920.avif 1920w, @@/assets/deeptime/argentavis-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/argentavis-1920.webp 1920w, @@/assets/deeptime/argentavis-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/argentavis-1600.webp" width="1920" height="1034" alt="A skeleton of Argentavis on display in Trelew. Not identified here as the type specimen."></picture>
<figcaption>Skeleton on display in Trelew. Not identified here as the type. Rique, CC0, via Wikimedia Commons. {_a(BONE, "Photograph file page")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(DOI, "Campbell and Tonni, 1980")}</li>
<li>{_a(PBDB, "Paleobiology Database occurrences of Argentavis magnificens")}</li>
<li>{_a(BONE, "Wikimedia Commons — the Trelew skeleton, CC0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — the life restoration, CC BY-SA 4.0")}</li>
</ul>'''

def _french():
    return f'''
<p>Il n’y a pas de film de cet animal pour ce site. L’image derrière le titre est un dessin. La photo plus bas est un squelette exposé.</p>
<h2>Ce que l’on sait</h2>
<ul>
<li>Campbell et Tonni, 1980, ont nommé Argentavis magnificens dans l’Huayquérien d’Argentine. {_a(DOI, "Campbell et Tonni, 1980")}</li>
<li>Les occurrences Paleobiology Database de cette espèce sont rangées de 8 à 5 millions d’années. Ce fichier est un tableau, pas une étiquette de musée. {_a(PBDB, "Occurrences Paleobiology Database")}</li>
<li>La photo est un squelette exposé à Trelew. Cette page ne l’identifie pas comme le spécimen type. Aucune envergure n’est donnée, parce que cette page n’en invente pas.</li>
<li>L’épingle est le musée de Trelew où ce squelette est exposé. Ce n’est pas la carrière. Créé par le fondateur et SI.</li>
</ul>
<figure><picture><source type="image/avif" srcset="@@/assets/deeptime/argentavis-1920.avif 1920w, @@/assets/deeptime/argentavis-1600.avif 1600w" sizes="(min-width: 900px) 720px, 100vw"><source type="image/webp" srcset="@@/assets/deeptime/argentavis-1920.webp 1920w, @@/assets/deeptime/argentavis-1600.webp 1600w" sizes="(min-width: 900px) 720px, 100vw"><img src="@@/assets/deeptime/argentavis-1600.webp" width="1920" height="1034" alt="Un squelette d’Argentavis exposé à Trelew. Pas identifié ici comme le type."></picture>
<figcaption>Squelette exposé à Trelew. Pas identifié ici comme le type. Rique, CC0, via Wikimedia Commons. {_a(BONE, "Page de la photo")}</figcaption></figure>
<h2>Sources (4)</h2>
<ul>
<li>{_a(DOI, "Campbell et Tonni, 1980")}</li>
<li>{_a(PBDB, "Occurrences Paleobiology Database d’Argentavis magnificens")}</li>
<li>{_a(BONE, "Wikimedia Commons — le squelette de Trelew, CC0")}</li>
<li>{_a(DRAW, "Wikimedia Commons — la reconstitution, CC BY-SA 4.0")}</li>
</ul>'''

def page(lang, prefix=""):
    fr = lang == "fr"
    title, desc = META[lang]
    h1 = "Argentavis"
    if fr:
        kicker, lead = "Un grand oiseau", "Un squelette exposé, pas une envergure inventée."
        credit = "Dessin : Connor Ashbridge, CC BY-SA 4.0, via Wikimedia Commons. Concept d’artiste, pas une photographie."
        where, aside_h = "Où est le squelette", "Le musée, pas la carrière"
        aside = "<p>L’épingle est le musée de Trelew, où le squelette est exposé. Ce n’est pas le lieu de découverte, et ce n’est pas une identification du type.</p>"
        back = '<p class="find-back"><a href="Aerial.html">Aérien</a> · <a href="Deep_Time.html">Temps profond</a></p>'
    else:
        kicker, lead = "A very large bird", "A skeleton on display, not an invented wingspan."
        credit = "Drawing: Connor Ashbridge, CC BY-SA 4.0, via Wikimedia Commons. Artist’s concept, not a photograph."
        where, aside_h = "Where the skeleton is", "The museum, not the quarry"
        aside = "<p>The pin is the museum in Trelew, where the skeleton is on display. It is not the discovery spot, and it is not a claim that this is the type.</p>"
        back = '<p class="find-back"><a href="Aerial.html">Aerial</a> · <a href="Deep_Time.html">Deep Time</a></p>'
    note = "" if lang in ("en", "fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en", "fr") else ' lang="en"'
    body = (_french() if fr else _english()).replace("@@/", prefix)
    pins = [{
        "lat": -43.2492366, "lng": -65.3069144, "species": "Argentavis magnificens",
        "href": DOI, "source": "OpenStreetMap way 187760836, the museum",
        "name": "Museo Paleontológico Egidio Feruglio, Trelew, Argentina",
        "note": "The museum where the skeleton is on display. Not the quarry.",
    }]
    blob = json.dumps(pins, ensure_ascii=False).replace("<", "\\u003c")
    hero = (
        f'<section class="sm-hero"><picture>'
        f'<source type="image/avif" srcset="{prefix}assets/deeptime/life-argentavis.avif">'
        f'<img src="{prefix}assets/deeptime/life-argentavis.webp" width="1600" height="1292" alt="{html.escape(ALT[lang])}" fetchpriority="high" decoding="async">'
        f'</picture><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
        f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p>'
        f'<p class="sm-credit">{credit} {_a(DRAW, "Page du dessin" if fr else "Drawing file page")}</p>'
        f'</div></section>'
    )
    main = (
        f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{body}'
        f'<section><h2>{where}</h2>'
        f'<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/deeptime/pin-argentavis.svg" role="region" aria-label="{h1}"></div>'
        f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
        f'<script type="application/json" id="sm-sites">{blob}</script></section>{back}</div></main>'
    )
    return title, desc, main
