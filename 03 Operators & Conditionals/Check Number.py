'''
Problem statement
Given an integer n, find if n is positive, negative or 0.

If n is positive, print "Positive"

If n is negative, print "Negative"

And if n is equal to 0, print "Zero".

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
-100 <= n <= 100

Sample Input 1 :
10
Sample Output 1 :
Positive
Sample Input 2 :
-10
Sample Output 2 :
Negative
'''

# write your code logic !!
n = int(input())

if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
