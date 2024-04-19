'''
Problem statement
Write a Python program that generates multiplication tables for numbers from 1 to a given integer N.



Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 100
Sample input 1:
2
Sample input 1:
1 2 3 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
Sample input 1:
3
Sample input 1:
1 2 3 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
'''

n = int(input())
for i in range(1, n+1):
    for j in range(1,11):
        if(j==10):
            print(i*j)
        else:
            print(i*j, end=" ")
