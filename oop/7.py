class Bank_account():
    low_interest_rate = 0.19
    high_interest_rate = 0.19
    th = 150

    def __init__(self, acc_no, owner):
        self.acc_no = acc_no
        self.owner = owner
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def calculate_interest(self):
        if self.balance > Bank_account.th:
            return self.balance * Bank_account.high_interest_rate
        else:
            return self.balance * Bank_account.low_interest_rate


a1 = Bank_account(120, 'Sara')
a2 = Bank_account(140, 'Ali')
print(a1.acc_no, a2.acc_no)

# print(a1.interest_rate)
# print(a2.interest_rate)
# print(Bank_account.interest_rate)

a1.deposit(100)
a2.deposit(200)
print(a1.balance, a2.balance)
a2.calculate_interest()

Bank_account.th = 300
print(a1.low_interest_rate)
print(a1.th)
a1.calculate_interest()
a2.calculate_interest()

print(a1.__dict__)
print(a2.__dict__)
print(Bank_account.__dict__)


class Person():
    n = 0
    mean_age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.mean_age = (Person.mean_age * Person.n + self.age) / (Person.n + 1)
        Person.n += 1


print(Person.n, Person.mean_age)
p1 = Person('Ali', 18)
print(Person.n, Person.mean_age)

p2 = Person('Alireza', 26)
print(Person.n, Person.mean_age)

p3 = Person('Sara', 35)
print(Person.n, Person.mean_age)
