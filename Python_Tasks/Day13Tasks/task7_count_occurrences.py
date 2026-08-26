#7. Count Occurrences
#You have:
#data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
#Task:
# ● Count how many times each unique number appears.
# ● Return numbers with their counts.

import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

unique_values, counts = np.unique(data, return_counts=True)

print("Original data:", data)
print("Unique values:", unique_values)
print("Counts:", counts)