# 최소 공배수
# def lcm(a, b):
#     x = 1
#     y = 1
#     while True:
#         if a*x > b*y:
#             y += 1
#         elif a*x < b*y:
#             x += 1
#         else:
#             break
#     return a*x

# a = int(input('1번째 정수: '))
# b = int(input('2번째 정수: '))

# print(f'두 정수의 최소 공배수는 {lcm(a, b)}입니다.')


# 금액 계산
# def bill(price, quantity, budget):
#     total_amount = price * quantity
#     additional_amount = total_amount - budget

#     if additional_amount <= 0:
#         return f"구입이 가능합니다. 잔액: {int(budget - total_amount)}원"
#     else:
#         return f"추가로 필요한 금액: {int(additional_amount)}원"

# price = float(input("상품 가격을 입력하세요: "))
# quantity = int(input("구입할 물품의 개수를 입력하세요: "))
# budget = float(input("현재 소지금액을 입력하세요: "))

# result = bill(price, quantity, budget)
# print(result)