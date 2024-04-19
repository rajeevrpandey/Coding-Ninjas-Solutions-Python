'''
Problem statement
Write a function that takes a square matrix represented by a 2D integer array of size n x n as input. The function should determine if the matrix is an X-matrix, which is defined as follows:

Note:
All elements along the main diagonal (from top-left to bottom-right) of the matrix are non-zero.
All elements outside the main diagonal are zero.
The function should return true if the input matrix meets these criteria for an X-matrix, and false otherwise.
Sample input 1:
[[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
Sample output 1:
true 
Sample input 2 :
[[5,7,0],[0,3,1],[0,5,0]] 
Sample output 1:
false
'''

def checkXMatrix(grid):
    # write your code here !!!
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if(i==j or i+j==n-1):
                if grid[i][j]==0:
                    return False
            else:
                if grid[i][j]!=0:
                    return False
    return True

