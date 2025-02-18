# Dictionaries

user_dictionary = {
    'username': 'Pham Dang Khoi',
    'name': 'John',
    'age': 21
}
user_dictionary["married"] = True

print(user_dictionary)
print(user_dictionary.get("username"))
print(len(user_dictionary))

user_dictionary.pop("age")
print(user_dictionary)

# del user_dictionary # delete luôn variable
# user_dictionary.clear()
# print(user_dictionary) # name 'user_dictionary' is not defined

for x in user_dictionary:
    print(x)

for x in user_dictionary.items():
    print(x)

for x, y in user_dictionary.items():
    print(x, y)

user_dictionary2 = user_dictionary
user_dictionary2.pop("username") # memory management dictionary
print(user_dictionary)
print(user_dictionary2)

user_dictionary3 = user_dictionary.copy()
user_dictionary3.pop("name") # only remove in dic3
print(user_dictionary)
print(user_dictionary3)