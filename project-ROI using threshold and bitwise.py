import cv2 as c
import numpy as np
#img1=c.imread(r"C:\Users\rhars\open_cv\data\hero1.jpg")
#img2=c.imread(r"C:\Users\rhars\open_cv\data\strom_breaker.JPG")
"""

img1=c.resize(img1,(1024,650))
img2=c.resize(img2,(600,650))
# data
row,col,ch=img2.shape
print(row,col,ch)
roi=img1[0:row,0:col]

img2_gray=c.cvtColor(img2,c.COLOR_BGR2GRAY)
_,mask=c.threshold(img2_gray, 50, 255, c.THRESH_BINARY)
mask_inv=c.bitwise_not(mask)
img1_bg=c.bitwise_and(roi, roi,mask=mask_inv)

img2_fg=c.bitwise_and(img2, img2,mask=mask)
res=c.add(img1_bg,img2_fg)

img1[0:row,0:col]=res



#c.imshow("thorr",img1)
c.imshow("strom_breaker",img2)
#c.imshow("roi",roi)
c.imshow("gray",img2_gray)
c.imshow("mask",mask)
c.imshow("strom",img2_fg)
c.imshow("mask_inv",mask_inv)
c.imshow("img1_bg",img1_bg)
c.imshow("result",res)
c.imshow("final",img1)
c.waitKey()
c.destroyAllWindows()
"""
img1=c.imread(r"C:\Users\rhars\open_cv\data\hero2.jpg")
img2=c.imread(r"C:\Users\rhars\open_cv\data\hero1.jpg")
img1=c.resize(img1,(1024,650))
img2=c.resize(img2,(600,650))
row,col,ch=img2.shape

roi=img1[0:row,0:col]
img2_gray=c.cvtColor(img2, c.COLOR_BGR2GRAY)
_,mask=c.threshold(img2_gray, 50, 255, c.THRESH_BINARY)
img2_fg=c.bitwise_and(img2, img2,mask=mask)
mask_inv=c.bitwise_not(mask)
img1_bg=c.bitwise_and(roi, roi,mask=mask_inv)
res=c.add(img1_bg,img2_fg)
img1[0:row,0:col]=res

c.imshow("result",img1)
c.waitKey()
c.destroyAllWindows()
