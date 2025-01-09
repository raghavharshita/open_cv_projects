import cv2
cap=cv2.VideoCapture(r"C:\Users\rhars\OneDrive\Documents\vaishnavi_dance.mp4")
print("cap",cap)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(700,450))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k=cv2.waitKey(25)#the value in waitkey will fast or slow the video
    
    if k==ord("s") & 0xFF:
        break
    
cap.release()
cv2.destroyAllWindows()