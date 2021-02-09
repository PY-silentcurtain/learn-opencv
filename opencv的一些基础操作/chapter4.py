import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(50,0),(462,51),(0,255,255),5)
cv2.circle(img,(400,50),100,(255,255,0),3)#(图像，x.y位置，半径，颜色，轮廓粗细)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("Image",img)

cv2.waitKey(0)