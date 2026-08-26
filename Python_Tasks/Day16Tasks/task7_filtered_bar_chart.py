#7. Filtered Bar Chart
#Scenario:
#marks = np.array([45, 80, 60, 30, 90])
#names = ["A", "B", "C", "D", "E"]
#Task:
# ● Convert to DataFrame
# ● Filter students with marks > 50
# ● Plot bar chart only for filtered students

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student marks and names
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Filter students with marks greater than 50
filtered_df = df[df["Marks"] > 50]

# Display filtered DataFrame
print("\nFiltered DataFrame:")
print(filtered_df)

# Plot bar chart for filtered students
plt.bar(filtered_df["Name"], filtered_df["Marks"])

# Add labels and title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students with Marks Greater Than 50")

# Display graph
plt.show()