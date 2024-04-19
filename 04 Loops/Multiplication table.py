'''
Problem statement
Write a program that generates a multiplication table for a given integer.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
The input integer n is non-negative and less than or equal to 10,000.


Note:
The program should take an integer as input and print the first 10 multiples of the input integer. Each multiple should be printed on a new line. The program should not print anything else. The program should handle the case where the input integer is 0. In this case, the program should print ten lines of 0. The program does not need to handle invalid input. It can assume that the input will always be a valid integer within the specified constraints.
Sample Input 1 :
2
Sample Output 1 :
2
4
6
8
10
12
14
16
18
20
Sample Input 2 :
5
Sample Output 2 :
5
10
15
20
25
30
35
40
45
50
'''

## Read input as specified in the question.
n = int(input())
## Print output as specified in the question.
for i in range(1, 11):
    print(i*n)
