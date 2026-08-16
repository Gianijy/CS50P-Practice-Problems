def main():
    bill, tip_prcnt, num_people = get_input()
    tip = calculate_tip(bill, tip_prcnt)
    total = calculate_total(tip, bill)
    per_person = calculate_per_person(total, num_people)
    
    print("===== Receipt =====")
    print(f"Customer: {num_people}")
    print(f"Tip percent: {tip_prcnt}%")
    print(f"Tip amount: ₱{tip}")
    print(f"Total bill: ₱{total}")
    print(f"Each person pays: ₱{per_person}")

def get_input():
    while True:
        try:
            bill = int(input("Bill: "))
            tip_percent = int(input("Tip percentage: "))
            num_of_people = int(input("Number of people: "))
        except ValueError:
            print("Inputs must be an integer. Please try again.")
            continue
        else:
            return bill, tip_percent, num_of_people


def calculate_tip(bill, percent):
    total_tip = (percent / 100) * bill
    return total_tip


def calculate_total(tip, bill):
    return tip + bill


def calculate_per_person(total, num_people):
    return total / num_people


if __name__ == "__main__":
    main()