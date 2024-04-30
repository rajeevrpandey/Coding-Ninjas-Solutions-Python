'''
Problem statement
Given k, find the geometric sum i.e.

1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
Note :
using recursion.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= k <= 1000
Sample Input 1 :
3
Sample Output 1 :
1.87500
Sample Input 2 :
4
Sample Output 2 :
1.93750
Explanation for Sample Input 1:
1+ 1/(2^1) + 1/(2^2) + 1/(2^3) = 1.87500
'''

from math import *
from collections import *
from sys import *
from os import *

def Gsum(k):
    if k==0:
        return 1
    return 1/2**k + Gsum(k-1)

k = int(input())
print (str.format('{0:.5f}',Gsum(k)))
