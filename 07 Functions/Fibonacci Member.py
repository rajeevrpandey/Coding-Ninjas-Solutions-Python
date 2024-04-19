'''
Problem statement
Create a function that determines whether a given number N belongs to the Fibonacci sequence. If N is found in the Fibonacci sequence, the function should return true; otherwise, it should return false.



Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= n <= 10^4
Sample Input 1 :
5
Sample Output 1 :
true
Explanation :
Fibonacci sequence begins 0, 1, 1, 2, 3, 5, ... and so on. Since 5 appears in the sequence.
Sample Input 2 :
14
Sample Output 2 :
false    
'''


def checkMember(n):
    first = 0
    second = 1
    while(first<n):
        third = first + second
        if(n==first or n== second or n==third):
            return True
        first = second
        second = third
    return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")

