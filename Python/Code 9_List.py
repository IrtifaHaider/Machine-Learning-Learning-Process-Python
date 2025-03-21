# List of integers
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])   # Output: [20, 30, 40] (Index 1 to 3)
print(numbers[:3])    # Output: [10, 20, 30] (First 3 elements)
print(numbers[3:])    # Output: [40, 50, 60] (Elements from index 3 onward)
print(numbers[-3:])   # Output: [40, 50, 60] (Last 3 elements)

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1]) # Output: cherry (last element)

fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"  # Changing "banana" to "mango"
print(fruits)  # Output: ['apple', 'mango', 'cherry']

fruits.append("orange")
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'orange']

fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'mango', 'cherry', 'orange']

new_fruits = ["pineapple", "watermelon"]
fruits.extend(new_fruits)
print(fruits)  # Output: ['apple', 'grape', 'mango', 'cherry', 'orange', 'pineapple', 'watermelon']

fruits.remove("mango")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange', 'pineapple', 'watermelon']

# Removes an element at a specific index (default is last).
fruits.pop(2)
print(fruits)  # Output: ['apple', 'grape', 'orange', 'pineapple', 'watermelon']

fruits.pop()
print(fruits) # Output: ['apple', 'grape', 'orange', 'pineapple']

del fruits[1]  # Deletes the second element
print(fruits) # Output: ['apple', 'orange', 'pineapple']

for fruit in fruits:
    print(fruit)
print('\n')
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
print('\n')  
 
[print(fruit) for fruit in fruits]

print("banana" in fruits)  # Output: False
print("grape" not in fruits)  # Output: True

fruits_copy = fruits.copy()
print(fruits_copy)

fruits_copy = list(fruits)
print(fruits_copy)

fruits_copy = fruits[:]
print(fruits_copy)

del fruits  # Deletes the entire list
# print(fruits)

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 5, 8]

numbers.sort(reverse=True)
print(numbers)  # Output: [8, 5, 3, 2, 1]

numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Mixed data types
mixed_list = [10, "Hello", 3.14, True]

# Empty list
empty_list = []

squares = [x**2 for x in range(3, 9)]
print(squares)  # Output: [9, 16, 25, 36, 49, 64]
