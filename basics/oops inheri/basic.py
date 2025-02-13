class Shape:
    def __init__(self, color="white", border_width=1):
        self.color = color
        self.border_width = border_width

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getBorderWidth(self):
        return self.border_width

    def setBorderWidth(self, border_width):
        self.border_width = border_width


class Rectangle(Shape):
    def __init__(self, length=1, width=1, color="white", border_width=1):
        super().__init__(color, border_width)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length


class Circle(Shape):
    def __init__(self, radius=1, color="white", border_width=1):
        super().__init__(color, border_width)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius


class Triangle(Shape):
    def __init__(self, base=1, height=1, color="white", border_width=1):
        super().__init__(color, border_width)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def getBase(self):
        return self.base

    def setBase(self, base):
        self.base = base


# Example usage:
c = Circle(radius=5, color="red", border_width=2)
print("Circle Color:", c.getColor())
print("Circle Border Width:", c.getBorderWidth())
print("Circle Area:", c.area())

r = Rectangle(length=4, width=5, color="blue")
print("\nRectangle Area:", r.area())

t = Triangle(base=4, height=3)
print("\nTriangle Area:", t.area())
