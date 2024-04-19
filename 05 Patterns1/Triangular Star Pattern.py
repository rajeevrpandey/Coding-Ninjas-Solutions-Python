'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
*
**
***
****
Note : There are no spaces between the stars (*).
Detailed explanation ( Input/output format, Notes, Images )
Constraints
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
*
**
***
****
*****
Sample Input 2:
6
Sample Output 2:
*
**
***
****
*****
******
'''

## Read input as specified in the question
n = int(input())
## Print the required output in given format
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()
