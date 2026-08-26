#1. Student Score Processor
#Scenario: A teacher stores student names and marks in a list of tuples.
#Task:
# ● Convert data into a dictionary
# ● Use a loop + condition to find students scoring above 50
# ● Use math module to calculate average
# ● Store results in a text file

import math

students = [
    ("Rahul", 75),
    ("Priya", 45),
    ("Arun", 65),
    ("Sneha", 50),
    ("Kiran", 80)
]

# Convert list of tuples into dictionary
student_dict = dict(students)

print("Student Dictionary:")
print(student_dict)

# Find students scoring above 50
print("\nStudents scoring above 50:")

for name, marks in student_dict.items():
    if marks > 50:
        print(name, marks)

# Calculate average
marks = list(student_dict.values())

average = sum(marks) / len(marks)

average = math.floor(average)

print("\nAverage:", average)

# Store results in a file
with open("student_results.txt", "w") as file:

    file.write("Student Score Report\n")
    file.write("====================\n")

    for name, marks in student_dict.items():
        if marks > 50:
            file.write(f"{name}: {marks}\n")

    file.write(f"Average: {average}\n")

print("\nResults saved to student_results.txt")