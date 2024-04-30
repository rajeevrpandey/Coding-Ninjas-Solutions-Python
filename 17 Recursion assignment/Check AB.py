'''
Problem statement
Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:

a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
abb
Sample Output 1 :
true
Sample Input 2 :
abababa
Sample Output 2 :
false
Explanation for Sample Input 2
In the above example, a is not followed by either "a" or "bb", instead it's followed by "b" which results in false to be returned.
'''
from math import *
from collections import *
from sys import *
from os import *

def checkab(s):
    if len(s)==0:
        return True
    if s[0]=="a":
        if len(s[1:])>1 and s[1:3]=="bb":
            return checkab(s[3:])
        else:
            return checkab(s[1:])
    else:
        return False
s=input()
if checkab(s)==True:
    print("true")
else:
    print("false")
