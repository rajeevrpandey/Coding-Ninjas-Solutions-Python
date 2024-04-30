'''
Problem statement
Given the 'start' and the 'end'' positions of the array 'input'. Your task is to sort the elements between 'start' and 'end' using quick sort.



Note :
Make changes in the input array itself.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
6 
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8
Sample Input 2 :
5
1 2 3 5 7
Sample Output 2 :
1 2 3 5 7 
Constraints :
1 <= N <= 10^3
0 <= input[i] <= 10^9
'''
"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List
def quickSort(arr: List[int], start: int, end: int):
    if start < end:
        # Partition the array
        pivot_index = partition(arr, start, end)

        # Sort the partitions
        quickSort(arr, start, pivot_index-1)
        quickSort(arr, pivot_index+1, end)

def partition(arr, start, end):
    pivot = arr[end]  # Choosing the last element as the pivot
    i = start - 1  # Index of smaller element

    for j in range(start, end):
        # If current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1
