# 딕셔너리를 사용해 내 인적사항 출력해보기

myData = {'name':'이지성', 'age':21, 'gender':'남자', 'birth_day':7.15, 'hobby':'파이썬 코딩'}

print(
f'''내 이름은 {myData['name']}야. 
나는 {myData['age']}살이고 {myData['gender']}야. 
내 생일은 {myData['birth_day']}일이야.
내 취미는 {myData['hobby']}이야.''')











# 인적사항에 학교와 집주소(구,동) 추가
myData['school'] = '한신대학교'
myData['home'] = '부평구 십정동'

print(
f'''내 이름은 {myData['name']}야. 
나는 {myData['age']}살이고 {myData['gender']}야. 
내 생일은 {myData['birth_day']}일이야.
내 취미는 {myData['hobby']}이야.
나는 {myData['school']}에 다녀.
내 집은 {myData['home']}이야.''')