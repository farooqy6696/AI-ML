#3. Product Rating System An e-commerce website stores product ratings:
#[4, 5, 3, 4, 2]
#Task:
# ● Convert it to a NumPy array.
# ● Print the first and last rating using indexing.

import numpy as np

ratings = [4, 5, 3, 4, 2]

arr = np.array(ratings)

print("Product Ratings:", arr)

print("First Rating:", arr[0])

print("Last Rating:", arr[-1])