#!/usr/bin/env python3
"""Short: Meta Muse Spark Open (motion-graphics style, PIL + ffmpeg). Usage: MP3_DIR=... OUT_DIR=... python3 build_muse_short.py"""
import os, re, subprocess, math
from PIL import Image, ImageDraw, ImageFont

MP3 = os.environ["MP3_DIR"]
OUT = os.environ["OUT_DIR"]
FR = f"{OUT}/frames"
os.makedirs(FR, exist_ok=True)

F = "/usr/share/fonts/opentype/inter/"
XB, BD, SB, MD = F + "Inter-ExtraBold.otf", F + "Inter-Bold.otf", F + "Inter-SemiBold.otf", F + "Inter-Medium.otf"
W, H = 1080, 1920
NIGHT = (18, 18, 28)
GREEN, CYAN, VIOLET, MAGENTA, AMBER = (34, 197, 94), (34, 211, 238), (139, 92, 246), (236, 72, 153), (245, 158, 11)
WHITE, GREY, RED = (255, 255, 255), (150, 156, 175), (239, 68, 68)
LEAD, GAP, TAIL = 0.3, 0.2, 1.2

SEGS = {
 1: "Meta has released Muse Spark Open, a huge AI model whose weights anyone can download.",
 2: "816 billion parameters, 42 billion active, and a 1 million token context.",
 3: "The catch is the license. Anyone can use and fine-tune it, but a company above $20 million in revenue needs a separate deal with Meta to offer it as a service.",
 4: "Meta calls it the most capable US open-weight model. But on Meta's own table, Kimi K3 and GLM 5.3 score higher on the Artificial Analysis index: 44 and 45, against 39.",
 5: "And you will not run it on a laptop. The smallest official version needs at least 700 gigabytes of GPU memory.",
 6: "Why it matters: an open model with terms most teams can accept. Independent tests will show how it holds up. Sources and details at deyronlabs.com.",
}

def fnt(p, s): return ImageFont.truetype(p, s)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2500:]); raise SystemExit(1)
    return r

def dur(p):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).stdout)

def speech_intervals(p, d):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    sp, cur = [], 0.0
    for i, s in enumerate(st):
        e = en[i] if i < len(en) else d
        if s - cur > 0.05: sp.append((cur, s))
        cur = e
    if d - cur > 0.05: sp.append((cur, d))
    return sp or [(0, d)]

def to_real(sp, x):
    acc = 0.0
    for s, e in sp:
        if x <= acc + (e - s) + 1e-9: return s + (x - acc)
        acc += e - s
    return sp[-1][1]

# ------------------------------------------------------------------ drawing helpers
def tw(d, t, f): return d.textlength(t, font=f)

def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(d, t, f) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def ctext(d, y, t, f, fill=WHITE, shadow=True, cx=W // 2):
    x = cx - tw(d, t, f) / 2
    if shadow: d.text((x + 3, y + 4), t, font=f, fill=(0, 0, 0))
    d.text((x, y), t, font=f, fill=fill)

def block(d, y, text, f, maxw, fill=WHITE, lh=1.18, cx=W // 2):
    for ln in wrap(d, text, f, maxw):
        ctext(d, y, ln, f, fill, cx=cx); y += int(f.size * lh)
    return y

def pill(d, cx, y, t, f, bg, fg=(20, 20, 20), padx=30, pady=12):
    w = tw(d, t, f) + padx * 2; h = f.size + pady * 2
    d.rounded_rectangle([cx - w / 2, y, cx + w / 2, y + h], radius=h / 2, fill=bg)
    d.text((cx - w / 2 + padx, y + pady - 2), t, font=f, fill=fg)
    return y + h

def cube(d, x, y, s):
    """small isometric cube, centre (x, y)."""
    a = s
    top = [(x, y - a), (x + a * .87, y - a / 2), (x, y), (x - a * .87, y - a / 2)]
    left = [(x - a * .87, y - a / 2), (x, y), (x, y + a), (x - a * .87, y + a / 2)]
    right = [(x + a * .87, y - a / 2), (x, y), (x, y + a), (x + a * .87, y + a / 2)]
    d.polygon(top, fill=(134, 239, 172)); d.polygon(left, fill=GREEN); d.polygon(right, fill=(21, 128, 61))

def background():
    img = Image.new("RGB", (W, H), NIGHT)
    d = ImageDraw.Draw(img)
    for yy in range(0, H, 4):
        t = yy / H
        d.rectangle([0, yy, W, yy + 4], fill=(int(16 + 10 * t), int(18 + 6 * t), int(34 + 20 * t)))
    # dot grid
    for gx in range(60, W, 90):
        for gy in range(120, H - 100, 90):
            d.ellipse([gx - 2, gy - 2, gx + 2, gy + 2], fill=(40, 46, 70))
    # header
    cube(d, 96, 150, 34)
    d.text((150, 118), "DEYRON LABS", font=fnt(XB, 40), fill=WHITE)
    d.text((152, 166), "AI NEWS · AI TOOLS, TESTED.", font=fnt(BD, 24), fill=GREEN)
    pill(d, 900, 128, "15 OCT 2026", fnt(XB, 28), AMBER, padx=26, pady=10)
    return img

# ------------------------------------------------------------------ scenes (area y≈300..1300)
def box(d, xy, fill, outline=None, r=36):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=5 if outline else 0)

def scene1():
    img = background(); d = ImageDraw.Draw(img)
    pill(d, W // 2, 340, "META · OPEN WEIGHTS", fnt(XB, 40), CYAN)
    y = block(d, 470, "Muse Spark", fnt(XB, 150), 960, WHITE)
    y = block(d, y, "Open", fnt(XB, 150), 960, GREEN)
    d.rounded_rectangle([140, y + 50, 940, y + 66], radius=8, fill=GREEN)
    ctext(d, y + 110, "weights anyone can download", fnt(SB, 48), GREY)
    ctext(d, y + 180, "Source: Meta announcement + model card", fnt(SB, 34), GREY)
    return img

def stat(d, x, y, w, h, big, small, col):
    box(d, [x, y, x + w, y + h], (26, 30, 50), col, r=32)
    ctext(d, y + 40, big, fnt(XB, 104), col, cx=x + w // 2)
    ctext(d, y + 170, small, fnt(SB, 40), WHITE, cx=x + w // 2)

def scene2():
    img = background(); d = ImageDraw.Draw(img)
    stat(d, 90, 360, 900, 260, "816B", "total parameters", GREEN)
    stat(d, 90, 660, 900, 260, "42B", "active per token", CYAN)
    stat(d, 90, 960, 900, 260, "1M", "token context", AMBER)
    return img

def scene3():
    img = background(); d = ImageDraw.Draw(img)
    pill(d, W // 2, 340, "THE LICENSE", fnt(XB, 40), CYAN)
    y = block(d, 450, "Use it.", fnt(XB, 100), 960, GREEN)
    y = block(d, y, "Fine-tune it.", fnt(XB, 100), 960, GREEN)
    box(d, [90, y + 60, 990, y + 470], (50, 38, 12), AMBER)
    ctext(d, y + 95, "OVER $20M REVENUE", fnt(XB, 58), AMBER)
    ctext(d, y + 180, "and offering it as a service?", fnt(SB, 40), WHITE)
    ctext(d, y + 280, "Separate deal", fnt(XB, 76), WHITE)
    ctext(d, y + 375, "with Meta", fnt(XB, 76), WHITE)
    return img

def scene4():
    img = background(); d = ImageDraw.Draw(img)
    ctext(d, 340, "Artificial Analysis Index", fnt(XB, 54), WHITE)
    ctext(d, 410, "from Meta's own table", fnt(SB, 36), GREY)
    rows = [("GLM 5.3", 45, CYAN), ("Kimi K3", 44, VIOLET), ("Muse Spark Open", 39, GREEN)]
    y = 520
    for name, v, col in rows:
        d.text((90, y), name, font=fnt(XB, 46), fill=WHITE)
        bw = int(900 * v / 50)
        d.rounded_rectangle([90, y + 70, 90 + bw, y + 150], radius=24, fill=col)
        d.text((90 + bw - 110, y + 80), str(v), font=fnt(XB, 60), fill=(15, 15, 25))
        y += 230
    ctext(d, y + 10, "Meta: \"most capable US open-weight model\"", fnt(SB, 34), GREY)
    return img

def scene5():
    img = background(); d = ImageDraw.Draw(img)
    pill(d, W // 2, 340, "SMALLEST OFFICIAL VERSION", fnt(XB, 36), CYAN)
    # laptop outline with red cross
    d.rounded_rectangle([300, 460, 780, 700], radius=24, outline=GREY, width=12)
    d.rounded_rectangle([220, 712, 860, 760], radius=20, fill=GREY)
    d.line([250, 440, 830, 780], fill=RED, width=22); d.line([830, 440, 250, 780], fill=RED, width=22)
    y = block(d, 860, "700 GB", fnt(XB, 150), 960, AMBER)
    ctext(d, y + 10, "of GPU memory, at least", fnt(SB, 50), WHITE)
    ctext(d, y + 100, "not a laptop model", fnt(SB, 40), GREY)
    return img

def scene6():
    img = background(); d = ImageDraw.Draw(img)
    y = block(d, 360, "Open weights,", fnt(XB, 96), 940, WHITE)
    y = block(d, y, "terms most teams", fnt(XB, 96), 940, WHITE)
    y = block(d, y, "can accept.", fnt(XB, 96), 940, GREEN)
    ctext(d, y + 20, "Independent tests come next.", fnt(SB, 44), GREY)
    pill(d, W // 2, y + 120, "deyronlabs.com", fnt(XB, 64), GREEN, padx=48, pady=20)
    ctext(d, y + 300, "AI-generated voice and visuals.", fnt(SB, 34), AMBER)
    ctext(d, y + 348, "Made with AI assistance (Claude).", fnt(SB, 34), AMBER)
    return img

SCENES = {1: scene1, 2: scene2, 3: scene3, 4: scene4, 5: scene5, 6: scene6}

# ------------------------------------------------------------------ subtitles
def chunks(text, maxc=30):
    sents = re.split(r"(?<=[.!?])\s+", text)
    out = []
    for s in sents:
        words, cur = s.split(), ""
        parts = []
        for w in words:
            if len((cur + " " + w).strip()) <= maxc * 2 and len((cur + " " + w).strip().split()) <= 9: cur = (cur + " " + w).strip()
            else: parts.append(cur); cur = w
        if cur: parts.append(cur)
        out += parts
    return out

def draw_sub(img, text):
    img = img.copy(); d = ImageDraw.Draw(img, "RGBA")
    f = fnt(XB, 58)
    lines = wrap(d, text, f, 900)
    bh = len(lines) * 74 + 36
    y0 = 1390
    d.rounded_rectangle([60, y0, 1020, y0 + bh], radius=30, fill=(8, 8, 16, 205))
    y = y0 + 18
    for ln in lines:
        x = W / 2 - tw(d, ln, f) / 2
        d.text((x, y), ln, font=f, fill=WHITE)
        y += 74
    return img

# ------------------------------------------------------------------ build
def main():
    timeline = []  # (png, dur)
    audio_parts = []
    t = 0.0
    # silence helper
    def sil(name, secs):
        p = f"{OUT}/{name}.wav"
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", f"{secs:.3f}", p]); return p
    audio_parts.append(sil("lead", LEAD))
    scene_imgs = {k: SCENES[k]() for k in SCENES}
    for k in range(1, 7):
        mp = f"{MP3}/seg-0{k}.mp3"
        wav = f"{OUT}/seg-0{k}.wav"
        run(["ffmpeg", "-y", "-i", mp, "-ac", "1", "-ar", "44100", wav])
        d = dur(mp)
        sp = speech_intervals(mp, d)
        total = sum(e - s for s, e in sp)
        ch = chunks(SEGS[k]); n = [len(c) for c in ch]; ct = sum(n)
        pre = LEAD if k == 1 else 0.0
        seg_len = d + GAP + (TAIL if k == 6 else 0.0)
        # cue times (relative to segment start)
        bounds, acc = [], 0
        for c, nn in zip(ch, n):
            a = to_real(sp, acc / ct * total + 0.001); acc += nn; b = to_real(sp, acc / ct * total - 0.001)
            bounds.append((c, a, b))
        # frames: each cue starts at its start; first starts at 0 (plus lead), last extends to segment end
        for i, (c, a, b) in enumerate(bounds):
            start = 0.0 if i == 0 else a - 0.05
            end = seg_len if i == len(bounds) - 1 else (bounds[i + 1][1] - 0.05)
            dd = end - start + (pre if i == 0 else 0)
            png = f"{FR}/s{k}_c{i}.png"
            draw_sub(scene_imgs[k], c).save(png)
            timeline.append((png, dd))
        audio_parts.append(wav)
        audio_parts.append(sil(f"gap{k}", GAP + (TAIL if k == 6 else 0.0)))
    # concat video
    lst = f"{OUT}/frames.txt"
    with open(lst, "w") as fh:
        for p, dd in timeline: fh.write(f"file '{p}'\nduration {dd:.3f}\n")
        fh.write(f"file '{timeline[-1][0]}'\n")
    al = f"{OUT}/audio.txt"
    with open(al, "w") as fh:
        for p in audio_parts: fh.write(f"file '{p}'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", al, "-c:a", "aac", "-b:a", "160k", f"{OUT}/audio.m4a"])
    total_v = sum(dd for _, dd in timeline)
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", f"{OUT}/audio.m4a",
         "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "copy", "-movflags", "+faststart", "-shortest", f"{OUT}/short-meta-muse-spark-open.mp4"])
    print("video seconds ~", round(total_v, 2), "audio", round(dur(f"{OUT}/audio.m4a"), 2))

    # cover 1080x1920
    img = background(); d = ImageDraw.Draw(img)
    pill(d, W // 2, 360, "AI NEWS · OPEN WEIGHTS", fnt(XB, 42), CYAN)
    ctext(d, 470, "Meta", fnt(XB, 90), GREY)
    y = block(d, 590, "Muse Spark", fnt(XB, 150), 960, WHITE)
    y = block(d, y, "Open", fnt(XB, 150), 960, GREEN)
    y = block(d, y + 20, "816B open weights", fnt(XB, 84), 960, AMBER)
    ctext(d, y + 40, "but check the license", fnt(SB, 56), WHITE)
    ctext(d, y + 130, "and the 700 GB GPU bill", fnt(SB, 44), GREY)
    ctext(d, 1700, "deyronlabs.com", fnt(XB, 54), GREEN)
    ctext(d, 1790, "AI-generated voice and visuals. Made with AI assistance (Claude).", fnt(SB, 26), AMBER)
    img.save(f"{OUT}/cover-short-meta-muse-spark-open-1080x1920.png")

if __name__ == "__main__":
    main()
