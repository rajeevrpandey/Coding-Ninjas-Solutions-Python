'''
Problem statement
You and your friends are having a cookie-baking party, and you want to ensure that each person gets an equal share of cookies. You have a total number of cookies baked, and you need to divide them equally among your friends

Note:
1. Ask the user to input the total number of cookies baked.
2. Ask the user to input the number of friends present.
3. Calculate how many cookies each friend will get if the cookies are divided equally among them.
4. Print the total number of cookies each friend will get.
Sample input 1:
 10
 2
Sample output 1:
 5
Explanation:
 In this scenario, there are 10 cookies baked, and 5 friends are present. So, each of the 5 friends will receive 2 cookies each, ensuring that the distribution is fair and equal.
Sample input 1:
 20
 40
Sample output 1:
 0
Explanation:
In this scenario, there are 20 cookies baked, but there are 40 friends present. Since the number of friends exceeds the number of cookies, each friend will receive 0 cookies. This indicates that there are not enough cookies to distribute equally among all friends, resulting in each friend receiving none.
'''

# write your code here !!!
noOfCookies = int(input())
noOfFriends = int(input())

cPerF = noOfCookies // noOfFriends
print(cPerF)
