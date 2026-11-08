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
# Same destination on this site. A shared filename is not enough: Oceans.html is a different page.
SAME = {
    "index.html", "About.html", "Contact.html", "Search.html", "Ways_to_Help.html",
    "World_Map.html", "Learn.html", "Kids_Map.html", "Myth_vs_Fact.html",
    "Teachers.html", "Courses.html", "Kids.html",
}
GAPS = (
    "Other languages still use the previous menu. Their page bodies were not replaced.",
    "Search uses the Saving Planets form and does not call Pagefind or the SI Helper worker. The shared corpus is not published.",
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


def rewrite_href(href):
    """Keep a link that resolves here. Anything else stays on Saving Planets."""
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "?", "data:", "//")):
        return href
    base, query = (href.split("?", 1) + [""])[:2] if "?" in href else (href, "")
    path, frag = (base.split("#", 1) + [""])[:2] if "#" in base else (base, "")
    if not path or path.endswith("/"):
        return href
    name = os.path.basename(path)
    if name in SAME and _local(path):
        return href
    if not name.endswith(".html") and _local(path):
        return href
    out = SP_ORIGIN + path.lstrip("./")
    if query:
        out += "?" + query
    if frag:
        out += "#" + frag
    return out


def rewrite(html):
    html = re.sub(r'<p class="biosi-cc">[\s\S]*?</p>', "", html)
    html = html.replace("Biological SI Partner", "the Founder")

    def sub(match):
        return match.group(1) + rewrite_href(match.group(2)) + '"'

    return re.sub(r'(href="|src=")([^"]*)"', sub, html)


def nav_html(page):
    raw = _read("nav.html")
    raw = re.sub(r"<picture>[\s\S]*?</picture>", _LOGO, raw, count=1)
    raw = raw.replace("Home - Saving Planets", "Home - Before Saving Planets")
    raw = raw.replace("%2FAbout.html", "%2F" + page + ".html")
    raw = re.sub(
        r'href="((?:[a-z]{2}/)?)About\.html"( hreflang=")',
        lambda m: 'href="%s%s.html"%s' % (m.group(1), page, m.group(2)),
        raw,
    )
    raw = raw.replace(' aria-current="page"', "").replace(' aria-current="true"', "")
    raw = raw.replace(" is-current", "")
    raw = raw.replace(
        'href="%s.html" hreflang="en"' % page,
        'href="%s.html" hreflang="en" aria-current="true"' % page,
        1,
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
    return rewrite(raw)


def main_html(page):
    html = rewrite(_read(page + ".html"))
    if page == "Search":
        html = html.replace(
            '<form class="sp-search-form"',
            '<form class="sp-search-form" data-corpus=""',
            1,
        )
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
    pages = {}
    for page in PAGES:
        text = open(os.path.join(root, page + ".html"), encoding="utf-8").read()
        pages[page] = text
        if "Biological SI Partner" in text:
            raise SystemExit("prohibited credit returned: " + page)
        if 'href="Oceans.html"' in text or 'href="Lesson_Builder.html"' in text or 'href="Privacy.html"' in text:
            raise SystemExit("a different page was treated as local: " + page)
        if "assets/bsp-search.js" in text or "pagefind" in text or "search-ui.js" in text:
            raise SystemExit("baseline page points at a separate search stack: " + page)
    first = menu_links(pages["About"])
    for page, text in pages.items():
        if menu_links(text) != first:
            raise SystemExit("menu drifted on " + page)
        if 'class="sticky-help" href="Ways_to_Help.html"' not in text:
            raise SystemExit("help control drifted on " + page)
    for page in ("About", "Contact", "Ways_to_Help"):
        if "sp-anim-banner" not in pages[page]:
            raise SystemExit("title banner drifted on " + page)
    search = pages["Search"]
    if "sp-search-form" not in search or 'data-corpus=""' not in search or "assets/bsp-shared-search.js" not in search:
        raise SystemExit("search is not the shared baseline form")
    if FROZEN:
        return
