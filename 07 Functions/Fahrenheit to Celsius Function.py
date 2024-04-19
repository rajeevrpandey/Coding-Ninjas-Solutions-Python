'''
Problem statement
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.



Note:
You don't have to write the main function or take input. It has already been taken care of and you need to just print the integer value . Just write the code that prints Fahrenheit to Celsius table in the function itself.
Formula is C = (F - 32) * 5/9
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= S <= 1000
0 <= E <= 1000
0 <= W <= 1000
Sample Input 1:
0 
100 
20
Sample Output 1:
0   -17
20  -6
40  4
60  15
80  26
100 37
Sample Input 2:
120 
200 
40
Sample Output 2:
120 48
160 71
200 93
Explanation for Sample Output 2 :
Start value is 120, end value is 200 and step size is 40. Therefore, the values we need to convert are 120, 120 + 40 = 160, and 160 + 40 = 200. 
The formula for converting Fahrenheit to Celsius is:
Celsius Value = (5/9)*(Fahrenheit Value - 32)  
Plugging 120 into the formula, the celsius value will be (5 / 9)*(120 - 32) => (5 / 9) * 88 => (5 * 88) / 9 => 440 / 9 => 48.88
But we'll only print 48 because we are only interested in the integral part of the value.

'''

def printTable(start,end,step):
#Implement Your Code Here
	for f in range(start, end, step):
		c = int((f-32)*5/9)
		print(f, c)

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
	   

