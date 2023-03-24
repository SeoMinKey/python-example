#각종 자료형
print("\n각종 자료형")

print(7, type(7))
print(7.2, type(7.2))
print(3 + 4j, type(3 + 4j))
print(True, type(True))

print('abc', type('abc'))
print([1], type([1]))
print((1), type((1)))
print({1}, type({1}))
print({'key':1}, type({'key':1}))

# 서로 다른 자료형 연산
print("\n서로 다른 자료형 연산")

print(10+5, type(10+5))
print(10+5.0, type(10+5.0))
# print(10+'5', type(10+'5'))

# 타입 변환
print("\n타입 변환")

print(int(10+5.0), type(int(10+5.0)))
print(10+int('5'), type(10+int('5')))

print(10/4, type(10/4))
print(int(10/4), type(int(10/4)))

