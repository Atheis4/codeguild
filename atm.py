"""
5-16-16:

Review all classes and methods--They were made when I didn't have a firm understanding of classes.
"""

class BankAccount:
    """docstring for Account"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __eq__(self, other_entry):
        return(
            self.name == other_entry.name
            and self.balance == other_entry.balance
        )

    def __str__(self):
        return 'BankAccount(name = {}, balance = {})'.format(
            self.name,
            self.balance
        )

    def check_balance(self):
        return self.balance

    def deposit(self, deposit):
        self.deposit = deposit
        self.balance += deposit

    def withdraw(self, withdraw):
        if withdraw % 20 != 0:
            print('You can only withdraw in $20 increments.')
        elif withdraw > 300:
            print('You can\'t withdraw more than $300.')
        elif withdraw > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= withdraw

    def interest(self):
        self.interest = self.balance * 1.005
        return self.interest

def main_menu():
    print()
    print('Welcome to the Bank-O-Matic 5000:\nthe latest and greatest in faux banking technology.')
    print()
    user_input = input('What would you like to do?:\n1. Balance (BAL)\n2. Deposit (DEP)\n3. Withdraw (WIT)\n4. Interest (INT)\n(type \'done\' to end transaction)\n> ')
    return user_input

def balance(new_account):
    print(new_account)


new_account = BankAccount('Andrew', 200)

transaction = True

while transaction:
    user_input = main_menu()
    if user_input == 'done':
        balance(new_account)
        transaction = False
    if user_input == '1' or user_input == 'bal':
        balance(new_account)
    elif user_input == '2' or user_input == 'dep':
        new_account.deposit(int(input('Enter the amount you would like to deposit:\n> ')))
        balance(new_account)
    elif user_input == '3' or user_input == 'wit':
        new_account.withdraw(int(input('Enter the amount you wish to withdraw in $20 increments:\n> ')))
        balance(new_account)
    elif user_input == '4' or user_input == 'int':
        print('Your priciple with interest is {0:.2f}'.format(new_account.interest()))
        print('')


# Write a program that functions as a simple ATM for a single account.
#
# An account will be a class: it will have a field for the balance.
#
# Write functions for the account class that:
#
# Deposit to the account.
# Check if enough funds for a withdrawal.
# Withdraw an allowed amount.
# Calculate 0.5% interest on the account.
# Implement a user interface that lets a user pick each of those actions and updates the account. After each action it will print the balance.
