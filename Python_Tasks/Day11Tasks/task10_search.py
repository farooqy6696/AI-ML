#10. Find Indexes of Specific Value A quality check system stores product defect codes:
#[2, 4, 1, 4, 3, 4, 5]
#Task:
# ● Find the indexes where value = 4 using NumPy searching.

import numpy as np

defect_codes = [2, 4, 1, 4, 3, 4, 5]

arr = np.array(defect_codes)

print("Defect Codes:", arr)

indexes = np.where(arr == 4)

print("Indexes where value is 4:", indexes)