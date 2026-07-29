DATA = {"user": {"profile": {"age": 25}}}

def main():
    print(DATA)
    age = path()
    print(age)


def path():
    while True:
        try:
            main, subdir1, subdir2 = input("Please enter the file path. Must be separated by '/': ").split("/")
            age = DATA[main][subdir1][subdir2]
        except KeyError:
            print("Wrong filepath. Please try again.")
            continue
        except ValueError:
            print("Must be separated by '/'. Please try again.")
        else:
            return age


if __name__ == "__main__":
    main()