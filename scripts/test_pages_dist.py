#!/usr/bin/env python3
"""The Pages output is a complete public tree, and preview noindex stays off production."""
import os, shutil, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import export_public as exp

ROOT = exp.ROOT
PROD = "https://www.beforesavingplanets.com"


def read(path):
    return open(path, encoding="utf-8").read()


def check(dest, preview):
    index = read(os.path.join(dest, "index.html"))
    if 'rel="canonical" href="%s/"' % PROD not in index and 'rel="canonical" href="%s/index.html"' % PROD not in index:
        if PROD not in index.split("</head>", 1)[0]:
            raise SystemExit("canonical left production: preview=%s" % preview)
    head = index.split("</head>", 1)[0]
    if 'href="%s' % PROD not in head:
        raise SystemExit("production canonical missing")
    robots = 'content="noindex,follow"' if preview else 'content="index,follow"'
    if '<meta name="robots" %s>' % robots not in head and 'name="robots" %s' % robots not in head:
        # attribute order in the generator is name then content
        if ('noindex,follow' in head) != preview:
            raise SystemExit("robots meta wrong for preview=%s" % preview)
    if preview and 'content="index,follow"' in head:
        raise SystemExit("preview home is still indexable")
    if not preview and "noindex" in head:
        raise SystemExit("production home was marked noindex")
    missing = read(os.path.join(dest, "404.html"))
    if "noindex,follow" not in missing or "Page not found" not in missing:
        raise SystemExit("404 lost its noindex or heading")
    kids = read(os.path.join(dest, "Kids.html"))
    if "cloudflareinsights" in kids or "assets/bsp-search.js" in kids or "assets/bsp-live-search.js" in kids or "data-no-newsletter" not in kids:
        raise SystemExit("kids privacy changed in the public output")
    search = read(os.path.join(dest, "Search.html"))
    if "assets/bsp-search.js" not in search or "assets/bsp-live-search.js" not in search or 'id="bsp-search"' not in search:
        raise SystemExit("public search lost the notes search or the live index")
    if "data-corpus" in search or "bsp-shared-search.js" in search:
        raise SystemExit("empty shared-corpus client is in the public search page")
    if not os.path.isfile(os.path.join(dest, "assets", "bsp-search.js")) or not os.path.isfile(os.path.join(dest, "assets", "data", "bsp-search-index.json")):
        raise SystemExit("notes search files missing from the public output")
    if not os.path.isfile(os.path.join(dest, "assets", "bsp-live-search.js")):
        raise SystemExit("live search script missing from the public output")
    headers = os.path.join(dest, "_headers")
    if preview:
        if "X-Robots-Tag: noindex" not in read(headers):
            raise SystemExit("preview _headers missing")
    elif os.path.exists(headers):
        raise SystemExit("production output must not ship a noindex header")
    for banned in ("NOTES.md", "README.md", "scripts", ".cursor", ".git"):
        if os.path.exists(os.path.join(dest, banned)):
            raise SystemExit("internal path leaked: " + banned)
    for dirpath, _, names in os.walk(dest):
        for name in names:
            if name.endswith(".py") or name.endswith(".pyc"):
                raise SystemExit("python leaked: " + os.path.join(dirpath, name))
    info_files = exp.public_files(ROOT)
    copied = []
    for dirpath, _, names in os.walk(dest):
        for name in names:
            if name == "_headers":
                continue
            copied.append(os.path.relpath(os.path.join(dirpath, name), dest))
    if sorted(copied) != sorted(info_files):
        raise SystemExit("public output is not the complete public tree")


def main():
    parent = tempfile.mkdtemp(prefix="bsp-dist-")
    try:
        prod = os.path.join(parent, "prod")
        prev = os.path.join(parent, "prev")
        exp.export_public(dest=prod, preview=False)
        exp.export_public(dest=prev, preview=True)
        check(prod, False)
        check(prev, True)
        files = exp.public_files(ROOT)
        total = 0
        largest = (0, "")
        for rel in files:
            size = os.path.getsize(os.path.join(ROOT, rel))
            total += size
            if size > largest[0]:
                largest = (size, rel)
        if len(files) > exp.PAGES_FILE_LIMIT or largest[0] > exp.PAGES_FILE_BYTES:
            raise SystemExit("Pages limit exceeded")
        print("pages dist ok %d files %d bytes largest %s %d preview-noindex separate from production" % (
            len(files), total, largest[1], largest[0]))
    finally:
        shutil.rmtree(parent)


if __name__ == "__main__":
    main()
