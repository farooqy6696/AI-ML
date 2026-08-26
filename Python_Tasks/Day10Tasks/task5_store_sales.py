#5. Store Sales Comparison Two stores record daily sales for 3 days.
#Scenario: Store A = [200, 250, 300] Store B = [180, 270, 310]
#Task:
#● Store them in NumPy arrays.
#● Find the daily difference in sales between the two stores.
#● Print the resulting array.

import numpy as np

storeA = np.array([200,250,300])

storeB = np.array([180,270,310])

difference = storeA - storeB

print(difference)