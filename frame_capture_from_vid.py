import cv2 as c
cap=c.VideoCapture(r"C:\Users\rhars\open_cv\data\vaishnavi_dance.mp4")
ret,image=cap.read()
count=0
while True:
    if ret==True:
        c.imwrite(r"C:\Users\rhars\open_cv\project_2 output\imgN%d.jpg"%count,image)
        #cap.set(c.CAP_PROP_POS_MSEC,(count**100))
        ret,image=cap.read()
        c.imshow("res",image)
        print(count)
        count+=1
        if c.waitKey(1)==ord("s"):
            break
        
cap.release()
c.destroyAllWindows()