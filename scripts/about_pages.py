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
MAPS = [
    ("assets/hero/paleo/m540.webp", ""),
    ("assets/hero/paleo/m360.webp", ""),
    ("assets/hero/paleo/m180.webp", ""),
    ("assets/deep/photo-earth.webp", "is-still-frame"),
]
FILM_CREDIT = (
    "Lava and the first oceans are an artist’s interpretation, Created by the Founder and SI, not a photograph. "
    "The last frame is the Blue Marble, Earth photographed from Apollo 17 on 7 December 1972, NASA, public domain."
)
MAP_CREDIT = (
    "The moving maps are flat Scotese PALEOMAP reconstructions via GPlates (EarthByte), not a cartoon globe. "
    "When motion is off, the still is the NASA Blue Marble, public domain."
)
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
        f'<div class="bsp-title-copy"><h1>About</h1><p>{_e(t["d_about"])}</p>'
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
        f'<div class="bsp-title-copy"><h1>{_e(t["help"])}</h1><p>{_e(t["d_help"])}</p>'
        f'<p class="bsp-title-credit">{_e(FILM_CREDIT)}</p></div>{_pause(pause, play)}</section>'
    )
    return (
        f'<main id="main">{hero}<div class="bsp-about">{NOTE[lang]}'
        f'<h2>{_e(support.T[lang]["h"])}</h2>{museums}'
        f'<h2>How help is chosen</h2>{more}'
        f'<h2>{_e(support.T[lang]["sp"])}</h2>{support.hubs(lang)}'
        f'</div></main>'
    )


def myth(lang, prefix, t, title):
    pause = t["pause"]
    play = PLAY[lang]
    pending = _cards([
        ("The checks", _e("This page is the place for Earth and fossil claims checked against a source. Those checks are not written yet.")),
        ("What stays readable", _e("The maps move behind this panel. The words sit on the card so they stay readable. Reduced motion keeps one still photograph.")),
    ])
    sources = _cards([
        (name, f'{_e(line)} <a href="{html.escape(url, quote=True)}">{_e(name)}</a>')
        for name, url, line in SOURCES
    ])
    return (
        f'<main id="main" class="bsp-myth">{_frames(prefix, MAPS)}'
        f'<section class="page-hero bsp-title-film">'
        f'<div class="bsp-title-shade" aria-hidden="true"></div>'
        f'<div class="bsp-title-copy"><h1>{_e(title)}</h1><p>{_e("Claims wait for a source. The background is the approved map sequence.")}</p>'
        f'<p class="bsp-title-credit">{_e(MAP_CREDIT)}</p></div>{_pause(pause, play)}</section>'
        f'<div class="bsp-about">{NOTE[lang]}{pending}'
        f'<h2>Sources already used on this site</h2>{sources}</div></main>'
    )
