#9. Online Shopping System (Multilevel Inheritance)

class Product:

    def __init__(self, name):
        self.name = name


class ElectronicProduct(Product):

    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand


class MobilePhone(ElectronicProduct):

    def __init__(self, name, brand, price):
        super().__init__(name, brand)
        self.price = price

    def display(self):
        print("Product Name :", self.name)
        print("Brand :", self.brand)
        print("Price :", self.price)


mobile = MobilePhone("Galaxy F41", "Samsung", 18500)

mobile.display()