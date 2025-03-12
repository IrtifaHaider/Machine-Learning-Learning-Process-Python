age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


marks = int(input("Enter your mark: "))
if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 65:
    print("Grade: A-")
elif marks >= 60:
    print("Grade: B+")
elif marks >= 55:
    print("Grade: C")
else:
    print("Grade: F")

num = int(input("Enter the number to check if it is Positive Even/Odd or Negative Eve/Odd: "))
if num > 0:
    print("Positive number and also")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative Number and also")
    if num % 2 ==0:
        print("Even number")
    else:
        print("Odd Number")

age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)

# it is equivalent 
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

temperature = int(input("Enter a Temperature: "))
if temperature > 20 and temperature < 30:
    print("The weather is nice.")

fruits = input("Enter fruits separated by space: ").split()
if "banana" in fruits:
    print("Banana is available.")

is_student = input("Are you a student? (yes/no): ").lower() == "yes" 
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")
