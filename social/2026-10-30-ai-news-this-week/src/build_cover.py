#!/usr/bin/env python3
"""YouTube cover 1920x1080 for AI News This Week episodes. Usage: OUT=cover.png TOPS="A|B|C" python3 -I build_cover.py"""
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
FD="/usr/share/fonts/opentype/inter/"; XB=FD+"Inter-ExtraBold.otf"; SB=FD+"Inter-SemiBold.otf"
W,H=1920,1080; NAVY=(10,14,30); CYAN=(34,211,238); AMBER=(245,158,11); GREEN=(34,197,94)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32); rr=np.sqrt(((xx-W/2)/W)**2+((yy-H/2)/H)**2)
bg=np.array(NAVY,np.float32)[None,None,:]*np.clip(1.45-1.7*rr,0.35,1.45)[...,None]; bg[...,2]+=14*np.clip(.6-rr*1.2,0,1)
bg[(yy%60<2)&(xx%60<2)]+=22
img=Image.fromarray(np.clip(bg,0,255).astype(np.uint8)); d=ImageDraw.Draw(img,"RGBA")
f=lambda p,s: ImageFont.truetype(p,s)
d.text((90,70),"DEYRON LABS",font=f(XB,40),fill=(255,255,255))
d.text((W-90,76),"FRI 30 OCT",font=f(SB,36),fill=(178,190,214),anchor="ra")
d.text((90,170),"AI NEWS",font=f(XB,300),fill=(255,255,255)); 
d.text((90,455),"THIS WEEK",font=f(XB,200),fill=CYAN)
tops=os.environ.get("TOPS","ANTHROPIC IPO|GEMINI 4 CARBON|ARTEX").split("|")
cols=[CYAN,AMBER,GREEN]; x=90; y=780
for i,t in enumerate(tops):
    c=cols[i%3]; fn=f(XB,56); tw=d.textlength(t,font=fn)+70
    d.rounded_rectangle((x,y,x+tw,y+96),16,fill=(20,28,56,235),outline=c+(255,),width=4)
    d.rectangle((x,y+14,x+9,y+82),fill=c); d.text((x+38,y+48),t,font=fn,fill=c,anchor="lm"); x+=tw+24
img.save(os.environ.get("OUT","cover.png"))
