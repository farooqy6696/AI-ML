#1. Student Performance Dashboard
#Scenario: A school records marks of students in one subject:
#marks = np.array([45, 67, 89, 56, 72, 91, 38])
#students = ["A", "B", "C", "D", "E", "F", "G"]
#Task:
# ● Convert to Pandas DataFrame
# ● Plot:
# ○ Line graph → trend of marks
# ○ Bar chart → student vs marks
# ○ Pie chart → Pass (>50) vs Fail
# ○ Histogram → distribution of marks
# ○ Scatter plot → index vs marks

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])

students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)


# Line Graph
plt.plot(df["Student"], df["Marks"], marker="o")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks Trend")
plt.show()


# Bar Chart
plt.bar(df["Student"], df["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student vs Marks")
plt.show()


# Pie Chart
pass_count = (df["Marks"] > 50).sum()
fail_count = (df["Marks"] <= 50).sum()

labels = ["Pass", "Fail"]
values = [pass_count, fail_count]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()


# Histogram
plt.hist(df["Marks"], bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Marks")
plt.show()


# Scatter Plot
plt.scatter(df.index, df["Marks"])
plt.xlabel("Index")
plt.ylabel("Marks")
plt.title("Index vs Marks")
plt.show()