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
 1: dict(kicker="THIS WEEK · 31 OCT–6 NOV 2026", headline="The week in AI", img=None, src="", facts=[
     ("OpenAI introduced", "OPENAI", "GPT-6 Cyber: approved customers only", GREEN),
     ("Apple opened", "APPLE", "Siri AI developer preview in iOS 27.3", CYAN),
     ("Thinking Machines", "INKLING 2", "Small: open weights promised next week", AMBER)]),
 2: dict(kicker="OPENAI · SECURITY", headline="GPT-6 Cyber and the kernel run", img="openai-gpt-6-cyber-2026-11-05.jpg",
     src="OpenAI posts (2–5 Nov) · all figures are OpenAI's own", facts=[
     ("GPT six Cyber", "GPT-6 Cyber", "Finds and validates exploitable vulnerabilities", CYAN, "openai-gpt-6-cyber-2026-11-05.jpg"),
     ("forty-eight point five", "48.5%", "ExploitGym · up from 32.1% for GPT-5.6 Cyber", GREEN, "openai-gpt-6-cyber-2026-11-05.jpg"),
     ("eighty-one", "81 flaws", "High-severity Firefox flaws found with it", AMBER, "openai-gpt-6-cyber-2026-11-05.jpg"),
     ("one thousand seven hundred twenty-four", "1,724 → 948", "Kernel bugs reproduced → privilege-escalation exploits", CYAN, "openai-paths-to-root-2026-11-04.jpg"),
     ("Cathedral", "Security sprint", "With Cathedral · critical bounties more than 4x", GREEN, "openai-security-sprint-cathedral-bug-bounty-2026-11-04.jpg"),
     ("competes with OpenAI", "Disclosure", "Anthropic, maker of Claude, competes with OpenAI", AMBER)]),
 3: dict(kicker="OPENAI · MORE", headline="Images, biology, Abu Dhabi", img="openai-images-2-6-2026-11-04.jpg",
     src="OpenAI posts · Abu Dhabi Media Office (30 Oct–4 Nov)", facts=[
     ("Images two point six", "Images 2.6", "Animated GIFs · 50% faster · Flare + Sunburst", CYAN, "openai-images-2-6-2026-11-04.jpg"),
     ("GPT Rosalind six", "Rosalind-6", "Biology model · approved users only", GREEN),
     ("four agreements", "Abu Dhabi", "4 agreements · ADNOC · Inception42 · no amounts", AMBER, "openai-abu-dhabi-four-agreements-2026-11-02.jpg"),
     ("Dan Driscoll", "Dan Driscoll", "Senior Counselor, National Security Modernization", CYAN, "openai-appoints-dan-driscoll-national-security-modernization-2026-11-04.jpg")]),
 4: dict(kicker="ANTHROPIC", headline="S-1/A, Ultra, watermark", img="anthropic-s1-ipo-filing-nasdaq-ant-2026-10-26.jpg",
     src="Anthropic SEC filing (2 Nov) · pricing page · release notes (31 Oct–3 Nov)", facts=[
     ("amendment", "S-1/A", "Filed 2 Nov · adds Q3 and nine-month results", CYAN, "anthropic-s1-ipo-filing-nasdaq-ant-2026-10-26.jpg"),
     ("still blank", "Price range", "Price range and share count still blank", AMBER),
     ("Ultra at two hundred", "Ultra $200", "No 5-hour limit for verified accounts", GREEN, "anthropic-claude-ultra-plan-no-5-hour-limit-2026-10-31.jpg"),
     ("text watermark", "Text watermark", "Mythos 5 · Opus 4.7 · Sonnet 4.6 · docs conflict", AMBER, "anthropic-claude-text-watermark-older-models-2026-11-03.jpg"),
     ("FlashProve", "FlashProve", "Proves which model made an output · prototype", CYAN, "anthropic-flashprove-provable-inference-2026-11-04.jpg"),
     ("makes Claude, which", "Disclosure", "Anthropic makes Claude, our drafting tool", AMBER)]),
 5: dict(kicker="APPLE", headline="China and Siri AI", img="apple-siri-ai-developer-preview-ios-27-3-2026-11-03.jpg",
     src="Apple newsroom (China) 31 Oct · Apple Developer news 3 Nov", facts=[
     ("reaches users in China in December", "China · Dec", "Apple Intelligence + Alibaba Qwen · iOS 27.3", CYAN, "apple-intelligence-china-alibaba-qwen-2026-10-31.jpg"),
     ("Siri AI is not included", "Not included", "Siri AI is not part of the China launch", GREY, "apple-intelligence-china-alibaba-qwen-2026-10-31.jpg"),
     ("Siri AI developer preview", "Siri AI preview", "Any developer · App Intents · multi-step skills", GREEN, "apple-siri-ai-developer-preview-ios-27-3-2026-11-03.jpg"),
     ("a few months", "In a few months", "Customer shipping · unavailable in the EU for now", AMBER, "apple-siri-ai-developer-preview-ios-27-3-2026-11-03.jpg")]),
 6: dict(kicker="GOOGLE", headline="Omni 1.2, classrooms, chemistry", img="gemini-omni-1-2-flash-2026-11-05.jpg",
     src="Google posts (3–5 Nov) · all figures are Google's own", facts=[
     ("fifteen seconds", "15 s clips", "Gemini Omni 1.2 Flash · was 10 s", CYAN, "gemini-omni-1-2-flash-2026-11-05.jpg"),
     ("seven cents", "$0.07 / s", "720p · 30% below Omni 1.1", GREEN, "gemini-omni-1-2-flash-2026-11-05.jpg"),
     ("K-12", "K-12: off", "Gemini and Search off until admins turn on", AMBER, "google-k12-student-accounts-ai-search-off-by-default-2026-11-03.jpg"),
     ("Cheminformatics", "10,000 scientists", "Antigravity Cheminformatics Skills · 6 months free", CYAN, "google-antigravity-cheminformatics-skills-2026-11-03.jpg"),
     ("competes with Google", "Disclosure", "Anthropic competes with Google", AMBER)]),
 7: dict(kicker="MODELS & OPEN WEIGHTS", headline="Promised and published", img="thinking-machines-inkling-2-small-2026-11-05.jpg",
     src="Thinking Machines · Moonshot · Baidu · Deep Principle — benchmarks are the makers' own", facts=[
     ("Inkling two Small,", "Inkling 2 Small", "594B · 17B active · closed weights for now", CYAN, "thinking-machines-inkling-2-small-2026-11-05.jpg"),
     ("follow next week", "Apache 2.0 · next week", "A plan, not yet a fact", AMBER, "thinking-machines-inkling-2-small-2026-11-05.jpg"),
     ("Kimi K three point one Pro", "Kimi K3.1 Pro", "Weights on Hugging Face · custom license", GREEN, "moonshot-kimi-k3-1-pro-2026-10-23.jpg"),
     ("ERNIE five point five", "ERNIE 5.5 Flash Base", "280B · 14B active · Baidu license", CYAN, "baidu-ernie-5-5-flash-base-2026-11-05.jpg"),
     ("Hydrogen one point oh", "Hydrogen-1.0", "753B · MIT weights · from GLM-5.3", GREEN, "deep-principle-hydrogen-1-0-open-weights-2026-11-04.jpg")]),
 8: dict(kicker="SECURITY & RESEARCH", headline="Kill switch, weights, edits", img="crowdstrike-ai-kill-switch-falcon-guardian-2026-11-03.jpg",
     src="CrowdStrike (3 Nov) · DeepSeek repo · MIT CSAIL (2 Nov) · Krea (3 Nov)", facts=[
     ("AI Kill Switch", "AI Kill Switch", "Falcon Guardian · blocks model access via gateway", CYAN, "crowdstrike-ai-kill-switch-falcon-guardian-2026-11-03.jpg"),
     ("dsh-superagent", "dsh-superagent", "DeepSeek team prototype · MIT · not official", AMBER, "deepseek-dsh-superagent-prototype-mit-2026-11-02.jpg"),
     ("forty-eight point one", "7.9% → 48.1%", "MIT: GPT-6 Astra edited Qwen weights · MATH-500", GREEN, "mit-weight-space-programming-gpt-6-astra-2026-11-02.jpg"),
     ("could not improve Gemma", "Early results", "The approach did not help Gemma", GREY, "mit-weight-space-programming-gpt-6-astra-2026-11-02.jpg"),
     ("eight seconds", "8 s edit", "Krea 3 vs 22.3 s for Nano Banana Pro · own figures", CYAN, "krea-3-technical-report-edit-latency-cost-2026-11-03.jpg")]),
 9: dict(kicker="BUSINESS & CHIPS", headline="Deals, earnings, rounds", img="marvell-to-acquire-lumentum-115-billion-2026-11-02.jpg",
     src="Marvell · AMD · Cohere · fal · Truth Social via archive (2–6 Nov)", facts=[
     ("Marvell said", "$115B", "Marvell–Lumentum · all-stock · close H1 2028", CYAN, "marvell-to-acquire-lumentum-115-billion-2026-11-02.jpg"),
     ("ninety-seven percent", "AMD +97%", "Data Center $8.5B · Q4 guide about $17B", GREEN, "amd-q3-2026-data-center-revenue-97-percent-2026-11-03.jpg"),
     ("Series E targeting", "C$7B target", "Cohere Series E · Schwarz Group · C$4B+ in Canada", AMBER),
     ("fal announced", "fal E + F", "Amounts undisclosed · press reports $1.3B", CYAN, "fal-series-e-f-sequoia-bessemer-nvidia-2026-11-04.jpg"),
     ("Super Intelligence", "Trump post", "No policy, order or rule announced", GREY)]),
 10: dict(kicker="NEXT WEEK", headline="Coming up", img=None, src="", facts=[
     ("Inkling two Small", "Inkling weights", "Apache 2.0 promised after safety testing", CYAN),
     ("price range", "Anthropic IPO", "No price range in the amended filing", AMBER),
     ("Siri AI is a developer preview", "Siri AI", "Customers in a few months · China in Dec", GREEN),
     ("Every article", "deyronlabs.com", "Every article, with sources · subscribe", WHITE),
     ("the voice you are hearing", "Disclosure", "The voice is AI · ElevenLabs", AMBER)]),
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
    d.text((W - 90, 52), "FRIDAY 6 NOV 2026", font=font(SB, 26), fill=GREY + (255,), anchor="ra")
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
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(OUT, "ai-news-this-week-ep-2026-11-06-raw.mp4")])
    raw = os.path.join(OUT, "ai-news-this-week-ep-2026-11-06-raw.mp4")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", os.path.join(OUT, "ai-news-this-week-ep-2026-11-06.mp4")])
    print("done")
