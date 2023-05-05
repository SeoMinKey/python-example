#while함수는 ~할때까지 반복

a = 0

while a <= 10:
    print(a)
    a = a+1 #a =-+ 1 로 줄여쓸 수 있음

# input함수
n = input("정수를 입력하시오.")
print("n:", n)
print("n의 자료형:", type(n))

# break, continue
num = int(input('0부터 n까지 출력합니다. 0을 입력하면 바로 종료합니다.'))
i = 0
while num != 0:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    if i == num:
        break #while문을 빠져나가는 명령어

print('종료합니다.')    
