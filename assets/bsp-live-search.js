/* The Search page on Saving Planets queries the Pagefind index served from
   https://www.savingplanets.com/pagefind/ . This file calls that index.
   It does not rank a second corpus and it does not send the question to the
   SI Helper worker. Result links keep the absolute URL Pagefind returns.
   The notes search on the same page is separate and stays in place. */
const ROOT = "https://www.savingplanets.com";
const initial = new URLSearchParams(location.search).get("q") || "";

const form = document.getElementById("sp-live-form");
const input = document.getElementById("sp-q");
const status = document.getElementById("sp-status");
const list = document.getElementById("sp-results");

function say(text) {
  if (status) status.textContent = text;
}

function linked(url) {
  if (!url) return "";
  if (url.startsWith(ROOT + "/")) return url;
  return "";
}

async function start() {
  if (!form || !input || !status || !list) return null;
  if (initial) input.value = initial;
  let pf;
  try {
    pf = await import(ROOT + "/pagefind/pagefind.js");
    await pf.options({ basePath: ROOT + "/pagefind/", baseUrl: ROOT });
    await pf.init();
  } catch (err) {
    say("The Saving Planets index did not load. The notes search on this page still works.");
    return null;
  }
  say("This box searches the Saving Planets index.");
  return pf;
}

const ready = start();

if (form && input && list) {
  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const q = input.value.trim();
    list.replaceChildren();
    const pf = await ready;
    if (!q) {
      say(pf ? "This box searches the Saving Planets index." : "The Saving Planets index did not load. The notes search on this page still works.");
      return;
    }
    if (!pf) {
      say("The Saving Planets index did not load. The notes search on this page still works.");
      return;
    }
    try {
      const found = await pf.search(q);
      const hits = (found.results || []).slice(0, 8);
      const rows = [];
      for (const hit of hits) {
        const data = await hit.data();
        const url = linked(data.url || "");
        if (!url) continue;
        rows.push({ url, title: (data.meta && data.meta.title) || url });
      }
      if (!rows.length) {
        say("Nothing in the Saving Planets index matches. The notes search on this page still works.");
        return;
      }
      say(rows.length + (rows.length === 1 ? " result" : " results") + " from the Saving Planets index.");
      for (const row of rows) {
        const item = document.createElement("li");
        const link = document.createElement("a");
        link.href = row.url;
        link.textContent = row.title.split(" | ")[0];
        const where = document.createElement("span");
        where.className = "bsp-search-host";
        where.textContent = "Saving Planets · www.savingplanets.com";
        item.append(link, where);
        list.append(item);
      }
    } catch (err) {
      say("The Saving Planets index did not load. The notes search on this page still works.");
    }
  });
}
