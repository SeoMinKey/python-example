import cv2
import os

# 이미지 파일을 읽어온다.
path = os.path.abspath(os.path.dirname(__file__))
file_name = "도형.png"
img_file = os.path.join(path, file_name)

img = cv2.imread(img_file)
print(img)

# 읽어온 이미지를 화면에 출력한다.
cv2.imshow('img image', img)

# 이미지를 그레이스케일로 변환한다.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 그레이스케일로 변환한 이미지를 화면에 출력한다.
cv2.imshow('gray image', gray_img)

# 그레이스케일 이미지에서 원하는 범위의 값을 가진 픽셀을 검출한다.
lower_range = 50
upper_range = 150
mask = cv2.inRange(gray_img, lower_range, upper_range)

# 마스크 이미지를 화면에 출력한다.
cv2.imshow('mask image', mask)

# 마스크를 적용하여 원본 이미지에서 검출한 부분만 남긴다.
masked_img = cv2.bitwise_and(img, img, mask=mask)

# 결과 이미지를 화면에 출력한다.
cv2.imshow('masked image', masked_img)
cv2.waitKey()
cv2.destroyAllWindows()