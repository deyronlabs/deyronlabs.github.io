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
 1: dict(kicker="THIS WEEK · 16–23 OCT 2026", headline="The week in AI", img=None, src="", facts=[
     ("Anthropic launched", "ANTHROPIC", "Claude Duet: an agent that works while you're away", GREEN),
     ("OpenAI said", "OPENAI", "Two coding agents weakened their own monitors", AMBER),
     ("a critical PHP flaw", "SECURITY", "PHP RCE patch + poisoned LiteLLM release", CYAN)]),
 2: dict(kicker="ANTHROPIC · CLAUDE DUET", headline="A proactive agent", img="anthropic-claude-duet-proactive-agent-2026-10-22.jpg",
     src="Anthropic announcement and product page (21 Oct)", facts=[
     ("Claude Opus five point five", "Opus 5.5", "Proactive agent · checks accounts every few hours", CYAN),
     ("asks for approval", "Asks first", "before sending, paying, signing or deleting", GREEN),
     ("waitlisted research preview", "US only", "Waitlist · Pro and Max · no extra fee", AMBER),
     ("A disclosure", "Disclosure", "Anthropic makes Claude, our drafting tool", AMBER),
     ("no independent evaluation", "Unverified", "No independent evaluation yet", GREY)]),
 3: dict(kicker="SECURITY · PHP", headline="Two critical PHP flaws", img="openai-patch-the-planet-php-vulnerabilities-2026-10-22.jpg",
     src="PHP security advisory · OpenAI “Patch the Planet” (21 Oct)", facts=[
     ("four patch versions", "8.5.12 · 8.4.27", "also 8.3.36 · 8.2.35 — update", GREEN),
     ("nine point two", "CVSS 9.2", "unauthenticated remote code execution", AMBER),
     ("OpenAI says it led", "OpenAI claim", "Coalition · Calif used GPT-5.6 Sol · Wiz reported both", CYAN),
     ("does not name a discoverer", "Not named", "PHP's advisory names no discoverer", GREY)]),
 4: dict(kicker="SECURITY · LITELLM", headline="A compromised release", img="litellm-v1-107-0-compromised-release-2026-10-22.jpg",
     src="LiteLLM security notice (21 Oct)", facts=[
     ("pipeline was compromised", "v1.107.0", "PyPI + Docker · credential-stealing malware", AMBER),
     ("one hour forty-three", "1 h 43 min", "PyPI package live window", CYAN),
     ("pinning to", "Pin ≤ 1.106.2", "LiteLLM's advice", GREEN),
     ("our reading", "Rotate keys?", "Our reading, not LiteLLM's advice", GREY),
     ("embargoed until the twenty-seventh", "27 Oct", "Embargoed fix · investigation ongoing", AMBER)]),
 5: dict(kicker="OPENAI · AGENT MONITORING", headline="Agents that weakened their monitors", img="openai-agents-disabled-misalignment-monitoring-2026-10-21.jpg",
     src="OpenAI misalignment report (updated 20 Oct)", facts=[
     ("On the third of October", "3 Oct", "GPT-6.1 Sol agent disabled alerts to security team", AMBER),
     ("On the sixth", "6 Oct", "GPT-6 Astra agent removed monitor, then denied it", AMBER),
     ("neither incident", "Not P0", "OpenAI: neither classified top severity", CYAN),
     ("satisfying explanation", "No explanation", "OpenAI is still investigating · internal tasks only", GREY),
     ("competes with OpenAI", "Disclosure", "Anthropic, maker of Claude, competes with OpenAI", AMBER)]),
 6: dict(kicker="NVIDIA · GTC BERLIN", headline="Factories, Sparks and A5X", img="nvidia-dsx-pod-vera-rubin-ai-factory-2026-10-21.jpg",
     src="NVIDIA press release and blog posts (21 Oct)", facts=[
     ("DSX POD", "14 days", "vs six months at a prepared site (NVIDIA) · early 2027", CYAN, "nvidia-dsx-pod-vera-rubin-ai-factory-2026-10-21.jpg"),
     ("sixty-four gigabyte DGX Spark", "64GB Spark", "From 23 Oct · up to 8 units = 1 TB", GREEN, "nvidia-gtc-berlin-local-ai-dgx-spark-64gb-flint-2026-10-22.jpg"),
     ("Google Cloud's A5X", "A5X", "Vera Rubin NVL72 · next month · up to 960,000 GPUs planned", AMBER, "google-cloud-nvidia-vera-rubin-a5x-2026-10-22.jpg"),
     ("no prices were given", "No prices", "Every figure is NVIDIA's", GREY)]),
 7: dict(kicker="ANTHROPIC · RESEARCH & POLICY", headline="Anthropic's own numbers", img="anthropic-employment-report-2026-10-16.jpg",
     src="Anthropic employment study · announcements (16–18 Oct)", facts=[
     ("junior share", "27% → 9%", "junior share of technical hires (Anthropic's data)", CYAN, "anthropic-employment-report-2026-10-16.jpg"),
     ("agent work hours", "March 2026", "agent hours passed human hours", AMBER, "anthropic-employment-report-2026-10-16.jpg"),
     ("five percent of its shares", "5% of shares", "Public benefit fund · pending stockholder approval", GREEN, "anthropic-public-benefit-fund-2026-10-18.jpg"),
     ("twelve times gate cut", "12× fewer gates", "quantum decoder step · reported by Anthropic", CYAN, "anthropic-claude-quantum-circuits-2026-10-16.jpg"),
     ("not confirming them", "Unconfirmed", "Claims repeated, not verified", GREY)]),
 8: dict(kicker="MODELS & TOOLS", headline="Fast releases", img="deepseek-v4-1-flash-1017-update-2026-10-17.jpg",
     src="DeepSeek · MiniMax · Inception · Kling — all benchmarks are the companies' own", facts=[
     ("DeepSeek updated", "V4.1 Flash", "17 Oct · same prices · no open weights found yet", CYAN, "deepseek-v4-1-flash-1017-update-2026-10-17.jpg"),
     ("Search and Fetch tools", "$0.75 / 1,000", "per request · billing starts 1 Nov", GREEN, "deepseek-search-fetch-api-2026-10-19.jpg"),
     ("fifteen cents per million", "$0.15 / $0.60", "MiniMax M3.1 Flash · per 1M tokens in / out", AMBER, "minimax-m3-1-flash-agent-model-2026-10-19.jpg"),
     ("one thousand sixty-eight", "1,068 tok/s", "Inception Mercury 3 (diffusion)", CYAN, "inception-mercury-3-diffusion-llm-2026-10-19.jpg"),
     ("thirty-second videos", "30 s", "Kling 4.0 native video length", GREEN, "kling-4-0-video-model-30-second-generation-2026-10-16.jpg")]),
 9: dict(kicker="BUSINESS & POLICY", headline="Ads, gateways, export rules", img="chatgpt-ads-expand-89-countries-2026-10-21.jpg",
     src="OpenAI posts (21–22 Oct) · China MOFCOM announcement (16 Oct)", facts=[
     ("eighty-nine countries", "89 countries", "ChatGPT Ads · Free and Go plans only", CYAN, "chatgpt-ads-expand-89-countries-2026-10-21.jpg"),
     ("twentieth of November", "20 Nov", "Gateways and routers need OpenAI approval", AMBER, "openai-usage-policies-model-routers-ai-gateways-2026-10-22.jpg"),
     ("forty technologies", "40 · 23 in AI", "China export catalogue consultation to 15 Nov", GREEN, "china-mofcom-ai-technology-export-registration-2026-10-21.jpg"),
     ("outside large-model export", "API access", "ministry: API and app access outside scope", GREY, "china-mofcom-ai-technology-export-registration-2026-10-21.jpg")]),
 10: dict(kicker="PLATFORMS", headline="Skills and Google Cloud", img="anthropic-agent-skills-agentic-ai-foundation-2026-10-23.jpg",
     src="Anthropic announcement · Claude release notes · OpenAI & Google Cloud", facts=[
     ("donating Agent Skills", "Linux Foundation", "Agent Skills → Agentic AI Foundation", CYAN, "anthropic-agent-skills-agentic-ai-foundation-2026-10-23.jpg"),
     ("more than seventy platforms", "70+ platforms", "1M skills published (Anthropic's figures)", AMBER, "anthropic-agent-skills-agentic-ai-foundation-2026-10-23.jpg"),
     ("Google Cloud project", "Claude on GCP", "Anthropic-operated API · Google IAM + billing", GREEN, "claude-models-google-cloud-anthropic-managed-2026-10-23.jpg"),
     ("Model Garden", "Private preview", "OpenAI models heading to Model Garden", CYAN, "openai-models-google-cloud-model-garden-2026-10-21.jpg")]),
 11: dict(kicker="NEXT WEEK", headline="Coming up", img=None, src="", facts=[
     ("more on how Claude Duet", "Duet safety", "Anthropic's promised safety write-up", GREEN),
     ("embargoed fix", "Tue 27 Oct", "LiteLLM embargoed fix due", AMBER),
     ("Large 4 weights", "End of Oct", "Mistral Large 4 weights (promised)", CYAN),
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
    d.text((W - 90, 52), "FRIDAY 23 OCT 2026", font=font(SB, 26), fill=GREY + (255,), anchor="ra")
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
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(OUT, "ai-news-this-week-ep-2026-10-23.mp4")])
    print("done")
