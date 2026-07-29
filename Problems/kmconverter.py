def main():
    km = float(input("Please enter distance (km): "))
    miles = km_to_miles(km)
    print(f"{km} km = {miles:.2f} miles")


def km_to_miles(kilometer):
    miles = kilometer * 0.621371
    return miles


if __name__ == "__main__":
    main()
