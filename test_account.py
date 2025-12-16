import unittest
from account import Account

class TestAccount(unittest.TestCase):
    """Unit tests for the Account class"""
    def setUp(self):
        self.account = Account("Test User", 1000)
    
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)
    
    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_negative_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-200)
    
    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
    
    def test_transaction_history(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        transactions = self.account.get_transactions()
        expected_transactions = [
            'Deposit: 1000',
            'Deposit: $200',
            'Withdrawal: $100'
        ]
        self.assertEqual(transactions, expected_transactions)

if __name__ == '__main__':
    unittest.main(exit=False)
