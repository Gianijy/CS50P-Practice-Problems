BASE = 100


def main():
    division()


def division():
    while True:
        try:
            denominator = float(input("Enter a denominator (100/?): "))
            if denominator < 0:
                raise ZeroDivisionError
            final = BASE / denominator
        except ValueError:
            print("Denominator must be a float. Please try again")
            continue
        except ZeroDivisionError:
            print("Denominator cannot be 0 or negative. Please try again")
            continue
        else:
            print(f"Final answer: {final}")
            break


if __name__ == "__main__":
    main()