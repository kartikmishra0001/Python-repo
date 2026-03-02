# Class Properties :-
# Properties are variables that belong to a class. They store data for each object created from the class. 
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Tobi", 36)

print(p1.name)
print(p1.age)

# Access Properties :-
# You can access object properties using dot notation.
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = car("Toyota", "supra")

print(car1.brand)
print(car1.model)

# Modify Properties :-
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Tobi", 36)
print(p1.age)

p1.age = 26
print(p1.age)

# Delete Properties :-
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error

# Class Properties vs Object Properties :-
# Properties defined inside __init__() belong to each object (instance properties).

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Modifying Class Properties :-
# When you modify a class property, it affect all ojects:
class person:
    lastname = ""

    def __init__(self, name):
        self.name = name
    
p1 = person("Obito")
p2 = person("Madara")

person.lastname = "War"

print(p1.lastname)
print(p2.lastname)

# Add New Properties :-
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)