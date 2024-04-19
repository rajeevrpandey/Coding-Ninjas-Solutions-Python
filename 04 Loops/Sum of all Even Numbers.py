'''
Problem statement
Given a number N, print sum of all even numbers from 1 to N.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
 6
Sample Output 1 :
12
Sample Input 2 :
 7
Sample Output 2 :
12
'''

## Read input as specified in the question.
n = int(input())
sum = 0
i=1
## Print output as specified in the question.
while i<=n:
    if(i%2==0):
        sum += i
    i += 1
print(sum)
