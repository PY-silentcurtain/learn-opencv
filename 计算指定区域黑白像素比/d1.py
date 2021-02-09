import cv2
import  numpy as np

img=cv2.imread('Resources/tom.jpg')
#缩放

rows,cols,channels = img.shape

img=cv2.resize(img,None,fx=0.5,fy=0.5)
rows,cols,channels = img.shape

#转换hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue=np.array([78,43,46])
upper_blue=np.array([124,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

#这一步裁剪指定区域图片。
s = mask[30:200, 50:250] #y,x
#起始x,y坐标，终止x,y坐标，而非加上宽和高
# 和之前用到的cv2.boundingRect()函数定位法不同
cv2.rectangle(img,(50,30),(250,200),(0,0,255),3)
cv2.imshow('res',img)

cv2.imshow('ss',s)
#注意这里s已经是单通道，此时不返回通道值。
x,y= s.shape

bk = 0
wt = 0
#遍历二值图，为0则bk+1，否则wt+1
for i in range(x):
    for j in range(y):
        if s[i,j]==0:
            bk+=1
        else:
            wt+=1
rate1 = wt/(x*y)
rate2 = bk/(x*y)
#round()第二个值为保留几位有效小数。
print("白色占比:", round(rate1*100,2),'%')
print("黑色占比:", round(rate2*100,2),'%')

cv2.waitKey(0)