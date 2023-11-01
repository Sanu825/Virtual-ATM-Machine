
import json
import random

class ATMSystem():
    def __init__(self):
        self.user_data_file = "user_data.json"  # Fixed file location
        self.users = self.load_user_data()

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
        self.users = self.load_user_data()


    # Function to authenticate the user and return the user ID if successful
    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user['user_id'] == user_id and user['pin'] == pin:
                return user
        return print("Wrong Credential")
    
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
                user['transactions'].append(transaction_text)
                self.save_user_data()

    # Function to get user mini statement
    def get_mini_statement(self, user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                if 'transactions' in user:
                    transactions = user['transactions'][-5:]    # Get the last 5 transaction
                    return transactions
                else:
                    return["No transaction yet.."]
        return []
    

    def change_pin(self, user_id, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            for user in self.users:
                if user['user_id'] == user_id:
                    user['pin'] = new_pin   # Use '=' for assignment, not '=='
                    self.save_user_data()
                    return True
        return False

# Sample ATM System
# user_data_file = "user_data.json"
# atm = ATMSystem(user_data_file)

atm = ATMSystem()


# Sample user data (in a real system, this would be stored securely)
user_data = atm.users

# Take user input or new user Credential
user_id = input("Enter the User ID or the new user: ")
pin = input("Enter the PIN for the new user: ")

# Check if the user already exists
user_ids = [user['user_id'] for user in user_data]
# user_pin = [user['pin'] for user in user_data]

if user_id in user_ids:
    print(f"User with ID {user_id} already exists.")
else:
    print("User not Found.")
    register_option = input("Do you want to register as a new user? (yes/no): ")

    if register_option.lower() == "yes":
            while True:
                pin = input("Enter your 4-digit PIN: ")

                if pin.isdigit() and len(pin) == 4:
                    break
                else:
                    print("Invalid PIN. Please enter a 4-digit number.")
                    
            balance = float(input("Enter the initial balance for the new user: "))

            new_user_data = {'user_id': user_id, 'pin': pin, 'balance': balance}
            atm.add_user(new_user_data)
            print("User registered successfully.")
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


# Main program
while True:
    user_id = input("Enter your user ID: ")
    pin =(input("Enter your PIN: "))

    # Authenticate the user
    autheticated_user = atm.authenticate_user(user_id, pin)


    if autheticated_user:

        print(f'\nWelcome "{user_id}" to our ATM System')

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
                amount = int(input("Enter the amount to withdraw: "))
                if atm.withdraw_money(autheticated_user['user_id'], amount):
                    print(f"Withdrew ${amount:.2f}. Your new balance is: ${autheticated_user['balance']:.2f}")
                else:
                    print("Insufficient balance.")
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
                    print("PIN change successfully.")
                else:
                    print("Invalid PIN. Please enter a 4-digit number.")

            elif choice == "6":
                # print("Thank you for using our ATM. Goodbye!")
                
                break
            else:
                print("Invalid choice. Please try again.")

    another_transaction = input("Do you want to perform another transaction? (yes/no): ")
    if another_transaction.lower() != "yes":
        print("Thank you for using our ATM. Goodbye!")
        break