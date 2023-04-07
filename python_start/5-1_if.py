# if문 예제

a = 5
b = 10

if a < b :
    print('a는 b보다 작음')
else :  #단점 : 둘이 같을때도 크다 함
    print('a는 b보다 큼')

#모든 변수 적용
if a < b :
    print('a는 b보다 작음')
elif a == b:  
    print('a와 b는 같음')
else :
    print('a는 b보다 큼')
    
