a = 10
b = 5

print(a == b)  # False (10 is not equal to 5)
print(a != b)  # True  (10 is not equal to 5)
print(a > b)   # True  (10 is greater than 5)
print(a < b)   # False (10 is not less than 5)
print(a >= 10) # True  (10 is greater than or equal to 10)
print(a <= b)  # False (10 is not less than or equal to 5)

print("apple" == "Apple")   # False (case-sensitive)
print("banana" > "apple")   # False ('b' has lower ASCII than 'a')
print("hello" < "world")    # True  ('h' comes before 'w')

x = 10.5
y = 10.50

print(x == y)  # True (values are the same)
print(x >= y)  # True (10.5 is greater than or equal to 10.50)

age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
