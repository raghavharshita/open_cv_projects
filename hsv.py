#HSV: hue saturation value
import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\color_balls.jpg")
while True:
    hsv=c.cvtColor(img,c.COLOR_BGR2HSV)
    u_v=np.array([32,246,250])
    l_v=np.array([19,133,135])
    mask=c.inRange(hsv, l_v, u_v)
    
    #filter img by mask
    res=c.bitwise_and(img,img,mask=mask)
    
    c.imshow("img",img)
    c.imshow("mask",mask)
    c.imshow("res",res)
    if c.waitKey(1)==ord("s"):
        break




c.destroyAllWindows()