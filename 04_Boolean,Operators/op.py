# Operators are used to perform operations on variables and values.

print(10 + 5)
# "+" is an operator

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
# (+, -, *, /, %, **, //)

a = 10 
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b) # return a float
print(a % b)
print(a ** b)
print(a // b) # return an integer - It rounds down to the nearest integer.

# Assignment operators
# (=, +=, -=, *=, /=, %=, //=, **=, %=, |=, ^=, >>=, <<=, :=)

# Comparison operators
# (==, !=, >, <, >=, <=)

# Logical operators (and, or, not)
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverse the result, returns False if the result is true

# Identity operators (is, is not)
# is - Returns True if both variables are the same object
# is not - 	Returns True if both variables are not the same object

# Membership operators (in, not in)
# in - Returns True if a sequence with the specified value is present in the object
# not in - Returns True if a sequence with the specified value is not present in the object

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

# Bitwise operators
# '&' 'AND' Sets each bit to 1 if both bits are 1
# '|' 'OR' Sets each bit to 1 if one of two bits is 1
# '^' 'XOR' Sets each bit to 1 if only one of two bits is 1
# '~' 'NOT' Inverts all the bits
# '<<' 'Zero fill left shift' Shift left by pushing zeros in from the right and let the leftmost bits fall off
# '>>' 'Signed right shift' Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off