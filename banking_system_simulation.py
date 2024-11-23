# python 3.12.3
# A simulation of a banking system managing different account types and their balances.

class Account:
    """
    Represents a basic bank account allowing deposits, withdrawals, and balance checks.

    Attributes:
    - name (str): The name of the account holder.
    - balance (float): The current balance of the account.

    Methods:
    - deposit(amount): Adds the specified amount to the account balance.
    - withdraw(amount): Withdraws the specified amount if sufficient funds are available.
    - check_balance(): Prints the current balance of the account.
    """
    def __init__(self, name, balance):
        self.name = name  # Account holder's name
        self.balance = balance  # Initial account balance
    
    def deposit(self, amount):
        """
        Adds money to the account balance.
        
        :param amount: The amount of money to deposit (float).
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws money from the account if there are sufficient funds.
        
        :param amount: The amount to withdraw (float).
        :return: None
        """
        if amount > self.balance:
            print("Insufficient funds.")  # Notify the user if funds are insufficient
            return
        self.balance -= amount

    def check_balance(self):
        """Displays the current balance of the account."""
        print(f"There is ${self.balance} left in the account.")


class SavingsAccount(Account):
    """
    A savings account that adds interest and requires maintaining a minimum balance.

    Attributes:
    - interest_rate (float): The monthly interest rate in percentage.
    - min_balance (float): The minimum balance required to avoid penalties.

    Methods:
    - apply_interest(period): Applies the interest rate to the balance over a specified period.
    - withdraw(amount): Withdraws money with checks to ensure the minimum balance is maintained.
    - deposit(amount): Deposits money and restores the interest rate if penalties were applied.
    """
        
    def __init__(self, name, balance, interest_rate, min_balance):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance
        self.interest_backup = self.interest_rate  # Backup of the original interest rate

    def apply_interest(self, period):
        """
        Applies the interest to the balance over the specified period (in months).

        :param period: The number of months over which to apply the interest.
        """
        self.balance *= (1 + (self.interest_rate / 100)) ** period  # Compound interest calculation

    def withdraw(self, amount):
        """
        Withdraws money while checking the minimum balance requirement.

        If the balance falls below the minimum, the interest rate is set to 0%
        and a penalty equivalent to the interest rate on the minimum balance is applied.
        """
        super().withdraw(amount)
        if self.balance < self.min_balance:
            print(f"Below minimum balance! Applying penalty and setting interest rate to 0%.")
            self.interest_rate = 0
            self.balance -= (self.interest_backup * self.min_balance) / 100

    def deposit(self, amount):
        """
        Deposits money into the account and restores the interest rate if penalties were applied.
        """
        super().deposit(amount)
        if self.interest_rate == 0 and self.balance >= self.min_balance:
            self.interest_rate = self.interest_backup
            print("Interest rate restored.")


class CheckingAccount(Account):
    """
    A checking account with an overdraft feature that allows the balance to go negative up to a limit.

    Attributes:
    - overdraft_limit (float): The maximum amount the account can be overdrawn.

    Methods:
    - write_check(amount): Withdraws money using a check, allowing the account to go negative up to the overdraft limit.
    """
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def write_check(self, amount):
        """
        Withdraws money using a check, allowing the account to go negative within the overdraft limit.

        :param amount: The amount to withdraw.
        """
        if amount > (self.balance + self.overdraft_limit):
            print("Insufficient funds. Overdraft limit exceeded.")
            return
        self.balance -= amount