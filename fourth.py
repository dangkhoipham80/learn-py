# String methods
name = "ka odkhoi oa aoakmJJS JAIK Khsoas Khoi khoi kcosd hl"
phone_number = "+84 795-335-577"

print(f"length: {len(name)}")
print(f"the first \"kh\" at the index: {name.find("kh")}")
print(f"the last \"kh\" at the index: {name.rfind("kh")}")
print(f"Capitalize: {name.capitalize()}") # only the first letter capitalize
print(f"Upper Case: {name.upper()}")
print(f"Check digit: {name.isdigit()}") # boolean
print(f"Check alphabet: {name.isalpha()}") # have 'space' -> false

print(f"Count \"-\": {phone_number.count("-")}")
phone_number = phone_number.replace("+84 ", "0")
phone_number = phone_number.replace("-", ".")
print(f"phone_number after replace {phone_number}")