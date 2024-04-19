'''
Problem statement
You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.

You don't need to print or return anything, just change in the input array itself.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
Time Limit: 1sec
Sample Input 1:
1
6
9 3 6 12 4 32
Sample Output 1 :
3 9 12 6 32 4
Sample Input 2:
2
9
9 3 6 12 4 32 5 11 19
4
1 2 3 4
Sample Output 2 :
3 9 12 6 32 4 11 5 19 
2 1 4 3 
'''
  
from sys import stdin

def swapAlternate(arr, n) :
    #Your code goes here
    i = 0
    j = 1
    while i<len(arr) and j<len(arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 2
        j+=2
        



