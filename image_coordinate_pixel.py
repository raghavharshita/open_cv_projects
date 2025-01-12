import cv2 as c

img=c.imread(r"C:\Users\rhars\open_cv\data\lion.jpg")
img=c.resize(img,(1020,700))
#c.imshow("original",img)
print("shape-->",img.shape)
print("pixel-->",img.size)
print("datatype-->",img.dtype)
print("image_type-->",type(img))

px=img[520,580]
print("pixel of the coordinate-->",px)
# to get the blue value of the coordinate
blue=img[520,580,0]
print("blue",blue)
green=img[520,580,1]
print("green",green)
red=img[520,580,2]
print("red",red)
c.waitKey(0)
c.destroyAllWindows()