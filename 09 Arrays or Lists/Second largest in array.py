'''
Problem statement
You have been given a random integer array/list(ARR) of size N. You are required to find and return the second largest element present in the array/list.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^2
1<=arr[i]<=10^3

Time Limit: 1 sec
Sample Input 1:
5
4 3 10 9 2
Sample Output 1:
9
Sample Input 2:
7
13 6 31 14 29 44 3
Sample Output 2:
31
'''

from sys import stdin
#MIN_VALUE = -2147483648


def secondLargestElement(arr, n):
    first  = arr[0]
    second = arr[0]
    for i in arr:
        if i>first:
            second = first
            first = i
        elif i>second:
            second = i
    return second

    



def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#main
arr, n = takeInput()
print(secondLargestElement(arr, n))


