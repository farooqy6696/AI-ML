#4. Write a program using logical operators to check age eligibility for voting.

age = int(input("Enter your age: "))

if age >= 18 and age <= 100:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")