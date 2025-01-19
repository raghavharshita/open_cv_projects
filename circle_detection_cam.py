import cv2 as c
import numpy as np

#img=c.imread(r"C:\Users\rhars\open_cv\data\col_balls.jpg")
'''
img2=img.copy()
gray=c.cvtColor(img, c.COLOR_BGR2GRAY)
gray=c.medianBlur(gray, 5)
#param1>param2
circles=c.HoughCircles(gray, c.HOUGH_GRADIENT, 1, 20,param1=50,param2=30,
                       minRadius=0,maxRadius=0)
if circles is not None:
    data=np.uint16(np.around(circles))
    for circle in data[0, :]:  
        x, y, r = circle      
        c.circle(img2, (x, y), r, (50, 10, 50), 2)
        c.circle(img2, (x, y), 2, (0, 255, 100), -1)

c.imshow("result",img2)
c.imshow("gray",gray)
c.waitKey()
c.destroyAllWindows()
'''

#video cam
cap=c.VideoCapture(0)
while True:
    _,img=cap.read()
    img2=img.copy()
    gray=c.cvtColor(img2, c.COLOR_BGR2GRAY)
    gray=c.medianBlur(gray, 5)
    circles=c.HoughCircles(gray,c.HOUGH_GRADIENT, 1, 10,param1=50,param2=30,
                           minRadius=0,maxRadius=0)
    if circles is not None:
        data=np.uint16(np.around(circles))
        for (x,y,r) in data[0,:]:
            c.circle(img2, (x,y), r, (50,10,50),3)
            c.circle(img2, (x,y), 2, (0,255,0),-1)
            
            
    c.imshow("result",img2)
    if c.waitKey(25)==ord("s"):
        break
cap.release()
c.destroyAllWindows()
            
            
            
            
            

