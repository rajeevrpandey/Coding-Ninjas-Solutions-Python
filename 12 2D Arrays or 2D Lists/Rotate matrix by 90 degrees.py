'''
Problem statement
You are given a square matrix of non-negative integers 'MATRIX'. Your task is to rotate that array by 90 degrees in an anti-clockwise direction using constant extra space.

For example:

For given 2D array :

    [    [ 1,  2,  3 ],
         [ 4,  5,  6 ],
         [ 7,  8,  9 ]  ]

After 90 degree rotation in anti clockwise direction, it will become:

    [   [ 3,  6,  9 ],
        [ 2,  5,  8 ],
        [ 1,  4,  7 ]   ]
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 100
1 ≤ MATRIX[i][j] ≤ 10 ^ 5

Time Limit: 1 sec.
Sample Input 1:
2
3
1  2  3
4  5  6
7  8  9
4
1  2  3  4 
5  6  7  8 
9 10 11 12 
13 14 15 16
Sample Output 1:
3  6  9 
2  5  8 
1  4  7
4  8 12 16 
3  7 11 15 
2  6 10 14 
1  5  9 13
Explanation of Input 1:
For, first test case, the given matrix has been rotated by 90 degrees in an anticlockwise direction as the first row is now the first column inverted and so on for second and third rows.

For, second test case, the given matrix has been rotated by 90 degrees in an anticlockwise direction as the first row is now first column inverted and so on for second, third and fourth rows.
Sample Input 2:
2
3
7  4  1 
8  5  2 
9  6  3
4
13  9  5  1 
14  10  6  2 
15 11 7 3 
16 12 8 4
Sample Output 2:
1  2  3
4  5  6
7  8  9
1  2  3  4 
5  6  7  8 
9 10 11 12 
13 14 15 16
'''

from os import *
from sys import *
from collections import *
from math import *

def rotateMatrix(matrix):
    n = len(matrix)-1
    ans = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            row = n-j
            col = i
            ans[row][col] = matrix[i][j]
            # print(matrix[i][j])
    return ans

