#6. Data Analysis Tool (NumPy + Pandas)
#Scenario: Analyze student marks.
#Task:
# ● Generate marks using NumPy
# ● Convert into Pandas DataFrame
# ● Use conditions to filter passing students
# ● Calculate mean using math/NumPy
# ● Use loop to print results

import numpy as np
import pandas as pd

# Student names
students = ["Rahul", "Priya", "Arun", "Sneha", "Kiran"]

# Generate random marks using NumPy
marks = np.random.randint(0, 101, size=5)

print("Student marks:")
print(marks)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print("\nStudent Data:")
print(df)

# Filter passing students
passing_students = df[df["Marks"] >= 50]

print("\nPassing Students:")
print(passing_students)

# Calculate average using NumPy
average = np.mean(marks)

print("\nAverage Marks:", average)

# Print results using loop
print("\nAll Student Results:")

for index, row in df.iterrows():
    print(row["Student"], ":", row["Marks"])