# Python Classes/Objects :-
# A Class is like an object constructor, or a "blueprint" for creating objects.abs

# Create a Class :-
class MyClass:
    x = 5

# Create Object :-
# Now we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)

# Delete Objects :-
del p1

# Multiple Objects :-
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Note: Each object is independent and has its own copy of the class properties.

# The pass Statement :-
# Class definitions cannot be empty, but if you for some reason hava a class definition with no content, put in the pass statement to avoid getting an error.
class person:
    pass

# The __init__() Method :-
# All classes hava a built-in method called __init__(), which is always executed when the class is being initiated.
# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Poopu", 34)
print(p1.name)
print(p1.age)

# Note: The __init__() method is called automatically every time the class is being used to create a new object.

# Why Use __init__()?
# Without the __init__() method, you would need to set properties manually for each object.
class person:
    pass

p1 = person()
p1.name = "Tobirama"
p1.age = 45

print(p1.name)
print(p1.age)

# Using  __init__() makes it easier to create objects with initial values:

# Default Values in __init__() :-
# You can also set default values for parameters in the __init__() method:
class person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age

p1 = person("Eren")
p2 = person("yeager", 18)

print(p1.name)
print(p1.age)

# Multiple Parameters
class person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = person("Eren Yeager", 20, "oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

# Self Parameter :-
# The self paramter is a reference to the current instance of the class.
# It is used to access properties and methods that belongs to the class.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = person("Kira", 25)
p1.greet()

# Note: The self parameter must be the first parameter of any method in the class.

# Why Use self?
# Without self, Python would not know which object's properties you want to access:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name)

p1 = person("Kira", 25)
p1.printname()

# self Does Not Have to Be Named "self" :-
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class.
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

# Accessing Properties with self :-
class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = car("Toyota", "Corolla", 2020)
car1.display_info()

# Calling Methods with self :-
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()

