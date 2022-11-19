from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import img2stringArt as i2s

learnStep=32

img=i2s.importImg('input/test.jpg',256)
imgdata=img.copy()
imgExport=0*imgdata
nailList=i2s.nails(np.shape(img),4)
maxString=1500
p0=nailList[0]
finalList=[]
for iteration in range(maxString):
	if (iteration%100)==0:
		print(iteration)
	temScore=255
	p1=p0.copy()
	finalList.append(p0)
	nlC=nailList.copy()
	nlC.remove(p1)

	for p in nlC:
		if (i2s.measure(imgdata,p,p1)<temScore) :
			temScore=i2s.measure(imgdata,p,p1)
			p0=p.copy()
	for p in i2s.bresenham(p0,p1):
		if imgdata[p[0]][p[1]]<=255-learnStep :
			imgdata[p[0]][p[1]]+=learnStep
		else:
			imgdata[p[0]][p[1]]=255
		if imgExport[p[0]][p[1]]<=255-learnStep:
			imgExport[p[0]][p[1]]+=learnStep
		else:
			imgExport[p[0]][p[1]]=255
print(finalList)
imgExport=Image.fromarray(255-np.uint8(imgExport),mode="L")
imgExport.save("output/export.png")
imgExport.show()
			

