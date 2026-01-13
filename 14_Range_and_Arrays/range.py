# Python range :-
# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# This set of numbers has its own data type called range.

# Note: Immutable means that it cannot be modified after it is created.

# Creating ranges :-
# The range() function can be called with 1, 2, or 3 arguments, using this syntax:

# range(start, stop, step)

# Call range() With One Argument :-
for x in range(5):
    print(x, end=", ")

# Call range() With Two Argument :-
print()
for x in range(3, 10):
    print(x, end=", ")

# Call range() With Three Arguments
print()
for x in range(2, 20, 2):
    print(x, end=", ")

# Slicing Ranges :-
r = range(10)
print(r[2])
print(r[:3])

# Membership Testing :- Ranges support membership testing with the in operator.
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# Length :-
r = range(0, 10, 2)
print(len(r))