import cv2
## for colourful image (3-channel)
img1=cv2.imread(r"C:\Users\rhars\OneDrive\Pictures\thor.jpg",1)
img1=cv2.resize(img1,(1000,500))
print(img1)
cv2.imshow("original",img1)
cv2.waitKey(3000)
cv2.destroyAllWindows()

## for grey image 
img2=cv2.imread(r"C:\Users\rhars\OneDrive\Pictures\thor.jpg",0)
img2=cv2.resize(img2,(1000,500))
print(img2)
cv2.imshow("original",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

## for colourful image with high pixel quality, saturation of colour has been increased
img3=cv2.imread(r"C:\Users\rhars\OneDrive\Pictures\thor.jpg",-1)
img3=cv2.resize(img3,(1000,500))
print(img3)
cv2.imshow("unchanged image",img3)
cv2.waitKey()
cv2.destroyAllWindows()