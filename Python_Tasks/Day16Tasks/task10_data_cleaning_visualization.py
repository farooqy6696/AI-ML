#10. Data Cleaning + Visualization
#Scenario:
#data = np.array([100, np.nan, 200, 150, np.nan, 300])
#Task:
#1. Convert to Pandas Series
#2. Replace NaN with mean
#3. Plot:
# ○ Line graph of cleaned data
# ○ Bar chart of values > average

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data with missing values
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert NumPy array into a Pandas Series
series = pd.Series(data)

print("Original data:")
print(series)

# Calculate the mean while ignoring NaN values
mean_value = series.mean()

# Replace NaN values with the mean
cleaned_series = series.fillna(mean_value)

print("\nMean value:")
print(mean_value)

print("\nCleaned data:")
print(cleaned_series)

# Create one figure with two subplots
plt.figure(figsize=(10, 4))

# 1. Line graph of cleaned data
plt.subplot(1, 2, 1)
plt.plot(cleaned_series, marker="o")
plt.title("Cleaned Data - Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")

# 2. Bar chart of values greater than average
above_average = cleaned_series[cleaned_series > mean_value]

plt.subplot(1, 2, 2)
plt.bar(above_average.index, above_average.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Value")

plt.tight_layout()
plt.show()