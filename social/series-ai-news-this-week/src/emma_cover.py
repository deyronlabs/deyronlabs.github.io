import os, sys, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FD="/usr/share/fonts/opentype/inter/"; XB=FD+"Inter-ExtraBold.otf"; SB=FD+"Inter-SemiBold.otf"
W,H=1920,1080; NAVY=(10,14,30); CYAN=(34,211,238); AMBER=(245,158,11); GREEN=(34,197,94)
FRAME,OUT=sys.argv[1],sys.argv[2]
DATE=os.environ.get("DATE","FRI 6 NOV"); TOPS=os.environ.get("TOPS","GPT-6 CYBER|SIRI AI|INKLING 2").split("|")
yy,xx=np.mgrid[0:H,0:W].astype(np.float32); rr=np.sqrt(((xx-W*0.74)/W)**2+((yy-H/2)/H)**2)
bg=np.array(NAVY,np.float32)[None,None,:]*np.clip(1.6-1.9*rr,0.35,1.6)[...,None]; bg[...,2]+=18*np.clip(.6-rr*1.2,0,1)
bg[(yy%60<2)&(xx%60<2)]+=22
img=Image.fromarray(np.clip(bg,0,255).astype(np.uint8)).convert("RGBA")
# Emma keyed
f=np.array(Image.open(FRAME).convert("RGB")).astype(np.float32)
R,G,B=f[...,0],f[...,1],f[...,2]; gd=G-np.maximum(R,B)
a=np.clip(1-(gd-8)/70,0,1)
h,w=a.shape; p=np.pad(a,1,mode="edge"); a=np.min([p[i:i+h,j:j+w] for i in range(3) for j in range(3)],axis=0)
f[...,1]=np.where(gd>0,np.maximum(R,B),G)
a=np.array(Image.fromarray((a*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1))).astype(np.float32)/255
em=Image.fromarray(np.dstack([f,a*255]).astype(np.uint8),"RGBA")
S=1.02; em=em.resize((int(w*S),int(h*S)),Image.LANCZOS)
ex=int(W*0.745-em.width/2); ey=H-em.height+50
# soft spotlight behind Emma + contact shadow (no outline)
sp=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sp)
cx=int(W*0.745); sd.ellipse((cx-520,80,cx+520,1160),fill=(40,92,140,120)); sp=sp.filter(ImageFilter.GaussianBlur(120)); img.alpha_composite(sp)
sh=em.split()[3].filter(ImageFilter.GaussianBlur(30)); shadow=Image.new("RGBA",em.size,(0,0,0,0)); shadow.putalpha(sh.point(lambda v:int(v*0.5)))
img.alpha_composite(shadow,(ex-30,ey+10)); img.alpha_composite(em,(ex,ey))
d=ImageDraw.Draw(img,"RGBA"); ft=lambda p,s: ImageFont.truetype(p,s)
d.text((90,70),"DEYRON LABS",font=ft(XB,40),fill=(255,255,255))
d.text((90,200),"AI NEWS",font=ft(XB,215),fill=(255,255,255))
d.text((90,430),"THIS WEEK",font=ft(XB,142),fill=CYAN)
d.text((96,640),DATE,font=ft(SB,44),fill=(178,190,214))
x=90; y=740
for i,t in enumerate(TOPS):
    c=[CYAN,AMBER,GREEN][i%3]; fn=ft(XB,52); tw=d.textlength(t,font=fn)+66
    d.rounded_rectangle((x,y,x+tw,y+90),16,fill=(20,28,56,240),outline=c+(255,),width=4)
    d.rectangle((x,y+14,x+9,y+76),fill=c); d.text((x+36,y+45),t,font=fn,fill=c,anchor="lm"); x+=tw+22
img.convert("RGB").save(OUT)
