#!/usr/bin/env python3
"""Intro "AI News This Week" (weekly news show), 1920x1080, 30 fps, 7 s, with synthesized sound.

Style: news-studio navy, cyan + amber accents. Build-up (speed lines converge, riser, white-out),
IMPACT at 2.0 s (flash, shockwaves, particle burst, screen shake, title slam with chromatic split),
shine sweep, amber ticker, fade out.

Usage: OUT_DIR=/some/dir python3 build_intro.py
Outputs: ai-news-this-week-intro.mp4, ai-news-this-week-title-card.png
Needs: numpy, Pillow, ffmpeg, Inter fonts in /usr/share/fonts/opentype/inter/
"""
import os, math, random, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = os.environ["OUT_DIR"]
os.makedirs(OUT, exist_ok=True)
W, H, FPS, DUR = 1920, 1080, 30, 7.0
NF = int(FPS * DUR)
FD = "/usr/share/fonts/opentype/inter/"
XB, BD, SB = FD + "Inter-ExtraBold.otf", FD + "Inter-Bold.otf", FD + "Inter-SemiBold.otf"
NAVY, CYAN, AMBER = (10, 14, 30), (34, 211, 238), (245, 158, 11)
GREEN, WHITE, MAG, VIOLET = (34, 197, 94), (255, 255, 255), (236, 72, 153), (139, 92, 246)
T0 = 2.0                      # impact time
CX, CY = W // 2, 525          # centre of the title block
rnd = random.Random(7)


def font(p, s): return ImageFont.truetype(p, s)
def clamp01(x): return min(max(x, 0.0), 1.0)
def ease_out(x): x = clamp01(x); return 1 - (1 - x) ** 3
def col(c, a): return tuple(int(min(255, max(0, v * a))) for v in c)


# ------------------------------------------------------------------ static layers
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
rr = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2)
BG = np.array(NAVY, dtype=np.float32)[None, None, :] * np.clip(1.45 - 1.7 * rr, 0.35, 1.45)[..., None]
BG[..., 2] += 14 * np.clip(0.6 - rr * 1.2, 0, 1)            # soft blue core
DIAG = xx + 0.35 * yy                                        # for the shine sweep


def build_title():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    f1 = font(XB, 340); t = "AI NEWS"
    w = d.textlength(t, font=f1)
    d.text(((W - w) / 2 + 9, 200 + 11), t, font=f1, fill=(0, 0, 0, 175))
    d.text(((W - w) / 2, 200), t, font=f1, fill=WHITE + (255,))
    f2 = font(XB, 190); a, b = "THIS ", "WEEK"
    wa, wb = d.textlength(a, font=f2), d.textlength(b, font=f2)
    x0, y = (W - wa - wb) / 2, 585
    d.text((x0 + 7, y + 9), a + b, font=f2, fill=(0, 0, 0, 175))
    d.text((x0, y), a, font=f2, fill=CYAN + (255,))
    d.text((x0 + wa, y), b, font=f2, fill=AMBER + (255,))
    return img


TITLE = build_title()
T_ARR = np.asarray(TITLE).astype(np.float32)
T_RGB, T_A = T_ARR[..., :3], T_ARR[..., 3] / 255.0
GLOW = np.asarray(TITLE.split()[3].filter(ImageFilter.GaussianBlur(26))).astype(np.float32) / 255.0


def scaled_title(s):
    if s < 1.002:
        return T_RGB, T_A
    im = TITLE.resize((int(W * s), int(H * s)), Image.BICUBIC)
    l, t = int(CX * s - CX), int(CY * s - CY)
    arr = np.asarray(im.crop((l, t, l + W, t + H))).astype(np.float32)
    return arr[..., :3], arr[..., 3] / 255.0


def shifted(a, dx):
    return np.roll(a, dx, axis=1)


# subtitle (tracked caps) and logo
def tracked(d, x, y, text, f, fill, track):
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + track
    return x


def build_sub():
    img = Image.new("RGBA", (W, 120), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    f = font(SB, 44); text = "THE WEEK'S BIGGEST AI STORIES, EXPLAINED"; track = 9
    wt = sum(d.textlength(c, font=f) + track for c in text) - track
    tracked(d, (W - wt) / 2, 30, text, f, (214, 222, 240, 255), track)
    return np.asarray(img).astype(np.float32)


SUB = build_sub()


def build_logo():
    img = Image.new("RGBA", (460, 130), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    x, y, a = 66, 62, 42
    d.polygon([(x, y - a), (x + a * .87, y - a / 2), (x, y), (x - a * .87, y - a / 2)], fill=(134, 239, 172, 255))
    d.polygon([(x - a * .87, y - a / 2), (x, y), (x, y + a), (x - a * .87, y + a / 2)], fill=GREEN + (255,))
    d.polygon([(x + a * .87, y - a / 2), (x, y), (x, y + a), (x + a * .87, y + a / 2)], fill=(21, 128, 61, 255))
    d.text((130, 36), "DEYRON LABS", font=font(XB, 38), fill=WHITE + (255,))
    d.text((132, 82), "AI NEWS · AI TOOLS, TESTED.", font=font(BD, 20), fill=GREEN + (255,))
    return np.asarray(img).astype(np.float32)


LOGO = build_logo()


def build_ticker():
    f = font(XB, 38)
    unit = "DEYRON LABS   ·   AI NEWS THIS WEEK   ·   GLOBAL AI, EVERY FRIDAY   ·   "
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    uw = int(probe.textlength(unit, font=f))
    reps = W // uw + 3
    img = Image.new("RGB", (uw * reps, 76), AMBER); d = ImageDraw.Draw(img)
    for i in range(reps):
        d.text((i * uw, 15), unit, font=f, fill=(24, 18, 6))
    return np.asarray(img).astype(np.float32), uw


TICK, TICK_PERIOD = build_ticker()

# ------------------------------------------------------------------ particles / lines
DOTS = [(x, y) for x in range(30, W, 60) for y in range(30, H, 60)]
DOT_DIST = [math.hypot(x - CX, y - CY) for x, y in DOTS]
LINES = [dict(a=rnd.uniform(0, 2 * math.pi), off=rnd.uniform(0, 0.9), ln=rnd.uniform(90, 260),
              c=rnd.choice([CYAN, CYAN, WHITE, AMBER])) for _ in range(80)]
PARTS = []
for _ in range(340):
    PARTS.append(dict(a=rnd.uniform(0, 2 * math.pi), v=rnd.uniform(500, 2300) ** 1.0, life=rnd.uniform(0.9, 2.2),
                      c=rnd.choice([CYAN, CYAN, AMBER, WHITE, WHITE, MAG, VIOLET]), w=rnd.choice([2, 3, 3, 4])))
EMBERS = []
for _ in range(160):
    EMBERS.append(dict(a=rnd.uniform(0, 2 * math.pi), v=rnd.uniform(120, 700), life=rnd.uniform(2.5, 4.6),
                       c=rnd.choice([CYAN, AMBER, WHITE]), r=rnd.choice([2, 3, 3, 4]), ph=rnd.uniform(0, 6.28)))
RINGS = [(T0, WHITE, 11), (T0 + 0.06, CYAN, 18), (T0 + 0.14, AMBER, 13), (T0 + 0.26, VIOLET, 9)]


def draw_fx(t):
    F = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(F)
    # dot grid with scan + shockwave pulse
    scan_y = (t / T0) * H if t < T0 else -999
    for (x, y), dist in zip(DOTS, DOT_DIST):
        b = 0.26
        if t < T0:
            b += 0.7 * math.exp(-((y - scan_y) / 55) ** 2)
        for ts, _, _ in RINGS:
            if t > ts:
                p = (t - ts) / 1.5
                if p < 1:
                    b += 1.0 * math.exp(-((dist - 2400 * ease_out(p)) / 95) ** 2) * (1 - p)
        r = 2 + (1.5 if b > 0.8 else 0)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col(CYAN, min(b, 1.5)))
    if t < T0:
        # converging speed lines
        for L in LINES:
            p = clamp01((t - 0.1 - L["off"] * 0.9) / (1.75 - L["off"] * 0.9))
            if p <= 0: continue
            head = 1500 * (1 - p ** 1.5)
            if head < 30: continue
            tail = head + L["ln"] * (0.4 + p)
            ca, sa = math.cos(L["a"]), math.sin(L["a"])
            d.line([CX + ca * head, CY + sa * head, CX + ca * tail, CY + sa * tail],
                   fill=col(L["c"], 0.25 + 0.75 * p), width=2 + int(3 * p))
        # growing core
        u = t / T0
        r = 6 + 80 * u ** 3
        d.ellipse([CX - r * 2.2, CY - r * 2.2, CX + r * 2.2, CY + r * 2.2], outline=col(CYAN, 0.5 + 0.5 * u), width=3)
        d.ellipse([CX - r, CY - r, CX + r, CY + r], fill=col(WHITE, 0.4 + 0.6 * u))
    else:
        tau = t - T0
        # shockwave rings
        for ts, c, wd in RINGS:
            p = (t - ts) / 1.5
            if 0 < p < 1:
                R = 2400 * ease_out(p)
                d.ellipse([CX - R, CY - R, CX + R, CY + R], outline=col(c, (1 - p) ** 1.4), width=max(2, int(wd * (1 - p * 0.6))))
        # anamorphic streak
        if tau < 0.9:
            ln = W * 1.1 * ease_out(tau / 0.25); a = (1 - tau / 0.9) ** 2
            d.line([CX - ln / 2, CY, CX + ln / 2, CY], fill=col(CYAN, a), width=8)
            d.line([CX - ln / 2, CY, CX + ln / 2, CY], fill=col(WHITE, a), width=3)
        # particle burst
        k = 2.3
        for P in PARTS:
            if tau >= P["life"]: continue
            dist = P["v"] / k * (1 - math.exp(-k * tau)); sp = P["v"] * math.exp(-k * tau)
            ca, sa = math.cos(P["a"]), math.sin(P["a"])
            x, y = CX + ca * dist, CY + sa * dist
            tl = min(sp * 0.045, 160)
            a = (1 - tau / P["life"]) ** 1.2
            d.line([x, y, x - ca * tl, y - sa * tl], fill=col(P["c"], a), width=P["w"])
        # embers
        for E in EMBERS:
            if tau >= E["life"]: continue
            dist = E["v"] / 1.4 * (1 - math.exp(-1.4 * tau))
            x = CX + math.cos(E["a"]) * dist; y = CY + math.sin(E["a"]) * dist - 18 * tau
            a = (1 - tau / E["life"]) * (0.55 + 0.45 * math.sin(tau * 9 + E["ph"]))
            r = E["r"]
            d.ellipse([x - r, y - r, x + r, y + r], fill=col(E["c"], max(a, 0)))
    return F


def bloom(F):
    small = F.resize((W // 4, H // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(5))
    return np.asarray(small.resize((W, H), Image.BICUBIC)).astype(np.float32)


# ------------------------------------------------------------------ frame composition
def compose(t, want_title_only=False):
    fx = draw_fx(t)
    frame = BG + np.asarray(fx).astype(np.float32) + 1.15 * bloom(fx)
    # whiteout ramp then flash decay
    if t < T0:
        fl = clamp01((t - 1.62) / 0.38) ** 3
    else:
        fl = clamp01(1 - (t - T0) / 0.38) ** 2
    # title
    if t >= T0:
        p = clamp01((t - T0) / 0.24)
        s = 1 + 0.9 * (1 - ease_out(p)) ** 2
        rgb, a = scaled_title(s)
        op = clamp01(p * 5)
        d_px = int(22 * math.exp(-(t - T0) * 6.5))
        if d_px >= 2:      # chromatic split
            ga = shifted(a, -d_px) * 0.7 * op; gb = shifted(a, d_px) * 0.7 * op
            frame = frame * (1 - ga[..., None]) + np.array(MAG, np.float32) * ga[..., None]
            frame = frame * (1 - gb[..., None]) + np.array(CYAN, np.float32) * gb[..., None]
        frame += (GLOW[..., None] * np.array([20, 70, 85], np.float32)) * op * clamp01((t - T0 - 0.2) / 0.5)
        aa = (a * op)[..., None]
        frame = frame * (1 - aa) + rgb * aa
        # shine sweep
        if 3.4 <= t <= 4.3:
            pos = -300 + (W + 700) * ((t - 3.4) / 0.9)
            sh = np.exp(-((DIAG - pos) / 75) ** 2) * T_A
            frame += 235 * sh[..., None]
        # subtitle + line
        if t >= 2.7:
            q = ease_out((t - 2.7) / 0.45)
            sa = SUB[..., 3:4] / 255.0 * q
            y0 = 842
            frame[y0:y0 + 120] = frame[y0:y0 + 120] * (1 - sa) + SUB[..., :3] * sa
            ln = int(900 * q)
            if ln > 2:
                frame[828:832, CX - ln // 2:CX + ln // 2] = np.array(AMBER, np.float32)
        # logo
        if t >= 2.35:
            q = clamp01((t - 2.35) / 0.4)
            la = LOGO[..., 3:4] / 255.0 * q
            frame[40:170, 50:510] = frame[40:170, 50:510] * (1 - la) + LOGO[..., :3] * la
        # ticker
        if t >= 3.0:
            q = ease_out((t - 3.0) / 0.4)
            top = int(H - 76 * q)
            off = int((t - 3.0) * 240) % TICK_PERIOD
            frame[top:top + 76] = TICK[:, off:off + W][: H - top]
    # shake
    if t >= T0:
        amp = 30 * math.exp(-(t - T0) * 7.5)
        dx, dy = int(amp * math.sin(t * 95)), int(amp * math.cos(t * 120))
        frame = np.roll(frame, (dy, dx), axis=(0, 1))
    frame = frame * (1 - fl) + 255.0 * fl
    # final fade
    if t > 6.55:
        frame *= 1 - clamp01((t - 6.55) / 0.45)
    return np.clip(frame, 0, 255).astype(np.uint8)


# ------------------------------------------------------------------ sound (numpy synth)
def build_audio(path):
    SR = 44100; N = int(SR * DUR)
    t = np.arange(N) / SR
    g = np.random.default_rng(3)
    ramp = lambda x: np.clip(x, 0, 1)
    pre = (t < T0).astype(np.float64)
    u = np.where(t < T0, t / T0, 0.0)
    # riser: stacked sine sweep + rising noise
    f = 90 * 2 ** (u * 4.4)
    ph = 2 * np.pi * np.cumsum(f) / SR
    riser = (np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.3 * np.sin(3 * ph)) * (u ** 2.2) * 0.30 * pre
    nz = g.standard_normal((2, N))
    hp = np.diff(nz, axis=1, prepend=0)
    risen = hp * (u ** 3) * 0.10 * pre
    duck = np.where(t < T0, 1 - ramp((t - (T0 - 0.08)) / 0.01), 1.0)
    L = (riser + risen[0]) * duck; R = (riser + risen[1]) * duck
    tau = np.clip(t - T0, 0, None); post = (t >= T0).astype(np.float64)
    # sub boom with pitch drop
    fb = 30 + 70 * np.exp(-tau / 0.12)
    boom = np.sin(2 * np.pi * np.cumsum(fb) / SR) * np.exp(-tau / 0.9) * 0.95 * post
    click = g.standard_normal(N) * np.exp(-tau / 0.006) * 0.55 * post
    whoosh = np.convolve(g.standard_normal(N), np.ones(26) / 26, mode="same") * np.exp(-tau / 0.28) * 1.4 * post
    L += boom + click + whoosh; R += boom + click * 0.9 + np.convolve(g.standard_normal(N), np.ones(26) / 26, mode="same") * np.exp(-tau / 0.28) * 1.4 * post
    # bright "news stab" chord: A major add9, detuned saws
    stab = np.zeros(N)
    for fn in (110.0, 220.0, 277.18, 329.63, 440.0, 554.37, 659.26):
        for det in (0.996, 1.0, 1.004):
            stab += 2 * np.mod(fn * det * tau, 1.0) - 1
    stab = np.convolve(stab, np.ones(5) / 5, mode="same") * np.exp(-tau / 0.75) * 0.045 * post
    L += stab; R += stab
    # rhythmic pulse + hats after the hit
    for tb in np.arange(3.0, 6.45, 0.5):
        tt = np.clip(t - tb, 0, None); m = (t >= tb).astype(np.float64)
        pulse = np.sin(2 * np.pi * (52 + 40 * np.exp(-tt / 0.03)) * tt) * np.exp(-tt / 0.14) * 0.30 * m
        L += pulse; R += pulse
        th = np.clip(t - (tb + 0.25), 0, None); mh = (t >= tb + 0.25).astype(np.float64)
        hat = np.diff(g.standard_normal(N), prepend=0) * np.exp(-th / 0.03) * 0.05 * mh
        L += hat; R += np.roll(hat, 60)
    # outro whoosh
    mo = ((t >= 6.4) & (t <= 7.0)).astype(np.float64)
    env = np.sin(np.pi * np.clip((t - 6.4) / 0.6, 0, 1)) ** 1.5
    wo = np.convolve(g.standard_normal(N), np.ones(10) / 10, mode="same") * env * 0.22 * mo
    L += wo; R += np.roll(wo, 90)
    mix = np.stack([L, R])
    mix = np.tanh(1.5 * mix) / np.tanh(1.5)
    mix *= 0.78 / max(1e-6, np.abs(mix).max())
    mix[:, -int(SR * 0.03):] *= np.linspace(1, 0, int(SR * 0.03))
    pcm = (mix.T * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


def main():
    wav = f"{OUT}/intro-sound.wav"
    build_audio(wav)
    mp4 = f"{OUT}/ai-news-this-week-intro.mp4"
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
         "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", mp4], stdin=subprocess.PIPE)
    for i in range(NF):
        ff.stdin.write(compose(i / FPS).tobytes())
    ff.stdin.close(); ff.wait()
    Image.fromarray(compose(4.9)).save(f"{OUT}/ai-news-this-week-title-card.png")
    print("done", mp4)


if __name__ == "__main__":
    main()
