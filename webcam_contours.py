import cv2 as c
import numpy as np

cap=c.VideoCapture(0)
def nothing(a):
    pass 

c.namedWindow("result",c.WINDOW_NORMAL)
c.resizeWindow("result", (300,300))
c.createTrackbar("thresh", "result", 0, 255, nothing)
#color detection---

c.createTrackbar("lower-h", "result", 0, 255, nothing)
c.createTrackbar("lower-s", "result", 0, 255, nothing)
c.createTrackbar("lower-v", "result", 0, 255, nothing)
c.createTrackbar("upper-h", "result", 255, 255, nothing)
c.createTrackbar("upper-s", "result", 255, 255, nothing)
c.createTrackbar("upper-v", "result", 255, 255, nothing)

while True:
    _,frame=cap.read()
    frame=c.resize(frame,(400,400))
    hsv=c.cvtColor(frame, c.COLOR_BGR2HSV)
    l_h=c.getTrackbarPos("lower-h", "result")
    l_s=c.getTrackbarPos("lower-s", "result")
    l_v=c.getTrackbarPos("lower-v", "result")
    u_h=c.getTrackbarPos("upper-h", "result")
    u_s=c.getTrackbarPos("upper-s", "result")
    u_v=c.getTrackbarPos("upper-v", "result")
    
    lower_bound=np.array([l_h,l_s,l_v])
    upper_bound=np.array([u_h,u_s,u_v])
    
    mask=c.inRange(hsv, lower_bound, upper_bound)
    filtr=c.bitwise_and(frame, frame,mask=mask)
    
    mask1=c.bitwise_not(mask)
    m_g=c.getTrackbarPos("thresh", "result")
    ret,thresh=c.threshold(mask1, m_g, 255, c.THRESH_BINARY)

    d=c.dilate(thresh, (1,1),iterations=6)
    cnt,hier=c.findContours(thresh,c.RETR_TREE,c.CHAIN_APPROX_SIMPLE)
    #frame=c.drawContours(frame, cnt, -1, (176,10,15),4)
    for i in cnt:
        epsilon=0.0001*c.arcLength(i, True)
        data=c.approxPolyDP(i, epsilon, True)
        
        hull=c.convexHull(data)
        c.drawContours(frame, [i], -1, (50,50,150),2)
        c.drawContours(frame, [hull], -1, (0,255,0),2)
    
    
    c.imshow("thresh",d)
    c.imshow("mask",mask)
    c.imshow("filter",filtr)
    c.imshow("frame",frame)
    
    if c.waitKey(25)==ord("s"):
        break
    
cap.release()
c.destroyAllWindows()


    
    
    
    
    
    
    
