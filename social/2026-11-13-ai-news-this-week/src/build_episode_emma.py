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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_logo

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
 2: dict(kicker="ANTHROPIC · MODELS", headline="Claude Fable 5.2 and Mythos 5.2", img="claude-fable-5-2-2026-11-09.jpg",
     src="Anthropic announcement (9 Nov) · all figures are Anthropic's own", facts=[
     ("Claude Fable five point two and", "Fable 5.2 + Mythos 5.2", "Same underlying model · Fable open to everyone", CYAN),
     ("eight dollars per million input", "$8 / $40", "Per million tokens in / out · Fable 5.1 was $10 / $50", GREEN),
     ("twenty percent below", "−20% price", "And up to 30% faster output", AMBER),
     ("one million tokens", "1M context", "Up to 128K tokens of output", CYAN),
     ("forty-nine point one percent", "49.1%", "FrontierCode 2.0 · Fable 5.1: 32.4% · own numbers", GREEN)]),
 3: dict(kicker="GOOGLE · GEMINI 4", headline="Carbon goes GA, Hydrogen arrives", img="google-gemini-4-carbon-general-availability-2026-11-10.jpg",
     src="Google posts (10 and 12 Nov) · all figures are Google's own", facts=[
     ("Gemini four Carbon became", "Carbon: GA", "Generally available 10 Nov · was limited to defenders", CYAN, "google-gemini-4-carbon-general-availability-2026-11-10.jpg"),
     ("two dollars per million input", "$2 / $10", "Introductory price through 30 Nov", GREEN, "google-gemini-4-carbon-general-availability-2026-11-10.jpg"),
     ("then four dollars", "$4 / $20", "From 1 Dec · Argon still better for most work", AMBER, "google-gemini-4-carbon-general-availability-2026-11-10.jpg"),
     ("Gemini four Hydrogen,", "Hydrogen $1.50 / $7.50", "Flat across a 1M-token context · 12 Nov", CYAN, "google-gemini-4-hydrogen-2026-11-12.jpg"),
     ("fifty-one on the Artificial", "51 vs 50", "Artificial Analysis index · Hydrogen vs Argon", GREEN, "google-gemini-4-hydrogen-2026-11-12.jpg")]),
 4: dict(kicker="ANTHROPIC · IPO", headline="From filing to roadshow", img="anthropic-s1-ipo-filing-nasdaq-ant-2026-10-26.jpg",
     src="Anthropic SEC filings (S-1/A 2 Nov · roadshow 10 Nov) · Reuters", facts=[
     ("sixteen point nine six billion", "$16.96B", "Q3 revenue · amended S-1 filed 2 Nov", CYAN),
     ("eight hundred ninety-five billion", "~$895B", "Committed spend · mostly compute and infrastructure", AMBER),
     ("eight hundred twenty-five million Class A", "825M shares", "Expected $70–78 · Nasdaq: ANT", GREEN),
     ("fifty-eight to sixty-four", "~$58–64B", "Our own arithmetic · before fees", CYAN),
     ("not yet effective", "Not effective", "Price and terms can change · not investment advice", GREY)]),
 5: dict(kicker="NVIDIA", headline="Huang steps down", img="nvidia-ceo-huang-resigns-2026-11-12.jpg",
     src="Nvidia board announcement (12 Nov) · Nvidia statements", facts=[
     ("Jensen Huang has resigned", "Huang resigned", "President, CEO and director · effective immediately", CYAN),
     ("Colette Kress is interim", "Kress: interim CEO", "Chief financial officer steps in", GREEN),
     ("Harvey Jones", "Harvey Jones", "Former Synopsys CEO · board's first chair", AMBER),
     ("The release gives no reason", "No reason given", "We do not repeat unconfirmed press reports", GREY),
     ("seventeenth of November", "Earnings 17 Nov", "Q3 results still scheduled · roadmap unchanged", CYAN)]),
 6: dict(kicker="MODELS & PRICES", headline="Three small and cheap launches", img="meta-muse-ember-2026-11-09.jpg",
     src="Meta (9 Nov) · Alibaba (11 Nov) · Google (11 Nov) · benchmarks are the makers' own", facts=[
     ("Muse Ember", "Muse Ember", "Meta · smallest, most efficient · built for agents", CYAN, "meta-muse-ember-2026-11-09.jpg"),
     ("ten cents per million input", "$0.10 / $0.50", "1M context · weights not stated", GREEN, "meta-muse-ember-2026-11-09.jpg"),
     ("Qwen four Max", "Qwen4-Max preview", "1M context · no price, weights or benchmarks", AMBER, "alibaba-qwen4-max-preview-2026-11-11.jpg"),
     ("twenty-fifth of November", "To 25 Nov", "Token Plan subscribers only", GREY, "alibaba-qwen4-max-preview-2026-11-11.jpg"),
     ("Gemini Decision one", "Decision 1", "Up to 1,000 yes/no answers in one pass · $0.10 in", CYAN, "google-gemini-decisions-api-decision-1-2026-11-11.jpg")]),
 7: dict(kicker="ANTHROPIC · PRODUCTS", headline="Finance, Sheets, Meetings", img="claude-sheets-whiteboards-data-2026-11-10.jpg",
     src="Anthropic announcements (5, 10 and 12 Nov)", facts=[
     ("Personal Finance in Claude", "Personal Finance", "Beta · US · Pro, Max, Ultra", CYAN, "claude-personal-finance-2026-11-05.jpg"),
     ("read-only", "Read-only", "Banks linked via Plaid · Claude cannot move money", GREEN, "claude-personal-finance-2026-11-05.jpg"),
     ("Claude Sheets and Claude Whiteboards", "Sheets + Whiteboards", "Beta · Dashboards GA as Claude Data", AMBER, "claude-sheets-whiteboards-data-2026-11-10.jpg"),
     ("nineteenth of November", "19 Nov", "Claude Data on by default for Enterprise", GREY, "claude-sheets-whiteboards-data-2026-11-10.jpg"),
     ("Claude Meetings", "Claude Meetings", "Beta · Google Meet notes and action items", CYAN, "claude-meetings-beta-2026-11-12.jpg")]),
 8: dict(kicker="OPENAI", headline="Businesses in ChatGPT", img="openai-businesses-in-chatgpt-2026-11-10.jpg",
     src="OpenAI (10 Nov) · Reuters citing Bloomberg", facts=[
     ("Businesses in ChatGPT", "Businesses", "Beta · Business Hub, product feeds, mention tracking", CYAN, "openai-businesses-in-chatgpt-2026-11-10.jpg"),
     ("Business Agent", "Business Agent", "US ecommerce and services · sponsor for ChatGPT ads", GREEN, "openai-businesses-in-chatgpt-2026-11-10.jpg"),
     ("one point two billion weekly", "1.2B weekly", "OpenAI's own user figure", AMBER, "openai-businesses-in-chatgpt-2026-11-10.jpg"),
     ("eleven billion dollars", "$11B", "First part of a round at $1.25T · press report", CYAN, "openai-1-25t-funding-2026-11-06.jpg"),
     ("has not confirmed it", "Unconfirmed", "OpenAI has not confirmed · no investors named", GREY, "openai-1-25t-funding-2026-11-06.jpg")]),
 9: dict(kicker="SECURITY, CHIPS, POLICY", headline="Fireworks, TPUs, S. 5653", img="fireworks-security-incident-update-2026-11-09.jpg",
     src="Fireworks bulletin (9 Nov) · Google (9 Nov) · Truth Social via archive (8 Nov)", facts=[
     ("Fireworks AI", "Fireworks incident", "Dev machines reached 24 Oct · rotate any secrets", CYAN, "fireworks-security-incident-update-2026-11-09.jpg"),
     ("card numbers were not affected", "Cards not affected", "Account and billing data were", GREEN, "fireworks-security-incident-update-2026-11-09.jpg"),
     ("T P U eight t x", "TPU 8tx", "AMD hosts · confidential compute · up to 2x lower latency", AMBER, "google-tpu-8tx-8i-max-2026-11-09.jpg"),
     ("eight i Max", "TPU 8i Max", "Two 8i chips per package · no specs or dates", CYAN, "google-tpu-8tx-8i-max-2026-11-09.jpg"),
     ("S. fifty-six fifty-three", "S. 5653", "Trump post · bill text not checked", GREY, "trump-s5653-data-centers-pay-own-electricity-2026-11-08.jpg")]),
 10: dict(kicker="NEXT WEEK", headline="Coming up", img=None, src="", facts=[
     ("Nvidia reports", "Nvidia results 17 Nov", "Kress as interim CEO · no permanent successor", CYAN),
     ("Inkling two Small", "Inkling 2 Small", "Apache 2.0 weights promised · not confirmed out", AMBER),
     ("Alibaba's Qwen four Max preview closes", "25 and 30 Nov", "Qwen4-Max preview ends · Carbon intro price ends", GREEN)]),
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

def draw_logo(img, x, y):
    """OFFICIAL cube pasted from public/brand/cube-official.png (never drawn with polygons) + wordmark."""
    c = brand_logo.cube(66)
    img.paste(c, (x - 26, y - 33), c)
    ImageDraw.Draw(img).text((x + 34, y - 20), "DEYRON LABS", font=font(XB, 30), fill=WHITE)

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
    draw_logo(img, 90, 70)
    d.text((W - 90, 52), "FRIDAY 13 NOV 2026", font=font(SB, 26), fill=GREY + (255,), anchor="ra")
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
    # end card (last segment only): written disclosure + attribution (rule: never spoken)
    if sid == 10:
        et = LEAD + dur + 0.3
        if t >= et:
            pe = ease((t - et) / 0.5); ea = int(255 * pe)
            d.rounded_rectangle((90, 805, 1830, 965), 18, fill=(20, 28, 56, int(235 * pe)), outline=GREEN + (int(220 * pe),), width=3)
            d.text((960, 855), "AI-generated video and voice \u00b7 We use Claude by Anthropic", font=font(XB, 42), fill=WHITE + (ea,), anchor="mm")
            d.text((960, 922), "Findings are the companies' own. Anthropic, maker of Claude, is covered in two segments and competes with OpenAI and Google.", font=fit(d, "Findings are the companies' own. Anthropic, maker of Claude, is covered in two segments and competes with OpenAI and Google.", SB, 28, 1680), fill=(214, 222, 238, ea), anchor="mm")
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
    total = LEAD + adur + (6.5 if sid == 10 else TAIL); nf = int(total * FPS + 0.999)
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
    # assemble: explosion intro + Emma intro + news + Emma outro (all re-encoded to match)
    def norm(src, dst):
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium",
                               "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", dst])
    intro = os.path.join(OUT, "intro-norm.mp4"); norm(INTRO, intro)
    ei = os.path.join(OUT, "emma-intro-norm.mp4"); norm(os.environ["EMMA_INTRO"], ei)
    eo = os.path.join(OUT, "emma-outro-norm.mp4"); norm(os.environ["EMMA_OUTRO"], eo)
    lst = os.path.join(OUT, "list.txt")
    parts = [intro, ei] + [os.path.join(OUT, f"seg-{i:02d}.mp4") for i in ids] + [eo]
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    raw = os.path.join(OUT, "ai-news-this-week-ep-2026-11-13-emma-raw.mp4")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", raw])
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", os.path.join(OUT, "ai-news-this-week-ep-2026-11-13-emma.mp4")])
    print("done")
