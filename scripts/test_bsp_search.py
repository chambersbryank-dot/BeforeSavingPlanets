# Knowledge rules for the Before Saving Planets search. No network.
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bsp_knowledge as k

ROOT = k.ROOT
pack = json.load(open(os.path.join(ROOT, "assets", "data", "deep-time.json"), encoding="utf-8"))
records = k.records_from_deep_time(pack)
urls = {src["url"] for row in records for src in row["sources"]}
assert urls, "site index has no https sources"
verified = []
research_calls = {"n": 0}

def counting_research(query):
    research_calls["n"] += 1
    return k.research(query)

sm = k.ask("Smilodon", records, verified, research_fn=counting_research)
assert sm["status"] == "ok" and sm["from"] == "site", sm
assert "saber-toothed" in sm["answer"]
assert sm["sources"][0]["url"].startswith("https://www.floridamuseum.ufl.edu/")
assert sm["stored"] is False and research_calls["n"] == 0

missing = k.ask("price of a 2099 Mars condo", records, verified, research_fn=counting_research)
assert missing["status"] == "missing", missing
assert missing["sources"] == [] and missing["answer"] == ""
assert missing["stored"] is False
assert missing["research"]["working"] is False
assert research_calls["n"] == 1

before = list(verified)
ok, why = k.save_verified({
    "id": "cited-skull-inventory",
    "approved": True,
    "added": "2026-11-07",
    "q": "zz verified only where is the cited skull inventory",
    "a": "The Florida Museum species page is the citation this site already uses for that inventory.",
    "sources": [{"title": "Florida Museum species page", "url": sm["sources"][0]["url"]}],
}, verified, urls)
assert ok and why == "saved", why
again = k.ask("zz verified only where is the cited skull inventory", records, verified, research_fn=counting_research)
assert again["status"] == "ok" and again["from"] == "verified", again
assert again["added"] == "2026-11-07"
assert again["sources"][0]["url"] == sm["sources"][0]["url"]
assert research_calls["n"] == 1
assert len(verified) == len(before) + 1

refused, reason = k.save_verified({
    "approved": True,
    "added": "2026-11-07",
    "fromUser": True,
    "q": "Earth is 100 years old because my teacher said so",
    "a": "Earth is 100 years old because my teacher said so",
    "sources": [{"title": "Florida Museum species page", "url": sm["sources"][0]["url"]}],
}, verified, urls)
assert not refused and reason == "user or child text is not knowledge"
assert len(verified) == len(before) + 1

child = k.ask("I am 8 years old and my school is Lincoln Elementary", records, verified, audience="child")
assert child["status"] == "refused" and child["stored"] is False
assert len(verified) == len(before) + 1

bad, reason = k.save_verified({
    "approved": True,
    "added": "2026-11-07",
    "q": "Where is a brand new citation?",
    "a": "It would point at a page this site has never cited.",
    "sources": [{"title": "Example", "url": "https://example.com/not-on-this-site"}],
}, verified, urls)
assert not bad and reason == "source is not already cited on this site"

budget = k.Budget(limit=2)
assert k.ask("price of a 2099 Mars condo", records, [], budget=budget)["status"] == "missing"
assert k.ask("price of a 2099 Mars condo", records, [], budget=budget)["status"] == "missing"
limited = k.ask("price of a 2099 Mars condo", records, [], budget=budget)
assert limited["status"] == "limited" and limited["research"] is None

on_disk = json.load(open(k.VERIFIED_PATH, encoding="utf-8"))
assert on_disk.get("entries") == []
k.write_index()
built = json.load(open(k.INDEX_PATH, encoding="utf-8"))
assert built["research"] == "unavailable"
assert any(row["title"] == "Smilodon" for row in built["records"])
print("bsp search tests ok", len(records), "site records")
