import openpyxl
from openpyxl.utils import get_column_letter

# 수업인원.xlsx 파일 열기
wb = openpyxl.load_workbook('수업인원.xlsx')

# 첫 번째 시트 선택
ws = wb.active

# 입력받은 데이터 엑셀에 추가
name = input("이름: ")
gender = input("성별: ")
age = int(input("나이: "))
dev = input("개발여부 (O 또는 X): ")

# 추가할 데이터 리스트로 만들기
new_row = [name, gender, age, dev]

# 엑셀에 데이터 추가
ws.append(new_row)

# 엑셀 파일 저장
wb.save('수업인원.xlsx')
