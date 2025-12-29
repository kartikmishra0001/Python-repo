myset = {"apple", "banana", "cherry"}

# Sets are used to store multiple items in a single variable.

# Sets are used to store multiple items in a single variable.

# Set Items - Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered - Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable - Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed - Sets cannot have two items with the same value.

thisset = {"apple", "banana", "cherry", "apple"}
# Duplicate values will be ignored

print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set Items - Data Types
# Set items can be of any data type:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types
# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

# The Set() Constructor - It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Access Items - You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Add Items - Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets - To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable - The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove Item - To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You ca also remove items by pop() and clear()Method and del for delete the set

# Loop Items - You can loop through the set items by using a for loop:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Sets :-

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# Union :-

# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# intersection (&)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# intersection_update - The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# difference (-)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# difference_update - The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# symmetric_difference (^)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# symmetric_difference_update - The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)