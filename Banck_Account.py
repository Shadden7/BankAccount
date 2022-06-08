class BankAccount:

    def __init__(self, int_rate=0, balance=0):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        self.balance -= amount
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient Funds Charging a $5 fee")  
        return self   
    def display_account_info(self):
        self.balance
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:    
            self.balance = self.balance + self.balance * self.int_rate
        return self

Account1=BankAccount(.01, balance=0)
Account2=BankAccount(.01, 0) 

Account1.deposit(500).deposit(50).deposit(50).withdrawl(100).yield_interest().display_account_info()
Account2.deposit(700).deposit(1000).withdrawl(40).withdrawl(100).withdrawl(150).withdrawl(50).yield_interest().display_account_info()