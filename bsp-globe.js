/* Dig Quest time scrubber. Our own orthographic globe (no Ancient Earth code).
   Coastline masks and pin paths are PALEOMAP reconstructions from the GPlates Web Service. */
(function () {
  var root = document.querySelector('.bsp-globe-sec');
  if (!root) return;
  var canvas = root.querySelector('canvas');
  var slider = root.querySelector('input[type=range]');
  var readout = root.querySelector('[data-readout]');
  var far = root.querySelector('[data-far]');
  var pinsUrl = root.getAttribute('data-pins');
  var texBase = root.getAttribute('data-tex');
  var today = root.getAttribute('data-today') || 'Today';
  var farMsg = root.getAttribute('data-far-msg') || '';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var LOOK = [0.930274, 0.207912, 0.302264];
  var EAST = [-0.309017, 0, 0.951057];
  var NORTH = [-0.197736, 0.978148, -0.064248];
  var pack = null;
  var texCache = {};
  var pixCache = {};
  var pending = 0;

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
    var facing = x * LOOK[0] + y * LOOK[1] + z * LOOK[2];
    var sx = x * EAST[0] + y * EAST[1] + z * EAST[2];
    var sy = x * NORTH[0] + y * NORTH[1] + z * NORTH[2];
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
    var ctx = canvas.getContext('2d');
    var w = canvas.width, h = canvas.height;
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#070b14';
    ctx.beginPath();
    ctx.arc(w / 2, h / 2, Math.min(w, h) * 0.48, 0, Math.PI * 2);
    ctx.fill();
    var name = nearestMask(age());
    loadImage(name, function (img) {
      if (!img || name !== nearestMask(age())) return;
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
        var wx = nx * EAST[0] + ny * NORTH[0] + nz * LOOK[0];
        var wy = nx * EAST[1] + ny * NORTH[1] + nz * LOOK[1];
        var wz = nx * EAST[2] + ny * NORTH[2] + nz * LOOK[2];
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
    dot(ctx, A, '#ffd27a', w);
    dot(ctx, B, '#7ee0c6', w);
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

  if (slider) slider.addEventListener('input', schedule);
  root.querySelectorAll('input[name="bsp-pair"]').forEach(function (el) {
    el.addEventListener('change', schedule);
  });
  window.addEventListener('resize', schedule);
  if (far && farMsg) far.textContent = farMsg;

  fetch(pinsUrl).then(function (r) { return r.json(); }).then(function (data) {
    pack = data;
    schedule();
  }).catch(function () { schedule(); });

  if (reduce) schedule();
  else schedule();
})();
