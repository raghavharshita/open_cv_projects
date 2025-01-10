# mouse collab function

import cv2 as c 
import numpy as np
def draw(event,x,y,flag,params):
    print("x : ",x)
    print("y : ",y)
    print("flag : ",flag)
    print("params : ",params)
    if event==c.EVENT_LBUTTONDBLCLK:
        c.circle(img,(x,y),100,(120,0,255),5)
        
    elif event==c.EVENT_RBUTTONDBLCLK:
        c.rectangle(img,(x,y),(x+100,y+75),(2,156,34),5)
        
        
c.namedWindow(winname="result")

img=np.zeros([512,512,3],np.uint8)*255
c.setMouseCallback("result",draw)

while True:
    c.imshow("result",img)
    if c.waitKey(1)==ord("s"):
        break
    
c.destroyAllWindows()