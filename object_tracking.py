#Object Tracking using Meanshift Algo.
#The idea behind this algo is to move small window to get the high 
#density pixels same as histogram backprojection.

#Steps to use this algo-----
#First setup target and find its histogram for backproject the traget.
#ALso set one initial location
#setup the termination criteria

import cv2 as c
import numpy as np

cap=c.VideoCapture(r"C:\Users\rhars\open_cv\data\test2.mp4")
'''
ret,frame=cap.read()
x,y,width,height=580, 30, 80,150
track=(x,y,width,height)
roi=frame[y:y+height,x:x+width]
hsv=c.cvtColor(roi, c.COLOR_BGR2HSV)

mask=c.inRange(hsv,np.array((0.,60.,32.)),np.array((180.,255.,255.)))
hist=c.calcHist([hsv], [0], mask, [180], [0,180])
c.normalize(hist,hist,0,255,c.NORM_MINMAX)

#termination
termntn=(c.TERM_CRITERIA_EPS|c.TERM_CRITERIA_COUNT,10,1)
c.imshow("roi",roi)

while True:
    ret,frame=cap.read()
    if ret==True:
        hsv_vid=c.cvtColor(frame, c.COLOR_BGR2HSV)
        dst=c.calcBackProject([hsv_vid], [0], hist, [0,180], 1)
        ret,track=c.meanShift(dst, track, termntn)
        x,y,w,h=track
        final=c.rectangle(frame, (x,y),(x+w,y+h), (0,0,255),3)
        
        #c.imshow("original",frame)
        frame=c.resize(final,(600,600))
        c.imshow("final",frame)
        if c.waitKey(60)==ord("s"):
            break
    else:
        break
    
cap.release()
c.destroyAllWindows()
'''
#There are few disadvantages of this algo
#Fixe of target window should not be changed.
#to manuaaly pass roi and then detect our target




#CAMshift (Continuously Adaptive Meanshift)
rat,frame=cap.read()
x,y,width,height=580, 30, 80,150
track=(x,y,width,height)


roi=frame[y:y+height,x:x+width]
hsv_roi=c.cvtColor(roi, c.COLOR_BGR2HSV)
mask=c.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180.,255.,255.)))
hist=c.calcHist([hsv_roi], [0], mask, [180], (0,180))
c.normalize(hist,hist,0,255, c.NORM_MINMAX)

term=(c.TERM_CRITERIA_EPS|c.TERM_CRITERIA_COUNT,10,1)

while True:
    rat,frame=cap.read()
    if rat==True:
        hsv=c.cvtColor(frame, c.COLOR_BGR2HSV)
        dst=c.calcBackProject([hsv], [0], hist, [0,180], 1)

        ret,track=c.CamShift(dst, track, term)
        
        #x,y,w,h=track
        #final=c.rectangle(frame, (x,y),(x+w,y+h), (0,0,255),3)
        pts=c.boxPoints(ret)
        pts=np.int64(pts)
        final=c.polylines(frame, [pts], True, (2500,0,0),2)
    
    
        frame=c.resize(final,(600,400))
        c.imshow("image",frame)
        if c.waitKey(25)==ord("s"):
            break

cap.release()
c.destroyAllWindows()
