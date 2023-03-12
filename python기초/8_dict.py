#딕셔너리 형을 알아보자! (사전형)

dict1 = {'key':'value'} #딕셔너리 형은 키와 밸류로 이루어짐!
print (dict1['key']) #키를 선언하면 밸류가 나옴

#서울과 부산의 데이터 셋 준비
seoul = {'기온':'20', '습도':'40', '풍량':'3.5'}
busan = {'기온':'24', '습도':'60', '풍량':'4.5'}

locate = input('seoul, busan 중 어느 지역의 날씨인가요? :')
type = input('기온, 습도, 풍량 중 어느 것을 알고싶나요? :')

#사용자의 답변에 따라 데이터셋을 dict2 변수에 저장
if locate == 'seoul':
    dict2 = seoul
elif locate == 'busan':
    dict2 = busan
else :
    print('잘못된 지역입니다.')

#프린트 [답변1]의 [답변2]은(는) ---> ex) [seoul]의 [기온]은(는)
print(f'{locate}의 ',end = '')
print(f'{type}은(는) ' ,end='')

#기온이면 값 뒤에'°' 추가
#습도면 '%', 풍량이면 'm/s'
#2번째 답변을 저장한 type을 키로써 dict2에서 선언함 -> 기온, 습도, 풍량에 맞는 숫자값이 나옴
if type == '기온' :
    print(dict2[type],end='')
    print('°',end='')
    print('입니다.')
elif type == '습도' :
    print(dict2[type],end='')
    print('%',end='')
    print('입니다.')
elif type == '풍량' :
    print(dict2[type],end='')
    print('m/s',end='')
    print('입니다.')
else :
    print('잘못된 값입니다.')