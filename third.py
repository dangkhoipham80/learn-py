import math

#
friends = 0
friends += 3
friends **= 2
print(friends)

#
x = 3.14
y = -4.23
z = 5
print(round(x))
print(abs(y))
print(pow(3, 4))
print(f"max: {max(x, y, z)}")

#
print(f"PI: {math.pi}")
print(f"e: {math.e}")
print(f"sqrt(3): {math.sqrt(3)}")
# ceil
print(math.ceil(3.14))
# floor
print(math.floor(3.78))

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {round(circumference, 2)}")

# if = Do some code only IF some condition is True
#       Else do sth else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born to yet!")
else:
    print("You must be 18+ to sign up!")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# logical operators = evaluate multiple conditions (or, and, not)
age = 25
has_license = True
has_insurance = False

if age >= 18 and has_license:
    print("You are allowed to drive.")
if has_license or has_insurance:
    print("You can either drive or you have insurance.")
if not has_insurance:
    print("You need insurance to be fully covered.")

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on a condition
#                           X if condition else Y
num = 6
a = 5
b =4

print("Positive" if num > 0 else "Negative")

max_num = a if a > b else b
