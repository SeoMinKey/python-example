import random

print("up/down game start!!")
print("0부터 100까지의 숫자 중 하나만 생각하시오.")
start_sign = input("준비가 되었다면 yes를 입력하시오. : ")
user_sing = "user_sing"

max = 101
min = 1

if start_sign == "yes":
    while user_sing != "yes":
        
        num = random.randrange(min, max)

        print(f"당신의 숫자는 {num}??")
        user_sing = input("up/down/yes : ")
        
        if user_sing == "up":
            min = num + 1
        if user_sing == "down":
            max = num
    print(f"당신의 숫자는 {num}입니다.")
    print("프로그램을 종료합니다.")        
            
else:
    print("준비가 되면 프로그램을 다시 실행시켜주세요.")