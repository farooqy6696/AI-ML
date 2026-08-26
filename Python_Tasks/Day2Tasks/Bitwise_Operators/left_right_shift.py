#4. Write a program to perform left shift (<<) and right shift (>>) operations on a number.

num = int(input("Enter a number: "))
shift = int(input("Enter number of positions to shift: "))

left_shift = num << shift
right_shift = num >> shift

print("Left Shift Result :", left_shift)
print("Right Shift Result:", right_shift)