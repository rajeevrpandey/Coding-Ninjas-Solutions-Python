'''
Problem statement
Write a program that asks the user for a number N and a choice C. And then give them the possibility to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).



If C is equal to -
 1, then print the sum
 2, then print the product
 Any other number, then print '-1' (without the quotes)
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= N <= 12
Sample Input 1 :
10
1
Sample Output 1 :
55
Sample Input 2 :
10
2
Sample Output 2 :
3628800
Sample Input 3 :
10
4
Sample Output 3 :
-1
'''

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
n = int(input())
c = int(input())
## Print output as specified in the question.
match c:
    case 1:
        summ =0
        for i in range(1, n+1):
            summ += i
        print(summ)
    case 2:
        prod = 1
        for i in range(1, n+1):
            prod *= i
        print(prod)
    case _:
        print(-1)
