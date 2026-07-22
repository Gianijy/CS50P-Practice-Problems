def main():
    members = {
        "Gian Clemente": 112803,
        "Hans Gabriel": 401007,
        "James Clemente": 726009
    }
    change_passcode = ''
    
    password(members)
    
    while change_passcode != 'Y':
        try:
            change_passcode = input("Change password (Y/N): ").upper()
            change_password(members)
            break
        except ValueError:
            print("Invalid input. Y for yes and N for no.")


def password(MEMBERS):
    while True:    
        try:
            username = input("Please enter your username: ")
            name = MEMBERS[username]
            passcode = int(input("Please enter your passcode: "))
            
            if passcode != MEMBERS[username]:
                print("Passcode incorrect")
                continue
        except KeyError:
            print("Your username or password is incorrect.")
        except ValueError:
            print("Your passcode is incorrect. Must be a number.")    
        else:
            print("The secret formula is E=MC^2")
            break


def change_password(MEMBERS):
    print("\n===CHANGE PASSWORD===")
    while True:
        try:
            username = input("Please enter your username: ")
            name = MEMBERS[username]
            passcode = int(input("Please enter your passcode: "))
            
            if passcode != MEMBERS[username]:
                print("Passcode incorrect")
                continue
            else:
                new_passcode = int(input("Please enter your new passcode: "))
                MEMBERS[username] = new_passcode
                print("Passcode changed successfully.")
                break
        except KeyError:
            print("Your username or password is incorrect.")
        except ValueError:
            print("Your passcode is incorrect. Must be a number.")    


if __name__ == "__main__":
    main()