#9. Write a program to count the frequency of each character in a string.

text = input("Enter a string: ")

for ch in set(text):

    print(ch, ":", text.count(ch))
