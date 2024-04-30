'''
Problem statement
Write a recursive function that returns the sum of the digits of a given integer.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^9
Sample Input 1 :
12345
Sample Output 1 :
15
Sample Input 2 :
9
Sample Output 2 :
9
 ''' 
from math import *
from collections import *
from sys import *
from os import *
def Sumdigit(n):
    if n <10:
        return n
    return (n%10)+Sumdigit(n//10)

N=int(input())
print(Sumdigit(N))
