#8. Iterate Through Daily Sales Daily sales data:
#[200, 300, 150, 400]
#Task:
# ● Store it in a NumPy array.
# ● Iterate through the array and print each sale value.

import numpy as np

sales = [200, 300, 150, 400]

arr = np.array(sales)

print("Daily Sales:", arr)

for sale in arr:
    print("Sale:", sale)