#!/usr/bin/env python3
"""Copy the public site into dist/ for a Cloudflare Pages output directory.

The generator writes HTML into the repository root, beside scripts/, notes, and
caches. Pages must not publish that root. This copies only the files a browser
requests. BSP_PAGES_PREVIEW=1 stamps noindex on that copy alone. Canonical URLs
stay on https://www.beforesavingplanets.com.
"""
import os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
PUBLIC_DIRS = ("assets", "fr", "es", "ar", "it", "he")
ROOT_EXT = {".html", ".css", ".js", ".xml", ".txt", ".ico", ".png", ".webmanifest"}
SKIP_NAMES = {"NOTES.md", "README.md", "dist"}
PAGES_FILE_LIMIT = 20000
PAGES_FILE_BYTES = 25 * 1024 * 1024
ROBOTS = re.compile(r'(<meta name="robots" content=")[^"]+(")')
PREVIEW_HEADER = "/*\n  X-Robots-Tag: noindex\n"


def preview_requested():
    return os.environ.get("BSP_PAGES_PREVIEW") == "1"


def public_files(root):
    found = []
    for name in sorted(os.listdir(root)):
        if name in SKIP_NAMES or name.startswith("."):
            continue
        path = os.path.join(root, name)
        if os.path.isfile(path):
            if os.path.splitext(name)[1].lower() in ROOT_EXT:
                found.append(name)
            continue
        if name not in PUBLIC_DIRS or not os.path.isdir(path):
            continue
        for dirpath, dirs, names in os.walk(path):
            dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith(".")]
            for filename in sorted(names):
                if filename.startswith(".") or filename.endswith(".pyc"):
                    continue
                full = os.path.join(dirpath, filename)
                found.append(os.path.relpath(full, root))
    return found


def stamp_preview(html, rel):
    if not ROBOTS.search(html):
        raise SystemExit("preview page has no robots meta: " + rel)
    return ROBOTS.sub(r"\1noindex,follow\2", html, count=1)


def export_public(root=ROOT, dest=DIST, preview=False):
    files = public_files(root)
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    total = 0
    largest = (0, "")
    for rel in files:
        src = os.path.join(root, rel)
        out = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if preview and rel.endswith(".html"):
            text = open(src, encoding="utf-8").read()
            open(out, "w", encoding="utf-8").write(stamp_preview(text, rel))
            size = os.path.getsize(out)
        else:
            shutil.copy2(src, out)
            size = os.path.getsize(src)
        total += size
        if size > largest[0]:
            largest = (size, rel)
    if preview:
        open(os.path.join(dest, "_headers"), "w", encoding="utf-8").write(PREVIEW_HEADER)
    if len(files) > PAGES_FILE_LIMIT:
        raise SystemExit("public output has %d files; Pages Free allows %d" % (len(files), PAGES_FILE_LIMIT))
    if largest[0] > PAGES_FILE_BYTES:
        raise SystemExit("public file exceeds 25 MiB: %s (%d bytes)" % (largest[1], largest[0]))
    return {"files": len(files), "bytes": total, "largest": largest, "preview": preview}


def main():
    preview = preview_requested()
    info = export_public(preview=preview)
    mode = "preview-noindex" if preview else "production-robots"
    print("pages output: dist %d files, %d bytes, largest %s %d bytes, %s" % (
        info["files"], info["bytes"], info["largest"][1], info["largest"][0], mode))


if __name__ == "__main__":
    sys.exit(main() or 0)
