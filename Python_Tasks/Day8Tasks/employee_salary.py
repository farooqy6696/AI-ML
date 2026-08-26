#6. Employee Salary Management System

file = open("Day8Tasks/employees.txt", "r")

highest_salary = 0
highest_employee = ""

print("Employee Details:")

for line in file:
    name, salary = line.split()
    print(name, salary)

    salary = int(salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

file.close()

print("\nHighest Salary:")
print(highest_employee, highest_salary)

file = open("Day8Tasks/employees.txt", "a")

name = input("Enter employee name: ")
salary = input("Enter salary: ")

file.write(name + " " + salary + "\n")

file.close()

print("New employee added successfully.")