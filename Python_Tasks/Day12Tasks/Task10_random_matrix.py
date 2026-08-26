import numpy as np

# Generate a 3x3 random matrix
matrix = np.random.randint(0, 51, size=(3, 3))

# Print the matrix
print("Random Matrix:")
print(matrix)

# Filter values greater than 25
filtered = matrix[matrix > 25]

# Print filtered values
print("\nValues greater than 25:")
print(filtered)