'''
Problem statement
Print the following pattern for the given number of rows.

Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
Detailed explanation ( Input/output format, Notes, Images )
Constraints
0 <= N <= 26
Sample Input 1:
8
Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH
Sample Input 2:
7
Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG
'''

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ord("A")+n-i+j-1), end="")
    print()

