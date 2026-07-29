def main():
    valid_pass = False
    while valid_pass == False:
        password = input("Please set a password: ").strip()
        if len(password) >= 8 and password[0].isalpha():
            valid_pass = True
            print("Password valid and set.\n")

    lock = input("Please enter your password: ")
    pass_checker(password, lock)


def pass_checker(password, lock):
    if password == lock:
        print("The secret is...none. Just be you.\n")


if __name__ == "__main__":
    main()
