from PIL import Image, ImageDraw, ImageFont
import sys
out = sys.argv[1]
W,H=1280,720
im=Image.new("RGB",(W,H),"#1a1a1a"); d=ImageDraw.Draw(im)
F="/usr/share/fonts/opentype/inter/Inter-%s.otf"
f=lambda w,s: ImageFont.truetype(F%w,s)
d.rectangle([0,0,12,H],fill="#22c55e")
d.text((70,60),"DEYRON LABS  ·  AI NEWS",font=f("Bold",26),fill="#86efac")
d.text((70,140),"NVIDIA Nemotron 3.5",font=f("Bold",70),fill="white")
d.text((70,225),"Super VL and Bolt open models",font=f("Bold",46),fill="#22c55e")
rows=[("120B","Super VL (open weights)"),("74B-A9B","Bolt, 2-bit, fits 24GB"),("Oct 23","Bolt E4B (4GB) arrives")]
x=70
for big,small in rows:
    d.rounded_rectangle([x,340,x+360,540],radius=16,fill="#242424",outline="#15803d",width=3)
    d.text((x+24,370),big,font=f("Bold",60),fill="white")
    d.text((x+24,460),small,font=f("Regular",26),fill="#d4d4d4")
    x+=385
d.text((70,600),"Specs and rankings are NVIDIA's own; license not stated in the post",font=f("Regular",28),fill="#f59e0b")
d.text((70,650),"deyronlabs.com",font=f("Bold",24),fill="#86efac")
im.convert("RGB").save(out,quality=92)
