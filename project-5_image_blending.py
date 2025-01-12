# image blending project 

import cv2 as c
import numpy as np

img1=c.imread(r"C:\Users\rhars\open_cv\data\roi_opr.jpg")
img1=c.resize(img1,(500,700))
img2=c.imread(r"C:\Users\rhars\open_cv\data\bro_thor.jpg")
img2=c.resize(img2,(500,700))
#c.imshow("thorrr-->",img1)
#c.imshow("bro_thorrr->",img2)
def blend(x):
    pass

img=np.zeros((400,400,3),np.uint8)
c.namedWindow(winname="win")
switch="OFF:0 \n ON:1"
c.createTrackbar(switch, "win", 0, 1, blend)
c.createTrackbar("alpha", "win", 1, 100, blend)

while True:
    s=c.getTrackbarPos(switch, "win")
    a=c.getTrackbarPos("alpha", "win")
    n=float(a/100)
    
    if s==0:
        dst=img[:]
    else:
        dst=c.addWeighted(img1,n, img2, 1-n, 0)
        font=c.FONT_HERSHEY_COMPLEX
        c.putText(dst,str(a),(20,50),font,1,(23,12,105),2)
    c.imshow("blended_image ",dst)
    if c.waitKey(1)==ord("s"):
        break

c.destroyAllWindows()