import cv2
import os

# 이미지 열기
path = os.path.abspath(os.path.dirname(__file__))
file_name = "image.jpeg"
img_file = os.path.join(path, file_name)
img = cv2.imread(img_file)

# 이미지 블러처리
blurred_image = cv2.GaussianBlur(img, (5,5), 0)
blurred_file = os.path.join(path, 'blurred.jpg')
cv2.imwrite(blurred_file,blurred_image)
