'''
Problem statement
For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:

a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)
 Mind that every element will be printed only once.

Refer to the Image:
Spiral path of a matrix

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec
Sample Input 1:
1
4 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16
Sample Output 1:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
Sample Input 2:
2
3 3 
1 2 3 
4 5 6 
7 8 9
3 1
10
20
30
Sample Output 2:
1 2 3 6 9 8 7 4 5 
10 20 30 

'''
from sys import stdin

def spiralPrint(arr, nRows, mCols):
    #Your code goes here
    if nRows==0 or mCols==0:
        return
    rows = len(arr) 
    cols = len(arr[0]) 
    startRow, startCol, endRow, endCol = 0, 0, rows-1, cols-1
    while startRow<=endRow and startCol<=endCol:
        # Print startRow 
        for j in range(startCol, endCol+1): 
            print(arr[startRow][j], end=' ')
        startRow += 1
        if startRow>endRow or startCol>endCol: 
            break 
        # Print endCol 
        for i in range(startRow, endRow+1): 
            print(arr[i][endCol], end=' ') 
        endCol -= 1 
        if startRow>endRow or startCol>endCol: 
            break 
        for j in range(endCol, startCol-1, -1):
            print(arr[endRow][j], end=' ')
        endRow -= 1 
        if startRow>endRow or startCol>endCol:
            break 
        # Print startCol 
        for i in range(endRow, startRow-1, -1): 
            print(arr[i][startCol], end=' ') 
        startCol += 1 


