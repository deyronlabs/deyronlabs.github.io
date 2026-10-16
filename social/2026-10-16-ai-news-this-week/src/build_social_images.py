#!/usr/bin/env python3
"""Social images for AI News This Week. Usage: python3 -I build_social_images.py (run from the episode folder)."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np
FD="/usr/share/fonts/opentype/inter/"; XB=FD+"Inter-ExtraBold.otf"; SB=FD+"Inter-SemiBold.otf"
NAVY=(10,14,30); CYAN=(34,211,238); AMBER=(245,158,11); GREEN=(34,197,94)
f=lambda p,s: ImageFont.truetype(p,s)
def bg(W,H):
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32); rr=np.sqrt(((xx-W/2)/W)**2+((yy-H/2)/H)**2)
    a=np.array(NAVY,np.float32)[None,None,:]*np.clip(1.45-1.7*rr,.35,1.45)[...,None]; a[...,2]+=14*np.clip(.6-rr*1.2,0,1)
    a[(yy%60<2)&(xx%60<2)]+=22
    return Image.fromarray(np.clip(a,0,255).astype(np.uint8))
# 1280x720 (X) and 1200x627 (LinkedIn) from the 1920x1080 cover
cov=Image.open("cover-ai-news-this-week-2026-10-16-1920x1080.png").convert("RGB")
cov.resize((1280,720),Image.LANCZOS).save("x-1280x720.png")
cov.crop((0,40,1920,1040)).resize((1200,627),Image.LANCZOS).save("linkedin-1200x627.png")
# Pinterest 1000x1500
W,H=1000,1500; im=bg(W,H); d=ImageDraw.Draw(im,"RGBA")
d.text((70,80),"DEYRON LABS",font=f(XB,38),fill=(255,255,255)); d.text((W-70,86),"FRI 16 OCT 2026",font=f(SB,28),fill=(178,190,214),anchor="ra")
d.text((70,210),"AI NEWS",font=f(XB,185),fill=(255,255,255)); d.text((70,410),"THIS WEEK",font=f(XB,150),fill=CYAN)
items=[("META","Muse Wonder (closed) + Muse Spark Open (816B weights)",CYAN),("GOOGLE","Gemini 4 Argon GA · price doubles 1 Dec",AMBER),("xAI","Grok Voice 3.0 at $0.08/min",GREEN),("ANTHROPIC","Says defenses cut distillation 90–99%",CYAN),("OPEN MODELS","Liquid LFM2.5 · Timestral · Xiaomi MiMo",AMBER)]
y=680
for k,t,c in items:
    d.rounded_rectangle((70,y,W-70,y+128),18,fill=(20,28,56,235),outline=c+(255,),width=3); d.rectangle((70,y+16,80,y+112),fill=c)
    d.text((105,y+36),k,font=f(XB,40),fill=c,anchor="lm")
    d.text((105,y+88),t,font=f(SB,28),fill=(222,230,246),anchor="lm"); y+=150
d.text((W/2,1450),"deyronlabs.com",font=f(SB,30),fill=(178,190,214),anchor="mm")
im.save("pinterest-1000x1500.png")
