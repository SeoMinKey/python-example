#while함수는 ~할때까지 반복

a = 0

while a <= 10:
    print(a)
    a = a+1 #a =-+ 1 로 줄여쓸 수 있음
    
#응용 , input
num = int(input('0부터 n까지 출력합니다. 0을 입력하면 바로 종료합니다.'))
a = 0
while num != 0:
    for i in range(num+1) :
        print(i)
    break #while문을 빠져나가는 명령어
        
print('종료합니다.')
    

    