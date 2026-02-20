from models.expense import Expense
from services.tracker import ExpenseTracker
from utils.validators import get_float_input, get_int_input


def run():
    tracker = ExpenseTracker()

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Total Expense")
        print("3. View Category-wise Total")
        print("4. View Highest Spending Category")
        print("5. View Percentage Analysis")
        print("6. Monthly Summary")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = get_float_input("Enter amount: ")
                category = input("Enter category: ")
                date = input("Enter date (YYYY-MM-DD): ")

                expense = Expense(amount, category, date)
                tracker.add_expense(expense)

                print("Expense added successfully!")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            print(f"Total Expense: ₹{tracker.calculate_total()}")

        elif choice == "3":
            totals = tracker.category_wise_total()
            if totals:
                for category, amount in totals.items():
                    print(f"{category}: ₹{amount}")
            else:
                print("No expenses recorded.")

        elif choice == "4":
            category, amount = tracker.highest_spending_category()
            if category:
                print(f"Highest Spending: {category} (₹{amount})")
            else:
                print("No expenses recorded.")

        elif choice == "5":
            percentages = tracker.percentage_analysis()
            if percentages:
                for category, percent in percentages.items():
                    print(f"{category}: {percent:.2f}%")
            else:
                print("No expenses recorded.")

        elif choice == "6":
            try:
                month = get_int_input("Enter month (1-12): ")
                year = get_int_input("Enter year: ")

                monthly_expenses = tracker.monthly_summary(month, year)
                total = tracker.calculate_total(monthly_expenses)

                print(f"Total for {month}/{year}: ₹{total}")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    run()
