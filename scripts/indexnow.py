#!/usr/bin/env python3
"""Tell IndexNow about the indexable URLs. Dry-run unless --submit.

The key file has to be live at https://www.beforesavingplanets.com/{key}.txt
and return the key before a search engine will accept the list. One POST to
https://api.indexnow.org/indexnow is shared with the other IndexNow engines,
including Bing and Yandex. Google does not take IndexNow.

https://www.indexnow.org/documentation
https://www.indexnow.org/faq
"""
import json, pathlib, re, sys, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
HOST = "www.beforesavingplanets.com"

def urls():
    found=[]
    for path in sorted(ROOT.glob("sitemap-*.xml")):
        found += re.findall(r"<loc>(.*?)</loc>", path.read_text(encoding="utf-8"))
    if not found:
        raise SystemExit("no language sitemaps. Run scripts/build.py first.")
    return found

def key():
    for path in ROOT.glob("*.txt"):
        if path.name=="robots.txt":
            continue
        body=path.read_text(encoding="utf-8").strip()
        if path.stem==body and 8<=len(body)<=128:
            return body
    raise SystemExit("IndexNow key file not found")

def main():
    submit="--submit" in sys.argv
    listed=urls()
    token=key()
    payload={
        "host": HOST,
        "key": token,
        "keyLocation": f"https://{HOST}/{token}.txt",
        "urlList": listed,
    }
    print(f"{len(listed)} URLs, key file https://{HOST}/{token}.txt")
    if not submit:
        print("dry run. Pass --submit after the key file is live on www.")
        return
    req=urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type":"application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=60) as res:
        print(res.status)
        print(res.read(300).decode("utf-8", "replace"))

if __name__=="__main__":
    main()
