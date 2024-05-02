'''
Problem statement
Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).

Return true or false.

Do it recursively.

E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
abchjsgsuohhdhyrikkknddg
coding
Sample Output 1 :
true
Sample Input 2 :
abcde
aeb
Sample Output 2 :
false
'''
def contains(s,t):
    # Base case: if t is empty, it is already contained in s
    if not t:
        return True
    # Base case: if s is empty and t is not, t cannot be contained in s
    if not s:
        return False
    # If the first character of s matches the first character of t, recursively check the rest of the strings
    if s[0] == t[0]:
        return contains(s[1:], t[1:])
    # If the first characters don't match, continue checking the rest of s
    else:
        return contains(s[1:], t)
    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')

