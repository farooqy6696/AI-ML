#2. Student Marks Analysis
#Given marks of 5 students in 3 subjects:
#marks = np.array([
#[70, 80, 90],
#[60, 75, 85],
#[50, 65, 70],
#[90, 95, 85],
#[40, 55, 60]
#])
#Task:
# ● Calculate total marks of each student.
# ● Identify students whose total marks are above the class average.

import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

total_marks = np.sum(marks, axis=1)

class_average = np.mean(total_marks)

students_above_average = total_marks[total_marks > class_average]

print("Marks:")
print(marks)

print("Total marks of each student:", total_marks)

print("Class average:", class_average)

print("Students above class average:", students_above_average)