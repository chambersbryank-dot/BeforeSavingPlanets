(function () {
  var h = document.querySelector('.bsp-hero');
  if (!h) return;
  var b = h.querySelector('.bsp-pause');
  var v = h.querySelector('.m-vid');
  var story = h.closest('.bsp-story');
  var eras = story ? Array.prototype.slice.call(story.querySelectorAll('.bsp-era')) : [];
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var held = false;
  var scrubbing = false;
  var label = b ? b.textContent : '';

  function arm() {
    if (!v || v.getAttribute('src')) return;
    v.preload = 'auto';
    v.src = '/assets/hero/morph/hero-1080.mp4';
  }

  function go() {
    if (held || scrubbing || !v || h.classList.contains('is-on') || v.readyState < 2) return;
    if (v.currentTime > 0.05) {
      v.addEventListener('seeked', function once() { v.removeEventListener('seeked', once); go(); });
      v.currentTime = 0;
      return;
    }
    h.classList.add('is-on');
    var play = v.play();
    if (play && play.catch) play.catch(function () { h.classList.add('is-playing'); });
  }

  if (v) {
    v.muted = true;
    v.playsInline = true;
    v.addEventListener('playing', function () { h.classList.add('is-playing'); });
    v.addEventListener('canplay', function () { if (!reduce && !scrubbing && !held) go(); });
    v.addEventListener('loadedmetadata', function () { if (scrubbing) applyScrub(); });
    v.addEventListener('error', function () { h.classList.add('is-playing'); });
  }

  function progress() {
    if (!story) return 0;
    var track = story.querySelector('.bsp-eras');
    if (!track) return 0;
    var into = window.innerHeight - track.getBoundingClientRect().top;
    if (into <= 8) return 0;
    return Math.max(0, Math.min(1, into / track.offsetHeight));
  }

  function applyScrub() {
    if (reduce || held || !v || !eras.length) return;
    var p = progress();
    if (p <= 0) {
      if (scrubbing) {
        scrubbing = false;
        h.classList.remove('is-scrubbing');
        if (v.paused && v.ended !== true && h.classList.contains('is-on')) {
          var resume = v.play();
          if (resume && resume.catch) resume.catch(function () {});
        }
      }
      return;
    }
    scrubbing = true;
    h.classList.add('is-scrubbing', 'is-on', 'is-playing');
    if (!v.getAttribute('src')) arm();
    if (!v.paused) v.pause();
    var idx = Math.min(eras.length - 1, Math.floor(p * eras.length));
    var local = p * eras.length - idx;
    var a = parseFloat(eras[idx].getAttribute('data-t0'));
    var btm = parseFloat(eras[idx].getAttribute('data-t1'));
    var dur = v.duration;
    if (isFinite(a) && isFinite(btm) && dur && isFinite(dur) && v.readyState >= 1) {
      var t = Math.min(Math.max(0, a + (btm - a) * local), Math.max(0, dur - 0.04));
      if (Math.abs((v.currentTime || 0) - t) > 0.08) {
        try { v.currentTime = t; } catch (err) {}
      }
    }
    for (var i = 0; i < eras.length; i++) eras[i].classList.toggle('is-active', i === idx);
  }

  if (b) {
    b.addEventListener('click', function () {
      if (reduce && v && !h.classList.contains('is-on')) {
        arm();
        h.classList.add('is-on');
        var started = v.play();
        if (started && started.catch) started.catch(function () {});
        b.textContent = label;
        b.setAttribute('aria-pressed', 'false');
        return;
      }
      held = !h.classList.contains('bsp-paused');
      h.classList.toggle('bsp-paused', held);
      b.setAttribute('aria-pressed', held ? 'true' : 'false');
      b.textContent = held ? '▶' : label;
      if (!v) return;
      if (held) v.pause();
      else if (scrubbing) applyScrub();
      else if (h.classList.contains('is-on')) {
        var resume = v.play();
        if (resume && resume.catch) resume.catch(function () { h.classList.add('is-playing'); });
      } else go();
    });
  }

  if (reduce) {
    if (v) { v.removeAttribute('autoplay'); v.pause(); v.preload = 'none'; }
    if (b) b.textContent = b.getAttribute('data-play') || 'Play';
    return;
  }
  if (!v) return;

  if (story && eras.length) {
    window.addEventListener('scroll', applyScrub, { passive: true });
    window.addEventListener('resize', applyScrub);
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function () { applyScrub(); }, { threshold: [0, 0.25, 0.5, 0.75, 1] });
      for (var i = 0; i < eras.length; i++) io.observe(eras[i]);
    }
  }

  requestAnimationFrame(function () { requestAnimationFrame(arm); });
  setTimeout(function () {
    if (!h.classList.contains('is-playing')) h.classList.add('is-playing');
  }, 15000);
})();
