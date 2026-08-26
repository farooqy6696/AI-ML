#5. Vehicle Management System (Inheritance)

class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print("Brand: ", self.brand)
        print("Speed: ", self.speed, "km/h")

class Car(Vehicle):  
    pass

class Bike(Vehicle):
    pass

car1 = Car("Toyoto", 180)
bike1 = Bike("Yamaha", 120)

print("Car Details")
car1.display()

print("Bike Details")
bike1.display()
  

            