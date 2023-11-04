
import json
import random
import sys      # Import the sys module
import datetime     # Import the datetime module

class ATMSystem():
    def __init__(self):
        self.user_data_file = "user_data.json"  # Fixed file location
        self.users = self.load_user_data()
        # self.pin_changed = False    #Initialize the pin_changed flag

    # Save user data and Also used for write purpose
    def save_user_data(self):
        with open(self.user_data_file, 'w') as file:
            json.dump(self.users, file)

    # Save user data and Also read the data
    def load_user_data(self):
        try:
            with open(self.user_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    # Function to add new user into the user_data    
    def add_user(self, user_data):
        self.users.append(user_data)
        self.save_user_data()
        # print("User added successfully")

        # Update self.users with the latest data
        # self.users = self.load_user_data()


    # Function to authenticate the user and return the user ID if successful
    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user['user_id'] == user_id and user['pin'] == pin:
                return user
        # return print("Wrong Credential")
    
    # Function to check if a user exists
    def user_exists(self, user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                return True
        return False
    
    # Function to deposit money
    def deposit_money(self, user_id, amount):
        for user in self.users:
            if user['user_id'] == user_id:
                user['balance'] += amount
                self.save_user_data()   # Save the user data immediately
                self.add_transaction(user_id, f"Deposit ${amount:.2f}")    # To store transaction histry
                return True
        return False
    
    # Function to withdraw money
    def withdraw_money(self, user_id, amount):
        for user in self.users:
            if user['user_id'] == user_id:
                if user['balance'] >= amount:
                    user['balance'] -= amount
                    self.save_user_data()   # Save the user data immediately
                    self.add_transaction(user_id, f"Withdrawl ${amount:.2f}")
                    return True
        return False
    
    # Function to save user transactions 
    def add_transaction(self, user_id, transaction_text):
        for user in self.users:
            if user['user_id'] == user_id:
                if 'transactions' not in user:
                    user['transactions'] = []

                # Add this feature for note user transaction activity

                timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")   # Format - "%Y-%m-%d %H:%M:%S" -> 2023-11-04 17:31:22
                                                                                    # Format - "%d-%m-%Y %I:%M %p" -> 
                transaction_entry = f"{timestamp} - {transaction_text}"
                user['transactions'].append(transaction_entry)
                self.save_user_data()

    # Function to get user mini statement
    def get_mini_statement(self, user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                if 'transactions' in user:
                    transactions = user['transactions'][-5:]    # Get the last 5 transaction
                    current_balance = user['balance']
                    transactions_with_balance = transactions + ["\n"f"Your Current Balance: ${current_balance:.2f}"]     #  Also print the current balance
                    return transactions_with_balance
                    return transactions
                else:
                    return["No transaction yet.."]
        return []
    

    def change_pin(self, user_id, new_pin):
        while True:
            if len(new_pin) == 4 and new_pin.isdigit():
                for user in self.users:
                    if user['user_id'] == user_id:
                        user['pin'] = new_pin   # Use '=' for assignment, not '=='
                        # self.save_user_data()
                        self.pin_changed = True
                        self.save_user_data()   # Save the user data immediatly
                        print("Your PIN changed successfully. Goodbye!")
                        sys.exit()  # End the program
                        return True
            
            else:
                print("Invalid PIN. Please enter a 4-digit number.")
                retry = input("Do you want to retry changing your PIN?  (yes/no): ")
                if retry.lower() != "yes":
                        return False
                new_pin = input("Enter a new 4-digit PIN: ")



# Sample ATM System
# user_data_file = "user_data.json"
# atm = ATMSystem(user_data_file)

atm = ATMSystem()


# Sample user data (in a real system, this would be stored securely)
user_data = atm.users

# Take user input or new user Credential
user_id = input("Enter the User ID: ")

# Check if the user already exists
if atm.user_exists(user_id):
    # It ensures that if the user typing right credential then login directly
    pin = input("Enter the PIN: ")
    autheticated_user = atm.authenticate_user(user_id, pin)
    if autheticated_user:

        # print(f'\nWelcome "{user_id}" to our ATM System')
        pass
        
        # Continue with the main menu as in your existing code
    else:
        print("User ID exists but you have entered the wrong password")
        exit()
else:
    print("User not Found.")
    register_option = input("Do you want to register as a new user? (yes/no): ")

    if register_option.lower() == "yes":
            while True:
                pin = input("Create your 4-digit PIN: ")

                if pin.isdigit() and len(pin) == 4:
                    break
                else:
                    print("Invalid PIN. Please enter a 4-digit number.")
                    
            balance = float(input("Enter the initial balance for the new user: "))

            new_user_data = {'user_id': user_id, 'pin': pin, 'balance': balance}
            atm.add_user(new_user_data)
            print("User registered successfully.")
            print(f'\n\nWelcome "{user_id}" to our ATM System')

            user_id = input("Enter Your User Id: ")
            pin = input("Enter your PIN: ")

    else:
        print("Goodbye!.... Visit Again")
        exit() #Exit the main loop
    
    # user_data.append(new_user_data)   # for that traction repedate


# Display the updated list of users
# print("Updated user list: ")
# for user in user_data:
#     print(f"User ID: {user['user_id']}, PIN: {user['pin']}, Balance: {user['balance']}")


# Function to generate a unique transaction ID
def generate_transaction_id():
    return random.randint(1000, 9999)


# Function to check account balance
def check_balance(user_id):
    for user in user_data:
        if user['user_id'] == user_id:
            return user['balance']
    return None


# Initialize a flag to track weather the PIN has been changed
# pin_changed  = False

# Main program
while True:
    # if pin_changed:
    #     print(f'Goodbye! "{user_id}"Thank you for using our ATM')
    #     break
    # user_id = input("Enter your user ID: ")
    # pin =(input("Enter your PIN: "))



    # Authenticate the user
    autheticated_user = atm.authenticate_user(user_id, pin)
    if autheticated_user:

        print(f'\nWelcome "{user_id}" ')

    # If user don't exists then registered new user

        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Mini Statement")
            print("5. Change Pin")
            print("6. Exit")

            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == "1":
                print(f"Your balance is: ${autheticated_user['balance']:.2f}")

            elif choice == "2":
                while True:
                    amount_input = input("Enter the amount to withdraw: ")
                    try:
                        amount = float(amount_input)
        
                        if not amount.is_integer() or amount <= 0:
                            print("Invalid amount. Please enter a positive round number (E.g., 500, 550, 1000 etc)")
                               # Ask for input again
                        else:
                            amount = int(amount)  # Convert to an integer if it's a whole number
                            
                            if atm.withdraw_money(autheticated_user['user_id'], amount):
                                print(f"Withdrew ${amount:.2f}. Your new balance is: ${autheticated_user['balance']:.2f}")
                            else:
                                print("Insufficient balance.")     
                        break   #Exit the loop after processing the withdrawl

                    except ValueError:
                        print("Invalid input. Please enter a valid numeric amount.")
            
            elif choice == "3":
                amount = float(input("Enter the amount to deposit: "))
                if atm.deposit_money(autheticated_user['user_id'], amount):
                    print(f"Deposited ${amount:.2f}. Your new balance is: ${autheticated_user['balance']:.2f}")
            
            elif choice == "4":
                mini_statement = atm.get_mini_statement(autheticated_user['user_id'])
                print("Mini Statement:")
                for transaction in mini_statement:
                    print(transaction)

            elif choice == "5":
                new_pin = input("Enter a new 4-digit PIN: ")
                if atm.change_pin(autheticated_user['user_id'], new_pin):
                    autheticated_user['pin'] = new_pin      # update the PIN in the current user data
                    print("PIN change successfully.")
                    pin = new_pin   # Update the PIN for the current session

                # Save the modified user data to the json file
                atm.save_user_data()

            elif choice == "6":
                # print("Thank you for using our ATM. Goodbye!")
                
                break
            else:
                print("Invalid choice. Please try again.")

    another_transaction = input("Do you want to perform another transaction? (yes/no): ")
    if another_transaction.lower() != "yes":
        print("Thank you for using our ATM. Goodbye!")
        break