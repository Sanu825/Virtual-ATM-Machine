
import random



# Sample user data (in a real system, this would be stored securely)
# Existing User data
user_data = [
    {'user_id': "Sanu", "pin": "1234", "balance": 1000},
    {'user_id': "Akash", "pin": "5678", "balance": 1500}

]

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
    return user_data[user_id]["balance"]

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
    user_data[user_id]["balance"] += amount


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
                if deposit_money(user_id, amount)
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