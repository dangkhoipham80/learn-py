# This is our first Python program
print("Hello World!!!")
print("Line 2")

# Variable
# Strings
first_name = "Pham"
food = "pizza"

# Integer
age = 20;

# Float
price = 10.99

# Booolean
is_student = True

print(first_name)
print(f"Hello {first_name}, you like {food}, age: {age}, student: {is_student}") # f_string
print(f"The price is ${price}")

# if-else
if is_student:
    print("You are a student")
else:
    print("you are NOT student")

# Typecasting = the process of converting a variable from one data type to another
#               str(). int(). float(), bool()

name = "Pham Dang Khoi"
age = 20
gpa = 3.2
is_student = True

print(type(gpa))
print(int(gpa))
print(float(age))
print(bool(name))

# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

full_name = input("What is your name?: ")
birth = int(input("What is your birth year?; "))
print(f"Hello {full_name}")
