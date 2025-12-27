# Tuples are used to store multiple items in a single variable.

mytuple = ("apple", "banana", "cherry")

# Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.

# Unchangeable - Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Tuple Length - To determine how many items a tuple has, use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item - To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

# The tuple() Constructor - It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Update Tuples
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there are some workarounds.

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("kiwi",)
thistuple += y

print(thistuple)

# Remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple

# print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "pineapple", "cherry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples 
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)