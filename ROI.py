import cv2 as c
import numpy as np
# one way of finding the coordinates of the image points
img=c.imread(r"C:\Users\rhars\open_cv\data\roi_opr.jpg")
img=c.resize(img,(800,800))
'''l=[]
def draw(event,x,y,flag,params):
    if event==c.EVENT_LBUTTONDOWN:
        l.append((x,y))
        st="."+str(x)+","+str(y)
        font=c.FONT_HERSHEY_PLAIN
        c.putText(img, st, (x,y), font,1, (201,127,5))
    
# ROI--> region of interest
c.namedWindow(winname="result")
c.setMouseCallback("result", draw)
while True:
    c.imshow("result",img)
    if c.waitKey(1)==ord("s"):
        break
    
print(l)
c.destroyAllWindows()
'''
#(328,56)(433,193)
#[(y1:y2),(x1:x2)]
roi=img[50:205,320:440]
#x=105 y=137
#img[56:193,434:539]=roi
#img[56:193,540:645]=roi
#img[56:193,222:327]=roi
#img[56:193,116:221]=roi

ironman=c.imread(r"C:\Users\rhars\open_cv\data\ironman.jpg")
ironman=c.resize(ironman,(900,600))
#(495,3)
ironman[1:156,560:680]=roi

c.imshow("original",ironman)
c.waitKey()
c.destroyAllWindows()