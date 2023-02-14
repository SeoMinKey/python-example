#리스트 출력, 슬라이싱
list1 = ['안','녕','하','세','요']
print(list1)

print(list1[0:2])  #시작:끝 인덱스는 0부터 시작
print(str(list1))

list1.append('!')   #더하기
print(list1)

del list1[:4]   #빼기
print(list1)

print(len(list1))  #길이

