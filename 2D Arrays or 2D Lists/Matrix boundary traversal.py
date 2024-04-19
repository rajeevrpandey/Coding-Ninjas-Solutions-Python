'''
Problem statement
Given a matrix of integers containing ‘M’ rows and ‘N’ columns. Print the boundary elements of the matrix. The order of printing does not matter.

Note :

The output you will see will be in sorted order.
Your order of output does not matter.
You can return your result in any order.
Example :
Input: ‘M’ = 2, ‘N’ = 2, ‘MAT’ = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
input

Output: [1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16]
If we traverse the matrix in clockwise order from the top left then it will be 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5. Which in output will be shown in sorted order which is 1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16.
output

Referring to the image above, we are printing only the elements that lie on the boundary.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
2 <= T <= 10
1 <= N, M <= 2000

Time Limit: 1 sec
Sample Input 1 :
2
3 2
5 3 
5 7 
5 5 
2 2
6 8 
5 5 
Sample Output 1 :
3 5 5 5 5 7
5 5 6 8
Explanation Of Sample Input 1 :
For the first case:
If we do the clockwise traversal of boundary elements from the top left corner the traversal will be 5 3 5 7 5 5 but in output, you will see the elements sorted that is 3 5 5 5 5 7.

For the second case:
If we do the clockwise traversal of boundary elements from the top left corner the traversal will be 6 8 5 5 but in output, you will see the elements sorted that is 5 5 6 8.
Sample Input 2 :
2
3 3
7 3 5 
5 5 5 
8 7 7 
3 3
7 5 7 
7 2 6 
2 8 6 
Sample Output 2 :
3 5 5 5 7 7 7 8
2 5 6 6 7 7 7 8
'''


from os import *
from sys import *
from collections import *
from math import *

def matrixBoundaryTraversal(mat: [[]], m: int, n: int) -> []:
    ls = []
    for i in range(m):
        for j in range(n):
            if i==0 or j==0 or i==m-1 or j==n-1:
                ls.append(mat[i][j])
    return ls

