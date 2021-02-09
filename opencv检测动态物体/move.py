import cv2
import time
import numpy as np

def videos():
    cap = cv2.VideoCapture(1)
    #不设置是默认640*480，我们这里设置出来
    cap.set(3, 640)
    cap.set(4, 480)

    img_num = 0
    k = np.ones((3, 3), np.uint8)

    while True:
        success, img = cap.read()
        localtime = time.asctime(time.localtime(time.time()))

        if not img_num:
            # 这里是由于第一帧图片没有前一帧
            previous = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_diff = cv2.absdiff(gray, previous)  # 计算绝对值差
        # previous 是上一帧图片的灰度图

        thresh = cv2.threshold(gray_diff, 40, 255, cv2.THRESH_BINARY)[1]
        mask = cv2.medianBlur(thresh, 3)

        close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k)

        cnts = cv2.findContours(close,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 50:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x>0:
                    print("动",localtime)

        cv2.putText(img, localtime, (30, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("x", close)
        cv2.imshow("Result", img)
        img_num += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

videos()