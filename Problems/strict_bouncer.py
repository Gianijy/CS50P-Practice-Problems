def main():
    gmail = validator()
    print(gmail)


def validator():
    while True:
        try:
            email = input("Please enter your email: ")
            if "@" not in email or " " in email:
                raise ValueError
        except ValueError:
            print("Missing '@' or contain spaces. Please try again.")
            continue
        else:
            return email
        

if __name__ == "__main__":
    main()