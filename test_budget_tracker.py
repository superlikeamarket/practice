"""Testing block."""
"""Expenses."""
expense1 = Expense(12, "Food", "Cafe 'Bread & Butter',", datetime.datetime(2020, 5, 17, 12, 45, 37))
expense2 = Expense(98, "Clothing", "H&M", datetime.datetime(2021, 7, 23, 14, 54, 34))
expense3 = Expense(200, "Withdrawal", date_time=datetime.datetime(2021, 7, 23, 7, 37, 23))

expense1.display()
expense2.display()
expense3.display()

budget_tracker =BudgetTracker()
budget_tracker.display_balance()
budget_tracker.add_expense(expense1)
budget_tracker.add_expense(expense2)
budget_tracker.add_expense(expense3)
total = budget_tracker.total_expenses()
print(f"The total of your expenses: ${total}")
budget_tracker.display_balance()

print(f"\n")
budget_tracker.list_all_expenses()

expense4 = Expense(11, "Subscriptions", "Netflix", datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
expense5 = Expense(20, "Subscriptions", "The best thing in the whole white world (GPT+) <3")
expense6 = Expense(15, "Subscriptions", "Disney+", datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
expense7 = Expense(10, "Food", date_time=datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
expense8 = Expense(5, "Subscriptions",date_time=datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
budget_tracker.add_expense(expense4)
budget_tracker.add_expense(expense5)
budget_tracker.add_expense(expense6)
budget_tracker.add_expense(expense7)
budget_tracker.add_expense(expense8)

expenses_by_date = sorted(budget_tracker.expenses, key=lambda exp: exp.date_time)

print("\nExpenses sorted by date:")
for exp in expenses_by_date:
    print(f"{exp.category}: {exp.description}, Date: {exp.date_time}")

# Step 1: Get all unique categories
categories = set(expense.category for expense in budget_tracker.expenses)
# Step 2: Print total expenses for each unique category
print("\nTotal expenses by category:")
for category in categories:
    # Print total spending for the category
    total_spent = budget_tracker.total_expense_by_category(category)
    print(f"\nYou've spent {total_spent} on {category}")
    # Step 3: List all expenses for that category
    budget_tracker.show_expenses_by_category(category)

budget_tracker.display_balance()


"""Income."""
print(f"\n")
income1 = Income(12, "Food", "Cafe 'Bread & Butter',", datetime.datetime(2020, 5, 17, 12, 45, 37))
income2 = Income(98, "Clothing", "H&M", datetime.datetime(2021, 7, 23, 14, 54, 34))
income3 = Income(200, "Withdrawal", date_time=datetime.datetime(2021, 7, 23, 7, 37, 23))

income1.display()
income2.display()
income3.display()

budget_tracker.add_income(income1)
budget_tracker.add_income(income2)
budget_tracker.add_income(income3)
total = budget_tracker.total_income()
print(f"The total of your income: ${total}")
budget_tracker.display_balance()

print(f"\n")
budget_tracker.list_all_incomes()

income4 = Income(11, "Subscriptions", "Netflix", datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
income5 = Income(20, "Subscriptions", "The best thing in the whole white world (GPT+) <3")
income6 = Income(15, "Subscriptions", "Disney+", datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
income7 = Income(10, "Food", date_time=datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
income8 = Income(5, "Subscriptions",date_time=datetime.datetime(2020, 2, 6, randint(0,23), randint(0,59), randint(0,59)))
budget_tracker.add_income(income4)
budget_tracker.add_income(income5)
budget_tracker.add_income(income6)
budget_tracker.add_income(income7)
budget_tracker.add_income(income8)

incomes_by_date = sorted(budget_tracker.incomes, key=lambda exp: exp.date_time)

print("\nIncome sorted by date:")
for exp in incomes_by_date:
    print(f"{exp.category}: {exp.description}, Date: {exp.date_time}")


# Step 1: Get all unique categories
categories = set(income.category for income in budget_tracker.incomes)
# Step 2: Print total income for each unique category
print("\nTotal income by category:")
for category in categories:
    # Print total income for the category
    total_earned = budget_tracker.total_income_by_category(category)
    print(f"\nYou've gotten {total_earned} from {category}")
    # Step 3: List all income for that category
    budget_tracker.show_income_by_category(category)

budget_tracker.display_balance()

# Test saving to a file
budget_tracker.save_to_file("budget_data.json")

# Create a new BudgetTracker instance and load the data from the file
new_budget_tracker = BudgetTracker()
print(f'\n\n')
new_budget_tracker.load_from_file("budget_data.json")

# Check if the loaded data is correct
new_budget_tracker.list_all_expenses()
new_budget_tracker.list_all_incomes()
new_budget_tracker.display_balance()


budget_tracker.generate_spending_report()

budget_tracker.display_expense_chart()