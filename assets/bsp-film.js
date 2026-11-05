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
