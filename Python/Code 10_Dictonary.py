# Creating a dictionary
student = {
    "name": "Irtifa Haider",
    "age": 24,
    "grade": "A"
}
print(student)  # Output: {'name': 'Irtifa Haider', 'age': 24, 'grade': 'A'}

print(student["name"])  # Output: Irtifa Haider
print(student["age"])   # Output: 24

print(student.get("grade"))  # Output: A
print(student.get("city", "Not Available"))  # Output: Not Available (default value)

student["age"] = 25  # Update value
student["city"] = "Dhaka"  # Add new key-value pair

print(student) # Output: {'name': 'Irtifa Haider', 'age': 25, 'grade': 'A', 'city': 'Dhaka'}

for key in student:
    print(key)  # Output: name, age, grade, city
    
del student["grade"]  # Deletes a key-value pair
print(student)

age = student.pop("age")  # Removes and returns the value
print(age)  # Output: 25

# Using popitem() (Removes the last inserted item)
student.popitem() 
print(student)  
# Output: {'name': 'Irtifa Haider'}

for value in student.values():
    print(value)  
# Output: Irtifa Haider

student = {
    "name": "Irtifa Haider",
    "age": 24,
    "grade": "A"
}
for key, value in student.items():
    print(key, ":", value)

if "name" in student:
    print("Key exists!")

student_copy = student.copy()
class_data = {
    "student1": {"name": "Irtifa Haider", "age": 24},
    "student2": {"name": "Solaimi Hamid", "age": 24}
}

print(class_data["student1"]["name"])  # Output: Irtifa Haider

squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
