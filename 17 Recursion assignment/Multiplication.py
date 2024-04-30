'''
Problem statement
Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= M <= 1000
0 <= N <= 1000
Sample Input 1 :
3 
5
Sample Output 1 :
15
Sample Input 2 :
4 
0
Sample Output 2 :
0
'''
from math import *
from collections import *
from sys import *
from os import *

from sys import setrecursionlimit
setrecursionlimit(10**6) 

def mul(m, n):

…
m = int(input())
n = int(input())

print(mul(m,n))
