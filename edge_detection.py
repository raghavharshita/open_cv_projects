#Image Gradient--
#It is a directional change in the color or intensity in an image.
#It is most important part to find inormation from image
#Like finding edges within the images.
#There are various methods to find image gradient.
#These are - Laplacian Derivatives,SobelX and SobelY.
#All these functions have diff. mathematical approach to get result.
#All load image in the gray scale
import cv2 as c 
import numpy as np
 

img=c.imread(r"C:\Users\rhars\open_cv\data\avengers.jpg")
img=c.resize(img,(300,300))
img_gray=c.cvtColor(img,c.COLOR_BGR2GRAY)


#laplace image
lap=c.Laplacian(img_gray,c.CV_64F,ksize=1)
lap=np.uint8(np.absolute(lap))
#Sobel operation - 
# is a joint Gausssian smoothing plus differentiation operation, 
#so it is more  resistant to noise
#This is use for x and y bth
#parameter (img,type for -ve val,x = 1,y = 0,ksize)
#Sobel X focus on vertical lines
#Sobel y focus on horizontal lines

sobelx=c.Sobel(img_gray,c.CV_64F,1, 0,ksize=3)
sobely=c.Sobel(img_gray, c.CV_64F, 0, 1,ksize=3)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
comb=c.bitwise_or(sobelx, sobely)

c.imshow("combined",comb)
c.imshow("sobelx",sobelx)
c.imshow("sobely",sobely)
c.imshow("laplace",lap)
c.imshow("original",img)
c.imshow("gray",img_gray)

c.waitKey()
c.destroyAllWindows()