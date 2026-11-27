import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import emma_ticker as ET
import subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
CLIP, LOGO, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
FD="/usr/share/fonts/opentype/inter/"
def font(w,s): return ImageFont.truetype(FD+f"Inter-{w}.otf",s)
W,H=1920,1080
bg=Image.new("RGB",(W,H),"#0b1220"); d=ImageDraw.Draw(bg)
for y in range(H):
    t=y/H; d.line([(0,y),(W,y)],fill=(int(11+14*t),int(18+22*t),int(32+36*t)))
for i in range(-6,14): d.line([(W*0.5+i*160,H*0.62),(W*0.5+i*420-1200,H)],fill=(20,52,70),width=2)
for k in range(8):
    y=H*0.62+(k**1.8)*14; d.line([(0,y),(W,y)],fill=(18,44,60),width=2)
COVER=sys.argv[4]
sx0,sy0,sx1,sy1=1010,200,1850,673   # 840x473 = 16:9
glow=Image.new("RGB",(W,H),(0,0,0)); gd=ImageDraw.Draw(glow)
gd.rounded_rectangle([sx0-25,sy0-25,sx1+25,sy1+25],radius=30,fill=(10,90,110)); glow=glow.filter(ImageFilter.GaussianBlur(45))
bg=Image.blend(bg,Image.composite(glow,bg,glow.convert("L")),0.55); d=ImageDraw.Draw(bg)
d.rounded_rectangle([sx0-14,sy0-14,sx1+14,sy1+14],radius=22,fill="#0a1424",outline="#22c55e",width=4)
cv=Image.open(COVER).convert("RGB").resize((sx1-sx0,sy1-sy0),Image.LANCZOS); bg.paste(cv,(sx0,sy0))
# monitor stand
d.rectangle([(sx0+sx1)//2-12,sy1+14,(sx0+sx1)//2+12,sy1+70],fill="#16263f")
d.rounded_rectangle([(sx0+sx1)//2-120,sy1+66,(sx0+sx1)//2+120,sy1+80],radius=6,fill="#16263f")
bg.save(f"{OUT}/studio-bg3.png")
desk=Image.new("RGBA",(W,H),(0,0,0,0)); dd=ImageDraw.Draw(desk)
dd.rectangle([0,H-160,W,H],fill=(15,29,51,255))
dd.line([(0,H-160),(W,H-160)],fill=(34,197,94,255),width=4)
dd.text((60,H-52),"AI-generated presenter and voice",font=font("Regular",28),fill=(154,154,154,255))
desk.save(f"{OUT}/desk-overlay2.png")
DISC=ET.disclosure_overlay(); SID=0 if 'cover' in sys.argv[0] else 12
bgA=np.array(bg).astype(np.float32); deskA=np.array(desk).astype(np.float32)
PW,PH,PX,PY=1632,918,-240,162
rd=subprocess.Popen(["ffmpeg","-v","error","-i",CLIP,"-vf",f"crop=1920:1080:0:0,scale={PW}:{PH},fps=30","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
out=f"{OUT}/intro-emma-cover.mp4"
wr=subprocess.Popen(["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r","30","-i","-","-i",CLIP,
    "-map","0:v","-map","1:a","-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",out],stdin=subprocess.PIPE)
n=0
while True:
    buf=rd.stdout.read(PW*PH*3)
    if len(buf)<PW*PH*3: break
    f=np.frombuffer(buf,dtype=np.uint8).reshape(PH,PW,3).astype(np.float32)
    R,G,B=f[...,0],f[...,1],f[...,2]
    gd_=G-np.maximum(R,B)
    alpha=np.clip(1-(gd_-8)/70,0,1)
    # erode alpha by 1px (3x3 min)
    p=np.pad(alpha,1,mode="edge"); stack=[p[i:i+PH,j:j+PW] for i in range(3) for j in range(3)]
    alpha=np.min(stack,axis=0)
    # despill: clamp green only where green dominates
    G2=np.where(gd_>0,np.maximum(R,B),G); f[...,1]=G2
    frame=bgA.copy()
    x0,y0=PX,PY; sx=max(0,-x0); dx=max(0,x0); w=min(PW-sx,W-dx); h=min(PH,H-y0)
    reg=frame[y0:y0+h,dx:dx+w]; a=alpha[:h,sx:sx+w,None]
    frame[y0:y0+h,dx:dx+w]=f[:h,sx:sx+w]*a+reg*(1-a)
    da=DISC[...,3:4]/255.0; frame=DISC[...,:3]*da+frame*(1-da)
    frame[990:1080]=ET.ticker_strip(n/30.0,SID)
    try:
        wr.stdin.write(frame.astype(np.uint8).tobytes()); n+=1
    except BrokenPipeError:
        break
try:
    wr.stdin.close()
except BrokenPipeError:
    pass
wr.wait(); print("frames",n)
