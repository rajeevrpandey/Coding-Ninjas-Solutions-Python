'''
Problem statement
Write a program for a theme park that categorizes visitors into five groups: infants, children, adolescents, adults, and seniors, based on their age. The program should print a message indicating the category the visitor falls into and the corresponding ticket price.

Categorize the visitor based on the following age groups and ticket prices:
- Infants: Age 0 to 4, Ticket Price: Free
- Children: Age 5 to 12, Ticket Price: 10
- Adolescents: Age 13 to 17, Ticket Price: 15
- Adults: Age 18 to 64, Ticket Price: 20
- Seniors: Age 65 and above, Ticket Price: 15
Sample Input 1:
3
Sample Output 1:
Infants Free
Sample Input 2:
25
Sample Output 2:
Adults 20
'''

#write your code logic !!!
age = int(input())

if age<=4:
    print("Infants Free")
elif age<=12:
    print("Children 10")
elif age<=17:
    print("Adolescents 15")
elif age<=64:
    print("Adults 20")
else:
    print("Seniors 15")
