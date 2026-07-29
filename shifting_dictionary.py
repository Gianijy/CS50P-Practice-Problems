office = {"Alice": 1, "Bob": 2, "Charlie": 3}

for employee, desk in office.items():
    if desk == 3:
        office[employee] = 1
    else:
        office[employee] = desk + 1
    
print(office)