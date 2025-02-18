# Functions

def my_function():
    print("Inside my_fucntion")

def print_my_name(name):
    print(f"Hello {name}")

my_function()
print_my_name("John")

# Functions Assignment
def my_info(first_name, last_name, age):
    user_dictionary = {
        'firstname': first_name,
        'lastname': last_name,
        'age': age
    }
    return user_dictionary

dictionary = my_info("Phạm", "Khôi", 20)
print(dictionary)