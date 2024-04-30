'''
Problem statement
Given an integer N, count and return the number of zeros that are present in the given integer using recursion.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^9
Sample Input 1 :
0
Sample Output 1 :
1
Sample Input 2 :
00010204
Sample Output 2 :
2
Explanation for Sample Output 2 :
Even though "00010204" has 5 zeros, the output would still be 2 because when you convert it to an integer, it becomes 10204.
Sample Input 3 :
708000
Sample Output 3 :
4
'''
from math import *
from collections import *
from sys import *
from os import *

def count_digit(N):
    if N == 0:
        return 1
    elif N < 10:
        return 0
    elif N % 10 == 0:
        return 1 + count_digit(N // 10)
    else:
        return count_digit(N // 10)

n=int(input())
print(count_digit(n))
