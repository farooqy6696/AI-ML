#2. Rectangle Area Calculator (Constructor)

class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        area = self.lenght * self.width
        print("Lenght: ", self.lenght)
        print("Width: ", self.width)
        print("Area of Rectangle: ", area)

rect1 = Rectangle(10, 5)
rect1.area()            