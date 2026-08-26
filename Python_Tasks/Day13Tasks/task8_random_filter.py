#8. Random Data & Filtering
#Generate random numbers:
#nums = np.random.randint(1, 100, 10)
#Task:
# ● Filter values that are divisible by 5
# ● Return sorted result.

import numpy as np

nums = np.random.randint(1, 100, 10)

divisible_by_5 = nums[nums % 5 == 0]

sorted_result = np.sort(divisible_by_5)

print("Random numbers:", nums)
print("Numbers divisible by 5:", divisible_by_5)
print("Sorted result:", sorted_result)