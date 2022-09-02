class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        # self.int_rate = 0.01
        # self.balance = 0
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {self.balance}")
        # your code here
        return self
    def withdraw(self, amount):
        if(self.balance < 0):
            print("Can Not Withdraw")
        else:
            self.balance -= amount
            print(f"Withdrew {self.balance}")
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        # your code here
    def yield_interest(self):
        self.balance *= self.int_rate
        print(f"Intrest Rate: {self.balance}")
        return self
        # your code here


# my_account = BankAccount(12, 100)
# their_account = BankAccount(18, 10000)

# my_account.deposit(3).withdraw(1).yield_interest().display_account_info()
# their_account.deposit(2).withdraw(4).yield_interest().display_account_info()
# my_account.yield_interest()
