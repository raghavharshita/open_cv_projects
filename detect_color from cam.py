#detection using webcam and trackbar
import cv2 as c
import numpy as np

cap=c.VideoCapture(0)
def nothing(x):
    pass

c.namedWindow("color_adjustment")
c.createTrackbar("lower-h", "color_adjustment", 0, 255, nothing)
c.createTrackbar("lower-s", "color_adjustment", 0, 255, nothing)
c.createTrackbar("lower-v", "color_adjustment", 0, 255, nothing)

c.createTrackbar("higher-h", "color_adjustment", 255, 255, nothing)
c.createTrackbar("higher-s", "color_adjustment", 255, 255, nothing)
c.createTrackbar("higher-v", "color_adjustment", 255, 255, nothing)

while True:
    _,frame=cap.read()
    frame=c.resize(frame,(400,400))
    hsv=c.cvtColor(frame,c.COLOR_BGR2HSV)
    l_h=c.getTrackbarPos("lower-h", "color_adjustment")
    l_s=c.getTrackbarPos("lower-s", "color_adjustment")
    l_v=c.getTrackbarPos("lower-v", "color_adjustment")
    u_h=c.getTrackbarPos("higher-h", "color_adjustment")
    u_s=c.getTrackbarPos("higher-s", "color_adjustment")
    u_v=c.getTrackbarPos("higher-v", "color_adjustment")
    
    lower_bound=np.array([l_h,l_s,l_v])
    upper_bound=np.array([u_h,u_s,u_v])
    
    mask=c.inRange(frame,lower_bound,upper_bound)
    res=c.bitwise_and(frame, frame,mask=mask)
    c.imshow("original_frame",frame)
    c.imshow("mask",mask)
    c.imshow("res",res)

    if c.waitKey(1)==ord("s"):
        break
    
c.destroyAllWindows()

        