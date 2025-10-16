#  In this file we will learn the Encapsulation concept in python

# In this file, we will learn the Encapsulation concept in Python

class BankAccount:
    def __init__(self):
        # Private attributes (encapsulation)
        self.__balance = 0.00
        self.__name = ""
        self.__account_number = 0

    # Method to set account credentials
    def set_account_credentials(self):
        self.__name = input("Enter your Name: ")
        self.__account_number = input("Enter your Account Number: ")
        print(f"\nWelcome {self.__name}! Your account has been created successfully.\n")

    # Method to deposit amount
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Amount ₹{amount:.2f} deposited successfully.")
        self.show_balance()

    # Method to withdraw amount
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Insufficient balance.")
            return
        self.__balance -= amount
        print(f"Amount ₹{amount:.2f} withdrawn successfully.")
        self.show_balance()

    # Method to display account balance and details
    def show_balance(self):
        print(f"\nAccount Holder: {self.__name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Current Balance: ₹{self.__balance:.2f}")

    # Method to safely access balance (getter)
    def get_balance(self):
        return self.__balance


# ----------------- MAIN PROGRAM -----------------
print("======== Bank Management System ========")

account = BankAccount()
print("\nRegistration:")
account.set_account_credentials()

while True:
    try:
        choice = int(input(
            "\nTransaction Menu:\n"
            "1 → Check Balance\n"
            "2 → Deposit\n"
            "3 → Withdraw\n"
            "4 → Exit\n"
            "Enter your choice: "
        ))

        match choice:
            case 1:
                account.show_balance()
            case 2:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            case 3:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            case 4:
                print("\nThank you for using our service. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    except ValueError:
        print("Error: Please enter a valid number.")

'''
output :

======== Bank Management System ========

Registration:
Enter your Name: Pankaj
Enter your Account Number: ey234

Welcome Pankaj! Your account has been created successfully.


Transaction Menu:
1 → Check Balance
2 → Deposit
3 → Withdraw
4 → Exit
Enter your choice: 1

Account Holder: Pankaj
Account Number: ey234
Current Balance: ₹0.00

Transaction Menu:
1 → Check Balance
2 → Deposit
3 → Withdraw
4 → Exit
Enter your choice: 23
Invalid choice. Please try again.

Transaction Menu:
1 → Check Balance
2 → Deposit
3 → Withdraw
4 → Exit
Enter your choice: 33
Invalid choice. Please try again.

Transaction Menu:
1 → Check Balance
2 → Deposit
3 → Withdraw
4 → Exit
Enter your choice: 3
Enter withdrawal amount: 22
Error: Insufficient balance.

Transaction Menu:
1 → Check Balance
2 → Deposit
3 → Withdraw
4 → Exit
Enter your choice: 2 
Enter deposit amount: 12000
Amount ₹12000.00 deposited successfully.

Account Holder: Pankaj
Account Number: ey234
Current Balance: ₹12000.00

Transaction Menu:
1 → Check Balance
2 → Deposit
3 → Withdraw
4 → Exit
Enter your choice: 1

Account Holder: Pankaj
Account Number: ey234
Current Balance: ₹12000.00

'''