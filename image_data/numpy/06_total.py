import numpy as np

array = np.arange(16).reshape(4, 4)

print(array)

print("최대값:", np.max(array))
print("최소값:", np.min(array))
print("합계:", np.sum(array))
print("평균값:", np.mean(array))

print("세로 항 합계:", np.sum(array, axis=0))
print("가로 항 합계:", np.sum(array, axis=1))