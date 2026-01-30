# Dictionaries are mutable

person = {"name": "Bobo", "age": 30}
print(person)

person["age"] = 31
print(person)

person["language"] = "Rust"
print(person)

del person["age"]
print(person)

# Note: like lists, dictionaries are also located in memory, so variables just point to them as references.

# Expected output:
# {'name': 'Bobosan', 'age': 30}
# {'name': 'Bobosan', 'age': 31}
# {'name': 'Bobosan', 'age': 31, 'language': 'Rust'}
# {'name': 'Bobosan', 'language': 'Rust'}
