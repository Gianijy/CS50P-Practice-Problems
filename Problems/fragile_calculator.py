while True:
    try:
        num = int(input("Input a number to multiply by 2: "))
        final = num * 2
    except ValueError:
        print("Error: not a valid integer.")
        continue
    else:
        print(f"Final answer: {final}")
        break