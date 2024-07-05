'''
Problem statement
You are given a Python class MyClass with a static method getmaxvalue that returns the maximum of two given values.

Sample Input :
3
4
Sample Output:
4
'''
class MyClass:
	def __init__(self):
		pass

	@staticmethod
	def get_max_value(x, y):
		if x>y:
			return x
		else:
			return y


		

# Create an instance of MyClass
x = int(input())
y = int(input())
obj = MyClass()
print(MyClass.get_max_value(x, y))
