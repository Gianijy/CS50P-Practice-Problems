MESSY = [10, "twenty", 30, "forty", 50, 80, "ehehehe", "cappuccino"]
total = 0

for integers in MESSY:
    try:
        total += int(integers)
    except ValueError:
        pass

print(total)