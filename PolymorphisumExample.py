# There are 4 Type of Polymorphism in Python
# 1: Duck typing
# 2: Operator overloading
# 3: Method   overloading
# 4: Method   overriding

# class Python:
#     def code(self, ide):
#         ide.execute()
#
#
# class PyCharm:
#
#     def execute(self):
#         print("complied the code")
#         print("execute the code")
#
#
# class CustomEditor:
#
#     def execute(self):
#         print("complied the code")
#         print("Spell Check in  the code")
#         print("Convention Check in  the code")
#
#
# p = Python()
# ide = PyCharm()
# ide = CustomEditor()
# p.code(ide)

# class Student:
#
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         return Student(m1, m2)
#
#     def __gt__(self, other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1 > r2:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return '{},{} '.format(self.m1, self.m2)
#
#
# s1 = Student(58, 65)
# s2 = Student(65, 75)
#
# s3 = s1 + s2
#
# print(s3.__str__())
#
# if s3 > s2:
#     print("s3  wins")
# else:
#     print("s2  wins")


# class A:
#
#     def add(self, a=None, b=None, c=None):
#         s = 0
#         if a != None and b != None and c != None:
#             s = a + b + c
#         elif a != None and b != None:
#             s = a + b
#         else:
#             s = +a
#         return s
#
#
# a = A()
# print(a.add(8))


class A:
    def show(self):
        print("printing from A")


class B(A):
    def show(self):
        print("printing from B")


a = B()
a.show()
a = A()
a.show()
