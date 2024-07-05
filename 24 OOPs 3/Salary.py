'''
Problem statement
Rishabh has recently learnt about custom exceptions. His friend gave him a task to initialise the salary with 500 in a class and raise an exception with message as "Insufficent funds in the account" if the withdrawl amount is greater than the bank balance otherwise display a message as " Remaining:remaining balance"

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1
400 
Sample output 1
 Remaining:100
Sample Input 1
600
Sample output 1
Insufficient funds in the account.
'''


# class InsufficientFundsException(Exception):
#     """Custom exception to be raised when there are insufficient funds in the account."""
#     def __init__(self, message="Insufficient funds in the account."):
#         self.message = message
#         super().__init__(self.message)

# class BankAccount:
#     def __init__(self):
#         self.balance = 500

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFundsException()
#         else:
#             self.balance -= amount
#             print(f" Remaining:{self.balance}")

# # Example usage
# try:
#     account = BankAccount()
#     withdraw_amount = int(input())
#     account.withdraw(withdraw_amount)
# except InsufficientFundsException as e:
#     print(e)
# except ValueError:
#     print("Please enter a valid number.")
x = int(input())
if x>500:
    print("Insufficient funds in the account.")
else:
    print("Remaining:" + str(500-x))
