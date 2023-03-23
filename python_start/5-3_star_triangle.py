#별삼각형 만들기 실습

#10 x 10으로 왼쪽 정렬 직각삼각형 만들기
'''
*
**
***
****
*****
******
*******
********
*********
**********

^^ 이런 모양 ^^
'''
width = 10

for i in range(1, width+1) :
    print('*' * i)
    
# 다음은 오른쪽 정렬!

for i in range(1, width+1) :
    print(' ' * (width - i),end='')
    print('*' * i)
    
# 중앙 정렬, 별이 2개씩 늘어나도록! 9 x 5
'''
     *
    ***
   *****
  *******
 *********
'''
a = 1
for i in range(1, width+1, 2) : #맨 뒤는 늘어나는 숫자
    print(' ' * (int(width/2)-a),end='')
    print('*' * i)
    a += 1
    