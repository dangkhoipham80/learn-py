"""
Set are similar to lists but are unordered and cannot contain duplications
Use curly brackets {}
"""

my_set = {9, 7, 32, 8, 5, -3, 9, 32, 7, 14, -5, -3}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

# print(my_set[0]) # TypeError: 'set' object is not subscriptable

my_set.discard(5) # remove value
print(my_set)

my_set.add(6)
print(my_set)

my_set.update([7, 35, -3]) # add multiple values
print(my_set)

my_set.clear() # remove all elements
print(my_set) # set()

# Tuples ~ List, not change
my_tuple = (9, 7, 32, 8, 5, -3, 9, 32, 7, 14, -5, -3)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])
# my_tuple[1] = 100 # 'tuple' object does not support item assignment