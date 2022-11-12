# P(x) = 5x^2 + 3x^1 + 4x^0 ---> [5,3,4]
# y = 3x^4 -1 ---> [3,0,0,0,-1]

class Poly():
    def __init__(self, coeff):
        self.coeff = coeff

    def __str__(self):
        representation = 'P(x) = '
        l = len(self.coeff)
        for idx, c in enumerate(self.coeff):
            if c > 0:
                representation += f'+{c}x^{l - idx - 1}'
            elif c < 0:
                representation += f'{c}x^{l - idx - 1}'
            elif c == 0:
                pass
        return representation

    def evaluate(self, x0):
        s = 0
        l = len(self.coeff)
        for idx, c in enumerate(self.coeff):
            p = l - 1 - idx
            s += c * x0 ** p
        return s

    def __call__(self, x0):
        return self.evaluate(x0)

    def __len__(self):
        return len(self.coeff)

    def __getitem__(self, idx):
        return self.coeff[idx]


p1 = Poly([5, 3, 4])
print(p1)
print(p1.evaluate(0))

p2 = Poly([3, 0, 0, 0, -1])
print(p2)
print(p2.evaluate(1))

print(p2(-1))
print(len(p2))

for item in p2:
    print(item)

l = [1, 2, 3, 4]
for item in l:
    print(item)

for item in p1:
    print(item)

print(p1[2])
print(p1.__getitem__(2))
