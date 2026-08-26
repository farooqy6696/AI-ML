#5. Write a program to calculate the factorial of a number using a loop.

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)