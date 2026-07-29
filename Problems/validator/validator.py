def main():
    password = input("Please enter your password: ")
    pswrd = check_password(password)
    print(pswrd)


def check_password(password):
    if len(password) < 8:
        raise ValueError

    return password
    

if __name__ == "__main__":
    main()