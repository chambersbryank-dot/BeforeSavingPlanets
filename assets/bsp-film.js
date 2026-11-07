/* Homepage film. Same loop as Saving Planets. No colored-Earth poster. */
(function () {
  var hero = document.querySelector(".hero.bsp-film");
  if (!hero) return;
  var video = hero.querySelector("video.hero-video");
  var button = hero.querySelector(".bsp-pause");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!video) return;
  if (reduce) {
    video.removeAttribute("autoplay");
    video.pause();
    if (button) button.hidden = true;
    return;
  }
  var play = video.play && video.play();
  if (play && play.catch) play.catch(function () {});
  if (!button) return;
  var pauseLabel = button.textContent;
  var playLabel = button.getAttribute("data-play") || "Play";
  button.addEventListener("click", function () {
    var paused = !video.paused;
    if (paused) video.pause();
    else {
      var again = video.play && video.play();
      if (again && again.catch) again.catch(function () {});
    }
    button.setAttribute("aria-pressed", paused ? "true" : "false");
    button.textContent = paused ? playLabel : pauseLabel;
  });
})();
/* Species reconstruction film. Same pause and reduced-motion rules. */
(function () {
  var hero = document.querySelector(".sm-hero.bsp-film");
  if (!hero) return;
  var video = hero.querySelector("video.sm-hero-video");
  var button = hero.querySelector(".bsp-pause");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!video) return;
  if (reduce) {
    video.removeAttribute("autoplay");
    video.pause();
    video.hidden = true;
    if (button) button.hidden = true;
    return;
  }
  var play = video.play && video.play();
  if (play && play.catch) play.catch(function () {});
  if (!button) return;
  var pauseLabel = button.textContent;
  var playLabel = button.getAttribute("data-play") || "Play";
  button.addEventListener("click", function () {
    var paused = !video.paused;
    if (paused) video.pause();
    else {
      var again = video.play && video.play();
      if (again && again.catch) again.catch(function () {});
    }
    button.setAttribute("aria-pressed", paused ? "true" : "false");
    button.textContent = paused ? playLabel : pauseLabel;
  });
})();
/* Title stills on About, Ways to Help, and Myth vs Fact. No new film. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.querySelectorAll(".bsp-title-film, .bsp-myth").forEach(function (root) {
    if (root.classList.contains("bsp-title-film") && root.closest(".bsp-myth")) return;
    var button = root.querySelector(".bsp-pause");
    if (reduce) {
      root.classList.add("is-still");
      if (button) button.hidden = true;
      return;
    }
    if (!button) return;
    var pauseLabel = button.textContent;
    var playLabel = button.getAttribute("data-play") || "Play";
    button.addEventListener("click", function () {
      var paused = root.classList.toggle("is-paused");
      button.setAttribute("aria-pressed", paused ? "true" : "false");
      button.textContent = paused ? playLabel : pauseLabel;
    });
  });
})();
/* Myth vs Fact: filter the six cards on this page. No web search. */
(function () {
  var root = document.querySelector("[data-myth]");
  if (!root) return;
  var box = root.querySelector("[data-myth-q]");
  var cards = [].slice.call(root.querySelectorAll("[data-myth-card]"));
  var empty = root.querySelector("[data-myth-empty]");
  var buttons = [].slice.call(root.querySelectorAll("[data-myth-filter]"));
  var topic = "all";
  function apply() {
    var words = (box.value || "").toLowerCase().trim();
    var shown = 0;
    cards.forEach(function (card) {
      var hay = (card.getAttribute("data-myth-text") || "").toLowerCase();
      var okTopic = topic === "all" || card.getAttribute("data-myth-topic") === topic;
      var ok = okTopic && (!words || hay.indexOf(words) !== -1);
      card.hidden = !ok;
      if (ok) shown += 1;
    });
    empty.hidden = shown !== 0;
  }
  box.addEventListener("input", apply);
  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      topic = button.getAttribute("data-myth-filter");
      buttons.forEach(function (other) {
        other.setAttribute("aria-pressed", other === button ? "true" : "false");
      });
      apply();
    });
  });
})();
