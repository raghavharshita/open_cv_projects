import cv2 as c
import datetime
## can pass all the drawing fxn on frames
cap=c.VideoCapture(0)
width=cap.get(c.CAP_PROP_FRAME_WIDTH)
height=cap.get(c.CAP_PROP_FRAME_HEIGHT)
print("width : ",cap.get(3))
print("height : ",cap.get(4))
while cap.isOpened():
    ret,frames=cap.read()
    frames=c.resize(frames,(700,500))
    if ret==True:
        font=c.FONT_HERSHEY_COMPLEX_SMALL
        text="HEIGHT : "+str(cap.get(4))+ "  WIDTH : "+str(cap.get(3))
        frames=c.putText(frames, text,(10,20),font,1,(1,39,215),1,c.LINE_AA)
        date_date="DATE : "+str(datetime.datetime.now())
        frames=c.putText(frames,date_date,(20,50),font,1,(100,150,42),1,c.LINE_AA)
        c.imshow("res",frames)
        if c.waitKey(30)==ord("s"):
            break
        
cap.release()
c.destroyAllWindows()