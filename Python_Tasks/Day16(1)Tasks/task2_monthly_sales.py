#2. Monthly Sales Analysis
#Scenario:
#sales = np.array([100, 150, 200, 180, 220, 300])
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph → sales trend
# ○ Bar chart → month-wise comparison
# ○ Pie chart → contribution of each month
# ○ Histogram → frequency of sales values
# ○ Scatter plot → month index vs sales

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
sales = np.array([100, 150, 200, 180, 220, 300])

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)


# Line Graph
plt.plot(df["Month"], df["Sales"], marker="o")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")

plt.show()


# Bar Chart
plt.bar(df["Month"], df["Sales"])

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Month-wise Sales Comparison")

plt.show()


# Pie Chart
plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)

plt.title("Monthly Sales Contribution")

plt.show()


# Histogram
plt.hist(df["Sales"], bins=5)

plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales Frequency Distribution")

plt.show()


# Scatter Plot
plt.scatter(df.index, df["Sales"])

plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.title("Month Index vs Sales")

plt.show()