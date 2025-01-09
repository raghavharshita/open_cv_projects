import cv2
path=input("enter the path.....:")
print("you entered ....:",path)

img1=cv2.imread(path,0)
img1=cv2.resize(img1,(1000,500))
#img1=cv2.flip(img1,1)#can take 0,1,-1 values
cv2.imshow("original",img1)
#cv2.waitKey()
#cv2.destroyAllWindows()
k=cv2.waitKey()
if k==ord("s"):
    cv2.imwrite(r"C:\Users\rhars\Documents\output.jpg",img1)
else:
    cv2.destroyAllWindows()