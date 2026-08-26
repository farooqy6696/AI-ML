#11. Filter High Temperature Values A weather station records temperatures:
#[28, 31, 35, 27, 40, 22]
#Scenario: The system needs temperatures above 30°C.
#Task:
# ● Filter the values greater than 30 using NumPy boolean filtering.

import numpy as np

temperatures = [28, 31, 35, 27, 40, 22]

arr = np.array(temperatures)

print("Temperatures:", arr)

high_temperatures = arr[arr > 30]

print("Temperatures above 30:", high_temperatures)