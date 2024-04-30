'''
Problem statement
Given a string, compute recursively a new string where all 'x' chars have been removed.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string S. 
Sample Input 1 :
xaxb
Sample Output 1:
ab
Sample Input 2 :
abc
Sample Output 2:
abc
Sample Input 3 :
xx
Sample Output 3:

'''
# Problem: Remove x from string
def removeX(s):
    chr = 'x'
    l = len(s)
    if len(s) == 0:
        return s
    smalleroutput = removeX(s[1:])
    if s[0] == chr :
        return ''+smalleroutput
    else:
        return s[0]+smalleroutput


# Main
string = input()
print(removeX(string))

