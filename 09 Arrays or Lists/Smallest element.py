'''
Problem statement
Write a program that returns minimum element in an array.

Hint : the Math.min method is used to find the minimum of two numbers .

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1<=N<=10^5
Note for C++:
It is advisable to declare an array with a size that can accommodate all the elements, considering that N has a maximum value of 10^5.
Input 1:
5 
6 4 3 8 9
Output 1:
3
Input 2:
4
8 8 8 8
Output 2:
8
'''

def minimum_element(arr, n):
    # write the code here !
    min_el = arr[0]
    for el in arr:
        if el < min_el:
            min_el = el
    return min_el




	
n = int(input())
arr = list(map(int, input().split()))
print(minimum_element(arr, n))



