'''
Problem statement
Print the following pattern for given number of rows.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
   5
Sample Output :
 5432*
 543*1
 54*21
 5*321
 *4321
'''
 
from os import *
from sys import *
from collections import *
from math import *

n = int(input())
for i in range(1, n+1):
    for j in range(n, 0, -1):
        if(i==j):
            print("*",end="")
        else:
            print(j,end="")
    print()

