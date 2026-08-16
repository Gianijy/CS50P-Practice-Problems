def main():
    expenses = get_expenses()
    int_expenses = convert_int(expenses)
    total, average, num_expenses = calculate_total(int_expenses)
    int(num_expenses)
    
    print(f"Number of expenses: {num_expenses}")
    print(f"Total: ₱{total:.2f}")
    print(f"Average: {average:.2f}")
    

def get_expenses():
    expenses = []
    while True:
        expense = input("Expense: ").lower()
        if expense == "done":
            break
        else:
            expenses.append(expense)
            continue
            
    return expenses
        

def convert_int(expenses):
    int_expenses = [int(x) for x in expenses]
    return expenses


def calculate_total(expenses):
    num_exp = len(expenses)
    total_cost = 0
    
    for expense in expenses:
        total_cost += int(expense)
    
    average = total_cost / num_exp
    return float(total_cost), float(average), float(num_exp)


if __name__ == "__main__":
    main()