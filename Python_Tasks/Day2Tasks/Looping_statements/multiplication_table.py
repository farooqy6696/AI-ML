#2. Write a program to print the multiplication table of a number using a loop.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)