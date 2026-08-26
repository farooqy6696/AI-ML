num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    num = num // 10

if sum == original:
    print(original, "is a strong number")
else:
    print(original, "is not a strong number")        