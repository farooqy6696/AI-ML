#4. Temperature Trend Line Plot
#Scenario: Daily temperatures:
#temps = np.array([28, 30, 32, 31, 29])
#Task:
# ● Convert into Pandas Series
# ● Plot a line graph
# ● Add title and grid

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Daily temperatures
temps = np.array([28, 30, 32, 31, 29])

# Convert NumPy array into a Pandas Series
temperature_series = pd.Series(temps)

# Display the Series
print(temperature_series)

# Plot line graph
plt.plot(temperature_series)

# Add title and grid
plt.title("Daily Temperature Trend")
plt.grid(True)

# Display graph
plt.show()