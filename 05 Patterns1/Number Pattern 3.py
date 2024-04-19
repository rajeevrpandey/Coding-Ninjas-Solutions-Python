'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
1
11
121
1221
Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
5
Sample Output :
1
11
121
1221
12221
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
for i in range(1, n+1):
    for j in range(1, i+1):
        if(j==1 or j==i):
            print(1,end="")
        else:
            print(2, end="")
    print()

