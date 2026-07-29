import json

# Define the file where we will store our permanent data
FILENAME = "members.json"

def load_members():
    # Attempt to open the filing cabinet
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return the default hardcoded dictionary
        return {
            "Gian Clemente": 112803,
            "Hans Gabriel": 401007,
            "James Clemente": 726009
        }

def save_members(members):
    # Open the filing cabinet and overwrite the old paper with the new dictionary
    with open(FILENAME, "w") as file:
        json.dump(members, file, indent=4) 

def main():
    # 1. Start of Program: Load the persistent data from the hard drive into RAM
    members = load_members()
    change_passcode = ''
    
    password(members)
    
    while change_passcode != 'Y':
        try:
            change_passcode = input("Change password (Y/N): ").upper()
            if change_passcode == 'Y':
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
            continue # Added to loop again on error
        except ValueError:
            print("Your passcode is incorrect. Must be a number.")
            continue # Added to loop again on error
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
                
                # 2. Middle of Program: Update the dictionary in RAM
                MEMBERS[username] = new_passcode
                
                # 3. End of Action: Save the updated RAM dictionary back to the Hard Drive
                save_members(MEMBERS)
                
                print("Passcode changed successfully.")
                break
        except KeyError:
            print("Your username or password is incorrect.")
        except ValueError:
            print("Your passcode is incorrect. Must be a number.")    

if __name__ == "__main__":
    main()