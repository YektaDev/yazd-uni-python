class Car():
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def describe(self):
        print('This car is', self.color, 'and its speed is', self.speed)

    def __str__(self):
        return 'This car is ' + self.color + ' and its speed is ' + str(self.speed)

    def __repr__(self):
        return f'{self.__class__.__name__}(' + self.color + ', ' + str(self.speed) + ')'


car1 = Car('red', 100)
print(car1)
print(car1.color, car1.speed)
car1.describe()
print(str(car1))
print(repr(car1))

from datetime import date
import datetime

t = date.today()
print(t)
print(repr(t))

t2 = datetime.date(2022, 10, 30)
print(t2 == t)
