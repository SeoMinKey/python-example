#BMI 테스트 프로그램

height = float(input("키를 입력해주세요: "))
weight = float(input("몸무게를 입력해주세요: "))
#BMI지수 = 몸무게에 키제곱을 나눈 값 (M단위이기 때문에 나누기 100 해야함)
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



