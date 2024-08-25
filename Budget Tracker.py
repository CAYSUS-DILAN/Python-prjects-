class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount):
        self.transactions.append({'type': 'income', 'amount': amount})
        print(f"Added income: ${amount}")

    def add_expense(self, amount):
        self.transactions.append({'type': 'expense', 'amount': amount})
        print(f"Added expense: ${amount}")

    def view_balance(self):
        balance = sum(t['amount'] if t['type'] == 'income' else -t['amount'] for t in self.transactions)
        print(f"Current balance: ${balance:.2f}")

    def view_summary(self):
        if not self.transactions:
            print("No transactions available.")
            return

        income_total = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expense_total = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')

        print("Transaction Summary:")
        print(f"Total Income: ${income_total:.2f}")
        print(f"Total Expenses: ${expense_total:.2f}")
        print(f"Net Balance: ${income_total - expense_total:.2f}")


def main():
    tracker = BudgetTracker()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            tracker.add_income(amount)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(amount)
        elif choice == '3':
            tracker.view_balance()
        elif choice == '4':
            tracker.view_summary()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
