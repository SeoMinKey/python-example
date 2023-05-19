num = 1
sum = 0

print("0을 입력하면 바로 종료합니다.")
while True:
    num = int(input("더할 값을 입력하시오: "))
    if num < 0:
        print("음수는 더하지 않습니다.")
        continue
    if num == 0:
        break
    sum += num
    print(sum)

print(f"총합은 {sum}입니다.")