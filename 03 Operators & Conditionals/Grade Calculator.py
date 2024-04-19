'''
Problem statement
Your program should take an integer input representing the numerical score and output the corresponding grade. If the input score is not within the valid range (0-100), the program should display "Invalid score".



Instructions :
The grading system is as follows:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
-1 
Sample Output 1:
Invalid score
Sample Input 2:
85 
Sample Output 2:
B
Sample Input 3:
10 
Sample Output 3:
F
'''

# write your code logic !! 
n = int(input())

if(n>=0 and n<=59):
    print("F")
elif(n>=60 and n<=69):
    print("D")
elif(n>=70 and n<=79):
    print("C")
elif(n>=80 and n<=89):
    print("B")
elif(n>=90 and n<=100):
    print("A")
else:
    print("Invalid score")

