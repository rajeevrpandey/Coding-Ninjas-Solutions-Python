'''
Problem statement
You have been given a 2-D array 'MAT' of size M x N where 'M' and 'N' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order.

Moreover, the first element of a row is greater than the last element of the previous row (if exists).

You are given an integer 'TARGET' and your task is to find if it exists in the given 'MAT' or not.

Example :

Given Matrix : 1 1 and Target : 8
               4 8 

The output should be "TRUE" as 8 is present in the Matrix.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 10^2
1 <= N <= 50
1 <= M <= 50
-10^5 <= MAT[i], TARGET <= 10^5

Time Limit : 1 sec
Sample Input 1 :
1
3 4 8
1 2 3 4
5 6 7 8
9 10 11 12
Sample Output 1 :
TRUE
Explanation For Sample Input 1 :

The 'TARGET' = 8 exists in the 'MAT' at index (1, 3).
Sample Input 2 :
2
3 3 78
1 2 4 
6 7 8
9 10 34
2 2 8
1 1
4 8
Sample Output 2 :
FALSE
TRUE
Explanation For Sample Input 2 :

The 'TARGET' = 78 do not exists in the 'MAT'.
The 'TARGET' = 8 exists in the 'MAT' at index (1, 1).
'''

from os import *
from sys import *
from collections import *
from math import *

def findTargetInMatrix(matrix, m, n, target):
	# Write your code here.
    start, end = 0, (m*n)-1
    while start<=end:
        mid = start + (end-start)//2
        
        item = matrix[mid//n][mid%n]
        # print(item)
        if item==target:
            return True
        elif item>target:
            end = mid-1
        else:
            start = mid+1
    return False

