# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

mylist = ["apple", "banana", "cherry"]

# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join Two Lists - There are several ways to join, or concatenate, two or more lists in Python.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# or

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# List Methods
# append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()