# TODO: Account class will be defined here
# We'll build this step by step

class Account:
    def __init__(self, owner_name, initial_balance):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
        # record initial deposit transaction
        self.transactions.append(f'Deposit: {initial_balance}')

    def deposit(self, amount):
        """Add money to the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        return self.balance
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Balance: ${self.balance}")
        self.balance -= amount
        self.transactions.append(f"Withdrawal: ${amount}")
        return self.balance
    
    def get_balance(self):
        """Return the current balance"""
        return self.balance
    
    def get_transactions(self):
        """Return the list of all transactions"""
        return self.transactions