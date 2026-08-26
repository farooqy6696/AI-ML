#15. Infinite Even Number Generator (Generators)

def even_numbers():

    num = 2

    while True:
        yield num
        num = num + 2


generator = even_numbers()

n = int(input("Enter how many even numbers you want: "))

for i in range(n):
    print(next(generator))