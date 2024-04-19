'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
A
BC
CDE
DEFG
Detailed explanation ( Input/output format, Notes, Images )
Constraints
0 <= N <= 13
Sample Input 1:
5
Sample Output 1:
A
BC
CDE
DEFG
EFGHI
Sample Input 2:
6
Sample Output 2:
A
BC
CDE
DEFG
EFGHI
FGHIJK
'''

## Read input as specified in the question
n = int(input())
## Print the required output in given format
for i in range(1, n+1):
    for j in range(1,i+1):
        print(chr(ord("A")+j+i-2), end="")
    print()
