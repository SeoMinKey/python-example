# 리스트 선언
list = [1, 2, 3, 'a', 'b', 'c']

# 리스트의 인덱싱
print(list[0])
print(list[-1])

# 리스트 안의 리스트
list2 = [1, 2, 3, ['a', 'b', 'c']]

print(list2[3][1])

#리스트 슬라이싱
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list3[:5])
print(list3[5:])
print(list3[::2])

# 리스트 연산
a = ['씐', '나', '는']
b = ['파', '이', '썬']

print(a + b)
print(a * 2)