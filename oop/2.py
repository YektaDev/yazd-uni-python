l = list([1, 2, 3, 4])
print(type(l))

print(l)


class Bankaccount():
    def __init__(self, name, no):
        print('A new bank account is created!')
        self.no = no
        self.mojodi = 0
        self.owner = name

    def variz(self, num):
        self.mojodi += num

    def bardasht(self, num):
        if self.mojodi - num >= 0:
            self.mojodi -= num
        else:
            print('Not enough money!')


acc1 = Bankaccount('ali', 123)
print(type(acc1))
print(acc1.no)
print(acc1.mojodi)
print(acc1.owner)

acc2 = Bankaccount('sara', 1000)
print(acc2.owner, acc2.no, acc2.mojodi)

print(acc1.mojodi)
acc1.variz(50000)
print(acc1.mojodi)

acc1.bardasht(60000)
acc1.bardasht(30000)
print(acc1.mojodi)
