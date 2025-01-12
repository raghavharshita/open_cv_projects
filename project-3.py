# create the function to get the coordinate of the pixel and color of the point
import cv2 as c 
import numpy as np
def draw(event,x,y,flag,params):
    print("x : ",x)
    print("y : ",y)
    print("flag : ",flag)
    print("params : ",params)
    font=c.FONT_HERSHEY_PLAIN
    if event==c.EVENT_LBUTTONDOWN:
        print(x ,",",y)
        cord="."+str(x)+" ,"+str(y)
        c.putText(img, cord, (x,y), font, 1, (15,147,85),2)
        #c.imshow("result",img)
    if event==c.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        s="."+str(b)+", "+str(g)+", "+str(r)
        c.putText(img, s, (x,y), font, 1, (51,204,102),2)      

c.namedWindow(winname="result")
#img=np.zeros([512,512,3],np.uint8)*255
img=c.imread(r"C:\Users\rhars\open_cv\data\thor.jpg")
c.setMouseCallback("result",draw)

while True:
    c.imshow("result",img)
    if c.waitKey(1)==ord("s"):
        break
    
c.destroyAllWindows()