# 구구단
print("\n구구단")
for i in range(2,10):
    for j in range(2,10):
        mul = j * i
        print(f"{j} * {i} = {mul}", end = "\t")
    print()

# 구구단 홀수
print("\n구구단 홀수")
for i in range(2,10):
    if i % 2 == 1:
        for j in range(2,10):
            mul = j * i
            print(f"{j} * {i} = {mul}", end = "\t")
        print()