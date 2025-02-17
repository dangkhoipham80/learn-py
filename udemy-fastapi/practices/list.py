# Lists are a collection of data
my_list = [80, 96, 72, 100, 8]
print(my_list[0])
print(my_list)

my_list[0] = 10
print(my_list[0])
print(my_list)

my_list.append(300)
print(my_list)

my_list.insert(2, -3)
print(my_list)

# my_list.remove(6) # error because value '6' not in the list
my_list.remove(72) # remove value in the list
print(my_list)

my_list.pop(0) # remove at index
print(my_list)

my_list.sort()
print(my_list)

people_list = ["Eric", "Adil", "Jeff", "Khôi", "Java"]
print(people_list)
print(people_list[1:3]) # from 1 to 2