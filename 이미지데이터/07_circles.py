import cv2
import numpy as np

# 이미지 파일 읽기
img = cv2.imread("이미지데이터/도형.png", cv2.IMREAD_COLOR)

# 이미지가 제대로 읽혔는지 확인
if img is not None:
    # 이미지를 회색조로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 이미지의 경계 검출
    edges = cv2.Canny(gray, 50, 150)

    # 동그라미 검출
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

    # 동그라미가 검출된 경우
    if circles is not None:
        # 소수점으로 된 동그라미 좌표를 정수로 변환
        circles = np.round(circles[0, :]).astype("int")

        # 검출된 동그라미 그리기
        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 2)

        # 결과 이미지 출력
        cv2.imshow("Detected Circle", img)
        cv2.waitKey(0)
    else:
        print("No circle detected.")
else:
    print("Failed to read image.")
