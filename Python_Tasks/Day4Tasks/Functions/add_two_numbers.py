#11. Write a program using a user-defined function to add two numbers.

def add(a, b):

    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum =", result)