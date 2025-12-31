thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Dictionary :-

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Dictionary Items :-

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Changeable :-

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed :-
# Dictionaries cannot have two items with the same key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# The dict() Constructor :-
# It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "kartik", age = 22, country = "Norway")
print(thisdict)

# Accessing Items :-
# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])
print(thisdict.get("model")) # same result

# Get Keys :-
# The keys() method will return a list of all the keys in the dictionary.

print(thisdict.keys())

# Get Values :-
# The values() method will return a list of all the values in the dictionary.

print(thisdict.values())

# Get Items :-
# The items() method will return each item in a dictionary, as tuples in a list.

print(thisdict.items())

# Change Values :- is same as update dictionary
# You can change the value of a specific item by referring to its key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Adding items 
# Update Dictionary - update()
# Removing items - pop("model"), popitem()
# Delete item - del dictName["model"]
# Delete dict - del dictName
# Clear - clear() empties the dictionary

# Loop Through a Dictionary
for x in thisdict:
  print(x)

# Copy a Dictionary - copy() other way is make a new dictionary
# dictionary - dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries :-
# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])