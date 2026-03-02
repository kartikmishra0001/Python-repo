# Inheritance :-
# Inheritance allows us to define a class that inherits all the methods and properties from another class. 
# Parent class is the class being inherited from, also called base class. 
# Child class is the class that inherits from another class, also called derived class. 

# Create a Parent Class :-
class person: 
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

p1 = person("John", "Doe")
p1.printname()

# Create a Child Class :-
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class. 
class Student(person): 
    pass

# Now the Student class has the same properties and methods as the person class. 
s1 = Student("Mike", "Tyson")
s1.printname()

# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent. 
# We want to add the __init__() function to the child class (instead of the pass keyword). 
class Student(person):
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function. 

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent. 
class Student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add Properties :-
class Student1(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2025

x = Student("Mike", "Olsen", 2019)

# Add Methods :-
class Student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

