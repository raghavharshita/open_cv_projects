# opening and closing in morphological transformation
import cv2 as c 
import numpy as np
#img=c.imread(r"C:\Users\rhars\open_cv\data\col_balls.jpg",0)
"""

_,mask=c.threshold(img, 230, 255, c.THRESH_BINARY_INV)
kernel=np.ones((5,5),np.uint8)
e=c.erode(mask, kernel)

kernel=np.ones((3,3),np.uint8)
d=c.dilate(mask, kernel)
# opening is performing the erosion first and then dilution
kernel=np.ones((4,4),np.uint8)
o=c.morphologyEx(mask,c.MORPH_OPEN, kernel)
# closing is performing dilution first and then opening
kernel=np.ones((2,2),np.uint8)
cl=c.morphologyEx(mask,c.MORPH_CLOSE, kernel)

#---optional---
x1=c.morphologyEx(mask,c.MORPH_TOPHAT, kernel)#difference bt mask and opening
x2=c.morphologyEx(mask, c.MORPH_GRADIENT, kernel)#difference bt dilate and erosion
x3=c.morphologyEx(mask, c.MORPH_BLACKHAT, kernel)#difference bt closing and input image

c.imshow("opening",o)
c.imshow("closing",cl)
c.imshow("x1",x1)
c.imshow("x2",x2)
c.imshow("x3",x3)
c.waitKey()
c.destroyAllWindows()
"""

img=c.imread(r"C:\Users\rhars\open_cv\data\girl.jpg",0)
img=c.resize(img,(300,300))
_,mask=c.threshold(img, 220, 255, c.THRESH_BINARY_INV)
kernel=np.ones((2,2),np.uint8)
e=c.erode(mask, kernel)
d=c.dilate(mask, kernel)
o=c.morphologyEx(mask, c.MORPH_OPEN, kernel)
cl=c.morphologyEx(mask,c.MORPH_CLOSE, kernel)
x1=c.morphologyEx(mask, c.MORPH_TOPHAT, kernel)
x2=c.morphologyEx(mask,c.MORPH_GRADIENT, kernel)
x3=c.morphologyEx(mask, c.MORPH_BLACKHAT, kernel)

titles=["image","erosion","dilution","opening","closing","x1","x2","x3"]
values=[img,e,d,o,cl,x1,x2,x3]
from matplotlib import pyplot as plt
for i in range(8):
    plt.subplot(3,3,i+1)
    plt.imshow(values[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
c.waitKey()
c.destroyAllWindows()













