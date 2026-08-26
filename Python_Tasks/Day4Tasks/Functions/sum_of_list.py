#18. Write a function to find the sum of elements in a list using a user-defined function.

def list_sum(lst):
    total = 0
    for i in lst:

        total = total + i

    return total

numbers = [1, 2, 3, 4, 5,]

print("Sum =", list_sum(numbers))