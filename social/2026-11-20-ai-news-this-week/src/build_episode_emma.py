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
 2: dict(kicker="ANTHROPIC · IPO", headline="Anthropic prices its IPO", img="anthropic-s1-ipo-filing-nasdaq-ant-2026-10-26.jpg",
     src="Anthropic announcement (18 Nov) · Nasdaq: ANT · Anthropic makes Claude, which we use", facts=[
     ("eighty-three dollars a share", "$83", "Priced 18 Nov · above the $70–78 range", GREEN),
     ("nine hundred eighty million Class A", "980M shares", "~956M Anthropic · ~24M selling holders", CYAN),
     ("roughly eighty-one billion", "~$81B", "Our own arithmetic · before fees", AMBER),
     ("registration statement effective", "SEC: effective", "Declared effective 18 Nov", GREEN),
     ("not investment advice", "Not advice", "We report only what Anthropic's release says", GREY)]),
 3: dict(kicker="OPENAI · MODELS", headline="GPT-6.2 Astra and Sol", img="openai-gpt-6-2-astra-sol-2026-11-18.jpg",
     src="OpenAI announcement (17 Nov) · all comparisons are OpenAI's own", facts=[
     ("GPT six point two Astra", "GPT-6.2 Astra + Sol", "Released 17 Nov · ChatGPT Work, Codex, API", CYAN, "openai-gpt-6-2-astra-sol-2026-11-18.jpg"),
     ("eight dollars per million input", "$8 / $40", "Astra · 20% below GPT-6 Astra", GREEN, "openai-gpt-6-2-astra-sol-2026-11-18.jpg"),
     ("two dollar and ten dollar", "$2 / $10", "Sol keeps its rates", AMBER, "openai-gpt-6-2-astra-sol-2026-11-18.jpg"),
     ("five point five points above", "+5.5 vs Fable 5.2", "Agents' Last Exam · OpenAI's own", CYAN, "openai-gpt-6-2-astra-sol-2026-11-18.jpg"),
     ("Astra for Law", "Astra for Law", "On request · ChatGPT Enterprise", GREY, "openai-astra-law-6-2-2026-11-18.jpg")]),
 4: dict(kicker="NVIDIA", headline="Record quarter, CEO search", img="nvidia-q3-fy27-results-record-revenue-kress-interim-ceo-2026-11-18.jpg",
     src="Nvidia release and SEC filing (17 Nov) · CBS News · Reuters", facts=[
     ("one hundred fifteen point eight billion", "$115.8B", "Q3 revenue · up 103% year on year", GREEN, "nvidia-q3-fy27-results-record-revenue-kress-interim-ceo-2026-11-18.jpg"),
     ("one hundred thirty billion", "$130B guide", "Q4 · no China data center compute assumed", CYAN, "nvidia-q3-fy27-results-record-revenue-kress-interim-ceo-2026-11-18.jpg"),
     ("interim chief executive Colette Kress", "Kress signs", "Interim CEO · results release", AMBER, "nvidia-q3-fy27-results-record-revenue-kress-interim-ceo-2026-11-18.jpg"),
     ("honored to return", "CBS: Huang", "Would return · chair: no plan to rehire him", CYAN, "nvidia-huang-return-statement-2026-11-17.jpg"),
     ("no longer shipping licensed Hopper", "Hopper to China", "Reuters · stopped · $2.4B sold in the quarter", GREY, "nvidia-huang-return-statement-2026-11-17.jpg")]),
 5: dict(kicker="MODELS", headline="Gemini 4 Neon and Qwen4-Max", img="google-gemini-4-neon-2026-11-18.jpg",
     src="Google (18 Nov) · Alibaba (16 Nov) · all figures are the makers' own", facts=[
     ("Gemini four Neon", "Gemini 4 Neon", "Between Carbon and Hydrogen · 18 Nov", CYAN, "google-gemini-4-neon-2026-11-18.jpg"),
     ("three dollars per million input", "$3 / $15", "1M-token context window", GREEN, "google-gemini-4-neon-2026-11-18.jpg"),
     ("thirty-two percent less per task", "−32% per task", "vs Carbon at the default setting", AMBER, "google-gemini-4-neon-2026-11-18.jpg"),
     ("Qwen four Max", "Qwen4-Max", "Launched 16 Nov · 1M context", CYAN, "alibaba-qwen4-max-launch-2026-11-16.jpg"),
     ("one dollar sixty-seven", "$4.43 → $1.67", "Cost per task on Alibaba's own test", GREEN, "alibaba-qwen4-max-launch-2026-11-16.jpg")]),
 6: dict(kicker="OPEN WEIGHTS · MICROSOFT", headline="Hy4 flash, Clairic, MAI", img="tencent-hy4-flash-open-weights-2026-11-20.jpg",
     src="Tencent model card · Cloudflare · Microsoft AI (17 Nov) · claims are the makers' own", facts=[
     ("Hy four flash", "Hy4 flash", "Tencent · 220B total · 12B active · 1M context", CYAN, "tencent-hy4-flash-open-weights-2026-11-20.jpg"),
     ("under its own license", "Custom license", "Tencent Hy License · not Apache", AMBER, "tencent-hy4-flash-open-weights-2026-11-20.jpg"),
     ("Apache two point oh", "Clairic", "Cloudflare · Apache 2.0 · $0.10 per M input", GREEN, "cloudflare-clairic-open-weight-2026-11-18.jpg"),
     ("seven new M A I models", "7 MAI models", "Microsoft · Ignite · 17 Nov", CYAN, "microsoft-ignite-mai-seven-models-2026-11-18.jpg"),
     ("ninety-eight percent", "98% at ~40%", "MAI Code 2 vs GPT-6.1 Sol · Microsoft's own", AMBER, "microsoft-ignite-mai-seven-models-2026-11-18.jpg")]),
 7: dict(kicker="AGENTS & MONEY", headline="Agents learn to pay", img="openai-chatgpt-wallet-2026-11-13.jpg",
     src="OpenAI · Google · Replit · Sierra (12–17 Nov) · all claims are the companies' own", facts=[
     ("ChatGPT Wallet", "ChatGPT Wallet", "Agents pay without seeing the card · US Pro", CYAN, "openai-chatgpt-wallet-2026-11-13.jpg"),
     ("Google connected Google Wallet", "Google Wallet + Gemini", "US · read-only, cannot move money", GREEN, "google-wallet-gemini-personal-finance-2026-11-13.jpg"),
     ("free in six countries", "Tasks: 6 countries", "Calls, texts, capped purchases in the US", AMBER, "google-tasks-in-gemini-free-six-countries-2026-11-18.jpg"),
     ("run Google Ads campaigns", "Replit agent", "Buys supplies · runs Google Ads", CYAN, "replit-agent-commerce-ads-2026-11-12.jpg"),
     ("more than one hundred organizations", "Sierra Poppy 1.0", "100+ organizations back it · Sierra's claim", GREY, "sierra-personal-agent-protocol-1-0-2026-11-13.jpg")]),
 8: dict(kicker="TOOLS & INFRASTRUCTURE", headline="Routing, search fees, Rubin", img="perplexity-orchestrator-api-and-multiagent-2026-11-18.jpg",
     src="Perplexity (17 Nov) · DeepSeek docs · TechNode · Nvidia blog (19 Nov)", facts=[
     ("Orchestrator", "Orchestrator", "One API · 85+ models", CYAN, "perplexity-orchestrator-api-and-multiagent-2026-11-18.jpg"),
     ("Multiagent", "Multiagent", "Perplexity Computer · Max subscribers", GREEN, "perplexity-orchestrator-api-and-multiagent-2026-11-18.jpg"),
     ("no longer carry a separate fee", "No search fee", "DeepSeek · model-run searches · tokens only", AMBER, "deepseek-web-search-fee-removal-2026-11-20.jpg"),
     ("took effect on the eighteenth", "18 Nov", "TechNode's date · not in DeepSeek's change log", GREY, "deepseek-web-search-fee-removal-2026-11-20.jpg"),
     ("Vera Rubin N V L seventy-two", "Rubin in Azure", "Nvidia's statement · 10,240 GPUs in MLPerf", CYAN, "nvidia-microsoft-ignite-azure-vera-rubin-2026-11-20.jpg")]),
 9: dict(kicker="SECURITY, LAW, CHIPS", headline="Lawsuit, swap, Signal, rules", img="openai-california-lawsuit-hugging-face-hack-2026-11-17.jpg",
     src="California AG complaint via NPR · Prime Intellect advisory · Reuters · BIS · CNBC", facts=[
     ("California's attorney general", "California v. OpenAI", "State's allegations · filed 16 Nov", CYAN, "openai-california-lawsuit-hugging-face-hack-2026-11-17.jpg"),
     ("from the eighth to the tenth of November", "Prime Intellect", "Endpoint swapped ~53 hours · refusals removed", AMBER, "prime-intellect-deepseek-v4-1-flash-substitution-advisory-2026-11-20.jpg"),
     ("Signal messages", "Meta Muse", "Reuters: read Signal in tests · Meta: isolated", GREEN, "meta-muse-signal-messages-2026-11-18.jpg"),
     ("Bureau of Industry and Security issued a rule", "BIS remote-access rule", "Thresholds and countries not stated", CYAN, "bis-remote-access-super-intelligence-ifr-2026-11-17.jpg"),
     ("eight hundred seventy-nine thousand", "879,000+ chips", "Approved for Chinese firms to May · CNBC", GREY, "commerce-879k-ai-chips-china-2026-11-20.jpg")]),
 10: dict(kicker="NEXT WEEK", headline="Coming up", img=None, src="", facts=[
     ("OpenAI opens fifty thousand", "23 Nov", "50,000 academic researcher grants open", CYAN),
     ("introductory price ends", "30 Nov", "Gemini 4 Carbon intro price ends", AMBER),
     ("Jensen Huang is due before the House", "1 Dec", "Huang before the House · per CBS", GREEN)]),
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
    d.text((W - 90, 52), "FRIDAY 20 NOV 2026", font=font(SB, 26), fill=GREY + (255,), anchor="ra")
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
            d.text((960, 922), "Findings are the companies' own. Anthropic, maker of Claude, is covered here and competes with OpenAI and Google.", font=fit(d, "Findings are the companies' own. Anthropic, maker of Claude, is covered here and competes with OpenAI and Google.", SB, 28, 1680), fill=(214, 222, 238, ea), anchor="mm")
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
    raw = os.path.join(OUT, "ai-news-this-week-ep-2026-11-20-emma-raw.mp4")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", raw])
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", os.path.join(OUT, "ai-news-this-week-ep-2026-11-20-emma.mp4")])
    print("done")
