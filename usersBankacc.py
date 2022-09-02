from bankAccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.balance += amount
        print(f"Deposited: {self.account.balance}")
    # your code here
    def make_withdraw(self, amount):
        if(self.account.balance < 0):
            print("Can Not Withdraw")
        else:
            self.account.balance -= amount
            print(f"Withdrew {self.balance}")
    def display_user_balance(self):
        print(f"Balance: {self.account.balance}")
        return self

my_account = BankAccount(12, 100)
their_account = BankAccount(18, 10000)

my_account.deposit(3).withdraw(1).yield_interest().display_account_info()
their_account.deposit(2).withdraw(4).yield_interest().display_account_info()