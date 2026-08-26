#5. Write a program to check whether a substring exists in a string.

text = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub in text:

    print("Substring found")

else:

    print("Substring not found")