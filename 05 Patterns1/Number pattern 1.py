'''
Problem statement
Print the following pattern for the given N number of rows.

Pattern for N = 4
1
11
111
1111
Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
5
Sample Output :
1
11
111
1111
11111
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
for i in range(n):
    for j in range(i+1):
        print(1, end="")
    print()

