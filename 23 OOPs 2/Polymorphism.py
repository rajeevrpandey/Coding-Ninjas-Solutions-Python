'''
Problem statement
Write a Python program that defines two classes, India and USA, each representing a country. Both classes have methods to display information about the country's capital and language. The program allows the user to choose between India and the USA by entering a number (1 or 2), and then it calls the appropriate methods to display information about the selected country.

Requirements:
1. Create a Python program that allows the user to input a number (1 or 2) to select between two countries: India and the USA.
2. Implement two classes: India and USA.
3. In the India class, implement a capital method that prints "New Delhi is the capital of India" and a language method that prints "Hindi is the most widely spoken language of India."
4. In the USA class, implement a capital method that prints "Washington, D.C. is the capital of USA" and a language method that prints "English is the primary language of USA."
Sample Input 1 :
1
Sample Output 1 :
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
Sample Input 2 :
2
Sample Output 2 :
Washington, D.C. is the capital of USA.
English is the primary language of USA.
Sample Input 3 :
10
Sample Output 3 :
Invalid input. Please enter 1 for India or 2 for USA.
'''

class India():


    # write your code logic 
    def capital(self):
        print("New Delhi is the capital of India." )

    def language(self):
        print("Hindi is the most widely spoken language of India.")

class USA():
	
    # write your code logic 
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

x = int(input())
if x == 1:
    country1 = India()
    country1.capital()
    country1.language()
elif x == 2:
    country2 = USA()
    country2.capital()
    country2.language()
else:
    print("Invalid input. Please enter 1 for India or 2 for USA.")
