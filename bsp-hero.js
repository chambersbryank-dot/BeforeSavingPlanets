(function () {
  var h = document.querySelector('.bsp-hero');
  if (!h) return;
  var b = h.querySelector('.bsp-pause');
  var story = h.closest('.bsp-story');
  var eras = story ? Array.prototype.slice.call(story.querySelectorAll('.bsp-era')) : [];
  var eraFrames = Array.prototype.slice.call(h.querySelectorAll('.m-era'));
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var held = false;
  var scrubbing = false;
  var label = b ? b.textContent : '';

  function showEra(idx) {
    for (var i = 0; i < eraFrames.length; i++) eraFrames[i].classList.toggle('is-show', i === idx);
    for (var j = 0; j < eras.length; j++) eras[j].classList.toggle('is-active', j === idx);
  }

  function start() {
    h.classList.add('is-on', 'is-playing');
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
    if (reduce || held || !eras.length) return;
    var p = progress();
    if (p <= 0) {
      if (scrubbing) {
        scrubbing = false;
        h.classList.remove('is-scrubbing');
        h.classList.add('is-settled', 'is-on', 'is-playing');
      }
      return;
    }
    scrubbing = true;
    h.classList.add('is-scrubbing', 'is-on', 'is-playing', 'is-settled');
    var idx = Math.min(eras.length - 1, Math.floor(p * eras.length));
    showEra(idx);
  }

  if (b) {
    b.addEventListener('click', function () {
      if (reduce && !h.classList.contains('is-on')) {
        start();
        b.textContent = label;
        b.setAttribute('aria-pressed', 'false');
        return;
      }
      held = !h.classList.contains('bsp-paused');
      h.classList.toggle('bsp-paused', held);
      b.setAttribute('aria-pressed', held ? 'true' : 'false');
      b.textContent = held ? '▶' : label;
    });
  }

  if (reduce) {
    if (b) b.textContent = b.getAttribute('data-play') || 'Play';
    return;
  }
  if (!h.querySelector('.bsp-morph')) return;

  if (story && eras.length) {
    window.addEventListener('scroll', applyScrub, { passive: true });
    window.addEventListener('resize', applyScrub);
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function () { applyScrub(); }, { threshold: [0, 0.25, 0.5, 0.75, 1] });
      for (var i = 0; i < eras.length; i++) io.observe(eras[i]);
    }
  }

  requestAnimationFrame(function () { requestAnimationFrame(start); });
})();
