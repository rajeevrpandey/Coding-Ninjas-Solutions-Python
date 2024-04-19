'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4




The dots represent spaces.



Detailed explanation ( Input/output format, Notes, Images )
Constraints
0 <= N <= 50
Sample Input 1:
3
Sample Output 1:
      1 
    12
  123
Sample Input 2:
4
Sample Output 2:
      1 
    12
  123
1234
'''

## Read input as specified in the question
n = int(input())
## Print the required output in given format
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j, end="")
    print()
