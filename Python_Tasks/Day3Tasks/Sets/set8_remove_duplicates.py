#8. Write a program to remove duplicate values from a list using a set.

numbers = [1, 2, 3, 4, 5, 6, 2, 3, 4]

unique_numbers = list(set(numbers))

print("Original List", numbers)
print("List after removing duplicates", unique_numbers)