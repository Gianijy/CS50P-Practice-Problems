MY_STR = ["apple", "application", "maple", "cat", "dog", "apricot", "grape", "pineapple", "appliances"]
TARGET = "app"

def main():
    targets = hunter()
    print("Strings with 'app':")
    for str in targets:
        print(str)


def hunter():
    str_w_app = []
    for str in MY_STR:
        if TARGET in str:
            str_w_app.append(str)
            continue
    
    return str_w_app


if __name__ == "__main__":
    main()
