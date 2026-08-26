def check_balance(balance):
    print("\n*** BALANCE CHECKER ***")
    print("Checking Balance...")
    print(f"Your current balance is: ${balance:.2f}")


def deposit(balance):
    print("\n*** DEPOSIT AMOUNT ***")
    amount = float(input("Enter amount to deposit: $"))
    if amount < 0:
        print("Invalid Amount\n")
        return 0.0
    else:
        print(f"Successfully deposited an amount of ${amount:.2f}")
        return amount


def withdraw(balance):
    print("\n*** WITHDRAW BALANCE ***")
    amount = float(input("Enter amount to withdraw: $"))
    if amount < 0:
        print("Invalid amount")
        return 0.0
    elif amount > balance:
        print(f"Insufficient funds! Your balance is ${balance:.2f}")
        return 0.0
    else:
        print(f"Successfully withdrawn an amount of ${amount:.2f}")
        return amount


def main():
    choice = 0
    balance = 0

    while choice != 4:
        print("\n*** WELCOME TO THE BANK ***")
        print("\nSelect an option:\n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance += deposit(balance)
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("\nTHANK YOU FOR USING THE BANK! GOODBYE...")
        else:
            print("\nInvalid Choice! Please Select 1-4")


if __name__ == "__main__":
    main()

# Logic would be fun to think about hereee
