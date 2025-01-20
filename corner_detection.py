#Feature Detection and Description.
"""
For understanding  this we recall jisaw puzzle game where we combine multiple 
small pieces in correct order by identifying its corners , shape and pattern.

On the basis of all these we all detect corners in images with so many approaches,
"""

#Harris Corner Detection 

"""
OpenCV has the function cv2.cornerHarris() for this purpose. Its arguments are :

img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.
"""
import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\shapes.png")
gray=c.cvtColor(img, c.COLOR_BGR2GRAY)
'''
gray=np.float32(gray)
res=c.cornerHarris(gray,3, 3, 0.04)
img[res>0.01*res.max()]=[0,0,255]

c.imshow("image",img)
c.waitKey()
c.destroyAllWindows()
'''

#-------------------------------------------


#We will learn about the another corner detector: Shi-Tomasi Corner Detector
#We will see the function: cv2.goodFeaturesToTrack().
#Shi- Tomasi approach is more effective as compared with Harris Corner detection

#In this we limit the number of corners and corners quality.
#It is more user friendly.


corners=c.goodFeaturesToTrack(gray, 20, 0.01, 5)
corners=np.int64(corners)

for i in corners:
    x,y=i.ravel()
    c.circle(img, (x,y), 3, 255,-1)
    
    
c.imshow("img",img)
c.waitKey()
c.destroyAllWindows()























