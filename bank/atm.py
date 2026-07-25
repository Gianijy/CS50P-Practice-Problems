import random
import re
import json
FILENAME = "bank_accounts.json"

def load_bank_data():
    # Attempt to open the filing cabinet
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an EMPTY dictionary!
        # This is a brand new bank with zero customers.
        return {}


def save_bank_data(bank_data):
    # Open the filing cabinet and overwrite it with the updated dictionary
    with open(FILENAME, "w") as file:
        json.dump(bank_data, file, indent=4)


#=====================================MAIN FUNCTION=======================================
def main():
    # 1. Start of Program: Load the data from the hard drive into RAM (The Whiteboard)
    all_accounts = load_bank_data()
    
    while True:
        option = welcome_message()
        
        if option == 1:
            account_number, fullname, pincode = create_account()
            user_folder = {
                "name": fullname,
                "pin": pincode,
                "balance": 0.0
            }

            all_accounts[account_number] = user_folder
            save_bank_data(all_accounts)
            print("Account saved successfully!")
        elif option in [2, 3, 4, 5]:
            acc_number = login(all_accounts)
            match option:
                case 2: 
                    check_balance(acc_number, all_accounts)
                case 3:
                    new_balance_withdraw = withdraw(acc_number, all_accounts)
                    all_accounts[acc_number]["balance"] = new_balance_withdraw
                    save_bank_data(all_accounts)
                    print("Withdrawn successfully!")
                case 4:
                    new_balance_deposit = deposit(acc_number, all_accounts)
                    all_accounts[acc_number]["balance"] = new_balance_deposit
                    save_bank_data(all_accounts)
                    print("Deposit saved successfully!")
                case 5:
                    new_pincode = change_pincode(acc_number, all_accounts)
                    all_accounts[acc_number]["pin"] = new_pincode
                    save_bank_data(all_accounts)
                    print("PIN updated successfully!")
        
        again = input("\nWould you like to do another transaction? (Y/N): ").upper()
        if again != "Y":
            print("Thank you for banking with Eastwest Bank. Goodbye!")
            break    
    

def welcome_message():
    print(" ===== Welcome to Eastwest Bank! =====")
    print("[1] Open an account\n[2] Check Balance\n[3] Withdraw\n[4] Deposit\n[5] Change pincode")
    while True:
        try:
            option = int(input("Service: "))
        except ValueError:
            print("Not in the option. Please try again.")
            continue
        else:
            return option


def login(all_accounts):
    while True:
        try:
            bank_account = input("Please enter your bank account number: ").replace(" ", "")
            formatted_bank_account = " ".join(re.findall(r'.{1,4}', str(bank_account)[::-1]))[::-1]
            account = all_accounts[formatted_bank_account]
            real_pin = account["pin"]
            
            pin = int(input("Please enter your pin: "))
            if pin != real_pin:
                raise ValueError
        except ValueError:
            print("Invalid bank account/pincode number. Please try again.")
            continue
        except KeyError:
            print("Bank account do not exist. Please try another account.")
            continue
        else:
            return formatted_bank_account


def create_account():
    bank_account = random.randint(100000000000, 999999999999)
    formatted_bank_account = " ".join(re.findall(r'.{1,4}', str(bank_account)[::-1]))[::-1]
    print(f"You bank account number: {formatted_bank_account}")
    while True:
        try:
            name = input("Please enter your name (FN - MN - LN): ")
            pin = int(input("Please set your pin: "))
            if len(str(abs(pin))) != 6:
                print("Pin must be 6 numbers. Please try again.")
                continue
        except ValueError:
            print("Pin must be integers.")
            continue
        else:
            return formatted_bank_account, name, pin


def check_balance(account_number, all_accounts):
    balance = all_accounts[account_number]["balance"]
    print(f"Current balance: ₱{balance:.2f}")


def withdraw(account_number, all_accounts):
    balance = all_accounts[account_number]["balance"]
    while True:
        try:
            withdraw = int(input("Amount to withdraw: ₱"))
            if withdraw > balance:
                raise ArithmeticError
            else:
                total = balance - withdraw
        except ArithmeticError:
            print("You do not have enough balance to withdraw.")
            continue
        except ValueError:
            print("Must be an integer.")
            continue
        else:
            print(f"₱{withdraw:.2f} successfully withdrawn")
            print(f"Total balance remaining: ₱{total:.2f}")
            return total


def deposit(account_number, all_accounts):
    balance = all_accounts[account_number]["balance"]
    while True:
        try:
            deposit = int(input("Enter amount to deposit: ₱"))
            if deposit < 0:
                raise ArithmeticError
            else:
                balance += deposit
        except ArithmeticError:
            print("Deposit amount cannot be negative.")
            continue
        except ValueError:
            print("Deposit amount must be a number.")
            continue
        else:
            return balance


def change_pincode(account_number, all_accounts):
    while True:
        try:
            pin = int(input("Please set your new pin: "))
            if len(str(abs(pin))) != 6:
                print("Pin must be 6 numbers. Please try again.")
                continue
        except ValueError:
            print("Pin must be integers.")
            continue
        else:
            return pin


if __name__ == "__main__":
    main()