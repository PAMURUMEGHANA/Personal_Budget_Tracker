import json
import os

# Function to load transactions from file
def load_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as file:
            return json.load(file)
    else:
        return {"income": [], "expenses": []}

# Function to save transactions to file
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

# Function to input expenses
def add_expense(transactions):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    transactions["expenses"].append({"category": category, "amount": amount})
    print("Expense added successfully.")

# Function to input income
def add_income(transactions):
    amount = float(input("Enter income amount: "))
    transactions["income"].append(amount)
    print("Income added successfully.")

# Function to calculate remaining budget
def calculate_budget(transactions):
    total_income = sum(transactions["income"])
    total_expenses = sum(expense["amount"] for expense in transactions["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function for expense analysis
def expense_analysis(transactions):
    categories = {}
    for expense in transactions["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        categories[category] = categories.get(category, 0) + amount
    
    print("Expense Analysis:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")

# Main function
def main():
    transactions = load_transactions()

    while True:
        print("\n1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Remaining Budget")
        print("4. Expense Analysis")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(transactions)
        elif choice == "2":
            add_income(transactions)
        elif choice == "3":
            remaining_budget = calculate_budget(transactions)
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == "4":
            expense_analysis(transactions)
        elif choice == "5":
            save_transactions(transactions)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()