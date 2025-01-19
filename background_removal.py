#backproject using histogram techniques
import cv2 as c 
img=c.imread(r"C:\Users\rhars\open_cv\data\green.jpg")
img=c.resize(img,(600,650))
hsv=c.cvtColor(img, c.COLOR_BGR2HSV)

roi=c.imread(r"C:\Users\rhars\open_cv\data\copy.jpg")
hsv_roi=c.cvtColor(roi, c.COLOR_BGR2HSV)

roi_hist=c.calcHist([hsv_roi], [0,1], None, [180,256], [0,180,0,256])
mask=c.calcBackProject([hsv], [0,1], roi_hist, [0,180,0,256], 1)
kernel=c.getStructuringElement(c.MORPH_ELLIPSE, (5,5))
mask=c.filter2D(mask,-1,kernel)
_,mask=c.threshold(mask, 200,255, c.THRESH_BINARY)
mask=c.merge((mask,mask,mask))
result=c.bitwise_or(img, mask)

c.imshow("original",img)
c.imshow("result",result)
c.imshow("mask",mask)
c.imshow("hsv",hsv)
c.waitKey()
c.destroyAllWindows()