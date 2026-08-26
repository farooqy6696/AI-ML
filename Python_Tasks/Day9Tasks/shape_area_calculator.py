#6. Shape Area Calculator (Polymorphism)

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area =", 3.14 * self.radius * self.radius)

class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        print("Area of Rectangle =", self.lenght * self.width)

class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Triangle Area =", 0.5 * self.base * self.height)

circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

circle.area()
rectangle.area()
triangle.area()


