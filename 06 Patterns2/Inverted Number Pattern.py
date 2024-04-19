'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
4444
333
22
1
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
55555 
4444
333
22
1
Sample Input 2:
6
Sample Output 2:
666666
55555 
4444
333
22
1
'''

## Read input as specified in the question
n = int(input())
## Print the required output in given format
for i in range(n,0,-1):
    for j in range(1, i+1):
        print(i, end="")
    print()
