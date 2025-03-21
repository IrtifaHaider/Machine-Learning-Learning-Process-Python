# Reuseable block
# Make code 
#   - Readable 
#   - Reusable 
#   - Organized
# Avoid repetition (DRY – Don’t Repeat Yourself)

# Built-in Functions : print(), len(), type()
# User-defined Functions
# Lambda Functions : Anonymous one-liner functions

def greet():
    print("Hello! Welcome to Python Functions.")

greet()  # Call the function

# FUNCTION WITH PARAMETERS
def add(a, b):
    return a + b
result = add(10, 5)
print("Addition Result:", result)

# DEFAULT PARAMETERS
def say_hello(name="User"):
    print("Hello,", name)
say_hello()              # Hello, User
say_hello("Ahona")       # Hello, Ahona

# KEYWORD ARGUMENTS
def student_info(name, age, dept):
    print(f"{name} is {age} years old and studies in {dept} department.")
student_info(age=22, dept="CSE", name="Irtifa")

# RETURNING MULTIPLE VALUES
def get_stats(x, y):
    return x + y, x - y, x * y
sum_, diff, prod = get_stats(8, 3)
print("Sum:", sum_, "\nDifference:", diff, "\nProduct:", prod)

# VARIABLE NUMBER OF ARGUMENTS (*args, **kwargs)
# *args: accepts multiple positional arguments -
def print_items(*args):
    for item in args:
        print("Item: ",item)
print_items("apple", "banana", "cherry")
print_items("apple", "banana", "cherry", "papaya")

# **kwargs: accepts multiple keyword arguments
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} → {value}")
print_key_values(name="Ahona", age=22, city="Dhaka")
print_key_values(name="Ahona", age=22, city="Dhaka", job="teacher")

# NESTED FUNCTIONS
def outer():
    print("Inside outer function.")

    def inner():
        print("Inside inner function.")
    
    inner()

outer()

# LAMBDA FUNCTION
square = lambda x: x * x # lambda parameter: return operation
print("Square of 5:", square(5))

add = lambda a, b: a + b
print("Lambda Add:", add(10, 20))

cube = lambda y: y * y * y
print("Cube of 3:", cube(3))

# FUNCTION AS ARGUMENT
def apply_function(f, value):
    return f(value * 10)

def double(x):
    return x * 2
print("Function as Argument:", apply_function(double, 5))

# RECURSIVE FUNCTION
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# ANONYMOUS FUNCTION + map() + filter()
nums = [1, 2, 3, 4, 5]
# Using map to square all numbers
squared = list(map(lambda x: x ** 2, nums))
print("Squared:", squared)
# Using filter to keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)
