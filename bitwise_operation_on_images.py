#Bitwise Operations : AND,OR,NOT,XOR
#used for masking
#help to find roi 
import cv2 as c
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
img1=c.rectangle(img1, (150,100),(200,250), (255,255,255),-1)

img2=np.zeros((250,500,3),np.uint8)
img2=c.rectangle(img2, (10,10),(170,190), (255,255,255),-1)

#c.imshow("img1",img1)
#c.imshow("img2",img2)

bit_and=c.bitwise_and(img1,img2)
c.imshow("bitwise_and",bit_and)
bit_or=c.bitwise_or(img1,img2)
c.imshow("bitwise_OR",bit_or)
bit_not=c.bitwise_not(img1)
c.imshow("bitwise_NOT",bit_not)
bit_xor=c.bitwise_xor(img1,img2)
c.imshow("bitwise_XOR",bit_xor)
c.waitKey()
c.destroyAllWindows()
