import re

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        # Checking Input
        if (initial_balance < 0):
            raise ValueError("Initial balance can't be negative")
        if (not isinstance(account_number, str)):
            raise TypeError("Account number should be a string")
        if (not isinstance(account_holder_name, str)):
            raise TypeError("Account holder name should be a string")
        
        correct_name_pattern = "/^[a-z ,.'-]+$/i"
        if not re.match(correct_name_pattern, account_holder_name):
            ValueError("Provide a valid full name")

        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        # Add amount to balance with validation
        if(amount<=0):
            raise ValueError("Can't Deposit Negative Amount")
        else:
            self.balance += amount
        
    
    def withdraw(self, amount):
        # Subtract amount from balance if sufficient funds
        if(amount<=0):
            raise ValueError("Can't Withraw Negative Amount")
        elif(amount>self.balance):
            print("Insufficient funds!")
        else:
            self.balance -= amount
        
    
    def get_balance(self):
        # Return current balance
        return self.balance
    
    def print_account_info(self):
        # Return formatted account information
        print(f"Dear, {self.account_holder_name}")
        print(f"Your account number is {self.account_number}")
        print(f"Balance: {self.get_balance()}\n")

