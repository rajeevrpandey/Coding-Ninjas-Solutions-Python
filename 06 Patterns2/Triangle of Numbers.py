'''
Problem statement
Print the following pattern for the given number of rows.

Pattern for N = 4



The dots represent spaces.




Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
          232
         34543
        4567654
       567898765
Sample Input 2:
4
Sample Output 2:
           1
          232
         34543
        4567654
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.

for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(i,2*i):
        print(j, end="")
    for k in range(2*i-2,i-1,-1):
        print(k ,end="")
    print()

