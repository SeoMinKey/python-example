import numpy as np

array1 = np.array([1, 2, 3]) 
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])

print(array3.shape)
#shape은 차원을 나타내는 기능 ex) 2차원인 경우, (세로,가로) / 1차원인 경우 (가로)
print(array3)

print('-' * 20)

array4 = np.arange(4).reshape(1, 4) #reshape은 차원 변환 즉, 행1, 열4
array5 = np.arange(8).reshape(2, 4) #행2 열4
array6 = np.concatenate([array4, array5], axis=0) #세로로 쌓아서 합치기

print(array6.shape)
print(array6)