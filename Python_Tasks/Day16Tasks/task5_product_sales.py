#5. Product Sales Bar Chart
#Scenario:
#products = ["Pen", "Book", "Pencil"]
#sales = np.array([50, 80, 40])
#Task:
# ● Create DataFrame
# ● Plot bar chart
# ● Add labels and title

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Product names
products = ["Pen", "Book", "Pencil"]

# Product sales
sales = np.array([50, 80, 40])

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

# Display DataFrame
print(df)

# Create bar chart
plt.bar(df["Product"], df["Sales"])

# Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")

# Display graph
plt.show()