#3. Employee Salary System (Simple Inheritance)

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name: ", self.name)
        print("Salary: ", self.salary)

class Manager(Employee):
    pass

manager1 = Manager("Farooq", 50000)

manager1.display()