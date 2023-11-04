import os
import csv

# Initialize budget variables
income = 0
expenses = []

# Check if the data file exists, and load existing data
data_file = "budget_data.csv"
if os.path.exists(data_file):
    with open(data_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type'] == 'Income':
                income += float(row['Amount'])
            else:
                expenses.append({'Category': row['Category'], 'Amount': float(row['Amount'])})

# Function to add income
def add_income():
    global income
    amount = float(input("Enter income amount: "))
    income += amount
    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Income', amount])
    print(f"Income of ${amount} added successfully.")

# Function to add an expense
def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({'Category': category, 'Amount': amount})
    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Expense', category, amount])
    print(f"Expense of ${amount} in the '{category}' category added successfully.")

# Function to calculate and display the remaining budget
def calculate_budget():
    total_expenses = sum(expense['Amount'] for expense in expenses)
    remaining_budget = income - total_expenses
    print(f"Total Income: ${income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Budget: ${remaining_budget}")

# Main menu
while True:
    print("\nBudget Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Calculate Budget")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_income()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        calculate_budget()
    elif choice == '4':
        print("Exiting the Budget Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

