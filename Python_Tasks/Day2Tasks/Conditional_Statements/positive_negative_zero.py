#1. Write a program to check whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")