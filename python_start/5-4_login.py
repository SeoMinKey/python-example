# 로그인 
ID = 'jiseong2'
PW = 'dlwltjd0715!'

in_ID = 'jiseong2'
in_PW = 'dlwltjd0715!'

if in_ID == ID:
    if in_PW == PW:
        print('로그인 성공')
    else:
        print('비밀번호가 일치하지 않습니다.')
else:
    print('ID가 일치하지 않습니다.')