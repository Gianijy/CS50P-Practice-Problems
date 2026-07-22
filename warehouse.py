STOCK = {
    "Pencil": 6,
    "Notebook": 11,
    "Bond Paper Rack": 4,
    "Ballpen": 17,
    "Highlighter": 9,
    "Ruler": 7
}


def main():
    inv_manager()
    for product, stock in STOCK.items():
        print(f"{product}: {stock}pcs")


def inv_manager():
    while True:
        try:
            product = input("Product: ").title()
            if product == "Done":
                break
            
            stocks = STOCK[product] #tripwire
            add_stock = int(input("Items arriving: "))
            STOCK[product] += add_stock
        except ValueError:
            print("A number is required.")
            continue
        except KeyError:
            print("Product not in inventory.")
            continue
            

if __name__ == "__main__":
    main()