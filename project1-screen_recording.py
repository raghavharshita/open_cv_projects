# screen recording......

import cv2 as c
import pyautogui as p
import numpy as np

#resolution
rs=p.size()
path=input("enter the path.....==")

fourcc=c.VideoWriter_fourcc(*"XVID")
output=c.VideoWriter(path,fourcc,20.0,rs)

c.namedWindow("screen recording",c.WINDOW_NORMAL)
c.resizeWindow("screen recording",(600,400))

while True:
    img=p.screenshot()
    f=np.array(img)
    f=c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("screen recording",f)
    if c.waitKey(1)==ord("s"):
        break
    
output.release()
c.destroyAllWindows()
    