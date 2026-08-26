#3. Employee Salary Insights
#Scenario:
#salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
#departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
#Task:
# ● Convert into DataFrame
# ● Plot:
# ○ Line graph → salary trend
# ○ Bar chart → department-wise salary comparison
# ○ Pie chart → department distribution
# ○ Histogram → salary distribution
# ○ Scatter plot → index vs salary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])

departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]


# Create DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print(df)


# Line Graph
plt.plot(df.index, df["Salary"], marker="o")

plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.title("Employee Salary Trend")

plt.show()


# Bar Chart
plt.bar(df["Department"], df["Salary"])

plt.xlabel("Department")
plt.ylabel("Salary")
plt.title("Department-wise Salary Comparison")

plt.show()


# Pie Chart
department_counts = df["Department"].value_counts()

print(department_counts)

plt.pie(
    department_counts,
    labels=department_counts.index,
    autopct="%1.1f%%"
)

plt.title("Department Distribution")

plt.show()


# Histogram
plt.hist(df["Salary"], bins=5)

plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")

plt.show()


# Scatter Plot
plt.scatter(df.index, df["Salary"])

plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.title("Employee Index vs Salary")

plt.show()