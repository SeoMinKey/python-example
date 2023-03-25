import numpy as np

array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10 #array1에서 10 미만인것을 true, 이상인 것을 false로 배열 생성 (마스킹 연산)
print(array2)

array1[array2] = 100 #array1에 array2배열을 넣으면 true인 부분만 100으로 변환 
print(array1)

'''
원래 파이썬의 리스트 형태로 해당 기능을 수행하려면
각 인덱스 하나하나 방문해서 체크 후 변환해야함
-> 굉장히 빠르고, 쉬움'''