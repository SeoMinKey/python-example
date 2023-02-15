#딕셔너리 형을 알아보자! (사전형)

dict1 = {'key':'value'}
print (dict1['key'])

seoul = {'기온':'20', '습도':'40', '풍량':'3.5'}
busan = {'기온':'24', '습도':'60', '풍량':'4.5'}

locate = input('seoul, busan 중 어느 지역의 날씨인가요? :')
type = input('기온, 습도, 풍량 중 어느 것을 알고싶나요? :')

if locate == 'seoul':
    dict2 = seoul
elif locate == 'busan':
    dict2 = busan
else :
    print('잘못된 지역입니다.')

print(f'{locate}의 ',end = '')
print(f'{type}은(는) ' ,end='')

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