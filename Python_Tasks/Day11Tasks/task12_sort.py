#12. Sorting Customer Names A system stores customer names:
#["Ravi", "Anil", "Sita", "John"]
#Task:
# ● Convert it to a NumPy array.
# ● Sort the names alphabetically.

import numpy as np

customers = ["Ravi", "Anil", "Sita", "John"]

arr = np.array(customers)

print("Original Names:", arr)

sorted_arr = np.sort(arr)

print("Sorted Names:", sorted_arr)
