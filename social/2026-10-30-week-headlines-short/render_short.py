#!/usr/bin/env python3
"""Short 1080x1920 week headlines 30 Oct 2026. Usage: render_short.py segdir outdir"""
import sys, os, subprocess, math, re
from PIL import Image, ImageDraw, ImageFont

SEG, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
FD = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(FD + f"Inter-{w}.otf", s)
GREEN, AMBER, WHITE, GREY, BG, CARD = "#22c55e", "#f59e0b", "#ffffff", "#9a9a9a", "#1a1a1a", "#262626"
DGREEN, LGREEN = "#15803d", "#86efac"
W, H = 1080, 1920
S = 2  # supersample

SUB = {
 1: "Anthropic filed to go public, Google built a model only cyber defenders can use, and attackers are running AI agents. Here are this week's headlines in under a minute.",
 2: "One. Anthropic filed an S-1 to list on Nasdaq as ANT, reporting $16.3 billion of revenue in the first half of the year.",
 3: "Two. Google says Gemini 4 Carbon ranks first on a major index, but only a subset of cyber defenders can use it. All figures are Google's own.",
 4: "Three. CrowdStrike and Microsoft each report attackers using the open-source ARTEX agent framework. Both are vendor findings, not independently confirmed.",
 5: "Four. Mistral released the weights of Large 4, and OpenAI's GPT-6.1 Terra costs $1 in, $5 out, per million tokens.",
 6: "The full episode is on the Deyron Labs YouTube channel, and every article, with sources, is at deyronlabs.com. Disclosure: Claude, made by Anthropic, helps draft our articles, and the voice is AI.",
}

def dur(p):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())

def S_(v): return int(v*S)

def base():
    im = Image.new("RGB", (W*S, H*S), BG); d = ImageDraw.Draw(im)
    d.rectangle([0,0,S_(14),H*S], fill=GREEN)
    d.text((S_(70), S_(80)), "DEYRON LABS  ·  AI tools, tested.", font=font("Bold", S_(30)), fill=GREEN)
    return im, d

def cube(d, cx, cy, s, ):
    # isometric cube
    a = s; h = s*0.5
    top = [(cx, cy-a), (cx+a*0.866, cy-a/2), (cx, cy), (cx-a*0.866, cy-a/2)]
    left = [(cx-a*0.866, cy-a/2), (cx, cy), (cx, cy+a), (cx-a*0.866, cy+a/2)]
    right = [(cx+a*0.866, cy-a/2), (cx, cy), (cx, cy+a), (cx+a*0.866, cy+a/2)]
    d.polygon(top, fill=LGREEN); d.polygon(left, fill=GREEN); d.polygon(right, fill=DGREEN)

def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur+" "+w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def block(d, text, f, x, y, maxw, fill, lh=1.18):
    for l in wrap(d, text, f, maxw):
        d.text((x,y), l, font=f, fill=fill); y += int(f.size*lh)
    return y

def card(d, x0, y0, x1, y1, accent):
    d.rounded_rectangle([x0,y0,x1,y1], radius=S_(28), fill=CARD)
    d.rounded_rectangle([x0,y0,x0+S_(12),y1], radius=S_(6), fill=accent)

def scene(n):
    im, d = base()
    pad = S_(90); maxw = (W-180)*S
    if n == 1:
        cube(d, S_(540), S_(560), S_(190))
        d.text((pad, S_(840)), "FRIDAY 30 OCT 2026", font=font("Bold", S_(34)), fill=AMBER)
        block(d, "This week in AI", font("Bold", S_(110)), pad, S_(900), maxw, WHITE)
        d.text((pad, S_(1130)), "4 headlines", font=font("Bold", S_(76)), fill=GREEN)
    elif n == 2:
        d.text((pad, S_(300)), "1  ·  ANTHROPIC", font=font("Bold", S_(32)), fill=AMBER)
        card(d, S_(70), S_(400), S_(1010), S_(1060), GREEN)
        d.text((S_(130), S_(470)), "Files S-1 for", font=font("Regular", S_(46)), fill=GREY)
        d.text((S_(130), S_(540)), "Nasdaq: ANT", font=font("Bold", S_(120)), fill=WHITE)
        d.line([S_(130),S_(740),S_(950),S_(740)], fill="#3a3a3a", width=S_(3))
        d.text((S_(130), S_(780)), "First-half 2026 revenue", font=font("Regular", S_(46)), fill=GREY)
        d.text((S_(130), S_(850)), "$16.3B", font=font("Bold", S_(130)), fill=GREEN)
    elif n == 3:
        d.text((pad, S_(300)), "2  ·  GOOGLE", font=font("Bold", S_(32)), fill=AMBER)
        card(d, S_(70), S_(400), S_(1010), S_(1060), AMBER)
        d.text((S_(130), S_(470)), "Gemini 4 Carbon", font=font("Bold", S_(100)), fill=WHITE)
        d.text((S_(130), S_(620)), "Defenders only", font=font("Bold", S_(110)), fill=AMBER)
        block(d, "Only a subset of cyber defenders has access. No date for others.", font("Regular", S_(46)), S_(130), S_(790), S_(800), GREY, 1.2)
        d.text((S_(130), S_(990)), "Google's own figures", font=font("Bold", S_(40)), fill=AMBER)
    elif n == 4:
        d.text((pad, S_(300)), "3  ·  SECURITY", font=font("Bold", S_(32)), fill=AMBER)
        card(d, S_(70), S_(400), S_(1010), S_(1060), AMBER)
        d.text((S_(130), S_(470)), "ARTEX", font=font("Bold", S_(150)), fill=WHITE)
        block(d, "Open-source agent framework used in real attacks, per CrowdStrike and Microsoft.", font("Bold", S_(54)), S_(130), S_(680), S_(800), GREEN, 1.22)
        d.text((S_(130), S_(960)), "Not independently confirmed", font=font("Bold", S_(40)), fill=AMBER)
    elif n == 5:
        d.text((pad, S_(300)), "4  ·  MODELS", font=font("Bold", S_(32)), fill=AMBER)
        card(d, S_(70), S_(400), S_(1010), S_(1100), GREEN)
        d.text((S_(130), S_(470)), "Mistral Large 4", font=font("Bold", S_(90)), fill=WHITE)
        d.text((S_(130), S_(590)), "Open weights released", font=font("Bold", S_(52)), fill=GREEN)
        d.line([S_(130),S_(700),S_(950),S_(700)], fill="#3a3a3a", width=S_(3))
        d.text((S_(130), S_(740)), "OpenAI GPT-6.1 Terra", font=font("Regular", S_(46)), fill=GREY)
        d.text((S_(130), S_(810)), "$1 in  ·  $5 out", font=font("Bold", S_(110)), fill=WHITE)
        d.text((S_(130), S_(960)), "per 1M tokens", font=font("Regular", S_(44)), fill=GREY)
    elif n == 6:
        d.text((pad, S_(300)), "FULL EPISODE + SOURCES", font=font("Bold", S_(32)), fill=AMBER)
        card(d, S_(70), S_(400), S_(1010), S_(1060), GREEN)
        d.text((S_(130), S_(470)), "YouTube", font=font("Regular", S_(46)), fill=GREY)
        d.text((S_(130), S_(530)), "@DeyronLabs", font=font("Bold", S_(110)), fill=WHITE)
        d.line([S_(130),S_(730),S_(950),S_(730)], fill="#3a3a3a", width=S_(3))
        d.text((S_(130), S_(770)), "Every article, with sources", font=font("Regular", S_(46)), fill=GREY)
        d.text((S_(130), S_(840)), "deyronlabs.com", font=font("Bold", S_(100)), fill=GREEN)
    return im

def add_sub(im, text):
    im = im.copy(); d = ImageDraw.Draw(im)
    f = font("Bold", S_(60)); maxw = S_(900)
    lines = wrap(d, text, f, maxw)
    lh = int(f.size*1.25); bh = lh*len(lines) + S_(50)
    y0 = S_(1450)
    ov = Image.new("RGBA", im.size, (0,0,0,0)); od = ImageDraw.Draw(ov)
    od.rounded_rectangle([S_(60), y0, S_(1020), y0+bh], radius=S_(26), fill=(0,0,0,185))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(im)
    y = y0 + S_(25)
    for l in lines:
        tw = d.textlength(l, font=f)
        d.text(((W*S-tw)/2, y), l, font=f, fill=WHITE); y += lh
    return im

def chunks(text, maxchars=34):
    words = text.split(); out = []; cur = ""
    for w in words:
        t = (cur+" "+w).strip()
        if len(t) <= maxchars: cur = t
        else:
            out.append(cur); cur = w
    if cur: out.append(cur)
    # merge tiny tail
    if len(out) > 1 and len(out[-1]) < 10:
        last = out.pop(); out[-1] = out[-1] + " " + last
    return out

frames = []  # (png, duration)
audio = []
for n in range(1, 7):
    mp3 = os.path.join(SEG, f"seg-0{n}.mp3"); audio.append(mp3)
    D = dur(mp3) + (0.8 if n == 6 else 0.0)
    sc = scene(n)
    cs = chunks(SUB[n]); tot = sum(len(c) for c in cs)
    for i, c in enumerate(cs):
        dd = D * len(c)/tot
        p = os.path.join(OUT, f"f{n}_{i}.png")
        add_sub(sc, c).resize((W,H), Image.LANCZOS).save(p)
        frames.append((p, dd))
    print(n, round(D,2), cs)

with open(os.path.join(OUT, "list.txt"), "w") as f:
    for p, dd in frames: f.write(f"file '{p}'\nduration {dd:.4f}\n")
    f.write(f"file '{frames[-1][0]}'\n")
with open(os.path.join(OUT, "alist.txt"), "w") as f:
    for a in audio: f.write(f"file '{a}'\n")

# cover
cv, d = base(); cube(d, S_(540), S_(520), S_(180))
d.text((S_(90), S_(800)), "FRIDAY 30 OCT 2026", font=font("Bold", S_(40)), fill=AMBER)
y = block(d, "This week in AI.", font("Bold", S_(140)), S_(90), S_(870), (W-180)*S, WHITE)
y = block(d, "4 headlines in under a minute.", font("Bold", S_(70)), S_(90), y+S_(20), (W-180)*S, GREEN)
d.text((S_(90), S_(1700)), "deyronlabs.com", font=font("Regular", S_(44)), fill=GREY)
cv.resize((W,H), Image.LANCZOS).save(os.path.join(OUT, "cover.png"))

subprocess.check_call(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",os.path.join(OUT,"alist.txt"),"-c:a","libmp3lame","-b:a","128k","-ar","44100",os.path.join(OUT,"voice.mp3")])
subprocess.check_call(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",os.path.join(OUT,"list.txt"),"-i",os.path.join(OUT,"voice.mp3"),
  "-vf","fps=30,format=yuv420p","-c:v","libx264","-preset","veryfast","-crf","20","-c:a","aac","-b:a","160k","-af","apad=pad_dur=0.8","-shortest",os.path.join(OUT,"week-headlines-short-2026-10-30.mp4")])
print("done")
