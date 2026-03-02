# Write to an Existing File :-
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file. 
# "w" - Write - will overwrite any existing content. 

with open("demofile.txt", "a") as f:
    f.write("Now the file has more content")

# open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read())

# Overwrite Existing Content :-
# To overwrite the existing content to the file, use the 'w' parameter. 
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

# open and read the file after the overwriting: 
with open("demofile.txt") as f:
    print(f.read())

# Note: the "w" method will overwrite the entire file. 

# Create a New File :- 
# "x" - Create - will create a file, returns an error if the file exists. 
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists
f = open("myfile.txt", "x")

# Result: a new empty file is created. 

# Note: If the file already exist, an error will be raised. 
