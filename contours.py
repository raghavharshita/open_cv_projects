#Contours - 
#Contours can be explained simply as a curve joining all the continuous points 
#(along the boundary), having same color or intensity. 

#The contours are a useful tool for shape analysis and object detection and recognition

#For better accuracy, use binary images and also apply edge detection before 
#finding countours.

#findCountour function manipulate original imge so copy it before proceeding.
#findContour is like finding white object from black background.
#so you must turn image in white and background is black.

#We have to find and draw contours as per the requirement.

import cv2 as c 
import numpy as np
img=c.imread(r"C:\Users\rhars\open_cv\data\logo.jpg")
img_gry=c.cvtColor(img, c.COLOR_BGR2GRAY)
ret,thres=c.threshold(img_gry, 20, 255, 0)

cnt,hier=c.findContours(thres, c.RETR_TREE, c.CHAIN_APPROX_SIMPLE)
#print(cnt,len(cnt))
img=c.drawContours(img,cnt,-1,(151,110,163),4)#we can replace -1 with the number of conter we want












c.imshow("thresh",thres)
c.imshow("original",img)
c.imshow("gray",img_gry)
c.waitKey()
c.destroyAllWindows()