#!/usr/bin/env python3
"""Renders the long episode "AI News This Week" (1920x1080, 30 fps) from seg-NN.mp3 files.

Structure: intro (ai-news-this-week-intro.mp4, own sound) + one scene per voice segment.
Each scene: kicker chip, headline, fact cards that appear at cue words in the voiceover,
article image on the right, source line, amber ticker. No burned subtitles (long-video rule).

Usage:
  MP3_DIR=/dir/with/seg-NN.mp3 INTRO=/path/ai-news-this-week-intro.mp4 OUT_DIR=/out \
  python3 -I build_episode.py            # renders all segments, then assembles episode.mp4
  ONLY=3 ... python3 -I build_episode.py  # render just one segment (test)
Needs: numpy, Pillow, ffmpeg, Inter fonts, article images in IMG_DIR (repo public/images/news).
"""
import os, sys, subprocess, json
import numpy as np
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont

MP3 = os.environ["MP3_DIR"]; OUT = os.environ["OUT_DIR"]; INTRO = os.environ["INTRO"]
IMG_DIR = os.environ.get("IMG_DIR", "/home/claude/deyronlabs.github.io/public/images/news")
VO = os.environ.get("VO", os.path.join(os.path.dirname(__file__), "..", "voiceover.txt"))
os.makedirs(OUT, exist_ok=True)
W, H, FPS = 1920, 1080, 30
LEAD, TAIL = 0.25, 0.45
FD = "/usr/share/fonts/opentype/inter/"
XB, BD, SB = FD + "Inter-ExtraBold.otf", FD + "Inter-Bold.otf", FD + "Inter-SemiBold.otf"
NAVY, CYAN, AMBER = (10, 14, 30), (34, 211, 238), (245, 158, 11)
GREEN, WHITE, GREY = (34, 197, 94), (255, 255, 255), (178, 190, 214)
_F = {}
def font(p, s):
    if (p, s) not in _F: _F[(p, s)] = ImageFont.truetype(p, s)
    return _F[(p, s)]
def clamp(x): return min(max(x, 0.0), 1.0)
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3

IMG = lambda n: os.path.join(IMG_DIR, n)
# kicker, headline, image, facts [(cue, value, label, colour)], source
S = {
 1: dict(kicker="THIS WEEK · 6–16 OCT 2026", headline="The week in AI", img=None, src="", facts=[
     ("Meta shipped", "META", "Two model launches in four days", CYAN),
     ("Google made", "GOOGLE", "Gemini 4 Argon is GA — price doubles 1 Dec", AMBER),
     ("Anthropic says", "ANTHROPIC", "Says it cut distillation harvesting 90–99%", GREEN)]),
 2: dict(kicker="META · MUSE WONDER", headline="Meta's closed frontier model", img="meta-muse-wonder-frontier-models-2026-10-12.jpg",
     src="Meta blog post · VentureBeat · Artificial Analysis", facts=[
     ("released Muse Wonder", "2 models", "Muse Wonder + Wonder Full · closed · 1M context", CYAN),
     ("Meta published no price", "No price", "Published by Meta", AMBER),
     ("Third parties report", "$4 / $20", "per 1M tokens in / out (reported)", CYAN),
     ("scores fifty-two", "52", "Artificial Analysis Intelligence Index", GREEN)]),
 3: dict(kicker="META · MUSE SPARK OPEN", headline="816B open weights", img="meta-muse-spark-open-816b-open-weight-model-2026-10-15.jpg",
     src="Meta announcement · Hugging Face model card", facts=[
     ("Eight hundred", "816B", "parameters · 42B active", CYAN),
     ("one million token", "1M", "token context", CYAN),
     ("a company above", "$20M", "revenue → separate deal to sell as a service", AMBER),
     ("Kimi K3", "44 / 45 vs 39", "Kimi K3 / GLM 5.3 vs Muse Spark Open (AA index)", GREEN),
     ("seven hundred", "~700 GB", "GPU memory for the smallest official build", AMBER)]),
 4: dict(kicker="GOOGLE · GEMINI 4 ARGON", headline="Now generally available", img="google-gemini-4-argon-general-availability-2026-10-14.jpg",
     src="Google API changelog · pricing page · model page", facts=[
     ("reached general", "13 Oct", "General availability", CYAN),
     ("Two dollars input", "$2 / $10", "per 1M tokens in / out, until 30 Nov", GREEN),
     ("From the first", "$4 / $20", "from 1 Dec — double the cost", AMBER),
     ("benchmarks are mixed", "Mixed", "Behind on FrontierSWE v2 and Terminal-bench 4.0", GREY)]),
 5: dict(kicker="xAI · GROK VOICE 3.0", headline="A new voice-agent model", img="xai-grok-voice-3-speech-to-speech-model-2026-10-15.jpg",
     src="xAI announcement (14 Oct)", facts=[
     ("eight cents", "$0.08/min", "unchanged price", GREEN),
     ("Developers calling", "Auto-upgrade", "grok-voice-latest switched by itself", AMBER),
     ("tau-Voice", "74.5 vs 71.6", "tau-Voice: GPT-Live-1 vs Grok Voice 3.0", CYAN),
     ("under one second", "< 1 s", "latency claim, no exact figure", GREY)]),
 6: dict(kicker="ANTHROPIC · DISTILLATION", headline="New anti-distillation defenses", img="anthropic-distillation-defenses-90-99-percent-2026-10-12.jpg",
     src="Anthropic research post (12 Oct)", facts=[
     ("A disclosure", "Disclosure", "Anthropic makes Claude, our drafting tool", AMBER),
     ("ninety to ninety-nine", "90–99%", "less data harvested (Anthropic's claim)", CYAN),
     ("tens of thousands", "10,000s", "accounts banned", GREEN),
     ("two Chinese labs", "2 labs accused", "Zhipu · Moonshot · no reply seen", AMBER),
     ("no outside party", "Unconfirmed", "no independent verification", GREY)]),
 7: dict(kicker="ANTHROPIC · RED TEAM", headline="Can a small AI copy itself?", img="anthropic-small-models-self-replication-iot-devices-2026-10-12.jpg",
     src="Anthropic Frontier Red Team (12 Oct)", facts=[
     ("copy itself", "Research", "small models on cheap IoT devices", CYAN),
     ("all eight", "8 / 8 nodes", "emulated Android devices · 4 of 5 trials", AMBER),
     ("upper bound", "Upper bound", "deliberately trivial entry point", GREY),
     ("boring defenses", "Defenses", "monitoring · quarantine · better default security", GREEN)]),
 8: dict(kicker="OPEN MODELS", headline="Three open releases", img="liquid-ai-lfm2-5-24b-a2b-open-weight-agent-model-2026-10-13.jpg",
     src="Liquid AI · Mistral · Xiaomi / Hugging Face — all benchmarks are the labs' own", facts=[
     ("Liquid AI released", "LFM2.5", "24B · ~2B active · 184 tok/s on Apple M5 Max",  CYAN, "liquid-ai-lfm2-5-24b-a2b-open-weight-agent-model-2026-10-13.jpg"),
     ("Mistral introduced", "Timestral", "5M–209M parameters · forecasts time series", AMBER, "mistral-timestral-time-series-forecasting-models-2026-10-15.jpg"),
     ("Xiaomi's MiMo", "MiMo V2.6 Pro", "1T parameters · MIT license · AA index 46", GREEN, "xiaomi-mimo-v2-6-2026-09-22.jpg")]),
 9: dict(kicker="CHINA · AI & JOBS", headline="China's AI employment plan", img="china-human-resources-ministry-ai-employment-initiative-2026-10-12.jpg",
     src="Xinhua report (10 Oct)", facts=[
     ("Ministry of Human", "MOHRSS", "Ministry of Human Resources and Social Security", CYAN),
     ("more than two hundred", "200+", "national occupational standards by 2030", GREEN),
     ("eleven new", "11", "new occupations announced in 2026", AMBER),
     ("statement of plans", "Plans only", "no budget or timetable yet", GREY)]),
 10: dict(kicker="NVIDIA · VERA RUBIN", headline="NVIDIA opens its rack designs", img="nvidia-opens-vera-rubin-designs-ocp-2026-2026-10-12.jpg",
     src="NVIDIA blog post (12 Oct)", facts=[
     ("Open Compute Project", "OCP summit", "12 Oct · parts of Vera Rubin opened", CYAN),
     ("two hundred fifty", "250 kW", "per rack supported (MGX 1.2)", GREEN),
     ("no release dates", "No dates", "no licenses · several partner items are plans", AMBER),
     ("AI Infrastructure series", "Watch", "our AI Infrastructure series", GREY)]),
 11: dict(kicker="NEXT WEEK", headline="Coming up", img=None, src="", facts=[
     ("NVIDIA's keynote", "Wed 21 Oct", "NVIDIA keynote at GTC Berlin", CYAN),
     ("Mistral has promised", "End of Oct", "Mistral Large 4 weights (promised)", AMBER),
     ("AI Infrastructure episode", "Wed 21 Oct · 20:00", "AI Infrastructure #2 (Romania time)", GREEN),
     ("Every article", "deyronlabs.com", "Every article, with sources · subscribe", WHITE)]),
}

def load_texts():
    t = {}
    for line in open(VO, encoding="utf-8"):
        if line.startswith("seg-"):
            k, v = line.split(":", 1); t[int(k[4:])] = v.strip()
    return t
TEXT = load_texts()

# ---------------------------------------------------------------- static layers
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
rr = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2)
BGA = np.array(NAVY, np.float32)[None, None, :] * np.clip(1.45 - 1.7 * rr, 0.35, 1.45)[..., None]
BGA[..., 2] += 14 * np.clip(0.6 - rr * 1.2, 0, 1)
BGA[(yy % 60 < 2) & (xx % 60 < 2)] += 22          # dot grid
BASE = Image.fromarray(np.clip(BGA, 0, 255).astype(np.uint8))

def draw_logo(d, x, y):
    a = 26
    d.polygon([(x, y - a), (x + a * .87, y - a / 2), (x, y), (x - a * .87, y - a / 2)], fill=(134, 239, 172))
    d.polygon([(x - a * .87, y - a / 2), (x, y), (x, y + a), (x - a * .87, y + a / 2)], fill=GREEN)
    d.polygon([(x + a * .87, y - a / 2), (x, y), (x, y + a), (x + a * .87, y + a / 2)], fill=(21, 128, 61))
    d.text((x + 44, y - 22), "DEYRON LABS", font=font(XB, 30), fill=WHITE)

def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def fit(d, text, path, size, maxw):
    while size > 28 and d.textlength(text, font=font(path, size)) > maxw: size -= 2
    return font(path, size)

TICK_ITEMS = ["DEYRON LABS", "AI NEWS THIS WEEK", "GLOBAL AI, EVERY FRIDAY"]
_ti = Image.new("RGB", (4, 4)); _td = ImageDraw.Draw(_ti)
GAP = 70
TPOS = []; _x = 0
for it in TICK_ITEMS:
    TPOS.append((_x, it)); _x += int(_td.textlength(it, font=font(XB, 36))) + GAP
TW = _x

def render_frame(sid, t, dur, cues, imgs):
    sc = S[sid]
    img = BASE.copy(); d = ImageDraw.Draw(img, "RGBA")
    fade = ease(t / 0.3)
    # header
    draw_logo(d, 90, 70)
    d.text((W - 90, 52), "FRIDAY 16 OCT 2026", font=font(SB, 26), fill=GREY + (255,), anchor="ra")
    # kicker + headline
    k = ease((t - 0.1) / 0.4)
    kf = font(BD, 28); kw = d.textlength(sc["kicker"], font=kf) + 44
    kx = 90 - (1 - k) * 60
    d.rounded_rectangle((kx, 150, kx + kw, 200), 10, fill=CYAN + (int(255 * k),))
    d.text((kx + 22, 175), sc["kicker"], font=kf, fill=NAVY + (int(255 * k),), anchor="lm")
    hf = fit(d, sc["headline"], XB, 84, 880 if sc["img"] else 1700)
    h = ease((t - 0.2) / 0.5)
    d.text((90 - (1 - h) * 80, 222), sc["headline"], font=hf, fill=WHITE + (int(255 * h),))
    # fact cards
    n = len(sc["facts"]); lead = sc["img"] is not None
    top, ch, gap = (350, 104, 12) if lead else (380, 118, 22)
    if n <= 4 and lead: top, ch, gap = 360, 118, 16
    cw = 880 if lead else 1740
    cur_img = sc["img"]
    for i, f in enumerate(sc["facts"]):
        st = cues[i]
        if t < st: continue
        p = ease((t - st) / 0.45)
        if len(f) > 4 and p > 0: cur_img = f[4]
        col = f[3]; y = top + i * (ch + gap); x = 90 + (1 - p) * 140; a = int(255 * p)
        d.rounded_rectangle((x, y, x + cw, y + ch), 16, fill=(20, 28, 56, int(235 * p)), outline=col + (int(200 * p),), width=3)
        d.rectangle((x, y + 14, x + 9, y + ch - 14), fill=col + (a,))
        glow = clamp(1 - (t - st) / 0.7)
        if glow > 0: d.rounded_rectangle((x - 3, y - 3, x + cw + 3, y + ch + 3), 18, outline=WHITE + (int(180 * glow),), width=3)
        vw = 380 if lead else 620
        d.text((x + 34, y + ch / 2), f[1], font=fit(d, f[1], XB, 58, vw), fill=col + (a,), anchor="lm")
        lf = font(SB, 28 if lead else 34)
        for j, ln in enumerate(wrap(d, f[2], lf, cw - vw - 90)[:3]):
            ly = y + ch / 2 + (j - (len(wrap(d, f[2], lf, cw - vw - 90)[:3]) - 1) / 2) * 34
            d.text((x + vw + 50, ly), ln, font=lf, fill=(222, 230, 246, a), anchor="lm")
    # image + source
    if lead and cur_img:
        pi = ease((t - 0.3) / 0.5)
        im = imgs[cur_img]
        ix, iy = 1030 - (1 - pi) * 100, 215
        d.rounded_rectangle((ix - 6, iy - 6, ix + 806, iy + 458), 16, fill=CYAN + (int(255 * pi),))
        mask = Image.new("L", im.size, int(255 * pi))
        img.paste(im, (int(ix), int(iy)), mask)
        d.text((1040, 700), "SOURCES", font=font(BD, 22), fill=AMBER + (int(255 * pi),))
        for j, ln in enumerate(wrap(d, sc["src"], font(SB, 28), 800)[:3]):
            d.text((1040, 735 + j * 34), ln, font=font(SB, 28), fill=(222, 230, 246, int(255 * pi)))
    # ticker
    d.rectangle((0, 990, W, H), fill=AMBER + (255,))
    off = int(t * 140 + sid * 311) % TW
    k0 = -1
    while k0 * TW - off < W:
        for px, it in TPOS:
            x = k0 * TW + px - off
            if -700 < x < W:
                d.text((x, 1035), it, font=font(XB, 36), fill=NAVY + (255,), anchor="lm")
                d.ellipse((x + int(d.textlength(it, font=font(XB, 36))) + GAP // 2 - 6, 1029, x + int(d.textlength(it, font=font(XB, 36))) + GAP // 2 + 6, 1041), fill=NAVY + (255,))
        k0 += 1
    if fade < 1:
        d.rectangle((0, 0, W, H), fill=NAVY + (int(255 * (1 - fade)),))
    return img

def cue_times(sid, dur):
    text = TEXT[sid]; out = []
    for f in S[sid]["facts"]:
        pos = text.find(f[0])
        if pos < 0: print("CUE NOT FOUND", sid, f[0], file=sys.stderr); pos = 0
        out.append(LEAD + max(0.4, dur * pos / len(text) - 0.15))
    return out

def render_segment(sid):
    mp3 = os.path.join(MP3, f"seg-{sid:02d}.mp3")
    adur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp3]))
    total = LEAD + adur + TAIL; nf = int(total * FPS + 0.999)
    sc = S[sid]; imgs = {}
    names = ([sc["img"]] if sc["img"] else []) + [f[4] for f in sc["facts"] if len(f) > 4]
    for nme in names: imgs[nme] = Image.open(IMG(nme)).convert("RGB").resize((800, 450), Image.LANCZOS)
    cues = cue_times(sid, adur)
    vid = os.path.join(OUT, f"seg-{sid:02d}.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", mp3, "-filter_complex", f"[1:a]adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad=whole_dur={total:.3f},aresample=48000[a]",
           "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-ac", "2", "-t", f"{total:.3f}", vid]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nf):
        p.stdin.write(render_frame(sid, i / FPS, adur, cues, imgs).tobytes())
    p.stdin.close(); p.wait()
    return sid, total

if __name__ == "__main__":
    only = os.environ.get("ONLY")
    ids = [int(only)] if only else sorted(S)
    with Pool(int(os.environ.get("PROCS", "4"))) as pool:
        res = dict(pool.map(render_segment, ids))
    print(res)
    if only: sys.exit(0)
    # assemble: intro (re-encoded to match) + segments
    intro = os.path.join(OUT, "intro-norm.mp4")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", INTRO, "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium",
                           "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", intro])
    lst = os.path.join(OUT, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in [intro] + [os.path.join(OUT, f"seg-{i:02d}.mp4") for i in ids]))
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(OUT, "ai-news-this-week-ep-2026-10-16.mp4")])
    print("done")
