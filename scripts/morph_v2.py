#!/usr/bin/env python3
"""Build the homepage morph v2.

0–~5.4s  SI artist’s interpretation (lava → cooling crust → first oceans), retimed.
then     PALEOMAP coastlines (Scotese 2016 via the GPlates Web Service) drift
         from 540 Ma to today on a globe in the same starfield.
finish   NASA Blue Marble (public domain) in that same camera, held.

Continents are redrawn at each age from reconstructed polygons, so the land
slides to its next position. This is not a crossfade between eras.
A true per-plate vertex morph needs stable plate ids; the coastline service
does not return them. TODO: native slide keyframes if EarthByte ships ids.

Run from the repo root: python3 scripts/morph_v2.py
"""
import json, os, subprocess, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets/hero/morph/hero-1080.mp4")
OUT = os.path.join(ROOT, "assets/hero/morph/hero-1080.mp4")
CACHE = "/tmp/paleo-cache"
TMP = "/tmp/morph-v2"
BM = "/tmp/paleo/bm2.jpg"

W, H = 1920, 1080
CX, CY = 960.0, 508.0
LAT0 = np.deg2rad(12.0)
LON0 = np.deg2rad(18.0)
STEP = 5  # million years between reconstructed coastlines
OCEAN = (7, 28, 68)

# Fossil site, then the Saving Planets solution it is paired with.
PAIRS = [
    # Solution pins sit on continental crust the PALEOMAP model can reconstruct.
    # The reef and the polar station are the onshore sites, not open water.
    ("burgess", "Burgess Shale, Canada", 51.43, -116.47,
     "reef", "Coral Restoration Foundation, Florida Keys", 25.40, -80.90,
     "https://www.savingplanets.com/Coral_Restoration_Foundation.html"),
    ("chicxulub", "Chicxulub crater, Mexico", 21.40, -89.52,
     "forest", "Cristalino forest, Brazil", -9.60, -55.90,
     "https://www.savingplanets.com/Deforestation.html"),
    ("jack", "Jack Hills, Australia", -26.00, 117.00,
     "reef2", "Cairns, Great Barrier Reef coast", -16.92, 145.78,
     "https://www.savingplanets.com/Oceans.html"),
    ("greenland", "Greenland ice core", 72.58, -37.64,
     "polar", "Syowa Station, East Antarctica", -69.00, 39.58,
     "https://www.savingplanets.com/Polar.html"),
]


def look_basis():
    look = np.array([np.cos(LAT0) * np.cos(LON0), np.sin(LAT0), np.cos(LAT0) * np.sin(LON0)], np.float64)
    up = np.array([0.0, 1.0, 0.0])
    east = np.cross(look, up)
    east /= np.linalg.norm(east)
    north = np.cross(east, look)
    return look, east, north


LOOK, EAST, NORTH = look_basis()


def fetch(url, dest, tries=4):
    if os.path.exists(dest) and os.path.getsize(dest) > 40 and open(dest, "rb").read(1) == b"{":
        return dest
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "BeforeSavingPlanets/morph-v2"})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if not data.startswith(b"{") and not data.startswith(b"["):
                raise RuntimeError("not json (%s bytes)" % len(data))
            if b"999.99" in data and b"MultiPoint" in data:
                pass
            if len(data) < 40:
                raise RuntimeError("short response %s" % len(data))
            open(dest, "wb").write(data)
            return dest
        except Exception as e:
            err = e
    raise RuntimeError("%s failed: %s" % (url, err))


def coast_path(ma):
    return os.path.join(CACHE, "coast-%03d.json" % ma)


def fetch_coast(ma):
    url = "https://gws.gplates.org/reconstruct/coastlines/?time=%d&model=PALEOMAP&wrap=true" % ma
    return ma, fetch(url, coast_path(ma))


def fetch_all_coasts():
    os.makedirs(CACHE, exist_ok=True)
    ages = list(range(0, 541, STEP))
    missing = [a for a in ages if not (os.path.exists(coast_path(a)) and os.path.getsize(coast_path(a)) > 1000)]
    print("coastlines", len(ages), "cached", len(ages) - len(missing))
    if not missing:
        return ages
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(fetch_coast, a) for a in missing]
        done = 0
        for f in as_completed(futs):
            f.result()
            done += 1
            if done % 10 == 0 or done == len(missing):
                print("  fetched", done, "/", len(missing))
    return ages


def fetch_pins():
    ages = list(range(0, 541, 10))
    # one request per age, all 8 points: lon,lat repeating
    pts = []
    for p in PAIRS:
        pts += [p[3], p[2], p[7], p[6]]  # lon, lat of fossil then solution
    q = ",".join("%.4f" % v for v in pts)
    out = {"model": "PALEOMAP", "stepMa": 10, "pairs": [], "ages": ages, "coords": {}}
    for p in PAIRS:
        out["pairs"].append({
            "id": p[0], "fossil": p[1], "flat": p[2], "flon": p[3],
            "sid": p[4], "solution": p[5], "slat": p[6], "slon": p[7], "href": p[8],
        })
    print("reconstructing pins", len(ages))
    for ma in ages:
        url = "https://gws.gplates.org/reconstruct/reconstruct_points/?points=%s&time=%d&model=PALEOMAP" % (q, ma)
        dest = os.path.join(CACHE, "pins-%03d.json" % ma)
        fetch(url, dest)
        data = json.load(open(dest))
        coords = data["coordinates"]
        if any(abs(c[0]) > 900 or abs(c[1]) > 900 for c in coords):
            raise RuntimeError("unreconstructed point at %s Ma: %s" % (ma, coords))
        out["coords"][str(ma)] = [[round(c[0], 3), round(c[1], 3)] for c in coords]
    dest = os.path.join(ROOT, "assets/data/paleo-pins.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    json.dump(out, open(dest, "w"), separators=(",", ":"))
    print("pins", dest, os.path.getsize(dest))
    return out


def lonlat_xyz(lon, lat):
    la = np.deg2rad(lat)
    lo = np.deg2rad(lon)
    cl = np.cos(la)
    return np.stack([cl * np.cos(lo), np.sin(la), cl * np.sin(lo)], axis=-1)


def clip_front(xyz, eps=0.04):
    if len(xyz) < 3:
        return []
    d = xyz @ LOOK
    out = []
    n = len(xyz)
    for i in range(n):
        a = xyz[i]
        b = xyz[(i + 1) % n]
        da = d[i]
        db = d[(i + 1) % n]
        if da >= eps and db >= eps:
            out.append(b)
        elif da >= eps and db < eps:
            t = (da - eps) / (da - db)
            out.append(a + (b - a) * t)
        elif da < eps and db >= eps:
            t = (eps - da) / (db - da)
            out.append(a + (b - a) * t)
            out.append(b)
    return out


def to_px(xyz, R):
    p = np.asarray(xyz, np.float64)
    x = p @ EAST
    y = p @ NORTH
    return np.stack([CX + x * R, CY - y * R], axis=1)


def land_row_colors(h):
    lat = 90.0 - (np.arange(h) + 0.5) * 180.0 / h
    cols = np.zeros((h, 3), np.uint8)
    for i, la in enumerate(lat):
        a = abs(la)
        if a >= 68:
            cols[i] = (214, 220, 224)
        elif a >= 48:
            t = (a - 48) / 20.0
            cols[i] = (int(118 + t * 70), int(132 - t * 10), int(72 + t * 40))
        else:
            t = a / 48.0
            cols[i] = (int(78 + t * 50), int(118 - t * 10), int(58 + t * 16))
    return cols


def raster_eq(features, size=1600):
    """Equirectangular land mask, used by the Dig Quest globe (not the hero video)."""
    W = size
    H = size // 2
    mask = Image.new("L", (W, H), 0)
    dr = ImageDraw.Draw(mask)
    for feat in features:
        g = feat.get("geometry") or {}
        t = g.get("type")
        polys = [g["coordinates"]] if t == "Polygon" else g.get("coordinates") or []
        if t not in ("Polygon", "MultiPolygon"):
            continue
        for poly in polys:
            for hi, ring in enumerate(poly):
                if len(ring) < 3:
                    continue
                step = max(1, len(ring) // 800)
                pts = []
                prev = None
                for lon, lat in ring[::step]:
                    lon = ((lon + 180.0) % 360.0) - 180.0
                    if prev is not None and abs(lon - prev) > 180:
                        if len(pts) >= 3:
                            dr.polygon(pts, fill=0 if hi else 255)
                        pts = []
                    pts.append(((lon + 180.0) / 360.0 * (W - 1), (90.0 - lat) / 180.0 * (H - 1)))
                    prev = lon
                if len(pts) >= 3:
                    dr.polygon(pts, fill=0 if hi else 255)
    arr = np.asarray(mask)
    cols = land_row_colors(H)
    rgb = np.empty((H, W, 3), np.uint8)
    rgb[:] = OCEAN
    land = arr > 127
    rgb[land] = cols[np.where(land)[0]]
    return rgb


def draw_globe_vectors(features, R, base):
    im = base.copy()
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dr = ImageDraw.Draw(overlay)
    ocean = (6, 32, 78, 255)
    # ocean disk first
    dr.ellipse([CX - R, CY - R, CX + R, CY + R], fill=ocean)
    for feat in features:
        g = feat.get("geometry") or {}
        t = g.get("type")
        if t == "Polygon":
            polys = [g["coordinates"]]
        elif t == "MultiPolygon":
            polys = g["coordinates"]
        else:
            continue
        for poly in polys:
            for hi, ring in enumerate(poly):
                if len(ring) < 3:
                    continue
                step = 1 if len(ring) < 600 else max(1, len(ring) // 500)
                ll = np.asarray(ring[::step], np.float64)
                xyz = lonlat_xyz(ll[:, 0], ll[:, 1])
                front = clip_front(xyz)
                if len(front) < 3:
                    continue
                px = to_px(front, R)
                # latitude of the ring's mean for a flat land color
                lat = float(np.mean(ll[:, 1]))
                a = abs(lat)
                if a >= 68:
                    col = (214, 220, 224, 255)
                elif a >= 48:
                    col = (168, 140, 96, 255)
                else:
                    col = (96, 124, 68, 255)
                if hi:
                    col = ocean
                dr.polygon([tuple(p) for p in px], fill=col)
    return im, overlay


def shade_disk(R):
    """Lambert shade and rim for a disk of radius R. Cached by rounding R."""
    yy, xx = np.mgrid[0:H, 0:W]
    x = (xx - CX) / R
    y = (CY - yy) / R
    m = x * x + y * y
    front = m <= 1.0
    z = np.zeros_like(x)
    z[front] = np.sqrt(1.0 - m[front])
    # light from the upper left, mostly in front, so the disk stays readable
    lx, ly, lz = -0.22, 0.38, 0.90
    ln = (lx * lx + ly * ly + lz * lz) ** 0.5
    ndot = np.clip((x * lx + y * ly + z * lz) / ln, 0, 1)
    shade = np.where(front, 0.48 + 0.62 * ndot, 0.0).astype(np.float32)
    rim = np.clip(1.0 - z, 0, 1) ** 1.6
    return front, shade, rim, m


_SHADE = {}


def shade_for(R):
    key = int(round(R))
    if key not in _SHADE:
        _SHADE[key] = shade_disk(float(key))
    return _SHADE[key]


def composite(base_rgb, overlay_rgba, R):
    front, shade, rim, m = shade_for(R)
    ov = np.asarray(overlay_rgba).astype(np.float32)
    a = ov[:, :, 3:4] / 255.0
    rgb = base_rgb.astype(np.float32)
    # only the globe disk receives the overlay; feather the limb
    disk = np.clip((1.02 - np.sqrt(np.maximum(m, 0))) * 40.0, 0, 1)[:, :, None]
    a = a * disk
    lit = ov[:, :, :3] * shade[:, :, None]
    # blue atmospheric rim
    lit = lit + np.array([80, 150, 220], np.float32) * (rim * front)[:, :, None] * 0.55
    out = rgb * (1 - a) + lit * a
    # soft glow just outside the disk
    glow = np.clip(1.0 - np.abs(np.sqrt(np.maximum(m, 0)) - 1.0) * 18.0, 0, 1)
    glow = glow * (m > 0.86) * (m < 1.18)
    out += np.array([40, 90, 160], np.float32) * glow[:, :, None] * 0.45
    return np.clip(out, 0, 255).astype(np.uint8)


def starfield():
    """SI Earth frame with the planet removed, so the nebula and stars stay."""
    dest = os.path.join(TMP, "stars.png")
    os.makedirs(TMP, exist_ok=True)
    if not os.path.exists(dest):
        src = os.environ.get("MORPH_SRC", SRC)
        subprocess.check_call([
            "ffmpeg", "-y", "-ss", "9.7", "-i", src, "-frames:v", "1", dest
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = np.asarray(Image.open(dest).convert("RGB")).astype(np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt((xx - CX) ** 2 + (yy - CY) ** 2)
    # cover the planet and its glow; keep stars and the nebula outside
    m = np.clip((r - 500.0) / 70.0, 0, 1)[:, :, None]
    return (im * m).astype(np.uint8)


def render_paleo_frame(features, R, bg):
    base = Image.fromarray(bg)
    im, ov = draw_globe_vectors(features, R, base)
    return composite(np.asarray(im), ov, R)


def render_eq(marble, R, bg):
    """Sample an equirectangular texture (Blue Marble or a paleomap) onto the globe."""
    R = float(int(round(R)))
    mh, mw = marble.shape[:2]
    front, shade, rim, m = shade_for(R)
    yy, xx = np.mgrid[0:H, 0:W]
    x = (xx - CX) / R
    y = (CY - yy) / R
    z = np.zeros_like(x)
    z[front] = np.sqrt(np.maximum(1.0 - x * x - y * y, 0))[front]
    world = (x[:, :, None] * EAST + y[:, :, None] * NORTH + z[:, :, None] * LOOK)
    lat = np.arcsin(np.clip(world[:, :, 1], -1, 1))
    lon = np.arctan2(world[:, :, 2], world[:, :, 0])
    u = (lon + np.pi) / (2 * np.pi) * (mw - 1)
    v = (np.pi / 2 - lat) / np.pi * (mh - 1)
    ui = np.clip(u.astype(np.int32), 0, mw - 1)
    vi = np.clip(v.astype(np.int32), 0, mh - 1)
    col = marble[vi, ui].astype(np.float32)
    col *= shade[:, :, None]
    col += np.array([80, 150, 220], np.float32) * (rim * front)[:, :, None] * 0.45
    rgb = bg.astype(np.float32)
    disk = np.clip((1.02 - np.sqrt(np.maximum(m, 0))) * 40.0, 0, 1)[:, :, None]
    out = rgb * (1 - disk) + col * disk
    glow = np.clip(1.0 - np.abs(np.sqrt(np.maximum(m, 0)) - 1.0) * 18.0, 0, 1)
    glow = glow * (m > 0.86) * (m < 1.18)
    out += np.array([40, 90, 160], np.float32) * glow[:, :, None] * 0.45
    return np.clip(out, 0, 255).astype(np.uint8)


def save_globe_textures(marble):
    """Small equirect masks for the quest scrubber, every 20 Ma, plus Blue Marble."""
    dest_dir = os.path.join(ROOT, "assets/hero/paleo")
    os.makedirs(dest_dir, exist_ok=True)
    im = Image.fromarray(marble).resize((1024, 512), Image.Resampling.LANCZOS)
    im.save(os.path.join(dest_dir, "earth.webp"), "WEBP", quality=72, method=4)
    for ma in range(0, 541, 20):
        feats = json.load(open(coast_path(ma)))["features"]
        rgb = raster_eq(feats, 640)
        Image.fromarray(rgb).save(os.path.join(dest_dir, "m%03d.webp" % ma), "WEBP", quality=68, method=4)
    print("textures", dest_dir)


def encode():
    os.makedirs(TMP, exist_ok=True)
    # The published mp4 is replaced in place. Keep the SI source for the opening.
    snap = os.path.join(TMP, "si-source.mp4")
    if not os.path.exists(snap):
        subprocess.check_call(["cp", SRC, snap])
    # starfield() and the SI trim read SRC; point them at the snapshot once it exists.
    os.environ["MORPH_SRC"] = snap
    bg = starfield()
    marble = np.asarray(Image.open(BM).convert("RGB"))
    ages = fetch_all_coasts()
    # Drift occupies 258 frames (8.6s). Blue-marble resolve 18 frames. Hold 36. Total 10.4s.
    drift_n = 258
    blend_n = 18
    hold_n = 36
    # radius eases from just under the SI globe to the finish size
    def radius(i, n):
        t = i / max(1, n - 1)
        t = t * t * (3 - 2 * t)
        return 452.0 + (488.0 - 452.0) * t

    paleo_mp4 = os.path.join(TMP, "paleo.mp4")
    enc = subprocess.Popen([
        "ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H), "-r", "30",
        "-i", "-", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "veryfast",
        "-movflags", "+faststart", paleo_mp4
    ], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendering drift", len(ages), "ages ->", drift_n, "frames")
    eq_cache = {}
    paleo_last = None
    total_n = drift_n + blend_n + hold_n
    for i in range(drift_n):
        t = i / max(1, drift_n - 1)
        ma = 540 * (1 - t)
        # snap to a reconstructed age so each step is a real map, held across a few frames
        ma_q = int(round(ma / STEP) * STEP)
        ma_q = max(0, min(540, ma_q))
        if ma_q not in eq_cache:
            feats = json.load(open(coast_path(ma_q)))["features"]
            eq_cache[ma_q] = raster_eq(feats, 1600)
        R = radius(i, total_n)
        frame = render_eq(eq_cache[ma_q], R, bg)
        enc.stdin.write(frame.tobytes())
        paleo_last = frame
        if i % 30 == 0:
            print("  frame", i, "Ma", ma_q)
        if len(eq_cache) > 2:
            for k in list(eq_cache):
                if k != ma_q:
                    del eq_cache[k]
    marble_frame = render_eq(marble, radius(drift_n + blend_n, drift_n + blend_n + hold_n), bg)
    for j in range(blend_n):
        a = (j + 1) / blend_n
        mix = (paleo_last.astype(np.float32) * (1 - a) + marble_frame.astype(np.float32) * a).astype(np.uint8)
        enc.stdin.write(mix.tobytes())
    for j in range(hold_n):
        enc.stdin.write(marble_frame.tobytes())
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError("paleo encode failed")
    nframes = drift_n + blend_n + hold_n
    print("paleo frames", nframes)

    # SI interpretation: lava hold, then cooling crust and first oceans. Stop before the old Pangaea blend.
    si_mp4 = os.path.join(TMP, "si.mp4")
    subprocess.check_call([
        "ffmpeg", "-y", "-i", os.environ.get("MORPH_SRC", SRC), "-filter_complex",
        "[0:v]trim=0:1.70,setpts=(PTS-STARTPTS)*2.0/1.70,fps=30[a];"
        "[0:v]trim=1.70:3.45,setpts=(PTS-STARTPTS)*3.40/1.75,fps=30[b];"
        "[a][b]concat=n=2:v=1:a=0,format=yuv420p",
        "-an", "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", si_mp4
    ])

    # 5.4s SI, fade 0.8s into the drift (offset 4.6).
    mixed = os.path.join(TMP, "mixed.mp4")
    subprocess.check_call([
        "ffmpeg", "-y", "-i", si_mp4, "-i", paleo_mp4, "-filter_complex",
        "[0:v][1:v]xfade=transition=fade:duration=0.8:offset=4.6,format=yuv420p",
        "-an", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", mixed
    ])

    # Web-friendly master. CRF tuned toward ≤3 MB; GOP 60 like the previous hero.
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    subprocess.check_call([
        "ffmpeg", "-y", "-i", mixed,
        "-c:v", "libx264", "-preset", "slow", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-crf", "30", "-g", "60", "-keyint_min", "60", "-movflags", "+faststart",
        "-an", OUT
    ])
    print("wrote", OUT, os.path.getsize(OUT))

    # Stills: reduced-motion end frame, and era cards.
    stills = {
        "end.webp": "14.7",
        "era-oceans.webp": "4.2",
        "era-540.webp": "6.4",
        "era-drift.webp": "10.2",
        "era-today.webp": "14.7",
    }
    for name, ts in stills.items():
        dest = os.path.join(ROOT, "assets/hero/morph", name)
        subprocess.check_call([
            "ffmpeg", "-y", "-ss", ts, "-i", OUT, "-frames:v", "1",
            "-vf", "scale=1280:-2" if name != "end.webp" else "scale=1920:-2",
            "-c:v", "libwebp", "-quality", "74", dest
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(name, os.path.getsize(dest))
    save_globe_textures(marble)


if __name__ == "__main__":
    import sys
    if "--pins-only" in sys.argv:
        fetch_pins()
    elif "--preview" in sys.argv:
        os.makedirs(TMP, exist_ok=True)
        bg = starfield()
        marble = np.asarray(Image.open(BM).convert("RGB"))
        Image.fromarray(render_eq(marble, 480, bg)).save("/tmp/morph-v2/preview-earth.jpg", quality=80)
        for ma in (540, 250, 0):
            p = coast_path(ma)
            if not os.path.exists(p):
                fetch_coast(ma)
            feats = json.load(open(p))["features"]
            Image.fromarray(render_paleo_frame(feats, 470, bg)).save("/tmp/morph-v2/preview-%d.jpg" % ma, quality=80)
            print("preview", ma)
        print("preview earth")
    else:
        fetch_pins()
        encode()
