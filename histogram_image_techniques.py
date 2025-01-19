#Image Histogram - Find, Plot and Analyze
#It which gives you an overall idea about the intensity distribution of an image. 
#It distribute data along x and y axis.
# x - axis contain range of color vlaues.
# y - axis contain numbers of pixels in an image.
#With histogram to extract information about contast, brigthness and intensity etc.

#plot histomgram using matplotlib
import cv2 as c
import numpy as np
from matplotlib import pyplot as plt
#black image
'''
img=np.zeros((200,200),np.uint8)
c.rectangle(img, (0,100),(200,200), (255),-1)
c.rectangle(img, (0,50),(50,100), (127),-1)
hist=c.calcHist([img], [0], None, [256],[0,256])

plt.plot(hist)
plt.show()
c.imshow("res",img)
c.waitKey()
c.destroyAllWindows()'''

img=c.imread(r"C:\Users\rhars\open_cv\data\thor.jpg")
img=c.resize(img,(500,600))

#colorful image
"""
b,g,r=c.split(img)
c.imshow("image",img)
c.imshow("b",b)
c.imshow("g",g)
c.imshow("r",r)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.title("colorful image")
plt.show()"""

#gray image---

img_gry=c.cvtColor(img, c.COLOR_BGR2GRAY)
'''
hist=c.calcHist([img_gry], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()

c.imshow("original",img)
c.imshow("gray",img_gry)
'''
'''
#it accept gray scale image
#equalization
equ=c.equalizeHist(img_gry)
res=np.hstack((img_gry,equ))
c.imshow("result",res)
hist=c.calcHist([equ], [0], None, [256], [0,256])
plt.title("equalization")
plt.plot(hist)
plt.show()
'''
#CLAHE (Contrast Limited Adaptive Histogram Equalization)
# create a CLAHE object (Arguments are optional).
#It is used to enchance image and also handle noise froom image region
#gray scale imge is required
clahe=c.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1=clahe.apply(img_gry)
c.imshow("clahe",cl1)
hist=c.calcHist([cl1], [0], None, [256], [0,256])
plt.plot(hist)
plt.title("clahe")
plt.show()








c.waitKey()
c.destroyAllWindows()