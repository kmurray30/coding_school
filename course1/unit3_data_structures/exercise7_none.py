# None represents the absence of a value
# It's Python's way of saying "nothing" or "no value"

result = None
print(result)
print(type(result))

# None is useful as a placeholder or default value
user_input = None  # Will be filled in later
response = None    # No response yet

print(user_input)
print(response)

# You can check if something is None
if result is None:
    print("Result is None")

# None is different from 0, empty string, or False
print(None == 0)        # False
print(None == "")       # False
print(None == False)    # False

# Now create a variable set to None and print it
my_variable = ...
print(my_variable)

# Expected output:
# None
# <class 'NoneType'>
# None
# None
# Result is None
# False
# False
# False
# None
