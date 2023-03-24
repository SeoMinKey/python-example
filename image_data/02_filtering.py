import cv2
import os

# 이미지 열기
path = os.path.abspath(os.path.dirname(__file__))
file_name = "image.jpeg"
img_file = os.path.join(path, file_name)

img = cv2.imread(img_file)

# 이미지 필터링
edges = cv2.Canny(img, 100, 200)
filter_file = os.path.join(path, 'filter.jpg')
cv2.imwrite(filter_file,edges)

# filtered_image = cv2.bitwise_and(img, img, mask=edges)
# cv2.imshow("filtered image", filtered_image)
