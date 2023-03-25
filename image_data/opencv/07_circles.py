import cv2
import os
import numpy as np

# 이미지 파일을 읽어온다.
path = os.path.abspath(os.path.dirname(__file__))
file_name = "shapes.png"
img_file = os.path.join(path, file_name)

img = cv2.imread(img_file)

# 이미지를 회색조로 변환
cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 동그라미 검출
circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 20, param1=50,param2=30,minRadius=0,maxRadius=0)

# 소수점으로 된 동그라미 좌표를 정수로 변환
circles = np.int16(np.around(circles))

# 검출된 동그라미 그리기
for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

# 결과 이미지 출력
cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()