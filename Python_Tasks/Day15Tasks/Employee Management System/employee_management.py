#5. Employee Management System (OOP + File + Dict)
#Scenario: Manage employee data.
#Task:
# ● Create a class Employee
# ● Store employees in a dictionary
# ● Save data to a file
# ● Use exception handling for invalid salary input
# ● Use loop to display all employees

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


employees = {}

# Add employees
for i in range(3):

    try:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))

        employee = Employee(emp_id, name, salary)

        employees[emp_id] = employee

    except ValueError:
        print("Invalid input. Employee was not added.")


# Display employees
print("\nEmployee Details:")

for emp_id, employee in employees.items():
    print(
        "ID:", employee.emp_id,
        "Name:", employee.name,
        "Salary:", employee.salary
    )


# Save employees to file
try:

    with open("employees.txt", "w") as file:

        for emp_id, employee in employees.items():

            file.write(
                f"ID: {employee.emp_id}, "
                f"Name: {employee.name}, "
                f"Salary: {employee.salary}\n"
            )

    print("\nEmployee data saved successfully.")

except Exception as e:
    print("File error:", e)