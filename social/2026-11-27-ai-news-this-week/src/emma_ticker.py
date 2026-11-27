import numpy as np
from PIL import Image, ImageDraw, ImageFont
FD="/usr/share/fonts/opentype/inter/"
XB=FD+"Inter-ExtraBold.otf"; SB=FD+"Inter-SemiBold.otf"
W,H=1920,1080
AMBER=(245,158,11); NAVY=(10,14,30)
ITEMS=["DEYRON LABS","AI NEWS THIS WEEK","GLOBAL AI, EVERY FRIDAY"]; GAP=70
_f=ImageFont.truetype(XB,36)
_d=ImageDraw.Draw(Image.new("RGB",(4,4)))
TPOS=[];_x=0
for it in ITEMS: TPOS.append((_x,it)); _x+=int(_d.textlength(it,font=_f))+GAP
TW=_x
def ticker_strip(t,sid=0):
    img=Image.new("RGB",(W,90),AMBER); d=ImageDraw.Draw(img)
    off=int(t*140+sid*311)%TW; k0=-1
    while k0*TW-off<W:
        for px,it in TPOS:
            x=k0*TW+px-off
            if -700<x<W:
                d.text((x,45),it,font=_f,fill=NAVY,anchor="lm")
                tl=int(d.textlength(it,font=_f))
                d.ellipse((x+tl+GAP//2-6,39,x+tl+GAP//2+6,51),fill=NAVY)
        k0+=1
    return np.array(img).astype(np.float32)
def disclosure_overlay():
    """RGBA 1920x1080: right-aligned text just above the ticker band"""
    o=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(o)
    f=ImageFont.truetype(SB,28); t="AI-generated presenter and voice"
    w=d.textlength(t,font=f); x1=W-60; y=940
    d.rounded_rectangle((x1-w-28,y-12,x1+28,y+46),radius=14,fill=(10,14,30,200))
    d.text((x1-w,y),t,font=f,fill=(214,222,238,255))
    return np.array(o).astype(np.float32)
