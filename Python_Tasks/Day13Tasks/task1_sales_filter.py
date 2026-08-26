#1. Sales Threshold Filtering
#You are given monthly sales:
#sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
#Task:
# ● Filter all sales values greater than the average sales
# ● Return the filtered array.

import numpy as np

sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

average_sales = np.mean(sales)

filtered_sales = sales[sales > average_sales]

print("Sales:", sales)
print("Average sales:", average_sales)
print("Sales greater than average:", filtered_sales)