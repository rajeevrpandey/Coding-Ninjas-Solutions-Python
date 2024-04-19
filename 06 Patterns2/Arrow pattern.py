'''
Problem statement
Print the following pattern for the given number of rows.

Assume N is always odd.

Note : There is space after every star. Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
11
Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
'''

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
x = (n+1)//2
for i in range(1, x+1):
    for s in range(i-1):
        print(" ",end="")
    for t in range(i):
        print("* ", end="")
    print()

