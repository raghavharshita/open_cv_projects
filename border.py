## Border on image
import cv2 as c 
img=c.imread(r"C:\Users\rhars\open_cv\data\lion.jpg")
img=c.resize(img,(1000,600))
brdr=c.copyMakeBorder(img, 10, 10, 5, 5, c.BORDER_ISOLATED,value=[255,0,125])
c.imshow("original",brdr)
c.waitKey()
c.destroyAllWindows()