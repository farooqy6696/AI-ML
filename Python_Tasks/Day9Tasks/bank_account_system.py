#4. Bank Account System (Class, Object, Constructor)

class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited: ", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
         self.balance = self.balance - amount
         print("Amount Withdrawn: ", amount)
        else:
         print("Insufficient Balance")

    def display_balance(self):
        print("Account Number: ", self.account_number)
        print("Current Balance: ", self.balance)

account1 = BankAccount(12345, 10000)

account1.display_balance()

account1.deposit(2000)
account1.display_balance()

account1.withdraw(50000)
account1.display_balance()
                


                
