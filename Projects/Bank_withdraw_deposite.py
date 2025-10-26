# Program to implement deposite and withdraw function in bank management system
class Bank_Account :
    def __init__(self , name ,balance = 0):
        self.name = name
        self.balance = balance
    
    def deposite(self , amount) :
        self.balance += amount
        print(f"Amount ₹{amount} is deposited succesfully\nBalance = {self.balance}")
    
    def withdraw(self , amount):
        if self.balance >= amount :
            self.balance -= amount
            print(f"Amount ₹{amount} withdraw succesfully")
        else :
            print("Insufficient Balance!")
            print(f"Balance : ₹{self.balance}")

    def display(self):
        print(f"{self.name}'s Balance: ₹{self.balance}")

# Main
print("****************Welcome to Our Bank****************") 
name = input("Enter your name : ")
init_balance = float(input("Enter your initial balance : "))

acc = Bank_Account(name, init_balance)

while 1 :
    choice = int(input("\nEnter 1 -> Check balance\nEnter 2 -> Deposite Amount\nEnter 3 -> Withdraw Amount\nEnter 4-> Exit\nYour choice : "))
    match choice: 
        
       case 1 :
            acc.display()
       case 2 :
            x = int(input("Enter Amount to deposite : "))
            acc.deposite(x)
       case 3 :
            x = int(input("Enter Amount to withdraw : "))
            acc.withdraw(x)
       case 4 :
            break
       case _:
        print("Invalid day number")
