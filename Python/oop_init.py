from __future__ import print_function

class Person:
	def __init__(self, name):
		self.name = name
		
	def say_hi(self):
		print('Hello, my name is', self.name)
	
p = Person('Swaroop')
p.say_hi()