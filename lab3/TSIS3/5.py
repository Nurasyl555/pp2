class Account:
    def __init__(self, owner, money):
        self.owner = owner
        self.balance = money
    def deposit(self, money):
        self.money = money
        self.balance += money
        print(f"New balance : {self.balance}")
    def withdraw(self, money_out):
        self.money_out = money_out
        if money_out > self.balance:
            print("The amount is insufficient")
p = Account("Nurasyl", 50000)
p.deposit(1000)
print(p.balance)
