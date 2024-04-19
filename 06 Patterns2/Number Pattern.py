'''
Problem statement
Print the following pattern for n number of rows.

Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
For eg. N = 5 

Sample Input 1 :
4
Sample Output 1 :
'''

n = int(input())

for x in range(1, n+1):
    for i in range(1, x+1):
        print(i, end="")
    for s in range(2*(n-x)):
        print(" ", end="")
    for j in range(x, 0, -1):
        print(j, end="")
    print()
