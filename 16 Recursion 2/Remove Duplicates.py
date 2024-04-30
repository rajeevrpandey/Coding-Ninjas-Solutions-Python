'''
Problem statement
Given a string S, remove consecutive duplicates from it recursively.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string
Sample Input 1 :
aabccba
Sample Output 1 :
abcba
Sample Input 2 :
xxxyyyzwwzzz
Sample Output 2 :
xyzwz
'''
# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    if len(s)<=1:
        return s
    smallOutput=removeConsecutiveDuplicates(s[1:])
    if s[0]==s[1]:
        return smallOutput
    else:
        return s[0]+smallOutput

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
