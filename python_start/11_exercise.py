# 10개의 요소를 가진 리스트에 랜덤한 값을 담고, 
# 오름차순 정렬, 
# 내림차순 정렬, 
# 최댓값 찾기, 
# 최소값 찾기, 
# 평균값을 구하는 
# 클래스를 함수 없이 구현한 코드 작성

import random

class CustomList:
    def __init__(self, size=10):
        self.list = [random.randint(0, 100) for _ in range(size)]
    
    def sort_ascending(self):
        for i in range(len(self.list)):
            for j in range(i + 1, len(self.list)):
                if self.list[i] > self.list[j]:
                    self.list[i], self.list[j] = self.list[j], self.list[i]
    
    def sort_descending(self):
        for i in range(len(self.list)):
            for j in range(i + 1, len(self.list)):
                if self.list[i] < self.list[j]:
                    self.list[i], self.list[j] = self.list[j], self.list[i]
    
    def find_max(self):
        max_val = self.list[0]
        for num in self.list:
            if num > max_val:
                max_val = num
        return max_val
    
    def find_min(self):
        min_val = self.list[0]
        for num in self.list:
            if num < min_val:
                min_val = num
        return min_val
    
    def calculate_average(self):
        total = 0
        for num in self.list:
            total += num
        return total / len(self.list)
    
    def display_list(self):
        print(self.list)

# 사용 예시
custom_list = CustomList()
print("랜덤 리스트:")
custom_list.display_list()

print("오름차순 정렬:")
custom_list.sort_ascending()
custom_list.display_list()

print("내림차순 정렬:")
custom_list.sort_descending()
custom_list.display_list()

print("최댓값:", custom_list.find_max())
print("최소값:", custom_list.find_min())
print("평균값:", custom_list.calculate_average())
