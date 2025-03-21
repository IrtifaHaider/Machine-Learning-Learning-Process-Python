# Python file you can import and reuse
# Reuse code across projects
# Modular programming and separation of concerns
# Reduces code duplication
# Built-in Modules -->	math, random, os, sys
# User-defined	--> Any .py file I create create

import my_math # Import the entire module

# Use its functions
print("Add:", my_math.add(10, 5))
print("Subtract:", my_math.subtract(10, 5))
print("Square:", my_math.square(6))
print("Value of pi:", my_math.pi)


# Import specific functions only
from my_math import add
print(add(2, 3))

# Import with alias
import my_math as mm
print(mm.square(5))

# Built-in Modules
import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("Cosine of 0:", math.cos(0))

from datetime import datetime
current_datetime = datetime.now()
print("Current Date and Time: ", current_datetime)
formatted_date = current_datetime.strftime("%Y-%m-%d")
print(formatted_date)
formatted_time = current_datetime.strftime("%H:%M-%S")
print(formatted_time)
custom_format = current_datetime.strftime("%A, %d %B %Y")
print(custom_format)
birthday = datetime(2000, 10, 15, 5, 00)
print("Birthday:", birthday)

from datetime import timedelta
today = datetime.now()
yesterday = today -timedelta(days=1)
print(today)
print(yesterday)
print(today-yesterday)

from datetime import date , time
today_date = date.today()
print(today_date)
specific_time= time(10,15,30)
print(specific_time)

# Importing modules from the packages
from my_package import string_operations
print("Uppercase:", string_operations.to_uppercase("irtifa"))