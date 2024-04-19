'''
Problem statement
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= x <= 1,000
Sample Input 1 :
10
Sample Output 1 :
5 11 14 17 23 26 29 35 38 41
Sample Input 2 :
4
Sample Output 2 :
5 11 14 17
Explanation :
Input is 4 and print the first 4 numbers that are not divisible by 4 and are of the form 3N + 2, where k is a non-negative integer.  
'''

## Read input as specified in the question.
x = int(input())
## Print output as specified in the question.

count = 0
n=1
while count<x:
    if(3*n+2)%4==0:
        n+=1
        continue
    print(3*n+2, end=" ")
    count+=1
    n+=1

