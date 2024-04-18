

# 1. 사각형 클래스
# 다음 조건을 만족하는 Rectangle 클래스를 작성하세요.

# - Rectangle 클래스는 가로(width)와 세로(height)를 
#   속성으로 가져야 합니다.

# - 모든 속성은 인스턴스 변수로 선언되어야 합니다.

# - Rectangle 클래스는 사각형의 넓이를 계산하는 
#   calculate_area() 메서드를 가져야 합니다.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# 2. 은행 계좌 클래스
# 다음 조건을 만족하는 BankAccount 클래스를 작성하세요.

# - BankAccount 클래스는 계좌 소유자의 이름(owner), 
#   계좌 번호(account_number), 잔액(balance)을 
#   속성으로 가져야 합니다.

# - 모든 속성은 인스턴스 변수로 선언되어야 합니다.

# - BankAccount 클래스는 입금(deposit)과 출금(withdraw)을 
#   위한 메서드를 가져야 합니다. 입금과 출금 메서드는 금액(amount)을 
#   매개변수로 받아 잔액을 적절히 갱신해야 합니다.

class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("*****<insufficient balance>*****")


# 3. 학생 클래스
# 다음 조건을 만족하는 Student 클래스를 작성하세요.

# - Student 클래스는 학생의 이름(name), 학년(grade), 
#   성적(scores)을 속성으로 가져야 합니다.

# - 이름과 학년은 문자열로, 성적은 딕셔너리로 저장되어야 합니다.

# - 모든 속성은 인스턴스 변수로 선언되어야 합니다.

# - Student 클래스는 성적을 추가하는 add_score() 메서드와 
#   평균 성적을 계산하는 calculate_average() 메서드를 가져야 합니다.

class Student:
    def __init__(self, name, grade, scores):
        self.name = name
        self.grade = grade
        self.scores = scores

    def add_score(self, subject, score):
        self.scores[subject] = score

    def calculate_average(self):
        sum = 0
        for n in self.scores.keys():
            sum += self.scores[n]

        mean = sum / len(self.scores)

        return mean
    
