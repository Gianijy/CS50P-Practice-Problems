def main():
    pos_int = get_int()
    steps, int_list = orbit(pos_int)
    highest_peak = max(int_list)

    print(f"\nTotal number of steps for 1 orbit: {steps}")
    print(f"Highest peak during orbit: {highest_peak}")


def get_int():
    while True:
        try:
            pos_int = int(input("Positive integer: "))
            if pos_int < 1:
                raise ValueError
        except ValueError:
            print("Wrong input. Please try again.")
            continue
        else:
            return pos_int


def orbit(pos_int):
    steps = 0
    int_list = []
    int_list.append(pos_int)
    
    while pos_int != 1:
        print(f"\nStart of while loop: {pos_int}") #remove later
        if pos_int % 2 == 0:
            pos_int //= 2
            steps += 1
            int_list.append(pos_int)
            print(f"If int is even: {pos_int}") #remove later
        else:
            pos_int = (pos_int * 3) + 1
            steps += 1
            int_list.append(pos_int)
            print(f"If int is odd: {pos_int}") #remove later                
    return steps, int_list

if __name__ == "__main__":
    main()