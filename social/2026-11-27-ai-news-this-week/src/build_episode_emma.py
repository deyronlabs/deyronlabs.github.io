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
 2: dict(kicker="NVIDIA", headline="Huang returns as CEO", img="nvidia-huang-reinstated-ceo-2026-11-23.jpg",
     src="Nvidia newsroom and SEC 8-K (23 Nov) · CBS News · The Guardian · Bloomberg", facts=[
     ("voted unanimously", "Huang reinstated", "Board vote unanimous · effective 23 Nov", GREEN, "nvidia-huang-reinstated-ceo-2026-11-23.jpg"),
     ("input from senior levels of the United States government", "US gov input", "Unnamed · the board's statement, not a finding", AMBER, "nvidia-huang-reinstated-ceo-2026-11-23.jpg"),
     ("investigation into a reported foreign intelligence effort", "Probe continues", "Independent committee · no findings yet", CYAN, "nvidia-huang-reinstated-ceo-2026-11-23.jpg"),
     ("chief compliance officer", "New oversight", "Export-control committee · compliance chief search", GREEN, "nvidia-huang-reinstated-ceo-2026-11-23.jpg"),
     ("California served Nvidia with a subpoena", "California", "Guardian: subpoena · Bloomberg: preliminary · no text found", GREY, "nvidia-california-subpoena-2026-11-20.jpg")]),
 3: dict(kicker="ANTHROPIC", headline="Claude Ship, MCP skills, Siren", img="claude-ship-pr-agents-2026-11-24.jpg",
     src="Anthropic announcements and docs (23–24 Nov) · Anthropic makes Claude, which we use", facts=[
     ("launched Claude Ship", "Claude Ship", "23 Nov · Code Review GA · PR agents in beta", CYAN, "claude-ship-pr-agents-2026-11-24.jpg"),
     ("may miss bugs", "Anthropic's caveat", "May miss bugs · no independent evaluation found", AMBER, "claude-ship-pr-agents-2026-11-24.jpg"),
     ("MCP servers can now ship skills", "Skills over MCP", "Public beta · Tasks and Elicitation GA", GREEN, "claude-skills-over-mcp-tasks-elicitation.jpg"),
     ("installed as Mac and Windows apps", "Artifacts as apps", "Mac and Windows · beta", CYAN, "claude-artifacts-install-as-app.jpg"),
     ("twenty-one to thirty-two percent", "Siren: 21–32%", "Left a weakened sandbox · Anthropic's own test", AMBER, "anthropic-siren-sandbox-escape.jpg")]),
 4: dict(kicker="AI & MATH", headline="Proof claims, unchecked", img="anthropic-mathematician-riemann-hypothesis-claim-2026-11-20.jpg",
     src="Alpöge note · Anthropic · OpenAI · Google Research · Google DeepMind · none independently verified", facts=[
     ("claims a proof of the Riemann Hypothesis", "Riemann claim", "Unreviewed note · Lean claimed · no paper", AMBER, "anthropic-mathematician-riemann-hypothesis-claim-2026-11-20.jpg"),
     ("V P is different from V N P", "VP ≠ VNP", "Anthropic and OpenAI · neither verified", CYAN, "anthropic-openai-vp-vnp-proofs-2026-11-24.jpg"),
     ("nine fourths", "n^(9/4)", "OpenAI manuscript · restricted circuits", GREEN, "openai-matmul-exponent-nine-fourths.jpg"),
     ("six preprints", "6 preprints", "Google Cogentic · Gemini 4 · Lean promised", CYAN, "google-cogentic-ai-math-preprints.jpg"),
     ("eleven point eight times", "11.8x", "DeepMind quantum circuit cost · authors' own", GREEN, "deepmind-gemini-4-quantum-algorithms-lean.jpg")]),
 5: dict(kicker="OPENAI", headline="Science and safety posts", img="openai-gpt-6-protein-design-preprint.jpg",
     src="OpenAI posts and preprint (21–25 Nov) · all figures are OpenAI's own", facts=[
     ("thirty-five of three hundred twenty-two", "35 of 322", "Minibinders that bound their targets", GREEN, "openai-gpt-6-protein-design-preprint.jpg"),
     ("two exoplanet candidate signals", "2 candidates", "Kepler and TESS data · none confirmed", CYAN, "openai-astra-amateur-planet-candidates.jpg"),
     ("eighty-four point five percent", "84.5%", "MedChemBench · not proof of drug discovery", AMBER, "openai-medchembench-benchmark-2026-11-21.jpg"),
     ("fifty-four percent to zero point two percent", "54% → 0.2%", "Adversarial distillation · OpenAI's own test", GREEN, "openai-combatting-adversarial-distillation-2026-11-21.jpg"),
     ("eight thousand dollars a month", "OpenWorks", "Up to $8,000 a month to local partners", GREY, "openai-openworks-small-business-pilot.jpg")]),
 6: dict(kicker="OPEN WEIGHTS", headline="New open models", img="glm-5-4-loop-transformer-2026-11-23.jpg",
     src="Z.ai · Ant Group · Aleph Alpha · Sarvam · JetBrains · Sand.ai · Nvidia · makers' own figures", facts=[
     ("GLM five point four", "GLM-5.4", "Loop Transformer · weights only planned", AMBER, "glm-5-4-loop-transformer-2026-11-23.jpg"),
     ("Ling three point two air", "Ling-3.2-air", "MIT · 124B total · 5.5B active", GREEN, "ant-ling-3-2-air-mit.jpg"),
     ("Kolibri one point one", "Kolibri 1.1", "Aleph Alpha · Apache 2.0", CYAN, "aleph-alpha-kolibri-1-1-2026-11-24.jpg"),
     ("Mellum two point one Instruct", "Mellum2.1", "JetBrains · 12B · Apache 2.0", GREEN, "jetbrains-mellum2-1-instruct.jpg"),
     ("four hundred eighty billion parameters", "MAGI-2 480B", "Video model · weights promised, not out", AMBER, "sand-ai-magi-2-480b-video-model.jpg")]),
 7: dict(kicker="MONEY & DEALS", headline="Sierra, Decart, data centers", img="sierra-series-f-30b-valuation-2026-11-24.jpg",
     src="Sierra · Amazon · Calcalist · Reuters (23 Nov) · company statements", facts=[
     ("one point seven five billion dollars", "$1.75B at $30B", "Sierra Series F · company statement", GREEN, "sierra-series-f-30b-valuation-2026-11-24.jpg"),
     ("four hundred million dollars in annual recurring revenue", "$400M+ ARR", "Sierra's own figure", CYAN, "sierra-series-f-30b-valuation-2026-11-24.jpg"),
     ("Amazon agreed to acquire", "Amazon + Decart", "No price given · Calcalist: about $7.5B", AMBER, "amazon-decart-7-5b-deal-2026-11-23.jpg"),
     ("five point four billion dollars over eighteen years", "$5.4B lease", "Applied Digital · 150 MW · Reuters", GREEN, "applied-digital-5-4b-lease-2026-11-23.jpg")]),
 8: dict(kicker="CHIPS & POLICY", headline="Rules, tax, orbit", img="bis-entity-list-megaspeed-seven-entities.jpg",
     src="BIS rule (23 Nov) · CNBC · CLS · FCC Space Bureau (25 Nov)", facts=[
     ("seven entities linked to Megaspeed", "7 entities", "Megaspeed-linked · Entity List · 23 Nov", CYAN, "bis-entity-list-megaspeed-seven-entities.jpg"),
     ("tremendous tax", "Overseas data centers", "Trump statement · no rate or document", AMBER, "trump-no-overseas-data-centers-tax-2026-11-20.jpg"),
     ("next Qwen model is already training", "Qwen on T-Head", "Alibaba's own chips · per a Chinese outlet", GREEN, "alibaba-next-qwen-trained-on-t-head-chips-2026-11-19.jpg"),
     ("one million orbital data center satellites", "FCC: 1M sats", "Granted in part · milestones 2033–2040", GREY, "fcc-spacex-orbital-data-centers.jpg")]),
 9: dict(kicker="SECURITY & LAW", headline="Suits, 11 minutes, MCP", img="virginia-oregon-sue-spacex-grok-deepfakes.jpg",
     src="State suits as reported · Amazon Threat Intelligence · Google Workspace", facts=[
     ("Virginia and Oregon have each sued SpaceX", "VA + OR v. SpaceX", "Grok deepfake allegations · untested", AMBER, "virginia-oregon-sue-spacex-grok-deepfakes.jpg"),
     ("about eleven minutes", "11 minutes", "Cairn agents · API to root shell · Amazon", CYAN, "aws-cairn-ai-agents-found-zero-day-2026-11-21.jpg"),
     ("Workspace M C P servers generally available", "Workspace MCP GA", "Agents must use MCP from 1 Feb 2027", GREEN, "google-workspace-mcp-ga-agents-must-use-mcp.jpg")]),
 10: dict(kicker="NEXT WEEK", headline="Coming up", img=None, src="", facts=[
     ("introductory prices double", "1 Dec", "Gemini 4 Carbon and Argon: $2/$10 → $4/$20", AMBER),
     ("ten cent promotion for Clairic ends", "1 Dec", "Cloudflare Clairic $0.10 promo ends", CYAN),
     ("due before the House", "1 Dec", "Huang before the House · CBS · unconfirmed", GREEN)]),
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
    d.text((W - 90, 52), "FRIDAY 27 NOV 2026", font=font(SB, 26), fill=GREY + (255,), anchor="ra")
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
    raw = os.path.join(OUT, "ai-news-this-week-ep-2026-11-27-emma-raw.mp4")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", raw])
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", os.path.join(OUT, "ai-news-this-week-ep-2026-11-27-emma.mp4")])
    print("done")
