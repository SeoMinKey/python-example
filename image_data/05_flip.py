import cv2
import os

# 이미지 열기
path = os.path.abspath(os.path.dirname(__file__))
file_name = "image.jpeg"
img_file = os.path.join(path, file_name)

img = cv2.imread(img_file)

flip = cv2.flip(img, 0)

cv2.imshow("original", img)
cv2.imshow("flip", flip)
cv2.waitKey()
cv2.destroyAllWindows()