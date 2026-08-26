#8. Write a program to check whether a string is a palindrome.

text = input("Enter a string: ")

if text == text[::-1]:

    print("Palindrome")

else:

    print("Not palindrome")    