# 현금 계산기
money = 187384
coin = 0

if money // 50000:
    coin = money // 50000
    print(f"오만원{coin}개")
    money %= 50000
if money // 10000:
    coin = money // 10000
    print(f"만원{coin}개")
    money %= 10000
if money // 5000:
    coin = money // 5000
    print(f"오천원{coin}개")
    money %= 5000
if money // 1000:
    coin = money // 1000
    print(f"천원{coin}개")
    money %= 1000
if money // 500:
    coin = money // 500
    print(f"오백원{coin}개")
    money %= 500
if money // 100:
    coin = money // 100
    print(f"백원{coin}개")
    money %= 100
if money // 50:
    coin = money // 50
    print(f"오십원{coin}개")
    money %= 50
if money // 10:
    coin = money // 10
    print(f"십원{coin}개")
    money %= 10
if money:
    print(f"일원{money}개")
