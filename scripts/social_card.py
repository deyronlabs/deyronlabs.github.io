#!/usr/bin/env python3
"""Deyron Labs card generator (Inter, #1a1a1a, green #22c55e, amber #f59e0b).
Usage: social_card.py spec.json   (spec: tag, title, bullets[], footer, outputs[{path,w,h}])"""
import json, sys
from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(F + f"Inter-{w}.otf", s)
GREEN, AMBER, WHITE, GREY, BG = "#22c55e", "#f59e0b", "#ffffff", "#9a9a9a", "#1a1a1a"
def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines
def render(spec, w, h, path):
    S = 2; W, H = w*S, h*S
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    u = min(w, h*16/9) / 1280 * (1.0 if w >= h else 1.0)
    if h > w: u = w / 1080 * 1.0
    pad = int((w*0.062 if h > w else 80*w/1280) * S); bar = int(14*S*w/1280) if w >= h else int(12*S)
    d.rectangle([0, 0, bar, H], fill=GREEN)
    fs = lambda base: int(base * u * S)
    ft, fh, fb, ff = font("Bold", fs(21 if h<=w else 22)), font("Bold", fs(54 if h<=w else 56)), font("Regular", fs(32 if h<=w else 30)), font("Regular", fs(21))
    if w == 1200 and h == 627: u2 = 0.88; fh, fb = font("Bold", int(54*u2*S)), font("Regular", int(30*u2*S)); ft = font("Bold", int(20*S)); ff = font("Regular", int(19*S))
    maxw = W - 2*pad
    # measure
    hl = wrap(d, spec["title"], fh, maxw); lh = int(fh.size*1.18)
    bl = []; 
    for b in spec["bullets"]:
        ls = wrap(d, b, fb, maxw - int(fb.size*1.3)); bl.append(ls)
    bh = int(fb.size*1.3)
    total = ft.size*2.6 + len(hl)*lh + fb.size*0.9 + sum(len(l)*bh + fb.size*0.45 for l in bl)
    foot_h = ff.size*3.4
    top = int(pad*0.8) if h <= w*0.6 else max(int(pad*0.8), int((H - total - foot_h)/2))
    y = top
    d.text((pad, y), "DEYRON LABS  ·  AI tools, tested.", font=ft, fill=GREEN); y += int(ft.size*1.4)
    d.text((pad, y), spec["tag"], font=ft, fill=AMBER); y += int(ft.size*1.9)
    for l in hl: d.text((pad, y), l, font=fh, fill=WHITE); y += lh
    y += int(fb.size*0.9)
    for ls in bl:
        r = int(fb.size*0.16); cy = y + int(fb.size*0.62)
        d.ellipse([pad, cy-r, pad+2*r, cy+r], fill=GREEN)
        for l in ls: d.text((pad+int(fb.size*1.3), y), l, font=fb, fill=WHITE); y += bh
        y += int(fb.size*0.45)
    fy = H - int(pad*0.8) - int(ff.size*2.7)
    for l in wrap(d, spec["footer"], ff, maxw):
        d.text((pad, fy), l, font=ff, fill=AMBER); fy += int(ff.size*1.3)
    d.text((pad, fy+int(ff.size*0.3)), "deyronlabs.com", font=font("Bold", int(ff.size*1.15)), fill=GREY)
    im = im.resize((w, h), Image.LANCZOS)
    if path.endswith(".jpg"): im.save(path, quality=92)
    else: im.save(path)
if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    for o in spec["outputs"]: render(spec, o["w"], o["h"], o["path"])
