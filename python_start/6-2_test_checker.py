#응용    
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print(f"{number}번 학생은 합격입니다.")
    else: 
        print(number,"번 학생은 불합격입니다.") #변수는 이렇게도 넣을 수 있음 but, 쉼표 = 띄어쓰기 