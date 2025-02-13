
# class Shape():
#     def __init__(self, c, b):
#         self.color = c
#         self.borderwidth = b
#
#     def area(self):
#         return -1
#
#     def setcolor(self, c):
#         self.color = c
#
#     def getcolor(self):
#         return self.color
#
#
# class Circle(Shape):
#     PI = 3.14
#
#     def __init__(self, r, c="", b=0):
#         self.radius = r
#         super(Circle, self).__init__(c, b)
#
#     def area(self):
#         return self.radius * self.radius * Circle.PI
#
#
# c1 = Circle(2, "red", 5)
# c2 = Circle(3, "blue")
# Circle(4)
#
# print(c1.area())
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, c='', b=0):
#         self.length = length
#         self.width = width
#         super(Rectangle, self).__init__(c, b)
#
#     def area(self):
#         return self.length * self.length
#
#
# class Triangle(Shape):
#     def __init__(self, base, height, c='', b=0):
#         self.base = base
#         self.height = height
#
#         super(Rectangle, self).__init__(c,b)
#
#     def area(self):
#         return (self.base * self.height)/2