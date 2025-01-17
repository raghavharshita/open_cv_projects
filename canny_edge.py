#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.
#It is use  multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
# 1) -  NOise reduction(gauss)), 2) -Gradient calculation( ,
# 3) - Non-maximum suppresson, 4) - Double Threshold,
# 5) - Edge Tracking by Hysteresis 

import cv2 as c
import numpy as np


img=c.imread(r"C:/Users/rhars/open_cv/data/building.jpg")
img=c.resize(img,(600,600))
img_gry=c.cvtColor(img,c.COLOR_BGR2GRAY)
"""
canny=c.Canny(img_gry,40, 100)

c.imshow("gray image",img_gry)
c.imshow("canny",canny)
c.waitKey()
c.destroyAllWindows()
"""
def nothing():
    pass

c.namedWindow(winname="canny")
c.createTrackbar("threshold", "canny", 0, 255, nothing)

while True:
    track=c.getTrackbarPos("threshold", "canny")
    print(track)
    res=c.Canny(img_gry,track, 255)
    c.imshow("canny",res)
    if c.waitKey(1)==ord("s"):
        break
    
c.destroyAllWindows()