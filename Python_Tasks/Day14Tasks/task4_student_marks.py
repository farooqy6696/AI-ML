#4. Student Marks DataFrame Analysis A DataFrame:
#data = pd.DataFrame({
#"Name": ["A", "B", "C"],
#"Math": [80, 70, 60],
#"Science": [90, 60, 70]
#})
#Task:
# ● Add a new column Total = Math + Science
# ● Find the student with the highest total marks

import pandas as pd

data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

print("Original DataFrame:")
print(data)

data["Total"] = data["Math"] + data["Science"]

print("\nDataFrame with Total:")
print(data)

highest_total = data["Total"].max()

print("\nHighest Total:")
print(highest_total)

top_student = data.loc[data["Total"].idxmax()]

print("\nStudent with highest total:")
print(top_student)

print("\nTop student name:")
print(top_student["Name"])