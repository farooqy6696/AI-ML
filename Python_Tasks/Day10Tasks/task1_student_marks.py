#1. Student Marks Analysis A teacher stores the marks of 5 students in a NumPy array.
#Scenario: You are given marks [45, 67, 89, 56, 72].
#Task:
# ● Convert the list into a NumPy array.
# ● Add 5 grace marks to every student.
# ● Print the updated marks.

import numpy as np

marks = np.array([45, 67, 89, 56, 72])

updated_marks = marks + 5

print("Original Marks:", marks)
print("Updated Marks:", updated_marks)