class A():
    def __init__(self):
        print('inside of A')


class B(A):
    pass


a1 = A()
b1 = B()


class C():
    pass


c1 = C()
print(C.__base__)


class A():
    def __init__(self):
        print('inside of A')


class B(A):
    pass


class C(A):
    def __init__(self):
        print('inside of C')


class D(B, C):
    pass


d1 = D()


class A():
    def __init__(self):
        self.x = 10
        self.z = 1000


class B(A):
    def __init__(self):
        super().__init__()
        self.w = 20


class C(A):
    def __init__(self):
        super().__init__()
        self.y = 40
        self.z = 2000


class D(B, C):
    def __init__(self):
        super().__init__()


d1 = D()
print(d1.y)
print(d1.z)
