import cv2
import numpy as np

path = './test_05.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
imgCanny = cv2.Canny(imgBlur,100,120)

cv2.imshow("O", imgCanny)

imgContour = img.copy()

cnts = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
for cnt in cnts:
    area = cv2.contourArea(cnt)
    # 这个输出各个轮廓的面积
    #print(area)
#
if area >= 500:
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
    peri = cv2.arcLength(cnt, True)
    # 找出轮廓的突变值
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    # approx找到的是一个轮廓有几个突变值，有几个角就会有几个突变值
    # 返回的是一个list，输出他的长度，就可以知道到底有几个角
    print(approx)
    a1,a2,a3,a4 = list(approx[0][0]),list(approx[1][0]),list(approx[2][0]),list(approx[3][0])

#cv2.imshow("Canny Image",imgContour)

mat1 = np.array([a1,a2,a3,a4],dtype=np.float32)

#透视变换
#计算矩形宽高
width = 402#int(((a4[0]-a1[0])+(a3[0]-a2[0]))/2)
height = 518#int(((a2[1]-a1[1])+(a3[1]-a4[1]))/2)

#计算还原后的坐标
new_a1 = [0,0]
new_a2 = [0,height]
new_a3 = [width,height]
new_a4 = [width,0]

mat2 = np.array([new_a1,new_a2,new_a3,new_a4],dtype=np.float32)
#计算变换矩阵
mat3 = cv2.getPerspectiveTransform(mat1,mat2)

#进行透视变换
res = cv2.warpPerspective(imgCanny,mat3,(width,height))
res1 = cv2.warpPerspective(img,mat3,(width,height))

imgxx = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(imgxx,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU )[1]
#变换完成
#cv2.imshow("Output",res1)

cntss = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
for cnt1 in cntss:
    area1 = cv2.contourArea(cnt1)
    # 这个输出各个轮廓的面积
    #print(area)
#
    if area1 >= 1500 and area1<=1700:
        #把圆的轮廓画成黑色
        cv2.drawContours(binary, cnt1, -1, (0, 0, 0), 10)

        kernel = np.ones((5, 5), np.uint8)
        imgDialation = cv2.dilate(binary, kernel, iterations=1)

cv2.imshow("Out", imgDialation)

cntsss = cv2.findContours(imgDialation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

l1 = []
l2 = []

for cnt2 in cntsss:
    area2 = cv2.contourArea(cnt2)
            #print(area)

    if area2 <= 1200 and 800<=area2:
                #cv2.drawContours(res1, cnt, -1, (0, 255, 0), 5)
                #轮廓长
        peri = cv2.arcLength(cnt2, True)
                # 找出轮廓的突变值
        approx1 = cv2.approxPolyDP(cnt2, 0.02 * peri, True)

        x, y, w, h = cv2.boundingRect(approx1)
                #外接矩形
        print(x+w//2,y+h//2)

        m = x+w//2
        n = y+h//2
        l1.append(m)
        l2.append(n)

        if 75<m<130:
            print("A")
        elif 130<m<185:
            print("B")
        elif 185 < m < 240:
            print("C")
        elif 240 < m < 295:
            print("D")
        elif 295 < m <350:
            print("E")

        if 400>x>80 and 50<y<350:
            cv2.rectangle(res1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #圆心
            # (图像，x.y位置，半径，颜色，轮廓粗细)
            cv2.circle(res1, (x+w//2,y+h//2), 1, (255, 0, 0), 5)


cv2.imshow("cc Image",res1)

cv2.imshow("dd Image",binary)

cv2.waitKey(0)
