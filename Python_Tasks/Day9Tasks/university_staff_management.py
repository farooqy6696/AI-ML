#10. University Staff Management (Hierarchical Inheritance)

class Staff:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print("Name :", self.name)
        print("Department :", self.department)


class Professor(Staff):
    pass


class LabAssistant(Staff):
    pass


class Administrator(Staff):
    pass


prof = Professor("Dr. Farooq", "Computer Science")
lab = LabAssistant("Ravi", "Physics Lab")
admin = Administrator("Anita", "Administration")

print("Professor Details")
prof.display()

print()

print("Lab Assistant Details")
lab.display()

print()

print("Administrator Details")
admin.display()