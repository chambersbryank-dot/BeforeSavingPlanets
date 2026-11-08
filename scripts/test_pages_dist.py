#!/usr/bin/env python3
"""The public output is only a temporary redirect to the Saving Planets homepage."""
import os, shutil, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import export_public as exp

HOME = "https://www.savingplanets.com/"
SAMPLES = [
    "/",
    "/index.html",
    "/About.html",
    "/Contact.html",
    "/Ways_to_Help.html",
    "/Search.html",
    "/Search",
    "/Deep_Time.html",
    "/fr/About.html",
    "/es/Contact.html",
    "/ar/Ways_to_Help.html",
    "/it/Search.html",
    "/he/index.html",
    "/Kids.html",
    "/assets/data/bsp-search-index.json",
    "/assets/smilodon/hero-1080.mp4",
    "/no-such-page",
    "/About.html/",
]


def location_for(path, query=""):
    """The park rule: every path, with or without a query, ends at one homepage."""
    del path, query
    return HOME


def check(dest):
    names = []
    for dirpath, _, files in os.walk(dest):
        for name in files:
            names.append(os.path.relpath(os.path.join(dirpath, name), dest))
    if names != ["_redirects"]:
        raise SystemExit("park output must not publish the old site: " + ", ".join(names[:12]))
    text = open(os.path.join(dest, "_redirects"), encoding="utf-8").read()
    if "/ " + HOME + " 302\n" not in text or "/* " + HOME + " 302\n" not in text:
        raise SystemExit("redirect is not the Saving Planets homepage")
    if ":splat" in text:
        raise SystemExit("redirect would keep the original path")
    for sample in SAMPLES:
        if location_for(sample) != HOME or location_for(sample, "q=smilodon") != HOME:
            raise SystemExit("route missed the homepage: " + sample)
    about = os.path.join(exp.ROOT, "About.html")
    if not os.path.isfile(about) or os.path.getsize(about) < 1000:
        raise SystemExit("source pages were removed")


def main():
    parent = tempfile.mkdtemp(prefix="bsp-dist-")
    try:
        dest = os.path.join(parent, "dist")
        info = exp.export_public(dest=dest, preview=False)
        check(dest)
        exp.export_public(dest=dest, preview=True)
        check(dest)
        if info["files"] != 1:
            raise SystemExit("unexpected park file count")
        print("park redirect ok " + HOME)
    finally:
        shutil.rmtree(parent)


if __name__ == "__main__":
    main()
