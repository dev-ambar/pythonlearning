# class A:
#
#     def __init__(self):
#         print("init from A")
#
#
# class B(A):
#    #pass
#    def __init__(self):
#        super().__init__()
#        print("init from B")
#
#
# a = B()


class A:
    def __init__(self):
        print("init from A")
    def feature1(self):
        print("printing from 1-A")

class B():
    def __init__(self):
        print("init from B")
    def feature1(self):
        print("printing from 1-B")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("init from C")
    def feature2(self):
        super().feature1()

c = C()
c.feature2()
