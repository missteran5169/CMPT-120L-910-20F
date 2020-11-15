# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 

class Polygon(ABC): 

	# abstract method 
	def num_sides(self): 
		pass

class Triangle(Polygon): 

	# overriding abstract method 
	def num_sides(self): 
		print("I have 3 sides") 

class Pentagon(Polygon): 

	# overriding abstract method 
	def num_sides(self): 
		print("I have 5 sides") 

class Hexagon(Polygon): 

	# overriding abstract method 
	def num_sides(self): 
		print("I have 6 sides") 

class Quadrilateral(Polygon): 

	# overriding abstract method 
	def num_sides(self): 
		print("I have 4 sides") 

class Septagon(Polygon): 

	# overriding abstract method 
	def num_sides(self): 
		print("I have 7 sides") 

class Octagon(Polygon): 

	# overriding abstract method 
	def num_sides(self): 
		print("I have 8 sides") 

def favoriteShape(shape_name):
    print("Wow your favorite shape is a {shape_name}! That's my favorite shape too!".format(shape_name = shape_name))