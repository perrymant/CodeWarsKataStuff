class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def withdraw(self, money):
        if self.balance - balance < 0:
            raise ValueError
        else:
            self.balance -= balance
        



"""
A withdraw method
Subtracts money from balence
One parameter, money to withdraw
Raise ValueError if there isn't enough money to withdraw
Return a string with name and balence(see examples)

A check method
Adds money to balence
Two parameters, other user and money
Other user will always be valid
Raise a ValueError if other user doesn't have enough money
Raise a ValueError if checking_account isn't true for other user
Return a string with name and balence plus other name and other balence(see examples)

An add_cash method
Adds money to balence
One parameter, money to add
Return a string with name and balence(see examples)
Additional Notes:

Checking_account should be stored as a boolean
No input numbers will be negitive
Output must end with period
Float numbers will not be used so, balence should be integer
No currency will be used
Examples:

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

Jeff.withdraw(2) # Returns 'Jeff has 68.'

Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

Jeff.check(Joe, 80) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

Joe.check(Jeff, 100) # Raises a ValueError

Jeff.add_cash(20.00) # Returns 'Jeff has 118.'
"""
