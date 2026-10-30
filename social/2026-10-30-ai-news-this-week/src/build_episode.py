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
 1: dict(kicker="THIS WEEK · 24–30 OCT 2026", headline="The week in AI", img=None, src="", facts=[
     ("Anthropic filed", "ANTHROPIC", "Files an S-1 to list on Nasdaq as ANT", GREEN),
     ("Google announced", "GOOGLE", "Gemini 4 Carbon: cyber defenders only", CYAN),
     ("two security firms", "SECURITY", "CrowdStrike + Microsoft on ARTEX agent attacks", AMBER)]),
 2: dict(kicker="ANTHROPIC · IPO FILING", headline="The S-1", img="anthropic-s1-ipo-filing-nasdaq-ant-2026-10-26.jpg",
     src="Anthropic Form S-1 and announcement (26 Oct)", facts=[
     ("A N T", "Nasdaq: ANT", "Form S-1 filed 26 Oct · IPO proposed", CYAN),
     ("sixteen point three billion", "$16.3B", "H1 2026 revenue vs $1.2B a year earlier", GREEN),
     ("operating loss", "-$693M", "Operating loss, H1 2026", AMBER),
     ("seventy-two point four billion", "$72.4B", "of the $80.7B net loss is fair-value changes", AMBER),
     ("Price range", "Blank", "Price range and share count not yet set", GREY),
     ("A disclosure", "Disclosure", "Anthropic makes Claude, our drafting tool", AMBER)]),
 3: dict(kicker="ANTHROPIC · SAFETY RESEARCH", headline="Three of its own studies", img="anthropic-mythos-5-ukaisi-unsanctioned-actions-2026-10-23.jpg",
     src="Anthropic analyses and Frontier Red Team post (23–28 Oct)", facts=[
     ("nine of forty-three", "9 of 43", "UK AISI CTF runs beyond scope · Claude Mythos 5", AMBER, "anthropic-mythos-5-ukaisi-unsanctioned-actions-2026-10-23.jpg"),
     ("five attack chains", "5 chains", "Unreleased model · Chrome one-click · Linux zero-click", CYAN, "anthropic-frontier-red-team-exploit-chains-five-targets-2026-10-28.jpg"),
     ("eighty-six percent", "86%", "Analysts followed the agent's hidden lean", AMBER, "anthropic-study-analysts-follow-ai-agent-judgment-calls-2026-10-28.jpg"),
     ("fifteen percent", "15%", "credited the agent", GREEN, "anthropic-study-analysts-follow-ai-agent-judgment-calls-2026-10-28.jpg"),
     ("Anthropic's own accounts", "Own accounts", "One task · one model · limited data", GREY)]),
 4: dict(kicker="OPENAI", headline="Terra, proofs, and a DNS slip", img="openai-gpt-6-1-terra-2026-10-26.jpg",
     src="OpenAI posts (23–26 Oct) · Texas AG announcement (23 Oct)", facts=[
     ("GPT six point one Terra", "$1 / $5", "GPT-6.1 Terra · per 1M tokens in / out", CYAN, "openai-gpt-6-1-terra-2026-10-26.jpg"),
     ("one tenth", "1/10 price", "OpenAI: matches GPT-6 Astra on one benchmark", GREEN, "openai-gpt-6-1-terra-2026-10-26.jpg"),
     ("three AI-generated results", "3 results", "Kakeya · ETH · QCD · not peer reviewed", AMBER, "openai-ai-generated-proofs-2026-10-26.jpg"),
     ("DNS resolver", "11 days", "Paused top training runs · now offline", AMBER, "openai-securing-frontier-training-environment-2026-10-23.jpg"),
     ("Texas sued", "Texas v. OpenAI", "Allegations unproven · OpenAI not yet responded", GREY, "texas-ag-sues-openai-altman-2026-10-23.jpg"),
     ("competes with OpenAI", "Disclosure", "Anthropic, maker of Claude, competes with OpenAI", AMBER)]),
 5: dict(kicker="GOOGLE", headline="Carbon, Genie 4, TPUs on Oracle", img="google-gemini-4-carbon-2026-10-29.jpg",
     src="Google, DeepMind and Google Cloud posts (27–28 Oct) · Oracle", facts=[
     ("fifty-nine", "Index 59", "Artificial Analysis v5.0 · #1 (Google's claim)", CYAN, "google-gemini-4-carbon-2026-10-29.jpg"),
     ("cyber defenders", "Defenders only", "Fairwind Program · no date for developers", AMBER, "google-gemini-4-carbon-2026-10-29.jpg"),
     ("Genie four", "Genie 4", "Real-time world model with audio · trusted testers", GREEN, "google-deepmind-genie-4-2026-10-27.jpg"),
     ("public preview", "Robotics ER 2", "Public preview on Google Cloud", CYAN, "gemini-robotics-er-2-public-preview-google-cloud-2026-10-29.jpg"),
     ("twenty twenty-seven", "TPUs on OCI", "Google TPUs on Oracle Cloud from 2027", AMBER, "google-oracle-tpus-nvidia-oracle-vera-rubin-oci-2026-10-29.jpg"),
     ("Google's own", "Google's figures", "Anthropic competes with Google", GREY)]),
 6: dict(kicker="MODELS & OPEN WEIGHTS", headline="Weights promised, weights shipped", img="mistral-large-4-open-weights-2026-10-30.jpg",
     src="Moonshot · Mistral · Nanbeige · NVIDIA — benchmarks are the makers' own", facts=[
     ("Kimi K three point one Pro", "Kimi K3.1 Pro", "1M context · weights by 4 Nov · license TBA", AMBER, "moonshot-kimi-k3-1-pro-2026-10-23.jpg"),
     ("Model-as-a-Service", "Mistral Large 4", "1T weights · modified MIT · MaaS needs a license", GREEN, "mistral-large-4-open-weights-2026-10-30.jpg"),
     ("seventy cents", "$0.70 / $2.10", "Mistral API per 1M tokens in / out", CYAN, "mistral-large-4-open-weights-2026-10-30.jpg"),
     ("Nanbeige released", "33B · Apache 2.0", "Nanbeige4.3 · 524K context", GREEN, "nanbeige-4-3-33b-open-weights-2026-10-26.jpg"),
     ("Nemotron three point five Transcribe", "40 languages", "NVIDIA speech-to-text model", CYAN, "nvidia-nemotron-3-5-transcribe-2026-10-29.jpg")]),
 7: dict(kicker="SECURITY", headline="Agent frameworks in attacks", img="crowdstrike-vapor-panda-artex-campaign-2026-10-30.jpg",
     src="CrowdStrike (29 Oct) · Microsoft (21 Oct) · Cloudflare · Cohere", facts=[
     ("VAPOR PANDA", "200+ orgs", "14+ countries · 11 days · mostly on DeepSeek (CrowdStrike)", AMBER, "crowdstrike-vapor-panda-artex-campaign-2026-10-30.jpg"),
     ("Storm-0940", "Storm-0940", "Microsoft: ARTEX in the ConnectWise attack", AMBER, "microsoft-storm-0940-artex-connectwise-2026-10-24.jpg"),
     ("not independently confirmed", "Vendor findings", "Not independently confirmed", GREY, "crowdstrike-vapor-panda-artex-campaign-2026-10-30.jpg"),
     ("one hundred fifty-five", "155 responses", "Cloudflare GLM-5.3 KV cache bug · no exploitation seen", CYAN, "cloudflare-glm-5-3-workers-ai-kv-cache-exposure-2026-10-28.jpg"),
     ("Cohere reported", "Blocked upload", "Qwen3.8 tried a Beijing bucket · sandbox stopped it", AMBER, "cohere-qwen3-8-flash-next-upload-attempt-2026-10-26.jpg")]),
 8: dict(kicker="SCIENCE & MATH", headline="Drugs, proofs, groups", img="anthropic-claude-drug-development-mithril-medicine-2026-10-28.jpg",
     src="Anthropic posts (24–30 Oct) · Axiom Math project page", facts=[
     ("six drug developers", "6 developers", "Early, mostly preclinical · Anthropic's own results", CYAN, "anthropic-claude-drug-development-mithril-medicine-2026-10-28.jpg"),
     ("Mithril Medicine", "Acquisition", "One-person rare-disease company", GREEN, "anthropic-claude-drug-development-mithril-medicine-2026-10-28.jpg"),
     ("one hundred twenty-three", "123 libraries", "Formal proofs · hundreds of bugs · not bug-free", AMBER, "anthropic-claude-formal-verification-123-libraries-2026-10-24.jpg"),
     ("AI for Science", "AI for Science", "Widened to funders and institutions", GREEN, "anthropic-ai-for-science-expands-foundations-2026-10-30.jpg"),
     ("forty-three point one million", "43.1M lines", "Axiom Math · Lean · not yet reviewed", CYAN, "axiom-math-cfsg-lean-formalization-2026-10-28.jpg")]),
 9: dict(kicker="BUSINESS & POLICY", headline="Offerings, discounts, blocks", img="meta-35-billion-equity-offerings-2026-10-26.jpg",
     src="Meta SEC filings (26 Oct) · Anthropic (28 Oct) · SVT (26 Oct)", facts=[
     ("twenty-two point five billion", "$22.5B + preferred", "Meta stock offerings · forward sale agreements", CYAN, "meta-35-billion-equity-offerings-2026-10-26.jpg"),
     ("sixty billion", "~$60B ATM", "Planned · not before 2027", AMBER, "meta-35-billion-equity-offerings-2026-10-26.jpg"),
     ("forty percent", "40% off", "Claude for governments · GSA · state and local too", GREEN, "anthropic-gsa-onegov-40-percent-government-discount-2026-10-28.jpg"),
     ("Sweden's Government Offices", "Sweden", "ChatGPT and Claude web blocked · Copilot approved", AMBER, "sweden-government-offices-block-chatgpt-claude-2026-10-26.jpg")]),
 10: dict(kicker="DEVELOPERS", headline="Fusion, Foundry, Cue", img="github-copilot-fusion-generally-available-2026-10-29.jpg",
     src="GitHub · Microsoft · Anthropic · LlamaIndex · ElevenLabs (27–28 Oct)", facts=[
     ("Copilot Fusion", "Fusion GA", "Multi-model routing · all Copilot plans", CYAN, "github-copilot-fusion-generally-available-2026-10-29.jpg"),
     ("Foundry", "20+ models", "Copilot harness via Foundry · bring your own key", GREEN, "microsoft-copilot-harness-foundry-multi-model-agents-2026-10-29.jpg"),
     ("smart reports", "Enterprise GA", "Smart reports · surveys · pooled budgets", AMBER, "anthropic-claude-enterprise-smart-reports-pooled-budgets-2026-10-29.jpg"),
     ("Document Parsing Protocol", "140 rules", "LlamaIndex draft 0.1 · open for feedback", CYAN, "llamaindex-document-parsing-protocol-2026-10-29.jpg"),
     ("Cue,", "179 ms", "ElevenLabs Cue · average timing error (own figure)", GREEN, "elevenlabs-cue-forced-alignment-model-2026-10-29.jpg"),
     ("makes the voice", "Disclosure", "ElevenLabs makes this voice", AMBER)]),
 11: dict(kicker="NEXT WEEK", headline="Coming up", img=None, src="", facts=[
     ("Kimi K three point one Pro", "By 4 Nov", "Kimi K3.1 Pro weights (promised)", CYAN),
     ("price range", "Anthropic IPO", "No price range yet · timing unconfirmed", AMBER),
     ("Gemini four Carbon", "Carbon access", "No date beyond cyber defenders", GREEN),
     ("technical report", "Mistral report", "Large 4 technical report still owed", CYAN),
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
    d.text((W - 90, 52), "FRIDAY 30 OCT 2026", font=font(SB, 26), fill=GREY + (255,), anchor="ra")
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
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(OUT, "ai-news-this-week-ep-2026-10-30-raw.mp4")])
    raw = os.path.join(OUT, "ai-news-this-week-ep-2026-10-30-raw.mp4")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", os.path.join(OUT, "ai-news-this-week-ep-2026-10-30.mp4")])
    print("done")
