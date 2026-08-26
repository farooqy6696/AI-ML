import numpy as np

# Employee salaries
salaries = np.array([25000, 40000, 15000, 50000, 30000])

# Filter salaries above 30000
above_30000 = salaries[salaries > 30000]

# Count employees satisfying the condition
count = np.sum(salaries > 30000)

print("Salaries:", salaries)
print("Salaries above 30000:", above_30000)
print("Number of employees:", count)