# Variables defined inside a function are local to that function

def my_function():
    local_variable = "I'm local"
    print(local_variable)

my_function()

# Uncomment below line to see the error - local_variable doesn't exist out here
# print(local_variable)

# Expected output (after uncommenting the line):
# <error message>
