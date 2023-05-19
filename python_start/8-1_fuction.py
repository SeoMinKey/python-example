#함수를 알아보자!
def helloPrint():
    print("Hello world!")

helloPrint()

def numPrint(num):
    print("Your number: " + str(num))

numPrint(10)

#반환값이 있는 경우, return 사용
def sum1 (a,b):
    c = a+b
    return c

print(f"sum: {sum1(9,7)}")
    
#반환값 없어도 ㅇㅋ
def sum2 (a,b):
    c = a+b
    print(c)

sum2(2,4)

#입력값 없어도 ㅇㅋ
def sum3 ():
    print('입력값 없어도 명령어 모아서 정리하는 용도로 사용 가능')
    
sum3() # << 요롷게 사용