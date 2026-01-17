# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# Create a Module :-
# To create a module just save the code you want in a file with the file extension .py:

# Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)

# Use a Module :-
# Now we can use the module we just created, by using the import statement:
import mymodule

mymodule.greeting("Kartik")

# Variables in Module :-
person1 = {
  "name": "kartik",
  "age": 22,
  "country": "Meerut"
}

# Re-naming a Module :-
# You can create an alias when you import a module, by using the (as) keyword:
import mymodule as mx

a = mx.person1["age"]
print(a)