/* One search client for Before Saving Planets and Saving Planets.
 *
 * The shared corpus is not published. Saving Planets search is a static Pagefind
 * index plus search/semantic-index.json built from Saving Planets pages only.
 * The SI Helper worker (https://si-helper.chambersbryank.workers.dev/ask) answers
 * from the Vectorize index si-helper-site, which is also Saving Planets pages,
 * and its origin list is only savingplanets.com. This file does not call that
 * worker, does not copy the 52 deep-time notes, and does not send the question
 * anywhere. A result is shown only when a corpus of absolute page URLs is
 * supplied, and each hit keeps the host that was in that URL.
 */
const SITE = {
  "www.beforesavingplanets.com": "Before Saving Planets",
  "beforesavingplanets.com": "Before Saving Planets",
  "www.savingplanets.com": "Saving Planets",
  "savingplanets.com": "Saving Planets",
};

const PERSONAL = /[^\s@]+@[^\s@]+\.[a-z]{2,}|(?:\+?\d[\s.\-()]*){9,}|\b(my name is|i am called|my school|my teacher|years old)\b|\b(school|elementary|academy)\b/i;

export function answer(query, corpus) {
  const q = String(query || "").trim();
  if (!q) return { ok: true, code: "ready", results: [] };
  if (PERSONAL.test(q)) return { ok: false, code: "refused", results: [] };
  if (!corpus || !Array.isArray(corpus.pages)) return { ok: false, code: "down", results: [] };
  const terms = q.toLowerCase().split(/[^\p{L}\p{N}]+/u).filter((word) => word.length > 1);
  if (!terms.length) return { ok: true, code: "missing", results: [] };
  const results = [];
  for (const page of corpus.pages) {
    if (!page || typeof page.url !== "string") continue;
    let host = "";
    try { host = new URL(page.url).hostname; } catch { continue; }
    const site = SITE[host];
    if (!site) continue;
    const hay = `${page.title || ""} ${page.text || ""}`.toLowerCase();
    let hits = 0;
    for (const term of terms) if (hay.includes(term)) hits += 1;
    if (!hits) continue;
    results.push({
      url: page.url,
      title: page.title || page.url,
      site,
      host,
      score: hits / terms.length,
    });
  }
  results.sort((a, b) => b.score - a.score || a.title.localeCompare(b.title));
  return { ok: true, code: results.length ? "ok" : "missing", results: results.slice(0, 8) };
}

const IDS = {
  ready: "bsp-search-ready",
  ok: "bsp-search-ok",
  missing: "bsp-search-missing",
  refused: "bsp-search-refused",
  limited: "bsp-search-limited",
  down: "bsp-search-down",
};
const COPY = {
  ready: "One search index is meant to cover Before Saving Planets and Saving Planets. That shared index is not published on this site yet.",
  ok: "From the shared index. Each result names its site.",
  missing: "Nothing in the shared index matches. The question was not saved. This page does not search a separate note list.",
  refused: "Leave out names, emails, phone numbers, and schools. Nothing from this search is saved.",
  limited: "Search is paused for a minute so it cannot run without a limit.",
  down: "The shared index did not load. There is no second index to search instead, and the question was not saved.",
};

function boot() {
  const form = document.querySelector("form.sp-search-form") || document.getElementById("bsp-search");
  const input = document.getElementById("q") || document.getElementById("bsp-q");
  const status = document.getElementById("status") || document.getElementById("bsp-search-status");
  const list = document.getElementById("results") || document.getElementById("bsp-search-results");
  if (!form || !input || !status || !list) return;
  const stamps = [];
  function allow() {
    const now = Date.now();
    while (stamps.length && now - stamps[0] > 60000) stamps.shift();
    if (stamps.length >= 8) return false;
    stamps.push(now);
    return true;
  }
  function show(code) {
    const node = document.getElementById(IDS[code] || "");
    status.textContent = (node && node.textContent) || COPY[code] || COPY.down;
  }
  function paint(out) {
    list.replaceChildren();
    show(out.code);
    for (const hit of out.results) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = hit.url;
      link.textContent = hit.title;
      const where = document.createElement("span");
      where.className = "bsp-search-host";
      where.textContent = `${hit.site} · ${hit.host}`;
      item.append(link, where);
      list.append(item);
    }
  }
  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const q = input.value.trim();
    if (q && PERSONAL.test(q)) { paint(answer(q, { pages: [] })); return; }
    if (q && !allow()) { paint({ code: "limited", results: [] }); return; }
    const src = form.getAttribute("data-corpus") || "";
    if (!src) { paint(answer(q, null)); return; }
    try {
      const res = await fetch(src);
      if (!res.ok) throw new Error(String(res.status));
      paint(answer(q, await res.json()));
    } catch {
      paint({ code: "down", results: [] });
    }
  });
  let once = "";
  try {
    once = sessionStorage.getItem("bsp-search-once") || "";
    if (once) sessionStorage.removeItem("bsp-search-once");
  } catch { /* session storage can be blocked; the form still works */ }
  const fromUrl = new URLSearchParams(location.search).get("q") || "";
  const start = (once || fromUrl).trim();
  if (start) {
    input.value = start;
    form.requestSubmit();
  } else {
    show("ready");
  }
}

if (typeof document !== "undefined") boot();
