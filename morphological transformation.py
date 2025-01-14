#-------------Morphological Transformations-----------------------

#Morphological transformations are some simple operations based on the image shape.
#It is normally performed on binary images. 
# It needs two inputs, 1)- original image, 2)- structuring element(kernel).
#Two basic Morphological Transformations are 1) - Erosion and 2) - Dilation
import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\col_balls.jpg",0)
_,mask=c.threshold(img, 230, 255, c.THRESH_BINARY_INV)
kernel=np.ones((5,5),np.uint8)
e=c.erode(mask,kernel)

kernel=np.ones((3,3),np.uint8)
d=c.dilate(mask,kernel)
from matplotlib import pyplot as plt
title=["image","mask","e","d"]
images=[img,mask,e,d]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
    

"""c.imshow("image",img)
c.imshow("mask",mask)
c.imshow("kernel",kernel)
c.imshow("e",e)
c.imshow("d",d)
c.waitKey()
c.destroyAllWindows()"""