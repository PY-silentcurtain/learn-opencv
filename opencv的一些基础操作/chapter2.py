import cv2
import numpy as np

img = cv2.imread("Resources/bird.jpg")
kernel = np.ones((5,5),np.uint8)

img = cv2.resize(img,(329,658))

rows,cols,channels = img.shape

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny = cv2.Canny(img,50,150)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

for i in range(rows):
    for j in range(cols):
        if imgCanny[i, j] == 255:
            imgCanny[i, j] = 0
        else:
            imgCanny[i, j] = 255

print(img.shape)
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
# cv2.imshow("Dialation Image",imgDialation)
# cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)