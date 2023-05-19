# 팩토리얼 함수
def factorial(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    
    return sum

print(f"10! : {factorial(10)}")

# 홀짝 판단
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print (is_even(1))
print (is_even(4))
print (is_even(7))


# 1!~10! 중 짝수만 출력
for i in range(1,11):
    fact = factorial(i)
    if is_even(fact):
        print(fact)

# 글자 삼각형
def text_tri(width, text):
    for i in range(1, width+1) :
        print(text * i)

text_tri(5,'@')
text_tri(6,'#')
text_tri(7,'%')