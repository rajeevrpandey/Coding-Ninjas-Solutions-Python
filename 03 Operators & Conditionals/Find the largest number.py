'''
Problem statement
Write a program that takes three integers as input and prints the largest of the three numbers.



Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
4
10
5
Sample Output :
10 
'''

# write your code logic here !!!!!!!
x = int(input())
y = int(input())
z = int(input())

print(max(max(x,y),z))
