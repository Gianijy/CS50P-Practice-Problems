def main():
    fname, lname, birthyear = get_input()
    username = generate_username(fname, lname, birthyear)
    print(username)


def get_input():
    while True:
        try:
            first_name = input("First name: ")
            last_name = input("Last name: ")
            birth_year = input("Birth year: ")
        except ValueError:
            print("Input not allowed. Please try again.")
            continue
        else:
            return first_name, last_name, birth_year


def generate_username(fname, lname, birthyear):
    first = fname[0:1]
    birth = birthyear[2:]
    
    username = first + lname + birth
    return username.lower()
            

if __name__ == "__main__":
    main()