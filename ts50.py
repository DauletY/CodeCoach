# Bank accounts

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __add__(self, other):
        total = self.balance + other.balance
        return BankAccount(total)
a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result.balance)