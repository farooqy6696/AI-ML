#8. Pie Chart with Conditional Data
#Scenario:
#scores = np.array([40, 60, 80, 30, 90])
#Task:
# ● Categorize into:
# ○ Pass (>50)
# ○ Fail (<=50)
# ● Count using NumPy/Pandas
# ● Plot pie chart for Pass vs Fail

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student scores
scores = np.array([40, 60, 80, 30, 90])

# Create DataFrame
df = pd.DataFrame({
    "Score": scores
})

# Categorize scores
df["Result"] = np.where(df["Score"] > 50, "Pass", "Fail")

# Count Pass and Fail
result_counts = df["Result"].value_counts()

# Display the data and counts
print(df)
print("\nPass/Fail counts:")
print(result_counts)

# Create pie chart
plt.pie(
    result_counts.values,
    labels=result_counts.index,
    autopct="%1.1f%%"
)

# Add title
plt.title("Pass vs Fail Distribution")

# Display chart
plt.show()