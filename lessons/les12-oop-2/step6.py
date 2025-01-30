class A:
    def __init__(self):
        print("Init A")
        super().__init__()


class B(A):
    def __init__(self):
        print("Init B")
        A.__init__(self)


class C(A):
    def __init__(self):
        print("Init C")
        A.__init__(self)


class D(B, C):
    def __init__(self):
        print("Init D")
        super().__init__()

d = D()

print(D.__mro__)
print(issubclass(D, A) )