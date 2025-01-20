#Background Subtraction is a way to access the foreground objects.
#Technically, you need to extract the moving 
#foreground from static background.
#There are multiple approach for backgroud subtract

#We discuss all of them.

import cv2 as c
import numpy as np

cap=c.VideoCapture(r"C:\Users\rhars\open_cv\data\test2.mp4")
#old_algo = cv.bgsegm.createBackgroundSubtractorMOG() not available now
algo1=c.createBackgroundSubtractorMOG2(detectShadows=True)
algo2=c.createBackgroundSubtractorKNN(detectShadows=True)
while True:
    ret,frame=cap.read()
    frame=c.resize(frame,(600,400))
    res1=algo1.apply(frame)
    res2=algo2.apply(frame)
    c.imshow("original",frame)
    c.imshow("res1",res1)
    c.imshow("res2",res2)
    if c.waitKey(60)==ord("s"):
        break
    
cap.release()
c.destroyAllWindows()