inventory = {
    "Screws": 550, 
    "Nails": 120, 
    "Hammers": 15
    }

for item, quant in inventory.items():
    if inventory[item] < 200:
        print(f"Restock needed for {item}. Current stock: {quant}pcs")