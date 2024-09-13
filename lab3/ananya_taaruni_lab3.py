'''
Author: Taaruni Ananya
'''

class BankAccount:
   def __init__(self, new_name, checking_balance, savings_balance):
      self.name = new_name
      self.checking_balance = checking_balance
      self.savings_balance = savings_balance
   def deposit_checking(self, amount):
      if amount > 0:
         self.checking_balance += amount
   def deposit_savings(self, amount):
      if amount > 0:
         self.savings_balance += amount
   def withdraw_checking(self, amount):
      if amount > 0:
         self.checking_balance -= amount
   def withdraw_savings(self, amount):
      if amount > 0:
         self.savings_balance -= amount
   def transfer_to_savings(self, amount):
      if amount > 0:
         self.checking_balance -= amount
         self.savings_balance += amount

#Demo code
account = BankAccount("Mickey", 500.00, 1000.00)
account.checking_balance = 500    
account.savings_balance = 500    
account.withdraw_savings(100)
account.withdraw_checking(100)
account.transfer_to_savings(300)
print()
print(account.name)
print(f'${account.checking_balance:.2f}')
print(f'${account.savings_balance:.2f}')
print()