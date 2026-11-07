# Local search for Before Saving Planets.
# Saving Planets answers from its own pages (Pagefind, and SI Helper on Vectorize).
# SI Helper does not research the web and does not store answers. Unanswered questions
# wait for a person. This module follows that rule on this site's sourced notes.
# It does not call Workers AI, Vectorize, or a paid search API.
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT, "assets", "data", "bsp-search-index.json")
VERIFIED_PATH = os.path.join(ROOT, "assets", "data", "bsp-verified.json")
INDEX_BUILT = "2026-11-07"
STOP = set("""a an and are as at be been but by can do does for from had has have how i in into is it its may me my of on or our so such that the their them there these they this to too was we were what when where which who why will with would you your about also any some very just not""".split())
PII = re.compile(r"[^\s@]+@[^\s@]+\.[a-z]{2,}|(?:\+?\d[\s.\-()]*){9,}", re.I)
PERSONAL = re.compile(
    r"\b(my name is|i am called|my school|my teacher|years old)\b|\b(school|elementary|academy)\b",
    re.I,
)
HTTPS = re.compile(r"^https://[^\s]+$")


def _norm(text):
    text = (text or "").casefold()
    text = re.sub(r"[^\w\s]+", " ", text, flags=re.U)
    return re.sub(r"\s+", " ", text).strip()


def _tokens(text):
    return [w for w in _norm(text).split() if len(w) >= 3 and w not in STOP and not w.isdigit()]


def _https_sources(sources):
    out = []
    for src in sources or []:
        title = str(src.get("title") or "").strip()
        url = str(src.get("url") or "").strip()
        if title and HTTPS.match(url):
            out.append({"title": title, "url": url})
    return out


def records_from_deep_time(pack):
    rows = []
    for item in pack.get("life") or []:
        sources = _https_sources([{"title": item.get("source") or item.get("name"), "url": item.get("sourceHref")}])
        answer = str(item.get("blurb") or "").strip()
        if not sources or not answer or not item.get("name"):
            continue
        rows.append({
            "id": "life-" + _norm(item["name"]).replace(" ", "-")[:60],
            "kind": "life",
            "title": item["name"],
            "titleFr": item.get("nameFr") or item["name"],
            "answer": answer,
            "answerFr": str(item.get("blurbFr") or "").strip(),
            "page": item.get("href") or "Deep_Time.html",
            "sources": sources,
        })
    for item in pack.get("extinctions") or []:
        sources = _https_sources([{"title": item.get("source") or item.get("name"), "url": item.get("sourceHref")}])
        answer = str(item.get("cause") or "").strip()
        if not sources or not answer or not item.get("name"):
            continue
        rows.append({
            "id": "ext-" + _norm(item["name"]).replace(" ", "-")[:60],
            "kind": "extinction",
            "title": item["name"],
            "titleFr": item.get("nameFr") or item["name"],
            "answer": answer,
            "answerFr": str(item.get("causeFr") or "").strip(),
            "page": item.get("href") or "Deep_Time.html",
            "sources": sources,
        })
    return rows


def load_index(path=INDEX_PATH):
    doc = json.load(open(path, encoding="utf-8"))
    return doc.get("records") or []


def write_index(path=INDEX_PATH):
    pack = json.load(open(os.path.join(ROOT, "assets", "data", "deep-time.json"), encoding="utf-8"))
    rows = records_from_deep_time(pack)
    known = {src["url"] for row in rows for src in row["sources"]}
    doc = {
        "built": INDEX_BUILT,
        "research": "unavailable",
        "records": rows,
        "sourceUrls": sorted(known),
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(path, "a", encoding="utf-8").write("\n")
    return len(rows)


def _score(query, row):
    qn = _norm(query)
    if len(qn) < 3:
        return 0
    names = [_norm(row.get("title")), _norm(row.get("titleFr"))]
    if any(name and len(name) >= 4 and (name == qn or name in qn or qn in name) for name in names):
        return 100
    words = _tokens(query)
    if len(words) < 2:
        return 0
    hay = _norm(" ".join([row.get("title", ""), row.get("titleFr", ""), row.get("answer", ""), row.get("answerFr", "")]))
    hit = [w for w in words if w in hay]
    if len(hit) >= 2 and len(hit) * 2 >= len(words):
        return len(hit)
    return 0


def best_site(query, records):
    ranked = sorted((( _score(query, row), row) for row in records), key=lambda pair: -pair[0])
    if not ranked or ranked[0][0] <= 0:
        return None
    return ranked[0][1]


def research(query):
    return {
        "working": False,
        "status": "unavailable",
        "reason": "No research backend is configured. This search does not call Workers AI, Vectorize, or the public web.",
    }


def personal(query):
    text = query or ""
    return bool(PII.search(text) or PERSONAL.search(text))


def validate_entry(entry, allowed_urls):
    if not isinstance(entry, dict):
        return "not a record"
    if entry.get("approved") is not True:
        return "not approved"
    if entry.get("fromUser") or entry.get("audience") == "child":
        return "user or child text is not knowledge"
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(entry.get("added") or "")):
        return "added date"
    question = str(entry.get("q") or "").strip()
    answer = str(entry.get("a") or "").strip()
    if len(question) < 8 or len(answer) < 8:
        return "too short"
    if personal(question) or personal(answer):
        return "personal"
    if _norm(question) == _norm(answer):
        return "answer copies the question"
    sources = _https_sources(entry.get("sources"))
    if not sources:
        return "https source"
    if allowed_urls is not None and any(src["url"] not in allowed_urls for src in sources):
        return "source is not already cited on this site"
    return ""


def usable_entries(entries, allowed_urls):
    good = []
    for entry in entries or []:
        if validate_entry(entry, allowed_urls):
            continue
        good.append({
            "id": str(entry.get("id") or _norm(entry["q"])[:40]),
            "q": str(entry["q"]).strip(),
            "a": str(entry["a"]).strip(),
            "added": entry["added"],
            "sources": _https_sources(entry.get("sources")),
        })
    return good


def match_verified(query, entries):
    want = _norm(query)
    if len(want) < 8:
        return None
    for entry in entries:
        if _norm(entry["q"]) == want:
            return entry
    return None


class Budget:
    def __init__(self, limit=10):
        self.limit = limit
        self.used = 0

    def allow(self):
        if self.used >= self.limit:
            return False
        self.used += 1
        return True


def ask(query, records, verified, audience="public", budget=None, research_fn=research):
    text = str(query or "").strip()
    calls = {"n": 0}

    def run_research():
        calls["n"] += 1
        return research_fn(text)

    if audience == "child" and personal(text):
        return {"status": "refused", "stored": False, "research": None, "sources": [], "calls": calls["n"]}
    if personal(text):
        return {"status": "refused", "stored": False, "research": None, "sources": [], "calls": calls["n"]}
    if budget is not None and not budget.allow():
        return {"status": "limited", "stored": False, "research": None, "sources": [], "calls": calls["n"]}
    hit = best_site(text, records)
    if hit:
        return {
            "status": "ok",
            "from": "site",
            "stored": False,
            "title": hit["title"],
            "answer": hit["answer"],
            "answerFr": hit.get("answerFr") or "",
            "page": hit.get("page") or "",
            "sources": hit["sources"],
            "research": None,
            "calls": calls["n"],
        }
    saved = match_verified(text, verified)
    if saved:
        return {
            "status": "ok",
            "from": "verified",
            "stored": False,
            "title": saved["q"],
            "answer": saved["a"],
            "added": saved["added"],
            "page": "",
            "sources": saved["sources"],
            "research": None,
            "calls": calls["n"],
        }
    gap = run_research()
    return {
        "status": "missing",
        "from": "",
        "stored": False,
        "title": "",
        "answer": "",
        "page": "",
        "sources": [],
        "research": gap,
        "calls": calls["n"],
    }


def save_verified(entry, store, allowed_urls):
    reason = validate_entry(entry, allowed_urls)
    if reason:
        return False, reason
    saved = usable_entries([entry], allowed_urls)[0]
    if any(_norm(row["q"]) == _norm(saved["q"]) for row in store):
        return True, "already saved"
    store.append(saved)
    return True, "saved"
