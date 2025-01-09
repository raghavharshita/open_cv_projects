import cv2
cap=cv2.VideoCapture(0)#for external cam use 1
#DIVX XVID MJPG X264 WMV1 WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID")
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
output = cv2.VideoWriter(r"C:\Users\rhars\Documents\output.avi", fourcc, 20.0, (frame_width, frame_height))#for gray scle frame i am to send 0
print("cap",cap)
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(frame)#and write it with gray
        if cv2.waitKey(1)==ord("s"):
            break
        
        
cap.release()
output.release()
cv2.destroyAllWindows()