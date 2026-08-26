#10. Data Processing Pipeline
#A data pipeline receives the following array:
#[12, 7, 25, 3, 18, 10]
#Scenario:
#1. Convert the list into a NumPy array.
#2. Sort the array.
#3. Split the sorted array into two equal parts.
#4. Calculate the sum of each part.
#Output:
# ● Sorted array
# ● Two split arrays
# ● Sum of each part

import numpy as np

data = np.array([12,7,25,3,18,10])

sorted_data = np.sort(data)

part1, part2 = np.split(sorted_data,2)

print("Sorted:", sorted_data)

print("Part1:", part1)

print("Part2:", part2)

print("Sum Part1:", np.sum(part1))

print("Sum Part2:", np.sum(part2))