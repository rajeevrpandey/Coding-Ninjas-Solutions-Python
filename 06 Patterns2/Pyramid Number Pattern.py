'''
Problem statement
Print the following pattern for the given number of rows.

Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
      212
    32123
  4321234
543212345
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.

for i in range(1, n+1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j, end="")
    for k in range(2,i+1):
        print(k, end="")
    print()

