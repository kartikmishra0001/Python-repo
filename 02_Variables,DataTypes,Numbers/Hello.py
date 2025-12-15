# Variables
# Variables are containers for storing data values.

x = 5
y = "Kartik"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# Casting
# If you want to specify the data type of a variable, this can be done with casting. Example:

x = str(3)    
y = int(3)    
z = float(3)

# Get the type
print(type(x))
print(type(y))
print(type(z))

# String - String variables can be declared either by using single or double quotes:

Name = "kartik"
name = 'kartik'

# Case Sensitive - Variable names are case-sensitive.

a = 4
A = "Prince"
# A will not overwrite a

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

cars = ["Honda", "BMW", "Nano"]
x, y, z = cars
print(x)
print(y)
print(z)

# Global Variables
# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

a = 'Hello'

def myfunc():
    print(a + " World")

myfunc()

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

def myfunc():
  global m
  m = "Beautiful"

myfunc()

print("You are " + m)

# Data Type - Built-in Data Types

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Python Numbers
x = 1 # int 
y = 3.4 # float
z = 1j # complex

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# You cannot convert complex numbers into another number type.

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))