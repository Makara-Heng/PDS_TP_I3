class ATM:

    def __init__(self):
        # Default variables
        self.balance = 40000

        self.cash = {
            100: 50,
            50: 20,
            20: 300,
            10: 0,
            5: 200,
            1: 10
        }

    # Display balance and available cash
    def display_balance(self):
        print("\n===== ATM INFORMATION =====")
        print(f"Account Balance: ${self.balance}")

        for denomination, quantity in self.cash.items():
            print(f"${denomination} bills: {quantity}")

    # Withdrawal method
    def withdraw(self, amount):
        try:
            
            if amount <= 0:
                print("Invalid amount!")
                return

            elif amount > self.balance:
                print("Insufficient balance!")
                return

            total_cash = sum(
                denomination * quantity
                for denomination, quantity in self.cash.items()
            )

            if amount > total_cash:
                print("Sorry! The ATM has insufficient cash.")
                return

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        remaining = amount
        withdrawn = {}

        # Calculate banknotes
        for denomination, quantity in self.cash.items():

            count = min(
                remaining // denomination,
                quantity
            )

            withdrawn[denomination] = count
            remaining -= count * denomination

        # Check available ATM cash
        if remaining > 0:
            print("ATM does not have enough cash!")
            return

        # Update ATM cash
        for denomination, count in withdrawn.items():
            self.cash[denomination] -= count

        # Update account balance
        self.balance -= amount

        print("\n===== WITHDRAWAL SUCCESS =====")
        print(f"\n\tWithdrawn: ${amount}")

        print("\tYou have received: ")
        for denomination, count in withdrawn.items():
            if count > 0:
                print(f"\t\t${denomination} x {count}")

        print(f"\tRemaining Balance: ${self.balance}")

    # Main menu
    def menu(self):

        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.display_balance()

            elif choice == "2":
                try:
                    amount = int(input("Enter amount: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input! Please enter a valid number without currency symbols.")

            elif choice == "3":
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid choice!")


# Create ATM object
atm = ATM()

# Run ATM
atm.menu()