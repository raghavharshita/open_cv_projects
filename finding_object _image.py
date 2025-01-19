"""
It is a method for searching and finding the location of a template image 
in a larger image.OpenCV comes with a function cv2.matchTemplate() for this 
purpose. It simply slides the template image over the input image 
(as in 2D convolution) and compares the template and patch of input image 
under the template image. 
"""
import cv2 as c
import numpy as np
#input
img=c.imread(r"C:\Users\rhars\open_cv\data\avengers.jpg")
gry_img=c.cvtColor(img, c.COLOR_BGR2GRAY)
#target
temp=c.imread(r"C:\Users\rhars\open_cv\data\star.jpg",0)
w,h=temp.shape[::-1]
'''
#template matching
res=c.matchTemplate(gry_img, temp, c.TM_CCORR_NORMED)

thresh=0.98
loc=np.where(res>=thresh)#finding bright pixel
count=0
for i in zip(*loc[::-1]):
    print("i--",i)
    c.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)
    count+=1

print("count",count)
img=c.resize(img,(800,600))
res=c.resize(res,(800,600))
c.imshow("original",img)
c.imshow("result",res)
c.waitKey()
c.destroyAllWindows()
'''
methods=["c.TM_CCORR_NORMED","c.TM_CCOEFF","c.TM_CCOEFF_NORMED","c.TM_CCORR",
         "c.TM_SQDIFF","c.TM_SQDIFF_NORMED"]
for m in methods:
    print("m==",m)
    img2=gry_img.copy()
    method=eval(m)
    
    res=c.matchTemplate(img2, temp, method)
    threshold=c.minMaxLoc(res)
    
    x1=threshold[3]
    c.rectangle(img2,x1,(x1[0]+w,x1[1]+h), (255,0,255),4)
    
    img2=c.resize(img2,(400,600))
    c.imshow(m+"img",img2)
    res=c.resize(res,(400,600))
    c.imshow(m+"res",res)
    
c.waitKey()
c.destroyAllWindows()























