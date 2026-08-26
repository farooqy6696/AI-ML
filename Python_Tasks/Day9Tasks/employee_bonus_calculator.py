#17. Employee Bonus Calculator (Decorators & OOP)

def bonus_decorator(func):

    def wrapper(self):
        self.salary = self.salary + 5000
        func(self)

    return wrapper


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus_decorator
    def display_salary(self):
        print("Employee Name :", self.name)
        print("Final Salary :", self.salary)


employee = Employee("Farooq", 50000)

employee.display_salary()