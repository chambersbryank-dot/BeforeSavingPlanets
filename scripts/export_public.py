#!/usr/bin/env python3
"""Copy the public site into dist/ for a Cloudflare Pages output directory.

The generator writes HTML into the repository root, beside scripts/, notes, and
caches. Pages must not publish that root.

While the site is parked, the public output is only a temporary redirect.
Every requested path goes to https://www.savingplanets.com/ and nowhere else.
The pages, media, and search files stay in the repository. To open the site
again, stop writing that redirect and copy the public tree as before.
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
PARK_HOME = "https://www.savingplanets.com/"
# Static rule first, then the splat. Neither copies the original path or query.
PARK_REDIRECTS = (
    "# Temporary park. Revert export_public.py to publish the saved pages again.\n"
    "/ " + PARK_HOME + " 302\n"
    "/* " + PARK_HOME + " 302\n"
)


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
    """Publish only the park redirect. preview is ignored while parked."""
    del root, preview
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    path = os.path.join(dest, "_redirects")
    open(path, "w", encoding="utf-8").write(PARK_REDIRECTS)
    size = os.path.getsize(path)
    return {"files": 1, "bytes": size, "largest": (size, "_redirects"), "preview": False, "park": PARK_HOME}


def main():
    preview = preview_requested()
    info = export_public(preview=preview)
    mode = "park-redirect " + info.get("park", "")
    print("pages output: dist %d files, %d bytes, largest %s %d bytes, %s" % (
        info["files"], info["bytes"], info["largest"][1], info["largest"][0], mode))


if __name__ == "__main__":
    sys.exit(main() or 0)
