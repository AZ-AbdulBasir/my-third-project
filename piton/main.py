#1
import math


class circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Введите радиус круга: "))
obj = circle(r)
print("Площадь круга:", round(obj.area(), 2))
print("Длина окружности:", round(obj.perimeter(), 2))



#2
class Employee:
    def name(self):
        return 'My name is Mike'

    def job(self):
        return 'I am a doctor'

    def age(self):
        return 'I thirty-six years old'

    def salary(self):
        return 'My salary is 800$'

class Manager:
    def name(self):
        return 'My name is Tom'

    def job(self):
        return 'I am a manager'

    def age(self):
        return 'I thirty-nine years old'

    def salary(self):
        return 'My salary is 800$'


a = '800'
b = '10%'
print(a + b)