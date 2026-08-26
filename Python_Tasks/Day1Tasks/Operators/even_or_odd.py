#3. Use modulus operator to check if a number is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an Even Number")
else:
    print(number, "is an Odd Number")