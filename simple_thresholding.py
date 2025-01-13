#Thresholding
#there are basically three type of thresholding -simple thresholding,adaptive thresholding

import cv2 as c
import numpy as np
img=c.imread(r"C:\Users\rhars\open_cv\data\black_white.png",0)
img=c.resize(img,(300,300))
c.imshow("original",img)

_,thre=c.threshold(img, 50, 255, c.THRESH_BINARY)
_,thre2=c.threshold(img,50,255,c.THRESH_BINARY_INV)
_,thre3=c.threshold(img,150,255,c.THRESH_TRUNC)
_,thre4=c.threshold(img, 127, 255, c.THRESH_TOZERO)
_,thre5=c.threshold(img,127,255,c.THRESH_TOZERO_INV)
c.imshow("threshold binary",thre)
c.imshow("threshold binary inverse",thre2)
c.imshow("threshold trunc",thre3 )
c.imshow("threshold tozero",thre4)
c.imshow("threshold tozero inverse",thre5)

c.waitKey()
c.destroyAllWindows()
