# 1. 동물 클래스(Animal Class)와 각종 동물 클래스의 상속
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class Cow(Animal):
    def speak(self):
        return "음메!"

# 사용 예시
dog = Dog("바둑이")
print(dog.speak())
cat = Cat("야옹이")
print(cat.speak())
cow = Cow("젖소")
print(cow.speak())


# 2. 도형 클래스(Shape Class)와 사각형 클래스(Rectangle Class)의 상속:
class Shape:
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 사용 예시
rectangle = Rectangle("빨강", 5, 4)
print(rectangle.color)
print(rectangle.area())
