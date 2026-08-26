#3. Expense Distribution Pie Chart
#Scenario: Monthly expenses:
#expenses = np.array([500, 300, 200])
#labels = ["Food", "Rent", "Travel"]
#Task:
# ● Create a pie chart
# ● Show percentage distribution

import numpy as np
import matplotlib.pyplot as plt

# Monthly expenses
expenses = np.array([500, 300, 200])

# Expense categories
labels = ["Food", "Rent", "Travel"]

# Create pie chart
plt.pie(expenses, labels=labels, autopct="%1.1f%%")

# Add title
plt.title("Monthly Expense Distribution")

# Display chart
plt.show()