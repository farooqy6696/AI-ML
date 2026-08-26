#4. Write a recursive function to reverse a string.

def reverse_string(text):
    if len(text) == 0:
        return text
    else:
        return reverse_string(text[1:]) + text[0]

word = input("Enter a string: ")

print("Reversed string =", reverse_string(word))