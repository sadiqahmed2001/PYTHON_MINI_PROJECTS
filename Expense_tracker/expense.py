import os
import json

# File to store expenses
EXPENSES_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from the file."""
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as file:
        return json.load(file)

def save_expenses(expenses):
    """Save expenses to the file."""
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense."""
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expenses.append({
        'description': description,
        'amount': amount,
        'category': category
    })
    save_expenses(expenses)
    print(f"Expense '{description}' added.")

def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("No expenses found.")
        return
    total_amount = sum(expense['amount'] for expense in expenses)
    print("Your expenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")
    print(f"Total Amount: {total_amount}")

def delete_expense(expenses):
    """Delete an expense by its number."""
    view_expenses(expenses)
    try:
        expense_num = int(input("Enter the expense number to delete: "))
        if 1 <= expense_num <= len(expenses):
            removed_expense = expenses.pop(expense_num - 1)
            save_expenses(expenses)
            print(f"Expense '{removed_expense['description']}' deleted.")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
