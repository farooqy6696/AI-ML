data = [[1, 2, 3], [4, 5], [6]]

# Step 1: Flatten the nested list
flattened = [num for sublist in data for num in sublist]

# Step 2: Square only even numbers
even_squares = [
    num ** 2
    for num in flattened
    if num % 2 == 0
]

print("Original:", data)
print("Flattened:", flattened)
print("Even squares:", even_squares)