'''
Problem statement
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.

Note :
For this question, you can assume that 0 raised to the power of 0 is 1


Detailed explanation ( Input/output format, Notes, Images )
Constraints:
0 <= x <= 8 
0 <= n 
Sample Input 1 :
 3 4
Sample Output 1 :
81
Sample Input 2 :
 2 5
Sample Output 2 :
32
'''

x, n = input().split()
x = int(x)
n = int(n)
# write your code logic and no need to take input !

print(x**n)

