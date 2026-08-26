#4. Write a program that searches for a number in a list and breaks the loop when found.

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter the number to search: "))

for num in numbers:
    if num == search:
        print("Number found:", num)
        break