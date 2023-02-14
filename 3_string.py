#string은 문자열!
string1 = "문자열은 쌍따움표"
string2 = '혹은 따움표로 감싸서 표현'

print(string1, string2)

string3 = '줄바꿈은\n으로 기입'
string4 = "print에서 줄바꿈 없이 하려면" 
string5 = '뒤에 ",end = ''" 넣기' #문자열 안에 따움표 넣으려면 각각 작은 따움표, 쌍따움표로 다르게 감싸면 됨
print(string3)
print(string4,end='')
print(string5)
