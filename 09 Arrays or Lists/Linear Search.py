'''
Problem statement
You have been given a random integer array/list(ARR) of size N, and an integer X. You need to search for the integer X in the given array/list using 'Linear Search'.

 You have been required to return the index at which X is present in the array/list. If X has multiple occurrences in the array/list, then you need to return the index at which the first occurrence of X would be encountered. In case X is not present in the array/list, then return -1.

'Linear search' is a method for finding an element within an array/list. It sequentially checks each element of the array/list until a match is found or the whole array/list has been searched.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
-2 ^ 31 <= X <= (2 ^ 31) - 1
Time Limit: 1 sec
Sample Input 1:
1
7
2 13 4 1 3 6 28
3
Sample Output 1:
4
Sample Input 2:
2
7
2 13 4 1 3 6 28
9
5
7 8 5 9 5      
5
Sample Output 2:
-1
2
'''

from sys import stdin

def linearSearch(arr, n, x) :
    #Your code goes here
    found = False
    for i in range(n):
        if arr[i]==x:
            found = True
            return i
    if not found:
        return -1


