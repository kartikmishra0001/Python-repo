# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Arrays
# Note: This document shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]

# What is an Array?
# An array is a special variable, which can hold more than one value at a time.

# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# Access the Elements of an Array :-
x = cars[0]

# The Length of an Array :-
x = len(cars)
# Note: The length of an array is always one more than the highest array index.

# Looping Array Elements :-
for x in cars:
  print(x)

# Adding Array Elements :- You can use the append() method to add an element to an array.
cars.append("Honda")

# Removing Array Elements :- You can use the pop() method to remove an element from the array.
cars.pop(1)

# You can also use the remove() method to remove an element from the array.
cars.remove("Volvo")
# Note: The list's remove() method only removes the first occurrence of the specified value.

# Array Methods :- 
# (append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort())