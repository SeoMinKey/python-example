# Person 클래스
# 속성: name, age
# 메서드: print()

# Score 클래스
# 속성: kor, eng, math
# 메서드: print()

# Student 클래스 
# 상속: Score, Person
# 속성: name, age, kor, eng, math
# 메서드: print()

# ClassRoom 클래스
# 속성: count
# 메서드: print(), updateStudent(), delStudent()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')


class Score:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def print(self):
        super().print()
        print(f'kor: {self.kor}')
        print(f'eng: {self.eng}')
        print(f'math: {self.math}')


class Student(Person, Score):
    def __init__(self, name, age, kor, eng, math):
        Person.__init__(name, age)
        Score.__init__(kor, eng, math)

    def print(self):
        Person.print()
        Score.print()

class ClassRoom:
    def __init__(self, count):
        self.count = count
        self.students = {}

    def updateStudent(self, data):
        if len(self.students) >= self.count:
            print('Student full')
        else:
            student = {}
            student["age"] = data.age
            student["kor"] = data.kor
            student["eng"] = data.eng
            student["math"] = data.math
            self.students[data.name] = student
            print(f'{data.name} Student update')

    def delStudent(self, data):
        if data.name in self.students:
            del self.students[data.name]
            print(f'{data.name} deleted')
        else:
            print('Student not found')

    def print(self):
        for student in self.students.keys():
            print(f'{student} -> {self.students[student]}')




a = Student('a',1,1,1,1)
b = Student('b',2,1,1,1)
c = Student('c',3,1,1,1)
d = Student('d',4,1,1,1)
e = Student('e',5,1,1,1)

a_class = ClassRoom(4)
a_class.updateStudent(a)
a_class.updateStudent(b)
a_class.updateStudent(c)
a_class.updateStudent(d)
a_class.updateStudent(e)
a_class.print()
a_class.delStudent(a)
a_class.delStudent(e)

a_class.print()