import numpy as np

# Generate 10 random sales values between 100 and 500
sales = np.random.randint(100, 501, size=10)

# Print sales
print("Sales:", sales)

# Calculate average
average_sales = np.mean(sales)

print("Average sales:", average_sales)