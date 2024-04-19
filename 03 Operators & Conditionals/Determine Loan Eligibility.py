'''
Problem statement
You are tasked with creating a program for a bank that determines whether a person is eligible for a loan. The eligibility criteria for the loan are as follows:

Conditions :
The person must be at least 18 years old.
The person must have a monthly income of at least $2,000.
The person must not have any outstanding loans with the bank.
Hint for Python Users:
Use the lower() function to take boolean input.
Like this, has_loans = input("").lower() == 'true'. 
Detailed explanation ( Input/output format, Notes, Images )
Sample input 1:
16
27000.78
true 
Sample output 1:
You are not eligible for the loan.
Sample input 2:
30
27450.78
false 
Sample output 2:
You are eligible for the loan.
'''

# write your code here !!
age = int(input())
inc = float(input())
out = bool(input())

print("You are eligible for the loan.") if age>18 and inc>=2000 and( out) else print("You are not eligible for the loan.")
