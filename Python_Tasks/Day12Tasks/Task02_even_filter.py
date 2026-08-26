#2. Even Number Filter (List Comprehension) A system stores numbers:
#nums = [1, 2, 3, 4, 5, 6]
#Task:
# ● Use list comprehension to create a new list containing only even numbers.

nums = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in nums if num % 2 == 0]

print("Original list:", nums)
print("Even numbers:", even_numbers)