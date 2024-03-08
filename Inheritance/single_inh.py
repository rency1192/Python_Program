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


# savings_account = SavingsAccount("12345", 1000.0, 3.5)
# print(savings_account.display_info()) 
# print(f"Interest: ${savings_account.calculate_interest():.2f}")

class FixedDepositAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, tenure):
        super().__init__(account_number, balance, interest_rate)
        self.tenure = tenure

    def display_info(self):
        return f"{super().display_info()}, Tenure: {self.tenure} months"

# Example of Multilevel Inheritance
fixed_deposit_account = FixedDepositAccount("67890", 5000.0, 5.0, 12)
print(fixed_deposit_account.display_info())  # Output: Account Number: 67890, Balance: $5000.00, Tenure: 12 months
print(f"Interest: ${fixed_deposit_account.calculate_interest():.2f}")

