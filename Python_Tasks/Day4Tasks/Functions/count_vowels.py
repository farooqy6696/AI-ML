#19. Write a function that takes a string as input and returns the number of vowels.

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in text:
        if ch in vowels:
            count += 1

    return count

word = input("Enter a string: ")

print("Number of vowels =", count_vowels(word))