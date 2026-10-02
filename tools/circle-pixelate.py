#!/usr/bin/env python3
"""Builds the circles of the Hell pack: one landscape (1920×1080) and one portrait (1080×1920)
picture for each of the nine circles of angelOS's hell, made the way hell-pixelate.py makes
the rest — a public-domain painting cropped, reduced to 1/4, mapped through a gradient,
pushed into 16 colours with 4×4 Bayer dithering and scaled back up without smoothing — but
in the circle's own colours: the 16 colours are sampled from the circle's palette in
angelOS (story/circles.json: body → face → rim → dim text → text, and the accent family).

  circle-pixelate.py [CIRCLES_JSON] [--only CIRCLE …]

The sources are Gustave Doré's engravings for Dante's Inferno (1861; Wikimedia Commons,
public domain), one scene of each circle — downloaded into ./src/ by hand or with the
list in Hell/CREDITS.md (src/sources.json keeps what was used). Writes ../Hell/hell-<circle>.png
and ../Hell/hell-<circle>-portrait.png. Needs numpy and Pillow.
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance

HERE = Path(__file__).resolve().parent
OUT = Path(__import__("os").environ.get("CIRCLE_OUT", HERE.parent / "Hell"))
B4 = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16 - 0.5

# (source in ./src, box: vertical and horizontal place of the crop 0..1, gradient mix, gamma)
# The engravings are mostly paper: a gamma like hell-pixelate.py's Lucifer (1.9) sinks it
# into the circle's dark, the lines and the lit figures stay.
JOBS = {
    "limbo": [("limbo-l", 0.6, 0.5, 0.75, 2.4), ("limbo-p", 0.35, 0.5, 0.6, 1.8)],
    "lust": [("lust-l", 0.3, 0.5, 0.65, 1.7), ("lust-p", 0.4, 0.5, 0.65, 1.7)],
    "gluttony": [("gluttony", 0.45, 0.5, 0.65, 1.8), ("gluttony", 0.4, 0.42, 0.65, 1.8)],
    "greed": [("greed", 0.5, 0.5, 0.75, 2.5), ("greed", 0.45, 0.35, 0.75, 2.5)],
    "wrath": [("wrath-l", 0.55, 0.5, 0.65, 1.8), ("wrath-p", 0.5, 0.5, 0.65, 1.8)],
    "heresy": [("heresy-l", 0.3, 0.5, 0.65, 1.8), ("heresy-p", 0.4, 0.5, 0.65, 1.8)],
    "violence": [("violence-l", 0.5, 0.5, 0.65, 1.8), ("violence-p", 0.4, 0.5, 0.65, 1.8)],
    "fraud": [("fraud-l", 0.5, 0.5, 0.7, 1.9), ("fraud-p", 0.4, 0.5, 0.7, 1.9)],
    "treachery": [("treachery-l", 0.5, 0.5, 0.65, 1.8), ("treachery-p", 0.6, 0.5, 0.65, 1.8)],
}
TRIM = 0.05     # the scan's margins and the plate's border, off every side first


def rgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


def circle_colours(circles, cid):
    """the circle's palette over base, as angelOS merges it (config/HellLook.qml)"""
    pal = dict(circles["base"]["palette"])
    pal.update(circles[cid].get("palette", {}))
    return pal


def gradient(pal):
    """dark → light through the circle: its body, faces, rim, the blood and the accent's
    family in the middle tones, dim text, text"""
    return [(0.0, pal["body"]), (0.16, pal["faceAlt"]), (0.32, pal["rim"]), (0.5, pal["blood"]),
            (0.66, pal["flame"]), (0.8, pal["accent"]), (0.9, pal["textDim"]), (1.0, pal["text"])]


def palette16(pal):
    """16 colours: 12 steps along the gradient, plus the ember, gold, edge and hi"""
    stops = [(p, rgb(h)) for p, h in gradient(pal)]
    cols = []
    for k in range(12):
        t = k / 11
        for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
            if p0 <= t <= p1:
                cols.append(c0 + (c1 - c0) * ((t - p0) / max(1e-6, p1 - p0)))
                break
    for key in ("ember", "gold", "edge", "hi"):
        cols.append(rgb(pal[key]))
    return np.array(cols)


def gradmap(lum, stops):
    out = np.zeros(lum.shape + (3,))
    st = [(p, rgb(h)) for p, h in stops]
    for (p0, c0), (p1, c1) in zip(st, st[1:]):
        m = (lum >= p0) & (lum <= p1)
        t = ((lum - p0) / max(1e-6, p1 - p0))[..., None]
        out[m] = (c0 + (c1 - c0) * t)[m]
    return out


def crop_box(w, h, cy, cx, portrait):
    r = 9 / 16 if portrait else 16 / 9
    if w / h > r:
        bw, bh = int(h * r), h
    else:
        bw, bh = w, int(w / r)
    x = int((w - bw) * cx)
    y = int((h - bh) * cy)
    return (x, y, x + bw, y + bh)


def pixel(src, portrait, cy, cx, mix, gamma, pal, out, spread=26, contrast=1.2, scale=4):
    im = Image.open(src).convert("RGB")
    tw, th = int(im.width * TRIM), int(im.height * TRIM)
    im = im.crop((tw, th, im.width - tw, im.height - th))
    im = im.crop(crop_box(im.width, im.height, cy, cx, portrait))
    im = ImageEnhance.Contrast(im).enhance(contrast)
    size = (270, 480) if portrait else (480, 270)
    im = im.resize(size, Image.LANCZOS)
    a = np.asarray(im, float)
    lum = np.clip(((0.3 * a[..., 0] + 0.55 * a[..., 1] + 0.15 * a[..., 2]) / 255) ** gamma, 0, 1)
    # the engravings are black and white: their light is laid onto the circle's gradient
    a = a * (1 - mix) + gradmap(lum, gradient(pal)) * mix
    h, w, _ = a.shape
    a = a + np.tile(B4, (h // 4 + 1, w // 4 + 1))[:h, :w, None] * spread
    P = palette16(pal)
    d = ((a[:, :, None, :] - P[None, None, :, :]) ** 2).sum(-1)
    q = P[d.argmin(-1)].astype(np.uint8)
    Image.fromarray(q).resize((w * scale, h * scale), Image.NEAREST).save(out, optimize=True)


def main():
    args = sys.argv[1:]
    path = Path.home() / ".config/quickshell/angelos/story/circles.json"
    only = []
    while args:
        a = args.pop(0)
        if a == "--only":
            only.append(args.pop(0))
        else:
            path = Path(a)
    circles = json.loads(path.read_text())
    for cid, (land, port) in JOBS.items():
        if only and cid not in only:
            continue
        pal = circle_colours(circles, cid)
        for (name, cy, cx, mix, gamma), portrait in ((land, False), (port, True)):
            out = OUT / ("hell-%s%s.png" % (cid, "-portrait" if portrait else ""))
            pixel(HERE / "src" / (name + ".jpg"), portrait, cy, cx, mix, gamma, pal, out)
            print(out.name)


if __name__ == "__main__":
    main()
