/* Dig Quest time scrubber. Our own orthographic globe (no Ancient Earth code).
   Coastline masks and pin paths are PALEOMAP reconstructions from the GPlates Web Service.
   The drift keeps the homepage's Africa view. At today the globe rests on North America
   (about 48°N, 90°W) so Greenland and the United States are both in view. */
(function () {
  var root = document.querySelector('.bsp-globe-sec');
  if (!root) return;
  var canvas = root.querySelector('canvas');
  var slider = root.querySelector('input[type=range]');
  var readout = root.querySelector('[data-readout]');
  var far = root.querySelector('[data-far]');
  var card = root.querySelector('.bsp-pin-card');
  var pinsUrl = root.getAttribute('data-pins');
  var texBase = root.getAttribute('data-tex');
  var today = root.getAttribute('data-today') || 'Today';
  var farMsg = root.getAttribute('data-far-msg') || '';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pack = null;
  var texCache = {};
  var pixCache = {};
  var pending = 0;
  var pinHits = [];
  var cards = [];
  var userMoved = false;
  var camLook, camEast, camNorth;

  function basis(latDeg, lonDeg) {
    var la = latDeg * Math.PI / 180, lo = lonDeg * Math.PI / 180, cl = Math.cos(la);
    return frameFromLook([cl * Math.cos(lo), Math.sin(la), cl * Math.sin(lo)]);
  }
  function frameFromLook(look) {
    var len = Math.hypot(look[0], look[1], look[2]) || 1;
    look = [look[0] / len, look[1] / len, look[2] / len];
    var east = [-look[2], 0, look[0]];
    var el = Math.hypot(east[0], east[2]) || 1;
    east = [east[0] / el, 0, east[2] / el];
    var north = [
      east[1] * look[2] - east[2] * look[1],
      east[2] * look[0] - east[0] * look[2],
      east[0] * look[1] - east[1] * look[0]
    ];
    return { look: look, east: east, north: north };
  }
  function slerp(a, b, t) {
    var dot = a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    dot = Math.max(-1, Math.min(1, dot));
    var th = Math.acos(dot);
    if (th < 1e-4) return a.slice();
    var s = Math.sin(th);
    var w1 = Math.sin((1 - t) * th) / s, w2 = Math.sin(t * th) / s;
    return [a[0] * w1 + b[0] * w2, a[1] * w1 + b[1] * w2, a[2] * w1 + b[2] * w2];
  }
  var AFRICA = basis(12, 18);
  var AMERICA = basis(48, -90);

  function setCamera(ma) {
    var t = ma >= 40 ? 0 : (40 - ma) / 40;
    t = t * t * (3 - 2 * t);
    var look = slerp(AFRICA.look, AMERICA.look, t);
    var frame = frameFromLook(look);
    camLook = frame.look;
    camEast = frame.east;
    camNorth = frame.north;
  }

  function resize() {
    var box = canvas.parentElement.getBoundingClientRect();
    var css = Math.max(240, Math.min(420, box.width || 320));
    var dpr = Math.min(window.devicePixelRatio || 1, 1.25);
    var px = Math.round(Math.min(css * dpr, 380));
    if (canvas.width !== px) { canvas.width = px; canvas.height = px; }
    canvas.style.width = css + 'px';
    canvas.style.height = css + 'px';
  }

  function age() { return slider ? +slider.value : 0; }

  function nearestMask(ma) {
    if (ma <= 8) return 'earth.webp';
    var q = Math.round(ma / 20) * 20;
    if (q < 0) q = 0;
    if (q > 540) q = 540;
    return 'm' + ('00' + q).slice(-3) + '.webp';
  }

  function loadImage(name, cb) {
    if (texCache[name]) { cb(texCache[name]); return; }
    var img = new Image();
    img.onload = function () { texCache[name] = img; cb(img); };
    img.onerror = function () { cb(null); };
    img.src = texBase + name;
  }

  function pixels(img) {
    if (pixCache[img.src]) return pixCache[img.src];
    var c = document.createElement('canvas');
    c.width = img.width; c.height = img.height;
    var g = c.getContext('2d', { willReadFrequently: true });
    g.drawImage(img, 0, 0);
    var p = g.getImageData(0, 0, c.width, c.height);
    pixCache[img.src] = { w: c.width, h: c.height, d: p.data };
    return pixCache[img.src];
  }

  function project(lat, lon, R, cx, cy) {
    var la = lat * Math.PI / 180, lo = lon * Math.PI / 180, cl = Math.cos(la);
    var x = cl * Math.cos(lo), y = Math.sin(la), z = cl * Math.sin(lo);
    var facing = x * camLook[0] + y * camLook[1] + z * camLook[2];
    var sx = x * camEast[0] + y * camEast[1] + z * camEast[2];
    var sy = x * camNorth[0] + y * camNorth[1] + z * camNorth[2];
    return { x: cx + sx * R, y: cy - sy * R, front: facing > 0.08 };
  }

  function pinAt(list, ma) {
    var keys = Object.keys(list).map(Number).sort(function (a, b) { return a - b; });
    var lo = keys[0], hi = keys[keys.length - 1];
    for (var i = 0; i < keys.length; i++) {
      if (keys[i] <= ma) lo = keys[i];
      if (keys[i] >= ma) { hi = keys[i]; break; }
    }
    var a = list[String(lo)], b = list[String(hi)];
    if (!a) return null;
    if (!b || lo === hi) return a;
    var t = (ma - lo) / (hi - lo);
    return a.map(function (p, i) {
      var q = b[i];
      var lon0 = p[0], lon1 = q[0];
      var d = lon1 - lon0;
      if (d > 180) d -= 360;
      if (d < -180) d += 360;
      return [lon0 + d * t, p[1] + (q[1] - p[1]) * t];
    });
  }

  function draw() {
    resize();
    var ma = age();
    setCamera(ma);
    var ctx = canvas.getContext('2d');
    var w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#070b14';
    ctx.beginPath();
    ctx.arc(w / 2, h / 2, Math.min(w, h) * 0.48, 0, Math.PI * 2);
    ctx.fill();
    var name = nearestMask(ma);
    loadImage(name, function (img) {
      if (!img || name !== nearestMask(age())) return;
      setCamera(age());
      paint(ctx, w, h, pixels(img));
      paintPins(ctx, w, h);
    });
  }

  function paint(ctx, w, h, tex) {
    var R = Math.min(w, h) * 0.44;
    var cx = w / 2, cy = h / 2;
    var img = ctx.createImageData(w, h);
    var d = img.data;
    var td = tex.d, tw = tex.w, th = tex.h;
    for (var y = 0; y < h; y++) {
      for (var x = 0; x < w; x++) {
        var nx = (x - cx) / R, ny = (cy - y) / R, m = nx * nx + ny * ny;
        var o = (y * w + x) * 4;
        if (m > 1) { d[o + 3] = 0; continue; }
        var nz = Math.sqrt(1 - m);
        var wx = nx * camEast[0] + ny * camNorth[0] + nz * camLook[0];
        var wy = nx * camEast[1] + ny * camNorth[1] + nz * camLook[1];
        var wz = nx * camEast[2] + ny * camNorth[2] + nz * camLook[2];
        var lat = Math.asin(Math.max(-1, Math.min(1, wy)));
        var lon = Math.atan2(wz, wx);
        var u = ((lon + Math.PI) / (2 * Math.PI)) * (tw - 1);
        var v = ((Math.PI / 2 - lat) / Math.PI) * (th - 1);
        var ui = u | 0, vi = v | 0;
        if (ui < 0) ui = 0;
        if (vi < 0) vi = 0;
        if (ui > tw - 1) ui = tw - 1;
        if (vi > th - 1) vi = th - 1;
        var to = (vi * tw + ui) * 4;
        var nd = Math.max(0, (nx * -0.22 + ny * 0.38 + nz * 0.90) / 1.02);
        var shade = 0.5 + 0.58 * nd;
        var rim = Math.pow(1 - nz, 1.6) * 70;
        d[o] = Math.min(255, td[to] * shade + rim * 0.35);
        d[o + 1] = Math.min(255, td[to + 1] * shade + rim * 0.65);
        d[o + 2] = Math.min(255, td[to + 2] * shade + rim);
        d[o + 3] = 255;
      }
    }
    ctx.putImageData(img, 0, 0);
  }

  function paintPins(ctx, w, h) {
    pinHits = [];
    if (!pack) return;
    var R = Math.min(w, h) * 0.44;
    var cx = w / 2, cy = h / 2;
    var ma = age();
    var pts = pinAt(pack.coords, ma);
    if (!pts) return;
    var picked = root.querySelector('input[name="bsp-pair"]:checked');
    var idx = picked ? +picked.value : 0;
    var fossil = pts[idx * 2], solution = pts[idx * 2 + 1];
    if (!fossil || !solution) return;
    var A = project(fossil[1], fossil[0], R, cx, cy);
    var B = project(solution[1], solution[0], R, cx, cy);
    if (A.front && B.front) {
      ctx.strokeStyle = 'rgba(255,210,140,.7)';
      ctx.lineWidth = Math.max(2, w / 180);
      ctx.setLineDash([6, 6]);
      ctx.beginPath();
      ctx.moveTo(A.x, A.y);
      ctx.lineTo(B.x, B.y);
      ctx.stroke();
      ctx.setLineDash([]);
    }
    var rad = Math.max(5, w / 55);
    dot(ctx, A, '#ffd27a', w);
    dot(ctx, B, '#7ee0c6', w);
    if (A.front) pinHits.push({ x: A.x, y: A.y, r: rad * 1.8, pair: idx });
    if (B.front) pinHits.push({ x: B.x, y: B.y, r: rad * 1.8, pair: idx });
    if (far) far.hidden = A.front && B.front;
    if (readout) {
      readout.textContent = ma < 0.5 ? today : (Math.round(ma) + ' Ma');
    }
    if (slider) slider.setAttribute('aria-valuetext', readout ? readout.textContent : String(ma));
  }

  function dot(ctx, p, color, w) {
    if (!p.front) return;
    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.strokeStyle = '#140c06';
    ctx.lineWidth = Math.max(2, w / 160);
    ctx.arc(p.x, p.y, Math.max(5, w / 55), 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
  }

  function schedule() {
    pending++;
    var token = pending;
    requestAnimationFrame(function () { if (token === pending) draw(); });
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function showCard(i) {
    if (!card || !cards[i]) return;
    var c = cards[i];
    var href = /^https:\/\//i.test(c.href) ? c.href : '';
    card.innerHTML =
      '<div class="bsp-pin-head"><h3>' + esc(c.fossil) + '</h3>' +
      '<button type="button" class="bsp-pin-x">Close</button></div>' +
      '<dl>' +
      '<dt>What</dt><dd>' + esc(c.what) + '</dd>' +
      '<dt>When it lived</dt><dd>' + esc(c.when) + '</dd>' +
      '<dt>Where found</dt><dd>' + esc(c.where) + '</dd>' +
      '<dt>Why it matters</dt><dd>' + esc(c.why) + '</dd>' +
      '</dl>' +
      '<div class="bsp-pin-now"><p><span class="bsp-pin-s">● ' + esc(c.solution) + '</span></p>' +
      '<p>' + esc(c.now) + '</p>' +
      (href ? '<p><a href="' + esc(href) + '" rel="noopener noreferrer">' + esc(c.solution) + ' on Saving Planets →</a></p>' : '') +
      '</div>';
    card.hidden = false;
    var x = card.querySelector('.bsp-pin-x');
    if (x) x.addEventListener('click', function () { card.hidden = true; });
  }

  function selectPair(i, open) {
    var radio = root.querySelector('input[name="bsp-pair"][value="' + i + '"]');
    if (radio) radio.checked = true;
    schedule();
    if (open) showCard(i);
  }

  function hitPin(ev) {
    var rect = canvas.getBoundingClientRect();
    if (!rect.width || !rect.height) return null;
    var x = (ev.clientX - rect.left) * (canvas.width / rect.width);
    var y = (ev.clientY - rect.top) * (canvas.height / rect.height);
    var best = null, bestD = Infinity;
    for (var i = 0; i < pinHits.length; i++) {
      var p = pinHits[i];
      var dx = x - p.x, dy = y - p.y, d = dx * dx + dy * dy;
      if (d <= p.r * p.r && d < bestD) { best = p; bestD = d; }
    }
    return best;
  }

  root.querySelectorAll('.bsp-pin-open').forEach(function (btn) {
    btn.addEventListener('click', function () {
      selectPair(+btn.getAttribute('data-pair'), true);
    });
  });
  root.querySelectorAll('input[name="bsp-pair"]').forEach(function (el) {
    el.addEventListener('change', function () {
      schedule();
      if (card && !card.hidden) showCard(+el.value);
    });
  });
  if (slider) {
    slider.addEventListener('input', function () { userMoved = true; schedule(); });
    slider.addEventListener('pointerdown', function () { userMoved = true; });
  }
  canvas.addEventListener('click', function (ev) {
    var hit = hitPin(ev);
    if (!hit) return;
    selectPair(hit.pair, true);
  });
  canvas.addEventListener('mousemove', function (ev) {
    canvas.style.cursor = hitPin(ev) ? 'pointer' : '';
  });
  window.addEventListener('resize', schedule);
  if (far && farMsg) far.textContent = farMsg;

  try {
    cards = JSON.parse(document.getElementById('bsp-pin-cards').textContent);
  } catch (e) { cards = []; }

  function playToToday() {
    if (!slider || reduce || userMoved) return;
    var t0 = performance.now();
    var dur = 8000;
    function step(now) {
      if (userMoved) return;
      var u = Math.min(1, (now - t0) / dur);
      var e = 1 - Math.pow(1 - u, 3);
      slider.value = String(Math.round(540 * (1 - e)));
      slider.setAttribute('aria-valuenow', slider.value);
      schedule();
      if (u < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if (reduce && slider) {
    slider.value = '0';
    slider.setAttribute('aria-valuenow', '0');
  }

  fetch(pinsUrl).then(function (r) { return r.json(); }).then(function (data) {
    pack = data;
    schedule();
    playToToday();
  }).catch(function () { schedule(); playToToday(); });

  schedule();
})();
