#Adaptive thresholding
#we use it becoz simple holding can not handle low luminious pixel
#the algo calculate threshold for small region of image
#so we get multiple threshold in same image
import cv2 as c 
import numpy as np
img=c.imread(r"C:\Users\rhars\open_cv\data\page.jpg",0)
_,thres=c.threshold(img, 127, 255, c.THRESH_BINARY)
thres2=c.adaptiveThreshold(img, 255, c.ADAPTIVE_THRESH_MEAN_C, c.THRESH_BINARY, 11, 2)
thres3=c.adaptiveThreshold(img, 255, c.ADAPTIVE_THRESH_GAUSSIAN_C, c.THRESH_BINARY, 11, 2)
c.imshow("original",img)
c.imshow("threshold",thres)
c.imshow("adaptive",thres2)
c.imshow("gaussian",thres3)
c.waitKey()
c.destroyAllWindows()