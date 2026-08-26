#6. Remove Outliers
#Given data:
#values = np.array([10, 12, 15, 18, 100, 14, 13])
#Task:
# ● Compute the mean and standard deviation
# ● Remove values that are more than 2 standard deviations from the mean

import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = np.mean(values)

std = np.std(values)

lower_limit = mean - 2 * std
upper_limit = mean + 2 * std

filtered_values = values[
    (values >= lower_limit) & (values <= upper_limit)
]

print("Original values:", values)
print("Mean:", mean)
print("Standard deviation:", std)
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Values after removing outliers:", filtered_values)