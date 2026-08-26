# Product details (tuples inside a dictionary) & categories set
PRODUCT_DETAILS = {
    "Pen": ("Stationery", 10),
    "Notebook": ("Stationery", 50),
    "Pencil": ("Stationery", 5)
}

PRODUCTS = {item: details[1] for item, details in PRODUCT_DETAILS.items()}
CATEGORIES = {details[0] for details in PRODUCT_DETAILS.values()}

cart = []  # Items added to cart stored in a list of dicts/tuples


def display_products():
    """Displays available products and their prices."""
    print("Available Products:")
    for name, price in PRODUCTS.items():
        print(f"{name}: {price}")


def add_to_cart():
    """Adds a valid product and quantity to the cart."""
    try:
        name = input("Enter product name: ").strip()
        
        if name not in PRODUCTS:
            raise NameError("Product not found in store.")
            
        quantity_str = input("Enter quantity: ").strip()
        if not quantity_str.isdigit():
            raise ValueError("Invalid quantity! Please enter a number.")
            
        quantity = int(quantity_str)
        cart.append((name, PRODUCTS[name], quantity))
        print("Item added to cart successfully.")
        
    except NameError as e:
        print(f"NameError\n{e}")
    except ValueError as e:
        print(f"ValueError\n{e}")


def recursive_cart_total(cart_items):
    """Recursive function to compute total cart cost."""
    if not isinstance(cart_items, list):
        raise TypeError("Cart data type error.")
    if not cart_items:
        return 0
    
    item = cart_items[0]
    if not (isinstance(item, tuple) and len(item) == 3):
        raise TypeError("Cart data type error.")
        
    _, price, qty = item
    
    if not (isinstance(price, (int, float)) and isinstance(qty, int)):
        raise TypeError("Cart data type error.")
        
    return (price * qty) + recursive_cart_total(cart_items[1:])


def view_total_bill():
    """Displays items in cart and calculates total bill."""
    try:
        if not cart:
            print("Cart is empty.")
            return

        print("Items in Cart:")
        for item in cart:
            name, _, qty = item
            print(f"{name} x {qty}")
            
        # Example condition check to handle edge ZeroDivisionError requirement
        discount_factor = len(cart)
        if discount_factor == 0:
            raise ZeroDivisionError("Calculation error: division by zero.")

        total_bill = recursive_cart_total(cart)
        print(f"Total Bill: {total_bill}")

    except TypeError:
        print("TypeError\nCart data type error.")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError\n{e}")


def main():
    while True:
        print("1. Display Products")
        print("2. Add Item to Cart")
        print("3. View Total Bill")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_total_bill()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()