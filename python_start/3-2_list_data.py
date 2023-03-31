# 리스트를 사용해 내 인적사항 출력해보기

myData = ['이지성', 21, '남자', 7.15, '파이썬 코딩']

print(
f'''내 이름은 {myData[0]}야. 
나는 {myData[1]}살이고 {myData[2]}야. 
내 생일은 {myData[3]}일이야.
내 취미는 {myData[4]}이야.''')









# 이름과 나이만 추출
data1 = myData[0:2]

print(data1)

# 성별과 생일만 추출
data2 = myData[2:4]

print(data2)

# 이름 생일만 추출
data3 = myData[::3]

print(data3)