class Account:
    
    def __init__(self, balance = 0):
        self.balance = balance
        
    def __repr__(self):
        return(f"Account(balance:{self.balance}PLN)")

    def deposit(self, amount):
        if amount <= 0:
            return("Deposit must exceed 0PLN")
        print(f"You have made a deposit of {amount}PLN")
        self.balance += amount

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")  
        else:
            print(f"You have withdrawn {amount}PLN")
            self.balance -= amount
            

