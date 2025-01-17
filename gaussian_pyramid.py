#Image Pyramids in OpenCV
"""
We use Image Pyramid because somethimes we work on same imge
but different resolution.e.g. searching face, eye in an image
and it vary image to image so in this case we create a set 
of images with diff. resolution which is called pyramid.
We also use these pyramids to blends the images.
"""
#There are two types of Image Pyramid-
# 1) Gaussian Pyramid and 2) Laplacian Pyramids

import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\avengers.jpg")
img=c.resize(img,(700,700))
"""
#Gaussian Pyramid Have 2 function-1) cv2.pyrUp(),2)-cv2.pyrDown()
#pyrdown----
pd1=c.pyrDown(img)
pd2=c.pyrDown(pd1)

#pyrup---
pu1=c.pyrUp(pd2)
pu2=c.pyrUp(pu1)

c.imshow("down",pd1)
c.imshow("down2",pd2)
c.imshow("original",img)
c.imshow("up",pu1)
c.imshow("up2",pu2)
c.waitKey()
c.destroyAllWindows()
"""
img1=img.copy()
data=[img1]
for i in range(4):
    img1=c.pyrDown(img1)
    data.append(img1)
    c.imshow("res"+str(i),img1)
    
    
    
c.waitKey()
c.destroyAllWindows() 
    
    
    
    
    
    
    