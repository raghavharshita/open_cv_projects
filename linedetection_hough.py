"""
Hough Transform is a popular technique to detect any shape,
if you can represent that shape in mathematical form. 
It can detect the shape even if it is broken or distorted a 
little bit.
functions: cv2.HoughLines(), cv2.HoughLinesP()
"""
#We represent shapes with the help of lines.
#And line are expressed for Hough Transform by --
#Cartesian CS(cordinate system) --> y= mx+c and Polar CS --> xcos0+ysin0
import cv2 as c
import numpy as np
img=c.imread(r"C:\Users\rhars\open_cv\data\chess.jpg")
img=c.resize(img,(400,400))
gray=c.cvtColor(img, c.COLOR_BGR2GRAY)
edges=c.Canny(gray, 20, 250,apertureSize = 3)
'''
lines=c.HoughLines(edges, 1, np.pi/180, 200)
#rho value -- distance resolution of pixels
#thetha - angle resolution
#line threshold
for rho,theta in lines[0]:
    
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    
    c.line(img,(x1,y1),(x2,y2),(255,0,255),2)
'''
lines=c.HoughLinesP(edges,1,np.pi/180,100,minLineLength=8,maxLineGap=100)

for line in lines:
    x1,y1,x2,y2=line[0]
    c.line(img, (x1,y1), (x2,y2), (100,200,125),2)
img=c.imread(r"C:\Users\rhars\open_cv\data\square.png")
img=c.resize(img,(400,400))
gray=c.cvtColor(img, c.COLOR_BGR2GRAY)
edges=c.Canny(gray,20, 250)
lines=c.HoughLinesP(edges, 1, np.pi/180, 80,minLineLength=100,maxLineGap=80)
for line in lines:
    x1,y1,x2,y2=line[0]
    c.line(img,(x1,y1),(x2,y2),(100,200,125),2)

c.imshow("original",img)
c.imshow("edges",edges)
c.waitKey()
c.destroyAllWindows()