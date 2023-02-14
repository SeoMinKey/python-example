#딕셔너리형을 알아보자! (사전형)

dict1 = {'key':'value'}
print (dict1['key'])

dict2 = {'기온':'24', '습도':'60', '풍량':'3.5'}
type = input('기온, 습도, 풍량중 어느것을 알고싶나요? :')

print(f'{type}은(는) ' ,end='')
print(dict2[type],end='')

if type == '기온' :
    print('°',end='')
elif type == '습도' :
    print('%',end='')
elif type == '풍량' :
    print('m/s',end='')
else :
    print('값이 이상합니다')

print('입니다')