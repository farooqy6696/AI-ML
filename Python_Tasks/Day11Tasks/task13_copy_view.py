#13. Copy vs View Behavior in Data Processing
#Scenario: A dataset:
#[10, 20, 30, 40]
#Task:
# ● Create a copy of the array.
# ● Modify the original array.
# ● Show that the copy does not change.
# ● Repeat using view() and observe the difference.

import numpy as np

original = np.array([10, 20, 30, 40])

copy_array = original.copy()

print("Original before modification:", original)
print("Copy before modification:", copy_array)

original[0] = 100

print("Original after modification:", original)
print("Copy after modification:", copy_array)