# #  single inheritance
#
# class Parent():
#     def show(self):
#         print("parent method")
#
# class Child(Parent):
#     def show1(self):
#         print("child method")
#
# p=Child()
# p.show()
# p.show1()


############################# multilevel inheritance

# class Grandparent():
#     def show(self):
#         print("grandparent method")
#
#
# class Parent(Grandparent):
#     def show1(self):
#         print("parent method")
#
#
# class Child(Parent):
#     pass
#
#
# c = Child()
# c.show()
# c.show1()


##
# multiple inheritance
#
# class Grandparent():
#     def show(self):
#         print("grandparent method")
#
#
# class Parent(Grandparent):
#     def show1(self):
#         print("parent method")
#
# class Child(Grandparent,Parent):
#     pass
# c.Child()
# c.show()
# c.show1()


# class Grandparent:
#     def show(self):
#         print("Grandparent method")
#
#
# class Parent(Grandparent):
#     def show1(self):
#         print("Parent method")
#
#
# class Child(Parent, Grandparent):
#     def show2(self):
#         print("Child method")


# c = Child()
# c.show()
# c.show1()
# c.show2()

#
# class Parent1:
#     def show1(self):
#         print("parent1 method called")
#
#
# class Parent2:
#     def show1(self):
#         print("hello")
#
#
# class Child(Parent1, Parent2):
#     def show1(self):
#         Parent1.show1(self)
#         Parent2.show1(self)
#         print("c")
#
#
# obj = Child()
# obj.show1()


# hierarchical inheritanc
class Parent:
    def show(self):
        print("parent method")


class Child1(Parent):
    def display1(self):
        print("child1 method")


class Child2(Parent):
    def display2(self):
        print("child2 method")

obj1 = Child1()
obj1.display1()
obj1.show()

obj2 = Child2()
obj2.display2()
obj2.show()
