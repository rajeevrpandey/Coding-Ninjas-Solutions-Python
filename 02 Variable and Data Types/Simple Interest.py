'''
Problem statement
Take the principal amount, rate of interest, and the time period as input and calculate the Simple Interest.

Note: Print the answer as integer value.

Sample Input 1:
2000
2.2
4
Sample Output 1:
176
Explanation:
principal=2000,rate=2.2 and time=4.
Simple interest = (Principal*rate*time) /100
Hence answer is (2000*2.2*4)/100 = 176
'''

# write your code 
p = int(input())
r = float(input())
t = int(input())
print(int((p*r*t)/100))
