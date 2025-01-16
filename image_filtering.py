#Image Smoothing or bluring is most common used operation in Image Processing.
#It is use to remove noise from the images.
#There are so many filter  which is use for smoothing the image.
#There are LOW Pass Filter(LPS) which use to remove Noise from the images.
#There are High Pass Filter which use to detect and finding edges in an image.

#we discuss about various filters --
#like , homogeneous,blur(averaging),homogeneous,median,bilateral
import cv2 as c
import numpy as np

#img=c.imread(r"C:\Users\rhars\open_cv\data\noisy.jpg")
#img=c.resize(img,(300,300))
"""
kernel=np.ones((5,5),np.float32)/25
#FILTER NUMBER -----1
#this filter  work like, each output pixel is the mean of its kernal neigbours
#it is aka homogeneous filter in this all pixel contribute with equal weight.
#kernal is a small shape or matrix which we apply on image.
#in this filter kernal is [(1/kernal(h,w))*kernal]  
h_filter=c.filter2D(img, -1, kernel)
c.imshow("homogeneous",h_filter)
#FILtER NUMBER 2-----
#blur method or averaging
#takes the avg of all the pixels under kernel area and 
#replaces the central element with this average..
b_filter=c.blur(img, (7,7))
c.imshow("blur",b_filter)
#Filter Number 3------
#Gaussian Filter -here it using different weight kernel,in  row as well as col.
#means side values are small then centre .It manage distance b/w value of pixel.
gauss=c.GaussianBlur(img, (5,5), 0)
c.imshow("gauss",gauss)
#Filter Number 4--
#Median Filter --computes the median of all the pixels under the 
#kernel window and the central pixel is replaced with this median value.
# This is highly effective in removing salt-and-pepper noise. 
#here kernal size must be odd except one
median=c.medianBlur(img, 5)
c.imshow("median",median)
#bilateral filter --- is highly effective at noise removal while preserving edges.
#It work like gaussian filter but more focus on edges
#it is slow as compare with other filters
#argument (img, neigbour_pixel_diameter,sigma_color,sigma_space)
bi=c.bilateralFilter(img, 9, 75, 75)
c.imshow("bilateral",bi)
c.imshow("noisy",img)
c.waitKey()
c.destroyAllWindows()
"""
img=c.imread(r"C:\Users\rhars\open_cv\data\noisy2.jpg")
img=c.resize(img,(400,400))
kernel=np.ones((5,5),np.float32)/25
h_filter=c.filter2D(img, -1, kernel)
b_filter=c.blur(img, (5,5))
g_filter=c.GaussianBlur(img, (5,5), 0)
m_filter=c.medianBlur(img, 5)
bi_filter=c.bilateralFilter(img,9, 75, 75)
from matplotlib import pyplot as plt

titles=["original","homogeneous","blur","gaussian","median","bilateral"]
values=[img,h_filter,b_filter,g_filter,m_filter,bi_filter]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(values[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
c.waitKey()
c.destroyAllWindows()








