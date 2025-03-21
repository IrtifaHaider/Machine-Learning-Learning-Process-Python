numbers = [10, 20, 30, 40, 50]

print(20 in numbers)   # True (20 exists in the list)
print(100 in numbers)  # False (100 is not in the list)

fruits = ["apple", "banana", "cherry"]

print("mango" not in fruits)  # True (mango is not in the list)
print("apple" not in fruits)  # False (apple is in the list)

word = "hello"

print("h" in word)    # True
print("z" in word)    # False

tuple_data = (1, 2, 3, 4, 5)

print(3 in tuple_data)   # True
print(6 in tuple_data)   # False

person = {"name": "Alice", "age": 25, "city": "New York"}

print("name" in person)      # True  (Key exists)
print("Alice" in person)     # False (Values are not checked)
print("country" not in person)  # True (Key does not exist)

students = ["John", "Sara", "David"]

name = "David"

if name in students:
    print(f"{name} is in the class.")
else:
    print(f"{name} is not in the class.")
