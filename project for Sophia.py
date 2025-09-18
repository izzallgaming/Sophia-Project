# Personal Budget Tracker Program
# Will also help calculate weekly percentages from other Bank tracking excel sheet table with manuel input
# This program allows users to input their monthly income and expenses,
# categorize expenses, and view a financial summary including total income,
# total expenses, remaining balance, and expense breakdown by category.

# Initialize lists and variables to store data
expenses = []  # List to store expense dictionaries with amount and category
category_totals = {}  # Dictionary to store total expenses per category

# Prompt user for monthly income with input validation
while True:
    try:
        income = float(input("Enter your monthly income: $"))  # Get income as a float
        if income < 0:
            print("Income cannot be negative. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Prompt user for the number of expenses with input validation
while True:
    try:
        num_expenses = int(input("How many expenses do you want to record? "))  # Get number of expenses
        if num_expenses < 0:
            print("Number of expenses cannot be negative. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Collect expense details if there are any expenses
if num_expenses > 0:
    for i in range(num_expenses):
        # Prompt for expense amount with validation
        while True:
            try:
                amount = float(input(f"Enter amount for expense {i+1}: $"))  # Get expense amount
                if amount <= 0:
                    print("Expense amount must be positive. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        category = input(f"Enter category for expense {i+1} (e.g., groceries, utilities): ")  # Get expense category
        expenses.append({"amount": amount, "category": category})  # Store expense as a dictionary

# Calculate total expenses by summing all expense amounts
total_expenses = sum(expense["amount"] for expense in expenses)

# Calculate remaining balance by subtracting total expenses from income
balance = income - total_expenses

# Calculate expense breakdown by category if there are expenses
if total_expenses > 0:
    # Sum expenses by category
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    # Calculate percentage for each category
    for category in category_totals:
        category_totals[category] = {
            "total": category_totals[category],
            "percentage": (category_totals[category] / total_expenses) * 100
        }

# Display the financial summary
print("\n--- Financial Summary ---")
print(f"Total Income: ${income:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${balance:.2f}")

# Display expense breakdown if there are expenses
if total_expenses > 0:
    print("\nExpense Breakdown:")
    for category, data in category_totals.items():
        print(f"{category}: ${data['total']:.2f} ({data['percentage']:.2f}%)")
else:
    print("\nNo expenses recorded.")