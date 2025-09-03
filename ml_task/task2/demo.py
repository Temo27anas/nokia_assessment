from BankAccount import BankAccount

# Create account
account = BankAccount(123456, "John Doe", 1000.50)

# Display initial info
account.print_account_info()

# Perform deposit
account.deposit(200.00)
print(f"After Deposit: 200.00")
print(f"New Balance: {account.get_balance()}")
print("-----")

# Perform withdrawal
account.withdraw(500.00)
print(f"After Withdrawal: 500.00")
print(f"New Balance: {account.get_balance()}")