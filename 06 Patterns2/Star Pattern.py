'''
Problem statement
Print the following pattern

Pattern for N = 4




Hint
As taught in the video, you just have to modify the code so that instead of printing numbers, it should output stars ('*').
The dots represent spaces.




Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  *** 
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   *** 
  *****
 *******
'''
 
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.

for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*", end="")
    for k in range(1,i):
        print("*" ,end="")
    print()

