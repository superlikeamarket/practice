# python 3.12.3 64-bit

import json
import datetime
from random import randint

"""
2. Budget Tracker/Expense Manager (Intermediate)

	•	What you'll build: A personal finance app to track income, expenses, and savings goals.
	•	Key Features:
	•	Add income and expenses (with categories like food, rent, entertainment).
	•	Visualize spending trends (e.g., via text-based graphs).
	•	Set savings goals and track progress.
	•	Generate reports based on spending patterns.
	•	Focus Areas: File handling (for storing data), working with dates, classes for categorizing expenses.
"""


class BudgetTracker:
    """
    Stores the information about all of the manipulations with the balance
    (income, expenses). Allows to manipulate individual pieces of data and
    perform calculations on them.
    """
    def __init__(self, initial_balance = 0):
        self.expenses = [] # All expenses.
        self.incomes = [] # All income. "Incomes" to distinguish from single income.
        self.balance = initial_balance # Balance tracker.

    def add_expense(self, expense):
        """Adds expense to the tracker."""
        self.expenses.append(expense)
        self.balance -= expense.amount

    def total_expenses(self):
        """Calculates total of the expenses."""
        total = sum(expense.amount for expense in self.expenses)
        return total

    def total_expense_by_category(self, category):
        """Calculates total of the expenses in a category."""
        if not any(expense.category == category for expense in self.expenses):
            raise NonExistingCategoryError(f"{category} is not among your expenses.")
        expenses_by_category = [expense.amount for expense in self.expenses if expense.category == category]
        total = sum(expenses_by_category)
        return total
    
    def list_all_expenses(self):
        """Displays all the expenses for the user."""
        print("---- Expense List ----")
        for expense in self.expenses:
            expense.display()

    def show_expenses_by_category(self, category):
        """Displays all the expenses in a category for the user."""
        if not any(expense.category == category for expense in self.expenses):
            raise NonExistingCategoryError(f"{category} is not among your expenses.")
        print(f"Your spendings on {category}:")
        for expense in self.expenses:
            if expense.category == category:
                print(f"Amount: ${expense.amount}.")
                if expense.description:
                    print(f"Description: {expense.description}.")
                else:
                    print("No description.")
                    
    def add_income(self, income):
        """Adds income to the tracker."""
        self.incomes.append(income)
        self.balance += income.amount
        
    def total_income(self):
        """Calculates total income."""
        total = sum(income.amount for income in self.incomes)
        return total
    
    def total_income_by_category(self, category):
        """Calculates total income from a category."""
        if not any(income.category == category for income in self.incomes):
            raise NonExistingCategoryError(f"{category} is not among your income sources.")
        incomes_by_category = [income.amount for income in self.incomes if income.category == category]
        total = sum(incomes_by_category)
        return total

    def list_all_incomes(self):
        """Displays all the income for the user."""
        print("---- Income List ----")
        for income in self.incomes:
            income.display()

    def show_income_by_category(self, category):
        """Displays all the income from a category for the user."""
        if not any(income.category == category for income in self.incomes):
            raise NonExistingCategoryError(f"{category} is not among your income sources.")
        print(f"Your income from {category}:")
        for income in self.incomes:
            if income.category == category:
                print(f"Amount: ${income.amount}.")
                if income.description:
                    print(f"Description: {income.description}.")
                else:
                    print("No description.")

    def display_balance(self):
        """Shows the current balance."""
        print(f"\n Current balance: {self.balance}.")

    def generate_spending_report(self): # Copied from a GPT's code
        """Generates a report of total spending by category and saves it to a file."""
        report = "---- Spending Report ----\n"
        category_totals = {}
        # Calculate total expenses per category
        for expense in self.expenses:
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount
        # Build the report string
        for category, total in category_totals.items():
            report += f"Category: {category}\nTotal Spent: ${total:.2f}\n"
        # Grand total of all expenses
        grand_total = sum(category_totals.values())
        report += f"\nGrand Total of Expenses: ${grand_total:.2f}\n"
        print(report)
        # Optionally save the report to a file
        with open('spending_report.txt', 'w') as file:
            file.write(report)
        print("Spending report saved to 'spending_report.txt'.")

    def display_expense_chart(self): ## Copied from a GPT's code
        """Generates a simple horizontal bar chart for expenses by category."""
        # Create a dictionary to hold total expenses by category
        expense_by_category = {}
        # Loop through all expenses and group them by category
        for expense in self.expenses:
            if expense.category in expense_by_category:
                expense_by_category[expense.category] += expense.amount
            else:
                expense_by_category[expense.category] = expense.amount
        # Find the maximum expense to scale the graph
        max_amount = max(expense_by_category.values())
        # Generate and display the bar chart
        for category, total_amount in expense_by_category.items():
            bar_length = (total_amount * 50) // max_amount  # Scale the bar to fit within 50 characters
            bar = '#' * bar_length
            print(f"{category}: {bar} (${total_amount:.2f})")

    def save_to_file(self, filename):
        """Save the current expenses and income to a file."""
        data = {
            'expenses': [
                {
                    'amount': expense.amount,
                    'category': expense.category,
                    'description': expense.description,
                    'date_time': expense.date_time.isoformat() if expense.date_time else None
                }
                for expense in self.expenses
            ],
            'incomes': [
                {
                    'amount': income.amount,
                    'category': income.category,
                    'description': income.description,
                    'date_time': income.date_time.isoformat() if income.date_time else None
                }
                for income in self.incomes
            ],
            'balance': self.balance
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {filename}.")

    def load_from_file(self, filename):
        """Load expenses, incomes, and balance from a file."""
        with open(filename, 'r') as file:
            data = json.load(file)
        # Load balance
        self.balance = data['balance']
        # Load expenses
        self.expenses = [Expense(**expense) for expense in data['expenses']]
        # Load incomes
        self.incomes = [Income(**income) for income in data['incomes']]
        print(f"Data loaded from {filename}.")


    # Add methods for demonstrating graphs -- each category straight, each
    # category pie chart and 1 category over time.



class Expense:
    """
    Represents a single spending.
    """
    def __init__(self, amount, category, description = "", date_time = None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date_time = date_time if date_time else datetime.datetime.now()

    def display(self):
        print(f"You have spent ${self.amount} on {self.category} at {self.date_time}.")
        if self.description:
            print(f"Description: {self.description}.")
        else:
            print("No description.")
            

class Income:
    """
    Represents a single piece of income.
    """
    def __init__(self, amount, category, description = "", date_time = None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date_time = date_time if date_time else datetime.datetime.now()

    def display(self):
        print(f"You have got ${self.amount} from {self.category} at {self.date_time}.")
        if self.description:
            print(f"Description: {self.description}.")


"""Error block."""
class NonExistingCategoryError(Exception):
    """Raised when an category fed into a function isn't found in the category list."""
    pass

