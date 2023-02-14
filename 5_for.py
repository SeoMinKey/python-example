#for문은 길이가 정해져있는 반목문에 사용

list = ['나','는','파','이','썬','이','좋','아']

for i in list:
    print(i)
    
for i in list:
    print(i, end='') #엔터 안치는 법 복습
    
#10번 반복 (0부터 9까지임)
for i in range (0,10):
    print(i)
    
#응용    
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print(f"{number}번 학생은 합격입니다.")
    else: 
        print(f"{number}번 학생은 불합격입니다.")