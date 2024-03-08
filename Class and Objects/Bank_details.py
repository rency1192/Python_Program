class Bank_Account:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("New balance is: ",self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("balance after withdrawal is : ",self.balance)
        else:
            print("Insufficient balance, can't withdraw the amount")

o1=Bank_Account("xyz",5000)
o1.deposit(1000)
o1.withdraw(2389)
