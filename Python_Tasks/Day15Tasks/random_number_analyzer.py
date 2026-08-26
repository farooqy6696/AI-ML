#2. Random Number Analyzer
#Scenario: A system generates random numbers for testing.
#Task:
# ● Use random to generate 10 numbers
# ● Store in a list
# ● Use loop + condition to count even/odd numbers
# ● Use set to remove duplicates

import random

# Create an empty list
numbers = []

# Generate 10 random numbers
for i in range(10):
    number = random.randint(1, 20)
    numbers.append(number)

# Display random numbers
print("Random numbers:")
print(numbers)

# Count even and odd numbers
even_count = 0
odd_count = 0

for number in numbers:

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display even and odd counts
print("\nEven numbers:", even_count)
print("Odd numbers:", odd_count)

# Remove duplicates using set
unique_numbers = set(numbers)

print("\nUnique numbers:")
print(unique_numbers)