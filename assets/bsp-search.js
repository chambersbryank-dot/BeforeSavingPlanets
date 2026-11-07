/* Search over sourced notes already on Before Saving Planets.
   The query is not sent anywhere. Automatic research is not connected. */
(function () {
  var once = "";
  try { once = sessionStorage.getItem("bsp-search-once") || ""; sessionStorage.removeItem("bsp-search-once"); } catch (e) {}
  var initial = once || new URLSearchParams(location.search).get("q") || "";
  if (location.search.indexOf("q=") !== -1) history.replaceState(null, "", location.pathname);
  var form = document.getElementById("bsp-search");
  var input = document.getElementById("bsp-q");
  var status = document.getElementById("bsp-search-status");
  var list = document.getElementById("bsp-search-results");
  if (!form || !input || !status || !list) return;
  var prefix = form.getAttribute("data-prefix") || "";
  var lang = document.documentElement.lang === "fr" ? "fr" : "en";
  var stop = {};
  "a an and are as at be been but by can do does for from had has have how i in into is it its may me my of on or our so such that the their them there these they this to too was we were what when where which who why will with would you your about also any some very just not".split(" ").forEach(function (w) { stop[w] = 1; });
  var personal = /[^\s@]+@[^\s@]+\.[a-z]{2,}|(?:\+?\d[\s.\-()]*){9,}|\b(my name is|i am called|my school|my teacher|years old)\b|\b(school|elementary|academy)\b/i;
  var stamps = [];

  function textOf(id) {
    var el = document.getElementById(id);
    return el ? el.textContent : "";
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function norm(s) {
    return String(s || "").toLowerCase().replace(/[^\p{L}\p{N}\s]+/gu, " ").replace(/\s+/g, " ").trim();
  }
  function tokens(s) {
    return norm(s).split(" ").filter(function (w) { return w.length >= 3 && !stop[w] && !/^\d+$/.test(w); });
  }
  function allow() {
    var now = Date.now();
    stamps = stamps.filter(function (t) { return now - t < 60000; });
    if (stamps.length >= 10) return false;
    stamps.push(now);
    return true;
  }
  function score(query, row) {
    var qn = norm(query);
    if (qn.length < 3) return 0;
    var names = [norm(row.title), norm(row.titleFr)];
    for (var i = 0; i < names.length; i++) {
      var name = names[i];
      if (name && name.length >= 4 && (name === qn || qn.indexOf(name) !== -1 || name.indexOf(qn) !== -1)) return 100;
    }
    var words = tokens(query);
    if (words.length < 2) return 0;
    var hay = norm([row.title, row.titleFr, row.answer, row.answerFr].join(" "));
    var hit = words.filter(function (w) { return hay.indexOf(w) !== -1; });
    if (hit.length >= 2 && hit.length * 2 >= words.length) return hit.length;
    return 0;
  }
  function show(kind, html) {
    status.textContent = textOf(kind);
    list.innerHTML = html || "";
  }
  var index = [];
  var verified = [];
  var ready = Promise.all([
    fetch(prefix + "assets/data/bsp-search-index.json").then(function (r) { if (!r.ok) throw new Error("index"); return r.json(); }),
    fetch(prefix + "assets/data/bsp-verified.json").then(function (r) { return r.ok ? r.json() : { entries: [] }; }).catch(function () { return { entries: [] }; })
  ]).then(function (pair) {
    index = (pair[0] && pair[0].records) || [];
    verified = ((pair[1] && pair[1].entries) || []).filter(function (e) { return e && e.approved === true && e.q && e.a && e.sources && e.sources[0]; });
  });

  function run() {
    var q = input.value.trim();
    if (!q) { show("bsp-search-ready", ""); return; }
    if (personal.test(q)) { show("bsp-search-refused", ""); return; }
    if (!allow()) { show("bsp-search-limited", ""); return; }
    ready.then(function () {
      var best = null, bestScore = 0;
      index.forEach(function (row) {
        var s = score(q, row);
        if (s > bestScore) { bestScore = s; best = row; }
      });
      if (best) {
        var answer = lang === "fr" && best.answerFr ? best.answerFr : best.answer;
        var title = lang === "fr" && best.titleFr ? best.titleFr : best.title;
        var src = best.sources[0];
        show("bsp-search-ok", '<li class="bsp-card"><h2><a href="' + esc(prefix + best.page) + '">' + esc(title) + '</a></h2><p>' + esc(answer) + '</p><p><a href="' + esc(src.url) + '" rel="noopener noreferrer">' + esc(src.title) + '</a></p></li>');
        return;
      }
      var want = norm(q);
      var saved = verified.filter(function (e) { return norm(e.q) === want; })[0];
      if (saved && /^https:\/\//.test(saved.sources[0].url)) {
        show("bsp-search-ok", '<li class="bsp-card"><h2>' + esc(saved.q) + '</h2><p>' + esc(saved.a) + '</p><p><a href="' + esc(saved.sources[0].url) + '" rel="noopener noreferrer">' + esc(saved.sources[0].title) + '</a></p><p>' + esc(saved.added || "") + '</p></li>');
        return;
      }
      show("bsp-search-missing", "");
    }).catch(function () { show("bsp-search-down", ""); });
  }
  form.addEventListener("submit", function (e) { e.preventDefault(); run(); });
  if (initial) { input.value = initial; run(); }
})();
