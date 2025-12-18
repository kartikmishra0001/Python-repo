print("Hello World")
print('hello')

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""
print(a)

# Strings are Arrays
a = "Kartik Mishra"
print(a[1])

# Looping Through a String
for x in "kartik":
    print(x)

# String Length
a = "Kartik"
print(len(a))

# Check String 
txt = "One Man Army"
print("Man" in txt)

# Python - Slicing Strings

# Slicing - You can return a range of characters by using the slice syntax.

b = "kartik mishra"
print(b[2:4])
# Slice from the start
print(b[:5])
# Slice to the end
print(b[2:])
# Negative Indexing
print(b[-5:-2]) 

# Upper Case
a = "kartik Mishra"
print(a.upper())

# Lower Case
a = "KARTIK MISHRA"
print(a.lower())

# Remove Whitespaces from the beginning
a = "       kartik Mishra"
print(a.strip())

# Replace String
a = "kartik Mishra"
print(a.replace("k", "H"))

# Split String 
a = "kartik Mishra"
print(a.split(","))

# String Concatenation
a = "kartik"
b = "mishra"
c = a + " " + b 
print(c)

# F-String
age = 22
txt = f"My name is Kartik, I am {age}"
print(txt)

# Escape Character (\")
txt = "we are the so-called \" Vikings\" from the north"
