class A:

    def test(self):
        print(f'A class ')


class B(A):

    def test(self):
        print(f'B class ')


class C(A):
    def test(self):
        print(f'C class ')


class D(B, C):
    def test(self):
        print(f'D class ')

# Mistake MRO
# class E(C, B):
#     pass
#
# class F(D, E):
#     pass


# print(D.__mro__)
# D().test()
# F()   # TypeError: Cannot create a consistent method resolution
# order (MRO) for bases B, C
