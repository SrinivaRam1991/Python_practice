class BankAccount:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully. Current balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def balance_enquiry(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.name}")
        print(f"Current Balance: {self.balance}")

    def verify_pin(self, pin):
        return pin == self.pin

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder Name: {self.name}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, name, pin, balance=0):
        if account_number not in self.accounts:
            account = BankAccount(account_number, name, pin, balance)
            self.accounts[account_number] = account
            print(f"Account opened successfully. Account details:\n{account}")
        else:
            print("Account already exists.")

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account closed successfully.")
        else:
            print("Account not found.")

    def account_holder_list(self):
        if self.accounts:
            print("Account Holder List:")
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts found.")


bank = Bank()
# Adding pre-defined account holders
bank.open_account("1234567890", "srinivas", "1234", 5000)
bank.open_account("9876543210", "Ram", "4321", 10000)

while True:
    print("\n===== Bank Management System =====")
    print("1. Open Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Balance Enquiry")
    print("5. All Account Holder List")
    print("6. Close Bank Account")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        account_number = input("Enter account number: ")
        name = input("Enter account holder name: ")
        pin = input("Enter PIN: ")
        balance = float(input("Enter opening balance: "))
        bank.open_account(account_number, name, pin, balance)
        print("Thank you for using our service. Visit again!")
    elif choice == '2':
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        if account_number in bank.accounts:
            account = bank.accounts[account_number]
            if account.verify_pin(pin):
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print("Thank you for using our service. Visit again!")
            else:
                print("Invalid PIN.")
        else:
            print("Account not found.")
    elif choice == '3':
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        if account_number in bank.accounts:
            account = bank.accounts[account_number]
            if account.verify_pin(pin):
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print("Thank you for using our service. Visit again!")
            else:
                print("Invalid PIN.")
        else:
            print("Account not found.")
    elif choice == '4':
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        if account_number in bank.accounts:
            account = bank.accounts[account_number]
            if account.verify_pin(pin):
                account.balance_enquiry()
                print("Thank you for using our service. Visit again!")
            else:
                print("Invalid PIN.")
        else:
            print("Account not found.")
    elif choice == '5':
        bank.account_holder_list()
        print("Thank you for using our service. Visit again!")
    elif choice == '6':
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        if account_number in bank.accounts:
            account = bank.accounts[account_number]
            if account.verify_pin(pin):
                bank.close_account(account_number)
                print("Thank you for using our service. Visit again!")
            else:
                print("Invalid PIN.")
        else:
            print("Account not found.")
    elif choice == '7':
        print("Thank you for using the Bank Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
