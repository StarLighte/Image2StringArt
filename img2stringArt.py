import math
import numpy as np
from PIL import Image,ImageDraw

def sign(x):
	if x>0:
		return 1
	elif x<0:
		return -1
	else: return 0
	
def bresenham(p1,p2):
	x1,y1=p1
	x2,y2=p2
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	l=[]
	if dx==0:
		y=min(y1,y2)
		while y<(max(y1,y2)-1):
			y=y+1
			l.append([x1,y])
		return l
	k=dy/float(dx)
	x,y=x1,y1
	if k>1:
		dx,dy=dy,dx
		x,y=y,x
		x1,y1=y1,x1
		x2,y2=y2,x2
	p=2*dy-dx
	for param in range(2,dx+1):
		if p>0:
			y+=sign(y2-y)
			p+=2*(dy-dx)
		else:
			p+=2*dy
		x+=sign(x2-x)
		if k<=1:
			l.append([x,y])
		else:
			l.append([y,x])
	return l

def lamTable(f,inix,finalx,dx=1):
	l=[]
	x=inix
	if (sign(finalx-inix)*sign(dx))<0:
		return "error"
	while abs(x-inix)<=abs(finalx-inix):
		l.append(f(x))
		x+=dx
	return l


def nails(shape,n=1,placeType="square"):
	width,height=shape
	if placeType=="circle":
		r=0.45*min(width,height)
		f=lambda x:[round(width/2+r*math.sin(2*math.pi*x/360)),round(height/2+r*math.cos(2*math.pi*x/360))]
		l=lamTable(f,n,360,n)
	elif placeType=="square":
		l=[]
		x,y=1,1
		while x<width:
			l.append([x-1,y-1])
			x+=n
		x=width
		while y<height:
			l.append([x-1,y-1])
			y+=n
		y=height
		while x>1:
			l.append([x-1,y-1])
			x-=n
		x=1
		while y>1:
			l.append([x-1,y-1])
			y-=n
	return l
	
def measure(array,p_initial,p_final):
	score=0
	number=0
	for p in bresenham(p_initial,p_final):
		number+=1
		score+=array[p[0]][p[1]]
	if number==0 :
		return 255
	else:
		return score/number
		
def importImg(image_path,plotsize=128):
	img=Image.open(image_path)
	img=img.convert("L")
	w,h=img.size
	hnew=int(plotsize*h/w)
	img=img.resize((plotsize,hnew))
	img=np.pad(np.asarray(img),pad_width=1,mode="constant",constant_values=25500)
	return img
	

