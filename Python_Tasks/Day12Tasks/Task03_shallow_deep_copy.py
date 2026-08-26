import copy

# Employee data
employees = [[101, "A"], [102, "B"], [103, "C"]]

# Create shallow copy
shallow_copy = copy.copy(employees)

# Modify original data
employees[0][1] = "Z"

print("Original:", employees)
print("Shallow Copy:", shallow_copy)

# Create deep copy
employees = [[101, "A"], [102, "B"], [103, "C"]]

deep_copy = copy.deepcopy(employees)

# Modify original data
employees[0][1] = "Z"

print("\nAfter Deep Copy:")
print("Original:", employees)
print("Deep Copy:", deep_copy)