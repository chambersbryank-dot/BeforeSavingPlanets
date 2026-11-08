# Children's pages do not load visit analytics or collect an email address.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["", "fr", "es", "ar", "it", "he"]
CHILD = ["Kids.html", "Kids_Map.html"]
ADULT = ["index.html", "About.html", "Learn.html"]
BEACON = "cloudflareinsights.com"
js = open(os.path.join(ROOT, "site.js"), encoding="utf-8").read()
assert "child==='Kids'||child==='Kids_Map'" in js

def read(lang, name):
    base = "" if not lang else lang + os.sep
    return open(os.path.join(ROOT, base + name), encoding="utf-8").read()

for lang in LANGS:
    for name in CHILD:
        text = read(lang, name)
        where = (lang or "en") + " " + name
        assert BEACON not in text, where
        assert "mailerlite.com" not in text, where
        assert 'type="email"' not in text, where
        assert "data-no-newsletter" in text, where
        assert "<footer>" in text and 'id="topnav"' in text, where
        assert "site.js" in text, where
    for name in ADULT:
        text = read(lang, name)
        where = (lang or "en") + " " + name
        assert text.count(BEACON) == 1, where
        assert "data-no-newsletter" not in text, where
print("kids privacy html checks ok", len(LANGS) * len(CHILD), "child pages")
