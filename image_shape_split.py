import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\pikachu.jpg")
img=c.resize(img,(600,400))

c.imshow("original",img)

print("shape ==>",img.shape)
print("pixel-->",img.size)
print("datatype-->",img.dtype)
print("imagetype-->",type(img))
# split will divide the image in three different channels blue,green,red
#print(c.split(img))

b,g,r=c.split(img)
b=c.resize(b,(600,400))
g=c.resize(g,(600,400))
r=c.resize(r,(600,400))
"""
c.imshow("blue",b)
c.imshow("green",g)
c.imshow("red",r)
"""
# if we will pass r,g,b instead of b,g,r , the image has been changed
#mrg=c.merge((r,g,b))
mrg=c.merge((b,g,r))
c.imshow("merge",mrg)
c.waitKey(0)
c.destroyAllWindows()