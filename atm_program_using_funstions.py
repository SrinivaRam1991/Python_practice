def check_pin(pin):
    return pin == "1234"

def withdraw(amount, balance):
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. New balance: {balance}")
    else:
        print("Insufficient balance")

def deposit(amount, balance):
    balance += amount
    print(f"Deposit successful. New balance: {balance}")

def main():
    balance = 5000
    pin = input("Enter your PIN: ")
    if check_pin(pin):
        print("1. Withdraw")
        print("2. Deposit")
        option = input("Select an option: ")
        if option == "1":
            amount = int(input("Enter amount to withdraw: "))
            withdraw(amount, balance)
        elif option == "2":
            amount = int(input("Enter amount to deposit: "))
            deposit(amount, balance)
        else:
            print("Invalid option")
    else:
        print("Invalid PIN")

if __name__ == "__main__":
    main()