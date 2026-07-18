def main():
    first_name = input("First name: ")
    middle_name = input("Middle name: ")
    last_name = input("Last name: ")

    full_name = f"{first_name} {middle_name} {last_name}".strip().title()
    initial = formatter(full_name)

    print(f"Full name: {full_name}")
    print(f"Initial: {initial}")


def formatter(fullname):
    initial = []
    for char in fullname:
        if char.isupper():
            initial.append(char)

    x = "".join(initial)
    return x


if __name__ == "__main__":
    main()
