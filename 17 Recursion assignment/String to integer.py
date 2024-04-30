'''
Problem statement
Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 < |S| <= 9
where |S| represents length of string S.
Sample Input 1 :
00001231
Sample Output 1 :
1231
Sample Input 2 :
12567
Sample Output 2 :
12567
'''
def String_to_Integer(n,si):
    if(si==0):
        return int(n[si])
    smalloutput=int(n[si])+10*String_to_Integer(n,si-1)
    return smalloutput
a=input()
n=String_to_Integer(a,len(a)-1)
print(n)
