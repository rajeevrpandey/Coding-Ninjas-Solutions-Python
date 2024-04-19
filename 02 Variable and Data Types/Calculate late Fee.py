'''
Problem statement
Let's make a program for the library! You know when you forget to return a book on time? Well, this program will help you figure out how much you owe in late fees!

Here's how it works:

First, Take input "X" as how many days late you are with returning your book.
Then, it will calculate how much money you need to pay for being late. 
Don't worry; it's just a small amount for each day.
Finally, the program will tell you the total amount you owe. Easy, right?
Note:
Assume that the late fee is 0.25 per day.
Sample Input 1:
7
Sample Output 1:
1.75
Sample Input 2:
1000
Sample Output 2:
250.0
'''

# write your code logic !!
x = int(input())
print(x*0.25)
