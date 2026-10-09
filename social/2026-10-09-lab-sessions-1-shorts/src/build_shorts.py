#!/usr/bin/env python3
"""Build vertical Shorts from Lab Sessions #1 screen recordings (PIL + ffmpeg)."""
import re, subprocess, sys, os, json, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SP = "/tmp/claude-0/-home-claude-deyronlabs-github-io/07b8b40e-b381-5b08-9e32-18417e515872/scratchpad"
ASSETS = f"{SP}/assets"
OUT = f"{SP}/out"
os.makedirs(OUT, exist_ok=True)
FONT_XB = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FONT_B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FONT_SB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"

W, H = 1080, 1920
NIGHT = (18, 18, 28)
GREEN, CYAN, VIOLET, MAGENTA, AMBER = (34, 197, 94), (34, 211, 238), (139, 92, 246), (236, 72, 153), (245, 158, 11)
PALETTE = [GREEN, CYAN, VIOLET, MAGENTA, AMBER]
VX, VY, VW, VH = 90, 470, 900, 886          # screen position / size
CROP = "crop=902:888:672:112"
LEAD = 0.3
END_CARD = 3.0

def font(p, s):
    return ImageFont.truetype(p, s)

# ---------------------------------------------------------------- configs
SHORTS = {
 "s1": dict(
    rec="rec-08.mp4", seg="seg-08.mp3", slug="edit-photo-by-asking",
    line1="EDIT A PHOTO", line2="just by asking.", chip="STEP 4 · EDIT BY TALKING",
    pieces=[("play", 0.0, 6.5, 1.0), ("freeze", 6.5, 5.7), ("play", 8.0, 21.0, 5.0),
            ("play", 21.0, 29.0, 1.0), ("play", 36.0, 42.0, 1.0)],
    still=40.0,
    cues=[("Step four is the part that makes this tool different.", 0.0, 5.22),
          ("You edit the image by talking to it.", 5.79, 7.09),
          ("In the same chat, I wrote:", 7.55, 8.38),
          ("Edit this image, make the mug matte dark green,", 8.72, 10.75),
          ("with the text LAB in white.", 10.75, 11.88),
          ("Keep everything else exactly the same.", 12.32, 14.29),
          ("And look.", 14.88, 15.36),
          ("The mug changed color, the text changed color,", 15.76, 18.30),
          ("and the desk, the plant, the light", 18.56, 19.85),
          ("and the notebook stayed where they were.", 20.05, 22.27),
          ("The sentence “keep everything else exactly the same”", 22.89, 25.85),
          ("is doing real work here.", 25.85, 27.24),
          ("Always include it.", 27.67, 28.56)]),
 "s2": dict(
    rec="rec-09.mp4", seg="seg-09.mp3", slug="remove-and-add-in-one-prompt",
    line1="REMOVE & ADD", line2="in one prompt.", chip="STEP 5 · SEVERAL EDITS AT ONCE",
    pieces=[("play", 3.5, 8.5, 1.0), ("freeze", 8.5, 6.0), ("play", 9.0, 21.0, 8.0),
            ("play", 21.0, 32.0, 1.0), ("freeze", 32.0, 5.5)],
    still=30.0,
    cues=[("Step five,", 0.0, 0.79),
          ("make several changes in one message.", 1.2, 3.32),
          ("I asked:", 3.94, 4.45),
          ("remove the notebook from the desk,", 4.91, 6.62),
          ("and add a small paper airplane next to the mug.", 6.62, 8.93),
          ("Keep the lighting and everything else the same.", 9.48, 11.51),
          ("The notebook is gone,", 12.31, 13.30),
          ("a paper airplane appeared,", 13.58, 14.83),
          ("and the mug is untouched.", 15.12, 16.54),
          ("One tip.", 17.28, 17.70),
          ("If the model changes something you did not ask for,", 18.27, 20.71),
          ("say so in the next message,", 20.96, 22.32),
          ("for example:", 22.75, 23.29),
          ("the plant changed,", 23.76, 24.67),
          ("put it back as in the previous version.", 25.06, 26.74),
          ("It usually listens.", 27.19, 28.22)]),
 "s3": dict(
    rec="rec-11.mp4", seg="seg-11.mp3", slug="small-text-weak-spot",
    line1="SMALL TEXT", line2="is the weak spot.", chip="MISTAKE #1 · ALWAYS ZOOM IN",
    pieces=[("play", 3.5, 5.5, 1.0), ("freeze", 5.5, 9.2), ("play", 6.0, 18.0, 8.0),
            ("play", 19.0, 24.0, 1.2), ("play", 26.0, 32.5, 1.0), ("freeze", 32.5, 3.0)],
    still=29.0,
    cues=[("Now, the mistakes.", 0.0, 1.42),
          ("Number one, small text.", 2.02, 3.93),
          ("I asked the model to add a small line under the big word,", 4.5, 7.94),
          ("reading Deyron Labs, image editing test, 2026.", 8.15, 11.5),
          ("It added the line,", 12.01, 12.88),
          ("and at first glance it looks right,", 13.09, 14.7),
          ("but small letters are the weak spot.", 15.15, 16.96),
          ("Google itself lists small text as a known limitation,", 17.44, 20.57),
          ("so zoom in and check every character", 20.96, 22.9),
          ("before you publish anything.", 22.9, 24.48)]),
}

# ---------------------------------------------------------------- helpers
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("RETURNCODE", r.returncode); print(r.stderr[-3000:]); raise SystemExit(1)
    return r

def audio_info(path):
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).stdout)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    sil = []
    for i, s in enumerate(starts):
        e = ends[i] if i < len(ends) else dur
        sil.append((s, e))
    # speech intervals
    speech, cur = [], 0.0
    for s, e in sil:
        if s - cur > 0.05:
            speech.append((cur, s))
        cur = e
    if dur - cur > 0.05:
        speech.append((cur, dur))
    return dur, speech

def speech_to_real(speech, x):
    """Map a position in cumulative speech-time to real time."""
    acc = 0.0
    for s, e in speech:
        L = e - s
        if x <= acc + L + 1e-9:
            return s + (x - acc)
        acc += L
    return speech[-1][1]

def make_cues(phrases, speech):
    total = sum(e - s for s, e in speech)
    chars = [len(p) for p in phrases]
    ct = sum(chars)
    cues, acc = [], 0
    for p, c in zip(phrases, chars):
        a = acc / ct * total; b = (acc + c) / ct * total
        acc += c
        cues.append((p, speech_to_real(speech, a + 0.001), speech_to_real(speech, b - 0.001)))
    return cues

def draw_multicolor(d, xy, text, fnt, fill_shadow=(0, 0, 0)):
    x, y = xy
    ci = 0
    for ch in text:
        if ch == " ":
            x += d.textlength(" ", font=fnt); continue
        col = PALETTE[ci % len(PALETTE)]; ci += 1
        d.text((x + 5, y + 6), ch, font=fnt, fill=fill_shadow)
        d.text((x, y), ch, font=fnt, fill=col)
        x += d.textlength(ch, font=fnt)

def multicolor_width(d, text, fnt):
    return sum(d.textlength(ch, font=fnt) for ch in text)

def bg_image(cfg, hole=True):
    random.seed(7)
    img = Image.new("RGB", (W, H), NIGHT)
    px = img.load()
    # soft diagonal gradient
    g = Image.new("RGB", (W, H))
    gd = ImageDraw.Draw(g)
    for yy in range(0, H, 4):
        t = yy / H
        c = (int(18 + 14 * t), int(18 + 4 * t), int(28 + 22 * t))
        gd.rectangle([0, yy, W, yy + 4], fill=c)
    img = g
    d = ImageDraw.Draw(img)
    # particles
    for _ in range(26):
        x, y = random.randint(20, W - 40), random.choice([random.randint(180, 440), random.randint(1380, 1880)])
        s = random.choice([8, 10, 14])
        d.rectangle([x, y, x + s, y + s], fill=random.choice(PALETTE))
    # header: George head + pills
    thumb = Image.open(f"{ASSETS}/lab-sessions-1-thumbnail-1920x1080.png").convert("RGB")
    head = thumb.crop((60, 150, 380, 550)).resize((112, 140), Image.LANCZOS)
    img.paste(head, (60, 96))
    d = ImageDraw.Draw(img)
    f1 = font(FONT_XB, 34)
    pill = "LAB SESSIONS #1"
    pw = int(d.textlength(pill, font=f1)) + 48
    d.rounded_rectangle([190, 118, 190 + pw, 178], radius=30, fill=AMBER)
    d.text((190 + 24, 128), pill, font=f1, fill=(20, 20, 20))
    f2 = font(FONT_B, 30)
    sub = "NANO BANANA · FREE"
    d.text((190 + pw + 28, 132), sub, font=f2, fill=CYAN)
    # title
    big = font(FONT_XB, 118)
    tw = multicolor_width(d, cfg["line1"], big)
    draw_multicolor(d, ((W - tw) / 2, 218), cfg["line1"], big)
    sm = font(FONT_XB, 72)
    l2w = d.textlength(cfg["line2"], font=sm)
    d.text(((W - l2w) / 2 + 3, 368 + 4), cfg["line2"], font=sm, fill=(0, 0, 0))
    d.text(((W - l2w) / 2, 368), cfg["line2"], font=sm, fill=(255, 255, 255))
    # color bar
    bw = 120
    x0 = (W - bw * 5) // 2
    for i, c in enumerate(PALETTE):
        d.rectangle([x0 + i * bw, 458, x0 + (i + 1) * bw, 464], fill=c)
    # frame border around the screen
    d.rounded_rectangle([VX - 6, VY - 6, VX + VW + 6, VY + VH + 6], radius=34, fill=CYAN)
    if hole:
        img = img.convert("RGBA")
        mask = Image.new("L", (W, H), 255)
        md = ImageDraw.Draw(mask)
        md.rounded_rectangle([VX, VY, VX + VW, VY + VH], radius=28, fill=0)
        img.putalpha(mask)
        d = ImageDraw.Draw(img)
    # step chip (top-left of screen, on top)
    fc = font(FONT_XB, 32)
    cw = int(d.textlength(cfg["chip"], font=fc)) + 44
    d.rounded_rectangle([VX - 6, VY - 30, VX - 6 + cw, VY + 28], radius=29, fill=AMBER)
    d.text((VX - 6 + 22, VY - 21), cfg["chip"], font=fc, fill=(20, 20, 20))
    # footer note
    fn = font(FONT_SB, 27)
    note = "AI voice · animated host · screen-recorded in Gemini"
    nw = d.textlength(note, font=fn)
    d.text(((W - nw) / 2, 1648), note, font=fn, fill=(150, 150, 170))
    return img

def caption_png(text, path):
    img = Image.new("RGBA", (1000, 230), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(FONT_XB, 56)
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= 940:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    assert len(lines) <= 3, text
    lh = 70
    y = (230 - lh * len(lines)) // 2
    for ln in lines:
        w = d.textlength(ln, font=f)
        x = (1000 - w) / 2
        d.text((x, y), ln, font=f, fill=(255, 255, 255), stroke_width=8, stroke_fill=(0, 0, 0))
        y += lh
    img.save(path)

def endcard_png(path):
    img = Image.new("RGBA", (W, H), (10, 10, 18, 232))
    d = ImageDraw.Draw(img)
    thumb = Image.open(f"{ASSETS}/lab-sessions-1-thumbnail-1920x1080.png").convert("RGB")
    g = thumb.crop((0, 150, 780, 1010)).resize((390, 430), Image.LANCZOS)
    img.paste(g, ((W - 390) // 2, 330))
    d = ImageDraw.Draw(img)
    def center(txt, y, fnt, fill):
        w = d.textlength(txt, font=fnt)
        d.text(((W - w) / 2, y), txt, font=fnt, fill=fill)
    center("FULL TUTORIAL", 800, font(FONT_B, 40), CYAN)
    big = font(FONT_XB, 84)
    tw = multicolor_width(d, "LAB SESSIONS #1", font(FONT_XB, 84))
    if tw > 960:
        big = font(FONT_XB, 70); tw = multicolor_width(d, "LAB SESSIONS #1", big)
    draw_multicolor(d, ((W - tw) / 2, 860), "LAB SESSIONS #1", big)
    center("Edit images with Nano Banana", 980, font(FONT_XB, 54), (255, 255, 255))
    center("Watch on YouTube · Deyron Labs", 1070, font(FONT_B, 40), (190, 190, 205))
    center("deyronlabs.com", 1140, font(FONT_XB, 46), GREEN)
    img.save(path)

# ---------------------------------------------------------------- build
def build(key):
    cfg = SHORTS[key]
    d = f"{OUT}/{key}"; os.makedirs(d, exist_ok=True)
    seg = f"{ASSETS}/{cfg['seg']}"; rec = f"{ASSETS}/{cfg['rec']}"
    dur, speech = audio_info(seg)
    cues = cfg["cues"]
    speech_end = cues[-1][2]
    total_main = LEAD + speech_end + 0.4
    total = total_main + END_CARD
    json.dump(dict(dur=dur, speech=speech, cues=cues, total=total), open(f"{d}/info.json", "w"), indent=1)

    bg_image(cfg, True).save(f"{d}/bg_hole.png")
    endcard_png(f"{d}/endcard.png")
    Image.new("RGBA", (1000, 230), (0, 0, 0, 0)).save(f"{d}/blank.png")
    cap_files = []
    for i, (txt, a, b) in enumerate(cues):
        p = f"{d}/cap{i:02d}.png"; caption_png(txt, p); cap_files.append(p)

    # 1) encode each piece separately (avoids ffmpeg buffering 60fps frames)
    vf_common = f"fps=30,{CROP},scale={VW}:{VH}:flags=lanczos,setsar=1"
    piece_files = []
    for i, pc in enumerate(cfg["pieces"]):
        pf = f"{d}/piece{i}.mp4"
        if pc[0] == "play":
            _, s, e, sp = pc
            vf = f"setpts=(PTS-STARTPTS)/{sp},{vf_common}"
            cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(s), "-t", str(e - s), "-i", rec, "-vf", vf]
        else:
            _, tt, dd = pc
            vf = f"setpts=PTS-STARTPTS,{vf_common},tpad=stop_mode=clone:stop_duration={dd}"
            cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(tt), "-t", "0.1", "-i", rec, "-vf", vf]
        cmd += ["-an", "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p", "-r", "30", pf]
        run(cmd); piece_files.append(pf)
    with open(f"{d}/pieces.txt", "w") as f:
        for pf in piece_files:
            f.write(f"file '{pf}'\n")

    # 2) caption timeline as a single concat input
    events, cur = [], 0.0   # times on the final timeline (LEAD included)
    for (txt, a, b), cp in zip(cues, cap_files):
        s = a + LEAD
        e = b + LEAD + 0.25
        if s > cur:
            events.append(("blank", s - cur)); cur = s
        events.append((cp, max(e - cur, 0.1))); cur = cur + max(e - cur, 0.1)
    events.append(("blank", max(total + 1 - cur, 0.5)))
    with open(f"{d}/caps.txt", "w") as f:
        for name, dd in events:
            fn = f"{d}/blank.png" if name == "blank" else name
            f.write(f"file '{fn}'\nduration {dd:.3f}\n")
        f.write(f"file '{d}/blank.png'\n")

    inputs = ["-f", "concat", "-safe", "0", "-i", f"{d}/pieces.txt",              # 0 video pieces
              "-i", seg,                                                           # 1 audio
              "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r=30",                # 2 base
              "-loop", "1", "-framerate", "30", "-i", f"{d}/bg_hole.png",          # 3 frame
              "-loop", "1", "-framerate", "30", "-i", f"{d}/endcard.png",          # 4 end card
              "-f", "concat", "-safe", "0", "-i", f"{d}/caps.txt"]                 # 5 captions
    fc = [f"[0:v]tpad=start_mode=clone:start_duration={LEAD},tpad=stop_mode=clone:stop_duration=6[vc]",
          f"[2:v][vc]overlay={VX}:{VY}:eof_action=pass[b1]",
          "[b1][3:v]overlay=0:0[b2]",
          "[5:v]fps=30,format=rgba[cp]",
          "[b2][cp]overlay=40:1400:eof_action=pass[b3]",
          f"[b3][4:v]overlay=0:0:enable='gte(t,{total_main:.2f})'[vout]",
          "[1:a]adelay=300:all=1,loudnorm=I=-16:TP=-1.5:LRA=11,apad[aout]"]
    outp = f"{d}/short-lab-sessions-1-{cfg['slug']}.mp4"
    cmd = ["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", ";".join(fc),
           "-map", "[vout]", "-map", "[aout]", "-t", f"{total:.2f}", "-r", "30", "-c:v", "libx264", "-preset", "medium",
           "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", outp]
    run(cmd)

    # cover (1080x1920): still frame behind the hole
    still = f"{d}/still.png"
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(cfg["still"]), "-i", rec, "-vf",
         f"{CROP},scale={VW}:{VH}:flags=lanczos", "-frames:v", "1", still])
    cover = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    cover.paste(Image.open(still).convert("RGBA"), (VX, VY))
    bgc = bg_image(cfg, True)
    cover = Image.alpha_composite(cover, bgc).convert("RGB")
    cover.save(f"{d}/cover-1080x1920.png")
    print(key, "ok", f"{total:.1f}s", outp)

if __name__ == "__main__":
    for k in (sys.argv[1:] or list(SHORTS)):
        build(k)
