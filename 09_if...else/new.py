# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200
if b > a:
  print("b is greater than a")

# Multiple Statements in If Block

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

# The Elif Keyword - The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Multiple Elif Statements
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

# The Else Keyword - The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
a = 5
b = 2
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

# Assign a Value With If ... Else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Python Logical Operators (and , or , not)
# The and Operator - The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or Operator - The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# The not Operator - The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested If Statements
# You can have if statements inside if statements. This is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

# The pass Statement - if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass