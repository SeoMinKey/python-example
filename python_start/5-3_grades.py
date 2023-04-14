# 성적이 60점 이상 합격
student = 80

if student >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")


# 0~20 F, 20~40 D, 40~60 C, 60~80 B, 80~100 A
if student >= 80 and student <= 100:
    print("성적: A")
elif student >= 60 and student < 80:
    print("성적: B")
elif student >= 40 and student < 60:
    print("성적: C")
elif student >= 20 and student < 40:
    print("성적: D")
elif student >= 0 and student < 20:
    print("성적: F")
else:
    print("NP")

