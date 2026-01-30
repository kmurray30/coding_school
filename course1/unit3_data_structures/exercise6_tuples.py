# Tuples are like lists but IMMUTABLE (can't be changed)
# Use parentheses to create a tuple

coordinates = (10, 20)
rgb_color = (255, 128, 0)
person_info = ("Alice", 25, "Engineer")

print(coordinates)
print(rgb_color)
print(person_info)

# You can access tuple elements just like lists
print(coordinates[0])
print(person_info[2])

# Tuples are useful when you want data that shouldn't change
# You CANNOT do this (it will error):
# coordinates[0] = 15  # Error! Tuples are immutable.

# Now create your own tuple with at least 3 items
my_tuple = ...

print(my_tuple)
print(...)  # Print the second item

# Expected output:
# (10, 20)
# (255, 128, 0)
# ('Alice', 25, 'Engineer')
# 10
# Engineer
# (your tuple)
# (your second item)
