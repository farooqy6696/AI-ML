#7. Write a program to convert a tuple to a list and modify the element.

numbers = (10, 20, 30)

number_list = list(numbers)

number_list[2] = 100

numbers = tuple(number_list)

print(numbers)