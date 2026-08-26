#Create a Python module named calculator.py that contains functions to perform:
# Addition
# Subtraction
# Multiplication
# Division
#Then write another Python program that imports this module and performs calculations based on user input.

import calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", calculator.add(num1, num2))
print("Subtraction =", calculator.subtract(num1, num2))
print("Multiplication =", calculator.multiply(num1, num2))
print("Division =", calculator.divide(num1, num2))