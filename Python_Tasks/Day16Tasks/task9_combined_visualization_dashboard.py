#9. Combined Visualization Dashboard
#Scenario:
#sales = np.array([100, 200, 150, 300])
#products = ["A", "B", "C", "D"]
#Task:
# ● Create DataFrame
# ● Plot:
# ○ Line graph (trend)
# ○ Bar chart (comparison)
# ○ Pie chart (distribution)
# ● Show all in single figure (subplots)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sales data
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

# Display DataFrame
print(df)

# Create one figure with three subplots
plt.figure(figsize=(12, 4))

# 1. Line graph - trend
plt.subplot(1, 3, 1)
plt.plot(df["Product"], df["Sales"], marker="o")
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")

# 2. Bar chart - comparison
plt.subplot(1, 3, 2)
plt.bar(df["Product"], df["Sales"])
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

# 3. Pie chart - distribution
plt.subplot(1, 3, 3)
plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Sales Distribution")

# Adjust spacing
plt.tight_layout()

# Display all charts
plt.show()