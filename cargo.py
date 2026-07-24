weight = 0

while True:
    weight += int(input("Weight: "))
    if weight >= 10000:
        print(f"Remaining capacity: {10000 - weight}kg")
        print("Cargo is at maximum capacity.")
        break
    else:
        print(f"Remaining capacity: {10000 - weight}kg")
        continue