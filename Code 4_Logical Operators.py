x = 10
y = 5

print(x > 5 and y < 10)  # True (Both conditions are True)
print(x > 5 and y > 10)  # False (Second condition is False)

a = 20
b = 30

print(a > 25 or b > 25)  # True (b > 25 is True)
print(a > 25 or b < 25)  # False (Both conditions are False)

c = 15

print(not c > 10)  # False (c > 10 is True, but `not` makes it False)
print(not c < 10)  # True  (c < 10 is False, but `not` makes it True)

age = 20
citizen = True

if age >= 18 and citizen:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
