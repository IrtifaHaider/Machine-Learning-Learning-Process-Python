fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(0, 10, 2):  # Prints numbers from 0 to 8 with a step of 2
    print(i)

count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

for num in range(1, 6):
    if num == 3:
        break  # Stops the loop when num is 3
    print(num)

for num in range(1, 6):
    if num == 3:
        continue  # Skips 3 and moves to the next iteration
    print(num)

for num in range(1, 6):
    if num == 3:
        pass  # Does nothing, avoids syntax error
    print(num)

for i in range(1, 4):
    print(i)
else:
    print("Loop finished successfully!")

count = 1

while count < 4:
    print(count)
    count += 1
else:
    print("Loop ended normally.")

password = ""
while password != "secret":
    password = input("Enter password: ")

print("Access granted!")

word = input("Enter a word: ") # "Python"
for letter in word:
    print(letter)

for i in range(1, 6):  
    print(i)

for i in range(6):  
    print(i)