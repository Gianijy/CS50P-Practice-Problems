def main():
    while True:
        try:
            pin = int(input("Set your pin: "))
        except ValueError:
            print("Pin must be an int. Try again")
            continue
        else:
            passcode(pin)
            break


def passcode(pin):
    entrypin = int(input("Please enter your pin: "))
    if entrypin == pin:
        print("Access granted")


if __name__ == "__main__":
    main()