#!/usr/bin/env python3
"""Builds the Hell pack: public-domain paintings (see Hell/CREDITS.md, downloaded
into ./src/) → 16-colour pixel hell with 4×4 Bayer dithering, ×4 without smoothing,
written to ./out/. Needs numpy and Pillow.
"""
import numpy as np
from PIL import Image, ImageEnhance
PAL = ["#07020a","#16040a","#2a060e","#420a12","#5e1014","#7e1612","#a02212","#c23a14",
       "#de5a1c","#f07e2a","#fca444","#ffcc6a","#fff0b0","#1e0a1c","#3a1030","#5e1c40"]
P = np.array([[int(h[i:i+2],16) for i in (1,3,5)] for h in PAL], float)
GRAD = [(0,"#07020a"),(0.25,"#2a060e"),(0.45,"#6e1414"),(0.65,"#c23a14"),(0.82,"#f58a30"),(1,"#fff0b0")]
def gradmap(l):
    stops=[(p,np.array([int(h[i:i+2],16) for i in (1,3,5)],float)) for p,h in GRAD]
    out=np.zeros(l.shape+(3,))
    for (p0,c0),(p1,c1) in zip(stops,stops[1:]):
        m=(l>=p0)&(l<=p1); t=((l-p0)/(p1-p0))[...,None]
        out[m]=(c0+(c1-c0)*t)[m]
    return out
B4=np.array([[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]])/16-0.5
def pixel(src, box, size, mix=0.45, spread=28, contrast=1.15, out=None, scale=4, gamma=1.0):
    im=Image.open(src).convert("RGB").crop(box)
    im=ImageEnhance.Contrast(im).enhance(contrast)
    im=im.resize(size, Image.LANCZOS)
    a=np.asarray(im,float)
    lum=((0.3*a[...,0]+0.55*a[...,1]+0.15*a[...,2])/255)**gamma
    a=a*(1-mix)+gradmap(lum)*mix
    h,w,_=a.shape
    a=a+np.tile(B4,(h//4+1,w//4+1))[:h,:w,None]*spread
    d=((a[:,:,None,:]-P[None,None,:,:])**2).sum(-1)
    q=P[d.argmin(-1)].astype(np.uint8)
    Image.fromarray(q).resize((w*scale,h*scale),Image.NEAREST).save(out)
def box169(w,h,cy=0.5,cx=0.5,portrait=False):
    r = 9/16 if portrait else 16/9
    if w/h > r: bw,bh = int(h*r),h
    else: bw,bh = w,int(w/r)
    x=int((w-bw)*cx); y=int((h-bh)*cy)
    return (x,y,x+bw,y+bh)
L=(480,270); Pt=(270,480)
jobs=[
 ("src/pandemonium.jpg","hell-pandemonium.png",box169(1203,800,0.6),L,0.35),
 ("src/great-day.jpg","hell-great-day.png",box169(3136,2023,0.45),L,0.5),
 ("src/martin-002.jpg","hell-fallen-city.png",box169(1536,1267,0.55),L,0.3),
 ("src/pompeii.jpg","hell-ash-and-fire.png",box169(2012,1252,0.5),L,0.4),
 ("src/dore-lucifer.jpg","hell-lucifer.png",box169(3779,3068,0.05),L,1.0),
 ("src/dore-lucifer.jpg","hell-lucifer-portrait.png",box169(3779,3068,0,0.47,True),Pt,1.0),
 ("src/bosch-hell.jpg","hell-bosch-portrait.png",box169(1778,4324,0.0,0.5,True),Pt,0.4),
]
import sys
for src,out,box,size,mix in jobs:
    pixel(src,box,size,mix=mix,out="out/"+out, gamma=1.9 if "lucifer" in out else 1.0)
    print(out)
