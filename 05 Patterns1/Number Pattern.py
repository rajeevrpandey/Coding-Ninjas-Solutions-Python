'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
1234
123
12
1
Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
5
Sample Output :
12345
1234
123
12
1
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print()

