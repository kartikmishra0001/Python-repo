# Python Functions :-
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

# Creating a Function :-
def my_function():
  print("Hello from a function")

# Calling a Function :-
def my_function():
  print("Hello from a function")

my_function()

# Return Values :-
# Functions can send data back to the code that called them using the return statement.
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# The pass Statement :-
def my_function():
  pass

# Arguments :- Information can be passed into functions as arguments.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments :- The terms parameter and argument can be used for the same thing: information that are passed into a function.
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Number of Arguments :-
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Default Parameter Values :-
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# Keyword Arguments :-
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Positional Arguments :- When you call a function with arguments without using keywords, they are called positional arguments.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# Passing Different Data Types :-
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Return Values :- Functions can return values using the return statement:
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# Positional-Only Arguments(/) :- You can specify that a function can have ONLY positional arguments.
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

# Keyword-Only Arguments(*) :- To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

# args and **kwargs :-
# By default, a function must be called with the correct number of arguments.

# However, sometimes you may not know how many arguments that will be passed into your function.

# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args :-
def my_function(*kids):
  for kid in kids:
    print(kid)

my_function("Emil", "Tobias", "Linus")

# What is *args? :-
# The *args parameter allows a function to accept any number of positional arguments.

# Inside the function, args becomes a tuple containing all the passed arguments:

# Using *args with Regular Arguments :-
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments - **kwargs :-
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# What is **kwargs? :-
# The **kwargs parameter allows a function to accept any number of keyword arguments.

# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

# Unpacking Arguments :-
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

# Unpacking Lists with * :-
# If you have values stored in a list, you can use * to unpack them into individual arguments:
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# Unpacking Dictionaries with ** :-
# If you have keyword arguments stored in a dictionary, you can use ** to unpack them:
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)

# Scope :-
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope :-
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Global Scope :-
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.

# Global Keyword :-
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Nonlocal Keyword :-
# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# Decorators :-
# Decorators let you add extra behavior to a function, without changing the function's code.

# A decorator is a function that takes another function as input and returns a new function.

# Basic Decorator :-
# Define the decorator first, then apply it with @decorator_name above the function.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

# Multiple Decorator Calls :-
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# Arguments in the Decorated Function :-
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# Lambda Functions :-
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax - lambda arguments : expression
x = lambda a : a + 10
print(x(5))

# Lambda with Built-in Functions :-
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# Using Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Using Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Using Lambda with sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# Recursion :-
# Recursion is when a function calls itself.
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

# Base Case and Recursive Case
# Every recursive function must have two parts:

# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

# Generators :-
# Generators are functions that can pause and resume their execution.

# When a generator function is called, it returns a generator object, which is an iterator.
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

# Generators allow you to iterate over data without storing the entire dataset in memory.

# Instead of using return, generators use the yield keyword.

# The yield Keyword :-
# The yield keyword is what makes a function a generator.

# When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

# Unlike return, which terminates the function, yield pauses it and can be called multiple times.