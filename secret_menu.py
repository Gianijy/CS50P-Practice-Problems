menu = {
    "Caffe Americano": 2.65,
    "Caffe Mistro": 2.85,
    "Roast Coffee": 1.75,
    "Cappuccino": 3.35,
    "Espresso": 2.45 
}
total = 0
order = []

while True:
    try:
        item = input("Please enter your order: ").title()
        order.append(item)
        total += menu[item]
    except KeyError:
        print("Item is not on the menu.")
        continue
    except EOFError:
        print(f"\nOrder now processing. Total: ${total:.2f}")
        break
        
        
    