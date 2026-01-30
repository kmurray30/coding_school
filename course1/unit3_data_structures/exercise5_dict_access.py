# Access dictionary values using square brackets with the key

student = {
    "name": "Bob",
    "grade": 10,
    "gpa": 3.7
}

print(student["name"])
print(student["gpa"])

# You can change values by assigning to a key
student["grade"] = 11
print(student["grade"])

# You can add new key-value pairs
student["school"] = "Lincoln High"
print(student)

# You can also check if a key exists in the dictionary
if "name" in student:
    print("Name is a key in the dictionary")
else:
    print("Name is not a key in the dictionary")

# There are all sorts of methods you can use on dictionaries, so be sure to check the documentation.
# More on functions in the next unit.
# A couple examples:
print(student.keys())
print(student.values())

# Now practice with your own dictionary
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}

# Print the title
...
# Change the year to 1950
...
# Add a new key "pages" with value 328
...
# Print the whole dictionary
...
# Check if the key "pages" exists in the dictionary
...

# Expected output:
# Bob
# 3.7
# 11
# {'name': 'Bob', 'grade': 11, 'gpa': 3.7, 'school': 'Lincoln High'}
# 1984
# {'title': '1984', 'author': 'George Orwell', 'year': 1950, 'pages': 328}
