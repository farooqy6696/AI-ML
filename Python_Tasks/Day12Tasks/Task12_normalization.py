import numpy as np

# Generate 8 random float values between 0 and 1
data = np.random.rand(8)

print("Original values:")
print(data)

# Normalize by multiplying by 100
normalized = data * 100

print("\nNormalized values:")
print(normalized)

# Filter values greater than 50
filtered = normalized[normalized > 50]

print("\nValues greater than 50:")
print(filtered)

# Sort the filtered values
sorted_values = np.sort(filtered)

print("\nSorted values:")
print(sorted_values)