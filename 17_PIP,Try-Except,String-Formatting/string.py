# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# Before Python 3.6 we had to use the format() method.

# F-Strings :-
# F-string allows you to format selected parts of a string.

# To specify a string as an f-string, simply put an f in front of the string literal, like this:
txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

# Perform Operations in F-Strings
txt = f"The price is {20 * 59} dollars"
print(txt)

# You can perform if...else statements inside the placeholders:
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

# String format() :-
# Before Python 3.6 we used the format() method to format strings.

# The format() method can still be used, but f-strings are faster and the preferred way to format strings.

# format method()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))