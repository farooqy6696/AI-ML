#10. Advanced Simulation System
#Scenario: Simulate exam results and generate reports.
#Task:
# ● Generate random marks using random
# ● Store in NumPy array
# ● Convert to Pandas DataFrame
# ● Use OOP to represent Student
# ● Use conditions + loops to assign grades
# ● Save report to file
# ● Handle errors using try-except
# ● Use math module for statistics

import random
import math
import numpy as np
import pandas as pd


# Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = ""

    def assign_grade(self):

        if self.marks >= 90:
            self.grade = "A"

        elif self.marks >= 75:
            self.grade = "B"

        elif self.marks >= 60:
            self.grade = "C"

        elif self.marks >= 50:
            self.grade = "D"

        else:
            self.grade = "F"


# Student names
student_names = [
    "Rahul",
    "Priya",
    "Arun",
    "Sneha",
    "Kiran"
]


# Generate random marks
marks = np.random.randint(0, 101, size=5)

print("Generated Marks:")
print(marks)


# Create Student objects
students = []

for name, mark in zip(student_names, marks):

    student = Student(name, mark)

    student.assign_grade()

    students.append(student)


# Display student results
print("\nStudent Results:")

for student in students:

    print(
        student.name,
        student.marks,
        student.grade
    )


# Create Pandas DataFrame
data = {
    "Student": [],
    "Marks": [],
    "Grade": []
}

for student in students:

    data["Student"].append(student.name)
    data["Marks"].append(student.marks)
    data["Grade"].append(student.grade)


df = pd.DataFrame(data)

print("\nExam Report:")
print(df)


# Calculate average using NumPy
average = np.mean(marks)

print("\nAverage Marks:", average)


# Calculate average using math
total_marks = math.fsum(marks)

average_math = total_marks / len(marks)

print("Average using math:", average_math)


# Save report to file
try:

    with open("exam_report.txt", "w") as file:

        file.write("EXAM REPORT\n")
        file.write("===========\n\n")

        for student in students:

            file.write(
                f"Student: {student.name}, "
                f"Marks: {student.marks}, "
                f"Grade: {student.grade}\n"
            )

        file.write(
            f"\nAverage Marks: {average_math}\n"
        )

    print("\nReport saved successfully.")

except Exception as e:

    print("File error:", e)