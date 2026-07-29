MENU = {
    "Coffee": 330.00,
    "Caramel": 370.00,
    "Java Chip": 390.00,
    "Mocha": 395.00,
    "Double Chocolate Chip": 410.00,
    "Caramel Java Chip": 445
}

def main():
    total = 0
    display_menu()
    orders = register()
    for order in orders:
        total += MENU[order]
    
    print(f"Total: ₱{total:.2f}")
    

def display_menu():
    print("MENU:")
    for coffee, price in MENU.items():
        print(f"{coffee:<30} ₱{price:.1f}")
    print()

def register():
    cart = []
    while True:
        try:
            order = input("What is your order: ").title().strip()
            if order == "Checkout":
                return cart
        
            price = MENU[order]
            cart.append(order)
            print(f"Added {order} to your cart.")
        except KeyError:
            print("Item is not on the menu")
            continue
    
if __name__ == "__main__":
    main()