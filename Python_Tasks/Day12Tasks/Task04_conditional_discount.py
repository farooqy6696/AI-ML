#4. Conditional Discount System (List Comprehension) A shop has prices:
#prices = [100, 200, 300, 400]
#Scenario:
# ● Apply a 10% discount only if price > 200.
#Task:
# ● Use list comprehension with condition to create updated price list.

prices = [100, 200, 300, 400]

updated_prices = [
    price * 0.90 if price > 200 else price
    for price in prices
]

print("Original prices:", prices)
print("Updated prices:", updated_prices)