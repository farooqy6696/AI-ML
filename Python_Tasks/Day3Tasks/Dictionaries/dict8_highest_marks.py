#8. Write a program to find the student with the highest marks from a dictionary.

students = {
    "Rahul": 85,
    "Farooq": 95
}

topper = max(students, key=students.get)

print("Topper:", topper)
print("Highest marks", students[topper])