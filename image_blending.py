#image blending

import cv2 as c

img1=c.imread(r"C:\Users\rhars\open_cv\data\roi_opr.jpg")
img1=c.resize(img1,(500,700))
img2=c.imread(r"C:\Users\rhars\open_cv\data\bro_thor.jpg")
img2=c.resize(img2,(500,700))

c.imshow("thor ",img1)
c.imshow("bro_thorr",img2)

#result=img2+img1#it will destroy the images
#result=c.add(img2,img1)  in this u can not control which image should look more
result=c.addWeighted(img1, 0.6, img2, 0.4, 0)
c.imshow("result",result)
c.waitKey()
c.destroyAllWindows()