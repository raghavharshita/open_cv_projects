# dynamic hsv project
import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\color_balls.jpg")
img=c.resize(img,(600,400))

def track(x):
    pass

c.namedWindow(winname="wind")

c.createTrackbar("lower_h", "wind", 0, 255, track)
c.createTrackbar("lower_s", "wind", 0, 255, track)
c.createTrackbar("lower_v", "wind", 0, 255, track)

c.createTrackbar("upper_h", "wind", 255, 255, track)
c.createTrackbar("upper_s", "wind", 255, 255, track)
c.createTrackbar("upper_v", "wind", 255, 255, track)

while True:
    hsv=c.cvtColor(img,c.COLOR_BGR2HSV)
    l_h=c.getTrackbarPos("lower_h", "wind")
    l_s=c.getTrackbarPos("lower_s", "wind")
    l_v=c.getTrackbarPos("lower_v", "wind")
    
    h_h=c.getTrackbarPos("upper_h", "wind")
    h_s=c.getTrackbarPos("upper_s", "wind")
    h_v=c.getTrackbarPos("upper_v", "wind")
    
    lower_bound=np.array([l_h,l_s,l_v])
    upper_bound=np.array([h_h,h_s,h_v])
    
    mask=c.inRange(hsv,lower_bound,upper_bound)
    
    res=c.bitwise_and(img,img,mask=mask)
    c.imshow("original_frame",img)
    c.imshow("mask",mask)
    c.imshow("result",res)
    
    if c.waitKey(1)==ord("s"):
        break
    
    
c.destroyAllWindows()
    
    
    
    
    
    