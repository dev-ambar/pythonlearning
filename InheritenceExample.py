class A:
    def feature1(self):
        print("printing feature1 from A")

    def feature2(self):
        print("printing feature2 from A")


class B:
    def feature3(self):
        print("printing feature3 from B")

    def feature4(self):
        print("printing feature4 from B")

# multiple inheritance example
class C(B,A):
    def feature5(self):
        print("printing feature5 from C")

# multilevel inheritance example
class D(C):
    def feature6(self):
        print("printing feature6 from D")

# a1 = A()
#
# a1.feature1()
# a1.feature2()
#
# b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

# c1 = C()
# c1.feature3()
# c1.feature2()
# c1.feature1()
# c1.feature4()
# c1.feature5()

d =D()
d.feature1()
d.feature2()
d.feature3()
d.feature4()
d.feature5()
d.feature6()