#GrabCut Algoritm with the help of this algoritm we easily
#cutoff any foreground object from image or video.
#It works like a rectangle portion mark on the image
#and area outise the rectangle is treat as a extra part
#so this algo remove it completely.
#Gaussian mixtuere model help to achieve the target

import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\car.jpg")
img=c.resize(img,(800,800))
mask=np.zeros(img.shape[:2],np.uint8)
bck=np.zeros((1,65),np.float64)
fwd=np.zeros((1,65),np.float64)
rect=(146,162,639,760)
c.grabCut(img, mask, rect, bck, fwd, 5,c.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]

c.imshow("car",img)
c.waitKey()
c.destroyAllWindows()