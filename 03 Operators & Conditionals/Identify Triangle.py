'''
Problem statement
Given three positive integers as X, Y and Z representing three sides of a triangle, write a program that determines whether the triangle formed by the sides exist or not. If the triangle exists, classify it as isosceles, scalene or equilateral.

Condition for valid Triangle:
Sum of any two of its sides should be greater than the third side


Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1<=X,Y,Z<=10^5
Sample Input 1:
3
4
5
Sample Output 1:
Scalene Triangle
Explanation
As all three sides are different, so triangle is scalene.
Sample Input 2:
2
7
9
Sample Output 2:
Not a Triangle
'''
# write your code here !!
x = int(input())
y = int(input())
z = int(input())
if x+y>z and x+z>y and z+y>x:
    if(x==y and y==z):
        print("Equilateral Triangle")
    elif(x!=y and y!=z and x!=z):
        print("Scalene Triangle")
    else:
        print("Isosceles Triangle")
else:
    print("Not a Triangle")


