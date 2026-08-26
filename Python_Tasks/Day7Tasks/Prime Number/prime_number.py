num = int(input("Enter a number: "))

if num < 2:
    print(num, "is not a Prime Number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")