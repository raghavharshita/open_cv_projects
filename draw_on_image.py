## drawing on the image
import numpy as np
import cv2 as c

#img=c.imread(r"C:\Users\rhars\open_cv\data\thor.jpg")
#img=c.resize(img,(600,700))
img=np.zeros([512,512,3],np.uint8)*255# black color
img=np.ones([512,512,3],np.uint8)*255 # white color
## drawing line
img=c.line(img,(0,0),(200,200),(3,186,124),8)
## drawing arrowed line
img=c.arrowedLine(img,(200,200),(500,500),(3,186,252),8)
## draw rectangle
img=c.rectangle(img,(0,0),(500,500),(252,206,3),8)# if i take thickness to be - , the fig will get filled
## draw circle
img=c.circle(img,(447,125),63,(3,252,49),-8)
## putting text
font=c.FONT_ITALIC
img=c.putText(img,'Thor',(20,500),font,4,(196,186,124),10,c.LINE_AA)
## draw ellipse
img=c.ellipse(img,(400,600),(100,50),0,0,185,155,5)
c.imshow("res",img)
c.waitKey(0)
c.destroyAllWindows()