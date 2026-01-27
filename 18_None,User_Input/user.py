# User Input
# Python allows for user input.

# That means we are able to ask the user for input.
print("Enter your name:", end=" ")
name = input()
print(f"Hello {name}")

# Using prompt :-
name = input("Enter your name: ")
print(f"Hello {name}")

# Multiple Inputs :-
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# Input Number :-
import math
x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y:.2f}")