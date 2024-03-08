class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}"

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

class FixedDeposirAccount(SavingsAccount):
    def __init__(self,account_number,balance,interest_rate,tenure):
        super().__init__(account_number,balance,interest_rate)
        self.tenure=tenure

    def display_info(self):
        return f" {super().display_info()} Tenure : {self.tenure}"
    
o1=FixedDeposirAccount("67890", 5000.0, 5.0, 12)
print(o1.display_info())
print(f"Interest: ${o1.calculate_interest():.2f}")