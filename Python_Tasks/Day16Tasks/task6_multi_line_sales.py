#6. Multi-Line Graph for Sales Comparison
#Scenario:
#data = {
#"Month": ["Jan", "Feb", "Mar"],
#"Store_A": [100, 150, 200],
#"Store_B": [90, 140, 210]
#}
#Task:
# ● Create DataFrame
# ● Plot two line graphs on same plot
# ● Add legend

import pandas as pd
import matplotlib.pyplot as plt

# Sales data for two stores
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)

# Plot Store A sales
plt.plot(df["Month"], df["Store_A"], marker="o", label="Store A")

# Plot Store B sales
plt.plot(df["Month"], df["Store_B"], marker="o", label="Store B")

# Add labels, title, and legend
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Comparison: Store A vs Store B")
plt.legend()

# Display graph
plt.show()