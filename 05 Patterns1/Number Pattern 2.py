'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
1
11
202
3003
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= n <= 50
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
202
3003
40004
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
for i in range(1,n+1):
    if(i==1):
        print(1)
        continue
    for j in range(1, i+1):
        if(j==1 or j==i):
            print(i-1, end="")
        else:
            print(0, end="")
    print()

