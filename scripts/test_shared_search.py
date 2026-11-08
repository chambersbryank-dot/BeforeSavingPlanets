#!/usr/bin/env python3
"""The shared search client ranks a supplied corpus and refuses a missing one.

It does not read the 52-note index and it does not call the Saving Planets worker.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
NODE = r'''
import { answer } from "./assets/bsp-shared-search.js";

const corpus = { pages: [
  { url: "https://www.beforesavingplanets.com/Smilodon.html", title: "Smilodon", text: "saber-toothed cat fossil from La Brea" },
  { url: "https://www.savingplanets.com/Oceans.html", title: "Oceans", text: "ocean cleanup crews and coastal restoration" },
  { url: "https://example.com/other.html", title: "Other", text: "smilodon ocean cleanup" },
] };

function same(got, want, label) {
  if (got !== want) { console.error(label, JSON.stringify(got)); process.exit(1); }
}

let out = answer("", corpus);
same(out.code, "ready", "empty");
same(out.results.length, 0, "empty results");

out = answer("smilodon fossil", corpus);
same(out.code, "ok", "bsp code");
same(out.results[0].host, "www.beforesavingplanets.com", "bsp host");
same(out.results[0].site, "Before Saving Planets", "bsp site");
same(out.results[0].url, "https://www.beforesavingplanets.com/Smilodon.html", "bsp url");
if (out.results.some(hit => hit.host === "example.com")) { console.error("unknown host kept"); process.exit(1); }

out = answer("ocean cleanup", corpus);
same(out.code, "ok", "sp code");
same(out.results[0].host, "www.savingplanets.com", "sp host");
same(out.results[0].site, "Saving Planets", "sp site");

out = answer("nothing matches this phrase", corpus);
same(out.code, "missing", "missing");
same(out.results.length, 0, "missing results");

out = answer("smilodon", null);
same(out.code, "down", "no corpus");
same(out.results.length, 0, "no corpus results");

out = answer("write me at ada@example.com about smilodon", corpus);
same(out.code, "refused", "email");
same(out.results.length, 0, "email results");

console.log("shared search ok");
'''

def main():
    script = ROOT / "assets" / "bsp-shared-search.js"
    text = script.read_text(encoding="utf-8")
    code = "\n".join(line for line in text.splitlines() if not line.strip().startswith("*") and not line.strip().startswith("/*"))
    for banned in ("bsp-verified", "bsp_knowledge", "si-helper", "pagefind", "semantic-index", "workers.dev"):
        if banned in code:
            raise SystemExit("shared client must not call a private index or the worker: " + banned)
    subprocess.run(["node", "--input-type=module", "-e", NODE], cwd=ROOT, check=True)

if __name__ == "__main__":
    main()
