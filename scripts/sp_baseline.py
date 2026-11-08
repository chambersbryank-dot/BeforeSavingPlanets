"""One Saving Planets chrome for this site.

The snapshot in scripts/baseline/ is Saving Planets main at COMMIT.
It is the only source for the English menu and for the About, Contact,
Ways to Help, and Search bodies. Do not restyle those pages one at a time.

After Bryan approves this baseline, set FROZEN = True. New pages call
nav_html(). Reopen the chrome only for a broken control, an accessibility
defect, or an explicit request.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "baseline")
COMMIT = "166e94d042f8e0f3d5cca2ca15024057324e5243"
FROZEN = False
SP_ORIGIN = "https://www.savingplanets.com/"
PAGES = ("About", "Contact", "Ways_to_Help", "Search")
# Saving Planets uses four photographs in this banner. This site keeps that box and
# plays the approved Borealopelta film instead of the modern spacecraft stills.
# Search has no title banner.
TITLE = "borealopelta-video"
# A file that exists here stays on this site. These names exist on both sites and are not the same page.
NOT_SAME = {"Oceans.html", "Privacy.html", "Lesson_Builder.html"}
GAPS = (
    "The shared Pagefind index on Saving Planets does not yet contain this site's pages.",
    "Search calls the live Pagefind index on www.savingplanets.com. That index does not yet contain this site's pages. The notes search on the same page still answers this site.",
    "The Saving Planets logo webp and 216px files are not in this repo. The existing 72 and 144 png files are used.",
    "The Biological SI Partner line was removed.",
    "A link with no page here points at savingplanets.com. Oceans.html, Privacy.html, and Lesson_Builder.html were not treated as the same page.",
    "The About, Contact, and Ways to Help sentences are the Saving Planets text, still in that site's name. They were not rewritten into claims about this site.",
)

_LOGO = (
    '<img src="assets/brand/sp-logo-72.png" srcset="assets/brand/sp-logo-72.png 1x, '
    'assets/brand/sp-logo-144.png 2x" width="72" height="72" alt="Before Saving Planets logo" '
    'decoding="async">'
)


def _read(name):
    path = os.path.join(BASE, name)
    if not os.path.isfile(path):
        raise SystemExit("baseline snapshot missing: " + path)
    return open(path, encoding="utf-8").read()


def _local(path):
    full = os.path.normpath(os.path.join(ROOT, path))
    return full.startswith(ROOT + os.sep) and os.path.isfile(full)


HELP = {
    "en": "Help / Donate",
    "fr": "Aider / Faire un don",
    "es": "Ayudar / Donar",
    "ar": "ساعد / تبرّع",
    "it": "Aiuta / Dona",
    "he": "עזרה / תרומה",
}
LANGS = ("en", "fr", "es", "ar", "it", "he")


def _page_dir(lang):
    return ROOT if lang == "en" else os.path.join(ROOT, lang)


def _resolved(lang, rel):
    full = os.path.normpath(os.path.join(_page_dir(lang), rel))
    root = os.path.normpath(ROOT)
    if full != root and not full.startswith(root + os.sep):
        return ""
    return full if os.path.isfile(full) else ""


def _sp_abs(lang, rel):
    prefix = "" if lang == "en" else lang + "/"
    parts = []
    for part in (prefix + rel).split("/"):
        if part == "..":
            if parts:
                parts.pop()
        elif part not in ("", "."):
            parts.append(part)
    return SP_ORIGIN + "/".join(parts)


def rewrite_href(href, lang):
    """Keep a link that resolves here. Anything else stays on Saving Planets."""
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "?", "data:", "//")):
        return href
    base, query = (href.split("?", 1) + [""])[:2] if "?" in href else (href, "")
    path, frag = (base.split("#", 1) + [""])[:2] if "#" in base else (base, "")
    if not path or path.endswith("/"):
        return href
    name = os.path.basename(path)
    if name not in NOT_SAME and _resolved(lang, path):
        return href
    out = _sp_abs(lang, path)
    if query:
        out += "?" + query
    if frag:
        out += "#" + frag
    return out


def rewrite(html, lang):
    html = re.sub(r'<p class="biosi-cc">[\s\S]*?</p>', "", html)
    html = html.replace("Biological SI Partner", "the Founder")

    def sub(match):
        return match.group(1) + rewrite_href(match.group(2), lang) + '"'

    return re.sub(r'(href="|src=")([^"]*)"', sub, html)


def _logo(lang):
    pre = "" if lang == "en" else "../"
    return (
        f'<img src="{pre}assets/brand/sp-logo-72.png" srcset="{pre}assets/brand/sp-logo-72.png 1x, '
        f'{pre}assets/brand/sp-logo-144.png 2x" width="72" height="72" alt="Before Saving Planets logo" '
        'decoding="async">'
    )


def _snap(lang, name):
    return _read(name if lang == "en" else lang + "/" + name)


def nav_html(page, lang="en"):
    raw = _snap(lang, "nav.html")
    raw = re.sub(r"<picture>[\s\S]*?</picture>", _logo(lang), raw, count=1)

    def brand(match):
        inner = re.sub(r"(?<!Before )Saving Planets", "Before Saving Planets", match.group(2))
        return match.group(1) + inner + match.group(3)

    raw = re.sub(r'(<a class="spn-brand"[^>]*>)([\s\S]*?)(</a>)', brand, raw, count=1)
    raw = raw.replace("%2FAbout.html", "%2F" + page + ".html")
    raw = re.sub(
        r'href="([^"]*?)About\.html"( hreflang=")',
        lambda m: 'href="%s%s.html"%s' % (m.group(1), page, m.group(2)),
        raw,
    )
    raw = raw.replace(' aria-current="page"', "").replace(' aria-current="true"', "")
    raw = raw.replace(" is-current", "")
    raw = re.sub(
        r'(href="[^"]*' + re.escape(page) + r'\.html" hreflang="' + lang + r'")',
        r'\1 aria-current="true"',
        raw,
        count=1,
    )
    marked = {"done": False}

    def mark(match):
        tag = match.group(0)
        if marked["done"] or "spn-brand" in tag or "hreflang=" in tag:
            return tag
        needle = 'href="%s.html"' % page
        if needle not in tag:
            return tag
        marked["done"] = True
        return tag.replace(needle, needle + ' aria-current="page"', 1)

    raw = re.sub(r"<a\b[^>]*>", mark, raw)
    return rewrite(raw, lang)


def apply_title_video(html, lang):
    """Same banner box and pause control. The footage is the approved Borealopelta film."""
    pre = "" if lang == "en" else "../"
    video = pre + "assets/finds/borealopelta-founder-1280.mp4"
    still = pre + "assets/finds/borealopelta-title-still.webp"
    media = (
        f'<video class="spb-video" autoplay muted loop playsinline poster="{still}" width="1280" height="726">'
        f'<source src="{video}" type="video/mp4"></video>'
        f'<img class="bsp-title-still" src="{still}" alt="" width="1280" height="726">'
        '<span class="spb-sweep" aria-hidden="true"></span>'
    )
    html = html.replace("sp-anim-banner has-pause", "sp-anim-banner has-pause has-video is-playing", 1)
    html = re.sub(
        r'<!-- ANIMBAN:START -->[\s\S]*?<!-- ANIMBAN:END -->',
        '<!-- ANIMBAN:START -->' + media + '<!-- ANIMBAN:END -->',
        html,
        count=1,
    )
    credit = (
        '<span class="hero-credit spx-cred spx-c0">Artist&#8217;s reconstruction of Borealopelta. '
        'Created by the Founder and SI. Not a photograph.</span>'
    )
    html = re.sub(
        r'<!-- ANIMBAN:START --><span class="hero-credit[\s\S]*?</span>(?=<button)',
        '<!-- ANIMBAN:START -->' + credit,
        html,
        count=1,
    )
    return html.replace(
        "b.classList.toggle('spb-paused',held)",
        "b.classList.toggle('spb-paused',held);var v=b.querySelector('video');if(v){if(held)v.pause();else v.play();}",
        1,
    )


def main_html(page, lang="en"):
    html = rewrite(_snap(lang, page + ".html"), lang)
    if page in ("About", "Contact", "Ways_to_Help"):
        html = apply_title_video(html, lang)
    return html


def menu_links(html):
    start = html.find('<ul class="spn-main"')
    end = html.find("</ul>", start)
    menu = html[start:end]
    return re.findall(r'href="([^"]+)"', menu)


def check(root):
    pinned = open(os.path.join(BASE, "COMMIT"), encoding="utf-8").read().strip()
    if pinned != COMMIT:
        raise SystemExit("baseline commit pin does not match the module")
    for lang in LANGS:
        base = root if lang == "en" else os.path.join(root, lang)
        pages = {}
        for page in PAGES:
            text = open(os.path.join(base, page + ".html"), encoding="utf-8").read()
            pages[page] = text
            where = lang + "/" + page
            if "Biological SI Partner" in text:
                raise SystemExit("prohibited credit returned: " + where)
            if 'href="Oceans.html"' in text or 'href="../Oceans.html"' in text or 'href="Lesson_Builder.html"' in text or 'href="Privacy.html"' in text:
                raise SystemExit("a different page was treated as local: " + where)
            if page != "Search" and ("assets/bsp-search.js" in text or "bsp-live-search.js" in text):
                raise SystemExit("search scripts leaked onto " + where)
        first = menu_links(pages["About"])
        for page, text in pages.items():
            if menu_links(text) != first:
                raise SystemExit("menu drifted on " + lang + "/" + page)
            if 'class="sticky-help" href="Ways_to_Help.html">' + HELP[lang] not in text:
                raise SystemExit("help control drifted on " + lang + "/" + page)
        for page in ("About", "Contact", "Ways_to_Help"):
            if "sp-anim-banner" not in pages[page] or "borealopelta-founder-1280.mp4" not in pages[page]:
                raise SystemExit("title video missing on " + lang + "/" + page)
            if "Pacific_Clouds" in pages[page] or "ISS074" in pages[page] or "hero/morph" in pages[page]:
                raise SystemExit("title still uses spacecraft or cartoon Earth footage: " + lang + "/" + page)
            if "Created by the Founder and SI" not in pages[page]:
                raise SystemExit("title video credit missing: " + lang + "/" + page)
        search = pages["Search"]
        if "<video" in search or ".mp4" in search:
            raise SystemExit("search reference has no video: " + lang)
        if 'id="bsp-search"' not in search or "assets/bsp-search.js" not in search or "assets/bsp-live-search.js" not in search:
            raise SystemExit("search lost the notes search or the live Saving Planets index: " + lang)
        if "data-corpus" in search or "bsp-shared-search.js" in search:
            raise SystemExit("empty shared-corpus client is still on the search page: " + lang)
    if FROZEN:
        return
