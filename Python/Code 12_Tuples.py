# Immutable --> can't change or modify data. 
# Gives consistency to data 
#       - using in bank accounts data
# Allows Duplicates 
# Indexing - (0-based)

t1 = (1, 2, 3)
print(t1)

t2 = 1, 2, 3 # Tuple without parentheses (not recommended)
print(t2)

t3 = () # Empty tuple
print(t3)

# Single-element tuple
t4 = (10,)  # Notice the comma!
print(t4)
print(type(t4))  # <class 'tuple'>

# Tuple Indexing and Slicing
t = (10, 20, 30, 40, 50)
print(t[0])      
print(t[-1])     # (last element)
print(t[1:4])    # (20, 30, 40)

# Immutability
t = (1, 2, 3)
# t[0] = 100  ❌ This will raise TypeError

# Tuple Methods
t = (1, 2, 2, 3, 3)
print(t.count(2))  # (how many times 2 appears)
print(t.index(3))  # (first index where 3 appears)

# Iterating Over a Tuple
t = ('apple', 'banana', 'cherry')
for item in t:
    print(item)
    
# Tuple Packing and Unpacking
# Packing
person = ("Alice", 25, "Engineer")
# Unpacking
name, age, job = person
print(name)
print(person[1])
print(job)  
print(person)

# Tuple Inside Other Structures
# List of tuples
students = [("Alice", 85), ("Bob", 90), ("Eve", 78)]
print(students)
# Tuple of tuples
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix)

# Nested Tuple Access
nested = ((1, 2), (3, 4), (5, (6, 7)))
print(nested[1]) 
print(nested[2]) 
print(nested[2][1]) 
print(nested[2][1][1])  

# Tuples as Dictionary Keys
location_data = {
    ("New York", "USA"): 8.4,
    ("London", "UK"): 9.3,
    ("Tokyo", "Japan"): 14.0
}
print(location_data)
print(location_data[("New York", "USA")])
