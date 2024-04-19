'''
Problem statement
For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row or column) amongst all the rows/columns.

Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= t <= 10^2
1 <= N <= 10^3
1 <= M <= 10^3
Time Limit: 1sec
Sample Input 1:
1
3 2
6 9 
8 5 
9 2 
Sample Output 1:
column 0 23
Sample Input 2:
1
4 4
6 9 8 5 
9 2 4 1 
8 3 9 3 
8 7 8 6 
Sample Output 2:
column 0 31
'''


from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    rowsum = -2147483648
    rowind = 0
    colsum = -2147483648
    colind = 0
    for i in range(nRows):
        newtot = 0
        for j in range(mCols):
            newtot += arr[i][j]
        if newtot>rowsum:
            rowsum = newtot
            rowind = i
    for j in range(mCols):
        newtot = 0
        for i in range(nRows):
            newtot += arr[i][j]
        if newtot>colsum:
            colsum = newtot
            colind = j
    if rowsum < colsum:
        print("column", colind, colsum)
    else:
        print("row", rowind, rowsum)
        
    
