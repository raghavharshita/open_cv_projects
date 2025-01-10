# making color picker

import cv2 as c
import numpy as np

def cross(x):
    pass
img=np.zeros([300,512,3],np.uint8)
c.namedWindow(winname="Color Picker")

#create switch
s1="0:OFF \n 1:ON"
c.createTrackbar(s1, "Color Picker", 0,1,cross)

# create for RGB
c.createTrackbar("R", "Color Picker", 0,255,cross)
c.createTrackbar("G", "Color Picker", 0,255,cross)
c.createTrackbar("B", "Color Picker", 0,255,cross)
 

while True:
    c.imshow("Color Picker",img)
    if c.waitKey(1)==ord("s"):
        break
    
    s=c.getTrackbarPos(s1, "Color Picker")
    r=c.getTrackbarPos("R", "Color Picker")
    g=c.getTrackbarPos("G", "Color Picker")
    b=c.getTrackbarPos("B", "Color Picker")
    
    if s==0:
        img[:]=0
    else:
        img[:]=[r,g,b]
c.destroyAllWindows()