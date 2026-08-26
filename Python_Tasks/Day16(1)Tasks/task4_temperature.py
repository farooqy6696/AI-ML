#4. Temperature Monitoring System
#Scenario:
#temps = np.array([28, 30, 32, 35, 33, 31, 29])
#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph → daily temperature trend
# ○ Bar chart → day-wise temperature
# ○ Pie chart → proportion of high (>30) vs low temps
# ○ Histogram → temperature frequency
# ○ Scatter plot → day index vs temperature

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create data
temps = np.array([28, 30, 32, 35, 33, 31, 29])

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


# Create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)


# Line Graph
plt.plot(df["Day"], df["Temperature"], marker="o")

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Daily Temperature Trend")

plt.show()


# Bar Chart
plt.bar(df["Day"], df["Temperature"])

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Day-wise Temperature")

plt.show()


# Pie Chart
high_count = (df["Temperature"] > 30).sum()
low_count = (df["Temperature"] <= 30).sum()

labels = ["High (>30)", "Low (<=30)"]
values = [high_count, low_count]

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("High vs Low Temperature")

plt.show()


# Histogram
plt.hist(df["Temperature"], bins=5)

plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperature Frequency")

plt.show()


# Scatter Plot
plt.scatter(df.index, df["Temperature"])

plt.xlabel("Day Index")
plt.ylabel("Temperature")
plt.title("Day Index vs Temperature")

plt.show()