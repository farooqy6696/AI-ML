#1. Student Information System (Class & Object)

class student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Roll Number :", self.roll)
        print("Marks :", self.marks)
        print("-------------------------")

student1 = student("Farooq", 21, 85)
student2 = student("Dinesh", 22, 83)
student3 = student("Vineeth", 23, 81)

student1.display()
student2.display()
student3.display()