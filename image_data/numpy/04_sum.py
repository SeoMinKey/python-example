import numpy as np

array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2)
array3 = array1 + array2
#numpy는 서로 다른 형태의 배열을 연산할 때, 유동적으로 변환후, 수행
print(array1)
print(array2)
print(array3)