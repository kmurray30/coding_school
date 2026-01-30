# Local variables can shadow global variables

name = "Global Name"

def my_function():
    name = "Local Name"
    print(name)

my_function()
print(name)

# Expected output:
# Local Name
# Global Name
