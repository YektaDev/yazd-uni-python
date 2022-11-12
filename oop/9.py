a = 10
b = 20
print(type(a))
print(a < b, a.__lt__(b))


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = dict()

    def add_course(self, cname, cgrade):
        self.courses[cname] = cgrade

    def __str__(self):
        txt = f'{self.name}\n{self.courses}'
        return txt

    def get_avg(self):
        avg = sum(self.courses.values()) / len(self.courses)
        return avg

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.get_avg() < other.get_avg():
                return True
            else:
                return False
        elif isinstance(other, (int, float)):
            if self.get_avg() < other:
                return True
            else:
                return False
        else:
            raise TypeError('Invalid type')

    def __le__(self, other):
        if self.get_avg() <= other.get_avg():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.get_avg() > other.get_avg():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.get_avg() >= other.get_avg():
            return True
        else:
            return False


s1 = Student('Ali', 18)
print(s1)

s1.add_course('math', 17)
s1.add_course('physics', 12)
print(s1)

print(s1.get_avg())

s2 = Student('Sara', 22)
s2.add_course('art', 16)
s2.add_course('geography', 17)
print(s2)

print(s1 < s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 >= s2)

if s1 > s2:
    print(f'{s1.name} is smarter than {s2.name}')
elif s1 < s2:
    print(f'{s2.name} is smarter than {s1.name}')
else:
    print(f'{s1.name} and {s2.name} are equally smart')

if s1 < 10:
    print('Fail')
else:
    print('Pass')
