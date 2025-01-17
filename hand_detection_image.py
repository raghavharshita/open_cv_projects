import cv2 as c
import numpy as np

img=c.imread(r"C:\Users\rhars\open_cv\data\hand.jpg")
img=c.resize(img,(600,700))
img1=c.cvtColor(img, c.COLOR_BGR2GRAY)
blur=c.medianBlur(img1,11)
kernel=np.ones((3,3),np.uint8)
ret,thresh=c.threshold(blur,240, 255,c.THRESH_BINARY_INV)
d=c.dilate(thresh,kernel)
cnt,hier=c.findContours(thresh,c.RETR_EXTERNAL,c.CHAIN_APPROX_SIMPLE)
#img=c.drawContours(img, cnt, -1, (50,50,150),2)

for i in cnt:
    epsilon=0.001*c.arcLength(i,True)
    data=c.approxPolyDP(i, epsilon, True)
    hull=c.convexHull(data)

    c.drawContours(img, [i], -1, (50,50,150),2)
    c.drawContours(img, [hull], -1, (0,255,0),2)
"""
#convexity defects
hull2=c.convexHull(cnt[0],returnPoints=False)
defect=c.convexityDefects(cnt[0], hull2)
for j in range(defect.shape[0]):
    s,e,f,d=defect[j,0]
    print(s,e,f,d)
    start=tuple(i[s][0])
    end=tuple(i[e][0])
    far=tuple(i[f][0])
    c.circle(img,far, 5, (0,0,0),-1)
"""
c_max=max(cnt,key=c.contourArea)
extreme_left=tuple(c_max[c_max[:,:,0].argmin()][0])
extreme_right=tuple(c_max[c_max[:,:,0].argmax()][0])
extreme_top=tuple(c_max[c_max[:,:,1].argmin()][0])
extreme_down=tuple(c_max[c_max[:,:,1].argmax()][0])

c.circle(img, extreme_left, 5, (0,0,0),-1)
c.circle(img, extreme_right, 5, (0,0,0),-1)
c.circle(img, extreme_top, 5, (0,0,0),-1)
c.circle(img, extreme_down, 5, (0,0,0),-1)


c.imshow("original",img)
c.imshow("gray",img1)
c.imshow("threshold",thresh)
c.waitKey()
c.destroyAllWindows()