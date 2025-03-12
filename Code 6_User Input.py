# Basic User Input --> str
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Numeric Input
age = int(input("Enter your age: "))  # Converts input to integer
print("You will be", age + 1, "years old next year.")

# Floating Input
height = float(input("Enter your height in meters: "))  
print("Your height is", height, "meters.")

# Multiple Inputs
a, b = input("Enter two numbers separated by space: ").split()
a = int(a)  
b = int(b)
print("Sum:", a + b)

# map() for Multiple Inputs
x, y, z = map(int, input("Enter three numbers: ").split())
print("Product:", x * y * z)

# List Input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("You entered:", numbers)

# Input with a Default Value (Using input() or Operator)
name = input("Enter your name (or press enter to use default): ") or "Guest"
print("Hello,", name)

# Handling Boolean Input
is_student = input("Are you a student? (yes/no): ").lower() == "yes" 
print("Student status:", is_student)

# getpass for Secure Input (Hides Input)
from getpass import getpass 
password = getpass("Enter your password: ") 
print("Password received!")
