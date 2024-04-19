'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
4444
4444
4444
4444
Detailed explanation ( Input/output format, Notes, Images )
Constraints
0 <= N <= 50
Sample Input 1:
7
Sample Output 1:
7777777
7777777
7777777
7777777
7777777
7777777
7777777
Sample Input 1:
6
Sample Output 1:
666666
666666
666666
666666
666666
666666
'''

## Read input as specified in the question
n  = int(input())
## Print the required output in given format
for i in range(n):
    for j in range(n):
        print(n, end="")
    print()
