#BMI 테스트 프로그램

height = float(input("키를 입력해주세요: "))
weight = float(input("몸무게를 입력해주세요: "))

bmi = weight / ((height / 100) ** 2)
print(f"당신의 BMI는 {bmi:.2f} 입니다")

if bmi < 18.5 :
    print('저체중입니다')
elif bmi < 23 :
    print('정상입니다')
elif bmi < 25 :
    print('과체중입니다')
else :
    print('비만입니다')     



