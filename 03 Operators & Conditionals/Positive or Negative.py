'''
Problem statement
You are given an integer n. If the number is less than zero then the print ‘Negative’ otherwise the print ‘Positive’.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
-10^9<=n<=10^9
Sample Input1:
3
Sample Output 1:
Positive
Sample Input2:
-100
Sample Output 2:
Negative
'''

# Write your code here !!!!!!!!!
n = int(input())

print("Negative") if n<0 else print("Positive")
