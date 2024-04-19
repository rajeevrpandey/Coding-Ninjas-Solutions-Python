'''
Problem statement
Print the following pattern for the given number of rows.

Note: N is always odd.


Pattern for N = 5



The dots represent spaces.




Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
x = (n+1)//2
for i in range(1,x+1):
    for s in range(x-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()
for j in range(x-1, 0, -1):
    for s in range(x-j):
        print(" ", end="")
    for j in range(2*j-1):
        print("*", end="")
    print()

