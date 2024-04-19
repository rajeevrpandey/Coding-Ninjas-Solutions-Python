'''
Problem statement
Print the following pattern

Pattern for N = 4

*000*000*
0*00*00*0
00*0*0*00
000***000
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''

from os import *
from sys import *
from collections import *
from math import *

n = int(input())

for i in range(1, n+1):
    for o in range(1, i):
        print("0", end="")
    print("*", end="")
    for o in range(1, n-i+1):
        print("0", end="")
    print("*", end="")
    for o in range(1, n-i+1):
        print("0", end="")
    print("*", end="")
    for o in range(1, i):
        print("0", end="")
    print()

