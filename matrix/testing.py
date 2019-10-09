class A:
    def __init__(self, number):
        self.n = number

a = A(1)
b = A(1)
print(id(a) == id(b))    # False

L1 = [1, 2, 3]
L2 = [1, 2, 3]
print(id(L1) == id(L2))  # False

c = 1
d = 1
print(id(c) == id(d))    # True