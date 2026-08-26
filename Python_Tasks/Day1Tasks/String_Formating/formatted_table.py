#10. Print a table row using formatted strings.

name = "Farooq"
age = 27
course = "AI/ML"

print("{:<15} {:<10} {:<15}".format("Name", "Age", "Course"))
print("-" * 40)
print("{:<15} {:<10} {:<15}".format(name, age, course))