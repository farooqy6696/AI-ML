#3. Shopping Cart System
#Scenario: A user adds items to a shopping cart.
#Task:
# ● Store items in a list
# ● Convert to set to remove duplicates
# ● Use loop + condition to calculate total cost
# ● Handle invalid input using try-except

prices = {
    "apple": 30,
    "banana": 20,
    "milk": 50,
    "bread": 40
}

cart = []

try:
    count = int(input("How many items do you want to add? "))

    for i in range(count):
        item = input("Enter item name: ").lower()
        cart.append(item)

    # Remove duplicate items
    unique_items = set(cart)

    # Calculate total cost
    total = 0

    for item in unique_items:
        if item in prices:
            total += prices[item]
        else:
            print(f"{item} is not available.")

    print("\nCart items:")
    print(unique_items)

    print("Total cost: ₹", total)

except ValueError:
    print("Invalid input. Please enter a number.")