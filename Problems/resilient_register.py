INVENTORY = {
    "Ordinary Plywood": 240.00,
    "Marine Plywood": 288.00,
    "Phenolic": 600.00,
    "G.I. Wire": 999.00,
    "Plyboard": 840.00,
    "Hardieflex": 370.00,
    "Aluminum Window": 650.00
}

def main():
    display_inventory()
    take_order()


def display_inventory():
    print("Current Inventory: ")
    for item, price in INVENTORY.items():
        print(f"{item:<30} ₱{price:.2f}")
    print()


def take_order():
    total = 0
    while True:
        try:
            order = input("Order: ").title()
            if order == "Checkout":
                break
            else:
                total += INVENTORY[order]
                print(f"Current bill: {total:.2f}")
        except KeyError:
            print(f"{order} not available.")
            continue
        
    print(f"Total bill: ₱{total:.2f}")


if __name__ == "__main__":
    main()