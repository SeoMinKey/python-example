import cv2
import os

# 이미지 열기
path = os.path.abspath(os.path.dirname(__file__))
file_name = "image.jpeg"
img_file = os.path.join(path, file_name)

img = cv2.imread(img_file)


resize1 = cv2.resize(img, dsize=(500, 1000), interpolation=cv2.INTER_AREA)
resize2 = cv2.resize(img, dsize=(0, 0), fx=7, fy=3, interpolation=cv2.INTER_LINEAR)

cv2.imshow("original", img)
cv2.imshow("resize1", resize1)
cv2.imshow("resize2", resize2)
cv2.waitKey()
cv2.destroyAllWindows()