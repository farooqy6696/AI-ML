#1. Student Attendance Record

name = input("Enter student name: ")
file = open("attendance.txt", "a")
file.write(name + "\n")
file.close()

file = open("attendance.txt", "r")
print("\nAttendance Record:")
print(file.read())
file.close()