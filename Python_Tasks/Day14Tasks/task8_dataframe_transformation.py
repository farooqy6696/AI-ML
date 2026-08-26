#8. Complex DataFrame Transformation
#A DataFrame:
#df = pd.DataFrame({
#"Name": ["A", "B", "C", "D"],
#"Marks": [50, 80, 30, 90]
#})
#Scenario:
# ● Students scoring below 50 failed
#Task:
#1. Create a column Status ("Pass"/"Fail")
#2. Filter only passed students
#3. Calculate average marks of passed students

import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

print("Original DataFrame:")
print(df)

df["Status"] = df["Marks"].apply(
    lambda x: "Fail" if x < 50 else "Pass"
)

print("\nDataFrame with Status:")
print(df)

passed_students = df[df["Status"] == "Pass"]

print("\nPassed Students:")
print(passed_students)

average_marks = passed_students["Marks"].mean()

print(f"\nAverage marks of passed students: {average_marks:.2f}")