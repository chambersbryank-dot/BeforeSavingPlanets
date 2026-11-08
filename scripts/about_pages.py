# About, Ways to Help, and Myth vs Fact.
# Visual shell follows the Saving Planets About page: a title film, then a grid of cards.
# Facts are only ones this site already states. No sponsor program and no new partners.
import html
import support

PLAY = {"en": "Play", "fr": "Lecture", "es": "Reproducir", "it": "Riproduci", "ar": "تشغيل", "he": "הפעלה"}
NOTE = {
    "en": "",
    "fr": '<p class="bsp-ph" role="note">TODO machine-draft translation: the paragraphs below are English for review.</p>',
    "es": '<p class="bsp-ph" role="note">TODO machine-draft translation: the paragraphs below are English for review.</p>',
    "ar": '<p class="bsp-ph" role="note">TODO machine-draft translation: the paragraphs below are English for review.</p>',
    "it": '<p class="bsp-ph" role="note">TODO machine-draft translation: the paragraphs below are English for review.</p>',
    "he": '<p class="bsp-ph" role="note">TODO machine-draft translation: the paragraphs below are English for review.</p>',
}
# Still frames already on the site. Lava and first oceans are labeled interpretations.
# The last frame is the NASA Blue Marble and is the reduced-motion still.
FILM = [
    ("assets/hero/molten-earth.webp", ""),
    ("assets/hero/morph/era-oceans.webp", ""),
    ("assets/deep/photo-earth.webp", "is-still-frame"),
]
# NASA photographs already used on the deep pages. Not the flat PALEOMAP continent frames.
MAPS = [
    ("assets/deep/photo-pacific.webp", ""),
    ("assets/deep/photo-gibraltar.webp", ""),
    ("assets/deep/photo-earth.webp", "is-still-frame"),
]
FILM_CREDIT = (
    "Lava and the first oceans are an artist’s interpretation, Created by the Founder and SI, not a photograph. "
    "The last frame is the Blue Marble, Earth photographed from Apollo 17 on 7 December 1972, NASA, public domain."
)
MAP_CREDIT = (
    "Photographs only. Clouds over the northwestern Pacific, International Space Station, NASA, public domain. "
    "Strait of Gibraltar, 30 December 2016, Jeff Schmaltz, NASA, public domain. "
    "When motion is off, the still is the Blue Marble, Apollo 17, 7 December 1972, NASA, public domain."
)
CHECKS = [
    ("age", "earth", "Earth’s age is one number",
     "Earth is 4.6 billion years old, and that is the only number.",
     "The U.S. Geological Survey dates Earth at 4.54 billion years, with an uncertainty under one percent. NASA dates the birth of the solar system at about 4.6 billion years. This site keeps both sentences.",
     "The two numbers are not the same event. “About” stays on the solar-system age.",
     [("U.S. Geological Survey — Age of the Earth", "https://pubs.usgs.gov/gip/geotime/age.html"),
      ("NASA — Formation of the Solar System", "https://mobile.arc.nasa.gov/public/iexplore/missions/pages/yss/november.html")]),
    ("tiger", "animals", "Saber-toothed tiger",
     "Smilodon is a saber-toothed tiger.",
     "Smilodon is in the cat family. Saber-toothed cats are an extinct branch of that family. Tigers are a different branch, the living cat Panthera tigris. The La Brea Tar Pits museum says the nickname is the wrong animal.",
     "The nickname is old. The animal it names is not a tiger.",
     [("La Brea Tar Pits — Smilodon, saber-tooths, and tigers", "https://tarpits.org/stories/smilodon-saber-tooths-and-tigersoh-my"),
      ("This site’s Smilodon page", "Smilodon.html")]),
    ("birds", "animals", "The asteroid and the birds",
     "The asteroid killed every dinosaur, and birds are a separate story.",
     "The quest layer says an asteroid about 10 to 20 kilometers wide struck near today’s Yucatán. About 76 percent of species died out, including all dinosaurs except birds.",
     "“About 76 percent” and “10 to 20 kilometers” are the figures on that layer. They are not a new count made for this card.",
     [("National Park Service — Mass extinctions", "https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm"),
      ("The quest layer", "Quest.html")]),
    ("bin", "animals", "Mosasaurus outlived the dinosaurs",
     "Mosasaurus lived on after the dinosaurs died.",
     "Mosasaurus hoffmannii lived in the Campanian and Maastrichtian. Most records are Late Maastrichtian. That age ends at the close of the Cretaceous, about 66 million years ago. The animal did not live after that.",
     "The Paleobiology Database bins those occurrences from the Campanian through the Maastrichtian. The oldest bin on this timescale starts at 83.6 million years ago. The same list stores a younger bin edge at 61.66 million years. That edge is later than about 66 million years ago. It is a bin boundary, not a life date, and this site does not use it as the animal’s age.",
     [("Paleobiology Database — Mosasaurus hoffmannii", "https://paleobiodb.org/data1.2/occs/list.json?taxon_name=Mosasaurus%20hoffmannii&show=time"),
      ("This site’s Mosasaurus page", "Mosasaurus.html")]),
    ("hills", "earth", "The Jack Hills photograph",
     "The Jack Hills photograph is a picture of the 4.4-billion-year crystal.",
     "A zircon from the Jack Hills of Western Australia is 4.404 billion years old. The quest photograph is the host rock. It is not a microscope photo of that one crystal.",
     "The paper’s chemistry points to continental crust and liquid water. This card does not add a new measurement.",
     [("Wilde and others, Nature, 2001", "https://doi.org/10.1038/35051550"),
      ("The quest layer", "Quest.html")]),
    ("film", "animals", "The Borealopelta film",
     "The Borealopelta film shows a measured eye, spine, and skin.",
     "The film is an artist’s reconstruction, Created by the Founder and SI, kept whole. The 2017 paper found a reddish-brown pigment signature. Melanosome shapes were not preserved.",
     "The eye, spines, and skin texture are the artist’s interpretation. The fossil meal and the pigment result are the sourced parts.",
     [("Brown and others, Current Biology, 2017", "https://www.cell.com/current-biology/fulltext/S0960-9822(17)30808-4"),
      ("This site’s Borealopelta page", "Borealopelta.html")]),
]
SOURCES = [
    ("U.S. Geological Survey — Age of the Earth", "https://pubs.usgs.gov/gip/geotime/age.html", "The 4.54-billion-year age used on this site."),
    ("NASA Earth Observatory", "https://earthobservatory.nasa.gov/", "Satellite views cited on the deep pages."),
    ("Paleobiology Database", "https://paleobiodb.org/", "Find pages cite collection records from here."),
    ("Yale Peabody Museum", "https://peabody.yale.edu/", "Named on the continents sources."),
    ("Harvard Earth and Planetary Sciences", "https://eps.harvard.edu/", "Named on the continents sources. A citation, not a partnership."),
    ("Smithsonian National Museum of Natural History", "https://naturalhistory.si.edu/", "A museum named in the source list."),
    ("Natural History Museum, London", "https://www.nhm.ac.uk/", "A museum named in the source list."),
    ("UC Museum of Paleontology, Berkeley", "https://ucmp.berkeley.edu/", "A museum named in the source list."),
    ("International Commission on Stratigraphy", "https://stratigraphy.org/chart", "The chart named on the policy page."),
]


def _e(text):
    return html.escape(text)


def _frames(prefix, frames):
    bits = []
    for src, cls in frames:
        bits.append(
            f'<img src="{html.escape(prefix + src, quote=True)}" alt="" class="{cls}" decoding="async">'
        )
    return f'<div class="bsp-frames" aria-hidden="true">{"".join(bits)}</div>'


def _pause(pause, play):
    return (
        f'<button type="button" class="bsp-pause" aria-pressed="false" data-play="{_e(play)}">{_e(pause)}</button>'
    )


def title_band(prefix, frames, title, desc, credit, pause, play):
    return (
        f'<section class="page-hero bsp-title-film">{_frames(prefix, frames)}'
        f'<div class="bsp-title-shade" aria-hidden="true"></div>'
        f'<div class="bsp-title-copy"><div class="bsp-title-crystal"><h1>{_e(title)}</h1><p>{_e(desc)}</p></div>'
        f'<p class="bsp-title-credit">{_e(credit)}</p></div>{_pause(pause, play)}</section>'
    )


def _cards(rows):
    body = []
    for title, text in rows:
        body.append(f'<section class="w-card"><h3>{_e(title)}</h3><p>{text}</p></section>')
    return f'<div class="ws-grid">{"".join(body)}</div>'


def about(lang, prefix, t):
    pause = t["pause"]
    play = PLAY[lang]
    sister = html.escape("https://www.savingplanets.com/", quote=True)
    mail = html.escape(t["email"], quote=True)
    aim = _cards([
        ("The aim", _e("Show the fossil record in plain language, with the source next to the claim. No invented body length. No cartoon Earth.")),
        ("What we cover", _e("Dinosaurs, mammals, animals of the air, animals of the sea, a world map of finds, and Deep Time. Education pages outline geology and archaeology.")),
        ("The mission", _e("Saving Planets shows solutions for the living world. This site shows the record those solutions sit on: climates, ecosystems, and life through deep time.")),
        ("Write to us", f'<a href="mailto:{mail}">{_e(t["email"])}</a>. ' + _e("That is the Saving Planets inbox until a Before Saving Planets address exists.")),
    ])
    rules = _cards([
        ("A source you can open", _e("A date or a claim on a finished page links to a paper, a museum, a survey, or a park service page.")),
        ("A picture is labeled", _e("A photograph says who made it. An artist’s reconstruction says Created by the Founder and SI. A map says which model drew the coastlines.")),
        ("No invented measure", _e("A body length appears only when a cited source gives that length. A file note from an artist is not a measurement.")),
        ("Help goes to the museum", _e("Donate and volunteer buttons open the museum that holds the fossil. This site is free and asks for nothing for itself.")),
    ])
    team = (
        '<div class="ws-grid bsp-team">'
        '<section class="w-card"><h3>The Founder</h3><p>Sets the direction and approves the pages.</p></section>'
        '<section class="w-card"><h3>SI</h3><p>Researches, drafts, and checks the sources. The credit line is Created by the Founder and SI.</p></section>'
        f'<section class="w-card"><h3>Volunteers</h3><p>Language corrections are welcome at <a href="mailto:{mail}">{_e(t["email"])}</a>.</p></section>'
        '</div>'
    )
    sources = _cards([(name, f'{_e(line)} <a href="{html.escape(url, quote=True)}">{_e(name)}</a>') for name, url, line in SOURCES])
    rest = _cards([
        ("Sister site", f'<a href="{sister}">www.savingplanets.com</a>. ' + _e("Before Saving Planets does not run a sponsor program and does not list partners. A museum link is a citation or a way to help that museum, not a partnership.")),
        ("Analytics", _e("Home, About, Learn, and the other adult pages load Cloudflare Web Analytics. Kids and Kids Map do not load that script.")),
        ("Newsletter", _e("Adult pages can show the Weekly Before Saving Planets Brief signup. Kids and Kids Map do not show the form, and they do not send the event beacon. This is not a claim about Safari’s own privacy notice.")),
        ("Use", _e("Read the pages in class. Third-party images keep the credit printed beside them. Pictures and films made for this site stay credited Created by the Founder and SI. Questions about reuse go to the contact address.")),
    ])
    hero = (
        f'<section class="page-hero bsp-title-film">{_frames(prefix, FILM)}'
        f'<div class="bsp-title-shade" aria-hidden="true"></div>'
        f'<div class="bsp-title-copy bsp-title-crystal"><h1>About</h1><p>{_e(t["d_about"])}</p>'
        f'<p class="bsp-title-credit">{_e(FILM_CREDIT)}</p></div>{_pause(pause, play)}</section>'
    )
    return (
        f'<main id="main">{hero}<div class="bsp-about">{NOTE[lang]}'
        f'<h2>Before Saving Planets</h2>{aim}'
        f'<h2>How a page earns its place</h2>{rules}'
        f'<h2>Who builds this</h2>{team}'
        f'<p class="bsp-team-credit">Created by the Founder and SI</p>'
        f'<h2>Sources named on this site</h2>'
        f'<p>These are sources the pages already link. A link is not an endorsement and not a partnership. This list does not count pages.</p>'
        f'{sources}{rest}</div></main>'
    )


def ways(lang, prefix, t):
    pause = t["pause"]
    play = PLAY[lang]
    rows = []
    for slug, org in support.ORGS.items():
        bits = []
        if org["donate"]:
            bits.append(f'<a href="{html.escape(org["donate"], quote=True)}">{_e(support.T[lang]["d"])}</a>')
        if org["vol"]:
            bits.append(f'<a href="{html.escape(org["vol"], quote=True)}">{_e(support.T[lang]["v"])}</a>')
        links = " · ".join(bits)
        rows.append((slug, f'<span lang="en">{_e(org["org"])}</span>. {links}'))
    museums = _cards(rows)
    sister = html.escape(support._sp(lang), quote=True)
    more = _cards([
        ("This site", _e("Before Saving Planets is free and asks for nothing for itself. The find pages name the museum that cares for the fossil.")),
        ("Where a gift goes", _e(support.T[lang]["rule"])),
        ("Saving Planets", f'{_e(support.totals(lang))} <a href="{sister}">{_e(support.T[lang]["sp"])}</a>'),
    ])
    hero = (
        f'<section class="page-hero bsp-title-film">{_frames(prefix, FILM)}'
        f'<div class="bsp-title-shade" aria-hidden="true"></div>'
        f'<div class="bsp-title-copy bsp-title-crystal"><h1>{_e(t["help"])}</h1><p>{_e(t["d_help"])}</p>'
        f'<p class="bsp-title-credit">{_e(FILM_CREDIT)}</p></div>{_pause(pause, play)}</section>'
    )
    return (
        f'<main id="main">{hero}<div class="bsp-about">{NOTE[lang]}'
        f'<h2>{_e(support.T[lang]["h"])}</h2>{museums}'
        f'<h2>How help is chosen</h2>{more}'
        f'<h2>{_e(support.T[lang]["sp"])}</h2>{support.hubs(lang)}'
        f'</div></main>'
    )


def _check(prefix, row):
    cid, topic, title, myth, fact, doubt, sources = row
    links = []
    for name, url in sources:
        href = url if url.startswith("http") else prefix + url
        links.append(f'<li><a href="{html.escape(href, quote=True)}">{_e(name)}</a></li>')
    blob = " ".join([title, myth, fact, doubt, topic] + [name for name, _url in sources])
    return (
        f'<article class="w-card myth-card" id="myth-{cid}" data-myth-card data-myth-topic="{topic}" data-myth-text="{_e(blob)}">'
        f'<p class="myth-tag myth-tag-myth">Myth</p><h3>{_e(title)}</h3><p>{_e(myth)}</p>'
        f'<p class="myth-tag myth-tag-fact">Fact</p><p>{_e(fact)}</p>'
        f'<p class="myth-tag myth-tag-src">Evidence</p><p class="myth-honest">{_e(doubt)}</p>'
        f'<ul class="myth-source">{"".join(links)}</ul></article>'
    )


def myth(lang, prefix, t, title):
    pause = t["pause"]
    play = PLAY[lang]
    cards = "".join(_check(prefix, row) for row in CHECKS)
    tools = (
        '<div class="myth-tools">'
        '<label class="myth-find">Search these checks <input type="search" data-myth-q placeholder="Try tiger, zircon, or 4.54" aria-label="Search these checks"></label>'
        '<div class="myth-filters" role="group" aria-label="Filter checks">'
        '<button type="button" class="edu-crystal" data-myth-filter="all" aria-pressed="true">All</button>'
        '<button type="button" class="edu-crystal" data-myth-filter="earth" aria-pressed="false">Earth</button>'
        '<button type="button" class="edu-crystal" data-myth-filter="animals" aria-pressed="false">Animals</button>'
        '</div></div>'
        '<p class="w-card" data-myth-empty hidden>Nothing on this page matches. This box searches these six cards only. It does not research the web.</p>'
    )
    video = prefix + "assets/finds/borealopelta-founder-1280.mp4"
    still = prefix + "assets/finds/borealopelta-title-still.webp"
    credit = "Artist’s reconstruction of Borealopelta. Created by the Founder and SI. Not a photograph."
    script = (
        "<script>(function(){document.querySelectorAll('.sp-anim-banner.has-pause .spb-pause').forEach(function(btn){"
        "var b=btn.closest('.sp-anim-banner');btn.addEventListener('click',function(){var held=btn.getAttribute('aria-pressed')!=='true';"
        "btn.setAttribute('aria-pressed',held);btn.innerHTML=held?'&#9654;':'&#10074;&#10074;';b.classList.toggle('spb-paused',held);"
        "var v=b.querySelector('video');if(v){if(held)v.pause();else v.play();}})})})();</script>"
    )
    return (
        f'<main id="main" class="bsp-myth" data-myth>'
        f'<section class="page-hero sp-anim-banner has-pause has-video is-playing">'
        f'<video class="spb-video" autoplay muted loop playsinline poster="{still}" width="1280" height="726">'
        f'<source src="{video}" type="video/mp4"></video>'
        f'<img class="bsp-title-still" src="{still}" alt="" width="1280" height="726">'
        f'<span class="spb-sweep" aria-hidden="true"></span>'
        f'<div class="page-hero-content"><h1>{_e(title)}</h1>'
        f'<p>Six checks a seventh grader and a geologist can read. Each card names its myth, the sourced fact, and the evidence.</p>'
        f'<p class="hero-credit">{_e(credit)}</p></div>'
        f'<button type="button" class="spb-pause" aria-pressed="false" aria-label="Pause banner animation">&#10074;&#10074;</button>'
        f'</section>{script}'
        f'<div class="bsp-about">{NOTE[lang]}{tools}'
        f'<div class="ws-grid myth-grid">{cards}</div></div></main>'
    )
