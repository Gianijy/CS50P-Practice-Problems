while True:
    try:
        age = int(input("Please enter your age: "))
        if age < 18:
            print("Minors not allowed inside.")
            continue
    except ValueError:
        print("Invalid age.")
        continue
    else:
        print("You can enter.")
        break