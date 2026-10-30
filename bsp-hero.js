(function () {
  var h = document.querySelector('.bsp-hero');
  if (!h) return;
  var b = h.querySelector('.bsp-pause');
  var v = h.querySelector('.m-vid');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var held = false;
  var label = b ? b.textContent : '';

  if (b) {
    b.addEventListener('click', function () {
      held = h.classList.toggle('bsp-paused');
      b.setAttribute('aria-pressed', held ? 'true' : 'false');
      b.textContent = held ? '▶' : label;
      if (!v || reduce) return;
      if (held) v.pause();
      else if (h.classList.contains('is-on')) {
        var resume = v.play();
        if (resume && resume.catch) resume.catch(function () { h.classList.add('is-playing'); });
      } else go();
    });
  }

  if (!v || reduce) {
    if (v) { v.removeAttribute('autoplay'); v.pause(); v.preload = 'none'; }
    return;
  }

  function pick() {
    var c = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    var wide = window.matchMedia('(min-width: 1600px)').matches;
    if (wide && c && c.saveData !== true && c.effectiveType === '4g')
      return '/assets/hero/morph/hero-4k.mp4';
    return '/assets/hero/morph/hero-1080.mp4';
  }

  function go() {
    if (held || h.classList.contains('is-on') || v.readyState < 2) return;
    if (v.currentTime > 0.05) {
      v.addEventListener('seeked', function once() { v.removeEventListener('seeked', once); go(); });
      v.currentTime = 0;
      return;
    }
    h.classList.add('is-on');
    var play = v.play();
    if (play && play.catch) play.catch(function () { h.classList.add('is-playing'); });
  }

  v.muted = true;
  v.playsInline = true;
  v.addEventListener('playing', function () { h.classList.add('is-playing'); });
  v.addEventListener('canplay', go);
  v.addEventListener('error', function () { h.classList.add('is-playing'); });

  function arm() {
    if (v.getAttribute('src')) return;
    v.preload = 'auto';
    v.src = pick();
    if (v.readyState >= 3) go();
  }

  requestAnimationFrame(function () { requestAnimationFrame(arm); });
  setTimeout(function () {
    if (!h.classList.contains('is-playing')) h.classList.add('is-playing');
  }, 15000);
})();
