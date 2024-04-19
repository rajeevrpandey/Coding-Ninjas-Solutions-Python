'''
Problem statement
Given a binary number as an integer N, convert it into decimal and print.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^9
Sample Input 1 :
1100
Sample Output 1 :
12
Sample Input 2 :
111
Sample Output 2 :
7
'''

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
ans = 0
power = 0
while n :
    dig = n%10
    ans += dig * 2**power
    power +=1
    n//=10

print(ans)
