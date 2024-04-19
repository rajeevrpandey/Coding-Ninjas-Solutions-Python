'''
Problem statement
Given an array of length N, you need to find and print the sum of all elements of the array.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= N <= 10^6
Note for C++:
It is advisable to declare an array with a size that can accommodate all the elements, considering that N has a maximum value of 10^5.
Sample Input :
3
9 8 9
Sample Output :
26
'''

# Read input as sepcified in the question
n = int(input())
arr = list(map(int, input().split()))
# Print output as specified in the question
total = 0
for i in arr:
    total += i
print(total)
