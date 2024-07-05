'''
Problem statement
Python program that demonstrates the use of abstract base classes and inheritance. The program defines an abstract base class Animal with an abstract method move, and several concrete classes that inherit from Animal and implement the move method with different behaviors.

Note:
1. An abstract base class Animal with an abstract method move.
2. Five concrete classes that inherit from the Animal class, each representing a different type of animal:
Human : I can walk and run
Snake : I can crawl
Dog : I can bark
Lion : I can roar
3. Each concrete class should provide an implementation for the move method, displaying a message specific to that type of animal's movement.
Output :
I can walk and run
I can crawl
I can bark
I can roar
'''

from abc import ABC, abstractmethod
class Animal(ABC):
	@abstractmethod
	def move(self):
		pass

# write your code logic 

class Human(Animal):
	def move(self):
		print("I can walk and run")

class Snake(Animal):
	def move(self):
		print("I can crawl")



class Dog(Animal):
	def move(self):
		print("I can bark")



class Lion(Animal):
	def move(self):
		print("I can roar")













R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
