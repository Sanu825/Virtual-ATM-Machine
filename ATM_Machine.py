import json
import random

class ATMSystem():
    def __init__(self, user_data_file):
        self.user_data_file = user_data_file
        self.users = self()

    
    def save_user_data(self):
        with open(self.user_data_file, 'w') as file:
            json.dump(self.users, file)
# Sample user data (in a real system, this would be stored securely)
# Existing User data
atm = ATMSystem()
user_data = [
    {'user_id': "Sanu", "pin": "1234", "balance": 1000},
    {'user_id': "Akash", "pin": "5678", "balance": 1500}

]

# Take user input or new user Credential
user_id = input("Enter the User ID or the new user: ")
pin = input("Enter the PIN for the new user: ")
balance = float(input("Enter the initial balance for the new user: "))

# Check if the user already exists
user_ids = [user['user_id'] for user in user_data]

if user_id in user_ids:
    print(f"User with ID {user_id} already exists.")
else:
    new_user_data = {'user_id': user_id, 'pin': pin, 'balance': balance}
    atm.add_user(new_user_data)
    user_data.append(new_user_data)


# Function to generate a unique transaction ID
def generate_transaction_id():
    return random.randint(1000, 9999)


# Function to authenticate the user and return the user ID if successful
def authenticate_user(user_id, pin):
    for user in user_data:
        if user['user_id'] == user_id and user['pin'] == pin:
            return user_id
    return None

# Function to check account balance
def check_balance(user_id):
    for user in user_data:
        if user['user_id'] == user_id:
            return user['balance']
    return None

# Function to withdraw money
def withdraw_money(user_id, amount):
    for user in user_data:
        if user['user_id'] == user_id:
            if user['balance'] >= amount:
                user['balance'] -= amount
                return True
    return False

# Function to deposit money
def deposit_money(user_id, amount):
    for user in user_data:
        if user['user_id'] == user_id:
            user['balance'] += amount
            atm.save_user_data()


# Main program
while True:
    user_id = input("Enter your user ID: ")
    pin =(input("Enter your PIN: "))


    # Authenticate the user
    print("\nWelcome to the ATM System")
    user_id = authenticate_user(user_id, pin)

    if user_id:
        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                print(f"Your balance is: ${check_balance(user_id)}")
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                if withdraw_money(user_id, amount):
                    print(f"Withdrew ${amount}. Your new balance is: ${check_balance(user_id)}")
                else:
                    print("Insufficient balance.")
            elif choice == "3":
                amount = float(input("Enter the amount to deposit: "))
                deposit_money(user_id, amount)
                print(f"Deposited ${amount}. Your new balance is: ${check_balance(user_id)}")
            elif choice == "4":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    another_transaction = input("Do you want to perform another transaction? (yes/no): ")
    if another_transaction.lower() != "yes":
        print("Thank you for using our ATM. Goodbye!")
        break