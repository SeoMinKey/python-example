import cv2
import os

# 이미지 열기
path = os.path.abspath(os.path.dirname(__file__))
file_name = "image.jpeg"
img_file = os.path.join(path, file_name)

img = cv2.imread(img_file)
print(img)

# 이미지 흑백으로 변환
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_file = os.path.join(path, 'gray.jpg')
cv2.imwrite(gray_file,gray_img)

