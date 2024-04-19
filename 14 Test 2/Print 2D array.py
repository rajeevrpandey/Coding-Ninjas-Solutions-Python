'''
Problem statement
Given a 2D integer array with n rows and m columns. Print the 0th row from input n times, 1st row n-1 times…..(n-1)th row will be printed 1 time.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
3 3
1 2 3
4 5 6
7 8 9
Sample Output 1 :
1 2 3
1 2 3
1 2 3
4 5 6
4 5 6
7 8 9
'''

from os import *
from sys import *
from collections import *
from math import *

n, m = map(int, input().split())
example_matrix = []  
  
# taking RowsxColumns matrix from the user  
for i in range(n):
    # taking input for the row from the user  
    single_row = list(map(int, input().split()))  
    # appending the 'single_row' to the 'example_matrix'  
    example_matrix.append(single_row)  
for x in range(n, 0, -1):
    i=n-x
    while x:
        for j in range(m):
            print(example_matrix[i][j], end=" ")
        print()
        x-=1


