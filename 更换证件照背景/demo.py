#更换证件照背景
import cv2
import  numpy as np

img=cv2.imread('Resources/tom.jpg')
#缩放
print(img.shape)
rows,cols,channels = img.shape
img=cv2.resize(img,None,fx=0.5,fy=0.5)
rows,cols,channels = img.shape
cv2.imshow('img',img)
b,g,r = img[5,4]
print(b,g,r)

#转换hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue=np.array([78,43,46])
upper_blue=np.array([124,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
#cv2.imshow('Mask', mask)
print(mask.shape)

#腐蚀膨胀
erode=cv2.erode(mask,None,iterations=1)
#cv2.imshow('erode',erode)
dilate=cv2.dilate(erode,None,iterations=1)

#遍历替换
for i in range(rows):
    for j in range(cols):
        if dilate[i,j]==255:
            img[i,j]=(0,0,255)#此处替换颜色，为BGR通道

cv2.imshow('res',img)
cv2.imshow('dilate',dilate)

cv2.waitKey(0)

