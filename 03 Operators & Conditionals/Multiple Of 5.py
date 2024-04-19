'''
Problem statement
Given a number, print " Multiple of 5" if the number is a multiple of 5, otherwise print "Not a Multiple of 5"

for N = 5
"Multiple of 5" 
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
0 <= N <= 50
Sample Input 1:
7
Sample Output 1:
Not a Multiple of 5
Sample Input 2:
10
Sample Output 2:
Multiple of 5
'''

# write your code logic !!
x= int(input())

if x%5==0:
    print("Multiple of 5")
else:
    print("Not a Multiple of 5")
