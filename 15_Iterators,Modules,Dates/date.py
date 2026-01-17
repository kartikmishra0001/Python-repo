# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime

x = datetime.datetime.now()
print(x)

# Date Output :-
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))