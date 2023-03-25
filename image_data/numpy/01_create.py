import numpy as np
#numpy는 파이썬에서 다차원 배열을 활용할 수 있게 만들어주는 도구
#import ~~ as !!는 ~~라는 이름의 모듈을 !!라는 이름으로 불러오는 것! 

array = np.array([1, 2, 3])
print(array.size) # 배열의 크기
print(array.dtype) # 배열 원소의 타입
print(array[1]) # 인덱스 2의 원소