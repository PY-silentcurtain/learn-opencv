import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
#上面设置基础的窗口信息

#填入我们捕捉到的hsv值
#色调、饱和度、亮度的min~max
myColors = [[65,51,139,83,255,255]]
#笔触颜色
myColorValues = [[0,255,0]]

#把坐标轴放在list里，持续绘制留下笔迹。
myPoints =  []  ## [x , y , colorId ]

def findColor(img,myColors,myColorValues):
    #转换成hsv色彩空间。
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        cv2.imshow("x", mask)
        #print(mask.shape)验证图片通道数
        #调用函数，获取轮廓信息,经过inRange()方法，此时图片已为单通道。
        x,y=getContours(mask)
        #画上我们的笔尖
        cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
            #加上最小外接正矩形，更好理解我们对的笔尖运算方法。
            cv2.rectangle(imgResult, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        #print(point)
        #绘制我们的笔尖，参数依次为(图像，x.y位置，半径，颜色，轮廓粗细)
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    #读取图片
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break